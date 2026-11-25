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
    if p.get('front_plug_test'):
        return front_plug_preview(folder,p)
    if p.get('permanent_snap_test'):
        return permanent_snap_preview(folder,p)
    if p.get('drop_loop'):
        return loop_card_preview(folder,p)
    if p.get('finger_count',5)==4:
        return mechanism_preview(folder,p)
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


def mechanism_preview(folder,p):
    from shapely import affinity
    folder=Path(folder)
    fig=plt.figure(figsize=(14,10),facecolor='#faf9f6')
    gs=GridSpec(2,4,figure=fig,height_ratios=[1.3,1],hspace=.4,wspace=.25)
    captions=['Straight spring path\nControl snap',
              'Thick root, thinner tip\nDistributed bending',
              'Curved spring path\nDifferent compliance',
              'Snap first, add key\nBlocks hook squeezing']
    for i,t in enumerate(p['trials']):
        ax=fig.add_subplot(gs[0,i])
        shape=section(trimesh.load_mesh(folder/f"sample_{t['sample_number']}.stl"),2)
        draw_region(ax,shape,'#cce6ec')
        ax.text(0,-22,str(t['sample_number']),ha='center',va='center',weight='bold',fontsize=12)
        if t['technique']=='keeper':
            key=section(trimesh.load_mesh(folder/'keeper_key.stl'),2)
            draw_region(ax,affinity.translate(key,xoff=7.5),'#edc98f')
        ax.set_title(f"{t['sample_number']} · {['Straight','Tapered','S spring','Locking key'][i]}",weight='bold',loc='center',pad=10)
        ax.set_xlim(-11,11);ax.set_ylim(-32,11);ax.set_aspect('equal');ax.axis('off')
        ax.text(0,-35,captions[i],ha='center',va='top',fontsize=10,color='#3c454b')
    ax=fig.add_subplot(gs[1,:2]);ax.set_title('Four fingers, no fixed centre tongue',loc='left',weight='bold',pad=12)
    half=p['receiver_hole_width']/2
    for side in [-1,1]:
        ax.add_patch(Rectangle((-7 if side==-1 else half,0),7-half,6,facecolor='#c6a279',alpha=.85))
    draw_region(ax,section(trimesh.load_mesh(folder/'sample_50.stl'),2),'#cce6ec')
    ax.axhline(0,color='#8e6b44',ls='--',lw=.7);ax.axhline(6,color='#8e6b44',ls='--',lw=.7)
    ax.annotate('Two latch arms',xy=(2.6,3),xytext=(7.5,5),fontsize=10,arrowprops={'arrowstyle':'-','color':'#333'})
    ax.annotate('Thicker seating strips\n~1.75 mm each',xy=(4.5,-4),xytext=(7.5,-4),fontsize=10,arrowprops={'arrowstyle':'-','color':'#333'})
    ax.set_xlim(-8,23);ax.set_ylim(-15,10);ax.set_aspect('equal');ax.axis('off')
    ax=fig.add_subplot(gs[1,2:]);ax.set_title('One nominal fit for every mechanism',loc='left',weight='bold',pad=12)
    draw_region(ax,section(trimesh.load_mesh(folder/'receiver_6_0.stl'),.1),'#e4d4bc')
    for i,label in enumerate(p['receiver_labels']):ax.text((i-2)*24,9,label,ha='center',fontsize=10)
    ax.text(0,-10,'All five holes: 6.0 x 4.6 mm',ha='center',fontsize=10)
    ax.set_xlim(-68,68);ax.set_ylim(-30,30);ax.set_aspect('equal');ax.axis('off')
    ax.text(0,-35,'Printable receiver + matching 6 mm MDF DXF\nM3 beam/adapter included as a screw reference',ha='center',fontsize=10)
    fig.suptitle('V7 · Four-finger mechanism trials',x=.06,y=.975,ha='left',fontsize=23,weight='bold')
    fig.text(.06,.93,'Compare spring and locking techniques first. Clearance tuning comes afterwards.',fontsize=12,color='#49555d')
    fig.text(.06,.025,'Experimental PETG geometry. Force, fatigue, MDF wear and key retention need physical testing.',fontsize=10,color='#49555d')
    fig.subplots_adjust(top=.86,bottom=.12,left=.05,right=.96)
    fig.savefig(folder/'test_card_overview.png',dpi=150,facecolor=fig.get_facecolor());plt.close(fig)


def loop_card_preview(folder,p):
    folder=Path(folder)
    fig,axes=plt.subplots(1,5,figsize=(15,7),facecolor='#faf9f6')
    titles=['Straight','Tapered','S spring','Blocking key','Loop + drop key']
    for ax,t,title in zip(axes,p['trials'],titles):
        draw_region(ax,section(trimesh.load_mesh(folder/f"sample_{t['sample_number']}.stl"),2),'#cce6ec')
        ax.text(0,-22,str(t['sample_number']),ha='center',va='center',weight='bold',fontsize=12)
        ax.set_title(f"{t['sample_number']} · {title}",weight='bold',fontsize=11,pad=12)
        ax.set_xlim(-7,7);ax.set_ylim(-32,12);ax.set_aspect('equal');ax.axis('off')
    fig.suptitle('V7 · Mechanism card with rigid loop and vertical drop key',x=.05,y=.96,ha='left',weight='bold',fontsize=20)
    fig.text(.05,.89,'Same 6.0 x 4.6 mm receiver opening. 54 locks with a separate key dropped from ABOVE.',fontsize=12,color='#49555d')
    fig.text(.05,.08,'Full print: five numbered samples + two keys. Add-on print: sample 54 + its T key only.',fontsize=11)
    fig.text(.05,.03,'Experimental geometry. Previous samples, receiver compatibility and screw reference retained.',fontsize=10,color='#49555d')
    fig.subplots_adjust(top=.8,bottom=.18,wspace=.4)
    fig.savefig(folder/'test_card_overview.png',dpi=150,facecolor=fig.get_facecolor());plt.close(fig)
    # Side section at X=0, in the loop's service frame: +Y points outside,
    # +Z points down. The key is shown both raised and gravity-seated.
    from shapely import affinity
    mesh=trimesh.load_mesh(folder/'sample_54.stl')
    rotated=mesh.copy();rotated.apply_transform([[0,1,0,0],[0,0,-1,0],[-1,0,0,0],[0,0,0,1]])
    loop_section=section(rotated,0)
    d=p['drop_loop']
    fig,axes=plt.subplots(1,2,figsize=(12,6.5),facecolor='#faf9f6')
    for ax,raised in zip(axes,[True,False]):
        for z,height in [(.3,9),(-10,5.7)]:
            ax.add_patch(Rectangle((0,z),6,height,facecolor='#c6a279',alpha=.85))
        draw_region(ax,loop_section,'#cce6ec')
        shift=9 if raised else 0
        ax.add_patch(Rectangle((d['key_near'],-d['key_length']+shift),d['key_depth'],d['key_length']+d['key_head_height'],
                               facecolor='#edc98f',edgecolor='#29323a',lw=.8))
        ax.text(2.9,6.5,'6 mm\npanel',ha='center',fontsize=10)
        ax.text(-3,-4,'INSIDE',ha='center',fontsize=9)
        ax.text(10.9,-4,'OUTSIDE',ha='center',fontsize=9)
        ax.set_title('1 · Push loop through; drop key DOWN' if raised else '2 · Key crosses hole and blocks withdrawal',weight='bold',fontsize=11,pad=12)
        if raised:
            ax.annotate('',xy=(7.15,.7),xytext=(7.15,3),arrowprops={'arrowstyle':'->','lw':2,'color':'#6f4f24'})
        else:
            ax.annotate('',xy=(7.15,5),xytext=(7.15,2),
                        arrowprops={'arrowstyle':'->','lw':2,'color':'#6f4f24'})
            ax.text(9.8,5.2,'Lift key UP\nto release',fontsize=10)
        ax.set_xlim(-7,17);ax.set_ylim(-9,11.5);ax.set_aspect('equal');ax.axis('off')
    fig.suptitle('54 · Rigid loop + gravity-seated T key',x=.06,y=.96,ha='left',fontsize=21,weight='bold')
    fig.text(.06,.08,'Side section: the closed loop surrounds the key. No snap deflection is required.',fontsize=11)
    fig.text(.06,.03,'Print loop_key_addon.stl once. Key is loose/removable; accidental lift and loaded performance need testing.',fontsize=10,color='#49555d')
    fig.subplots_adjust(top=.83,bottom=.2,wspace=.15)
    fig.savefig(folder/'loop_key_preview.png',dpi=160,facecolor=fig.get_facecolor());plt.close(fig)


def permanent_snap_preview(folder,p):
    from shapely import affinity
    from action_validate_v7 import prescribed_flex
    folder=Path(folder)
    fig=plt.figure(figsize=(13,11),facecolor='#faf9f6')
    gs=GridSpec(2,6,figure=fig,height_ratios=[1,1.05],hspace=.25,wspace=.5)
    for i,t in enumerate(p['trials']):
        ax=fig.add_subplot(gs[0,2*i:2*i+2])
        draw_region(ax,section(trimesh.load_mesh(folder/f"sample_{t['sample_number']}.stl"),2),'#cce6ec')
        ax.text(0,-22,str(t['sample_number']),ha='center',va='center',weight='bold',fontsize=12)
        ax.set_title(f"{t['sample_number']} · {['Straight','Tapered','S spring'][i]}",weight='bold',pad=8)
        ax.set_xlim(-7,7);ax.set_ylim(-32,10);ax.set_aspect('equal');ax.axis('off')
    trial=p['trials'][0];mesh=trimesh.load_mesh(folder/f"sample_{trial['sample_number']}.stl")
    ax=fig.add_subplot(gs[1,:3]);ax.set_title('Recovered: larger one-way barbs',loc='left',weight='bold',pad=12)
    for side in [-1,1]:
        ax.add_patch(Rectangle((-8 if side<0 else 2.6,0),5.4,6,facecolor='#c6a279',alpha=.85))
    draw_region(ax,section(mesh,2),'#cce6ec')
    ax.annotate('1.4 mm hook reach\n1.2 mm overlap per side',xy=(3.6,6.6),xytext=(5.2,9),fontsize=9,
                arrowprops={'arrowstyle':'-','color':'#333'})
    ax.annotate('Back-raked shoulders\nNo designed release',xy=(3.2,6.17),xytext=(5.2,-2),fontsize=9,
                arrowprops={'arrowstyle':'-','color':'#333'})
    ax.set_xlim(-9,17);ax.set_ylim(-6,13);ax.set_aspect('equal');ax.axis('off')
    ax=fig.add_subplot(gs[1,3:]);ax.set_title('Insertion: arms close completely',loc='left',weight='bold',pad=12)
    for side in [-1,1]:
        ax.add_patch(Rectangle((-8 if side<0 else 2.6,0),5.4,6,facecolor='#c6a279',alpha=.85))
    # Slice the independently deformed halves, as in the contact validator.
    # A single touching-ring section can lose one arm during path stitching.
    from action_validate_v7_permanent_snap import region_clip
    from shapely.ops import unary_union
    left=region_clip(mesh,[-6,-31,-.1],[0,trial['tip_y']+.1,4.1])
    right=region_clip(mesh,[0,-31,-.1],[6,trial['tip_y']+.1,4.1])
    compressed=unary_union([section(prescribed_flex(part,p,trial),2) for part in [left,right]])
    draw_region(ax,affinity.translate(compressed,yoff=3-trial['shoulder_y']),'#d6cee9')
    ax.plot([0,0],[3.15,3.7],color='#8d4c26',lw=2)
    ax.annotate('Zero gap at hooks\n1.2 mm travel each',xy=(0,3.45),xytext=(5.2,8),fontsize=9,
                arrowprops={'arrowstyle':'->','color':'#8d4c26'})
    ax.annotate('Closed head: 5.2 mm\nHole: 5.2 x 4.2 mm',xy=(2.6,3.5),xytext=(5.2,-2),fontsize=9,
                arrowprops={'arrowstyle':'-','color':'#333'})
    ax.set_xlim(-9,17);ax.set_ylim(-6,13);ax.set_aspect('equal');ax.axis('off')
    fig.suptitle('V7 · Permanent full-squeeze snap trials',x=.06,y=.975,ha='left',fontsize=22,weight='bold')
    fig.text(.06,.93,'Larger hooks · smaller holes · intended one-time assembly',fontsize=13,color='#49555d')
    fig.text(.06,.065,'Print 3dpr.stl + NEW receiver_6_0.stl once each. All three holes are 5.2 x 4.2 mm.',fontsize=11)
    fig.text(.06,.025,'CAD verifies contact and capture. Physical destructive-removal tests must establish permanent retention.',fontsize=10,color='#49555d')
    fig.subplots_adjust(top=.86,bottom=.12,left=.04,right=.97)
    fig.savefig(folder/'test_card_overview.png',dpi=150,facecolor=fig.get_facecolor());plt.close(fig)


def front_plug_preview(folder,p):
    from action_validate_v7_front_plug import plug_to_clip,spread
    folder=Path(folder);s=p['front_plug']
    beam=trimesh.load_mesh(folder/'sample_70.stl')
    native=trimesh.load_mesh(folder/'front_plug.stl');plug=plug_to_clip(native,p)
    expanded=spread(beam,p,s['seated_spread'])
    fig,axes=plt.subplots(2,2,figsize=(13,10),facecolor='#faf9f6')
    ax=axes[0,0];ax.set_title('Front cap spreads and braces the arms',loc='left',weight='bold')
    for side in [-1,1]:ax.add_patch(Rectangle((-8 if side<0 else 2.6,0),5.4,6,facecolor='#c6a279',alpha=.85))
    draw_region(ax,section(expanded,2.5),'#cce6ec')
    draw_region(ax,section(plug,2.5),'#edc98f')
    ax.annotate('Spreads each arm 0.1 mm\nRibs click into pockets',xy=(1.4,4),xytext=(8,7.8),fontsize=9,
                arrowprops={'arrowstyle':'-','color':'#6f4f24'})
    ax.set_xlim(-9,23);ax.set_ylim(-10,12);ax.set_aspect('equal');ax.axis('off')
    ax=axes[0,1];ax.set_title('Taller inner shoulders support above the hole',loc='left',weight='bold')
    rotation=[[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,0,1]]
    sidebeam=beam.copy();sidebeam.apply_transform(rotation)
    sideplug=plug.copy();sideplug.apply_transform(rotation)
    ax.add_patch(Rectangle((0,-2),6,12,facecolor='#c6a279',alpha=.85))
    draw_region(ax,section(sidebeam,4.5),'#cce6ec')
    draw_region(ax,section(sideplug,4.5),'#edc98f')
    ax.add_patch(Rectangle((0,-.1),6,5.2,fill=False,ec='#6b553f',ls='--',lw=.8))
    ax.annotate('Upper bearing\n7 mm shoulder height',xy=(0,6.2),xytext=(-11,9),fontsize=9,
                arrowprops={'arrowstyle':'-','color':'#333'})
    ax.text(1,1,'6 mm\npanel',fontsize=10)
    ax.set_xlim(-13,14);ax.set_ylim(-2.5,11);ax.set_aspect('equal');ax.axis('off')
    ax=axes[1,0];ax.set_title('Outside view: cap covers the complete opening',loc='left',weight='bold')
    draw_region(ax,section(native,.1),'#edc98f')
    ax.add_patch(Rectangle((-2.6,-2.6),5.2,5.2,fill=False,ec='#6b553f',ls='--',lw=1))
    ax.text(0,-6,'11 x 8 mm cap; hole 5.2 x 5.2 mm\nDashed line shows the covered opening',ha='center',fontsize=10)
    ax.set_xlim(-9,9);ax.set_ylim(-8,6);ax.set_aspect('equal');ax.axis('off')
    ax=axes[1,1];ax.set_title('Plug print orientation: outside face DOWN',loc='left',weight='bold')
    printview=native.copy();printview.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]])
    draw_region(ax,section(printview,0),'#edc98f')
    ax.axhline(0,color='#49555d',lw=1)
    ax.text(0,-1.7,'Cap on bed, tapered stem UP',ha='center',fontsize=10)
    ax.set_xlim(-8,8);ax.set_ylim(-3,16);ax.set_aspect('equal');ax.axis('off')
    fig.suptitle('V7 sample 70 · Upper support + front expansion cover',x=.055,y=.97,ha='left',fontsize=21,weight='bold')
    fig.text(.055,.92,'Taller tongue and hole: 5.0 / 5.2 mm. Push snap in, then press the covering plug in from outside.',fontsize=11,color='#49555d')
    fig.text(.055,.025,'Fit and prescribed expansion are checked in CAD. Stiffness, retention and PETG creep need physical tests.',fontsize=10,color='#49555d')
    fig.subplots_adjust(top=.85,bottom=.09,hspace=.25,wspace=.2)
    fig.savefig(folder/'test_card_overview.png',dpi=150,facecolor=fig.get_facecolor());plt.close(fig)


if __name__=='__main__':
    import yaml
    import working_scad as drawing
    folder=next(Path('parts').glob('*ai_version_7_style*'))
    p=drawing.get_ai_version_7_parameters(**yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details'])
    main(folder,p)
