"""Selected V7 cabinet views and manufacturing instructions, normal SCAD stage."""
import json
from pathlib import Path
import oobb
import working_scad as drawing
from working_scad_v7 import views,export_dxfs


def write_outputs(folder,thing,kwargs,save_type,overwrite):
    folder=Path(folder);p=drawing.get_ai_version_7_frame_parameters(**kwargs);q=p['frame']
    thing['ai_files']={'3dpr':thing['ai_design']}
    for name in views(p):
        sub=oobb.get_default_thing(type='v7_unit_view')
        drawing.get_ai_version_7(sub,**dict(kwargs,connector_view=name))
        oobb.opsc_make_object(str(folder/f'{name}.scad'),sub['components'],mode='3dpr',
                             save_type=save_type,overwrite=overwrite)
        thing['ai_files'][name]=sub['ai_design']
    projections=[('front_laser_2d','front_laser'),('receiver_laser','receiver_6_0')]
    if p.get('laser_face_test'):
        projections += [(name+'_2d',name) for name in p['reinforcement_types']]
        projections += [('clip_reinforcements_2d','clip_reinforcements'),
                        ('front_3mm_test_2d','front_3mm_test_layout')]
    for name,source in projections:
        prefix='projection(cut=true) translate([0,0,-0.1]) ' if source=='receiver_6_0' else 'projection(cut=false) '
        (folder/f'{name}.scad').write_text(prefix+'{ include <'+source+'.scad>; }\n',encoding='utf-8')
    export_dxfs(folder,[name for name,source in projections])
    data=dict(version=7,variant=p['variant'],selected_clip_sample=71,
        grid_per_face=[p['column'],p['row']],drawer_sides=2,drawer_count=q['drawer_count'],bom=p['bom'],print_batches=p['print_batches'],
        frame_envelope_mm=[round(q['width_total'],6),round(q['height_total'],6),q['assembled_depth']],
        overall_depth_including_caps_mm=q['assembled_depth']+2*(p['front_plug']['outer_y']-p['panel_thickness']),
        plate_web_mm=6,printed_plate_max_depth_mm=18,rail_between_faces_mm=p['rail_length'],
        receiver_hole_mm=[5.2,5.2],frame_mounts=p['frame_mounts'],
        snap_interface={k:p[k] for k in ['spring_root_y','neck_width','tongue_height','upper_support_height','hook_projection','retaining_rake']},
        snap_trial=p['trials'][0],front_plug=p['front_plug'],screw=p['screw'],
        revision='interchangeable_windowed_beams',beam_windows=p['beam_windows'],
        minimum_beam_side_rail_mm=(p['grip_width']-p['beam_lightening']['width'])/2,
        interchangeable_beams=True,running_roof_above_receiver_axis_mm=p['beam_running_height']-p['tongue_height']/2,
        centre_stop_size_mm=[q['middle_stop_width'],q['middle_stop_thickness']],
        service_orientation='CAD negative Y is UP; wide T at top; drawers enter from both ends.',
        enclosure='Plywood/enclosure supplies the bottom drawer floor; sheet joinery is not included.',
        physical_feedback='User selected sample 71 style and tolerance; full-unit strength/loading unverified.')
    if p.get('laser_face_test'):
        data['laser_face_test']=dict(p['laser_face_test'],
            local_clip_thickness_mm=p['panel_thickness'],attachment='Bond to INSIDE of 3 mm face; align both holes.',
            pads_per_face=len(p['reinforcement_pads']),
            counts_per_face={name:sum(pad['view']==name for pad in p['reinforcement_pads']) for name in p['reinforcement_types']},
            placement=p['reinforcement_pads'],nested_cut_layout='front_3mm_test_2d.dxf',
            warning='Physical test only: nominal 3+3 mm stack; bondline and measured sheet thickness affect fit.')
    (folder/'assembly.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    overall=data['overall_depth_including_caps_mm']
    lines=[f"V7 / {p['column']} WIDE x {p['row']} TALL / TWO-SIDED / SYSTEMPAK 209 100 ml",
        f"{q['drawer_count']} drawers total; {p['column']*p['row']} from each end. Dimensions in mm.",
        f"Frame: {q['width_total']:.1f} wide x {q['height_total']:.1f} tall x {q['assembled_depth']:g} deep.",
        f"Overall depth including caps: {overall:g} mm.",
        ('Four screws replace outer mounts at first/last working rows.' if p.get('frame_mount_layout') else
         'Two screw beams at the top; four snap beams at working drawer levels.'),
        f"Either beam type fits ANY of the {len(p['frame_mounts'])} positions; roofs and centre stops align.",
        'Both beams have two rounded windows, 3 mm side rails and solid ends/centre.', '',
        'PRINT EACH LISTED FILE ONCE:',
        'front.stl + back.stl: identical faces; outside face DOWN; 6 mm web, 18 mm maximum depth.']
    lines.extend(f"{name}.stl: {batch['count']} x {batch['component']}. Print ONCE."
                 for name,batch in p['print_batches'].items())
    lines.extend([
        f"Face planning bed: {q['bed_width']:g} x {q['bed_height']:g} mm, with declared margins.",
        'Beam batches are at most 229 mm long; keep the supplied long-flat-face orientation.',
        'Use production PETG settings. Covers: outside face DOWN, stem UP.',
        'Adapters: outside face DOWN, cheeks UP. All numbered batches are required.',
        'Individual snap_beam, screw_beam, front_plug and screw_adapter files are SPARES.',
        'sample_71.stl and receiver_6_0.stl are OPTIONAL fit coupons.',
        '3dpr and assembled are REFERENCE OVERVIEWS, not single-bed print files.', '',
        'LASER ALTERNATIVE: cut front_laser_2d.dxf TWICE from measured 6 mm MDF instead of printing faces.',
        'Laser stops are flat solid 6 mm; printed stops retain angled profiles and inward floor tabs.',
        'MDF cannot provide 12 mm inward tabs: enclosure must supply drawer-floor support.',
        'DXF uses nominal finished mm CUT contours; apply measured kerf once in CAM.',
        'receiver_laser.dxf is an optional fit coupon with the same 5.2 x 5.2 opening.', '',
        f"HARDWARE: {p['bom']['M3_nut']} M3 x 20 countersunk screws and {p['bom']['M3_nut']} M3 nuts.",
        'Side-load nuts before attaching the second face. Seat beams against inside faces.',
        'Press pointed friction covers from outside until their skirts seat against the panel.',
        'No plug detents or arm pockets. Nose .8 mm; fitted stem 2.6 mm.',
        'Fit screw guides from outside and tighten gently. Centre stops separate opposing drawers.',
        'Wide T at TOP in service. Enclosure supplies the bottom drawer floor.',
        'Corner mounting screws depend on the enclosure and are not included.',
        'Test fit and loading progressively; full-assembly force, creep and capacity remain unverified.'])
    if p.get('laser_face_test'):
        lines.extend(['','OPTIONAL 3 mm LASER FACE TEST:',
            'Cut front_3mm_test_2d.dxf ONCE per face from measured 3 mm sheet.',
            f"Includes one face and {len(p['reinforcement_pads'])} reinforcing pieces nested in bin-opening waste.",
            'Each piece is a nominal 12 x 12 x 3 mm square with a centred 5.2 x 5.2 mm hole.',
            'Corner versions have relief for the existing mounting hole; keep their handed orientation.',
            'Bond pieces onto the INSIDE at EVERY snap AND screw receiver; align holes accurately.',
            '3 mm face + 3 mm reinforcement gives nominal 6 mm at the original beam seating plane.',
            'Measure the finished stack including bondline; it must match the existing 6 mm fit.',
            'clip_reinforcement_2d.dxf is one plain spare; clip_reinforcements_2d.dxf is pads only.',
            'Do not also cut pads-only when using the nested full-face layout.',
            'front_3mm_test.stl/scad shows the bonded geometry; it is a reference, not a replacement print kit.',
            'The standard front_laser_2d.dxf remains the existing 6 mm option.',
            'Thinner laser stops and the enclosure floor still need physical support/testing.',
            '3 mm face stiffness and bond strength are UNVERIFIED; this layout is for the requested test.'])
    (folder/'printing.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
