"""Source-led permanent snap trial: explicit full arm contact, no over-closure."""
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
from shapely.geometry import LineString,box
import working
import working_scad as drawing
from working_scad_v7 import views
from action_validate_v7 import export,check_dxf,to_receiver,prescribed_flex
from action_validate_ai_version_5 import overlap,moved,section,check_previous_versions
from action_lock_version_6 import check as check_release

ROOT=Path(__file__).resolve().parent


def check_previous_v7():
    previous=json.loads((ROOT/'validation_v7_permanent_snap/previous_v7_baseline.json').read_text(encoding='utf-8'))
    for name,expected in previous.items():
        folder=ROOT/'parts'/name
        assert yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details']==expected['inputs'],name
        for filename,digest in expected['files'].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    print('Previous V7:',len(previous),'records /',sum(len(p['files']) for p in previous.values()),'files unchanged',flush=True)


def region_clip(mesh,lo,hi):
    lo,hi=np.asarray(lo),np.asarray(hi)
    cutter=trimesh.creation.box(extents=hi-lo);cutter.apply_translation((lo+hi)/2)
    return trimesh.boolean.intersection([mesh,cutter],engine='manifold')


def main(skip_generation=False):
    out=ROOT/'validation_v7_permanent_snap';out.mkdir(exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter='ai_version_7',scad_navigation=False)
    check_previous_v7();frozen=check_release();check_previous_versions(ROOT)
    folder=next((ROOT/'parts').glob('*ai_version_7_style_permanent_full_squeeze_snap_test'))
    p=drawing.get_ai_version_7_parameters(**yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details'])
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    report=dict(version=7,revision='permanent_full_squeeze',meshes=[],joints=[],
        old_models_unchanged=len(frozen['parts']),intended_use='One-time push-in; permanence unproven physically')
    meshes={}
    for name in ['3dpr',*views(p)]:
        print('Exporting',name,flush=True);export(exe,folder,out,name)
        mesh=trimesh.load_mesh(folder/f'{name}.stl');meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,name
        pieces=list(mesh.split(only_watertight=False));expected=3 if name=='3dpr' else 1
        assert len(pieces)==expected,(name,len(pieces))
        assert all(abs(part.bounds[0,2])<.001 for part in pieces)
        assert max(mesh.extents[:2])+4<=180
        report['meshes'].append(dict(view=name,bodies=expected,closed=True,extents_mm=mesh.extents.tolist(),volume_mm3=float(mesh.volume)))
    assert abs(meshes['3dpr'].volume-sum(meshes[f"sample_{t['sample_number']}"].volume for t in p['trials']))<.03
    receiver=meshes['receiver_6_0'];profile=section(receiver,.1)
    for i in range(3):
        x=(i-1)*24
        hole=box(x-2.599,-2.099,x+2.599,2.099)
        assert profile.intersection(hole).area<1e-6
        assert profile.intersection(box(x+2.61,-1,x+2.7,1)).area>.17
        assert profile.intersection(box(x-1,2.11,x+1,2.2)).area>.17
    for t in p['trials']:
        n=t['sample_number'];print('Checking permanent snap',n,flush=True)
        mesh=meshes[f'sample_{n}'];seated=to_receiver(mesh,p)
        assert overlap(receiver,seated)<.005,(n,'recovered fit')
        assert overlap(receiver,moved(seated,[0,0,-.1]))>.02,(n,'inside seating shoulder')
        assert overlap(receiver,moved(seated,[0,0,.08]))<.005,(n,'nominal axial allowance')
        assert overlap(receiver,moved(seated,[0,0,.2]))>.02,(n,'retaining barb')
        # The actual mesh must have four fingers within the beam and larger
        # hooks, rather than just metadata asserting those dimensions.
        planar=section(mesh,2)
        spans=planar.intersection(LineString([(-7,-6),(7,-6)]))
        assert len(list(spans.geoms))==4,(n,'four-finger beam')
        hook=region_clip(mesh,[-6,t['shoulder_y']+.2,-.1],[6,t['shoulder_y']+.6,4.1])
        assert abs(hook.extents[0]-7.6)<.001,(n,'hook width')
        flex=prescribed_flex(mesh,p,t)
        # Isolate and flex each arm independently. This exposes any false
        # passage caused by one deformed arm overlapping the other.
        left=region_clip(mesh,[-6,-31,-.1],[0,t['tip_y']+.1,4.1])
        right=region_clip(mesh,[0,-31,-.1],[6,t['tip_y']+.1,4.1])
        left=prescribed_flex(left,p,t);right=prescribed_flex(right,p,t)
        self_interference=overlap(left,right)
        assert self_interference<.002,(n,'arms interpenetrate',self_interference)
        ltip=left.vertices[left.vertices[:,1]>=t['shoulder_y']+.05]
        rtip=right.vertices[right.vertices[:,1]>=t['shoulder_y']+.05]
        actual_gap=float(rtip[:,0].min()-ltip[:,0].max())
        assert abs(actual_gap)<.001,(n,'arms did not close completely',actual_gap)
        closed_head=region_clip(flex,[-6,t['shoulder_y']+.2,-.1],[6,t['shoulder_y']+.6,4.1])
        assert abs(closed_head.extents[0]-p['receiver_hole_width'])<.001,(n,'closed head width')
        # With only 95% closure, the head must FAIL to pass; full contact is
        # required, not merely an optional amount of extra prescribed flex.
        partial=prescribed_flex(mesh,dict(p,deflection=.95*p['deflection']),t)
        probe_shift=t['shoulder_y']-p['panel_thickness']/2
        partial_collision=overlap(receiver,moved(to_receiver(partial,p),[0,0,probe_shift]))
        assert partial_collision>.01,(n,'hooks are not aggressive enough to require contact')
        compressed=to_receiver(flex,p)
        collisions=[overlap(receiver,moved(compressed,[0,0,d])) for d in np.linspace(0,t['tip_y']+1,37)]
        assert max(collisions)<.01,(n,'closed arms do not pass',max(collisions))
        # Vertical fit is tightened as well: .1 mm free in each direction.
        for direction in [-1,1]:
            assert overlap(receiver,moved(seated,[0,direction*.08,0]))<.005
            assert overlap(receiver,moved(seated,[0,direction*.15,0]))>.01
        report['joints'].append(dict(sample_number=n,hook_projection_mm=1.4,recovered_head_width_mm=7.6,
            retaining_overlap_per_side_mm=p['retention_overlap'],deflection_per_arm_mm=p['deflection'],
            actual_closed_arm_gap_mm=actual_gap,self_interference_mm3=self_interference,
            closed_head_width_mm=float(closed_head.extents[0]),partial_95_percent_closure_collision_mm3=partial_collision,
            maximum_closed_insertion_collision_mm3=max(collisions),positive_pullout_stop=True,
            designed_release=False,physical_permanence='Not established'))
    report['dxf']=check_dxf(folder/'receiver_laser.dxf',profile)
    for name,source in [('clips_preview','3dpr'),('receiver_preview','receiver_6_0')]:
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900',
            '--projection=o','--viewall','--autocenter','--camera=50,-70,120,0,0,0','--colorscheme=Tomorrow',
            '-o',str(folder/f'{name}.png'),str(folder/f'{source}.scad')],capture_output=True,text=True,timeout=240)
        result.check_returncode()
    from action_preview_v7 import main as preview
    preview(folder,p)
    report.update(all_checks_passed=True,limitations='Rigid/kinematic CAD only; no force, permanence, destructive-removal or fatigue rating.')
    (out/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    names=['3dpr.stl','receiver_6_0.stl','receiver_laser.dxf','printing.txt','connector_test.json',
           'trial_index.csv','results.csv','test_card_overview.png','clips_preview.png','receiver_preview.png']
    names+=[f"sample_{t['sample_number']}.stl" for t in p['trials']]
    kit='v7_permanent_snap_test.zip'
    with zipfile.ZipFile(folder/kit,'w',zipfile.ZIP_DEFLATED) as archive:
        for name in names:archive.write(folder/name,name)
    delivery=ROOT/'output_v7_permanent_snap';delivery.mkdir(exist_ok=True)
    for name in [kit,'3dpr.stl','receiver_6_0.stl','receiver_laser.dxf','printing.txt','test_card_overview.png','clips_preview.png','receiver_preview.png']:
        shutil.copy2(folder/name,delivery/name)
    shutil.copy2(ROOT/'AI_VERSION_7_PERMANENT_SNAP.md',delivery/'testing_notes.md')
    check_previous_v7();check_release()
    print('PASS: full-contact permanent snap trial; five meshes, three joints, one DXF',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--skip-generation',action='store_true')
    main(parser.parse_args().skip_generation)
