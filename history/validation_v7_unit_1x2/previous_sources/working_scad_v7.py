"""V7 output metadata and flat DXF sources, called by the ordinary SCAD stage."""
import csv
import json
from pathlib import Path
import shutil
import subprocess
import ezdxf
import oobb
import working_scad as drawing


def views(p):
    result={f"sample_{t['sample_number']}":{} for t in p['trials']}
    if p.get('permanent_snap_test'):
        result['receiver_6_0']={}
        if p.get('front_plug_test'):result['front_plug']={}
        return result
    if p.get('finger_count',5)==4:
        result.update(receiver_6_0={},keeper_key={},screw_test={},screw_beam={},screw_adapter={})
        if p.get('drop_loop'):result.update(drop_key={},loop_key_addon={})
        result.update({f'front_{size}_{kind}':{} for size in ['small','large'] for kind in ['printed','laser']})
        return result
    result.update(receiver_6_0={},receiver_5_8={'receiver_print_thickness':5.8},
                  receiver_6_2={'receiver_print_thickness':6.2},
                  screw_test={},screw_beam={},screw_adapter={})
    result.update({f'front_{size}_{kind}':{} for size in ['small','large']
                   for kind in ['printed','laser']})
    return result


def export_dxfs(folder,sources):
    """Laser deliverables are emitted by the responsible SCAD stage itself."""
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    if not exe:
        raise RuntimeError('OpenSCAD is required to generate the V7 laser DXFs')
    for name in sources:
        result=subprocess.run([exe,'--backend=Manifold','--hardwarnings',
            '-o',str(folder/f'{name}.dxf'),str(folder/f'{name}.scad')],
            capture_output=True,text=True,timeout=240)
        (folder/f'{name}_export.log').write_text(result.stdout+result.stderr,encoding='utf-8')
        result.check_returncode()
        doc=ezdxf.readfile(folder/f'{name}.dxf')
        # OpenSCAD omits units in its legacy DXF header. Use a standard version
        # that supports explicit mm units and its closed lightweight polylines.
        doc.dxfversion='AC1024';doc.units=4;doc.header['$MEASUREMENT']=1
        if 'CUT' not in doc.layers:doc.layers.new('CUT',dxfattribs={'color':1})
        for entity in doc.modelspace():entity.dxf.layer='CUT'
        doc.saveas(folder/f'{name}.dxf')


def write_outputs(folder,thing,kwargs,save_type,overwrite):
    folder=Path(folder)
    p=drawing.get_ai_version_7_parameters(**kwargs)
    thing['ai_files']={'3dpr':thing['ai_design']}
    for name,extra in views(p).items():
        sub=oobb.get_default_thing(type='v7_test_view')
        drawing.get_ai_version_7(sub,**dict(kwargs,connector_view=name,**extra))
        oobb.opsc_make_object(str(folder/f'{name}.scad'),sub['components'],mode='3dpr',
                             save_type=save_type,overwrite=overwrite)
        thing['ai_files'][name]=sub['ai_design']
    # Pure projected contours: no pockets, countersinks, text or duplicate lines.
    # MDF card uses the bottom section of its printed counterpart, below labels.
    sources={'receiver_laser':'receiver_6_0',
             'front_small_laser_2d':'front_small_laser',
             'front_large_laser_2d':'front_large_laser'}
    if p.get('permanent_snap_test'):sources={'receiver_laser':'receiver_6_0'}
    for name,source in sources.items():
        (folder/f'{name}.scad').write_text(
            ('projection(cut=true) translate([0,0,-0.1]) '
             if name=='receiver_laser' else 'projection(cut=false) ')
            + '{ include <'+source+'.scad>; }\n',encoding='utf-8')
    export_dxfs(folder,sources)
    if p.get('front_plug_test'):
        return write_front_plug_metadata(folder,p)
    if p.get('permanent_snap_test'):
        return write_permanent_metadata(folder,p)
    if p.get('finger_count',5)==4:
        return write_concept_metadata(folder,p)
    (folder/'connector_test.json').write_text(json.dumps(dict(
        version=7,experimental=True,panel_material='6 mm nominal MDF',
        nominal_hole_mm=[p['receiver_hole_width'],p['receiver_hole_height']],
        nominal_side_clearance_mm=p['side_clearance'],retaining_overlap_mm=p['retention_overlap'],
        trials=p['trials'],screw=p['screw'],
        thickness_note='Measure actual sheet; 5.8 / 6.0 / 6.2 mm printed cards check sensitivity.',
        projection_note='DXF is nominal finished contour in mm; compensate measured kerf once in CAM.',
        adoption='Test coupons only; no full V7 rail selected. Prototype face files await physical testing.'
    ),indent=2),encoding='utf-8')
    fields=['sample_number','arm_thickness','axial_clearance','spring_length','root_radius',
            'tip_y','strain_proxy','stiffness_proxy']
    with (folder/'trial_index.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore')
        writer.writeheader(); writer.writerows(p['trials'])
    # Never erase the user's observations during a rebuild.
    if not (folder/'results.csv').exists():
        with (folder/'results.csv').open('w',newline='') as stream:
            writer=csv.writer(stream)
            writer.writerow(['sample_number','receiver_material','measured_thickness_mm','hole_width_mm',
                'insertion_effort','clicked','side_play','axial_play','release_effort','cycles','damage','preferred','notes'])
            writer.writerows([[t['sample_number']]+['']*12 for t in p['trials']])
    (folder/'printing.txt').write_text(
        'V7 EXPERIMENTAL THROUGH-PANEL CLIPS — 6 mm MDF — dimensions in mm\n\n'
        'PRINT FIRST: 3dpr.stl once (nine separate numbered clips 40–48), receiver_6_0.stl once,\n'
        'and screw_test.stl once (beam end + outside adapter). Do not connect parts with a raft.\n'
        'Optional receiver_5_8.stl and receiver_6_2.stl simulate sheet variation. sample_*.stl are spares.\n'
        'Keep all supplied orientations. Clips lie long-face-down; numbers UP; no designed supports.\n'
        'Use the production PETG, ideally 0.4 mm nozzle, 0.2 mm layers; record your actual settings.\n'
        'Start with sample 44 in the CENTRE 7.6 x 4.6 hole; then compare 41 and 47 (softer/stiffer).\n'
        '40–42: 1.2 mm arms; 43–45: 1.5 mm; 46–48: 1.8 mm. Within each row axial play is\n'
        '0.10 / 0.25 / 0.40 mm for a true 6.00 mm sheet. These are CAD values, not measured fit.\n'
        'Insert from the unlabelled back of the receiver; hooks emerge on the labelled outside.\n'
        'The broad beam shoulder seats on the inside; squeeze both exposed hooks to remove.\n'
        'Holes left-to-right: 7.2, 7.4, 7.6, 7.8, 8.0 mm; all 4.6 mm high. Printed labels show widths.\n'
        'Record insertion, play, removal, damage and repeat-cycle behaviour in results.csv.\n'
        'Test thickness variation separately: thin panels add play; thick panels can prevent clicking.\n\n'
        'LASER: receiver_laser.dxf is a 126 x 32 mm test card in nominal 6 mm MDF. No engraving\n'
        'is required: mark hole widths by hand using receiver_map.svg. DXF has CUT contours only,\n'
        'all at Z=0, mm units. Use measured kerf compensation ONCE in CAM and cut holes first.\n'
        'Measure actual sheet thickness and hole width on both faces before comparing to prints.\n\n'
        'SCREW: M3 x 20 countersunk screw + M3 nut, one each (not included). Side-load the nut\n'
        'into the beam; put the adapter from OUTSIDE through the SAME centre receiver hole;\n'
        'beam seats INSIDE. Adapter countersink face prints DOWN, cheeks UP. Screw is entered\n'
        'through the adapter into the nut. Flange adds 2.4 mm outside; tighten gently for this test.\n\n'
        'PROTOTYPE FACES: front_small/large_laser_2d.dxf are complete nominal flat MDF faces.\n'
        'Their stops are solid across the 6 mm sheet. front_small/large_printed.stl retain the V6\n'
        'angled slide-on stop and 12 mm inward floor supports, with the new rectangular holes.\n'
        'These demonstrate the two manufacturing paths; NO full-length V7 rail is selected yet.\n'
        'The flat MDF version has no inward floor extensions; plywood/enclosure support remains\n'
        'necessary. Do not mix these receiver holes with V6 rails. Test coupons before full faces.\n'
        'Analytical strain and stiffness are screening proxies; insertion force, fatigue, MDF edge\n'
        'durability, PETG creep and loaded cabinet performance require physical testing.\n',encoding='utf-8')
    labels=''.join(f'<rect x="{15+i*48-w}" y="30.8" width="{2*w}" height="9.2" fill="white" stroke="black"/>'
                   f'<text x="{15+i*48}" y="23" text-anchor="middle">{w:.1f}</text>'
                   for i,w in enumerate(p['receiver_hole_widths']))
    (folder/'receiver_map.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="756" height="240" viewBox="-20 0 270 85">'
        '<rect x="-15" y="3" width="252" height="64" rx="4" fill="#eee" stroke="black"/>'
        '<g font-family="Arial" font-size="7">'+labels+
        '<text x="110" y="58" text-anchor="middle">All holes 4.6 mm high; centre is nominal</text>'
        '<text x="110" y="80" text-anchor="middle">V7 receiver — printed or 6 mm MDF</text></g></svg>',encoding='utf-8')


def write_concept_metadata(folder,p):
    metadata=dict(version=7,revision='four_finger_mechanisms',finger_count=4,
        nominal_hole_mm=[p['receiver_hole_width'],p['receiver_hole_height']],
        neck_width_mm=p['neck_width'],outer_seating_strip_width_mm=p['outer_strip_width'],
        permanent_centre_tongue=False,axial_clearance_mm=.25,trials=p['trials'],
        keeper=p['keeper'],screw=p['screw'],
        comparison='Different mechanisms at one nominal fit; no clearance matrix.',
        limitations='Printed and MDF fit, force, fatigue and keeper retention await physical tests.')
    (folder/'connector_test.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    fields=['sample_number','technique','title','arm_thickness','axial_clearance','spring_length','root_radius','tip_y']
    with (folder/'trial_index.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(p['trials'])
    results=folder/'results.csv'
    if not results.exists():
        with results.open('w',newline='') as stream:
            writer=csv.writer(stream)
            writer.writerow(['sample_number','technique','receiver_material','measured_thickness_mm','insertion_effort',
                             'release_effort','side_play','axial_play','cycles','damage','preferred','notes'])
            writer.writerows([[t['sample_number'],t['technique']]+['']*10 for t in p['trials']])
    if p.get('drop_loop'):
        return write_loop_metadata(folder,p)
    (folder/'printing.txt').write_text(
        'V7 FOUR-FINGER MECHANISM CARD — PETG / nominal 6 mm MDF\n\n'
        'Print 3dpr.stl ONCE: FOUR numbered clips (50–53) + ONE separate locking key.\n'
        'Print receiver_6_0.stl ONCE and screw_test.stl ONCE (beam end + adapter).\n'
        'Keep supplied flat orientations, labels UP. Use production PETG settings; no designed supports.\n'
        'sample_*.stl and keeper_key.stl are replacement pieces, not additional kit quantities.\n\n'
        '50 — straight cantilever arms: control for insertion and squeeze-to-release.\n'
        '51 — tapered arms: 1.8 mm at the root to 1.2 mm at the hook; same mating envelope.\n'
        '52 — S-shaped arms: curved spring paths within the beam; same hook and hole.\n'
        '53 — snap plus removable blocking key: insert the clip normally, then slide the separate\n'
        'key down between the hooks from OUTSIDE. The key blocks inward hook movement.\n'
        'Remove the key before squeezing the hooks. It is an intentionally removable loose key;\n'
        'captive/anti-loss retention is not developed. It does not provide force-free insertion.\n'
        'The key is a separate optional lock, not a permanent centre tongue.\n\n'
        'All five receiver holes are IDENTICAL 6.0 x 4.6 mm, labelled 50 / 51 / 52 / 53 / M3.\n'
        'All clips use a 5.5 mm neck, 0.25 mm nominal axial play and matching external hooks.\n'
        'Each clip has TWO inner latch arms and TWO thicker outer seating strips. There is no\n'
        'centre tongue. Compare mechanisms first; do not sand/tune individual fits during the comparison.\n'
        'Insert clips from the UNLABELLED inside; hooks emerge on the LABELLED outside.\n'
        'Record effort, release, play, repeated use and damage in results.csv; regeneration preserves it.\n\n'
        'LASER: receiver_laser.dxf cuts the same card in nominal 6 mm MDF. DXF is finished geometry\n'
        'in mm, with closed CUT contours. Measure actual stock and apply measured kerf once in CAM.\n'
        'Use receiver_map.svg to mark the labels by hand.\n\n'
        'SCREW REFERENCE: one M3 x 20 countersunk screw + one M3 nut (not included). Side-load\n'
        'the nut into the beam; insert adapter from outside into the SAME 6.0 x 4.6 hole; beam\n'
        'seats inside. Adapter prints countersink DOWN, cheeks UP. Nominal flange depth is 2.4 mm.\n\n'
        'Prototype faces use this same nominal hole; printed stops stay angled, MDF stops solid\n'
        'through 6 mm. Full-length V7 rails remain unselected. Physical insertion force, durability,\n'
        'MDF wear and loaded performance are unverified; CAD flex probes are not force simulations.\n',encoding='utf-8')
    labels=''.join(f'<rect x="{15+i*48-6}" y="30.8" width="12" height="9.2" fill="white" stroke="black"/>'
                   f'<text x="{15+i*48}" y="23" text-anchor="middle">{label}</text>'
                   for i,label in enumerate(p['receiver_labels']))
    (folder/'receiver_map.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="756" height="240" viewBox="-20 0 270 85">'
        '<rect x="-15" y="3" width="252" height="64" rx="4" fill="#eee" stroke="black"/>'
        '<g font-family="Arial" font-size="7">'+labels+
        '<text x="110" y="58" text-anchor="middle">All five holes identical: 6.0 x 4.6 mm</text>'
        '<text x="110" y="80" text-anchor="middle">V7 mechanisms: printable receiver or 6 mm MDF</text></g></svg>',encoding='utf-8')


def write_loop_metadata(folder,p):
    d=p['drop_loop']
    metadata=json.loads((folder/'connector_test.json').read_text(encoding='utf-8'))
    metadata.update(revision='mechanisms_with_vertical_drop_key',drop_loop=d,
        comparison='50–53 retained; 54 is a rigid through-loop with a separate key dropped vertically from above.',
        print_bodies=7,receiver_labels=p['receiver_labels'])
    (folder/'connector_test.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    (folder/'printing.txt').write_text(
        'V7 MECHANISM CARD + RIGID LOOP / VERTICAL DROP KEY (54)\n\n'
        'Print 3dpr.stl ONCE: five numbered samples 50–54, the slim blocking key for 53,\n'
        'and the short, broad-headed DROP key for 54: SEVEN separate parts.\n'
        'Print receiver_6_0.stl ONCE and screw_test.stl ONCE. Individual sample/key STLs are spares.\n'
        'Keep supplied flat print orientations; use production PETG settings. No designed supports.\n\n'
        '50: straight cantilever. 51: tapered arms. 52: S-shaped spring.\n'
        '53: snap normally, then insert its slim blocking key from OUTSIDE between the arms.\n'
        '54: NO snapping or flexing. Push the rigid loop through the panel from INSIDE.\n'
        'Hold the receiver upright, with the loop eye open top-to-bottom. Drop the short\n'
        'broad-headed T key DOWN from ABOVE through the exposed loop. Its head rests on the\n'
        'loop; its stem crosses the panel opening vertically and prevents beam withdrawal.\n'
        'Lift the T key UP to release; then pull the loop back through the panel.\n'
        'The key moves vertically, perpendicular to the beam, not axially along the beam.\n'
        'This is a loose gravity-seated key: there is no captive latch or anti-loss detent.\n\n'
        'All SIX receiver holes are identical 6.0 x 4.6 mm, labelled 50 / 51 / 52 / 53 / 54 / M3.\n'
        'The 150 x 32 mm receiver is printable or laser-cuttable in nominal 6 mm MDF. DXF\n'
        'declares mm and finished CUT contours. Measure actual stock; compensate kerf once in CAM.\n'
        '54 uses the same 5.5 x 4.0 mm through-neck. Its eye is 2.4 x 2.2 mm; walls 1.55 mm,\n'
        'nose 1.5 mm. The key stem is 2 x 2 x 7 mm, with a 7 x 2 x 1.6 mm head.\n'
        'Loop projection is 3.75 mm beyond nominal MDF. Nominal axial free travel is .25 mm.\n'
        'There must be room above to drop/lift the key; the head and stem extend beyond the hole.\n'
        'Check drawer/front clearance before any full-unit adoption.\n\n'
        'M3 reference: one M3 x 20 countersunk screw and M3 nut, not supplied; side-load nut\n'
        'into beam, adapter from outside. Adapter prints countersink DOWN and cheeks UP.\n'
        'Record insertion, locking/release, play and repeated use in results.csv; it is preserved.\n'
        'Sample 54 is a mechanism trial, not a tested load-rated joint. Force, wear, creep,\n'
        'fatigue, accidental key lift and full-unit clearances remain physically unverified.\n',encoding='utf-8')
    with (folder/'printing.txt').open('a',encoding='utf-8') as stream:
        stream.write('\nALREADY PRINTED THE FOUR-FINGER CARD? Print loop_key_addon.stl once for only\n'
                     'sample 54 plus its T key. Use any existing 6.0 x 4.6 mm hole; no new receiver\n'
                     'is needed. Do not also print these parts from the full combined card.\n')
    labels=''.join(f'<rect x="{15+i*48-6}" y="30.8" width="12" height="9.2" fill="white" stroke="black"/>'
                   f'<text x="{15+i*48}" y="23" text-anchor="middle">{label}</text>'
                   for i,label in enumerate(p['receiver_labels']))
    (folder/'receiver_map.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="240" viewBox="-20 0 318 85">'
        '<rect x="-15" y="3" width="300" height="64" rx="4" fill="#eee" stroke="black"/>'
        '<g font-family="Arial" font-size="7">'+labels+
        '<text x="135" y="58" text-anchor="middle">All SIX holes: 6.0 x 4.6 mm</text>'
        '<text x="135" y="80" text-anchor="middle">54: loop through panel, key drops from ABOVE</text></g></svg>',encoding='utf-8')


def write_permanent_metadata(folder,p):
    (folder/'connector_test.json').write_text(json.dumps(dict(
        version=7,revision='permanent_full_squeeze',user_feedback='Previous snap hooks insufficiently aggressive; receiver holes too large.',
        intended_use='One-time push-in fitting; no designed release feature',
        receiver_hole_mm=[p['receiver_hole_width'],p['receiver_hole_height']],
        free_neck_width_mm=p['neck_width'],hook_projection_mm=p['hook_projection'],
        hook_overlap_per_side_mm=p['retention_overlap'],deflection_per_arm_mm=p['deflection'],
        retaining_back_rake_mm=p['retaining_rake'],trials=p['trials'],
        limitations='CAD contact does not establish permanent retention or destructive-removal force.'
    ),indent=2),encoding='utf-8')
    fields=['sample_number','technique','title','tip_thickness','axial_clearance','spring_length','closed_arm_gap','closed_hook_width']
    with (folder/'trial_index.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(p['trials'])
    if not (folder/'results.csv').exists():
        with (folder/'results.csv').open('w',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(['sample_number','material','actual_thickness_mm','arm_tips_met','insertion_effort','clicked',
                             'axial_play','side_play','destructive_pull_result','failure_location','preferred','notes'])
            writer.writerows([[t['sample_number']]+['']*11 for t in p['trials']])
    (folder/'printing.txt').write_text(
        'V7 PERMANENT FULL-SQUEEZE SNAP TEST — 60 / 61 / 62\n\n'
        'Print 3dpr.stl ONCE: three separate numbered snap ends. Print receiver_6_0.stl ONCE.\n'
        'sample_60/61/62.stl are spares. Use the supplied flat orientations, labels UP, production PETG.\n'
        '60: straight arms. 61: thick-root tapered arms. 62: S-shaped spring arms.\n'
        'All three have the SAME larger hooks and smaller receiver fit; choose a mechanism first.\n\n'
        'NEW receiver holes are 5.2 x 4.2 mm (previous 6.0 x 4.6). Neck is 4.8 x 4.0 mm.\n'
        'Hooks project 1.4 mm per side (previous .8); recovered head width is 7.6 mm.\n'
        'Each arm tip is 1.2 mm thick. Required inward travel is 1.2 mm per arm, closing the\n'
        '2.4 mm centre gap COMPLETELY at the hooks. Closed head width is exactly 5.2 mm.\n'
        'This is deliberate nominal contact, with no CAD over-compression of one arm into the other.\n'
        'The new height leaves .1 mm clearance per face. Do NOT use the older oversized receiver.\n\n'
        'INTENDED ONE-TIME USE: push from inside until the shoulders seat and hooks recover outside.\n'
        'Retaining faces are square/back-raked .15 mm; broad .8 mm lands resist withdrawal.\n'
        'No release pads, release ramp, or removable locking key are provided. Expect to sacrifice\n'
        'a sample/receiver when testing removal. Do not assume CAD proves removal requires damage.\n'
        'A tool may still reach the exposed hooks; physical destructive pull tests determine permanence.\n'
        'If the arms meet but a poor print still cannot enter, record that rather than forcing past\n'
        'the contact stop. The closed arms cannot move farther without crushing or deforming.\n'
        'Record arm contact, effort, click, play and the outcome/failure location when pulled.\n'
        'results.csv is preserved. Only physical fit feedback was supplied; no prior breakage was reported.\n\n'
        'MDF: receiver_laser.dxf cuts the SAME three smaller holes in nominal 6 mm stock.\n'
        'Use measured kerf compensation ONCE in CAM; DXF is finished nominal geometry in mm.\n'
        'The smaller receiver is for this test. No full cabinet rail or final interface is selected.\n'
        'Physical insertion force, permanent retention, PETG creep and MDF edge damage remain unverified.\n',encoding='utf-8')


def write_front_plug_metadata(folder,p):
    s=p['front_plug']
    (folder/'connector_test.json').write_text(json.dumps(dict(
        version=7,revision='upper_support_front_spreader_cap_friction',sample=p['trials'][0]['sample_number'],
        spring_slot_depth_mm=-p['spring_root_y'],
        hole_mm=[p['receiver_hole_width'],p['receiver_hole_height']],tongue_height_mm=p['tongue_height'],
        upper_shoulder_height_mm=p['upper_support_height'],plug=s,trials=p['trials'],
        intended_use='Permanent snap with front expansion/cover plug',
        limitations='Kinematic fit only; no physical strength, insertion force or permanence rating.'
    ),indent=2),encoding='utf-8')
    if not (folder/'results.csv').exists():
        with (folder/'results.csv').open('w',newline='') as stream:
            writer=csv.writer(stream)
            writer.writerow(['sample','material','actual_thickness_mm','snap_insertion','top_support','plug_insertion','plug_retention',
                             'play_before','play_after','pull_result','failure_location','notes'])
            writer.writerow([p['trials'][0]['sample_number']]+['']*11)
    (folder/'printing.txt').write_text(
        f"V7 SAMPLE {p['trials'][0]['sample_number']} — FRICTION-ONLY FRONT EXPANSION COVER\n\n"
        'Print 3dpr.stl ONCE: ONE numbered snap end + ONE front covering plug, two solids.\n'
        'Print receiver_6_0.stl ONCE. Individual sample_*.stl and front_plug.stl are spares.\n'
        'The new hole is 5.2 x 5.2 mm in a 6 mm panel. The old 4.2 mm-tall receiver is too short.\n'
        'Keep all supplied print orientations. Clip long face DOWN; plug outside cover face DOWN,\n'
        'spreading stem UP. Use production PETG settings. The parts have bed-rooted geometry.\n\n'
        'The tongue grows from 4 to 5 mm tall; the outer support columns rise to 7 mm. Orient\n'
        'the extra column height ABOVE the hole. The upper inside shoulders now bear above\n'
        'the opening, while the tongue also locates against its top/bottom edges.\n'
        'The 1.4 mm hooks still require the middle arms to meet when passing the 5.2 mm width.\n\n'
        '1. Push the snap from INSIDE until its shoulders seat and the barbs recover outside.\n'
        '2. From OUTSIDE, align the plug stem with the gap between the two arms.\n'
        '3. Press the plug inward to seat the covering rim. The tapered stem pushes each arm\n'
        '   OUTWARD .1 mm in its seated state; it does not merely fill the gap.\n'
        '4. The smooth stem is held by FRICTION ONLY. There are no retaining bumps or arm\n'
        '   pockets. The cover encloses the hooks and overlaps every hole edge.\n'
        'The fitted neck is 5.0 mm wide during both insertion and seating. There is\n'
        'no extra simulated spread beyond the actual hole width. Cap is 11 x 8 mm with a 2 mm\n'
        'front face and hollow skirt. Maximum outside projection is 4.6 mm beyond the panel.\n'
        'No designed service release is provided. Strength/stiffness gains are unproven until\n'
        'tested; preload can creep and frictional retention must be checked physically.\n\n'
        'Compare wiggle before and after fitting the plug, seating of the upper shoulders,\n'
        'plug insertion/pull-out force, and the outcome of a destructive pull. Preserve results.csv.\n'
        'An existing detent_click CSV column belongs to the earlier revision; leave it blank\n'
        'for friction tests and record this revision in notes. No existing results are erased.\n'
        'This first plug test uses the straight-arm control; no full rail is selected.\n'
        'receiver_laser.dxf provides the same square through-hole for nominal 6 mm MDF, in mm.\n'
        'Apply measured kerf once in CAM. Physical fit, fatigue, PETG creep, MDF wear and\n'
        'permanent retention need testing. Earlier numbered samples and releases are preserved.\n',encoding='utf-8')
    if p.get('short_spring_test'):
        with (folder/'printing.txt').open('a',encoding='utf-8') as stream:
            stream.write('\nSAMPLE 71: slots extend 7 mm behind the inner panel face, HALF the 14 mm\n'
                'depth of preferred sample 70. Hook, hole, arm thickness, upper bearing and\n'
                'friction cap fit are retained. Shorter arms will be stiffer; compare insertion\n'
                'effort and any damage. CAD checks do not establish PETG strength.\n'
                'If you have sample 70 already, print ONLY sample_71.stl and reuse its plug\n'
                'and 5.2 x 5.2 mm receiver. Otherwise print the supplied two-part kit.\n')
