
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []
    
    

    options = get_ai_version_1_options() + get_ai_version_2_options() + get_ai_version_3_options() + get_ai_version_4_options() + get_ai_version_5_options()

    #load from working_manual.yaml
    if False:
        with open("working_manual.yaml", 'r', encoding='utf-8') as file:
            import yaml
            data = yaml.safe_load(file)
            options_yaml = data.get("options", [])
            for option_yaml in options_yaml:
                options.append(option_yaml)

    
    ###### populate taxonomy details and oobb details
    if True:          
        for option in options:  
                option["taxonomy_1"] = "oobb"
                option["taxonomy_2"] = f"organization"  
                option["taxonomy_3"] = f"storage"             
                option["taxonomy_4"] = f"drawer_unit"                         
                value_name = "column"
                value = option.get(value_name, None)
                option["taxonomy_5"] = f"{value}_{value_name}"
                value_name = "row"
                value = option.get(value_name, None)
                option["taxonomy_6"] = f"{value}_{value_name}"
                value_name = "container_short"
                value = option.get(value_name, None)
                option["taxonomy_7"] = f"{value}_{value_name.replace('_short', '')}"                        
                value_name = "style"
                value = option.get(value_name, None)
                option["taxonomy_8"] = f"{value}_{value_name}"
                if option.get("variant"):
                    option["taxonomy_9"] = option["variant"]
                #oobb details
                if True:
                    pass
                    oobb_details = {}
                    #taxonomy_5 hole_cover
                    value_name = "style"
                value = option.get(value_name, None)
                oobb_details["oobb_name"] = value
                oobb_details.update(option)
                option["oobb_details"] = oobb_details
                #svg details
                if False:
                    pass
                    svg_details = {}
                    svg_details["svg_name"] = option_type
                    svg_details["svg_width"] = option.get("width", None)            
                    svg_details["svg_height"] = option.get("height", None)
                    option["svg_details"] = svg_details

    #load the options into full list
    extras = []
    for option in options:
        extra = {}
        extra.update(option)
        extras.append(extra)

    
    # Purchased drawer units have their own explicit taxonomy and no CAD inputs.
    # The research module returns only entries approved by the user.
    import working_oomp_populate_purchased
    extras.extend(working_oomp_populate_purchased.main(**kwargs))

    ######### add notes from an id string
    import working_oomp_populate_extra_detail
    working_oomp_populate_extra_detail.main(extras=extras)


    import working_oomp_populate_comparison
    working_oomp_populate_comparison.enrich(extras)
    write_extras(extras)



def get_ai_version_1_options():
    # Frozen release options, including the unchanged basic reference models.
    options = []
    if True:
        styles = ["basic","ai_version_1"]
        sizes = []
        sizes.append([1,1])
        sizes.append([2,2])
        for style in styles:
            for size in sizes:
                option = {}
                option["container"] = "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209"
                option["container_short"] = "rectangle_100_ml_tamper_evident_systempak_209"
                option["column"] = size[0]
                option["row"] = size[1]
                option["style"] = style
                if style == "ai_version_1":
                    option.update(get_ai_version_1_defaults())
                options.append(copy.deepcopy(option))

        # AI experiments are ordinary OOMP parts, including the small test prints.
        ai_template = next(o for o in options if o["style"] == "ai_version_1")
        experiments = [
            {"column": 4, "row": 12},
            # Largest face-down grids retaining the current clearance, ears and
            # 2 mm edge margin. Build volumes verified against Bambu specs.
            {"column": 1, "row": 4, "variant": "a1_mini_max",
             "printer": "Bambu Lab A1 mini", "bed_width": 180.0,
             "bed_height": 180.0, "build_height": 180.0},
            {"column": 2, "row": 7, "variant": "p1p_max",
             "printer": "Bambu Lab P1P", "bed_width": 256.0,
             "bed_height": 256.0, "build_height": 256.0},
            {"column": 2, "row": 2, "variant": "solid_reference", "lightening": False},
            {"column": 4, "row": 12, "variant": "layout", "part_role": "layout", "test_depth": 7.5},
            {"column": 2, "row": 2, "variant": "bank_layout", "part_role": "bank_layout", "test_depth": 7.5},
        ]
        # Clearance remains adjustable in defaults; no clearance-specific records.
        for experiment in experiments:
            option = copy.deepcopy(ai_template)
            option.update(experiment)
            options.append(option)

        # Systempak 214 shares the 209 lip profile but has a taller body.
        # Keep a separate mini variant even though its maximum is also 1 x 1.
        for experiment in [
            {"column": 1, "row": 1},
            {"column": 1, "row": 1, "variant": "a1_mini_max",
             "printer": "Bambu Lab A1 mini", "bed_width": 180.0,
             "bed_height": 180.0, "build_height": 180.0},
            {"column": 2, "row": 2, "variant": "p1p_max",
             "printer": "Bambu Lab P1P", "bed_width": 256.0,
             "bed_height": 256.0, "build_height": 256.0},
        ]:
            option = copy.deepcopy(ai_template)
            option["container"] = "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214"
            option["container_short"] = "rectangle_550_ml_tamper_evident_systempak_214"
            option["opening_height_extra"] = 1.5  # Extra vertical space per drawer before the v1 release.
            option.update(experiment)
            options.append(option)
    return options


def get_ai_version_2_options():
    # Released version 2 options; future refinement belongs in version 3.
    options = []
    if True:
        styles = ["ai_version_2"]
        sizes = []
        sizes.append([1,1])
        sizes.append([2,2])
        for style in styles:
            for size in sizes:
                option = {}
                option["container"] = "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209"
                option["container_short"] = "rectangle_100_ml_tamper_evident_systempak_209"
                option["column"] = size[0]
                option["row"] = size[1]
                option["style"] = style
                if style == "ai_version_2":
                    option.update(get_ai_version_2_defaults())
                options.append(copy.deepcopy(option))

        # AI experiments are ordinary OOMP parts, including the small test prints.
        ai_template = next(o for o in options if o["style"] == "ai_version_2")
        experiments = [
            {"column": 4, "row": 12},
            # Largest face-down grids retaining the current clearance, ears and
            # 2 mm edge margin. Build volumes verified against Bambu specs.
            {"column": 1, "row": 4, "variant": "a1_mini_max",
             "printer": "Bambu Lab A1 mini", "bed_width": 180.0,
             "bed_height": 180.0, "build_height": 180.0},
            {"column": 2, "row": 7, "variant": "p1p_max",
             "printer": "Bambu Lab P1P", "bed_width": 256.0,
             "bed_height": 256.0, "build_height": 256.0},
            {"column": 2, "row": 2, "variant": "solid_reference", "lightening": False},
            {"column": 4, "row": 12, "variant": "layout", "part_role": "layout", "test_depth": 7.5},
            {"column": 2, "row": 2, "variant": "bank_layout", "part_role": "bank_layout", "test_depth": 7.5},
        ]
        # Clearance remains adjustable in defaults; no clearance-specific records.
        for experiment in experiments:
            option = copy.deepcopy(ai_template)
            option.update(experiment)
            options.append(option)

        # Systempak 214 shares the 209 lip profile but has a taller body.
        # Keep a separate mini variant even though its maximum is also 1 x 1.
        for experiment in [
            {"column": 1, "row": 1},
            {"column": 1, "row": 1, "variant": "a1_mini_max",
             "printer": "Bambu Lab A1 mini", "bed_width": 180.0,
             "bed_height": 180.0, "build_height": 180.0},
            {"column": 2, "row": 2, "variant": "p1p_max",
             "printer": "Bambu Lab P1P", "bed_width": 256.0,
             "bed_height": 256.0, "build_height": 256.0},
        ]:
            option = copy.deepcopy(ai_template)
            option["container"] = "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214"
            option["container_short"] = "rectangle_550_ml_tamper_evident_systempak_214"
            option["opening_height_extra"] = 1.5  # Extra vertical space per drawer before the v1 release.
            option.update(experiment)
            options.append(option)
    # Front/back are files inside each main part folder, not catalogue records.
    part = copy.deepcopy(ai_template)
    part.update(variant="joint_fit", joint_test_depth=24.0,
                lightening=False, adhesion_ears=False)
    options.append(part)
    return options


def get_ai_version_1_defaults():
    # Starting values for physical trials, not calibrated material properties.
    # Keep all editable design inputs in population and pass via oobb_details.
    return {
        "part_role": "frame",
        "container_clearance": 1.5,
        "opening_height_extra": 0.0,
        "thickness_wall": 1.8,
        "drawer_border_edge": 2.4,
        "depth_clearance": 1.5,
        "opening_radius": 4.0,
        "outer_radius": 2.4,
        "front_band": 7.5,  # Retain the complete 6 mm catch ramp and 1.5 mm tip.
        "rear_band": 6.0,
        "runner_width": 10.0,
        "middle_rib_width": 0.0,
        "depth_lip": 12.0,  # Height of the user's full-width part of the opening.
        "inset_lip": 5.5,  # Retain the user's stepped profile on each side.
        "lip_cutout_radius": 1.0,
        "lip_shelf_thickness": 3.0,  # Continuous material above the step.
        "lip_support_reference_height": 26.0,  # Limit shoulders to the 100 ml lidless body height.
        "side_rail_width": 5.0,
        "roof_slope": 1.0,  # rise/run; 1 means a 45-degree closing roof
        "lightening": True,
        "catch_tab_width": 56.0,
        "catch_tab_height": 6.0,
        "catch_tab_ramp_depth": 6.0,
        "catch_tab_depth": 1.5,
        "adhesion_ears": True,
        "ear_diameter": 20.0,
        "ear_height": 0.6,
        "ear_gap": 0.5,
        "ear_link_width": 5.0,
        "ear_link_height": 0.3,
        "module_gap": 0.4,
        "bed_width": 400.0,
        "bed_height": 400.0,
        "bed_margin": 2.0,  # Margin outside the complete footprint, including ears.
    }


def get_ai_version_2_defaults():
    # Starting values for physical trials, not calibrated material properties.
    # Keep all editable design inputs in population and pass via oobb_details.
    return {
        "part_role": "frame",
        "assembly_half": "print_layout",  # Both halves flat in the main 3dpr file.
        "print_layout_gap": 8.0,  # Separation includes the removable ears.
        "interlock_depth": 3.0,
        "interlock_width": 8.0,
        "interlock_height": 7.0,
        "corner_interlock_diameter": 2.8,  # Locating peg at every unscrewed grid junction.
        "corner_interlock_min_wall": 0.6,  # Minimum material outside the socket.
        "interlock_clearance": 0.25,  # Per side in XY.
        "interlock_end_clearance": 0.2,
        "screw_length": 16.0,
        "screw_head_seat_offset": 6.0,  # In front of the centre joint.
        "hardware_axis_height": 5.0,  # Above the lip step.
        "hardware_min_wall": 1.2,
        "container_clearance": 1.5,
        "opening_height_extra": 0.0,
        "thickness_wall": 1.8,
        "drawer_border_edge": 5.5,
        "depth_clearance": 1.5,
        "opening_radius": 4.0,
        "outer_radius": 2.4,
        "front_band": 7.5,  # Retain the complete 6 mm catch ramp and 1.5 mm tip.
        "rear_band": 6.0,
        "runner_width": 10.0,
        "middle_rib_width": 0.0,
        "depth_lip": 12.0,  # Height of the user's full-width part of the opening.
        "inset_lip": 5.5,  # Retain the user's stepped profile on each side.
        "lip_cutout_radius": 1.0,
        "lip_shelf_thickness": 10.0,  # Continuous material above the step.
        "lip_support_reference_height": 26.0,  # Limit shoulders to the 100 ml lidless body height.
        "side_rail_width": 4.0,
        "roof_slope": 1.0,  # rise/run; 1 means a 45-degree closing roof
        "lightening": True,
        "catch_tab_width": 56.0,
        "catch_tab_height": 6.0,
        "catch_tab_ramp_depth": 6.0,
        "catch_tab_depth": 1.5,
        "adhesion_ears": True,
        "ear_diameter": 16.0,
        "ear_height": 0.6,
        "ear_gap": 0.5,
        "ear_link_width": 5.0,
        "ear_link_height": 0.3,
        "module_gap": 0.4,
        "bed_width": 400.0,
        "bed_height": 400.0,
        "bed_margin": 2.0,  # Margin outside the complete footprint, including ears.
    }


# Call main automatically

# Version 3: independent development copy of the locked version 2 release.

def get_ai_version_3_options():
    # Development options: independent copy of the version 2 release.
    options = []
    if True:
        styles = ["ai_version_3"]
        sizes = []
        sizes.append([1,1])
        sizes.append([2,2])
        for style in styles:
            for size in sizes:
                option = {}
                option["container"] = "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209"
                option["container_short"] = "rectangle_100_ml_tamper_evident_systempak_209"
                option["column"] = size[0]
                option["row"] = size[1]
                option["style"] = style
                if style == "ai_version_3":
                    option.update(get_ai_version_3_defaults())
                options.append(copy.deepcopy(option))

        # AI experiments are ordinary OOMP parts, including the small test prints.
        ai_template = next(o for o in options if o["style"] == "ai_version_3")
        experiments = [
            {"column": 4, "row": 12},
            # Largest face-down grids retaining the current clearance, ears and
            # 2 mm edge margin. Build volumes verified against Bambu specs.
            {"column": 1, "row": 4, "variant": "a1_mini_max",
             "printer": "Bambu Lab A1 mini", "bed_width": 180.0,
             "bed_height": 180.0, "build_height": 180.0},
            {"column": 2, "row": 7, "variant": "p1p_max",
             "printer": "Bambu Lab P1P", "bed_width": 256.0,
             "bed_height": 256.0, "build_height": 256.0},
            {"column": 2, "row": 2, "variant": "solid_reference", "lightening": False},
            {"column": 4, "row": 12, "variant": "layout", "part_role": "layout", "test_depth": 7.5},
            {"column": 2, "row": 2, "variant": "bank_layout", "part_role": "bank_layout", "test_depth": 7.5},
        ]
        # Clearance remains adjustable in defaults; no clearance-specific records.
        for experiment in experiments:
            option = copy.deepcopy(ai_template)
            option.update(experiment)
            options.append(option)

        # Systempak 214 shares the 209 lip profile but has a taller body.
        # Keep a separate mini variant even though its maximum is also 1 x 1.
        for experiment in [
            {"column": 1, "row": 1},
            {"column": 1, "row": 1, "variant": "a1_mini_max",
             "printer": "Bambu Lab A1 mini", "bed_width": 180.0,
             "bed_height": 180.0, "build_height": 180.0},
            {"column": 2, "row": 2, "variant": "p1p_max",
             "printer": "Bambu Lab P1P", "bed_width": 256.0,
             "bed_height": 256.0, "build_height": 256.0},
        ]:
            option = copy.deepcopy(ai_template)
            option["container"] = "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214"
            option["container_short"] = "rectangle_550_ml_tamper_evident_systempak_214"
            option["opening_height_extra"] = 1.5  # Extra vertical space per drawer before the v1 release.
            option.update(experiment)
            options.append(option)
    # Front/back are files inside each main part folder, not catalogue records.
    part = copy.deepcopy(ai_template)
    part.update(variant="joint_fit", joint_test_depth=24.0,
                lightening=False, adhesion_ears=False)
    options.append(part)
    return options


def get_ai_version_3_defaults():
    # Starting values for physical trials, not calibrated material properties.
    # Keep all editable design inputs in population and pass via oobb_details.
    return {
        "remove_internal_lower_supports": True,  # Keep only the top/bottom unscrewed rails.
        "part_role": "frame",
        "assembly_half": "print_layout",  # Both halves flat in the main 3dpr file.
        "print_layout_gap": 8.0,  # Separation includes the removable ears.
        "interlock_depth": 3.0,
        "interlock_width": 8.0,
        "interlock_height": 7.0,
        "corner_interlock_diameter": 2.8,  # Locating peg at every unscrewed grid junction.
        "corner_interlock_min_wall": 0.6,  # Minimum material outside the socket.
        "interlock_clearance": 0.25,  # Per side in XY.
        "interlock_end_clearance": 0.2,
        "screw_length": 16.0,
        "screw_head_seat_offset": 6.0,  # In front of the centre joint.
        "hardware_axis_height": 5.0,  # Above the lip step.
        "hardware_min_wall": 1.2,
        "container_clearance": 1.5,
        "opening_height_extra": 0.0,
        "thickness_wall": 1.8,
        "drawer_border_edge": 5.5,
        "depth_clearance": 1.5,
        "opening_radius": 4.0,
        "outer_radius": 2.4,
        "front_band": 7.5,  # Retain the complete 6 mm catch ramp and 1.5 mm tip.
        "rear_band": 6.0,
        "runner_width": 10.0,
        "middle_rib_width": 0.0,
        "depth_lip": 12.0,  # Height of the user's full-width part of the opening.
        "inset_lip": 5.5,  # Retain the user's stepped profile on each side.
        "lip_cutout_radius": 1.0,
        "lip_shelf_thickness": 10.0,  # Full reinforcement at the mating joint.
        "running_shelf_thickness": 4.0,  # Nominal rail above the bearing step away from the joint.
        "hardware_boss_band": 12.0,  # Full thickness around recessed hardware and interlocks.
        "hardware_boss_slope": 1.2,  # Print-height rise per mm of outward growth (about 50 degrees).
        "lip_support_reference_height": 26.0,  # Limit shoulders to the 100 ml lidless body height.
        "side_rail_width": 4.0,
        "roof_slope": 1.0,  # rise/run; 1 means a 45-degree closing roof
        "lightening": True,
        "catch_tab_width": 56.0,
        "catch_tab_height": 6.0,
        "catch_tab_ramp_depth": 6.0,
        "catch_tab_depth": 1.5,
        "adhesion_ears": True,
        "ear_diameter": 16.0,
        "ear_height": 0.6,
        "ear_gap": 0.5,
        "ear_link_width": 5.0,
        "ear_link_height": 0.3,
        "module_gap": 0.4,
        "bed_width": 400.0,
        "bed_height": 400.0,
        "bed_margin": 2.0,  # Margin outside the complete footprint, including ears.
    }


def get_ai_version_4_options():
    # Independent editable options; frozen v3 is only the initial size catalogue.
    options = []
    for original in get_ai_version_3_options():
        if original.get("variant") in ["solid_reference", "layout", "bank_layout", "joint_fit"]:
            continue
        option = copy.deepcopy(original)
        option.update(get_ai_version_4_defaults())
        option["style"] = "ai_version_4"
        options.append(option)
    trial = copy.deepcopy(options[0])
    trial.update(variant="joint_fit", part_role="modular_test", joint_test_depth=45.0,
                 adhesion_ears=False, lightening=False)
    options.append(trial)
    for code in ["209", "214"]:
        trial = copy.deepcopy(next(o for o in options if o["column"] == o["row"] == 1
                                  and o["container"].endswith(code)))
        trial.update(variant="face_fit", part_role="face_fit")
        options.append(trial)
    return options


def get_ai_version_4_defaults():
    return {
        "front_lip": True,
        "rear_lip": False,
        "part_role": "frame",
        "modular_view": "print_layout",
        "plate_thickness": 7.5,
        "drawer_border_edge": 10.5,  # Houses the same rail at top corners.
        "ear_diameter": 12.0,  # Preserves 1x4/2x7/4x12 bed envelopes.
        "rail_width": 11.0,
        "rail_height": 10.0,
        "rail_running_height": 4.0,
        "bottom_rail_running_height": 6.0,
        "rail_end_band": 12.0,
        "rail_taper_run": 7.2,
        "rail_layout_gap": 5.0,
        "rail_edge_gap": 0.25,
        "modular_key_depth": 3.0,
        "modular_key_clearance": 0.25,
        "modular_key_end_clearance": 0.2,
        "modular_screw_length": 16.0,
        "nut_side_clearance": "left",  # OOBB's left opens toward local +X.
        "nut_axis_height": 5.0,
        "inner_guide_depth": 6.0,  # Reverse slope on the back of the catch.
    }


def get_ai_version_5_defaults():
    # Connector trials ONLY. No v5 cabinet or screw/snap allocation yet.
    return {
        "part_role": "connector_test",
        "connector_view": "print_layout",
        "test_material": "PETG",
        "connection_intent": "mainly_permanent",
        "plate_thickness": 7.5,
        "coupon_width": 15.0,
        "coupon_height": 14.0,
        "rail_width": 11.0,
        "rail_height": 10.0,
        "test_rail_length": 32.0,
        "connector_clearance": 0.25,  # Per side; no clearance taxonomy/variants.
        "catch_end_clearance": 0.2,
        "hook_projection": 0.65,
        "hook_ramp_length": 2.4,
        "snap_arm_height": 4.0,
        "snap_arm_outer": 3.8,
        "single_arm_thickness": 1.6,
        "single_root_distance": 8.0,
        "twin_arm_thickness": 1.4,
        "twin_root_distance": 12.0,
        "root_radius": 1.1,  # Overlaps the spine at the root; avoids a tangent-only edge.
        "guide_half_width": 1.4,
        "guide_depth": 3.0,
        "key_arm_thickness": 0.8,
        "key_root_radius": 0.4,
        "key_half_width": 1.4,
        "key_height": 4.0,
        "key_head_x": -5.7,
        "key_shoulder_x": 2.7,
        "key_tongue_half_width": 2.5,
        "bed_width": 180.0,
        "bed_height": 180.0,
        "bed_margin": 2.0,
    }


def get_ai_version_5_options():
    template = {
        **get_ai_version_5_defaults(),
        "container": "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209",
        "container_short": "rectangle_100_ml_tamper_evident_systempak_209",
        "column": 1, "row": 1, "style": "ai_version_5",
    }
    options = [
        {**copy.deepcopy(template), "variant": name, "connector_design": name}
        for name in ["snap_single", "snap_twin", "snap_key", "screw_reference", "connector_suite"]
    ]
    options.append({
        **copy.deepcopy(template),
        "variant": "key_size_fit_suite",
        "connector_design": "key_size_fit_suite",
        "key_trials": get_ai_version_5_key_trials(),
    })
    options.append({
        **copy.deepcopy(template),
        "variant": "through_fit_suite",
        "connector_design": "key_size_fit_suite",
        "key_trials": get_ai_version_5_through_trials(),
    })
    options.append({
        **copy.deepcopy(template),
        "variant": "key_size_extension_suite",
        "connector_design": "key_size_fit_suite",
        "key_trials": get_ai_version_5_key_extension_trials(),
        "trial_layout_y_offset": 0,
        "test_rationale": "User reports sample 9 closest but still loose, sample 1 much too loose; continue the 3/6/9 size progression.",
    })
    options.append({
        **copy.deepcopy(template),
        "variant": "snap_recessed_twin",
        "connector_design": "snap_recessed_twin",
        "snap_arm_outer": 3.4,
        "snap_arm_height": 10.0,
        "twin_arm_thickness": 1.0,
        "twin_root_distance": 0.5,
        "hook_projection": 1.2,
        "hook_ramp_length": 1.5,
        "recessed_shoulder_depth": 6.0,
        "sample_number": 19,
        "number_depth": 0.6,
        "number_size": 4.0,
        "number_rail_z": 24.0,
    })
    trial = copy.deepcopy(options[-1])
    trial.update({
        "variant": "recessed_twin_fit_suite",
        "connector_design": "recessed_twin_fit_suite",
        "latch_trials": get_ai_version_5_latch_trials(),
        "test_rationale": "User reports sample 19 worked well; compare thicker arms for mainly permanent PETG connections.",
    })
    options.append(trial)
    options.append({
        **copy.deepcopy(trial),
        "variant": "recessed_twin_heavy_suite",
        "latch_trials": get_ai_version_5_heavy_latch_trials(),
        "test_rationale": "User reports 23 and 24 too narrow; keep 25/26 and add two thicker arms on one numbered bed.",
    })
    options.append({
        **copy.deepcopy(template),
        **get_ai_version_5_key_extension_trials()[-1],
        "variant": "tight_key_27",
        "connector_design": "snap_key",
        "sample_number": 27,
        "tight_key_trial": True,
        "key_latch_clearance": 0.1,  # At each tongue face, along key insertion.
        "test_rationale": "Sample 22 fits best; shorten head-to-latch capture span while retaining its existing beam and plate fit.",
    })
    options.extend(get_ai_version_5_tiled_options())
    return options


def get_ai_version_5_latch_trials():
    # Keep the receiver and hook fit unchanged; thicken arms toward the open centre.
    return [
        {
            "sample_number": 23+index,
            "twin_arm_thickness": thickness,
            "latch_thickness_trial": True,
        }
        for index, thickness in enumerate([1.0, 1.2, 1.4, 1.6])
    ]


def get_ai_version_5_heavy_latch_trials():
    # 27 already identifies the tightened separate key; keep IDs unambiguous.
    return copy.deepcopy(get_ai_version_5_latch_trials()[2:])+[
        {
            "sample_number": number,
            "twin_arm_thickness": thickness,
            "latch_thickness_trial": True,
            "heavy_latch_trial": True,
        }
        for number, thickness in [(28,1.8),(29,2.0)]
    ]


def get_ai_version_5_tiled_options():
    # Finished outside dimensions, not stretched container openings.
    template = copy.deepcopy(get_ai_version_4_options()[0])
    template.update({
        "style": "ai_version_5",
        "part_role": "frame",
        "connector_design": "tiled_hybrid",
        "connector_view": "print_layout",
        "test_material": "PETG",
        "row": 9,
        "target_height": 300.0,
        "bed_width": 256.0,
        "bed_height": 256.0,
        "bed_margin": 2.0,
        "bed_exclusion": [18.0, 28.0],
        "tile_lap_x": 11.0,
        "tile_lap_y": 9.0,
        "tile_seam_clearance": 0.15,
        "tile_layer_clearance": 0.0,  # Half-thickness faces bear directly together.
        "additional_screw_every": 0,  # 0: seams only; N: also every Nth rail.
        "snap_clearance": 0.25,
        "snap_hook_projection": 1.2,
        "outer_mount_offset": 0.9,  # Retain 1.55 mm beside outside snap pockets.
        "tile_ear_diameter": 12.0,
        "tile_ear_gap": 0.5,
        "tile_ear_height": 0.3,
        "tile_ear_link_width": 2.0,
        "tile_ear_link_height": 0.2,
    })
    return [
        {**copy.deepcopy(template), "column": 8, "target_width": 767.0,
         "variant": "tiled_767_by_300"},
        {**copy.deepcopy(template), "column": 3, "target_width": 362.0,
         "variant": "tiled_362_by_300"},
    ]


def get_ai_version_5_key_trials():
    # User-requested clearance trials are confined to this numbered test kit.
    # These are NOT clearance variants of the drawer catalogue.
    defaults = get_ai_version_5_defaults()
    trials = []
    for scale in [1.0, 1.15, 1.3]:
        for clearance in [0.2, 0.3, 0.4]:
            trial = {
                "sample_number": len(trials)+1,
                "key_scale": scale,
                "connector_clearance": clearance,
                "through_clearance": 0.25,
                "through_height_clearance": 0.25,
                "key_head_length": round(2.0*scale, 6),
                "key_tip_chamfer": round(0.2*scale, 6),
                "key_hook_flat": round(0.3*scale, 6),
                "number_depth": 0.6,
                "number_size": 5.0,
                "number_rail_z": 24.0,
            }
            for name in ["key_arm_thickness", "key_root_radius", "key_half_width",
                         "key_height", "key_head_x", "key_shoulder_x",
                         "key_tongue_half_width", "hook_projection", "hook_ramp_length"]:
                trial[name] = round(defaults[name]*scale, 6)
            trials.append(trial)
    return trials


def get_ai_version_5_through_trials():
    # Isolate through-tongue fit from key fit: every key uses sample 5 dimensions.
    reference = get_ai_version_5_key_trials()[4]
    trials = []
    for clearance in [0.1, 0.2, 0.3]:
        for interference in [-0.025, 0.025, 0.05]:
            trials.append({
                **copy.deepcopy(reference),
                "sample_number": 10+len(trials),
                "number_size": 4.0,
                "through_clearance": clearance,
                "through_height_clearance": 0.25,
                "through_seat_interference": interference,
                "through_taper_length": 6.0,
            })
    return trials


def get_ai_version_5_key_extension_trials():
    # Continue 3/6/9's +15 percentage-point SIZE steps, not the clearance axis.
    defaults = get_ai_version_5_defaults()
    reference = get_ai_version_5_key_trials()[8]
    trials = []
    for number, scale in zip([20,21,22], [1.45,1.6,1.75]):
        trial = {
            **copy.deepcopy(reference),
            "sample_number": number,
            "key_scale": scale,
            "key_head_length": round(2*scale,6),
            "key_tip_chamfer": round(0.2*scale,6),
            "key_hook_flat": round(0.3*scale,6),
            "key_slot_min_wall": 1.0,
            "number_size": 4.0,
            "plate_number_size": 1.8,
            "plate_number_x": -6.1,
        }
        for name in ["key_arm_thickness", "key_root_radius", "key_half_width",
                     "key_height", "key_head_x", "key_shoulder_x",
                     "key_tongue_half_width", "hook_projection", "hook_ramp_length"]:
            trial[name] = round(defaults[name]*scale,6)
        trials.append(trial)
    return trials


if __name__ == "__main__":
    main()
