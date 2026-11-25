"""Mesh checks for the current side-printed thin-runner revision.

Called by action_generate_current_v7 after the normal three-stage build.
Historical validators and their locked inputs remain historical.
"""
import hashlib
from pathlib import Path
import numpy as np
import trimesh
from action_validate_ai_version_5 import overlap, moved, section
from action_validate_v7_permanent_snap import region_clip
from action_validate_v7_front_plug import full_contact_check, to_panel, plug_to_clip, spread
from action_validate_v7 import prescribed_flex
import working_scad as drawing

ROOT=Path(__file__).resolve().parent


def to_service(mesh,p):
    result=mesh.copy();bed=p['side_runner']['bed_x']
    result.apply_transform([[0,0,1,bed],[0,1,0,0],[-1,0,0,0],[0,0,0,1]])
    return result


def validate(folder,p,meshes):
    r=p['side_runner'];s=p['screw'];q=p['frame'];length=p['rail_length']
    report=dict(runner_mm=[r['width'],r['thickness']],offset_mm=r['offset_x'],beams=[],nuts=[],outside_parts=[],
                preceding_adapter_head_envelope_collisions=[])
    old_folder=ROOT/'validation_v7_side_runner'/'previous_current'/Path(folder).name
    preceding_record=old_folder.is_dir()
    if not preceding_record:
        assert p['variant']=='unit_2_wide_2_tall','New variant needs an explicit shared-component baseline'
        old_folder=next((ROOT/'validation_v7_side_runner'/'previous_current').glob('*unit_1_wide_2_tall'))
    report['preceding_catalogue_record']=preceding_record
    # This baseline is a snapshot of the actual preceding active catalogue.
    unchanged=(['front','back','front_laser','screw_adapter','receiver_6_0',
                 'front_3mm_test','front_3mm_test_layout',*p['reinforcement_types'],'clip_reinforcements']
               if preceding_record else ['screw_adapter','receiver_6_0','clip_reinforcement'])
    for name in unchanged:
        old=old_folder/f'{name}.stl'
        assert old.read_bytes()==(Path(folder)/f'{name}.stl').read_bytes(),(name,'unchanged component altered')
    for kind in ['snap_beam','screw_beam']:
        beam=to_service(meshes[kind],p)
        axis=p['tongue_height']/2 if kind=='snap_beam' else s['axis_height']
        roof=axis+8
        running=region_clip(beam,[r['bed_x']-.1,-85,-10],[r['bed_x']+r['width']+.1,-80,30])
        assert np.allclose(running.bounds,[[r['bed_x'],-85,roof-3],[r['bed_x']+r['width'],-80,roof]],atol=.0001),(kind,'running strip')
        assert len(meshes[kind].split())==1 and meshes[kind].is_watertight
        # Every part lies above the bed; the clip broad face really is at Z=0.
        assert abs(meshes[kind].bounds[0,2])<1e-6
        contact=section(meshes[kind],.01)
        assert contact.area>length*2.9,(kind,'runner edge lacks bed contact')
        old=trimesh.load_mesh(old_folder/f'{kind}.stl')
        saving=100*(1-meshes[kind].volume/old.volume)
        assert saving>30,(kind,'material reduction',saving)
        # Retain the old inward runner limit: no extra material in the body path.
        assert r['bed_x']+r['width']<=p['grip_width']/2+1e-6
        # The +X stop still reaches the body of EVERY column at its left mount.
        for col in range(p['column']):
            centre=-q['width_total']/2+q['drawer_border_edge']+q['opening_width']/2+col*q['pitch_x']
            left=centre-q['pitch_x']/2
            body_left=centre-(q['opening_width']/2-q['inset_lip'])
            assert left+r['stop_max_x']>body_left+.5,('drawer stop misses body',col)
        report['beams'].append(dict(kind=kind,volume_mm3=float(meshes[kind].volume),
            previous_volume_mm3=float(old.volume),saving_percent=saving,roof_above_axis_mm=8,
            bed_contact_area_mm2=contact.area,one_closed_body=True))
    beam=to_service(meshes['screw_beam'],p)
    for rear in [False,True]:
        local=beam.copy()
        if rear:local.apply_transform([[1,0,0,0],[0,-1,0,-length],[0,0,-1,2*s['axis_height']],[0,0,0,1]])
        nut=trimesh.creation.cylinder(radius=s['nut_radius']-.03,height=s['nut_depth']-.08,sections=6)
        nut.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
        nut.apply_translation([0,-s['nut_near']-s['nut_depth']/2,s['axis_height']])
        collisions=[overlap(local,moved(nut,[-d,0,0])) for d in np.linspace(0,12,25)]
        assert max(collisions)<.02,('nut side loading',rear,max(collisions))
        capture=[overlap(local,moved(nut,[0,d,0])) for d in [-.3,.3]]
        assert min(capture)>.01,('nut lacks axial capture',rear,capture)
        bore=trimesh.creation.cylinder(radius=s['bore_radius']-.04,height=s['length'],sections=48)
        bore.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
        bore.apply_translation([0,6+s['flange_size'][2]-s['length']/2,s['axis_height']])
        assert overlap(local,bore)<.02,('screw bore not aligned',rear)
        report['nuts'].append(dict(rear=rear,primitive='OOBB version 5 oobb_nut',clearance='right / local -X',
            maximum_loading_collision_mm3=max(collisions),axial_capture_collision_mm3=capture,bore_clear=True))
    sample=meshes['sample_71'];receiver=meshes['receiver_6_0'];plug=plug_to_clip(meshes['front_plug'],p)
    report['full_squeeze']=full_contact_check(sample,receiver,p)
    closed=prescribed_flex(sample,p,p['trials'][0])
    insertion=[overlap(receiver,to_panel(moved(closed,pull),p)) for pull in [[0,d,0] for d in np.linspace(-12,0,25)]]
    assert max(insertion)<.015,('shorter clip insertion',max(insertion))
    expanded=spread(sample,p,p['front_plug']['seated_spread'])
    assert overlap(expanded,plug)<.02,'Friction plug no longer fits shortened arms'
    old_plug=trimesh.load_mesh(old_folder/'front_plug.stl')
    stem_box=[[-10,-10,p['front_plug']['cup_depth']+.01],[10,10,p['front_plug']['stem_depth']+.1]]
    old_stem=region_clip(old_plug,*stem_box);new_stem=region_clip(meshes['front_plug'],*stem_box)
    assert old_stem.difference(new_stem,engine='manifold').volume<.002
    assert new_stem.difference(old_stem,engine='manifold').volume<.002
    report['cover']=dict(size_mm=[p['front_plug']['cover_width'],p['front_plug']['cover_height']],
        orientation_change_degrees=90,stem_unchanged=True,
        minimum_side_wall_mm=(p['front_plug']['cover_width']-p['front_plug']['cavity_width'])/2)
    report['spring']=dict(slot_depth_mm=-p['spring_root_y'],
        conservative_in_beam_span_mm=-p['trials'][0]['effective_root_y'],
        total_to_shoulder_mm=p['trials'][0]['spring_length'],
        maximum_insertion_collision_mm3=max(insertion),friction_plug_clear=True)
    front=meshes['front'];back=front.copy()
    back.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,q['assembled_depth']],[0,0,0,1]])
    for mount in p['frame_mounts']:
        for kind in ['snap_beam','screw_beam']:
            is_snap=kind=='snap_beam';beam=meshes[kind].copy()
            beam.apply_transform(drawing.v7_beam_to_frame(p,mount,kind))
            for rear in [False,True]:
                name='front_plug' if is_snap else 'screw_adapter';part=meshes[name].copy()
                extension=p['front_plug']['outer_y']-6 if is_snap else s['flange_size'][2]
                turn=np.pi/2 if is_snap else 0
                rotation=trimesh.transformations.euler_matrix(0,np.pi if rear else 0,turn)
                part.apply_transform(rotation)
                part.apply_translation([mount['x'],mount['hole_y'],q['assembled_depth']+extension if rear else -extension])
                assert max(overlap(face,part) for face in [front,back])<.015,(mount,name,'face clash')
                if not is_snap:assert overlap(beam,part)<.015,(mount,'adapter clash')
                for d in [0,1,3,6,10,16]:
                    moving=moved(part,[0,0,d if rear else -d])
                    assert max(overlap(face,moving) for face in [front,back])<.015,(mount,name,'insertion clash')
                for corner in q['corner_holes']:
                    head=trimesh.creation.cylinder(radius=3,height=3,sections=32)
                    head.apply_translation([corner['x'],corner['y'],q['assembled_depth']+1.5 if rear else -1.5])
                    collision=overlap(part,head)
                    if name=='screw_adapter' and collision>=.015:
                        # The unchanged adapter already occupied this generic
                        # 6 mm head envelope in the preceding plywood layout.
                        # Establish non-regression without claiming clearance.
                        old=trimesh.load_mesh(old_folder/'screw_adapter.stl')
                        old.apply_transform(rotation)
                        old.apply_translation([mount['x'],mount['hole_y'],q['assembled_depth']+extension if rear else -extension])
                        prior=overlap(old,head)
                        assert collision<=prior+.001,(mount,'adapter head clearance regressed')
                        report['preceding_adapter_head_envelope_collisions'].append(dict(**mount,rear=rear,
                            intersection_mm3=collision,previous_intersection_mm3=prior,head_diameter_mm=6))
                    else:assert collision<.015,(mount,name,'corner screw blocked')
                report['outside_parts'].append(dict(**mount,beam=kind,rear=rear,face_and_insertion_clear=True))
    report.update(all_checks_passed=True,unchanged_faces=preceding_record,unchanged_adapters_receivers=True,
        limitations='Prescribed geometry only. New arm effort, narrow-side lip bearing, runner stiffness and creep require print tests.')
    return report
