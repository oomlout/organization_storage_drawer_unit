"""CAD checks for 3 mm laser faces with inside 3 mm receiver doublers."""
from pathlib import Path
import numpy as np
from shapely.geometry import box
from shapely.affinity import translate
from shapely.ops import unary_union
from action_validate_ai_version_5 import section,overlap
from action_validate_v7 import check_dxf


def validate(folder,p,meshes):
    folder=Path(folder);t=p['laser_face_test'];q=p['frame']
    reference=meshes['front_laser'];flat=section(reference,.1)
    test=meshes['front_3mm_test'];base=section(test,.1);upper=section(test,4.5)
    assert flat.symmetric_difference(base).area<.001,'3 mm face changes bin openings'
    assert abs(test.extents[2]-p['panel_thickness'])<.001,'Local stack is not 6 mm'
    pads=[];report=dict(pads_per_face=len(p['reinforcement_pads']),face_mm=t['face_thickness'],
                       doubler_mm=t['reinforcement_thickness'],square_mm=t['reinforcement_side'],
                       hole_mm=[p['receiver_hole_width'],p['receiver_hole_height']],mounts=[],dxf=[])
    for pad in p['reinforcement_pads']:
        local=section(meshes[pad['view']],.1)
        assert local.intersection(box(-2.599,-2.599,2.599,2.599)).area<1e-6,'Hole is not centred/clear'
        shape=translate(local,pad['x'],pad['hole_y']);pads.append(shape)
        assert shape.difference(flat.buffer(.0011)).area<.01,(pad,'Doubler enters a bin opening or blocks a fixing')
    # Binary STL stores float32 coordinates. Test boundary displacement rather
    # than accumulating tiny rounding strips around up to sixty squares.
    assert upper.boundary.hausdorff_distance(unary_union(pads).boundary)<.00005,'Assembled doubler placement mismatch'
    expected_volume=reference.volume*t['face_thickness']/p['panel_thickness']+sum(meshes[pad['view']].volume for pad in p['reinforcement_pads'])
    assert abs(test.volume-expected_volume)<.1,'Stack contains overlapping/missing material'
    assert abs(overlap(reference,test)-test.volume)<.1,'Test stack extends outside the original 6 mm face'
    nested=[]
    for pad in p['reinforcement_layout']:
        local=section(meshes[pad['view']],.1)
        shape=translate(local,pad['layout_x'],pad['layout_y'])
        assert shape.intersection(flat).area<1e-6,'Nested square overlaps the face outline'
        assert all(shape.intersection(other).area<1e-6 for other in nested),'Nested squares overlap'
        nested.append(shape)
    layout=section(meshes['front_3mm_test_layout'],.1)
    assert layout.boundary.hausdorff_distance(unary_union([flat,*nested]).boundary)<.00005
    assert abs(meshes['front_3mm_test_layout'].volume-test.volume)<.1,'Cut sheet and bonded reference volumes differ'
    for mount in p['frame_mounts']:
        for kind in ['snap_beam','screw_beam']:
            beam=meshes[kind].copy()
            from working_scad import v7_beam_to_frame
            beam.apply_transform(v7_beam_to_frame(p,mount,kind))
            collision=overlap(test,beam)
            assert collision<.015,(mount,kind,'Beam collision',collision)
            contact=section(beam,p['panel_thickness']+.01)
            old_area=contact.intersection(flat).area;new_area=contact.intersection(upper).area
            assert new_area>0 and new_area>=old_area*.9,(mount,kind,'Lost beam seating land',old_area,new_area)
            report['mounts'].append(dict(**mount,beam=kind,collision_mm3=collision,
                original_seating_area_mm2=old_area,test_seating_area_mm2=new_area))
        # Outside face remains at Z=0: existing caps/adapters and fixing heads
        # retain their original seating plane. The new material is only inside.
        for name,extension in [('front_plug',p['front_plug']['outer_y']-p['panel_thickness']),
                               ('screw_adapter',p['screw']['flange_size'][2])]:
            part=meshes[name].copy()
            if name=='front_plug' and p.get('beam_revision')=='side_printed_runner':
                part.apply_transform(trimesh_rotation_z_90())
            part.apply_translation([mount['x'],mount['hole_y'],-extension])
            assert overlap(test,part)<.015,(mount,name,'Outside fit blocked')
    for name in p['reinforcement_types']:
        report['dxf'].append(check_dxf(folder/f'{name}_2d.dxf',section(meshes[name],.1)))
    report['dxf'].append(check_dxf(folder/'clip_reinforcements_2d.dxf',section(meshes['clip_reinforcements'],.1)))
    report['dxf'].append(check_dxf(folder/'front_3mm_test_2d.dxf',layout))
    report.update(all_checks_passed=True,bin_openings_clear=True,corner_fixings_clear=True,
                  all_snap_and_screw_positions=True,limitations='CAD fit only; 3 mm face stiffness and bonded-joint strength require physical testing.')
    return report


def trimesh_rotation_z_90():
    return [[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]
