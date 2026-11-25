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
    for name,source in [('front_laser_2d','front_laser'),('receiver_laser','receiver_6_0')]:
        prefix='projection(cut=false) ' if source=='front_laser' else 'projection(cut=true) translate([0,0,-0.1]) '
        (folder/f'{name}.scad').write_text(prefix+'{ include <'+source+'.scad>; }\n',encoding='utf-8')
    export_dxfs(folder,['front_laser_2d','receiver_laser'])
    data=dict(version=7,variant=p['variant'],selected_clip_sample=71,
        grid_per_face=[1,2],drawer_sides=2,drawer_count=4,bom=p['bom'],
        frame_envelope_mm=[round(q['width_total'],6),round(q['height_total'],6),q['assembled_depth']],
        overall_depth_including_caps_mm=q['assembled_depth']+2*(p['front_plug']['outer_y']-p['panel_thickness']),
        plate_web_mm=6,printed_plate_max_depth_mm=18,rail_between_faces_mm=p['rail_length'],
        receiver_hole_mm=[5.2,5.2],frame_mounts=p['frame_mounts'],
        snap_interface={k:p[k] for k in ['spring_root_y','neck_width','tongue_height','upper_support_height','hook_projection','retaining_rake']},
        snap_trial=p['trials'][0],front_plug=p['front_plug'],screw=p['screw'],
        service_orientation='CAD negative Y is UP; wide T at top; drawers enter from both ends.',
        enclosure='Plywood/enclosure supplies the bottom drawer floor; sheet joinery is not included.',
        physical_feedback='User selected sample 71 style and tolerance; full-unit strength/loading unverified.')
    (folder/'assembly.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    (folder/'printing.txt').write_text(
        'V7 / ONE WIDE x TWO TALL / TWO-SIDED / SYSTEMPAK 209 100 ml\n\n'
        'FOUR drawers total: two from each end. All dimensions in mm.\n'
        'Frame: 108.5 wide x 99.8 tall x 224 deep; caps extend total depth to 233.2.\n'
        'Top border houses two screw braces, clear of the drawer openings.\n\n'
        'PRINT EACH ONCE:\n'
        'front.stl + back.stl: identical faces, outside face DOWN; 6 mm web, 18 mm maximum depth.\n'
        'snap_beams.stl: FOUR complete beams; BOTH ends use the selected sample 71 snap.\n'
        'screw_beams.stl: TWO complete top braces, with M3 nut pockets at BOTH ends.\n'
        'front_plugs.stl: EIGHT friction covers, outside face DOWN, stem UP.\n'
        'screw_adapters.stl: FOUR countersunk guides, outside face DOWN, cheeks UP.\n'
        'Use production PETG settings. Rails lie on their long flat faces. Retain orientations.\n'
        'Beam batches are 229 mm (snap tips included) / 212 mm long; use a P1P-size bed.\n'
        'Individual snap_beam, screw_beam, front_plug and screw_adapter files are SPARES.\n'
        'receiver_6_0.stl and sample_71.stl are OPTIONAL test coupons, not unit parts.\n'
        '3dpr and assembled are REFERENCE OVERVIEWS, not single-bed print files.\n\n'
        'LASER ALTERNATIVE: cut front_laser_2d.dxf TWICE from measured 6 mm MDF,\n'
        'instead of printing front/back. Stops are flat solid 6 mm; printed stops retain\n'
        'the angled slide-on profiles and inward floor tabs. MDF cannot provide the\n'
        '12 mm inward tabs: supply drawer-floor support from the enclosure.\n'
        'DXF is nominal finished mm contours on CUT; apply measured kerf once in CAM.\n'
        'receiver_laser.dxf is an optional fit coupon with the same 5.2 x 5.2 opening.\n\n'
        'HARDWARE: FOUR M3 x 20 countersunk screws plus FOUR M3 nuts, one per brace end.\n'
        'Side-load nuts before attaching the second face. Upper two receiver holes take\n'
        'screw braces; the four lower holes take snaps. Both use the same rectangular hole.\n'
        'Seat beams against the inside faces; snap hooks emerge outside. Then press each\n'
        'pointed friction plug in from outside until its skirt seats against the panel.\n'
        'There are NO plug detents or arm pockets. Tip width .8; fitted stem 2.6, unchanged.\n'
        'Fit screw guides from outside and tighten screws gently into side-loaded nuts.\n'
        'The beam centre stops separate front/back drawers. Wide T at TOP in service.\n'
        'Fit surrounding plywood/enclosure; it supplies the bottom drawer floor.\n'
        'Corner mounting screw lengths depend on your enclosure and are not included.\n'
        'Test fit and loading progressively; full-assembly force, creep and capacity are unverified.\n',encoding='utf-8')
