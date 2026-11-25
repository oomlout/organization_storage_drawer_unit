"""Section of the installed four-hole joiner, from production and hardware STLs."""

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Patch, PathPatch
from matplotlib.path import Path as PlotPath
import numpy as np
from shapely.geometry import LineString, box
from shapely.geometry.polygon import orient
import trimesh

from v8_validation import external_part, section, moved
import working_scad as drawing


def render(folder, frame_folder, p, output):
    part=p['joiners'][0];j=p['corner_fixing'];depth=part['size'][2]
    end=p['panel_thickness']+j['backer_depth'];hole_x,hole_y=part['holes'][-1]
    head=-depth+j['screw_reference_recess'];seat=end-j['nut_recess']
    fig=Figure(figsize=(8.6,3.7));FigureCanvasAgg(fig)
    ax=fig.subplots();fig.subplots_adjust(left=.04,right=.98,top=.86,bottom=.17)
    colors=['#bbced0','#e48b3e','#d1ad69','#55677a','#9daabb']
    bounds=box(-depth-1,-15,25,11)
    def draw(mesh,color):
        mesh.apply_transform([[0,0,1,0],[0,-1,0,0],[1,0,0,0],[0,0,0,1]])
        areas=section(mesh,hole_x+.002).intersection(bounds)
        for poly in (areas.geoms if areas.geom_type=='MultiPolygon' else [areas]):
            if poly.is_empty or poly.area<.005:continue
            poly=orient(poly,sign=1)
            rings=[np.asarray(r.coords) for r in (poly.exterior,*poly.interiors)]
            path=PlotPath.make_compound_path(*[PlotPath(r,closed=True) for r in rings])
            ax.add_patch(PathPatch(path,facecolor=color,edgecolor='#34434a',lw=.65))
    unit=trimesh.load_mesh(frame_folder/'assembled.stl')
    for xy in drawing.v8_joiner_layout(p)['units']:
        draw(moved(unit,xy),colors[0])
    for name,z,flip,color in [('joiners',-depth,False,colors[1]),('joiner_backers',end,True,colors[2])]:
        body=min(trimesh.load_mesh(folder/(name+'.stl')).split(),key=lambda b:b.centroid[0])
        body.apply_translation(-np.array(part['print_center']))
        draw(moved(body,[0,0,z],rear=flip),color)
    for x,y in part['holes']:
        for name,z,color in [('screw',head,colors[3]),('nut',seat,colors[4])]:
            draw(moved(trimesh.load_mesh(folder/f'joiner_{name}_reference.stl'),[x,y,z]),color)
    ax.set(xlim=(-depth-2,28),ylim=(-16,14),aspect='equal');ax.axis('off')
    ax.annotate('',xy=(head+25,12),xytext=(head,12),arrowprops=dict(arrowstyle='<->',color='#34434a'))
    ax.text(head+12.5,12.6,'25 mm countersunk screw',ha='center',fontsize=10)
    labels=['Face and rail','Front bracket','Backer','Screw','M3 nut']
    fig.legend([Patch(facecolor=c) for c in colors],labels,loc='lower center',ncol=5,frameon=False,fontsize=9)
    fig.savefig(output,dpi=170,bbox_inches='tight',pad_inches=.12)

def render_cap_section(folder, frame_folder, p, output):
    """Cut the real installed bracket and cap where their footprints overlap."""
    part = p['joiners'][0]
    bracket = min(trimesh.load_mesh(folder/'joiners.stl').split(), key=lambda body: body.centroid[0])
    bracket = moved(bracket, -np.array(part['print_center']) + [0, 0, -part['size'][2]])
    roof = section(bracket, bracket.bounds[0, 2] + .1)
    cap = trimesh.load_mesh(frame_folder/'front_plug_square.stl')
    candidates = []
    for xy in drawing.v8_joiner_layout(p)['units']:
        for mount in p['frame_mounts']:
            fitted = moved(external_part(cap, p, mount, 'snap_beam', False), xy)
            shared = section(fitted, fitted.bounds[0, 2] + .1).intersection(roof)
            if shared.area > .1:
                candidates.append((shared.area, shared, fitted, mount, xy))
    _, shared, fitted, mount, xy = max(candidates, key=lambda row: row[0])
    # Cut beside the screw bore so the continuous roof is visible in section.
    left, bottom, right, top = shared.bounds
    x = right - .65 if right > -left else left + .65
    y = shared.intersection(LineString([(x,bottom-1), (x,top+1)])).centroid.y
    face = moved(trimesh.load_mesh(frame_folder/'front.stl'), xy)
    beam = trimesh.load_mesh(frame_folder/'snap_beam.stl')
    beam.apply_transform(drawing.v8_beam_to_frame(p, mount, 'snap_beam'))
    beam = moved(beam, xy)
    def cut(mesh):
        mesh.apply_transform([[0,1,0,0],[0,0,-1,0],[-1,0,0,0],[0,0,0,1]])
        return section(mesh, -x)
    face_slice, beam_slice, cap_slice, front_slice = [cut(m) for m in (face, beam, fitted, bracket)]
    cap_top = cap_slice.bounds[3]
    probe = LineString([(y, cap_top), (y, part['size'][2]+1)])
    roof_bottom = front_slice.intersection(probe).bounds[1]
    gap = roof_bottom - cap_top
    assert abs(gap - p['corner_fixing']['cap_axial_clearance']) < .025
    window = box(y-10, -6.2, y+13, part['size'][2]+2)
    fig = Figure(figsize=(7.2, 4.6)); FigureCanvasAgg(fig)
    ax = fig.subplots()
    for shape, color, label in [(face_slice,'#bbced0','Faceplate'),(beam_slice,'#478b83','Snap beam'),
                                (cap_slice,'#486483','Clip cap'),(front_slice,'#e48b3e','Joiner front')]:
        clipped = shape.intersection(window)
        for poly in getattr(clipped, 'geoms', [clipped]):
            if poly.geom_type != 'Polygon' or poly.area < .005:
                continue
            poly = orient(poly, sign=1)
            rings = [PlotPath(np.asarray(r.coords), closed=True) for r in (poly.exterior,*poly.interiors)]
            ax.add_patch(PathPatch(PlotPath.make_compound_path(*rings),facecolor=color,edgecolor='#34434a',lw=.8))
    ax.annotate(f'{gap:.1f} mm above the cap', xy=(y, (roof_bottom+cap_top)/2),
                xytext=(y+3,part['size'][2]+.7), fontsize=11,
                arrowprops=dict(arrowstyle='->',lw=1.1,color='#253d49'))
    ax.set(xlim=(window.bounds[0],window.bounds[2]),ylim=(window.bounds[1],window.bounds[3]),aspect='equal')
    ax.set_axis_off()
    ax.set_title('Standard joiner over a fitted clip cap',fontsize=14)
    labels = [('Faceplate','#bbced0'),('Snap beam','#478b83'),('Clip cap','#486483'),('Joiner front','#e48b3e')]
    fig.legend([Patch(facecolor=c) for _,c in labels],[k for k,_ in labels],loc='lower center',ncol=4,frameon=False)
    fig.subplots_adjust(bottom=.14)
    fig.savefig(output,dpi=160,bbox_inches='tight',pad_inches=.16)
