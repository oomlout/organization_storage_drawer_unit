"""V6 generated view and assembly metadata, written by the normal SCAD stage."""
import json
from pathlib import Path
import oobb
import working_scad as drawing


def write_outputs(folder, thing, kwargs, save_type, overwrite):
    if kwargs.get('connector_design')=='v6_clearance_suite':
        from working_scad_v6_clearance import write_outputs as write_clearance
        return write_clearance(folder,thing,kwargs,save_type,overwrite)
    p = drawing.get_ai_version_6_parameters(**kwargs)
    views = drawing.get_ai_version_6_views(p)
    thing['ai_files'] = {'3dpr':thing['ai_design']}
    for filename, view in views.items():
        sub = oobb.get_default_thing(type='double_sided_view')
        drawing.get_ai_version_6(sub,**dict(kwargs,connector_view=view))
        oobb.opsc_make_object(f'{folder}/{filename}.scad',sub['components'],mode='3dpr',
                              save_type=save_type,overwrite=overwrite)
        thing['ai_files'][filename] = sub['ai_design']
    Path(folder,'assembly.json').write_text(json.dumps({
        'bom':p['bom'], 'views':views, 'drawer_count':p['drawer_count'],
        'grid_per_face':[p['column'],p['row']], 'identical_face_plates':True,
        'frame_envelope_mm':[p['width_total'],p['height_total'],p['assembled_depth']],
        'assembled_envelope_mm':[p['width_total'],p['height_total'],p['assembled_depth']+2*p['screw_rail']['flange_size'][2]],
        'rail_between_plates_mm':p['rail_length'], 'snap_tip_length_mm':p['snap_tip_length'],
        'plate_base_web_depth_mm':p['plate_thickness'], 'plate_overall_depth_mm':p['plate_print_depth'],
        'floor_support_tabs_per_face':sum(f['kind']=='floor' for f in p['floor_support_features']),
        'floor_support_tab_width_mm':p['floor_support_tab_width'],
        'floor_support_original_span_mm':p['catch_tab_width'],
        'floor_support_centre_gap_mm':p['catch_tab_width']-2*p['floor_support_tab_width'],
        'floor_support_projection_mm':p['floor_support_projection'],
        'floor_support_features':p['floor_support_features'],
        'service_orientation':'CAD negative Y is up; wide T at top; bottom row bears on plywood',
        'receiver_continuous_inner_web_mm':p['snap_inner_web_height'],
        'selected_rail_latch':p.get('selected_rail_fit'),
        'receiver_geometry_unchanged':True,
        'screw_rail':p['screw_rail'],
        'screw_rail_positions':p['screw_rail_positions'],
        'latch_feedback':'User preferred clearance sample 37; full-assembly loading remains unverified',
        'lower_full_width_relief_mm':p['body_extension_height'],
        'upper_and_lower_cutout_radius_mm':p['opening_radius'],
        'middle_stop_from_outer_face_mm':[p['bank_depth'],p['bank_depth']+p['middle_stop_thickness']],
        'middle_stop_size_mm':[p['middle_stop_width'],p['rail_height'],p['middle_stop_thickness']],
        'rail_positions':p['rail_positions'], 'density_limits':p['density_limits'],
        'rail_batches':[p['rail_kinds'][i*p['rails_per_plate']:(i+1)*p['rails_per_plate']]
                        for i in range(p['rail_plate_count'])],
        'required_usable_plate_area_mm':[p['width_total'],p['height_total']],
        'corner_holes':p['corner_holes'], 'corner_hole_size':p['corner_hole_size'],
        'corner_hole_diameter_mm':2*oobb.gv('hole_radius_'+p['corner_hole_size'],'3dpr'),
        'corner_hole_inset_mm':p['corner_hole_inset'],
        'plywood_enclosure':'Size to this frame; plywood thickness and joinery are not included',
        'optional_joining_plates':p['joining_plates'],
        'joining_plates_file':'joining_plates.stl',
        'joining_plate_unit_gap_mm':p['joining_plate_unit_gap'],
        'joining_plate_countersink':{'size':'M3','top_diameter_mm':2*oobb.gv('screw_countersunk_radius_m3','3dpr'),
                                    'depth_mm':oobb.gv('screw_countersunk_depth_m3','3dpr')},
        'physical_fit':'Unverified PETG',
    },indent=2),encoding='utf-8')
    Path(folder,'printing.txt').write_text(
        'V6 double sided Systempak 209 / 100 ml drawer unit. Dimensions in mm.\n'
        f"{p['width_total']} x {p['height_total']} x {p['assembled_depth']} frame; {p['column']} columns x {p['row']} rows on EACH side, {p['drawer_count']} pots total.\n"
        'Screw adapters add 2.4 mm outside EACH face; finished plastic depth is 228.8 mm including them.\n'
        'front.stl and back.stl: print ONE each, outside face on bed; they are identical.\n'
        f"One-piece plates require {p['width_total']} x {p['height_total']} mm usable area, plus margins/brim.\n"
        + (f"Planning area: {p['bed_width']} x {p['bed_height']} mm, {p['bed_margin']} mm margins; printer: {p['printer']}.\n")
        + ("P1P: retain the 18 x 28 mm corner exclusion; do not add an unchecked brim.\n" if p['printer']=='P1P'
         else "Requires a larger printer; these one-piece plates exceed the P1P and A1 mini beds. No specific large printer is verified.\n")
        + 'The plates exceed the A1 mini bed. No tile seams or filler border are included.\n'
        'Four plain M3 clearance holes per plate, centres 5 mm from each adjacent outside edge.\n'
        'Use these eight holes to secure both plates to the surrounding plywood enclosure.\n'
        'Plywood thickness, joinery and screw length are user supplied; they are outside the CAD frame dimensions.\n'
        f"rails_plate_*.stl: print EVERY numbered batch once; total {p['bom']['snap_rail']} sample-37 snap rails and FOUR screw rails replacing four snaps.\n"
        'screw_adapters.stl: print ONCE for all EIGHT adapters, one per screw-rail end.\n'
        'snap_rail.stl, screw_rail.stl and screw_adapter.stl are individual spares, not extra kit quantities.\n'
        'screw_upgrade.stl contains FOUR screw rails and EIGHT adapters together, for upgrading an already printed all-snap cabinet. Do not print it in addition to the complete mixed rail batches.\n'
        'For a new unit print the mixed rail batches plus screw_adapters.stl; for a retrofit print ONLY screw_upgrade.stl.\n'
        'joining_plates.stl contains ONE four-unit joiner and ONE two-unit joiner together in the same print file.\n'
        'Both joiners are 6 mm thick, with M3 countersinks facing UP and flat backs on the bed.\n'
        'Four-unit plate: 20 x 20 mm, four holes on 10 x 10 mm centres. Two-unit plate: 20 x 10 mm, two holes 10 mm apart.\n'
        'Mount on the outside faces over existing cabinet corner holes. Rotate the two-unit plate 90 degrees for vertically adjacent units.\n'
        'Default spacing assumes touching plastic face edges; extra plywood spacing between units changes the required hole pitch.\n'
        'Joiners are optional accessories, excluded from the single-cabinet BOM and assembled reference. Supply M3 countersunk screws and matching backing/nuts.\n'
        'Face plates: 6 mm base web plus two 15 mm-wide floor tabs projecting 12 mm inward, 18 mm overall print depth.\n'
        'The original 56 mm stop span is split into two 15 mm tabs with a 26 mm central gap.\n'
        'Tabs have 45-degree bed-supported root slopes, flat bearing roofs beneath the drawer above, and tapered inner tips.\n'
        'The physical bottom drawer has no added floor extension; the plywood supplies its support.\n'
        'CAD negative Y is UP in service: the wide T is the TOP of each drawer. Preview rotation is corrected.\n'
        'Snap receivers retain a continuous 1 mm inner web; use the matching NEW rail bevels with these plates.\n'
        'The former 1 mm full-width lower cutout relief is removed; shoulder webs connect solidly to the floor crossbar.\n'
        'Upper and lower drawer-opening rectangles both use 1 mm corner radii.\n'
        f"Full-length rails now use selected latch sample {p['selected_latch_sample']} at BOTH ends: {p['selected_rail_fit']['hook_side_clearance']} mm hook-pocket side clearance and {p['selected_rail_fit']['axial_clearance']} mm end play.\n"
        'The face plates have been regenerated; receiving holes and plate geometry remain unchanged, compatible with existing plates.\n'
        'The 1.8 mm arms, spring roots, flush tips, middle stops and rail length remain unchanged. Print all updated rail batches for this unit.\n'
        'Rails lie on the long flat face, with their central stop wings supported on the bed.\n'
        '3dpr.stl is the complete kit overview and exceeds one bed. assembled.stl is reference only.\n'
        'Install the four screw rails at the outermost upper and lower rail positions, as shown in assembly.json. The plate holes are unchanged.\n'
        'Side-load ONE M3 nut into EACH end of the four screw rails BEFORE fitting the second plate (EIGHT nuts total). OOBB left clearance opens toward local +X.\n'
        'Place each adapter from the OUTSIDE of the plate, tapered cheeks into the existing snap hole, broad flange outside.\n'
        'Insert EIGHT M3 x 20 countersunk screws through the adapters and tighten into the beam nuts; the heads seat flush with the adapter faces.\n'
        'Nut pockets are 7-10 mm inward from each beam end; screws project 1.6 mm beyond them into a clearance bore.\n'
        'Snap the remaining sample-37 rails into the plates, then progressively seat the second plate.\n'
        'The adapters print flange outside face DOWN, countersinks on the bed and tapered guides UP. Their two substantial cheeks avoid fragile bore slivers.\n'
        'Screw rails print on the long flat face, as supplied. End bosses are 13 mm high around the side-loaded nuts.\n'
        'Remaining snap catches finish flush with the plate outside faces. The optional joiners use separate hardware.\n'
        'Each rail has an integral 3 mm middle stop, with wings extending into the pot body channel.\n'
        'Drawers enter from both faces and stop at opposite sides of the middle barrier.\n'
        'Retained outer catches resist pullout at both faces; lift trays past them as before.\n'
        'Inspect the 0.5 mm receiver lands and spring slots in the slicer.\n'
        'The user preferred sample 37 in the snap fit trial. The new screw adapter/rail fit and full-unit loading still need a physical PETG check.\n',
        encoding='utf-8')
