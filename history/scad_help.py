import copy
import oobb
import yaml
import os
import re
import working_scad
###### utilities


def cleanup_raw_scad_artifacts(folder):
    if not folder or not os.path.isdir(folder):
        return

    hex_pattern = re.compile(r"^(?P<stem>.+)_[0-9a-f]{16}\.scad$")
    referenced_helpers = {}

    for entry in os.listdir(folder):
        if not entry.endswith(".scad"):
            continue

        scad_path = os.path.join(folder, entry)
        try:
            with open(scad_path, "r", encoding="utf-8") as handle:
                contents = handle.read()
        except OSError:
            continue

        for match in re.finditer(r"use <([^>]+/(?P<stem_abs>[^/>]+)_[0-9a-f]{16}\.scad|(?P<stem_rel>[^/>]+)_[0-9a-f]{16}\.scad)>", contents):
            stem = match.group("stem_abs") or match.group("stem_rel")
            hashed_name = os.path.basename(match.group(1))
            referenced_helpers[stem] = hashed_name

        updated = re.sub(
            r"use <([^>]+/)?(?P<stem>[^/>]+)_[0-9a-f]{16}\.scad>",
            lambda m: f"use <{m.group('stem')}.scad>",
            contents,
        )
        if updated != contents:
            with open(scad_path, "w", encoding="utf-8") as handle:
                handle.write(updated)

    for stem, hashed_name in referenced_helpers.items():
        friendly_path = os.path.join(folder, f"{stem}.scad")
        hashed_path = os.path.join(folder, hashed_name)
        if not os.path.exists(friendly_path) and os.path.exists(hashed_path):
            with open(hashed_path, "r", encoding="utf-8") as src:
                contents = src.read()
            with open(friendly_path, "w", encoding="utf-8") as dst:
                dst.write(contents)

    for entry in os.listdir(folder):
        match = hex_pattern.match(entry)
        if not match:
            continue

        friendly_name = f"{match.group('stem')}.scad"
        friendly_path = os.path.join(folder, friendly_name)
        hashed_path = os.path.join(folder, entry)

        if os.path.exists(friendly_path):
            try:
                os.remove(hashed_path)
            except OSError:
                pass

def get_typ(**kwargs):
    typ = kwargs.get("typ", "")

    if typ == "":
        #setup
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    return typ


def get_build_variables(typ, filter=""):
    if typ == "all":
        return {
            "filter": "",
            "save_type": "all",
            "navigation": True,
            "overwrite": True,
            "modes": ["3dpr"],
            "oomp_run": True,
        }

    if typ == "fast":
        return {
            "filter": "",
            "save_type": "none",
            "navigation": True,
            "overwrite": True,
            "modes": ["3dpr"],
            "oomp_run": False,
        }

    if typ == "manual":
        return {
            "filter": "",
            #"filter": "test"
            "save_type": "none",
            #"save_type": "all"
            "navigation": True,
            #"navigation": False
            "overwrite": True,
            "modes": ["3dpr"],
            #"modes": ["3dpr", "laser", "true"]
            #"modes": ["laser"]
            "oomp_run": True,
            #"oomp_run": False
        }

    raise ValueError(f"Unknown typ: {typ}")


def get_navigation_sort(oobb_style=False):
    sort = []
    if oobb_style:
        #sort.append("extra")
        sort.append("oobb_name") 
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
    else:
        for i in range(1, 16):
            sort.append(f"taxonomy_{i}")
    return sort


def prepare_base_for_print(thing, pos, **kwargs):
    #put into a rotation object
    components_second = copy.deepcopy(thing["components"])
    return_value_2 = {}
    return_value_2["type"]  = "rotation"
    return_value_2["typetype"]  = "p"
    pos1 = copy.deepcopy(pos)
    pos1[0] += 50
    return_value_2["pos"] = pos1
    return_value_2["rot"] = [180,0,0]
    return_value_2["objects"] = components_second

    thing["components"].append(return_value_2)

    #add slice # top
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_slice"
    pos1 = copy.deepcopy(pos)
    pos1[0] += -500/2
    pos1[1] += 0
    pos1[2] += -500/2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb.append_full(thing,**p3)

def make_parts(**kwargs):
    parts = kwargs.get("parts", [])
    filter = kwargs.get("filter", "")
    #make the parts
    if True:
        for part in parts:
            oobb_name = part.get("oobb_name", "default")            
            extra = part["kwargs"].get("extra", "")
            if filter in oobb_name or filter in extra or filter in part["kwargs"].get("variant", ""):
                print(f"making {part['oobb_name']}")
                make_scad_generic(part)            
                
            else:
                print(f"skipping {part['oobb_name']}")
    

def make_scad_generic(part):
    
    # fetching variables
    oobb_name = part.get("oobb_name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{oobb_name}"

    thing = oobb.get_default_thing(**kwargs)
    thing.update(part)
    kwargs.pop("size","")

    #get the part from the function get_{oobb_name}"
    try:
        func = getattr(working_scad, f"get_{oobb_name}")
    except AttributeError:
        func = None
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        working_scad.get_base(thing, **kwargs)   

    oomp_mode = kwargs.get("oomp_mode", "project")
    
    if oomp_mode == "project":
        descmain = ""
        current_description_main = thing.get("description_main", "default")
        current_size = thing.get("size", "default")
        new_size = current_size.replace(f"{project_name}_", "")
        descmain = f"{new_size}_{current_description_main}"
        kwargs["oomp_description_main"] = f"{descmain}"
        descextra = ""
        current_description_extra = thing.get("description_extra", "")
        descextra = f"{current_description_extra}"
        kwargs["oomp_description_extra"] = f"{descextra}"
    elif oomp_mode == "oobb":
        current_description_main = thing.get("description_main", "default")   
        descmain = f"{current_description_main}" 

        descextra = thing.get("extra", "")    
        if descextra != "":
            descextra = f"{descextra}_extra"
        kwargs["oomp_description_main"] = f"{current_description_main}"
        kwargs["oomp_description_extra"] = f"{descextra}"
        kwargs["oomp_size"] = f"{part['oobb_name']}"

    #id = thing.get("oobb_id", "default")    
    

    #kwargs["description_main"] = id

    oomp_keys = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]
    oomp_id = part.get("id", "")
    if oomp_id == "":
        for key in oomp_keys:
            deet = part.get(key, "")
            deet = deet.replace(".","_")
            if deet != "":
                oomp_id += f"{deet}_"
        oomp_id = oomp_id[:-1]
    part["id"] = oomp_id
    folder = f"parts/{oomp_id}"

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        

        oobb.opsc_make_object(f'{folder}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)
        # Split frames have one catalogue folder with all useful drawing views.
        # Every file is built from working_scad inputs, never patched output CAD.
        if mode == "3dpr" and oobb_name in ["ai_version_2", "ai_version_3"] and kwargs.get("part_role", "frame") == "frame":
            thing["ai_files"] = {"3dpr": "Both halves flat and separated; use individual files if the pair exceeds the bed."}
            for view in ["front", "back", "assembled"]:
                view_thing = oobb.get_default_thing(type="split_frame_view")
                view_kwargs = {**copy.deepcopy(kwargs), "assembly_half": view}
                getattr(working_scad, f"get_{oobb_name}")(view_thing, **view_kwargs)
                oobb.opsc_make_object(f'{folder}/{view}.scad', view_thing["components"], mode="3dpr", save_type=save_type, overwrite=overwrite)
                thing["ai_files"][view] = view_thing["ai_design"]
            from pathlib import Path
            layout_fits = thing["ai_design"]["print_layout_fits_single_bed"]
            bed_note = ("The combined layout fits the declared bed including its margin."
                        if layout_fits else
                        "The combined layout exceeds the declared bed. Print front and back on separate plates using their individual files.")
            Path(folder, "printing.txt").write_text(
                "3dpr.scad: both halves flat, joint upward, separated on Z=0.\n"
                "front.scad: front half alone, print orientation.\n"
                "back.scad: back half alone, print orientation.\n"
                "assembled.scad: assembled reference only; do not print as one piece.\n"
                "Full export or the matching version validator writes matching STL files.\n\n"
                + bed_note + "\n", encoding="utf-8")
        if mode == "3dpr" and oobb_name == "ai_version_7":
            from working_scad_v7 import write_outputs
            write_outputs(folder, thing, kwargs, save_type, overwrite)
        if mode == "3dpr" and oobb_name == "ai_version_6":
            from working_scad_double_sided import write_outputs
            write_outputs(folder, thing, kwargs, save_type, overwrite)
        if mode == "3dpr" and oobb_name == "ai_version_4":
            from pathlib import Path
            import json
            p = working_scad.get_ai_version_4_parameters(**kwargs)
            views = working_scad.get_ai_version_4_views(p)
            thing["ai_files"] = {"3dpr": thing["ai_design"]}
            for filename, view in views.items():
                view_thing = oobb.get_default_thing(type="modular_view")
                working_scad.get_ai_version_4(view_thing, **dict(kwargs, modular_view=view))
                oobb.opsc_make_object(f'{folder}/{filename}.scad', view_thing["components"], mode="3dpr", save_type=save_type, overwrite=overwrite)
                thing["ai_files"][filename] = view_thing["ai_design"]
            Path(folder, "assembly.json").write_text(json.dumps({
                "bom": p["bom"], "views": views, "rail_length_mm": p["rail_length"],
                "plate_thickness_mm": p["plate_thickness"],
                "identical_face_plates": thing["ai_design"]["identical_front_and_back"],
                "front_lip": p["front_lip"], "rear_lip": p["rear_lip"],
                "nut_loading": p["nut_side_clearance"], "physical_fit": "Not yet printed",
            }, indent=2), encoding="utf-8")
            Path(folder, "printing.txt").write_text(
                "Version 4 modular drawer unit. All dimensions are millimetres.\n"
                "3dpr.scad: complete kit overview, all components on Z=0; it may exceed one bed.\n"
                "front.scad: print ONE front plate with its catch lip. face_plate.scad is the front alias.\n"
                "back.scad: print ONE rear plate without a catch lip; do not print two front plates.\n"
                "rail.scad: universal shelf/top/top-corner rail. bottom_rail.scad: reinforced bottom row.\n"
                "rails_plate_*.scad: bed-sized batches containing the exact rail quantities in assembly.json.\n"
                "assembled.scad: reference only. Face-fit 3dpr contains one front plate; back.scad is an optional rear fit test.\n"
                "Print rails on their long flat bearing faces, as generated. No standing long rails.\n"
                "Load M3 nuts sideways into both end pockets before fitting the second face plate.\n"
                "Seat the 3 mm pointed keys, then use M3 x 16 countersunk screws from the outside.\n"
                "Small horizontal screw bores and nut-slot roofs need short bridging; inspect the slicer.\n"
                "Trial joint_fit and face_fit first. Tray clearance, fit and loading need physical checks.\n",
                encoding="utf-8")
        if mode == "3dpr" and oobb_name == "ai_version_5" and kwargs.get("connector_design") == "tiled_hybrid":
            from working_scad_tiling import write_outputs
            write_outputs(folder, thing, kwargs, save_type, overwrite)
        if mode == "3dpr" and oobb_name == "ai_version_5" and kwargs.get("connector_design") != "tiled_hybrid":
            from pathlib import Path
            import json
            p = working_scad.get_ai_version_5_parameters(**kwargs)
            views = working_scad.get_ai_version_5_views(p)
            thing["ai_files"] = {"3dpr": thing["ai_design"]}
            for filename, view in views.items():
                view_thing = oobb.get_default_thing(type="connector_view")
                working_scad.get_ai_version_5(view_thing, **dict(kwargs, connector_view=view))
                oobb.opsc_make_object(f'{folder}/{filename}.scad', view_thing["components"], mode="3dpr", save_type=save_type, overwrite=overwrite)
                thing["ai_files"][filename] = view_thing["ai_design"]
            Path(folder, "connector_test.json").write_text(json.dumps({
                "design": p["connector_design"], "material": "PETG",
                "scope": "Connector coupons only; no v5 cabinet",
                "views": views, "inputs": {k:v for k,v in p.items() if k in __import__("working_oomp_populate").get_ai_version_5_defaults()},
                "insertion_deflection_mm": p["insertion_deflection"],
                "physical_test_status": "Not printed or load tested",
                "future_hybrid_connections": "Screw count/positions will be configurable after connector selection",
            }, indent=2), encoding="utf-8")
            Path(folder, "printing.txt").write_text(
                "VERSION 5 CONNECTOR TRIALS ONLY - PETG, mainly permanent locks.\n"
                "Print 3dpr.stl as arranged. All parts lie on Z=0; the suite fits an A1 mini bed.\n"
                "Suite positions: upper-left A single latch; upper-right B twin latch;\n"
                "lower-left C captive locking key; lower-right D existing screw reference.\n"
                "Individual records provide plate.stl, rail.stl and (C only) key.stl.\n"
                "assembled.stl is a reference, not a one-piece print.\n"
                "Start with a 0.4 mm nozzle, 0.2 mm layers, 4 walls, 100% infill for comparable small coupons.\n"
                "Use your established PETG temperatures and bed settings. No supports in spring gaps.\n"
                "A/B springs and C key bend in the bed plane. C rail has a short key-slot bridge.\n"
                "A/B: push rail into the matching plate until the end seats and hooks emerge outside.\n"
                "C: seat the rigid tongue, then insert the fork from the side until both hooks recover.\n"
                "D: one M3 x 16 countersunk screw and side-loaded M3 nut; opposite rail-end pocket unused.\n"
                "Do not confuse a snug friction fit with a locked hook: inspect recovered shoulders.\n"
                "See AI_VERSION_5_CONNECTOR_TESTS.md for the test sequence and results sheet.\n"
                "These are unverified candidates, not rated joints. No full v5 units are generated.\n",
                encoding="utf-8")
            if p.get("tight_key_trial",False):
                metadata=json.loads(Path(folder,"connector_test.json").read_text(encoding="utf-8"))
                metadata.update({
                    "sample_number":27,
                    "compatible_with":"Sample 22 beam and plate",
                    "key_latch_clearance_per_face_mm":p["key_latch_clearance"],
                    "head_bearing_x_mm":p["key_head_x"]+p["key_head_length"],
                    "latch_bearing_x_mm":p["key_shoulder_x"],
                    "total_key_axial_play_mm":2*p["key_latch_clearance"],
                    "screening_key_strain":p["estimated_key_strain"],
                })
                Path(folder,"connector_test.json").write_text(json.dumps(metadata,indent=2),encoding="utf-8")
                Path(folder,"printing.txt").write_text(
                    "SAMPLE 27 - TIGHTER SEPARATE LOCKING KEY, based on sample 22.\n"
                    "Print key.stl alone to use with your existing sample 22 beam and plate.\n"
                    "3dpr.stl contains one key plus a matching numbered beam and plate.\n"
                    "rail.stl and plate.stl differ from 22 only in their recessed number.\n"
                    "assembled.stl is an assembly reference, not a one-piece print.\n"
                    "Print in the supplied orientation: key flexes in the bed plane.\n"
                    "PETG; use the same slicer settings as your successful sample 22.\n"
                    "Seat the beam in the plate, then press the key sideways until both hooks recover.\n"
                    f"Head and hooks capture the tongue with {p['key_latch_clearance']:g} mm at each face.\n"
                    "The larger head stop and closer hooks reduce sideways key play; beam/plate and slot clearances are unchanged.\n"
                    "The shorter free arms will be stiffer. Inspect both recovered hooks; do not rely on friction alone.\n"
                    "No support inside the key fork; the beam retains its original short slot bridge.\n"
                    "CAD-checked only. Confirm insertion, retention and durability with a physical PETG print.\n",
                    encoding="utf-8")
            if p["connector_design"] == "recessed_twin_fit_suite":
                import csv
                trials = [{
                    "number":t["sample_number"],
                    "arm_thickness_mm":t["twin_arm_thickness"],
                    "clearance_per_side_mm":p["connector_clearance"],
                    "hook_projection_mm":p["hook_projection"],
                    "free_arm_length_mm":p["effective_arm_length"],
                    "centre_gap_mm":2*(p["snap_arm_outer"]-t["twin_arm_thickness"]),
                } for t in p["latch_trials"]]
                Path(folder,"connector_test.json").write_text(json.dumps({
                    "design":p["connector_design"],"material":"PETG","views":views,
                    "scope":"Four matched two-piece latch-arm thickness tests based on sample 19",
                    "trials":trials,"printable_pieces":8,
                    "physical_feedback":"User reports original sample 19 worked well; thicker trials untested",
                },indent=2),encoding="utf-8")
                with Path(folder,"trial_index.csv").open("w",newline="",encoding="utf-8") as output:
                    writer=csv.DictWriter(output,fieldnames=list(trials[0]))
                    writer.writeheader()
                    writer.writerows(trials)
                Path(folder,"printing.txt").write_text(
                    "PETG FLUSH TWIN-TAB ARM THICKNESS TRIALS, BASED ON 19\n"
                    "Print 3dpr.stl once: four numbered rails and four matching receivers.\n"
                    "Bed order: 23 24 / 25 26. Arm thicknesses: 1.0 / 1.2 / 1.4 / 1.6 mm.\n"
                    "23 is the sample-19 geometry control with a new number; 19 itself is unchanged.\n"
                    "Both parts are engraved 0.6 mm deep. Receivers have identical fit geometry.\n"
                    "trial_XX prints one pair; rail_XX and plate_XX are individual replacement parts.\n"
                    "assembled and assembled_XX are inspection references, not one-piece prints.\n"
                    "Keep the supplied poses: receiver ENTRY FACE DOWN, rail on its long flat face.\n"
                    "Use the same PETG, nozzle, layer height and wall settings as successful sample 19.\n"
                    "No supports in the spring slot or catch pocket. Inspect preservation of each arm in the slicer.\n"
                    "Only arm thickness and its rounded slot-end radius change; receiver, hook, length and clearances stay fixed.\n"
                    "Try 23 first, then 24, 25, 26. Use a fresh matched pair for each single-use insertion.\n"
                    "Confirm both hooks recover and the beam seats flush; note force, looseness and cracking/whitening.\n"
                    "Thicker arms may increase insertion force or break before seating; single use does not remove that risk.\n"
                    "No drawer units adopt these thicker arms yet. See RECESSED_TWIN_FIT_TESTS.md.\n",
                    encoding="utf-8")
            if p.get("variant") == "recessed_twin_heavy_suite":
                metadata=json.loads(Path(folder,"connector_test.json").read_text(encoding="utf-8"))
                metadata["physical_feedback"]="User reports 23 and 24 too narrow; 28 and 29 are untested thicker extensions"
                Path(folder,"connector_test.json").write_text(json.dumps(metadata,indent=2),encoding="utf-8")
                instructions=Path(folder,"printing.txt").read_text(encoding="utf-8")
                instructions=instructions.replace(
                    "Bed order: 23 24 / 25 26. Arm thicknesses: 1.0 / 1.2 / 1.4 / 1.6 mm.",
                    "Bed order: 25 26 / 28 29. Arm thicknesses: 1.4 / 1.6 / 1.8 / 2.0 mm.")
                instructions=instructions.replace(
                    "23 is the sample-19 geometry control with a new number; 19 itself is unchanged.",
                    "25 and 26 are unchanged controls. 27 is the separate-key design and is not in this bed.")
                instructions=instructions.replace("Try 23 first, then 24, 25, 26.","Try 25 first, then 26, 28, 29.")
                Path(folder,"printing.txt").write_text(instructions,encoding="utf-8")
            if p["connector_design"] == "snap_recessed_twin":
                Path(folder, "printing.txt").write_text(
                    "19: RECESSED TWO-TAB PUSH-IN CONNECTOR - PETG, mainly permanent.\n"
                    "Print 3dpr.stl: one rail and one matching rectangular receiver.\n"
                    "plate.stl and rail.stl are separate print-ready parts; assembled.stl is reference only.\n"
                    "Keep the supplied orientation: receiver ENTRY FACE DOWN, rail on its long flat face.\n"
                    "The larger catch pocket prints above the entry throat, avoiding a hanging ledge.\n"
                    "Recessed 19 marks the print-top faces. There is no central guide or separate key.\n"
                    "Push both tabs through the smaller rectangular entry until the full-width beam seats directly against the plate.\n"
                    "Hooks recover into the wider pocket; both square catches remain inside the 7.5 mm receiver.\n"
                    "Inspect recovery through the larger outside opening. Hook tips finish flush with that front face.\n"
                    "Short tabs: 1.0 mm walls, 6 mm free length to the catches, 1.5 mm lead-in; no exposed neck behind the receiver.\n"
                    "1.2 mm hooks, nominal 0.95 mm inward flex per tab, 0.25 mm side clearance and 0.2 mm axial catch clearance.\n"
                    "Use the same PETG profile as the earlier coupons. Inspect the slicer for preserved tab walls.\n"
                    "Record seating effort, play, whitening, hook recovery and retention before selecting a cabinet joint.\n"
                    "This aggressive coupon is untested physically; no force or load rating is established.\n"
                    "See RECESSED_TWIN_TAB_TEST.md.\n",encoding="utf-8")
                metadata=json.loads(Path(folder,"connector_test.json").read_text(encoding="utf-8"))
                metadata.update(sample_number=19,receiver_shoulder_z_mm=p["receiver_shoulder_z"],
                                hook_tip_inside_outer_face_mm=p["plate_thickness"]+p["hook_tip_z"],
                                central_guide=False,receiver_print_pose="entry_face_down")
                Path(folder,"connector_test.json").write_text(json.dumps(metadata,indent=2),encoding="utf-8")
            if p["connector_design"] == "key_size_fit_suite":
                import csv
                trials = []
                for inputs in p["key_trials"]:
                    trial = working_scad.get_ai_version_5_parameters(
                        **{**p, **inputs, "connector_design":"snap_key"})
                    trials.append({
                        "number": trial["sample_number"],
                        "key_scale": trial["key_scale"],
                        "clearance_per_side_mm": trial["connector_clearance"],
                        "through_clearance_per_side_mm": trial["through_clearance"],
                        "through_seat_interference_per_side_mm": trial.get("through_seat_interference",0),
                        "through_taper_length_mm": trial.get("through_taper_length",0),
                        "key_length_mm": round(trial["key_shoulder_x"]+trial["hook_ramp_length"]-trial["key_head_x"],6),
                        "key_height_mm": trial["key_height"],
                        "arm_thickness_mm": trial["key_arm_thickness"],
                        "nominal_deflection_mm": round(trial["insertion_deflection"],6),
                        "rail_number_depth_mm": trial["number_depth"],
                    })
                Path(folder, "connector_test.json").write_text(json.dumps({
                    "design":p["connector_design"], "material":"PETG",
                    "scope":f"{len(trials)} numbered connector fit coupons; no drawer units",
                    "printable_pieces":3*len(trials), "views":views, "trials":trials,
                    "physical_test_status":"Not printed or load tested",
                },indent=2),encoding="utf-8")
                with Path(folder, "trial_index.csv").open("w",newline="",encoding="utf-8") as output:
                    writer = csv.DictWriter(output,fieldnames=list(trials[0]))
                    writer.writeheader(); writer.writerows(trials)
                through_suite = "through_taper_length" in p["key_trials"][0]
                matrix_instructions = (
                    "THROUGH-PIECE TAPER TRIALS: numbers 10 11 12 / 13 14 15 / 16 17 18.\n"
                    "Rows: 0.10, 0.20, 0.30 mm entry clearance PER SIDE in X.\n"
                    "Columns: 0.025 mm clearance, 0.025 mm interference, 0.050 mm interference PER SIDE in X.\n"
                    "Negative interference in trial_index.csv means clearance.\n"
                    "Each tongue widens gently over the final 6 mm inside the plate. Y clearance stays 0.25 mm per side.\n"
                    "All keys match sample 5 (115% size, 0.30 mm key slot clearance). Compare through fit before inserting the key.\n"
                    "Interference is deliberate CAD overlap, not a guarantee of physical tightness or strength.\n"
                    if through_suite else
                    "KEY TRIALS: numbers 1 2 3 / 4 5 6 / 7 8 9.\n"
                    "Rows: 100%, 115%, 130% key size. Columns: 0.20, 0.30, 0.40 mm key slot clearance PER SIDE.\n"
                    "Straight through-piece fit stays at 0.25 mm per side for this bed.\n"
                    "Original key size is 100%; its earlier slot clearance was 0.25 mm, between trials 1 and 2.\n"
                )
                if p["variant"] == "key_size_extension_suite":
                    matrix_instructions = (
                        "SIZE EXTENSION: 20 = 145%, 21 = 160%, 22 = 175% of the original key.\n"
                        "Continues 3 / 6 / 9 = 100% / 115% / 130%, keeping sample 9's 0.40 mm per-side key slot clearance.\n"
                        "Through fit stays 0.25 mm per side; axial catch clearance stays 0.2 mm.\n"
                        "User feedback: sample 9 closest but still loose, sample 1 much too loose.\n"
                        "This changes size/stiffness, not nominal clearance gaps. Print each complete matched set.\n"
                        "The largest slot leaves 1.1 mm above/below within the unchanged 11 x 10 mm rail; inspect these walls in the slicer.\n"
                        "See KEY_SIZE_EXTENSION_TESTS.md for the number/settings table and fit notes.\n"
                    )
                Path(folder, "printing.txt").write_text(
                    "NUMBERED LOCKING-KEY SIZE AND CLEARANCE TRIALS - PETG\n"
                    f"Print 3dpr.stl as arranged: {len(trials)} rail/plate/key sets, {3*len(trials)} pieces, one A1 mini bed.\n"
                    +matrix_instructions+
                    "Each long rail has its number recessed 0.6 mm into its top face; its receiver plate has the same number.\n"
                    "Keep each loose key next to its numbered pair until testing. Keys have no number to avoid weakening them.\n"
                    "trial_XX.stl prints an individual numbered three-piece set. rail_XX / plate_XX / key_XX are separate parts.\n"
                    "assembled and assembled_XX are reference views, not one-piece prints.\n"
                    "All rails retain an 11 x 10 mm section. Key geometry and matching tongues/slots change size.\n"
                    "Axial catch clearance remains 0.2 mm in all trials.\n"
                    "Use the same PETG profile for all: suggested starting point 0.4 mm nozzle, 0.2 mm layers, 4 walls, 100% infill.\n"
                    "Keep the supplied orientation. Avoid supports/brims in slots; inspect the short slot bridges in the slicer.\n"
                    "Press the tongue into the plate, then insert the key sideways until both catches recover.\n"
                    "Record the recessed number with insertion effort, play and retention. See trial_index.csv and KEY_SIZE_FIT_TESTS.md.\n",
                    encoding="utf-8")
        cleanup_raw_scad_artifacts(folder)
        


    yaml_file = f"{folder}/working.yaml"
    #partial dump
    with open(yaml_file, 'w') as file:
        part_new = copy.deepcopy(part)
        kwargs_new = part_new.get("kwargs", {})
        kwargs_new.pop("save_type","")
        part_new["kwargs"] = kwargs_new
        import os
        cwd = os.getcwd()
        part_new["project_name"] = cwd
        part_new["id_oobb"] = thing["id"]
        #part_new["thing"] = thing
        part_new.pop("thing", "")
        yaml.dump(part_new, file)
    
    #full dump
    yaml_file = f"{folder}/thing.yaml"
    with open(yaml_file, 'w') as file:
        part_new = copy.deepcopy(part)
        kwargs_new = part_new.get("kwargs", {})
        kwargs_new.pop("save_type","")
        part_new["kwargs"] = kwargs_new
        import os
        cwd = os.getcwd()
        part_new["project_name"] = cwd
        part_new["id_oobb"] = thing["id"]
        part_new["thing"] = thing
        yaml.dump(part_new, file)


    print(f"done {oomp_id}")

def generate_navigation(folder="parts", sort=["width", "height", "thickness"]):
    #crawl though all directories in scad_output and load all the working.yaml files
    parts = {}
    for root, dirs, files in os.walk(folder):
        if 'working.yaml' in files:
            yaml_file = os.path.join(root, 'working.yaml')
            #if working.yaml isn't in the root directory, then do it
            if root != folder:
                with open(yaml_file, 'r') as file:
                    part = yaml.safe_load(file)
                    # Process the loaded YAML content as needed
                    part["folder"] = root
                    part_name = root.replace(f"{folder}","")
                    
                    #remove all slashes
                    part_name = part_name.replace("/","").replace("\\","")
                    parts[part_name] = part

                    print(f"Loaded {yaml_file}")

    pass
    
    for part_id in parts:
        if part_id != "":
            part = parts[part_id]

            # Purchased catalogue records have no drawing kwargs, but belong
            # in navigation too. Include manufacturer/MPN to prevent collisions.
            if isinstance(part, dict):
                kwarg_copy = copy.deepcopy(part.get("kwargs", {}))
                folder_navigation = "navigation_oobb"
                folder_source = part["folder"]
                folder_extra = ""
                for s in sort:
                    if s == "oobb_name":
                        ex = part.get("oobb_name", "default")
                    else:                        
                        ex = kwarg_copy.get(s, "default")
                        if ex == "default":
                            ex = part.get(s, "default")
                        #if ex is a list
                        if isinstance(ex, list):
                            ex_string = ""
                            for e in ex:
                                ex_string += f"{e}_"
                            ex = ex_string[:-1]
                            ex = ex.replace(".","d")                            
                    if ex != "default" and ex != "":
                        if "taxonomy_" in s:
                            folder_extra += f"{ex}/"
                        else:
                            folder_extra += f"{s}_{ex}/"

                #replace "." with d
                folder_extra = folder_extra.replace(".","d")            
                folder_destination = f"{folder_navigation}/{folder_extra}"
                if not os.path.exists(folder_destination):
                    os.makedirs(folder_destination)
                # Python handles the long taxonomy/batch paths that xcopy
                # reports as "Insufficient memory" on Windows. Propagate errors.
                import shutil
                shutil.copytree(folder_source,folder_destination,dirs_exist_ok=True)
                cleanup_raw_scad_artifacts(folder_destination)

