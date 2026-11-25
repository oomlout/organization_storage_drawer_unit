"""Export the small V6 fit kit and check it against the unchanged actual plate."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import numpy as np
import trimesh
import yaml
from shapely.geometry import box
import working
import working_scad as drawing
from action_validate_ai_version_5 import check_previous_versions, compressed, moved, overlap, section


def clip(mesh,lo,hi):
    lo,hi=np.array(lo),np.array(hi)
    cutter=trimesh.creation.box(extents=hi-lo)
    cutter.apply_translation((hi+lo)/2)
    return trimesh.boolean.intersection([mesh,cutter],engine='manifold')


def local(mesh,offset):
    result=mesh.copy()
    result.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,offset],[0,0,0,1]])
    return result


def check_unchanged(root):
    baseline=json.loads((root/'validation_v6_clearance/previous_models_baseline.json').read_text())
    for name,expected in baseline.items():
        folder=root/'parts'/name
        assert yaml.safe_load((folder/'working.yaml').read_text())['oobb_details']==expected['inputs'],name
        for filename,digest in expected['scad'].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    check_previous_versions(root)
    return len(baseline)


def main(skip_generation=False):
    root=Path(__file__).resolve().parent
    out=root/'validation_v6_clearance';out.mkdir(exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter='ai_version_6')
    count=check_unchanged(root)
    folder=next(root.glob('parts/*ai_version_6_style_latch_clearance_suite'))
    p=drawing.get_ai_version_6_clearance_parameters(**yaml.safe_load((folder/'working.yaml').read_text())['oobb_details'])
    base=p['reference']
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    meshes={};report=dict(previous_models_unchanged=count,meshes=[],connections=[])
    for name in ['3dpr',*drawing.get_ai_version_6_views(p)]:
        print('Exporting',name,flush=True)
        result=subprocess.run([exe,'--backend=Manifold','--hardwarnings','--export-format=binstl',
            '-o',str(folder/f'{name}.stl'),str(folder/f'{name}.scad')],capture_output=True,text=True,timeout=180)
        (out/f'{name}_export.log').write_text(result.stdout+result.stderr)
        result.check_returncode()
        mesh=trimesh.load_mesh(folder/f'{name}.stl');meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,name
        bodies=list(mesh.split(only_watertight=False))
        assert len(bodies)==(9 if name=='3dpr' else 1),(name,'piece count')
        assert all(abs(b.bounds[0,2])<.001 for b in bodies),(name,'bed contact')
        assert np.all(mesh.extents[:2]+4<=180),(name,'small-bed envelope')
        report['meshes'].append(dict(view=name,closed=True,bodies=len(bodies),
            bounds_mm=mesh.bounds.tolist(),volume_mm3=float(mesh.volume)))
    assert np.allclose(meshes['3dpr'].extents,[43,70,10],atol=.001)
    assert abs(meshes['3dpr'].volume-sum(meshes[f"sample_{t['sample_number']}"].volume for t in p['trials']))<.02

    cabinet=next(root.glob('parts/*ai_version_6_style_double_sided_plywood_250_max'))
    # Exact current production plate, not a relaxed receiver invented for this kit.
    front=trimesh.load_mesh(cabinet/'front.stl')
    mount=min(base['rail_positions'],key=lambda r:abs(r['x'])+abs(r['y']))
    receiver=clip(front,[mount['x']-9,mount['y']-2,-.1],[mount['x']+9,mount['y']+12,6.1])
    receiver.apply_translation([-mount['x'],-mount['y'],0])
    assert receiver.is_watertight
    offset=(p['coupon_grip_length']-base['snap_tip_length'])/2
    control=local(meshes['control_rail'],offset)
    full=local(trimesh.load_mesh(cabinet/'snap_rail.stl'),base['rail_length']/2)
    reference=clip(full,[-10,-1,-7],[10,11,p['coupon_grip_length']])
    common=overlap(control,reference)
    assert abs(control.volume+reference.volume-2*common)<.03,'Unnumbered control differs from the production rail end'
    # Sample 30 differs from the identical reference only by its grip number.
    c30=local(meshes['sample_30'],offset)
    assert overlap(c30,control)>c30.volume-.02
    assert .1<control.volume-c30.volume<50,'Missing or excessive engraving'
    assert abs(clip(c30,[-10,-1,-7],[10,9.45,14]).volume-clip(control,[-10,-1,-7],[10,9.45,14]).volume)<.02

    for t in p['trials']:
        n=t['sample_number'];print('Checking sample',n,flush=True)
        rail=local(meshes[f'sample_{n}'],offset)
        seated=moved(rail,[0,0,base['plate_thickness']])
        seated_collision=overlap(receiver,seated)
        assert seated_collision<.02,(n,'seated collision',seated_collision)
        assert np.allclose(rail.bounds[:,2],[-6,14],atol=.001)
        # All spring/root sections stay identical; only hooks and shoulders vary.
        for z in [.5,2.1,4.5]:
            cross=section(rail,z);original=section(control,z)
            assert cross.symmetric_difference(original).area<.001,(n,'changed spring/root',z)
        cross=section(rail,-.1)
        for side in [-1,1]:
            lo,hi=sorted([side*1.6,side*3.4])
            assert abs(cross.intersection(box(lo,2,hi,9)).area-1.8*7)<.001,(n,'arm thickness')
        # The recovered hook's exported X extent and axial shoulder locate both
        # clearances against the UNCHANGED receiver wall/retaining ledge.
        shoulder=base['plate_thickness']-t['shoulder_depth']
        cross=section(rail,-t['shoulder_depth']-.05)
        pocket=base['snap_profile']['snap_arm_outer']+base['snap_hook_projection']+base['snap_clearance']
        assert abs(pocket-cross.bounds[2]-t['hook_side_clearance'])<.001,(n,'hook clearance')
        assert abs(base['snap_receiver_shoulder']-shoulder-t['axial_clearance'])<.001
        # Free play just below the nominal clearance, then contact just above it.
        free_side=max(overlap(receiver,moved(seated,[s*(t['hook_side_clearance']-.015),0,0])) for s in [-1,1])
        blocked_side=min(overlap(receiver,moved(seated,[s*(t['hook_side_clearance']+.05),0,0])) for s in [-1,1])
        free_axial=overlap(receiver,moved(seated,[0,0,t['axial_clearance']-.015]))
        blocked_axial=overlap(receiver,moved(seated,[0,0,t['axial_clearance']+.05]))
        assert free_side<.02 and free_axial<.02,(n,'less free clearance than specified',free_side,free_axial)
        assert blocked_side>.001 and blocked_axial>.001,(n,'no positive retaining contact',blocked_side,blocked_axial)
        assert overlap(receiver,moved(seated,[0,0,-.3]))>.1,(n,'no seating shoulder')
        q=dict(root_distance=base['snap_root_distance'],insertion_deflection=t['insertion_deflection'],
               hook_shoulder_z=-t['shoulder_depth'],guide_half_width=0,
               rigid_outer_half_width=base['snap_profile']['snap_arm_outer'])
        flex=compressed(rail,q)
        collisions=[overlap(receiver,moved(flex,[0,0,6+d])) for d in [0,.25,.5,1,2,3,4,5,6,7,8]]
        assert max(collisions)<.03,(n,'prescribed insertion collision',collisions)
        report['connections'].append(dict(sample_number=n,seated_clear=True,
            hook_side_clearance_mm=t['hook_side_clearance'],axial_clearance_mm=t['axial_clearance'],
            maximum_prescribed_insertion_interference_mm3=max(collisions),
            free_side_interference_mm3=free_side,free_axial_interference_mm3=free_axial,
            recovered_hooks_block_withdrawal=True,arms_and_roots_unchanged=True))
    report.update(all_checks_passed=True,receiver_unchanged=True,baseline_matches_production=True,
        kit_volume_mm3=float(meshes['3dpr'].volume),solid_petg_mass_g=float(meshes['3dpr'].volume*.00127),
        limitations='Nominal geometric fit and prescribed flex only; no physical fit, force, strength or slicer-time claim')
    for name,source in [('preview','3dpr'),('sample_38_preview','sample_38')]:
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1400,1100','--projection=o',
            '--viewall','--autocenter','--camera=70,-110,200,0,0,0','--colorscheme=Tomorrow',
            '-o',str(folder/f'{name}.png'),str(folder/f'{source}.scad')],capture_output=True,text=True,timeout=180)
        result.check_returncode()
    (out/'report.json').write_text(json.dumps(report,indent=2))
    print('PASS',len(meshes),'mesh views; nine clearances against unchanged receiver;',count,'previous models unchanged',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--skip-generation',action='store_true')
    main(parser.parse_args().skip_generation)
