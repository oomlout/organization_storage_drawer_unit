"""Plot the shared-runner support before/after from exported beam meshes."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import trimesh
import yaml
import working_scad as drawing
from action_validate_v7_side_runner import to_service
from action_validate_v7_permanent_snap import region_clip

ROOT=Path(__file__).resolve().parent


def main():
    out=ROOT/'validation_v7_balanced_runner'
    current=next((ROOT/'parts').glob('*unit_2_wide_2_tall'))
    preceding=out/'previous_current'/current.name
    fig,axes=plt.subplots(1,2,figsize=(12,4.8),sharey=True)
    summary=[]
    for ax,folder,title in zip(axes,[preceding,current],['Before: off-centre support','After: centred support']):
        inputs=yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details']
        p=drawing.get_ai_version_7_frame_parameters(**inputs);q=p['frame'];r=p['side_runner']
        mount=min(p['frame_mounts'],key=lambda m:abs(m.get('divider_x',m['x'])))
        divider=mount.get('divider_x',mount['x'])
        native=to_service(trimesh.load_mesh(folder/'snap_beam.stl'),p)
        strip=region_clip(native,[r['bed_x']-.1,-85,-10],[r['bed_x']+r['width']+.1,-80,30])
        axis=p['tongue_height']/2
        lo=mount['x']-strip.bounds[1,0]-divider
        hi=mount['x']-strip.bounds[0,0]-divider
        bottom=strip.bounds[0,2]-axis;roof=strip.bounds[1,2]-axis
        width=drawing.get_container_details(container=p['container'])['container_width']
        gap=(q['pitch_x']-width)/2;root=gap+q['inset_lip']
        bearing=[-gap-lo,hi-gap]
        ax.add_patch(Rectangle((lo,bottom),hi-lo,roof-bottom,facecolor='#24858A',edgecolor='#176168',linewidth=1.5))
        ax.plot([-root,-gap],[roof,roof],color='#CB8131',linewidth=5,solid_capstyle='butt')
        ax.plot([gap,root],[roof,roof],color='#CB8131',linewidth=5,solid_capstyle='butt')
        ax.axvline(0,color='#9DA8AE',linestyle='--',linewidth=1)
        for a,b,value in [(lo,-gap,bearing[0]),(gap,hi,bearing[1])]:
            ax.annotate('',xy=(a,9.1),xytext=(b,9.1),arrowprops=dict(arrowstyle='<->',color='#263940',shrinkA=0,shrinkB=0))
            ax.text((a+b)/2,9.45,f'{value:.2f} mm',ha='center',fontsize=12,color='#263940',weight='bold')
        hole_x=mount['x']-divider
        ax.scatter([hole_x],[0],s=65,color='#4A6D9B',zorder=5)
        ax.text(hole_x,-.8,'Receiver axis',ha='center',fontsize=10,color='#4A6D9B')
        if abs(hole_x)>.01:
            ax.annotate('',xy=(0,1.5),xytext=(hole_x,1.5),arrowprops=dict(arrowstyle='<->',color='#4A6D9B',shrinkA=0,shrinkB=0))
            ax.text(1.8,1.35,'hole shifted 1.5 mm',ha='left',fontsize=10,color='#4A6D9B')
        ax.set_title(title,loc='left',fontsize=14,pad=14,color='#263940')
        ax.set_xlim(-9,9);ax.set_ylim(-1.2,10.5)
        ax.set_xticks([-8,-4,0,4,8]);ax.set_yticks([0,5,8])
        ax.set_xlabel('Across the shared divider (mm)',fontsize=10,labelpad=9)
        ax.spines[['top','right']].set_visible(False)
        ax.spines[['bottom','left']].set_color('#D1D9DC')
        ax.tick_params(colors='#52646B');ax.grid(axis='y',alpha=.15,zorder=0)
        summary.append(dict(edges_mm=[float(lo),float(hi)],bearing_mm=[float(v) for v in bearing],roof_mm=float(roof)))
    axes[0].set_ylabel('Height above receiver axis (mm)',fontsize=10)
    fig.suptitle('2 × 2 unit — shared middle runner',fontsize=18,weight='bold',color='#263940',y=.98)
    fig.text(.5,.89,'The runner stays flat and 3 mm thick; the shifted receiver centres it between the drawers.',ha='center',fontsize=11,color='#52646B')
    fig.text(.5,.045,'Teal: exported runner cross-section     Orange: nominal drawer lip extents     Dashed line: divider centre',ha='center',fontsize=10,color='#52646B')
    fig.subplots_adjust(left=.07,right=.98,bottom=.2,top=.77,wspace=.15)
    fig.savefig(out/'shared_runner_comparison.png',dpi=160,facecolor='white')
    fig.savefig(out/'shared_runner_comparison.svg',facecolor='white')
    plt.close(fig)
    print(summary)


if __name__=='__main__':main()
