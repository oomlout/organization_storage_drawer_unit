"""Selected V7 cabinet views and manufacturing instructions, normal SCAD stage."""
import json
import re
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
        beam_depth_reduction_per_end_mm=p['beam_depth_reduction_per_end'],
        beam_total_depth_reduction_mm=2*p['beam_depth_reduction_per_end'],
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
    side=p.get('beam_revision')=='side_printed_runner'
    if p.get('cap_quantities'):
        data['push_in_cap_quantities']=p['cap_quantities']
        data['push_in_cap_styles']={'front_plug':'Corner clearances (four per complete unit).',
                                   'front_plug_square':'Full square; same friction stem and cavity.'}
    finishing=bool(p.get('finishing_revision'))
    if side:
        data.update(revision=p['beam_revision'],side_runner=p['side_runner'],minimum_beam_side_rail_mm=None,
            centre_stop_size_mm=[p['side_runner']['stop_max_x']-p['side_runner']['stop_min_x'],q['middle_stop_thickness']],
            centre_stop='One-sided reach into every drawer column; both banks stopped.',
            cap_orientation='Use NEW 9.8 x 8 mm covers; turn 90 degrees in the panel plane.',
            physical_feedback='Shorter 5 mm slots and side-printed 3 mm runners are new; print fit and loading require testing.')
    if p.get('runner_alignment'):
        data['runner_alignment']=dict(p['runner_alignment'],
            shared_divider_bearing_mm=[2.35,2.35],
            face_change='Shared receivers move +1.5 mm in front-face CAD X; reuse current beams/caps/adapters.',
            printed_faces_handed=any(m['shared_runner'] for m in p['frame_mounts']),
            back_local_mounts=[dict(m,x=-m['x']) for m in p['frame_mounts']],
            laser_orientation='Flat faces use the same global horizontal hole positions, not mirrored hole locations.',
            pads='Centre squares on dividers; shared-receiver holes are +1.5 mm from pad centres.')
    if finishing:
        top=max(-m['hole_y']+8+p['side_runner']['stop_height'] for m in p['frame_mounts'])
        overhang=max(0,top-q['height_total']/2)
        data.update(finishing_revision=p['finishing_revision'],
            centre_stop_height_above_runner_mm=p['side_runner']['stop_height'],
            centre_stop='Rises 6 mm ABOVE the running surface; no downward stop extension.',
            receiver_depth_split_mm=[p['screw']['beam_receiver_depth'],p['screw']['guide_depth']],
            receiver_actual_engagement_mm=[p['screw']['beam_engagement'],p['screw']['adapter_engagement']],
            cap_orientation='Centre the 9.8 mm square cover on the runner; its stem is offset 1.5 mm.',
            top_stop_overhang_mm=round(overhang,6),
            overall_height_including_stops_mm=round(q['height_total']+overhang,6),
            component_reuse='Reuse the preceding balanced faces and hardware; print new beams, locks and screw adapters.')
    if p.get('joiners'):
        data['optional_joiners']=dict(folder='joiners',file='joiners/joiners.stl',
            pieces=p['joiners'],settings=p['optional_joiners'],included_in_unit_bom=False,
            hardware='M3 countersunk screws with suitable backing/nuts; length depends on the face/backing stack.',
            placement='Outside faces, raised seating pads against face. Plastic face edges touch; rotate strip for vertical joins.')
    (folder/'assembly.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    overall=data['overall_depth_including_caps_mm']
    lines=[f"V7 / {p['column']} WIDE x {p['row']} TALL / TWO-SIDED / SYSTEMPAK 209 100 ml",
        f"{q['drawer_count']} drawers total; {p['column']*p['row']} from each end. Dimensions in mm.",
        f"Frame: {q['width_total']:.1f} wide x {q['height_total']:.1f} tall x {q['assembled_depth']:g} deep.",
        f"Overall depth including caps: {overall:g} mm.",
        f"Beams shortened {2*p['beam_depth_reduction_per_end']:g} mm total ({p['beam_depth_reduction_per_end']:g} mm per drawer bank); end fittings retain their original depths.",
        ('Four screws replace outer mounts at first/last working rows.' if p.get('frame_mount_layout') else
         f"{p['bom']['screw_beam']} screw beams at the top; {p['bom']['snap_beam']} snap beams at working drawer levels."),
        f"Either beam type fits ANY of the {len(p['frame_mounts'])} positions; roofs and centre stops align.",
        ('Both beams: 8 mm wide x 3 mm thick running strip, offset 1.5 mm from the clip/screw axis.' if side else
         'Both beams have two rounded windows, 3 mm side rails and solid ends/centre.'), '',
        'PRINT EACH LISTED FILE ONCE:',
        ('front.stl + back.stl: HANDED faces; print ONE of EACH; outside face DOWN; 6 mm web, 18 mm maximum.'
         if p.get('runner_alignment') and p['column']>1 else
         'front.stl + back.stl: identical faces; outside face DOWN; 6 mm web, 18 mm maximum depth.')]
    lines.extend(f"{name}.stl: {batch['count']} x {batch['component']}. Print ONCE."
                 for name,batch in p['print_batches'].items())
    if p.get('cap_quantities'):
        lines.extend([f"PUSH-IN LOCK CAPS: 4 corner-clearance + {p['cap_quantities']['front_plug_square']} full-square caps TOTAL across both faces.",
            'front_plug.stl is the relieved spare; front_plug_square.stl is the full-square spare.',
            'Use two relieved caps per face at the outer snap positions marked cap_component=front_plug in assembly.json.',
            'The new named cap batches replace the old all-relieved front_plugs batches; do not print both.'])
    if p.get('runner_alignment') and p['column']>1:
        lines.extend(['REVISED FACES REQUIRED for centred shared runners; existing beams/covers/adapters can be reused.',
            'Shared-divider holes move +1.5 mm in front-face CAD X: nominal lip bearing is 2.35 mm on BOTH sides.',
            'Laser faces: keep shifted holes horizontally aligned through the unit; do not mirror the hole locations.'])
    if finishing:
        lines.extend(['FINISHING REVISION: reuse the existing balanced faces and hardware; print NEW beams, locks and screw adapters.',
            'Centre stops rise 6 mm above the running surface; keep the supplied side-print orientation.',
            'The 6 mm receiver depth is split nominally 3 + 3 mm, with 2.95 mm engagement each and a 0.1 mm mating gap.',
            'Centre each square lock cover on its runner; the offset stem lines up with the receiver hole.',
            'Keep trimmed adapter edges toward the same cabinet side at both ends; do not mirror the offset flange.'])
        if overhang>1e-6:
            lines.append(f"Top-brace stops project {overhang:g} mm above the faces; overall nominal height {q['height_total']+overhang:.1f} mm.")
    lines.extend([
        f"Face planning bed: {q['bed_width']:g} x {q['bed_height']:g} mm, with declared margins.",
        ('Beam batches: SIDE DOWN as supplied; snap broad faces lie on the bed. No supports designed in.' if side else
         'Beam batches are at most 229 mm long; keep the supplied long-flat-face orientation.'),
        'Use production PETG settings. Covers: outside face DOWN, stem UP.',
        'Adapters: outside face DOWN, cheeks UP. All numbered batches are required.',
        'Individual snap_beam, screw_beam, front_plug and screw_adapter files are SPARES.',
        ('sample_71.stl is the REVISED 5 mm-slot coupon; receiver_6_0.stl is the existing optional receiver.' if side else
         'sample_71.stl and receiver_6_0.stl are OPTIONAL fit coupons.'),
        '3dpr and assembled are REFERENCE OVERVIEWS, not single-bed print files.', '',
        'LASER ALTERNATIVE: cut front_laser_2d.dxf TWICE from measured 6 mm MDF instead of printing faces.',
        'Laser stops are flat solid 6 mm; printed stops retain angled profiles and inward floor tabs.',
        'MDF cannot provide 12 mm inward tabs: enclosure must supply drawer-floor support.',
        'DXF uses nominal finished mm CUT contours; apply measured kerf once in CAM.',
        'receiver_laser.dxf is an optional fit coupon with the same 5.2 x 5.2 opening.', '',
        f"HARDWARE: {p['bom']['M3_nut']} M3 x 20 countersunk screws and {p['bom']['M3_nut']} M3 nuts.",
        ('Side-load nuts through the BED SIDE opening before fitting faces; OOBB v5 pocket shares the bore axis.' if side else
         'Side-load nuts before attaching the second face. Seat beams against inside faces.'),
        ('Use NEW 9.8 x 9.8 mm offset friction covers; centre covers on the runners and press from outside.' if finishing else
         'Use NEW 9.8 x 8 mm friction covers; turn 90 degrees from the old orientation and press from outside.' if side else
         'Press pointed friction covers from outside until their skirts seat against the panel.'),
        'No plug detents or arm pockets. Nose .8 mm; fitted stem 2.6 mm.',
        'Fit screw guides from outside and tighten gently. Centre stops separate opposing drawers.',
        'Wide T at TOP in service. Enclosure supplies the bottom drawer floor.',
        'Corner mounting screws depend on the enclosure and are not included.',
        'Test fit and loading progressively; full-assembly force, creep and capacity remain unverified.'])
    if p.get('laser_face_test'):
        lines.extend(['','OPTIONAL 3 mm LASER FACE TEST:',
            'Cut front_3mm_test_2d.dxf ONCE per face from measured 3 mm sheet.',
            f"Includes one face and {len(p['reinforcement_pads'])} reinforcing pieces nested in bin-opening waste.",
            ('Each piece is 12 x 12 x 3 mm: shared-divider holes are offset +1.5 mm; outer holes are centred.'
             if p.get('runner_alignment') else
             'Each piece is a nominal 12 x 12 x 3 mm square with a centred 5.2 x 5.2 mm hole.'),
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
    if p.get('joiners'):
        lines.extend(['','OPTIONAL UNIT JOINERS: joiners/joiners.stl contains one two-hole strip and one four-hole corner plate.',
            'Print outside faces DOWN (countersinks on bed), raised seating pads UP; choose quantities to suit your arrangement.',
            'Fasten on outside faces through the existing corner holes with M3 countersunk screws and backing/nuts.',
            'The 10 mm hole pitch assumes touching plastic face edges. See joiners/printing.txt for details.'])
    (folder/'printing.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    if p.get('cap_quantities'):
        # The preceding all-relieved batches are protected in the revision
        # snapshot. Retire their active names so they cannot double-count caps.
        for path in folder.glob('front_plugs*'):
            if re.fullmatch(r'front_plugs(?:_\d+)?\.(?:scad|stl)',path.name):path.unlink()
