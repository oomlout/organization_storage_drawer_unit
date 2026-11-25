"""Numbered V6 rail-fit kit metadata, emitted in the ordinary SCAD stage."""
import csv
import json
from pathlib import Path
import oobb
import working_scad as drawing


def write_outputs(folder,thing,kwargs,save_type,overwrite):
    folder=Path(folder)
    p=drawing.get_ai_version_6_clearance_parameters(**kwargs)
    base=p['reference']
    thing['ai_files']={'3dpr':thing['ai_design']}
    for filename,view in drawing.get_ai_version_6_views(p).items():
        sub=oobb.get_default_thing(type='v6_clearance_view')
        drawing.get_ai_version_6(sub,**dict(kwargs,connector_view=view))
        oobb.opsc_make_object(str(folder/f'{filename}.scad'),sub['components'],mode='3dpr',
                             save_type=save_type,overwrite=overwrite)
        thing['ai_files'][filename]=sub['ai_design']
    metadata=dict(trials=p['trials'],receiver_unchanged=True,
        baseline_sample=30,baseline_profile_sample=28,
        kit_envelope_mm=[p['width_total'],p['height_total'],base['rail_height']],
        sample_envelope_mm=[base['rail_width'],p['coupon_grip_length']+base['snap_tip_length'],base['rail_height']],
        arm_thickness_mm=base['snap_profile']['twin_arm_thickness'],
        arm_body_side_clearance_mm=base['snap_clearance'],
        vertical_clearance_mm=base['snap_clearance'],
        unchanged=['receiver','arm thickness','root relief','arm outer faces','tip position','vertical fit'],
        physical_feedback='Current cabinet latch clicks in but is loose; no strength or fracture result reported')
    (folder/'connector_test.json').write_text(json.dumps(metadata,indent=2))
    fields=['sample_number','hook_side_clearance','axial_clearance','hook_projection','shoulder_depth','insertion_deflection']
    with (folder/'trial_index.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        writer.writerows({k:t[k] for k in fields} for t in p['trials'])
    results=folder/'results.csv'
    if not results.exists():
        with results.open('w',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(['sample_number','insertion','click','sideways_play','end_play','preferred','notes'])
            writer.writerows([[t['sample_number'],'','','','','',''] for t in p['trials']])
    (folder/'printing.txt').write_text(
        'V6 numbered latch clearance test, samples 30-38. Dimensions in mm.\n'
        'Print 3dpr.stl ONCE for all nine short rail ends, as arranged with numbers UP. No receiver needs printing.\n'
        'The kit is 43 x 70 x 10 mm; each specimen is 11 x 20 x 10 mm. Keep the supplied long-face-down orientation.\n'
        'Use the same PETG, nozzle, layer height and slicer settings as the production rails. No designed supports.\n'
        'Numbers are recessed 0.5 mm into the solid grip, away from the springs.\n'
        'Test each numbered tip from INSIDE the existing V6 plate, just like a rail end. Seat the broad shoulder against the plate.\n'
        'The production receiver, both cabinet designs and all full rails remain unchanged.\n'
        '30 is the original V6 fit. 30/31/32: hook-pocket side clearance 0.25; 33/34/35: 0.15; 36/37/38: 0.05 per side.\n'
        'Within each group, end play is 0.20 / 0.10 / 0.05 respectively. These are nominal CAD clearances.\n'
        'Only the hook reach and retaining shoulder position change. Arm body side clearance and vertical clearance remain 0.25.\n'
        'The 1.8 mm arms, slot roots, bearing strips and flush tip position are unchanged. Tighter hooks require more insertion flex.\n'
        'Compare the seated sideways wiggle and pull/push play; report the preferred number and whether it clicked/needed excessive effort.\n'
        'For removal, squeeze the two hooks inward from the outside while withdrawing the grip.\n'
        'sample_*.stl are individual replacements; control_rail.stl is an unnumbered baseline for CAD validation, not an extra kit piece.\n'
        'results.csv is yours to fill in and will never be overwritten by regeneration. Physical PETG fit/retention are unverified.\n',encoding='utf-8')
