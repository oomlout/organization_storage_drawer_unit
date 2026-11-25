"""Taller upper bearing shoulders and a front cap that spreads/locks the arms."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import zipfile
import numpy as np
import trimesh
import yaml
from shapely.geometry import box
import working
import working_scad as drawing
from working_scad_v7 import views
from action_validate_v7 import export,check_dxf,prescribed_flex
from action_validate_v7_permanent_snap import region_clip
from action_validate_ai_version_5 import moved,overlap,section,check_previous_versions
from action_lock_version_6 import check as check_release

ROOT=Path(__file__).resolve().parent


def previous_check():
    previous=json.loads((ROOT/'validation_v7_front_plug/previous_v7_baseline.json').read_text(encoding='utf-8'))
    for name,expected in previous.items():
        folder=ROOT/'parts'/name
        assert yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details']==expected['inputs'],name
        for filename,digest in expected['files'].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    print('Previous V7 unchanged:',len(previous),'records /',sum(len(p['files']) for p in previous.values()),'files',flush=True)


def to_panel(mesh,p):
    result=mesh.copy()
    # Positive clip Z is service UP; the cabinet's CAD negative Y is UP.
    result.apply_transform([[-1,0,0,0],[0,0,-1,p['tongue_height']/2],[0,-1,0,p['panel_thickness']],[0,0,0,1]])
    return result


def plug_to_clip(mesh,p):
    result=mesh.copy();s=p['front_plug']
    result.apply_transform([[1,0,0,0],[0,0,-1,s['outer_y']],[0,1,0,p['tongue_height']/2],[0,0,0,1]])
    return result


def spread(mesh,p,amount):
    vertices,faces=trimesh.remesh.subdivide_to_size(mesh.vertices,mesh.faces,max_edge=.6)
    v=vertices.copy();trial=p['trials'][0]
    u=np.clip((v[:,1]-trial['effective_root_y'])/(-trial['effective_root_y']),0,1)
    motion=u*u*(3-2*u)
    active=(np.abs(v[:,0])>.05)&(np.abs(v[:,0])<p['outer']+p['hook_projection']+.01)
    active &= (v[:,1]>0.00001)|(np.abs(v[:,0])<p['outer']+.02)
    v[active,0]+=np.sign(v[active,0])*amount*motion[active]
    return trimesh.Trimesh(vertices=v,faces=faces,process=True)


def full_contact_check(beam,receiver,p):
    trial=p['trials'][0];end=trial['tip_y']+.1;top=p['upper_support_height']+.1
    halves=[region_clip(beam,[-6,-31,-.1],[0,end,top]),region_clip(beam,[0,-31,-.1],[6,end,top])]
    left,right=[prescribed_flex(part,p,trial) for part in halves]
    assert overlap(left,right)<.002,'Closed arms interpenetrate'
    a=left.vertices[left.vertices[:,1]>trial['shoulder_y']+.05,0]
    b=right.vertices[right.vertices[:,1]>trial['shoulder_y']+.05,0]
    gap=float(b.min()-a.max());assert abs(gap)<.001,'Arm tips do not meet'
    partial=prescribed_flex(beam,dict(p,deflection=.95*p['deflection']),trial)
    interference=overlap(receiver,to_panel(moved(partial,[0,-(trial['shoulder_y']-3),0]),p))
    assert interference>.01,'Partial closure passes the hole'
    return dict(actual_closed_tip_gap_mm=gap,closed_arm_interference_mm3=overlap(left,right),
                partial_95_percent_closure_collision_mm3=interference)


def main(skip_generation=False):
    out=ROOT/'validation_v7_front_plug';out.mkdir(exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
            generate_stl=False,scad_filter='ai_version_7',scad_navigation=False)
    previous_check();check_release();check_previous_versions(ROOT)
    folder=next((ROOT/'parts').glob('*ai_version_7_style_front_spreader_plug_test'))
    p=drawing.get_ai_version_7_parameters(**yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details'])
    s=p['front_plug'];trial=p['trials'][0]
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    report=dict(version=7,sample=70,meshes=[],checks={});meshes={}
    for name in ['3dpr',*views(p)]:
        print('Exporting',name,flush=True);export(exe,folder,out,name)
        mesh=trimesh.load_mesh(folder/f'{name}.stl');meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,name
        parts=list(mesh.split(only_watertight=False));expected=2 if name=='3dpr' else 1
        assert len(parts)==expected,(name,len(parts))
        assert all(abs(part.bounds[0,2])<.001 for part in parts),(name,'bed contact')
        assert max(mesh.extents[:2])+4<180
        report['meshes'].append(dict(view=name,bodies=expected,closed=True,extents_mm=mesh.extents.tolist(),volume_mm3=float(mesh.volume)))
    beam=meshes['sample_70'];receiver=meshes['receiver_6_0'];native_plug=meshes['front_plug']
    assert abs(meshes['3dpr'].volume-beam.volume-native_plug.volume)<.03
    assert abs(beam.extents[2]-7)<.001
    profile=section(receiver,.1)
    assert profile.intersection(box(-2.599,-2.599,2.599,2.599)).area<1e-6
    assert profile.intersection(box(-1,2.61,1,2.7)).area>.17
    assert overlap(receiver,to_panel(beam,p))<.005
    # Probe the actual material ABOVE the hole: taller outside columns bear
    # against the inside panel, while the tongue also has top/bottom location.
    upper=region_clip(beam,[-6,-.5,p['tongue_height']+.2],[6,.1,p['upper_support_height']+.1])
    assert upper.volume>1
    assert overlap(receiver,to_panel(moved(upper,[0,.1,0]),p))>.05,'No upper bearing contact'
    for direction in [-1,1]:
        assert overlap(receiver,to_panel(moved(beam,[0,0,direction*.08]),p))<.005
        assert overlap(receiver,to_panel(moved(beam,[0,0,direction*.15]),p))>.01
    closed=prescribed_flex(beam,p,trial)
    contact=full_contact_check(beam,receiver,p)
    collisions=[overlap(receiver,to_panel(moved(closed,[0,-d,0]),p)) for d in np.linspace(0,trial['tip_y']+1,29)]
    assert max(collisions)<.01,('Snap insertion',max(collisions))
    assert overlap(receiver,to_panel(moved(beam,[0,.2,0]),p))>.02,'No snap seating stop'
    assert overlap(receiver,to_panel(moved(beam,[0,-.2,0]),p))>.02,'No recovered retention'
    plug=plug_to_clip(native_plug,p)
    seated=spread(beam,p,s['seated_spread']);peak=spread(beam,p,s['insertion_spread'])
    assert overlap(beam,plug)>.05,'Plug fails to push the relaxed arms wider'
    assert overlap(seated,plug)<.01,('Seated plug interference',overlap(seated,plug))
    assert overlap(receiver,to_panel(seated,p))<.01
    assert overlap(receiver,to_panel(plug,p))<.01
    # A smooth friction stem needs only its seated expansion throughout drive.
    drives=[]
    for distance in np.linspace(0,s['stem_depth']+1,43):
        moving=moved(plug,[0,distance,0])
        drives.append(overlap(peak,moving))
        assert overlap(receiver,to_panel(moving,p))<.01,('Plug/receiver insertion',distance)
    assert max(drives)<.015,('Plug insertion',max(drives))
    assert overlap(receiver,to_panel(peak,p))<.01
    friction=s.get('retention')=='friction'
    if friction:
        assert max(drives)<.015,'Unintended geometric withdrawal interlock'
        # Material formerly removed for both detent pockets is now continuous.
        for side in [-1,1]:
            lo,hi=sorted([side*1.21,side*1.34])
            material=region_clip(beam,[lo,3.7,.6],[hi,4.2,4.4])
            assert abs(material.volume-(hi-lo)*.5*3.8)<.001,'Arm pocket remains'
        band=region_clip(native_plug,[-2,-2,6.4],[2,2,6.9])
        assert abs(band.extents[0]-s['stem_width'])<.001,'Retaining bump remains'
    else:
        assert overlap(seated,moved(plug,[0,.15,0]))>.01,'Plug ribs do not capture axially'
    assert overlap(receiver,to_panel(moved(plug,[0,-.1,0]),p))>.01,'Cover rim has no seating stop'
    # Once capped, compressing the hooks for removal must be physically blocked.
    assert overlap(closed,plug)>.1,'Cap stem does not block hook recompression'
    # Actual tongue width at the panel shows outward spread, not just a filler.
    local=region_clip(seated,[-3,1,-.1],[3,2,p['tongue_height']+.1])
    assert abs(local.extents[0]-s['expanded_neck_width'])<.001
    report['checks']=dict(upper_inside_bearing=True,top_and_bottom_tongue_location=True,
        snap_insertion_max_collision_mm3=max(collisions),seated_spread_per_arm_mm=s['seated_spread'],
        temporary_spread_per_arm_mm=s['insertion_spread'],expanded_neck_width_mm=float(local.extents[0]),
        plug_drive_max_collision_mm3=max(drives),retention='friction' if friction else 'detent',
        plug_ribs_capture=not friction,no_arm_pockets=friction,cover_rim_seating=True,
        blocks_recompression=True,front_projection_mm=s['outer_y']-p['panel_thickness'])
    report['checks'].update(contact)
    report['dxf']=check_dxf(folder/'receiver_laser.dxf',profile)
    for name,source in [('kit_preview','3dpr'),('receiver_preview','receiver_6_0'),('plug_preview','front_plug')]:
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o',
            '--viewall','--autocenter','--camera=50,-70,120,0,0,0','--colorscheme=Tomorrow',
            '-o',str(folder/f'{name}.png'),str(folder/f'{source}.scad')],capture_output=True,text=True,timeout=240)
        result.check_returncode()
    from action_preview_v7 import main as preview
    preview(folder,p)
    report.update(all_checks_passed=True,limitations='Prescribed fit only. No force, stiffness gain, creep or permanent-retention rating.')
    (out/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    names=['3dpr.stl','sample_70.stl','front_plug.stl','receiver_6_0.stl','receiver_laser.dxf','printing.txt',
           'connector_test.json','results.csv','test_card_overview.png','kit_preview.png','plug_preview.png','receiver_preview.png']
    kit='v7_front_spreader_plug_test.zip'
    with zipfile.ZipFile(folder/kit,'w',zipfile.ZIP_DEFLATED) as archive:
        for name in names:archive.write(folder/name,name)
    delivery=ROOT/'output_v7_front_plug';delivery.mkdir(exist_ok=True)
    for name in [kit,*names]:
        if name!='results.csv':shutil.copy2(folder/name,delivery/name)
    shutil.copy2(ROOT/'AI_VERSION_7_FRONT_PLUG.md',delivery/'testing_notes.md')
    previous_check();check_release()
    print('PASS: taller top bearing + front expansion cap; four meshes, one DXF',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--skip-generation',action='store_true')
    main(parser.parse_args().skip_generation)
