"""Section of the installed four-hole joiner, from production and hardware STLs."""
from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Patch, PathPatch
from matplotlib.path import Path as PlotPath
import numpy as np
from shapely.geometry import box
from shapely.geometry.polygon import orient
import trimesh
import yaml

from action_validate_ai_version_5 import section
from action_validate_v7_joiner_fit import moved
import working_scad as drawing


def render(folder,output):
    p=drawing.get_ai_version_7_frame_parameters(**yaml.safe_load((folder/'working.yaml').read_text())['oobb_details'])
    part=p['joiners'][0];j=p['optional_joiners'];depth=part['size'][2]
    end=p['panel_thickness']+j['backer_depth'];hole_x,hole_y=part['holes'][-1]
    head=-depth+j['screw_reference_recess'];seat=end-j['nut_recess']
    fig=Figure(figsize=(8.6,3.7));FigureCanvasAgg(fig)
    ax=fig.subplots();fig.subplots_adjust(left=.04,right=.98,top=.86,bottom=.17)
    colors=['#bbced0','#e48b3e','#d1ad69','#55677a','#9daabb']
    bounds=box(-5,-15,25,11)
    def draw(mesh,color):
        mesh.apply_transform([[0,0,1,0],[0,-1,0,0],[1,0,0,0],[0,0,0,1]])
        areas=section(mesh,hole_x+.002).intersection(bounds)
        for poly in (areas.geoms if areas.geom_type=='MultiPolygon' else [areas]):
            if poly.is_empty or poly.area<.005:continue
            poly=orient(poly,sign=1)
            rings=[np.asarray(r.coords) for r in (poly.exterior,*poly.interiors)]
            path=PlotPath.make_compound_path(*[PlotPath(r,closed=True) for r in rings])
            ax.add_patch(PathPatch(path,facecolor=color,edgecolor='#34434a',lw=.65))
    unit=trimesh.load_mesh(folder/'assembled.stl')
    for xy in drawing.v7_joiner_layout(p)['units']:
        draw(moved(unit,xy),colors[0])
    for name,z,flip,color in [('joiners',-depth,False,colors[1]),('joiner_backers',end,True,colors[2])]:
        body=min(trimesh.load_mesh(folder/(name+'.stl')).split(),key=lambda b:b.centroid[0])
        body.apply_translation(-np.array(part['print_center']))
        draw(moved(body,[0,0,z],rear=flip),color)
    for x,y in part['holes']:
        for name,z,color in [('screw',head,colors[3]),('nut',seat,colors[4])]:
            draw(moved(trimesh.load_mesh(folder/f'joiner_{name}_reference.stl'),[x,y,z]),color)
    ax.set(xlim=(-7,28),ylim=(-16,14),aspect='equal');ax.axis('off')
    ax.annotate('',xy=(head+25,12),xytext=(head,12),arrowprops=dict(arrowstyle='<->',color='#34434a'))
    ax.text(head+12.5,12.6,'25 mm countersunk screw',ha='center',fontsize=10)
    labels=['Face and rail','Front bracket','Backer','Screw','M3 nut']
    fig.legend([Patch(facecolor=c) for c in colors],labels,loc='lower center',ncol=5,frameon=False,fontsize=9)
    fig.savefig(output,dpi=170,bbox_inches='tight',pad_inches=.12)


if __name__=='__main__':
    root=Path(__file__).resolve().parent
    folder=next((root/'parts').glob('*_container_1_column_2_row_ai_version_7_style_unit_1_wide_2_tall'))
    render(folder,root/'validation_v7_joiner_25mm'/'installed_section.png')
