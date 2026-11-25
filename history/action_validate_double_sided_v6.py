"""V6 pipeline and exported mesh/mechanical checks; no physical-fit claims."""
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
from shapely.geometry import Point, box
import working
import working_scad as drawing
from action_validate_ai_version_5 import check_previous_versions, moved, overlap, compressed
from action_validate_ai_version_4 import section
from action_validate_v6_clearance import clip, local


def snapshot(root):
    return {f.parent.name:{'inputs':yaml.safe_load(f.read_text())['oobb_details'],
                           'scad':{s.name:hashlib.sha256(s.read_bytes()).hexdigest() for s in f.parent.glob('*.scad')}}
            for f in root.glob('parts/*ai_version_5_style*/working.yaml')}


def render_previews(folder, exe):
    # Wide T is the TOP: CAD -Y becomes service +Z. Print geometry is unchanged.
    p=drawing.get_ai_version_6_parameters(**yaml.safe_load((folder/'working.yaml').read_text())['oobb_details'])
    scene=folder/'preview_scene.scad'
    scene.write_text('rotate([-90,0,0]) { include <assembled.scad>; }\n')
    front=folder/'front_preview_scene.scad'
    front.write_text('rotate([-90,0,0]) { include <front.scad>; }\n')
    cx=-p['natural_width']/2+p['drawer_border_edge']+p['opening_width']/2
    y=p['opening_origin_y']
    detail=folder/'support_detail.scad'
    detail.write_text(f'rotate([-90,0,0]) intersection() {{\n include <front.scad>;\n translate([{cx-32},{y-1},-0.1]) cube([64,{p["pitch_y"]+9},18.2]);\n}}\n')
    mount=min(p['rail_positions'],key=lambda r:abs(r['x'])+abs(r['y']))
    receiver=folder/'receiver_detail.scad'
    receiver.write_text(f'rotate([-90,0,0]) intersection() {{\n include <front.scad>;\n translate([{mount["x"]-11},{mount["y"]-4},-0.1]) cube([22,26,6.2]);\n}}\n')
    sources={'assembled':scene,'snap_rail':folder/'snap_rail.scad','front':front,
             'support_detail':detail,'receiver_detail':receiver}
    for name,source in sources.items():
        camera='600,-800,400,0,0,0' if name in ['assembled','receiver_detail'] else '500,700,350,0,0,0' if name in ['front','support_detail'] else '0,0,0,55,0,25,1500'
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1400,1100','--projection=o',
            '--viewall','--autocenter',f'--camera={camera}','--colorscheme=Tomorrow',
            '-o',str(folder/f'{name}.png'),str(source)],capture_output=True,text=True,timeout=180)
        result.check_returncode()


def main(skip_generation=False, variant="double_sided_plywood_250_max"):
    root=Path(__file__).resolve().parent
    phase=root/'validation_double_sided_v6_screw_adapter'
    out=phase/variant; out.mkdir(parents=True,exist_ok=True)
    baseline=root/'validation_double_sided_v6/previous_v5_baseline.json'
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter=variant)
    assert snapshot(root)==json.loads(baseline.read_text()),'Previous V5 input/CAD changed'
    check_previous_versions(root)
    folder=next(root.glob('parts/*ai_version_6_style_'+variant))
    history=json.loads((phase/'previous_models_baseline.json').read_text())
    prior=history[folder.name]
    for name,record in history.items():
        if 'double_sided_plywood_' in name:
            continue
        other=root/'parts'/name
        assert yaml.safe_load((other/'working.yaml').read_text())['oobb_details']==record['inputs'],name
        for filename,digest in record['scad'].items():
            assert hashlib.sha256((other/filename).read_bytes()).hexdigest()==digest,(name,filename)
    inputs=yaml.safe_load((folder/'working.yaml').read_text())['oobb_details']
    changed_keys=['screw_rail_settings']
    assert {k:v for k,v in inputs.items() if k not in changed_keys}=={k:v for k,v in prior['inputs'].items() if k not in changed_keys},'Unrequested cabinet inputs changed'
    assert inputs['selected_latch_sample']==37
    assert hashlib.sha256((folder/'snap_rail.scad').read_bytes()).hexdigest()==prior['scad']['snap_rail.scad'],'Sample-37 snap rail changed'
    for name in ['front.scad','back.scad','joining_plates.scad']:
        assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==prior['scad'][name],(name,'Receiver/plate/joiner changed')
    p=drawing.get_ai_version_6_parameters(**yaml.safe_load((folder/'working.yaml').read_text())['oobb_details'])
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    meshes={}; report={'meshes':[],'prior_v5_records_unchanged':len(snapshot(root)),
        'limitations':['Physical PETG fit, pot stop contact, load capacity, creep and slicing remain unverified.']}
    for name in ['3dpr',*drawing.get_ai_version_6_views(p)]:
        print('Exporting',name,flush=True)
        result=subprocess.run([exe,'--backend=Manifold','--hardwarnings','--export-format=binstl',
            '-o',str(folder/f'{name}.stl'),str(folder/f'{name}.scad')],capture_output=True,text=True,timeout=600)
        (folder/f'validation_{name}.log').write_text(result.stdout+result.stderr)
        result.check_returncode()
        mesh=trimesh.load_mesh(folder/f'{name}.stl'); meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,(name,'invalid mesh')
        if name!='assembled':
            expected=2 if name=='joining_plates' else 10+len(p['rail_kinds']) if name=='3dpr' else 8 if name=='screw_adapters' else 12 if name=='screw_upgrade' else min(p['rails_per_plate'],len(p['rail_kinds'])-(int(name[-2:])-1)*p['rails_per_plate']) if name.startswith('rails_plate_') else 1
            bodies=mesh.split()
            assert len(bodies)==expected,(name,len(bodies),expected)
            assert all(abs(b.bounds[0,2])<.001 for b in bodies),(name,'bed contact')
            if name!='3dpr':
                lo,hi=mesh.bounds
                half=np.array([p['bed_width'],p['bed_height']])/2
                assert np.all(lo[:2]>=-half+p['bed_margin']-.001) and np.all(hi[:2]<=half-p['bed_margin']+.001),(name,'usable bed area')
                assert lo[0]>=-half[0]+p['bed_exclusion'][0]+p['bed_margin']-.001 or lo[1]>=-half[1]+p['bed_exclusion'][1]+p['bed_margin']-.001,(name,'cutter exclusion')
        if variant.endswith('395_max') and name not in ['3dpr','assembled']:
            assert np.all(mesh.bounds[0,:2]>=-p['max_face_size']/2+p['bed_margin']-.001)
            assert np.all(mesh.bounds[1,:2]<=p['max_face_size']/2-p['bed_margin']+.001)
        report['meshes'].append(dict(view=name,bounds_mm=mesh.bounds.tolist(),volume_mm3=float(mesh.volume),passed=True))
    for name,digest in prior['face_stl'].items():
        assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest,(name,'Regenerated plate mesh changed')
    for name,mesh in meshes.items():
        if name.startswith('rails_plate_'):
            assert all(min(abs(b.volume-meshes[k].volume) for k in ['snap_rail','screw_rail'])<.03 for b in mesh.split()),(name,'Rail batch has stale parts')
    assembly_depth=p['assembled_depth']+2*p['screw_rail']['flange_size'][2]
    assert np.allclose(meshes['assembled'].extents,[p['width_total'],p['height_total'],assembly_depth],atol=.015)
    assert np.allclose(meshes['front'].extents,[p['width_total'],p['height_total'],p['plate_print_depth']],atol=.015)
    assert np.allclose(meshes['front'].bounds,meshes['back'].bounds)
    assert abs(meshes['front'].volume-meshes['back'].volume)<1e-6
    assert hashlib.sha256((folder/'front.scad').read_bytes()).hexdigest()==hashlib.sha256((folder/'back.scad').read_bytes()).hexdigest()
    # Exported M3 holes remain open through every layer, with retained edge rings.
    radius=__import__('oobb').gv('hole_radius_m3','3dpr')
    for name in ['front','back']:
        for z in [.1,3,5.9]:
            face=section(meshes[name],z)
            for hole in p['corner_holes']:
                x,y=hole['x'],hole['y']
                assert not face.intersects(Point(x,y).buffer(radius-.05)),(name,'blocked corner hole')
                ring=Point(x,y).buffer(radius+.6).difference(Point(x,y).buffer(radius+.2))
                assert face.covers(ring),(name,'corner hole lacks surrounding material')
    # Verify top/bottom structural edges rather than a padded square.
    face=section(meshes['front'],3)
    assert face.contains(Point(0,-p['height_total']/2+.1))
    assert face.contains(Point(0,p['height_total']/2-.1))
    rear=meshes['back'].copy(); rear.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,224],[0,0,0,1]])
    expected_volume=meshes['front'].volume+rear.volume+sum(meshes[k].volume for k in p['rail_kinds'])+8*meshes['screw_adapter'].volume
    error=expected_volume-meshes['assembled'].volume
    assert abs(error)<.25,('assembly collision',error)
    assert abs(meshes['3dpr'].volume-expected_volume)<.25,'Complete overview has incorrect quantities'
    assert abs(meshes['screw_upgrade'].volume-4*meshes['screw_rail'].volume-8*meshes['screw_adapter'].volume)<.05
    assert abs(meshes['screw_adapters'].volume-8*meshes['screw_adapter'].volume)<.02
    rail=meshes['snap_rail'].copy()
    rail.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,p['rail_length']/2],[0,0,0,1]])
    assert np.allclose(rail.bounds[:,2],[-6,218],atol=.001),'Both tips must end at outer faces'
    # Compare BOTH complete rail ends with the user's actual numbered sample
    # 37, filling only its grip engraving. No receiver dimensions are adapted.
    coupon_folder=next(root.glob('parts/*ai_version_6_style_latch_clearance_suite'))
    selected=local(trimesh.load_mesh(coupon_folder/'sample_37.stl'),4)
    fill=trimesh.creation.box(extents=[11,10,9]);fill.apply_translation([0,5,9.5])
    selected=trimesh.boolean.union([selected,fill],engine='manifold')
    for end in ['front','back']:
        model=rail.copy()
        if end=='back':
            model.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,p['rail_length']],[0,0,0,1]])
        tip=clip(model,[-10,-1,-7],[10,11,14])
        assert abs(tip.volume+selected.volume-2*overlap(tip,selected))<.03,(end,'Does not match sample 37')
    previous=local(trimesh.load_mesh(phase/'previous_parts'/folder.name/'snap_rail.stl'),p['rail_length']/2)
    middle=clip(rail,[-20,-1,14],[20,11,p['rail_length']-14])
    old_middle=clip(previous,[-20,-1,14],[20,11,p['rail_length']-14])
    assert abs(middle.volume+old_middle.volume-2*overlap(middle,old_middle))<.03,'Rail body/stop changed'
    # Stop genuinely widens into the body channel at the exact shared middle.
    cross=section(rail,p['middle_stop_z'])
    assert abs(cross.area-19*10)<.001 and cross.contains(Point(9,8))
    for z in [p['middle_stop_z']-1.51,p['middle_stop_z']+1.51]:
        cross=section(rail,z)
        assert abs(cross.area-11*4)<.001
        assert not cross.contains(Point(9,8))
    # Every bay encounters solid stop wings from either direction.
    mid=section(meshes['assembled'],112)
    for row in range(p['row']):
        y=p['opening_origin_y']+row*p['pitch_y']+p['depth_lip']+7
        for a,b in zip(p['x_mounts'],p['x_mounts'][1:]):
            assert mid.contains(Point(a+8.5,y)) and mid.contains(Point(b-8.5,y))
    for z in [-.5,p['rail_length']+.5]:
        cross=section(rail,z)
        floor=p['snap_tip_root_floor']+p['snap_bevel_slope']*.5
        assert abs(cross.area-2*1.8*(p['rail_height']-floor))<.01,'Actual arm thickness'
    # Verify both 15 mm tabs, open middle, level bearing roofs, and the omitted
    # bottom floor extension in the ACTUAL exported plate, not just parameters.
    sections={z:section(meshes['front'],z) for z in [.1,3,5.9,6.1,12,17.9]}
    for f in p['floor_support_features']:
        if f['kind']!='floor':
            continue
        x=f['pos'][0]+p['floor_support_tab_width']/2
        floor=f['bearing_y']
        for z in [6.1,12,17.9]:
            assert sections[z].contains(Point(x,floor+.1)),('Missing bearing roof',f,z)
            assert not sections[z].contains(Point(x,floor-.1)),('Support intrudes into pot body',f,z)
        for z in [.1,3,6.1,12,17.9]:
            edge=f['envelope'][1]-z if z<f['ramp_end_z'] else p['floor_support_thickness']
            if z>18-p['floor_support_tip_chamfer']:
                edge-=z-(18-p['floor_support_tip_chamfer'])
            assert sections[z].contains(Point(x,floor+edge-.04)),('Missing taper material',z)
            assert not sections[z].contains(Point(x,floor+edge+.04)),('Taper exceeds profile',z)
    for col in range(p['column']):
        x=-p['natural_width']/2+p['drawer_border_edge']+p['opening_width']/2+col*p['pitch_x']
        for row in range(p['row']-1):
            floor=p['opening_origin_y']+row*p['pitch_y']+p['opening_height']
            for z in [6.1,12,17.9]:
                assert not sections[z].contains(Point(x,floor+.5)),('Centre gap filled',row)
        bottom=p['opening_origin_y']+(p['row']-1)*p['pitch_y']+p['opening_height']
        for dx in [-20.5,20.5]:
            for z in [6.1,12,17.9]:
                assert not sections[z].contains(Point(x+dx,bottom+.5)),('Bottom-floor extension should be omitted',col)
    # A continuous 1 mm bridge must survive on BOTH faces at every snap mount.
    for r in p['rail_positions']:
        for z in [.1,3,5.9]:
            cross=section(meshes['front'],z)
            for dx in [-.5,0,.5]:
                for dy in [.1,.5,.9]:
                    assert cross.contains(Point(r['x']+dx,r['y']+dy)),('Receiver web gap',r,z,dx,dy)
    # The user's lower gap was the inherited full-width 1 mm body-extension
    # relief, BELOW the receiver. Probe its former location across both lower
    # shoulders and the central web at EVERY mount and all web-depth layers.
    for mount in p['rail_positions']:
        floor=mount['y']-p['depth_lip']+p['opening_height']
        for z in [.1,3,5.9]:
            cross=sections[z]
            for dx in [-3,-1,0,1,3]:
                for dy in [-.8,-.5,-.2]:
                    assert cross.contains(Point(mount['x']+dx,floor+dy)),('Lower relief slit remains',mount,z,dx,dy)
    # Probe the EXPORTED lower corner against a radius-1 circle. This point
    # distinguishes the new corner from the old radius-4 body opening.
    radius=p['lip_cutout_radius']
    for col in range(p['column']):
        cx=-p['natural_width']/2+p['drawer_border_edge']+p['opening_width']/2+col*p['pitch_x']
        half=(p['opening_width']-2*p['inset_lip'])/2
        for row in range(p['row']):
            bottom=p['opening_origin_y']+row*p['pitch_y']+p['opening_height']
            for side in [-1,1]:
                for z in [.1,3,5.9]:
                    cross=sections[z]
                    # Near the lower corner: a point .5/.5 in from the nominal
                    # rectangle is open with R1, but was solid with R4.
                    assert not cross.contains(Point(cx+side*(half-.5),bottom-.5)),('Wrong lower radius',col,row,z)
                    assert cross.contains(Point(cx+side*(half-.1),bottom-.1)),('Lower radius removed corner material',col,row,z)
    # Layer footprints of each new support only shrink upward. They are rooted
    # on the bed and never introduce a floating flat underside.
    down=(meshes['front'].face_normals[:,2]<-.9)&(meshes['front'].triangles[:,:,2].max(axis=1)>6.05)
    assert not np.any(down),'New support has an unsupported flat underside'
    # Check seated fit at ALL mounts, plus recovered hooks resisting withdrawal.
    beam=local(meshes['screw_rail'],p['rail_length']/2)
    adapter=meshes['screw_adapter'].copy()
    adapter.apply_translation([0,p['screw_rail']['axis_height'],-p['screw_rail']['flange_size'][2]])
    assert np.allclose(beam.bounds[:,2],[0,p['rail_length']],atol=.001)
    assert np.allclose(beam.extents,[p['middle_stop_width'],p['screw_rail']['end_height'],p['rail_length']],atol=.001)
    for mount in p['rail_positions']:
        fitted=moved(beam if mount['file']=='screw_rail' else rail,[mount['x'],mount['y'],6])
        assert overlap(fitted,meshes['front'])<.02
        assert overlap(fitted,rear)<.02
        if mount['file']=='screw_rail':
            front_adapter=moved(adapter,[mount['x'],mount['y'],0])
            back_adapter=adapter.copy();back_adapter.apply_transform([[-1,0,0,mount['x']],[0,1,0,mount['y']],[0,0,-1,224],[0,0,0,1]])
            for part,face in [(front_adapter,meshes['front']),(back_adapter,rear)]:
                assert overlap(part,face)<.02,'Adapter hits existing receiver'
                assert overlap(part,fitted)<.02,'Guide prevents beam seating'
    from validation_v6_screw_geometry import check_screw_geometry,render_screw_previews
    report['screw_connection']=check_screw_geometry(meshes,p,adapter,beam)
    r=p['rail_positions'][10]
    fitted=moved(rail,[r['x'],r['y'],6])
    assert overlap(moved(fitted,[0,0,.5]),meshes['front'])>.1
    assert overlap(moved(fitted,[0,0,-.5]),rear)>.1
    fit=p['selected_rail_fit']
    # Probe free movement just below each selected clearance and retaining
    # contact just beyond it, against each regenerated, unchanged face.
    for face,direction in [(meshes['front'],1),(rear,-1)]:
        for side in [-1,1]:
            assert overlap(moved(fitted,[side*(fit['hook_side_clearance']-.015),0,0]),face)<.02
            assert overlap(moved(fitted,[side*(fit['hook_side_clearance']+.05),0,0]),face)>.001
        assert overlap(moved(fitted,[0,0,direction*(fit['axial_clearance']-.015)]),face)<.02
        assert overlap(moved(fitted,[0,0,direction*(fit['axial_clearance']+.05)]),face)>.001
    q=dict(root_distance=p['snap_root_distance'],insertion_deflection=fit['insertion_deflection'],
           hook_shoulder_z=-fit['shoulder_depth'],guide_half_width=0,
           rigid_outer_half_width=p['snap_profile']['snap_arm_outer'])
    flex=compressed(rail,q)
    collisions=[overlap(moved(flex,[r['x'],r['y'],6+d]),meshes['front']) for d in [0,.25,.5,1,2,3,4,5,6,7,8]]
    assert max(collisions)<.03,('Prescribed insertion',collisions)
    # Both faces are the same part; symmetry checks the second insertion too.
    report.update(all_checks_passed=True,drawer_count=p['drawer_count'],bom=p['bom'],assembled_envelope_mm=[p['width_total'],p['height_total'],assembly_depth],
                  assembly_interference_mm3=float(error),maximum_prescribed_insertion_interference_mm3=max(collisions))
    report['floor_support_tabs_per_face']=sum(f['kind']=='floor' for f in p['floor_support_features'])
    report['face_plate_overall_depth_mm']=p['plate_print_depth']
    report['support_centre_gap_mm']=p['catch_tab_width']-2*p['floor_support_tab_width']
    report['continuous_receiver_web_mm']=p['snap_inner_web_height']
    report['lower_relief_eliminated']=True
    report['matching_cutout_radius_mm']=p['opening_radius']
    report['selected_rail_fit']=fit
    report['both_rail_ends_match_numbered_sample_37']=True
    report['receiver_and_plate_scad_stl_unchanged']=True
    report['rail_body_and_middle_stop_unchanged']=True
    report['numbered_clearance_suite_unchanged']=True
    report['front_and_back_scad_identical']=True
    old_report=root/('validation_double_sided_v6_395_max' if variant.endswith('395_max') else 'validation_double_sided_v6_250_max')/'report.json'
    old=json.loads(old_report.read_text())
    before=next(m['volume_mm3'] for m in old['meshes'] if m['view']=='front')
    report['face_cad_volume_reduction_percent']=100*(before-meshes['front'].volume)/before

    if variant.endswith('395_max'):
        report['individual_prints_fit_395_mm_area_with_2_mm_margin']=True
        original=next(root.glob('parts/*ai_version_6_style*250_max'))
        report['rail_and_joiners_byte_identical_to_250']=all(
            hashlib.sha256((folder/name).read_bytes()).hexdigest()==hashlib.sha256((original/name).read_bytes()).hexdigest()
            for name in ['snap_rail.scad','snap_rail.stl','joining_plates.scad','joining_plates.stl'])
        assert report['rail_and_joiners_byte_identical_to_250']
        report['screw_parts_identical_to_250']=all(
            hashlib.sha256((folder/name).read_bytes()).hexdigest()==hashlib.sha256((original/name).read_bytes()).hexdigest()
            for name in ['screw_rail.scad','screw_rail.stl','screw_adapter.scad','screw_adapter.stl','screw_adapters.scad','screw_adapters.stl','screw_upgrade.scad','screw_upgrade.stl'])
        assert report['screw_parts_identical_to_250']
    render_previews(folder,exe)
    render_screw_previews(folder,exe,p)
    # A compact delivery containing actual individual prints, without the
    # oversized overview or assembled reference.
    print_names=['front','back','snap_rail','screw_rail','screw_adapter','screw_adapters','screw_upgrade','joining_plates']+[n for n in meshes if n.startswith('rails_plate_')]
    with zipfile.ZipFile(folder/'print_files_screw_adapter.zip','w',compression=zipfile.ZIP_DEFLATED) as archive:
        for name in print_names:
            archive.write(folder/f'{name}.stl',f'{name}.stl')
        for name in ['printing.txt','assembly.json']:
            archive.write(folder/name,name)
    (out/'report.json').write_text(json.dumps(report,indent=2))
    print('PASS',len(meshes),'mesh views;',len(p['rail_kinds']),'fitted rails; centre stops;',p['drawer_count'],'pot positions; 8 corner holes',flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--skip-generation',action='store_true')
    parser.add_argument('--variant',choices=['double_sided_plywood_250_max','double_sided_plywood_395_max'],default='double_sided_plywood_250_max')
    args=parser.parse_args()
    main(args.skip_generation,args.variant)
