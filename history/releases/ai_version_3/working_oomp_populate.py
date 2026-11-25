
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []
    
    

    options = get_ai_version_1_options() + get_ai_version_2_options() + get_ai_version_3_options()

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


if __name__ == "__main__":
    main()
