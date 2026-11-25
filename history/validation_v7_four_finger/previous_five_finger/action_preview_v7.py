"""Readable test-card overview drawn from exported meshes, not illustrative CAD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle
import trimesh
from shapely.geometry import box
from action_validate_ai_version_5 import section


def draw_region(ax,region,color,edge='#29323a',lw=.7):
    polygons=list(region.geoms) if hasattr(region,'geoms') else [region]
    for poly in polygons:
        if poly.is_empty or not hasattr(poly,'exterior'): continue
        x,y=poly.exterior.xy;ax.fill(x,y,color=color,ec=edge,lw=lw)
        for hole in poly.interiors:
            x,y=hole.xy;ax.fill(x,y,color='#faf9f6',ec=edge,lw=lw)


def main(folder,p):
    folder=Path(folder)
    fig=plt.figure(figsize=(13,10),facecolor='#faf9f6')
    gs=GridSpec(2,2,figure=fig,width_ratios=[.85,1.5],height_ratios=[1.35,1],hspace=.25,wspace=.22)
    ax=fig.add_subplot(gs[:,0]); ax.set_title('PRINT: nine numbered clips',loc='left',fontweight='bold',pad=14)
    mesh=trimesh.load_mesh(folder/'3dpr.stl')
    draw_region(ax,section(mesh,2),'#cce6ec')
    for i,t in enumerate(p['trials']):
        ax.text((i%3-1)*p['suite_pitch_x'],(i//3)*p['suite_pitch_y']-22,
                str(t['sample_number']),ha='center',va='center',weight='bold',fontsize=11)
    ax.set_aspect('equal');ax.set_xlim(-29,29);ax.set_ylim(-34,108)
    ax.axis('off')
    ax.text(0,-39,'Arms: 1.2 / 1.5 / 1.8 mm by row\nEnd play: 0.10 / 0.25 / 0.40 mm by column',
            ha='center',va='top',fontsize=10,color='#3c454b')
    detail=fig.add_subplot(gs[0,1]);detail.set_title('44: section through the seated joint',loc='left',weight='bold',pad=14)
    # This view is in the clip's print plane: panel thickness runs along Y.
    detail.add_patch(Rectangle((-8,0),4.2,6,facecolor='#c6a279',alpha=.85))
    detail.add_patch(Rectangle((3.8,0),4.2,6,facecolor='#c6a279',alpha=.85))
    shape=section(trimesh.load_mesh(folder/'sample_44.stl'),2)
    draw_region(detail,shape,'#cce6ec')
    detail.axhline(0,color='#8e6b44',ls='--',lw=.8)
    detail.axhline(6,color='#8e6b44',ls='--',lw=.8)
    detail.annotate('35° entry ramp\n~1.84 mm tip exposure',xy=(4.05,7.1),xytext=(7.8,8.8),
                    arrowprops={'arrowstyle':'-','color':'#333'},fontsize=10)
    detail.annotate('Square shoulder\ncatches outside face',xy=(4.05,6.25),xytext=(8.4,3.9),
                    arrowprops={'arrowstyle':'-','color':'#333'},fontsize=10)
    detail.annotate('Rigid seating strips',xy=(5.05,-.1),xytext=(8.4,-1.8),
                    arrowprops={'arrowstyle':'-','color':'#333'},fontsize=10)
    detail.annotate('Long spring arms\nrounded slot roots',xy=(2.8,-8),xytext=(8.4,-8),
                    arrowprops={'arrowstyle':'-','color':'#333'},fontsize=10)
    detail.text(-7.8,2.4,'6 mm\nMDF',fontsize=10)
    detail.text(-7.8,8,'OUTSIDE',fontsize=9,weight='bold')
    detail.text(-7.8,-3,'INSIDE',fontsize=9,weight='bold')
    detail.set_xlim(-9,24);detail.set_ylim(-14,11);detail.set_aspect('equal');detail.axis('off')
    card=fig.add_subplot(gs[1,1]);card.set_title('PRINT OR LASER CUT: common receiver card',loc='left',weight='bold',pad=14)
    shape=section(trimesh.load_mesh(folder/'receiver_6_0.stl'),.1)
    draw_region(card,shape,'#e4d4bc')
    for i,w in enumerate(p['receiver_hole_widths']):card.text((i-2)*24,9,f'{w:.1f}',ha='center',fontsize=10)
    card.text(0,-10,'All holes 4.6 mm high',ha='center',fontsize=10)
    card.set_xlim(-68,68);card.set_ylim(-25,25);card.set_aspect('equal');card.axis('off')
    card.text(0,-27,'Start with 44 in the centre hole.\nPrint 5.8 / 6.2 mm receivers to check thickness sensitivity.',
              ha='center',va='top',fontsize=10,color='#3c454b')
    fig.suptitle('V7  ·  Through-panel snap trials',x=.07,y=.98,ha='left',fontsize=23,weight='bold')
    fig.text(.07,.94,'Rectangular through-holes  •  PETG clips  •  6 mm MDF or printed receivers',fontsize=12,color='#49555d')
    fig.text(.07,.025,'Experimental geometry. Test insertion, play, release and repeated use before selecting a full rail.',fontsize=10,color='#49555d')
    fig.subplots_adjust(top=.88,bottom=.12,left=.06,right=.98)
    fig.savefig(folder/'test_card_overview.png',dpi=150,facecolor=fig.get_facecolor());plt.close(fig)


if __name__=='__main__':
    import yaml
    import working_scad as drawing
    folder=next(Path('parts').glob('*ai_version_7_style*'))
    p=drawing.get_ai_version_7_parameters(**yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details'])
    main(folder,p)
