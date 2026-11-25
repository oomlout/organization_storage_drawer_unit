"""Generate and test the M3 x 25 joining hardware for the two small V7 frames."""
import argparse
from pathlib import Path
import shutil
import subprocess
import zipfile

import numpy as np
import oobb
import trimesh
from shapely.geometry import Point

import working_scad as drawing
from action_validate_ai_version_5 import section

ROOT=Path(__file__).resolve().parent


def validate_stops(folder,p):
    """Line probes on every catch of both printed faces and both laser thicknesses."""
    from shapely.geometry import LineString
    q=p['frame'];results=[]
    for name,web in [('front',6),('back',6),('front_laser',6),('front_3mm_test',3)]:
        mesh=trimesh.load_mesh(folder/(name+'.stl'))
        sections=[section(mesh,z) for z in [.1,web/2,web-.1]]
        inside=section(mesh,web+.1) if name in ('front','back') else None
        for f in q['floor_support_features']:
            x,y,_=f['pos'];width,root,depth=f['envelope']
            x+=width/2
            probe=LineString([(x,y+.01),(x,y+root+.1)])
            lengths=[profile.intersection(probe).length for profile in sections]
            if inside is None:
                assert max(lengths)-min(lengths)<.001 and abs(lengths[0]-root+.01)<.01
            else:
                assert lengths[0]+.5<lengths[1]<lengths[2]-.5,('Ramp direction',name,f,lengths)
                assert abs(lengths[2]-root)<.25 and inside.intersection(probe).length<=q['floor_support_thickness']+.01
            results.append(dict(face=name,kind=f['kind'],column=f['column'],row=f['supported_row'],profile_mm=lengths))
    baseline=ROOT/'validation_v7_joiner_25mm'/'previous_current'/'parts'/Path(folder).name
    if baseline.is_dir():
        windows=[]
        for f in q['floor_support_features']:
            box=trimesh.creation.box(extents=np.array(f['envelope'])+.08)
            box.apply_translation(np.array(f['pos'])+np.array(f['envelope'])/2)
            windows.append(box)
        envelope=trimesh.util.concatenate(windows)
        for name in ['front','back']:
            old=trimesh.load_mesh(baseline/(name+'.stl')).difference(envelope,engine='manifold')
            new=trimesh.load_mesh(folder/(name+'.stl')).difference(envelope,engine='manifold')
            assert old.difference(new,engine='manifold').volume+new.difference(old,engine='manifold').volume<.005
    return results


def validate_samples(folder,p):
    """Compare each loose trial part with its crop from the actual production mesh."""
    from action_validate_v7_permanent_snap import region_clip
    q=p['frame']
    sample=trimesh.load_mesh(folder/'joiner_fit_samples.stl')
    pieces=list(sample.split(only_watertight=False))
    assert len(pieces)==7 and all(body.is_volume and abs(body.bounds[0,2])<.001 for body in pieces)
    comparisons=[]
    def compare(mesh,shift):
        mesh.apply_translation(shift)
        nearest=min(range(len(pieces)),key=lambda i:np.linalg.norm(pieces[i].centroid-mesh.centroid))
        actual=pieces.pop(nearest)
        diff=actual.difference(mesh,engine='manifold').volume+mesh.difference(actual,engine='manifold').volume
        assert abs(diff)<.015,('Fit coupon differs from production part',shift,diff)
        comparisons.append(float(diff))
    face=trimesh.load_mesh(folder/'front.stl')
    for hand in [-1,1]:
        x=hand*(q['width_total']/2-12);y=-q['height_total']/2+12
        compare(region_clip(face,[x-12,y-12,-1],[x+12,y+12,30]),[-hand*15-x,-y,0])
    for name,x in [('snap_beam',-18),('screw_beam',12)]:
        beam=trimesh.load_mesh(folder/(name+'.stl'))
        compare(region_clip(beam,[-30,-26,-1],[30,12,30]),[x,45,0])
    compare(trimesh.load_mesh(folder/'front_plug.stl'),[-38,0,0])
    compare(trimesh.load_mesh(folder/'screw_adapter.stl'),[-38,15,0])
    x,y,_=next(f['pos'] for f in q['floor_support_features'] if f['kind']=='floor')
    compare(region_clip(face,[x-2,y-2,-1],[x+17,y+12,30]),[32-x,-y,0])
    return comparisons


def validate(folder,p):
    mesh=trimesh.load_mesh(folder/'joiners.stl')
    assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0
    bodies=sorted(mesh.split(),key=lambda body:body.centroid[0])
    j=p['optional_joiners'];cap=p['front_plug']
    assert len(bodies)==2 and j['screw_length']==25
    report=dict(variant=p['variant'],pieces=[])
    # Check the visible outline against the actual latch and the OOBB cutter
    # at the mouth, along the cone and below the seat.
    from shapely.geometry import Polygon,box
    from shapely.affinity import translate
    latch=trimesh.load_mesh(folder/'front_plug_square.stl')
    outline=section(latch,.1)
    cap_corner=box(*outline.bounds).difference(Polygon(outline.exterior))
    cap_corner=sorted(cap_corner.geoms,key=lambda g:g.bounds[:2])[0]
    r=oobb.gv('hole_radius_m3','3dpr');head=oobb.gv('screw_countersunk_radius_m3','3dpr')
    cone=oobb.gv('screw_countersunk_depth_m3','3dpr')
    for body,part in zip(bodies,p['joiners']):
        assert np.allclose(body.extents,part['size'],atol=.01)
        assert abs(body.bounds[0,2])<.001 and abs(body.extents[2]-(cap['outer_y']-p['panel_thickness']))<.001
        front=section(body,.1)
        # The corner opposite the clasp cutouts retains the actual latch
        # arc. Compare the outline locally, excluding those deliberate cutouts.
        arc=translate(cap_corner,front.bounds[0]-outline.bounds[0],front.bounds[1]-outline.bounds[1])
        zone=box(front.bounds[0],front.bounds[1],front.bounds[0]+.75,front.bounds[1]+.75)
        assert zone.difference(front).symmetric_difference(arc).area<.004
        assert abs(box(*front.bounds).difference(Polygon(front.exterior)).area-4*cap_corner.area)<.015
        for z in [.1,j['countersink_setback']+cone/2,j['countersink_setback']+cone+.2]:
            cross=section(body,z)
            radius=max(r,head-(head-r)*max(0,z-j['countersink_setback'])/cone)
            for x,y in part['holes']:
                pt=Point(x+part['print_center'][0],y)
                assert not cross.contains(pt) and abs(cross.distance(pt)-radius)<.08,(part['name'],z)
        report['pieces'].append(dict(name=part['name'],size_mm=part['size'],corner_radius_mm=cap['cover_radius']))
    report['fit_sample_difference_mm3']=validate_samples(folder,p)
    report['printable_fit_samples']=len(report['fit_sample_difference_mm3'])
    report['face_stops']=validate_stops(folder,p)
    from action_validate_v7_joiner_fit import validate_hardware_and_group
    report['hardware_and_group']=validate_hardware_and_group(folder,p,bodies)
    report['all_checks_passed']=True
    return report


def render_stop_section(folder,p):
    """Draw the two manufacturing mesh sections at the same real drawer stop."""
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.patches import Polygon as Patch
    from shapely.geometry import Polygon,box
    f=next(f for f in p['frame']['floor_support_features'] if f['kind']=='floor')
    x,y,_=f['pos'];x+=f['envelope'][0]/2
    fig=Figure(figsize=(9,3.4),facecolor='white',layout='constrained')
    FigureCanvasAgg(fig)
    for ax,(name,title) in zip(fig.subplots(1,2),[('front','Printed face'),('front_laser','Laser-cut face')]):
        mesh=trimesh.load_mesh(folder/(name+'.stl'))
        path=mesh.section(plane_normal=[1,0,0],plane_origin=[x,0,0])
        for loop in path.discrete:
            shape=Polygon(np.column_stack((loop[:,2],loop[:,1]-y))).intersection(box(-1,-2,20,11))
            if shape.is_empty or shape.area<.01:continue
            shapes=shape.geoms if shape.geom_type=='MultiPolygon' else [shape]
            for poly in shapes:
                ax.add_patch(Patch(np.array(poly.exterior.coords),facecolor='#a5cfd3',edgecolor='#224a50',lw=1.4))
        ax.axvline(6,color='#707880',lw=.8,ls='--')
        ax.set(xlim=(-1,19),ylim=(11,-2),aspect='equal',xticks=[0,6,12,18],yticks=[],
               xlabel='Depth from outside face (mm)',title=title)
        ax.spines[['left','top','right']].set_visible(False)
    fig.savefig(folder/'face_stop_profile.png',dpi=150,bbox_inches='tight',pad_inches=.16)

def package(folder,p):
    """Keep a named joiners folder and a portable accessory ZIP with each unit."""
    folder=Path(folder);dest=folder/'joiners';dest.mkdir(exist_ok=True)
    for suffix in ['.scad','.stl','.png']:
        shutil.copy2(folder/('joiners'+suffix),dest/('joiners'+suffix))
    for suffix in ['.scad','.stl']:
        shutil.copy2(folder/('joiner_backers'+suffix),dest/('joiner_backers'+suffix))
    for name in ['joiners_in_use.png','joiners_detail.png','joiners_backing_detail.png','joiners_section.png','face_stop_profile.png']:
        shutil.copy2(folder/name,dest/name)
    for suffix in ['.scad','.stl']:
        shutil.copy2(folder/('joiners_clasp_clearance'+suffix),dest/('joiners_clasp_clearance'+suffix))
        shutil.copy2(folder/('joiner_fit_samples'+suffix),dest/('joiner_fit_samples'+suffix))
    text="""OPTIONAL JOINERS | M3 x 25 countersunk screws and standard M3 hex nuts
Print joiners.stl and joiner_backers.stl once per set. Each file includes a two-hole strip and a four-hole plate. The holes are on a 10 mm pitch for touching 6 mm faces.
Print all parts as supplied: outside faces and nut-pocket mouths down. Clear the bores and ensure the nuts drop into the rear pockets by hand.
Use joiners.stl for the supplied unit layout, which has screw adapters at the upper corner receivers. If you fit a push-in clasp in an upper corner receiver instead, print joiners_clasp_clearance.stl for that seam. Both front styles take the same backer.
Use the supplied updated beams. The nut relief is at a different depth from the 35 mm version. The existing face holes, push-in locks and screw adapters fit.
Fit the inside backers while there is access to the seams. Before closing the frame, load nuts into the backing piece from its open rear face. Hold them in place. Approach the inside face with the backer 8 mm above its installed position; slide down into the rail relief. Hold the backer against the inside face while starting screws from the outside.
Front and rear: install the outside plate with its flange recesses against the panel. At the rear, turn the outside plate over about Y and turn the inside backer 180 degrees about Z relative to its print orientation. Turn vertical strips +90 degrees on the right edge and -90 on the left as seen in front CAD coordinates. Match the reliefs to the runners before tightening.
Use two screws and nuts per strip or four per corner. Seat gently and confirm the drawer and clasps move freely. Use an open frame or remove drawers for access.
FIT SAMPLE: print joiner_fit_samples.stl, joiners_clasp_clearance.stl and joiner_backers.stl. The sample contains two separate top face corners, one shortened screw beam, one shortened snap beam, a screw adapter, a friction cap and a printed stop section. Arrange the straight outer edges of the two face corners together with the corner bores 10 mm apart. Mount the screw end and adapter on one corner and the snap end and push-in cap on the other. Use the two-hole joiner and backer across the seam. Use the normal M3 x 20 beam fixing for the screw beam, and two M3 x 25 fixings for the strip. Check seating, nut capture, hand insertion and latch operation before printing a full batch.
The pictures show assembled units. Only the test print can confirm tolerances on your printer.
"""
    (dest/'printing.txt').write_text(text,encoding='utf-8')
    upgrade=dest/'required_beam_update';upgrade.mkdir(exist_ok=True)
    beam_batches=[name for name,batch in p['print_batches'].items() if batch['component'] in ['snap_beam','screw_beam']]
    for name in beam_batches:
        for suffix in ['.scad','.stl']:shutil.copy2(folder/(name+suffix),upgrade/(name+suffix))
    (upgrade/'printing.txt').write_text('\n'.join([
        'Use these beams for the M3 x 25 joiners, including when upgrading from the M3 x 35 version.',
        'Print each listed batch ONCE; replace the existing beams, retaining faces, caps, adapters and beam hardware.',
        *[f"{name}.stl: {p['print_batches'][name]['count']} x {p['print_batches'][name]['component']}" for name in beam_batches],
        'Full print_files.zip already includes these beam batches at top level. Do NOT print those and this duplicate upgrade set.',
        'Original beam-end clips, locating guides and nut bosses are unchanged. New clearance is confined to the runners.'])+'\n',encoding='utf-8')
    names=[f'joiners/{name}' for name in ['joiners.scad','joiners.stl','joiners.png',
        'joiners_clasp_clearance.scad','joiners_clasp_clearance.stl','joiner_fit_samples.scad','joiner_fit_samples.stl','joiner_backers.scad','joiner_backers.stl','joiners_in_use.png','joiners_detail.png','joiners_backing_detail.png','joiners_section.png','face_stop_profile.png','printing.txt']]
    names += ['joiners/'+path.relative_to(dest).as_posix() for path in upgrade.iterdir()]
    with zipfile.ZipFile(folder/'joiners.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for name in names:archive.write(folder/name,name)
    with zipfile.ZipFile(folder/'joiners.zip') as archive:
        assert archive.testzip() is None
        for name in names:
            assert archive.read(name)==(folder/name).read_bytes(),name
    return names


def export_accessory(folder,p,logs):
    logs.mkdir(parents=True,exist_ok=True)
    render_stop_section(folder,p)
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    for name in ['joiners','joiners_clasp_clearance','joiner_backers','joiner_fit_samples','joiner_screw_reference','joiner_nut_reference']:
        result=subprocess.run([exe,'--backend=Manifold','--hardwarnings','--export-format=binstl',
            '-o',str(folder/(name+'.stl')),str(folder/(name+'.scad'))],
            capture_output=True,text=True,timeout=180)
        (logs/(name+'_export.log')).write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()
    for name,camera in [('joiners','0,0,0,35,0,25,100'),
                        ('joiners_in_use',f"{p['frame']['width_total']*3.2},-{p['frame']['width_total']*5.7},450,0,100,0"),
                        ('joiners_detail','65,-130,55,0,12,0'),
                        ('joiners_backing_detail','55,105,45,0,14,0'),
                        ('joiners_section','17,40,98,0,11,-5')]:
        framing=['--viewall','--autocenter'] if name=='joiners' else []
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1400,1000','--projection=o',
            *framing,'--camera='+camera,'--colorscheme=Tomorrow',
            '-o',str(folder/(name+'.png')),str(folder/('joiners_detail.scad' if name=='joiners_backing_detail' else name+'.scad'))],
            capture_output=True,text=True,timeout=180)
        (logs/(name+'_preview.log')).write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()


def main(variant=None):
    # This revision also changes faces, assembled views, beams and their kits.
    from action_generate_current_v7 import main as generate
    for selected in ([variant] if variant else ['unit_1_wide_2_tall','unit_2_wide_2_tall']):
        generate(variant=selected)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--variant',choices=['unit_1_wide_2_tall','unit_2_wide_2_tall'])
    main(**vars(parser.parse_args()))
