import copy
from turtle import position
import oobb
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    typ = scad_help.get_typ(**kwargs)
    oomp_mode = "project"
    #oomp_mode = "oobb"
    filt = ""
    build_variables = scad_help.get_build_variables(typ, filter=filt)
    if True:
        kwargs["filter"] = kwargs.get("scad_filter", build_variables["filter"])
        kwargs["save_type"] = build_variables["save_type"]
        kwargs["navigation"] = build_variables["navigation"]
        kwargs["overwrite"] = build_variables["overwrite"]
        kwargs["modes"] = build_variables["modes"]
        kwargs["oomp_mode"] = oomp_mode
        kwargs["oomp_run"] = build_variables["oomp_run"]
    parts = get_parts(kwargs, oomp_mode)
    
    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    if kwargs["navigation"]:
        oobb_style = False  
        sort = scad_help.get_navigation_sort(oobb_style=oobb_style)
        scad_help.generate_navigation(sort=sort)

def get_parts(kwargs, oomp_mode):
    parts = []    

    #load parts from parts/folder/working.yaml
    parts_directory = os.path.join(os.path.dirname(__file__), "parts")
    if not os.path.isdir(parts_directory):
        return parts

    for folder in os.listdir(parts_directory):
        folder_path = os.path.join(parts_directory, folder)
        if not os.path.isdir(folder_path):
            continue

        working_yaml_path = os.path.join(folder_path, "working.yaml")
        if not os.path.isfile(working_yaml_path):
            continue

        with open(working_yaml_path, "r", encoding="utf-8") as infile:
            loaded_part = yaml.safe_load(infile)

        if not isinstance(loaded_part, dict):
            continue

        oobb_details = loaded_part.get("oobb_details")
        if not isinstance(oobb_details, dict):
            continue

        part = loaded_part

        part_kwargs = copy.deepcopy(kwargs)
        part_kwargs.update(copy.deepcopy(loaded_part.get("kwargs", {})))
        part_kwargs.update(copy.deepcopy(oobb_details))
        part["kwargs"] = part_kwargs
        part["oobb_name"] = part.get("oobb_name", oobb_details.get("oobb_name", "default"))

        if oomp_mode == "oobb":
            part["kwargs"]["oomp_size"] = part["oobb_name"]

        parts.append(part)


    return parts

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("depth", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    


    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_plate"    
        p3["depth"] = depth
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb.append_full(thing,**p3)
    
    #add holes seperate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = "perimeter"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb.append_full(thing,**p3)

    #add a test screw_countersunk
    if False:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"screw_countersunk"
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += depth
        p3["pos"] = pos1
        p3["m"] = "#"
        oobb.append_full(thing,**p3)

    if prepare_print:
        scad_help.prepare_base_for_print(thing, pos, **kwargs)

def get_ai_version_1(thing, **kwargs):
    kwargs = get_ai_version_1_parameters(**kwargs)
    pos = copy.deepcopy(kwargs.pop("pos", [0, 0, 0]))

    # Two independent shallow modules show the actual seam and repeating grid.
    if kwargs["part_role"] == "bank_layout":
        pitch = kwargs["width_total"] + kwargs["module_gap"]
        for shift in [-pitch / 2, pitch / 2]:
            p3 = copy.deepcopy(kwargs)
            p3.update(part_role="layout", pos=[pos[0] + shift, pos[1], pos[2]])
            get_ai_version_1(thing, **p3)
        thing["ai_design"] = get_ai_version_1_summary(kwargs, copies=2)
        return

    # Keep the project's solid-body-minus-cutouts construction.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "positive",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [kwargs["width_total"], kwargs["height_total"], kwargs["depth_total"]],
        "radius": kwargs["outer_radius"],
        "pos": pos,
    }
    oobb.append_full(thing, **p3)

    start_x = -kwargs["width_total"] / 2 + kwargs["drawer_border_edge"] + kwargs["opening_width"] / 2
    start_y = -kwargs["height_total"] / 2 + kwargs["drawer_border_edge"] + kwargs["opening_height"] / 2
    for r in range(kwargs["row"]):
        for c in range(kwargs["column"]):
            pos1 = [pos[0] + start_x + c * kwargs["pitch_x"],
                    pos[1] + start_y + r * kwargs["pitch_y"], pos[2]]
            # Each cell owns its opening, surrounding reliefs and catch.
            cutout_kwargs = {
                **copy.deepcopy(kwargs),
                "row_index": r,
                "column_index": c,
            }
            get_container_cutout(pos1, thing, **cutout_kwargs)
    if kwargs["adhesion_ears"]:
        get_ai_version_1_ears(thing, pos=pos, **kwargs)
    thing["ai_design"] = get_ai_version_1_summary(kwargs)


def get_ai_version_1_parameters(**kwargs):
    import math
    from working_oomp_populate import get_ai_version_1_defaults

    parameters = get_ai_version_1_defaults()
    parameters.update(copy.deepcopy(kwargs))
    parameters["style"] = "ai_version_1"
    container = get_ai_version_1_container_details(container=parameters.get("container", ""))
    for key in ["container_width", "container_height", "container_depth"]:
        if key not in container:
            raise ValueError("ai_version_1 requires a known container dimension mapping")
        parameters[key] = container[key]

    for key in ["column", "row"]:
        value = parameters.get(key, 1)
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{key} must be a positive integer")
        parameters[key] = value
    role = parameters["part_role"]
    if role not in ["frame", "fit", "layout", "bank_layout"]:
        raise ValueError(f"Unknown ai_version_1 part_role: {role}")
    positive = ["thickness_wall", "drawer_border_edge", "opening_radius", "outer_radius",
                "front_band", "rear_band", "runner_width", "side_rail_width",
                "depth_lip", "inset_lip", "lip_cutout_radius", "lip_shelf_thickness", "lip_support_reference_height",
                "roof_slope", "catch_tab_width", "catch_tab_depth", "bed_width", "bed_height",
                "catch_tab_ramp_depth", "ear_diameter", "ear_height", "ear_gap",
                "ear_link_width", "ear_link_height"]
    nonnegative = ["opening_height_extra", "container_clearance", "depth_clearance", "catch_tab_height", "module_gap", "bed_margin", "middle_rib_width"]
    if "build_height" in parameters:
        positive.append("build_height")
    for key in positive + nonnegative:
        value = parameters[key]
        if not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0 or (key in positive and value == 0):
            raise ValueError(f"Invalid {key}: {value}")
    if parameters["roof_slope"] < 1:
        raise ValueError("roof_slope must be >= 1 for roofs at least 45 degrees from the bed")
    if parameters["drawer_border_edge"] < parameters["thickness_wall"]:
        raise ValueError("Outer borders must be at least as thick as the dividers")
    parameters["opening_width"] = parameters["container_width"] + parameters["container_clearance"]
    parameters["opening_height"] = parameters["container_height"] + parameters["container_clearance"] + parameters["opening_height_extra"]
    parameters["pitch_x"] = parameters["opening_width"] + parameters["thickness_wall"]
    parameters["pitch_y"] = parameters["opening_height"] + parameters["thickness_wall"]
    parameters["width_total"] = parameters["column"] * parameters["pitch_x"] - parameters["thickness_wall"] + 2 * parameters["drawer_border_edge"]
    parameters["height_total"] = parameters["row"] * parameters["pitch_y"] - parameters["thickness_wall"] + 2 * parameters["drawer_border_edge"]
    parameters["depth_total"] = parameters["container_depth"] + parameters["depth_clearance"]
    if role != "frame":
        test_depth = parameters.get("test_depth", 12)
        if not isinstance(test_depth, (int, float)) or not math.isfinite(test_depth) or test_depth <= 0:
            raise ValueError("test_depth must be positive and finite")
        parameters["depth_total"] = test_depth
    if "build_height" in parameters and parameters["depth_total"] > parameters["build_height"]:
        raise ValueError("Frame print height exceeds the printer build_height")
    width = parameters["width_total"]
    if role == "bank_layout":
        width = 2 * width + parameters["module_gap"]
    parameters["ear_extension"] = (parameters["ear_diameter"] + parameters["ear_gap"]
                                    if parameters["adhesion_ears"] else 0)
    parameters["print_height_total"] = parameters["height_total"] + 2 * parameters["ear_extension"]
    if width + 2 * parameters["bed_margin"] > parameters["bed_width"] or parameters["print_height_total"] + 2 * parameters["bed_margin"] > parameters["bed_height"]:
        raise ValueError("Module including adhesion ears exceeds bed limits and bed_margin")
    if 2 * parameters["opening_radius"] >= min(parameters["opening_width"], parameters["opening_height"]):
        raise ValueError("opening_radius is too large")
    if parameters["outer_radius"] > parameters["drawer_border_edge"]:
        raise ValueError("outer_radius must fit within the outside border")
    if parameters["runner_width"] < parameters["inset_lip"] + parameters["opening_radius"] or parameters["side_rail_width"] < parameters["opening_radius"]:
        raise ValueError("Edge rails must retain the stepped profile and rounded opening corners")
    parameters["lip_step_y"] = -parameters["opening_height"] / 2 + parameters["depth_lip"]
    parameters["lip_body_width"] = parameters["opening_width"] - 2 * parameters["inset_lip"]
    if parameters["lip_body_width"] <= 2 * parameters["opening_radius"] or not 2 * parameters["lip_cutout_radius"] < parameters["depth_lip"] < parameters["opening_height"]:
        raise ValueError("Lip profile dimensions do not fit the opening")
    if parameters["lip_shelf_thickness"] < parameters["thickness_wall"]:
        raise ValueError("Lip shelf must be at least as thick as the divider walls")
    parameters["lip_support_channel_height"] = min(
        parameters["opening_height"],
        parameters["lip_support_reference_height"] + parameters["container_clearance"])
    parameters["lip_support_end_y"] = -parameters["opening_height"] / 2 + parameters["lip_support_channel_height"]
    parameters["body_extension_height"] = parameters["opening_height"] - parameters["lip_support_channel_height"]
    if parameters["lip_support_channel_height"] < parameters["depth_lip"] + parameters["lip_shelf_thickness"]:
        raise ValueError("Lip support height must retain the complete bearing shelf")
    if parameters["catch_tab_width"] > parameters["opening_width"] - 2 * parameters["opening_radius"]:
        raise ValueError("catch_tab_width must fit between the opening's rounded corners")
    if parameters["catch_tab_height"] > 0:
        if parameters["catch_tab_ramp_depth"] < parameters["catch_tab_height"]:
            raise ValueError("Catch ramp must rise at least 45 degrees from the print bed")
        if parameters["catch_tab_height"] >= parameters["opening_height"] or parameters["catch_tab_ramp_depth"] + parameters["catch_tab_depth"] > min(parameters["front_band"], parameters["depth_total"]):
            raise ValueError("Catch ramp and tip must fit the opening and front band")
    if parameters["adhesion_ears"]:
        radius = parameters["ear_diameter"] / 2
        if parameters["ear_diameter"] * 2 >= parameters["width_total"]:
            raise ValueError("Corner ears must be separated")
        if parameters["ear_link_height"] > parameters["ear_height"] or parameters["ear_height"] >= parameters["depth_total"]:
            raise ValueError("Ear links must be no taller than pads, and pads shorter than the frame")
        # Links penetrate each circular pad by 0.8 mm, and the frame by 0.4 mm.
        if radius <= 0.8 or parameters["ear_link_width"] > 2 * math.sqrt(2 * radius * 0.8 - 0.8 ** 2):
            raise ValueError("Ear link must fit within the pad's attachment chord")
        if radius - parameters["ear_link_width"] / 2 <= parameters["outer_radius"] or parameters["drawer_border_edge"] <= 0.4:
            raise ValueError("Ear link must attach to a straight, solid outside edge")
    window_count = 2 if parameters["middle_rib_width"] > 0 else 1
    parameters["shelf_window_width"] = (parameters["opening_width"] - 2 * parameters["runner_width"] - parameters["middle_rib_width"]) / window_count
    parameters["side_window_lower_width"] = parameters["depth_lip"] - parameters["side_rail_width"] - parameters["lip_cutout_radius"]
    parameters["side_window_upper_width"] = parameters["opening_height"] - parameters["depth_lip"] - parameters["lip_shelf_thickness"] - parameters["side_rail_width"]
    for key in ["shelf_window_width", "side_window_lower_width", "side_window_upper_width"]:
        if parameters[key] <= 0:
            raise ValueError("Rails/ribs leave no room for relief windows")
        if role == "frame" and parameters["lightening"]:
            roof_rise = parameters[key] / 2 * parameters["roof_slope"]
            if parameters["front_band"] + parameters["rear_band"] + roof_rise >= parameters["depth_total"]:
                raise ValueError("Relief window roof does not fit within the frame depth")
    return parameters


def get_ai_version_1_summary(kwargs, copies=1):
    width = copies * kwargs["width_total"] + (copies - 1) * kwargs["module_gap"]
    return {
        "envelope_mm": [width, kwargs["print_height_total"], kwargs["depth_total"]],
        "finished_envelope_mm": [width, kwargs["height_total"], kwargs["depth_total"]],
        "adhesion_ears": kwargs["adhesion_ears"],
        "ear_count": copies * 4 if kwargs["adhesion_ears"] else 0,
        "printer": kwargs.get("printer", "unspecified"),
        "build_volume_mm": [kwargs["bed_width"], kwargs["bed_height"], kwargs.get("build_height")],
        "bed_margin_mm": kwargs["bed_margin"],
        "catch_projection_mm": kwargs["catch_tab_height"],
        "catch_ramp_depth_mm": kwargs["catch_tab_ramp_depth"],
        "cutout_revision": "ai_version_2_lip_supported",
        "lip_inset_mm": kwargs["inset_lip"],
        "lip_step_height_mm": kwargs["depth_lip"],
        "lip_shelf_thickness_mm": kwargs["lip_shelf_thickness"],
        "lip_support_channel_height_mm": kwargs["lip_support_channel_height"],
        "body_extension_height_mm": kwargs["body_extension_height"],
        "centre_support_width_mm": kwargs["middle_rib_width"],
        "opening_mm": [kwargs["opening_width"], kwargs["opening_height"]],
        "pitch_mm": [kwargs["pitch_x"], kwargs["pitch_y"]],
        "expected_bodies": copies,
        "drawer_count": copies * kwargs["column"] * kwargs["row"],
        "part_role": kwargs["part_role"],
        "print_orientation": "Front face on bed; +Z is insertion depth and print height",
        "physical_validation": "Pending container-fit, printing, shrinkage and load tests",
    }


def get_ai_version_1_ears(thing, **kwargs):
    import math
    pos = kwargs.get("pos", [0, 0, 0])
    radius = kwargs["ear_diameter"] / 2
    # Exact cardinal vertices keep nominal footprint checks independent of $fn.
    circle = [[radius * math.cos(i * math.tau / 64), radius * math.sin(i * math.tau / 64)]
              for i in range(64)]
    for side_x in [-1, 1]:
        for side_y in [-1, 1]:
            x = pos[0] + side_x * (kwargs["width_total"] / 2 - radius)
            edge_y = pos[1] + side_y * kwargs["height_total"] / 2
            y = edge_y + side_y * (radius + kwargs["ear_gap"])
            p3 = copy.deepcopy(kwargs)
            p3.update(type="positive_positive", shape="polygon", m="",
                      points=circle, height=kwargs["ear_height"], depth=kwargs["ear_height"],
                      pos=[x, y, pos[2]], rot=[0, 0, 0])
            oobb.append_full(thing, **p3)
            # Clear gap around the pad; only this thin neck needs snapping/cutting.
            ends = [edge_y - side_y * 0.4, edge_y + side_y * (kwargs["ear_gap"] + 0.8)]
            p3 = copy.deepcopy(kwargs)
            p3.update(type="positive_positive", shape="cube", m="",
                      size=[kwargs["ear_link_width"], abs(ends[1] - ends[0]), kwargs["ear_link_height"]],
                      pos=[x - kwargs["ear_link_width"] / 2, min(ends), pos[2]], rot=[0, 0, 0])
            oobb.append_full(thing, **p3)


# Version 2 is locked; use the independent version 3 functions for refinement.
def get_ai_version_2(thing, **kwargs):
    kwargs = get_ai_version_2_parameters(**kwargs)
    pos = copy.deepcopy(kwargs.pop("pos", [0, 0, 0]))

    # Assemble the separately generated halves only for the reference record.
    # Each printable half is generated directly from the same source, never
    # sliced from an STL. Rear half turns about Y when assembled.
    if kwargs["split_frame"] and kwargs["assembly_half"] in ["assembled", "print_layout"]:
        for half in ["front", "back"]:
            sub = oobb.get_default_thing(type="split_half")
            p3 = {**copy.deepcopy(kwargs), "assembly_half": half}
            get_ai_version_2(sub, **p3)
            shift = [0, 0, kwargs["assembled_depth"] if half == "back" else 0]
            rotation = [0, 180, 0] if half == "back" else [0, 0, 0]
            if kwargs["assembly_half"] == "print_layout":
                shift = [0, 0, 0]
                shift[kwargs["print_layout_axis"]] = kwargs["print_layout_pitch"] * (-0.5 if half == "front" else 0.5)
                rotation = [0, 0, 0]
            thing["components"].append({
                "type": "rotation",
                "typetype": "positive",
                "pos": [pos[k] + shift[k] for k in range(3)],
                "rot": rotation,
                "objects": sub["components"],
            })
        thing["ai_design"] = get_ai_version_2_summary(kwargs)
        return

    # Two independent shallow modules show the actual seam and repeating grid.
    if kwargs["part_role"] == "bank_layout":
        pitch = kwargs["width_total"] + kwargs["module_gap"]
        for shift in [-pitch / 2, pitch / 2]:
            p3 = copy.deepcopy(kwargs)
            p3.update(part_role="layout", pos=[pos[0] + shift, pos[1], pos[2]])
            get_ai_version_2(thing, **p3)
        thing["ai_design"] = get_ai_version_2_summary(kwargs, copies=2)
        return

    # Keep the project's solid-body-minus-cutouts construction.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "positive",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [kwargs["width_total"], kwargs["height_total"], kwargs["body_depth"]],
        "radius": kwargs["outer_radius"],
        "pos": pos,
    }
    oobb.append_full(thing, **p3)

    start_x = -kwargs["width_total"] / 2 + kwargs["drawer_border_edge"] + kwargs["opening_width"] / 2
    start_y = -kwargs["height_total"] / 2 + kwargs["drawer_border_edge"] + kwargs["opening_height"] / 2
    for r in range(kwargs["row"]):
        for c in range(kwargs["column"]):
            pos1 = [pos[0] + start_x + c * kwargs["pitch_x"],
                    pos[1] + start_y + r * kwargs["pitch_y"], pos[2]]
            # Each cell owns its opening, surrounding reliefs and catch.
            cutout_kwargs = {
                **copy.deepcopy(kwargs),
                "row_index": r,
                "column_index": c,
            }
            get_container_cutout(pos1, thing, **cutout_kwargs)
    if kwargs["adhesion_ears"]:
        get_ai_version_2_ears(thing, pos=pos, **kwargs)
    thing["ai_design"] = get_ai_version_2_summary(kwargs)


def get_ai_version_2_parameters(**kwargs):
    import math
    from working_oomp_populate import get_ai_version_2_defaults

    parameters = get_ai_version_2_defaults()
    parameters.update(copy.deepcopy(kwargs))
    parameters["style"] = "ai_version_2"
    container = get_ai_version_2_container_details(container=parameters.get("container", ""))
    for key in ["container_width", "container_height", "container_depth"]:
        if key not in container:
            raise ValueError("ai_version_2 requires a known container dimension mapping")
        parameters[key] = container[key]

    for key in ["column", "row"]:
        value = parameters.get(key, 1)
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{key} must be a positive integer")
        parameters[key] = value
    role = parameters["part_role"]
    if role not in ["frame", "fit", "layout", "bank_layout"]:
        raise ValueError(f"Unknown ai_version_2 part_role: {role}")
    positive = ["thickness_wall", "drawer_border_edge", "opening_radius", "outer_radius",
                "front_band", "rear_band", "runner_width", "side_rail_width",
                "depth_lip", "inset_lip", "lip_cutout_radius", "lip_shelf_thickness", "lip_support_reference_height",
                "roof_slope", "catch_tab_width", "catch_tab_depth", "bed_width", "bed_height",
                "catch_tab_ramp_depth", "ear_diameter", "ear_height", "ear_gap",
                "ear_link_width", "ear_link_height", "interlock_depth", "interlock_width",
                "interlock_height", "screw_length", "screw_head_seat_offset",
                "corner_interlock_diameter", "corner_interlock_min_wall",
                "hardware_axis_height", "hardware_min_wall"]
    nonnegative = ["print_layout_gap", "interlock_clearance", "interlock_end_clearance", "opening_height_extra", "container_clearance", "depth_clearance", "catch_tab_height", "module_gap", "bed_margin", "middle_rib_width"]
    if "build_height" in parameters:
        positive.append("build_height")
    for key in positive + nonnegative:
        value = parameters[key]
        if not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0 or (key in positive and value == 0):
            raise ValueError(f"Invalid {key}: {value}")
    if parameters["roof_slope"] < 1:
        raise ValueError("roof_slope must be >= 1 for roofs at least 45 degrees from the bed")
    if parameters["drawer_border_edge"] < parameters["thickness_wall"]:
        raise ValueError("Outer borders must be at least as thick as the dividers")
    parameters["opening_width"] = parameters["container_width"] + parameters["container_clearance"]
    parameters["opening_height"] = parameters["container_height"] + parameters["container_clearance"] + parameters["opening_height_extra"]
    parameters["pitch_x"] = parameters["opening_width"] + parameters["thickness_wall"]
    parameters["pitch_y"] = parameters["opening_height"] + parameters["thickness_wall"]
    parameters["width_total"] = parameters["column"] * parameters["pitch_x"] - parameters["thickness_wall"] + 2 * parameters["drawer_border_edge"]
    parameters["height_total"] = parameters["row"] * parameters["pitch_y"] - parameters["thickness_wall"] + 2 * parameters["drawer_border_edge"]
    parameters["depth_total"] = parameters["container_depth"] + parameters["depth_clearance"]
    if role != "frame":
        test_depth = parameters.get("test_depth", 12)
        if not isinstance(test_depth, (int, float)) or not math.isfinite(test_depth) or test_depth <= 0:
            raise ValueError("test_depth must be positive and finite")
        parameters["depth_total"] = test_depth
    parameters["split_frame"] = role == "frame"
    if parameters.get("assembly_half") not in ["assembled", "print_layout", "front", "back"]:
        raise ValueError("assembly_half must be print_layout, assembled, front or back")
    if "joint_test_depth" in parameters:
        parameters["depth_total"] = parameters["joint_test_depth"]
    parameters["assembled_depth"] = parameters["depth_total"]
    parameters["body_depth"] = parameters["depth_total"]
    if parameters["split_frame"]:
        parameters["body_depth"] = parameters["assembled_depth"] / 2
        if parameters["assembly_half"] != "assembled":
            parameters["depth_total"] = parameters["body_depth"] + (parameters["interlock_depth"] if parameters["assembly_half"] in ["front", "print_layout"] else 0)
        wall = parameters["hardware_min_wall"]
        nut_radius = oobb.gv("nut_radius_m3", "3dpr")
        nut_depth = oobb.gv("nut_depth_m3", "3dpr")
        parameters["nut_seat_offset"] = parameters["screw_length"] - parameters["screw_head_seat_offset"] - nut_depth
        if parameters["nut_seat_offset"] <= parameters["interlock_depth"] + parameters["interlock_end_clearance"] + wall:
            raise ValueError("Not enough material between the interlock socket and nut seat")
        if parameters["body_depth"] < max(parameters["screw_head_seat_offset"] + 3.2, parameters["screw_length"] - parameters["screw_head_seat_offset"]) + 1:
            raise ValueError("Half too shallow for recessed 16 mm hardware")
        if min(parameters["inset_lip"] + parameters["drawer_border_edge"], 2 * parameters["inset_lip"] + parameters["thickness_wall"]) < max(2 * nut_radius, parameters["interlock_width"] + 2 * parameters["interlock_clearance"]) + 2 * wall:
            raise ValueError("Widen border/shoulder to retain material around hardware and socket")
        if min(parameters["hardware_axis_height"], parameters["lip_shelf_thickness"] - parameters["hardware_axis_height"]) < max(nut_radius, parameters["interlock_height"] / 2 + parameters["interlock_clearance"]) + wall:
            raise ValueError("Shelf too thin around hardware/interlock")
        if min(parameters["interlock_width"], parameters["interlock_height"]) < 2 * oobb.gv("hole_radius_m3", "3dpr") + 2 * wall:
            raise ValueError("Interlock tongue too thin around screw bore")
        if parameters["assembly_half"] == "back":
            parameters["catch_tab_height"] = 0
    if "build_height" in parameters and parameters["depth_total"] > parameters["build_height"]:
        raise ValueError("Frame print height exceeds the printer build_height")
    width = parameters["width_total"]
    if role == "bank_layout":
        width = 2 * width + parameters["module_gap"]
    parameters["ear_extension"] = (parameters["ear_diameter"] + parameters["ear_gap"]
                                    if parameters["adhesion_ears"] else 0)
    parameters["print_height_total"] = parameters["height_total"] + 2 * parameters["ear_extension"]
    if width + 2 * parameters["bed_margin"] > parameters["bed_width"] or parameters["print_height_total"] + 2 * parameters["bed_margin"] > parameters["bed_height"]:
        raise ValueError("Module including adhesion ears exceeds bed limits and bed_margin")
    # Arrange both complete footprints, including ears, without overlap.
    # Prefer a layout that fits one bed; maximum-size pairs need separate plates.
    pair_x = [2 * parameters["width_total"] + parameters["print_layout_gap"], parameters["print_height_total"]]
    pair_y = [parameters["width_total"], 2 * parameters["print_height_total"] + parameters["print_layout_gap"]]
    margin = 2 * parameters["bed_margin"]
    scores = [max((size[0] + margin) / parameters["bed_width"], (size[1] + margin) / parameters["bed_height"]) for size in [pair_x, pair_y]]
    parameters["print_layout_axis"] = 0 if scores[0] <= scores[1] else 1
    parameters["print_layout_xy"] = [pair_x, pair_y][parameters["print_layout_axis"]]
    parameters["print_layout_pitch"] = [parameters["width_total"], parameters["print_height_total"]][parameters["print_layout_axis"]] + parameters["print_layout_gap"]
    parameters["print_layout_fits_single_bed"] = min(scores) <= 1
    if 2 * parameters["opening_radius"] >= min(parameters["opening_width"], parameters["opening_height"]):
        raise ValueError("opening_radius is too large")
    if parameters["outer_radius"] > parameters["drawer_border_edge"]:
        raise ValueError("outer_radius must fit within the outside border")
    if parameters["runner_width"] < parameters["inset_lip"] + parameters["opening_radius"] or parameters["side_rail_width"] < parameters["opening_radius"]:
        raise ValueError("Edge rails must retain the stepped profile and rounded opening corners")
    parameters["lip_step_y"] = -parameters["opening_height"] / 2 + parameters["depth_lip"]
    parameters["lip_body_width"] = parameters["opening_width"] - 2 * parameters["inset_lip"]
    if parameters["lip_body_width"] <= 2 * parameters["opening_radius"] or not 2 * parameters["lip_cutout_radius"] < parameters["depth_lip"] < parameters["opening_height"]:
        raise ValueError("Lip profile dimensions do not fit the opening")
    if parameters["lip_shelf_thickness"] < parameters["thickness_wall"]:
        raise ValueError("Lip shelf must be at least as thick as the divider walls")
    parameters["lip_support_channel_height"] = min(
        parameters["opening_height"],
        parameters["lip_support_reference_height"] + parameters["container_clearance"])
    parameters["lip_support_end_y"] = -parameters["opening_height"] / 2 + parameters["lip_support_channel_height"]
    parameters["body_extension_height"] = parameters["opening_height"] - parameters["lip_support_channel_height"]
    if parameters["split_frame"]:
        # Internal junction pegs sit at the upper edge of the lower opening.
        # Check the two adjacent rounded cavities, the open reliefs and border.
        radius = parameters["corner_interlock_diameter"] / 2
        required = radius + parameters["interlock_clearance"] + parameters["corner_interlock_min_wall"]
        wall = parameters["thickness_wall"]
        lip_radius = parameters["lip_cutout_radius"]
        body_radius = parameters["opening_radius"]
        corner_limits = [parameters["drawer_border_edge"] / 2,
                         parameters["side_rail_width"], parameters["runner_width"]]
        if parameters["row"] > 1:
            if parameters["column"] > 1:
                corner_limits.extend([
                    math.hypot(wall / 2 + lip_radius, wall + lip_radius) - lip_radius,
                    math.hypot(wall / 2 + body_radius, body_radius) - body_radius,
                ])
        if required > min(corner_limits):
            raise ValueError("Corner interlock socket leaves too little material at a grid junction")
    if parameters["lip_support_channel_height"] < parameters["depth_lip"] + parameters["lip_shelf_thickness"]:
        raise ValueError("Lip support height must retain the complete bearing shelf")
    if parameters["catch_tab_width"] > parameters["opening_width"] - 2 * parameters["opening_radius"]:
        raise ValueError("catch_tab_width must fit between the opening's rounded corners")
    if parameters["catch_tab_height"] > 0:
        if parameters["catch_tab_ramp_depth"] < parameters["catch_tab_height"]:
            raise ValueError("Catch ramp must rise at least 45 degrees from the print bed")
        if parameters["catch_tab_height"] >= parameters["opening_height"] or parameters["catch_tab_ramp_depth"] + parameters["catch_tab_depth"] > min(parameters["front_band"], parameters["depth_total"]):
            raise ValueError("Catch ramp and tip must fit the opening and front band")
    if parameters["adhesion_ears"]:
        radius = parameters["ear_diameter"] / 2
        if parameters["ear_diameter"] * 2 >= parameters["width_total"]:
            raise ValueError("Corner ears must be separated")
        if parameters["ear_link_height"] > parameters["ear_height"] or parameters["ear_height"] >= parameters["depth_total"]:
            raise ValueError("Ear links must be no taller than pads, and pads shorter than the frame")
        # Links penetrate each circular pad by 0.8 mm, and the frame by 0.4 mm.
        if radius <= 0.8 or parameters["ear_link_width"] > 2 * math.sqrt(2 * radius * 0.8 - 0.8 ** 2):
            raise ValueError("Ear link must fit within the pad's attachment chord")
        if radius - parameters["ear_link_width"] / 2 <= parameters["outer_radius"] or parameters["drawer_border_edge"] <= 0.4:
            raise ValueError("Ear link must attach to a straight, solid outside edge")
    window_count = 2 if parameters["middle_rib_width"] > 0 else 1
    parameters["shelf_window_width"] = (parameters["opening_width"] - 2 * parameters["runner_width"] - parameters["middle_rib_width"]) / window_count
    parameters["side_window_lower_width"] = parameters["depth_lip"] - parameters["side_rail_width"] - parameters["lip_cutout_radius"]
    parameters["side_window_upper_width"] = parameters["opening_height"] - parameters["depth_lip"] - parameters["lip_shelf_thickness"] - parameters["side_rail_width"]
    for key in ["shelf_window_width", "side_window_lower_width", "side_window_upper_width"]:
        if parameters[key] <= 0:
            raise ValueError("Rails/ribs leave no room for relief windows")
        if role == "frame" and parameters["lightening"] and not parameters["split_frame"]:
            roof_rise = parameters[key] / 2 * parameters["roof_slope"]
            if parameters["front_band"] + parameters["rear_band"] + roof_rise >= parameters["depth_total"]:
                raise ValueError("Relief window roof does not fit within the frame depth")
    return parameters


def get_ai_version_2_summary(kwargs, copies=1):
    width = copies * kwargs["width_total"] + (copies - 1) * kwargs["module_gap"]
    layout = kwargs["split_frame"] and kwargs["assembly_half"] == "print_layout"
    return {
        "envelope_mm": [*kwargs["print_layout_xy"], kwargs["depth_total"]] if layout else [width, kwargs["print_height_total"], kwargs["depth_total"]],
        "assembled_envelope_mm": [width, kwargs["height_total"], kwargs["assembled_depth"]],
        "print_layout_fits_single_bed": kwargs["print_layout_fits_single_bed"] if layout else None,
        "print_layout_gap_mm": kwargs["print_layout_gap"] if layout else None,
        "finished_envelope_mm": [width, kwargs["height_total"], kwargs["depth_total"]],
        "adhesion_ears": kwargs["adhesion_ears"],
        "ear_count": copies * (8 if kwargs["split_frame"] and kwargs["assembly_half"] in ["assembled", "print_layout"] else 4) if kwargs["adhesion_ears"] else 0,
        "printer": kwargs.get("printer", "unspecified"),
        "build_volume_mm": [kwargs["bed_width"], kwargs["bed_height"], kwargs.get("build_height")],
        "bed_margin_mm": kwargs["bed_margin"],
        "catch_projection_mm": kwargs["catch_tab_height"],
        "catch_ramp_depth_mm": kwargs["catch_tab_ramp_depth"],
        "cutout_revision": "ai_version_2_all_junction_interlocks",
        "assembly_half": kwargs["assembly_half"] if kwargs["split_frame"] else "sample",
        "assembled_depth_mm": kwargs["assembled_depth"],
        "half_body_depth_mm": kwargs["body_depth"],
        "interlock_depth_mm": kwargs["interlock_depth"],
        "interlock_clearance_per_side_mm": kwargs["interlock_clearance"],
        "corner_interlock_diameter_mm": kwargs["corner_interlock_diameter"],
        "corner_interlock_count": (kwargs["column"] + 1) * (kwargs["row"] + 1) if kwargs["split_frame"] else 0,
        "screw_length_mm": kwargs["screw_length"],
        "head_seat_offset_mm": kwargs["screw_head_seat_offset"],
        "nut_seat_offset_mm": kwargs.get("nut_seat_offset"),
        "screw_count": (kwargs["column"] + 1) * kwargs["row"] if kwargs["split_frame"] else 0,
        "printable": not (kwargs["split_frame"] and kwargs["assembly_half"] == "assembled"),
        "lip_inset_mm": kwargs["inset_lip"],
        "lip_step_height_mm": kwargs["depth_lip"],
        "lip_shelf_thickness_mm": kwargs["lip_shelf_thickness"],
        "lip_support_channel_height_mm": kwargs["lip_support_channel_height"],
        "body_extension_height_mm": kwargs["body_extension_height"],
        "centre_support_width_mm": kwargs["middle_rib_width"],
        "opening_mm": [kwargs["opening_width"], kwargs["opening_height"]],
        "pitch_mm": [kwargs["pitch_x"], kwargs["pitch_y"]],
        "expected_bodies": 2 if layout else copies,
        "drawer_count": copies * kwargs["column"] * kwargs["row"],
        "part_role": kwargs["part_role"],
        "print_orientation": "Outer face on bed, joint upward; back rotates 180 degrees about Y for assembly. The assembled.scad file is reference only; use front/back files for separate plates.",
        "physical_validation": "Pending container-fit, printing, shrinkage and load tests",
    }


def get_ai_version_2_ears(thing, **kwargs):
    import math
    pos = kwargs.get("pos", [0, 0, 0])
    radius = kwargs["ear_diameter"] / 2
    # Exact cardinal vertices keep nominal footprint checks independent of $fn.
    circle = [[radius * math.cos(i * math.tau / 64), radius * math.sin(i * math.tau / 64)]
              for i in range(64)]
    for side_x in [-1, 1]:
        for side_y in [-1, 1]:
            x = pos[0] + side_x * (kwargs["width_total"] / 2 - radius)
            edge_y = pos[1] + side_y * kwargs["height_total"] / 2
            y = edge_y + side_y * (radius + kwargs["ear_gap"])
            p3 = copy.deepcopy(kwargs)
            p3.update(type="positive_positive", shape="polygon", m="",
                      points=circle, height=kwargs["ear_height"], depth=kwargs["ear_height"],
                      pos=[x, y, pos[2]], rot=[0, 0, 0])
            oobb.append_full(thing, **p3)
            # Clear gap around the pad; only this thin neck needs snapping/cutting.
            ends = [edge_y - side_y * 0.4, edge_y + side_y * (kwargs["ear_gap"] + 0.8)]
            p3 = copy.deepcopy(kwargs)
            p3.update(type="positive_positive", shape="cube", m="",
                      size=[kwargs["ear_link_width"], abs(ends[1] - ends[0]), kwargs["ear_link_height"]],
                      pos=[x - kwargs["ear_link_width"] / 2, min(ends), pos[2]], rot=[0, 0, 0])
            oobb.append_full(thing, **p3)


def get_basic(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("depth", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")

    column = kwargs.get("column", 1)
    row = kwargs.get("row", 1)
    
    container = kwargs.get("container", "")
    kwargs = get_container_details(**kwargs)
    container_clearance = kwargs.get("container_clearance", 1.5)
    container_width = kwargs.get("container_width", 0)
    container_height = kwargs.get("container_height", 0)
    container_depth = kwargs.get("container_depth", 0)

    thickness_wall = 1
    kwargs["thickness_wall"] = thickness_wall
    drawer_border_edge = thickness_wall
    kwargs["drawer_border_edge"] = drawer_border_edge
    drawer_divider = thickness_wall
    kwargs["drawer_divider"] = drawer_divider
    

    width_total = ((container_width + container_clearance) * column) + (drawer_divider * (column-1)) + drawer_border_edge * 2
    height_total = ((container_height + container_clearance) * row) + (drawer_divider * (row-1)) + drawer_border_edge * 2
    depth_total = (container_depth + container_clearance) + thickness_wall

    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_total
        hei = height_total
        dep = depth_total
        size = [wid, hei, dep]
        p3["size"] = size
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb.append_full(thing,**p3)
    
    #add holes seperate
    if True:
        start_x = (-width_total/2) + (container_width + container_clearance)/2 + drawer_border_edge
        start_y = (-height_total/2) + (container_height + container_clearance)/2 + drawer_border_edge
        for r in range(row):
            for c in range(column):
                pos1 = copy.deepcopy(pos)
                # calculate the position for the current container cutout #move over and up to position one then across then down
                shift_x = start_x + c * (container_width + container_clearance + drawer_divider)
                pos1[0] += shift_x
                shift_y = start_y + r    * (container_height + container_clearance + drawer_divider)
                pos1[1] += shift_y
                get_container_cutout(pos1, thing, **kwargs)
        

    #add a test screw_countersunk
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"screw_countersunk"
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += depth
        p3["pos"] = pos1
        p3["m"] = "#"
        oobb.append_full(thing,**p3)

    if prepare_print:
        scad_help.prepare_base_for_print(thing, pos, **kwargs)

def get_container_details(**kwargs):
    container = kwargs.get("container", "")
    kwargs["container_clearance"] = 1.5
    if container == "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209":
        kwargs["container_width"] = 86
        kwargs["container_height"] = 26
        kwargs["container_depth"] = 109
    elif container == "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214":
        # Drawing axes: across, lidless height, insertion depth.
        # The 95 mm catalogue height includes the unused 3 mm lid.
        kwargs["container_width"] = 86
        kwargs["container_height"] = 95 - 3
        kwargs["container_depth"] = 108
    return kwargs

def get_ai_version_1_container_details(**kwargs):
    container = kwargs.get("container", "")
    kwargs["container_clearance"] = 1.5
    if container == "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209":
        kwargs["container_width"] = 86
        kwargs["container_height"] = 26
        kwargs["container_depth"] = 109
    elif container == "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214":
        # Drawing axes: across, lidless height, insertion depth.
        # The 95 mm catalogue height includes the unused 3 mm lid.
        kwargs["container_width"] = 86
        kwargs["container_height"] = 95 - 3
        kwargs["container_depth"] = 108
    return kwargs

def get_ai_version_2_container_details(**kwargs):
    container = kwargs.get("container", "")
    kwargs["container_clearance"] = 1.5
    if container == "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209":
        kwargs["container_width"] = 86
        kwargs["container_height"] = 26
        kwargs["container_depth"] = 109
    elif container == "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214":
        # Drawing axes: across, lidless height, insertion depth.
        # The 95 mm catalogue height includes the unused 3 mm lid.
        kwargs["container_width"] = 86
        kwargs["container_height"] = 95 - 3
        kwargs["container_depth"] = 108
    return kwargs

def get_container_cutout(pos, thing, **kwargs):
    import working_scad_container_cutout    
    working_scad_container_cutout.get_base(pos, thing, **kwargs)


def get_hole_cover(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("depth", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    diameter = kwargs.get("diameter", 10)
    clearance = kwargs.get("clearance", 0.5)
    thickness_wall = 2
    depth_taper = 3
    depth_top = 2
    diameter_top_extra = 10
    radius_gap=6
    diameter_top_taper = 5

    #add cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"    
    dep = depth - depth_taper 
    p3["depth"] = dep
    p3["radius"] = (diameter-clearance)/2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[2] += depth_taper + dep/2
    p3["pos"] = pos1
    oobb.append_full(thing,**p3)
    
    #add cylinder taper using radius_1 and radius_2
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"
    p3["depth"] = depth_taper
    p3["radius_2"] = (diameter-clearance)/2
    p3["radius_1"] = (diameter+clearance-thickness_wall)/2    
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth_taper/2
    p3["pos"] = pos1
    oobb.append_full(thing,**p3)

    #add top cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"
    p3["depth"] = depth_top
    dia = diameter+diameter_top_extra
    p3["radius_2"] = (dia-diameter_top_taper)/2
    p3["radius_1"] = (dia)/2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth-depth_top/2
    p3["pos"] = pos1
    oobb.append_full(thing,**p3)

    

    #add hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_cylinder"
    p3["depth"] = depth - depth_top/2
    p3["radius"] = (diameter+clearance-thickness_wall)/2    

    pos1 = copy.deepcopy(pos)
    pos1[2] += depth/2 - depth_top/2
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb.append_full(thing,**p3)

    
    #diameter_top 30
    #add hole_top
    diameter_top_hole = 30
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_cylinder"
    p3["depth"] = depth_top
    p3["radius"] = (diameter_top_hole)/2
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth - depth_top/2

    p3["pos"] = pos1
    p3["m"] = "#"
    oobb.append_full(thing,**p3)

    pos1 = copy.deepcopy(pos)
    pos1[1] += 100



    if prepare_print:
        scad_help.prepare_base_for_print(thing, pos, **kwargs)

    

# Version 3: independent development copy of the locked version 2 release.

def get_ai_version_3(thing, **kwargs):
    kwargs = get_ai_version_3_parameters(**kwargs)
    pos = copy.deepcopy(kwargs.pop("pos", [0, 0, 0]))

    # Assemble the separately generated halves only for the reference record.
    # Each printable half is generated directly from the same source, never
    # sliced from an STL. Rear half turns about Y when assembled.
    if kwargs["split_frame"] and kwargs["assembly_half"] in ["assembled", "print_layout"]:
        for half in ["front", "back"]:
            sub = oobb.get_default_thing(type="split_half")
            p3 = {**copy.deepcopy(kwargs), "assembly_half": half}
            get_ai_version_3(sub, **p3)
            shift = [0, 0, kwargs["assembled_depth"] if half == "back" else 0]
            rotation = [0, 180, 0] if half == "back" else [0, 0, 0]
            if kwargs["assembly_half"] == "print_layout":
                shift = [0, 0, 0]
                shift[kwargs["print_layout_axis"]] = kwargs["print_layout_pitch"] * (-0.5 if half == "front" else 0.5)
                rotation = [0, 0, 0]
            thing["components"].append({
                "type": "rotation",
                "typetype": "positive",
                "pos": [pos[k] + shift[k] for k in range(3)],
                "rot": rotation,
                "objects": sub["components"],
            })
        thing["ai_design"] = get_ai_version_3_summary(kwargs)
        return

    # Two independent shallow modules show the actual seam and repeating grid.
    if kwargs["part_role"] == "bank_layout":
        pitch = kwargs["width_total"] + kwargs["module_gap"]
        for shift in [-pitch / 2, pitch / 2]:
            p3 = copy.deepcopy(kwargs)
            p3.update(part_role="layout", pos=[pos[0] + shift, pos[1], pos[2]])
            get_ai_version_3(thing, **p3)
        thing["ai_design"] = get_ai_version_3_summary(kwargs, copies=2)
        return

    # Keep the project's solid-body-minus-cutouts construction.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "positive",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [kwargs["width_total"], kwargs["height_total"], kwargs["body_depth"]],
        "radius": kwargs["outer_radius"],
        "pos": pos,
    }
    oobb.append_full(thing, **p3)

    start_x = -kwargs["width_total"] / 2 + kwargs["drawer_border_edge"] + kwargs["opening_width"] / 2
    start_y = -kwargs["height_total"] / 2 + kwargs["drawer_border_edge"] + kwargs["opening_height"] / 2
    for r in range(kwargs["row"]):
        for c in range(kwargs["column"]):
            pos1 = [pos[0] + start_x + c * kwargs["pitch_x"],
                    pos[1] + start_y + r * kwargs["pitch_y"], pos[2]]
            # Each cell owns its opening, surrounding reliefs and catch.
            cutout_kwargs = {
                **copy.deepcopy(kwargs),
                "row_index": r,
                "column_index": c,
            }
            get_container_cutout(pos1, thing, **cutout_kwargs)
    if kwargs["adhesion_ears"]:
        get_ai_version_3_ears(thing, pos=pos, **kwargs)
    thing["ai_design"] = get_ai_version_3_summary(kwargs)


def get_ai_version_3_parameters(**kwargs):
    import math
    from working_oomp_populate import get_ai_version_3_defaults

    parameters = get_ai_version_3_defaults()
    parameters.update(copy.deepcopy(kwargs))
    parameters["style"] = "ai_version_3"
    container = get_ai_version_3_container_details(container=parameters.get("container", ""))
    for key in ["container_width", "container_height", "container_depth"]:
        if key not in container:
            raise ValueError("ai_version_3 requires a known container dimension mapping")
        parameters[key] = container[key]

    for key in ["column", "row"]:
        value = parameters.get(key, 1)
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{key} must be a positive integer")
        parameters[key] = value
    role = parameters["part_role"]
    if role not in ["frame", "fit", "layout", "bank_layout"]:
        raise ValueError(f"Unknown ai_version_3 part_role: {role}")
    positive = ["thickness_wall", "drawer_border_edge", "opening_radius", "outer_radius",
                "front_band", "rear_band", "runner_width", "side_rail_width",
                "depth_lip", "inset_lip", "lip_cutout_radius", "lip_shelf_thickness", "lip_support_reference_height",
                "roof_slope", "catch_tab_width", "catch_tab_depth", "bed_width", "bed_height",
                "catch_tab_ramp_depth", "ear_diameter", "ear_height", "ear_gap",
                "ear_link_width", "ear_link_height", "interlock_depth", "interlock_width",
                "interlock_height", "screw_length", "screw_head_seat_offset",
                "corner_interlock_diameter", "corner_interlock_min_wall",
                "hardware_axis_height", "hardware_min_wall", "running_shelf_thickness",
                "hardware_boss_band", "hardware_boss_slope"]
    nonnegative = ["print_layout_gap", "interlock_clearance", "interlock_end_clearance", "opening_height_extra", "container_clearance", "depth_clearance", "catch_tab_height", "module_gap", "bed_margin", "middle_rib_width"]
    if "build_height" in parameters:
        positive.append("build_height")
    for key in positive + nonnegative:
        value = parameters[key]
        if not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0 or (key in positive and value == 0):
            raise ValueError(f"Invalid {key}: {value}")
    if parameters["roof_slope"] < 1:
        raise ValueError("roof_slope must be >= 1 for roofs at least 45 degrees from the bed")
    if parameters["drawer_border_edge"] < parameters["thickness_wall"]:
        raise ValueError("Outer borders must be at least as thick as the dividers")
    parameters["opening_width"] = parameters["container_width"] + parameters["container_clearance"]
    parameters["opening_height"] = parameters["container_height"] + parameters["container_clearance"] + parameters["opening_height_extra"]
    parameters["pitch_x"] = parameters["opening_width"] + parameters["thickness_wall"]
    parameters["pitch_y"] = parameters["opening_height"] + parameters["thickness_wall"]
    parameters["width_total"] = parameters["column"] * parameters["pitch_x"] - parameters["thickness_wall"] + 2 * parameters["drawer_border_edge"]
    parameters["height_total"] = parameters["row"] * parameters["pitch_y"] - parameters["thickness_wall"] + 2 * parameters["drawer_border_edge"]
    parameters["depth_total"] = parameters["container_depth"] + parameters["depth_clearance"]
    if role != "frame":
        test_depth = parameters.get("test_depth", 12)
        if not isinstance(test_depth, (int, float)) or not math.isfinite(test_depth) or test_depth <= 0:
            raise ValueError("test_depth must be positive and finite")
        parameters["depth_total"] = test_depth
    parameters["split_frame"] = role == "frame"
    if parameters.get("assembly_half") not in ["assembled", "print_layout", "front", "back"]:
        raise ValueError("assembly_half must be print_layout, assembled, front or back")
    if "joint_test_depth" in parameters:
        parameters["depth_total"] = parameters["joint_test_depth"]
    parameters["assembled_depth"] = parameters["depth_total"]
    parameters["body_depth"] = parameters["depth_total"]
    if parameters["split_frame"]:
        parameters["body_depth"] = parameters["assembled_depth"] / 2
        if parameters["assembly_half"] != "assembled":
            parameters["depth_total"] = parameters["body_depth"] + (parameters["interlock_depth"] if parameters["assembly_half"] in ["front", "print_layout"] else 0)
        wall = parameters["hardware_min_wall"]
        nut_radius = oobb.gv("nut_radius_m3", "3dpr")
        nut_depth = oobb.gv("nut_depth_m3", "3dpr")
        parameters["nut_seat_offset"] = parameters["screw_length"] - parameters["screw_head_seat_offset"] - nut_depth
        if parameters["nut_seat_offset"] <= parameters["interlock_depth"] + parameters["interlock_end_clearance"] + wall:
            raise ValueError("Not enough material between the interlock socket and nut seat")
        if parameters["body_depth"] < max(parameters["screw_head_seat_offset"] + 3.2, parameters["screw_length"] - parameters["screw_head_seat_offset"]) + 1:
            raise ValueError("Half too shallow for recessed 16 mm hardware")
        if min(parameters["inset_lip"] + parameters["drawer_border_edge"], 2 * parameters["inset_lip"] + parameters["thickness_wall"]) < max(2 * nut_radius, parameters["interlock_width"] + 2 * parameters["interlock_clearance"]) + 2 * wall:
            raise ValueError("Widen border/shoulder to retain material around hardware and socket")
        if min(parameters["hardware_axis_height"], parameters["lip_shelf_thickness"] - parameters["hardware_axis_height"]) < max(nut_radius, parameters["interlock_height"] / 2 + parameters["interlock_clearance"]) + wall:
            raise ValueError("Shelf too thin around hardware/interlock")
        if min(parameters["interlock_width"], parameters["interlock_height"]) < 2 * oobb.gv("hole_radius_m3", "3dpr") + 2 * wall:
            raise ValueError("Interlock tongue too thin around screw bore")
        if parameters["assembly_half"] == "back":
            parameters["catch_tab_height"] = 0
    parameters["internal_lower_supports_removed"] = parameters["split_frame"] and parameters["remove_internal_lower_supports"] and parameters["row"] > 1
    parameters["corner_interlock_rows"] = ([0, parameters["row"]] if parameters["internal_lower_supports_removed"]
                                            else list(range(parameters["row"] + 1)))
    parameters["shelf_relief_active"] = parameters["split_frame"] and parameters["lightening"]
    parameters["relief_start_depth"] = (parameters["rear_band"] if parameters["assembly_half"] == "back" else parameters["front_band"])
    parameters["boss_taper_end"] = parameters["body_depth"] - parameters["hardware_boss_band"]
    parameters["boss_taper_start"] = parameters["boss_taper_end"] - (parameters["lip_shelf_thickness"] - parameters["running_shelf_thickness"]) * parameters["hardware_boss_slope"]
    if parameters["running_shelf_thickness"] < max(3.0, parameters["thickness_wall"]) or parameters["running_shelf_thickness"] > parameters["lip_shelf_thickness"]:
        raise ValueError("Running shelf must retain at least 3 mm nominal thickness and fit the joint shelf")
    if parameters["hardware_boss_slope"] < 1:
        raise ValueError("Hardware reinforcement must grow at 45 degrees or steeper")
    if parameters["shelf_relief_active"]:
        needed = max(parameters["screw_head_seat_offset"] + oobb.gv("screw_socket_cap_height_m3", "3dpr"),
                     parameters["nut_seat_offset"] + nut_depth) + parameters["hardware_min_wall"]
        if parameters["hardware_boss_band"] < needed:
            raise ValueError("Full hardware boss must surround the head/nut seats and access ends")
        if parameters["boss_taper_start"] <= parameters["relief_start_depth"]:
            raise ValueError("Half too short for the tapered shelf relief; disable lightening for short joint tests")
    if "build_height" in parameters and parameters["depth_total"] > parameters["build_height"]:
        raise ValueError("Frame print height exceeds the printer build_height")
    width = parameters["width_total"]
    if role == "bank_layout":
        width = 2 * width + parameters["module_gap"]
    parameters["ear_extension"] = (parameters["ear_diameter"] + parameters["ear_gap"]
                                    if parameters["adhesion_ears"] else 0)
    parameters["print_height_total"] = parameters["height_total"] + 2 * parameters["ear_extension"]
    if width + 2 * parameters["bed_margin"] > parameters["bed_width"] or parameters["print_height_total"] + 2 * parameters["bed_margin"] > parameters["bed_height"]:
        raise ValueError("Module including adhesion ears exceeds bed limits and bed_margin")
    # Arrange both complete footprints, including ears, without overlap.
    # Prefer a layout that fits one bed; maximum-size pairs need separate plates.
    pair_x = [2 * parameters["width_total"] + parameters["print_layout_gap"], parameters["print_height_total"]]
    pair_y = [parameters["width_total"], 2 * parameters["print_height_total"] + parameters["print_layout_gap"]]
    margin = 2 * parameters["bed_margin"]
    scores = [max((size[0] + margin) / parameters["bed_width"], (size[1] + margin) / parameters["bed_height"]) for size in [pair_x, pair_y]]
    parameters["print_layout_axis"] = 0 if scores[0] <= scores[1] else 1
    parameters["print_layout_xy"] = [pair_x, pair_y][parameters["print_layout_axis"]]
    parameters["print_layout_pitch"] = [parameters["width_total"], parameters["print_height_total"]][parameters["print_layout_axis"]] + parameters["print_layout_gap"]
    parameters["print_layout_fits_single_bed"] = min(scores) <= 1
    if 2 * parameters["opening_radius"] >= min(parameters["opening_width"], parameters["opening_height"]):
        raise ValueError("opening_radius is too large")
    if parameters["outer_radius"] > parameters["drawer_border_edge"]:
        raise ValueError("outer_radius must fit within the outside border")
    if parameters["runner_width"] < parameters["inset_lip"] + parameters["opening_radius"] or parameters["side_rail_width"] < parameters["opening_radius"]:
        raise ValueError("Edge rails must retain the stepped profile and rounded opening corners")
    parameters["lip_step_y"] = -parameters["opening_height"] / 2 + parameters["depth_lip"]
    parameters["lip_body_width"] = parameters["opening_width"] - 2 * parameters["inset_lip"]
    if parameters["lip_body_width"] <= 2 * parameters["opening_radius"] or not 2 * parameters["lip_cutout_radius"] < parameters["depth_lip"] < parameters["opening_height"]:
        raise ValueError("Lip profile dimensions do not fit the opening")
    if parameters["lip_shelf_thickness"] < parameters["thickness_wall"]:
        raise ValueError("Lip shelf must be at least as thick as the divider walls")
    parameters["lip_support_channel_height"] = min(
        parameters["opening_height"],
        parameters["lip_support_reference_height"] + parameters["container_clearance"])
    parameters["lip_support_end_y"] = -parameters["opening_height"] / 2 + parameters["lip_support_channel_height"]
    parameters["body_extension_height"] = parameters["opening_height"] - parameters["lip_support_channel_height"]
    if parameters["split_frame"]:
        # Internal junction pegs sit at the upper edge of the lower opening.
        # Check the two adjacent rounded cavities, the open reliefs and border.
        radius = parameters["corner_interlock_diameter"] / 2
        required = radius + parameters["interlock_clearance"] + parameters["corner_interlock_min_wall"]
        wall = parameters["thickness_wall"]
        lip_radius = parameters["lip_cutout_radius"]
        body_radius = parameters["opening_radius"]
        corner_limits = [parameters["drawer_border_edge"] / 2,
                         parameters["side_rail_width"], parameters["runner_width"]]
        if parameters["row"] > 1:
            if parameters["column"] > 1:
                corner_limits.extend([
                    math.hypot(wall / 2 + lip_radius, wall + lip_radius) - lip_radius,
                    math.hypot(wall / 2 + body_radius, body_radius) - body_radius,
                ])
        if required > min(corner_limits):
            raise ValueError("Corner interlock socket leaves too little material at a grid junction")
    if parameters["lip_support_channel_height"] < parameters["depth_lip"] + parameters["lip_shelf_thickness"]:
        raise ValueError("Lip support height must retain the complete bearing shelf")
    if parameters["catch_tab_width"] > parameters["opening_width"] - 2 * parameters["opening_radius"]:
        raise ValueError("catch_tab_width must fit between the opening's rounded corners")
    if parameters["catch_tab_height"] > 0:
        if parameters["catch_tab_ramp_depth"] < parameters["catch_tab_height"]:
            raise ValueError("Catch ramp must rise at least 45 degrees from the print bed")
        if parameters["catch_tab_height"] >= parameters["opening_height"] or parameters["catch_tab_ramp_depth"] + parameters["catch_tab_depth"] > min(parameters["front_band"], parameters["depth_total"]):
            raise ValueError("Catch ramp and tip must fit the opening and front band")
    if parameters["adhesion_ears"]:
        radius = parameters["ear_diameter"] / 2
        if parameters["ear_diameter"] * 2 >= parameters["width_total"]:
            raise ValueError("Corner ears must be separated")
        if parameters["ear_link_height"] > parameters["ear_height"] or parameters["ear_height"] >= parameters["depth_total"]:
            raise ValueError("Ear links must be no taller than pads, and pads shorter than the frame")
        # Links penetrate each circular pad by 0.8 mm, and the frame by 0.4 mm.
        if radius <= 0.8 or parameters["ear_link_width"] > 2 * math.sqrt(2 * radius * 0.8 - 0.8 ** 2):
            raise ValueError("Ear link must fit within the pad's attachment chord")
        if radius - parameters["ear_link_width"] / 2 <= parameters["outer_radius"] or parameters["drawer_border_edge"] <= 0.4:
            raise ValueError("Ear link must attach to a straight, solid outside edge")
    window_count = 2 if parameters["middle_rib_width"] > 0 else 1
    parameters["shelf_window_width"] = (parameters["opening_width"] - 2 * parameters["runner_width"] - parameters["middle_rib_width"]) / window_count
    parameters["side_window_lower_width"] = parameters["depth_lip"] - parameters["side_rail_width"] - parameters["lip_cutout_radius"]
    parameters["side_window_upper_width"] = parameters["opening_height"] - parameters["depth_lip"] - parameters["lip_shelf_thickness"] - parameters["side_rail_width"]
    for key in ["shelf_window_width", "side_window_lower_width", "side_window_upper_width"]:
        if parameters[key] <= 0:
            raise ValueError("Rails/ribs leave no room for relief windows")
        if role == "frame" and parameters["lightening"] and not parameters["split_frame"]:
            roof_rise = parameters[key] / 2 * parameters["roof_slope"]
            if parameters["front_band"] + parameters["rear_band"] + roof_rise >= parameters["depth_total"]:
                raise ValueError("Relief window roof does not fit within the frame depth")
    return parameters


def get_ai_version_3_summary(kwargs, copies=1):
    width = copies * kwargs["width_total"] + (copies - 1) * kwargs["module_gap"]
    layout = kwargs["split_frame"] and kwargs["assembly_half"] == "print_layout"
    return {
        "envelope_mm": [*kwargs["print_layout_xy"], kwargs["depth_total"]] if layout else [width, kwargs["print_height_total"], kwargs["depth_total"]],
        "assembled_envelope_mm": [width, kwargs["height_total"], kwargs["assembled_depth"]],
        "print_layout_fits_single_bed": kwargs["print_layout_fits_single_bed"] if layout else None,
        "print_layout_gap_mm": kwargs["print_layout_gap"] if layout else None,
        "finished_envelope_mm": [width, kwargs["height_total"], kwargs["depth_total"]],
        "adhesion_ears": kwargs["adhesion_ears"],
        "ear_count": copies * (8 if kwargs["split_frame"] and kwargs["assembly_half"] in ["assembled", "print_layout"] else 4) if kwargs["adhesion_ears"] else 0,
        "printer": kwargs.get("printer", "unspecified"),
        "build_volume_mm": [kwargs["bed_width"], kwargs["bed_height"], kwargs.get("build_height")],
        "bed_margin_mm": kwargs["bed_margin"],
        "catch_projection_mm": kwargs["catch_tab_height"],
        "catch_ramp_depth_mm": kwargs["catch_tab_ramp_depth"],
        "cutout_revision": "ai_version_3_outer_lower_supports_only",
        "internal_lower_supports_removed": kwargs["internal_lower_supports_removed"],
        "connections_per_vertical_boundary": kwargs["row"] + len(kwargs["corner_interlock_rows"]) if kwargs["split_frame"] else 0,
        "running_shelf_thickness_mm": kwargs["running_shelf_thickness"],
        "hardware_boss_band_mm": kwargs["hardware_boss_band"],
        "hardware_boss_slope": kwargs["hardware_boss_slope"],
        "shelf_relief_active": kwargs["shelf_relief_active"],
        "assembly_half": kwargs["assembly_half"] if kwargs["split_frame"] else "sample",
        "assembled_depth_mm": kwargs["assembled_depth"],
        "half_body_depth_mm": kwargs["body_depth"],
        "interlock_depth_mm": kwargs["interlock_depth"],
        "interlock_clearance_per_side_mm": kwargs["interlock_clearance"],
        "corner_interlock_diameter_mm": kwargs["corner_interlock_diameter"],
        "corner_interlock_count": (kwargs["column"] + 1) * len(kwargs["corner_interlock_rows"]) if kwargs["split_frame"] else 0,
        "screw_length_mm": kwargs["screw_length"],
        "head_seat_offset_mm": kwargs["screw_head_seat_offset"],
        "nut_seat_offset_mm": kwargs.get("nut_seat_offset"),
        "screw_count": (kwargs["column"] + 1) * kwargs["row"] if kwargs["split_frame"] else 0,
        "printable": not (kwargs["split_frame"] and kwargs["assembly_half"] == "assembled"),
        "lip_inset_mm": kwargs["inset_lip"],
        "lip_step_height_mm": kwargs["depth_lip"],
        "lip_shelf_thickness_mm": kwargs["lip_shelf_thickness"],
        "lip_support_channel_height_mm": kwargs["lip_support_channel_height"],
        "body_extension_height_mm": kwargs["body_extension_height"],
        "centre_support_width_mm": kwargs["middle_rib_width"],
        "opening_mm": [kwargs["opening_width"], kwargs["opening_height"]],
        "pitch_mm": [kwargs["pitch_x"], kwargs["pitch_y"]],
        "expected_bodies": 2 if layout else copies,
        "drawer_count": copies * kwargs["column"] * kwargs["row"],
        "part_role": kwargs["part_role"],
        "print_orientation": "Outer face on bed, joint upward; back rotates 180 degrees about Y for assembly. The assembled.scad file is reference only; use front/back files for separate plates.",
        "physical_validation": "Pending container-fit, printing, shrinkage and load tests",
    }


def get_ai_version_3_ears(thing, **kwargs):
    import math
    pos = kwargs.get("pos", [0, 0, 0])
    radius = kwargs["ear_diameter"] / 2
    # Exact cardinal vertices keep nominal footprint checks independent of $fn.
    circle = [[radius * math.cos(i * math.tau / 64), radius * math.sin(i * math.tau / 64)]
              for i in range(64)]
    for side_x in [-1, 1]:
        for side_y in [-1, 1]:
            x = pos[0] + side_x * (kwargs["width_total"] / 2 - radius)
            edge_y = pos[1] + side_y * kwargs["height_total"] / 2
            y = edge_y + side_y * (radius + kwargs["ear_gap"])
            p3 = copy.deepcopy(kwargs)
            p3.update(type="positive_positive", shape="polygon", m="",
                      points=circle, height=kwargs["ear_height"], depth=kwargs["ear_height"],
                      pos=[x, y, pos[2]], rot=[0, 0, 0])
            oobb.append_full(thing, **p3)
            # Clear gap around the pad; only this thin neck needs snapping/cutting.
            ends = [edge_y - side_y * 0.4, edge_y + side_y * (kwargs["ear_gap"] + 0.8)]
            p3 = copy.deepcopy(kwargs)
            p3.update(type="positive_positive", shape="cube", m="",
                      size=[kwargs["ear_link_width"], abs(ends[1] - ends[0]), kwargs["ear_link_height"]],
                      pos=[x - kwargs["ear_link_width"] / 2, min(ends), pos[2]], rot=[0, 0, 0])
            oobb.append_full(thing, **p3)


def get_ai_version_3_container_details(**kwargs):
    container = kwargs.get("container", "")
    kwargs["container_clearance"] = 1.5
    if container == "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209":
        kwargs["container_width"] = 86
        kwargs["container_height"] = 26
        kwargs["container_depth"] = 109
    elif container == "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214":
        # Drawing axes: across, lidless height, insertion depth.
        # The 95 mm catalogue height includes the unused 3 mm lid.
        kwargs["container_width"] = 86
        kwargs["container_height"] = 95 - 3
        kwargs["container_depth"] = 108
    return kwargs


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)

# Version 4: front/rear face plates and independently printed full-depth rails.
def get_ai_version_4_parameters(**kwargs):
    import math
    from working_oomp_populate import get_ai_version_4_defaults
    inputs = {**get_ai_version_4_defaults(), **copy.deepcopy(kwargs)}
    role = inputs.get('part_role', 'frame')
    if role not in ['frame', 'face_fit', 'modular_test']:
        raise ValueError('Unknown modular part role')
    # Read the frozen v3 dimensional mapping; do not change its geometry/defaults.
    base = {**inputs, 'part_role': 'frame', 'assembly_half': 'front', 'lightening': False}
    p = get_ai_version_3_parameters(**base)
    p.update(inputs)
    p['style'] = 'ai_version_4'
    p['part_role'] = role
    for key in ['plate_thickness', 'rail_width', 'rail_height', 'rail_running_height',
                'bottom_rail_running_height', 'rail_end_band', 'rail_taper_run',
                'rail_layout_gap', 'modular_key_depth', 'modular_screw_length', 'inner_guide_depth']:
        if not isinstance(p[key], (int, float)) or not math.isfinite(p[key]) or p[key] <= 0:
            raise ValueError(f'Invalid modular dimension: {key}')
    for key in ['modular_key_clearance', 'modular_key_end_clearance', 'rail_edge_gap']:
        if not isinstance(p[key], (int, float)) or not math.isfinite(p[key]) or p[key] < 0:
            raise ValueError(f'Invalid modular clearance: {key}')
    if p['nut_side_clearance'] not in ['left', 'right']:
        raise ValueError('Nut clearance must be left or right')
    if p['rail_height'] != 10 or p['nut_axis_height'] != 5:
        raise ValueError('The keyed mounting profile currently requires a 10 mm rail and 5 mm axis')
    p['rail_length'] = p['assembled_depth'] - 2 * p['plate_thickness']
    p['nut_depth'] = oobb.gv('nut_depth_m3', '3dpr')
    p['nut_near'] = p['modular_screw_length'] - p['plate_thickness'] - p['nut_depth']
    p['nut_far'] = p['nut_near'] + p['nut_depth']
    p['key_points'] = [[-3.5, 1.5], [3.5, 1.5], [3.5, 5], [0, 8.5], [-3.5, 5]]
    c = p['modular_key_clearance']
    p['socket_points'] = [[-3.5-c, 1.5-c], [3.5+c, 1.5-c], [3.5+c, 5+c],
                          [0, 8.5+2*c], [-3.5-c, 5+c]]
    if p['plate_thickness'] < p['catch_tab_ramp_depth'] + p['catch_tab_depth']:
        raise ValueError('Plate must contain the full outside catch ramp and tip')
    if 8.5 + 2*c + 1.0 > p['rail_height'] or 1.5-c < 1.0:
        raise ValueError('Key socket must retain at least 1 mm above and below')
    if p['nut_near'] - 0.6 < p['modular_key_depth'] + p['modular_key_end_clearance'] + 1.2:
        raise ValueError('Nut pocket too close to the alignment socket')
    if p['rail_end_band'] < p['nut_far'] + 1.5 or p['rail_length'] < 2*p['rail_end_band']:
        raise ValueError('Rail too short or end reinforcement too small')
    if not 3 <= p['rail_running_height'] <= p['bottom_rail_running_height'] <= p['rail_height']:
        raise ValueError('Keep at least 3 mm running material and a reinforced bottom rail')
    if p['rail_width']/2 < max(3.5+c+1, oobb.gv('nut_radius_m3','3dpr')+1.2):
        raise ValueError('Rail too narrow around nut/key')
    if p['rail_width']/2 > p['inset_lip']:
        raise ValueError('Universal outside rail intrudes into the container body opening')
    if p['drawer_border_edge'] < p['rail_height'] + 2*p['rail_edge_gap']:
        raise ValueError('Border must accommodate the universal top/corner rail')
    if p['inner_guide_depth'] < p['catch_tab_height']:
        raise ValueError('Inner guide must have a 45-degree or gentler lead-in')
    p['plate_print_depth'] = p['plate_thickness'] + max(p['modular_key_depth'], p['inner_guide_depth'])
    p['plate_width'] = 15.0 if role == 'modular_test' else p['width_total']
    p['plate_height'] = 14.0 if role == 'modular_test' else p['height_total']
    p['plate_footprint_height'] = p['plate_height'] + (2*p['ear_extension'] if p['adhesion_ears'] else 0)
    p['rail_positions'] = []
    start_x = -p['width_total']/2 + p['drawer_border_edge']
    start_y = -p['height_total']/2 + p['drawer_border_edge']
    if role == 'modular_test':
        p['rail_positions'] = [{'x':0, 'y':-5, 'kind':'rail'}]
    else:
        for col in range(p['column']+1):
            x = (start_x if col == 0 else start_x + (col-1)*p['pitch_x'] + p['opening_width']
                 if col == p['column'] else start_x + col*p['pitch_x'] - p['thickness_wall']/2)
            for row in range(p['row']):
                p['rail_positions'].append({'x':x, 'y':start_y+row*p['pitch_y']+p['depth_lip'], 'kind':'rail'})
            p['rail_positions'].append({'x':x, 'y':p['height_total']/2-p['drawer_border_edge']+p['rail_edge_gap'], 'kind':'rail'})
            p['rail_positions'].append({'x':x, 'y':start_y-p['rail_edge_gap']-p['rail_height'], 'kind':'bottom_rail'})
    p['rail_kinds'] = [r['kind'] for r in p['rail_positions']]
    gap = p['rail_layout_gap']
    p['rails_per_line'] = int((p['bed_width'] - 2*p['bed_margin'] + gap)//(p['rail_width']+gap))
    rows = int((p['bed_height'] - 2*p['bed_margin'] + gap)//(p['rail_length']+gap))
    p['rails_per_plate'] = p['rails_per_line'] * rows
    if min(p['rails_per_line'], rows) < 1:
        raise ValueError('A rail does not fit the declared bed')
    p['rail_plate_count'] = math.ceil(len(p['rail_kinds'])/p['rails_per_plate'])
    p['bom'] = {'front':1, 'back':1, 'rail':p['rail_kinds'].count('rail'),
                'bottom_rail':p['rail_kinds'].count('bottom_rail'),
                'M3_countersunk_screw_16_mm':2*len(p['rail_kinds']), 'M3_nut':2*len(p['rail_kinds'])}
    if role == 'face_fit':
        p['bom'] = {'front':1, 'back':0, 'rail':0, 'bottom_rail':0,
                    'M3_countersunk_screw_16_mm':0, 'M3_nut':0}
    return p


def get_ai_version_4_views(p):
    if p['part_role'] == 'face_fit':
        return {name:name for name in ['face_plate','front','back']}
    views = {name:name for name in ['face_plate','front','back','rail','bottom_rail','assembled']}
    views.update({f'rails_plate_{i+1:02d}':f'rails_plate_{i+1:02d}' for i in range(p['rail_plate_count'])})
    return views


def get_ai_version_4(thing, **kwargs):
    import math
    import working_scad_container_cutout as cuts
    p = get_ai_version_4_parameters(**kwargs)
    view = p['modular_view']
    if p['part_role'] == 'face_fit' and view == 'print_layout':
        view = 'face_plate'
    origin = p.get('pos', [0,0,0])

    def component(kind, shift, assembled=False, rear=False):
        sub = oobb.get_default_thing(type='modular_component')
        q = {**copy.deepcopy(p), 'modular_component':kind}
        q['include_forward_lip'] = p['rear_lip'] if rear else p['front_lip']
        q.pop('pos', None)
        if kind == 'face_plate':
            p3 = {
                **copy.deepcopy(q),
                'type':'positive', 'shape':'rounded_rectangle', 'm':'',
                'size':[p['plate_width'], p['plate_height'], p['plate_thickness']],
                'radius':p['outer_radius'], 'pos':[0,0,0],
            }
            oobb.append_full(sub, **p3)
            if p['part_role'] != 'modular_test':
                for row in range(p['row']):
                    for col in range(p['column']):
                        cell = [-p['width_total']/2+p['drawer_border_edge']+p['opening_width']/2+col*p['pitch_x'],
                                -p['height_total']/2+p['drawer_border_edge']+p['opening_height']/2+row*p['pitch_y'], 0]
                        cuts.get_container_cutout_ai_version_4(cell, sub, **dict(q, row_index=row, column_index=col))
            cuts.get_container_cutout_ai_version_4([0,0,0], sub, **dict(q, modular_component='plate_mounts'))
            if p['adhesion_ears']:
                get_ai_version_3_ears(sub, **q)
            rot = [0,180,0] if rear and assembled else [0,0,0]
        else:
            p3 = {
                **copy.deepcopy(q),
                'type':'positive', 'shape':'cube', 'm':'',
                'size':[p['rail_width'],p['rail_height'],p['rail_length']],
                'pos':[-p['rail_width']/2,0,0],
            }
            oobb.append_full(sub, **p3)
            cuts.get_container_cutout_ai_version_4([0,0,0], sub, **q)
            rot = [0,0,0] if assembled else [90,0,0]
            if not assembled:
                shift = [shift[0],shift[1]+p['rail_length']/2,shift[2]]
        thing['components'].append({'type':'rotation','typetype':'positive',
                                    'pos':[origin[i]+shift[i] for i in range(3)],'rot':rot,'objects':sub['components']})

    def rail_layout(kinds, shift):
        columns = min(p['rails_per_line'],len(kinds))
        rows = math.ceil(len(kinds)/columns)
        width = columns*(p['rail_width']+p['rail_layout_gap'])-p['rail_layout_gap']
        height = rows*(p['rail_length']+p['rail_layout_gap'])-p['rail_layout_gap']
        for index, kind in enumerate(kinds):
            x = -width/2+p['rail_width']/2+(index%columns)*(p['rail_width']+p['rail_layout_gap'])
            y = -height/2+p['rail_length']/2+(index//columns)*(p['rail_length']+p['rail_layout_gap'])
            component(kind,[shift[0]+x,shift[1]+y,0])
        return width,height

    count = 1
    if view in ['face_plate','front','back']:
        component('face_plate',[0,0,0],rear=view == 'back')  # face_plate aliases front.
    elif view in ['rail','bottom_rail']:
        component(view,[0,0,0])
    elif view == 'assembled':
        component('face_plate',[0,0,0])
        component('face_plate',[0,0,p['assembled_depth']],assembled=True,rear=True)
        for rail in p['rail_positions']:
            component(rail['kind'],[rail['x'],rail['y'],p['plate_thickness']],assembled=True)
        count = 1
    elif view.startswith('rails_plate_'):
        index = int(view.rsplit('_',1)[-1])-1
        kinds = p['rail_kinds'][index*p['rails_per_plate']:(index+1)*p['rails_per_plate']]
        if not kinds:
            raise ValueError('Empty rail print plate')
        rail_layout(kinds,[0,0,0]); count = len(kinds)
    elif view == 'print_layout':
        gap = p['print_layout_gap']
        component('face_plate',[-(p['plate_width']+gap)/2,0,0])
        component('face_plate',[(p['plate_width']+gap)/2,0,0],rear=True)
        rows = math.ceil(len(p['rail_kinds'])/min(p['rails_per_line'],len(p['rail_kinds'])))
        height = rows*(p['rail_length']+p['rail_layout_gap'])-p['rail_layout_gap']
        rail_layout(p['rail_kinds'],[0,(p['plate_footprint_height']+height)/2+gap,0])
        count = len(p['rail_kinds'])+2
    else:
        raise ValueError(f'Unknown modular view: {view}')
    thing['ai_design'] = {'style':'ai_version_4', 'view':view, 'expected_bodies':count,
                          'bom':p['bom'], 'rail_length_mm':p['rail_length'],
                          'plate_size_mm':[p['plate_width'],p['plate_height'],p['plate_thickness']],
                          'assembled_envelope_mm':[p['width_total'],p['height_total'],p['assembled_depth']],
                          'identical_front_and_back':p['part_role'] == 'modular_test' or p['front_lip'] == p['rear_lip'],
                          'front_lip':p['front_lip'], 'rear_lip':p['rear_lip'],
                          'nut_side_clearance':p['nut_side_clearance'],
                          'printable':view != 'assembled', 'part_role':p['part_role']}


def get_ai_version_5_parameters(**kwargs):
    if kwargs.get('connector_design') == 'recessed_twin_fit_suite':
        p = get_ai_version_5_parameters(**dict(kwargs,connector_design='snap_recessed_twin'))
        p['connector_design'] = 'recessed_twin_fit_suite'
        numbers = [25,26,28,29] if p.get('variant') == 'recessed_twin_heavy_suite' else [23,24,25,26]
        if len(p['latch_trials']) != 4 or [t['sample_number'] for t in p['latch_trials']] != numbers:
            raise ValueError(f'Latch thickness suite requires numbered pairs {numbers}')
        for trial in p['latch_trials']:
            get_ai_version_5_parameters(**{**p,**trial,'connector_design':'snap_recessed_twin'})
        return p
    if kwargs.get('connector_design') == 'tiled_hybrid':
        from working_scad_tiling import parameters
        return parameters(kwargs)
    import math
    from working_oomp_populate import get_ai_version_5_defaults
    p = {**get_ai_version_5_defaults(), **copy.deepcopy(kwargs)}
    designs = ['snap_single', 'snap_twin', 'snap_key', 'screw_reference', 'connector_suite', 'key_size_fit_suite', 'snap_recessed_twin']
    if p.get('connector_design') not in designs or p['part_role'] != 'connector_test':
        raise ValueError('Version 5 currently supports connector coupons only')
    for name, default in get_ai_version_5_defaults().items():
        if isinstance(default, (int, float)):
            if not isinstance(p[name], (int, float)) or not math.isfinite(p[name]):
                raise ValueError(f'Invalid connector parameter: {name}')
            if (p[name] >= 0 if name == 'key_head_x' else p[name] <= 0):
                raise ValueError(f'Invalid connector parameter: {name}')
    if p['rail_width'] != 11 or p['rail_height'] != 10 or p['plate_thickness'] != 7.5:
        raise ValueError('Keep these trials at the current 11 x 10 / 7.5 mm interface scale')
    if p['connector_design'] == 'snap_recessed_twin':
        p['arm_thickness'] = p['twin_arm_thickness']
        p['root_distance'] = p['twin_root_distance']
        p['hook_shoulder_z'] = -p['recessed_shoulder_depth']
        p['hook_tip_z'] = p['hook_shoulder_z']-p['hook_ramp_length']
        p['insertion_deflection'] = p['hook_projection']-p['connector_clearance']
        p['open_center_half_width'] = p['snap_arm_outer']-p['arm_thickness']
        p['receiver_shoulder_z'] = p['plate_thickness']+p['hook_shoulder_z']+p['catch_end_clearance']
        p['receiver_pocket_half_width'] = p['snap_arm_outer']+p['hook_projection']+p['connector_clearance']
        if not 0.5 <= p['insertion_deflection'] <= 1.1:
            raise ValueError('Aggressive tab deflection must stay in the trial range')
        if p['open_center_half_width'] <= p['insertion_deflection']+0.3:
            raise ValueError('Open centre must leave both tabs room to flex')
        if abs(p['plate_thickness']+p['hook_tip_z']) > 0.000001 or not 1.5 <= p['receiver_shoulder_z'] <= 2.5:
            raise ValueError('Keep tips flush and retaining shoulders near the front edge')
        if p['coupon_width']/2-p['receiver_pocket_half_width'] < 2:
            raise ValueError('Internal pockets must retain at least 2 mm side walls')
        heavy_trial = p.get('heavy_latch_trial',False) and p.get('sample_number') in [28,29]
        thickness_trial = p.get('latch_thickness_trial',False) and (p.get('sample_number') in [23,24,25,26] or heavy_trial)
        maximum_thickness = 2.0 if heavy_trial and thickness_trial else 1.6 if thickness_trial else 1.1
        if not 0 < p['root_distance'] <= 1 or not 0.9 <= p['arm_thickness'] <= maximum_thickness:
            raise ValueError('Short flush tabs need shallow root relief and thin trial walls')
        if p['root_distance']+p['open_center_half_width'] >= p['number_rail_z']-4:
            raise ValueError('Keep the rounded slot root clear of the numbered grip')
        if p['snap_arm_height'] != p['rail_height'] or (p['sample_number'] != 19 and not thickness_trial):
            raise ValueError('Recessed twin coupon uses full-height tabs and number 19')
        # Full-width beam starts at Z=0. Do not count the root relief as
        # additional free cantilever length in this screening estimate.
        p['effective_arm_length'] = -p['hook_shoulder_z']
        p['estimated_arm_strain'] = 1.5*p['arm_thickness']*p['insertion_deflection']/p['effective_arm_length']**2
        return p
    p['arm_thickness'] = p['single_arm_thickness'] if p['connector_design'] == 'snap_single' else p['twin_arm_thickness']
    tight_key = p.get('tight_key_trial',False)
    if tight_key:
        if p['connector_design'] != 'snap_key' or p.get('sample_number') != 27:
            raise ValueError('Tight key is a separate sample 27 trial')
        gap = p['key_latch_clearance']
        if not isinstance(gap,(int,float)) or not math.isfinite(gap) or not 0.05 <= gap <= 0.2:
            raise ValueError('Keep a small positive key latch clearance, 0.05 to 0.2 mm per face')
        # Head and recovered latch bear on opposite faces of the existing 22
        # tongue. Only the key changes; the transverse slot stays untouched.
        p['key_head_length'] = -p['key_tongue_half_width']-gap-p['key_head_x']
        p['key_shoulder_x'] = p['key_tongue_half_width']+gap
    p['root_distance'] = p['single_root_distance'] if p['connector_design'] == 'snap_single' else p['twin_root_distance']
    p['hook_shoulder_z'] = -p['plate_thickness'] - p['catch_end_clearance']
    p['hook_tip_z'] = p['hook_shoulder_z'] - p['hook_ramp_length']
    p['insertion_deflection'] = p['hook_projection'] - p['connector_clearance']
    p['key_z'] = -(p['plate_thickness'] + p['key_half_width'] + p['hook_projection'] + p['catch_end_clearance'])
    p['key_tongue_depth'] = -p['key_z'] + p['key_half_width'] + p['connector_clearance'] + 1.6
    key_extension = (p.get('sample_number') in [20,21,22] or tight_key) and p['connector_design'] == 'snap_key'
    deflection_limit = 0.65*p['key_scale'] if key_extension else 0.65
    if not 0 < p['insertion_deflection'] < deflection_limit:
        raise ValueError('Hook must retain positive engagement without excessive deflection')
    if p['snap_arm_outer'] - p['arm_thickness'] - p['guide_half_width'] < p['insertion_deflection'] + 0.25:
        raise ValueError('Arm needs free travel beside the rigid guide')
    if p['root_distance'] + 2 >= p['test_rail_length'] or p['root_radius'] > p['arm_thickness']:
        raise ValueError('Invalid cantilever root')
    if p['key_half_width'] - p['key_arm_thickness'] < p['insertion_deflection'] + 0.1:
        raise ValueError('Locking-key arms would collide during insertion')
    if p['key_root_radius'] >= p['key_half_width']-p['key_arm_thickness']:
        raise ValueError('Key fillets must leave an open fork gap')
    p['effective_arm_length'] = p['root_distance'] - p['root_radius'] - p['hook_shoulder_z']
    # Screening calculation only: rectangular cantilever, imposed tip deflection.
    # No material limit, force rating or FEA claim is derived from this.
    p['estimated_arm_strain'] = 1.5 * p['arm_thickness'] * p['insertion_deflection'] / p['effective_arm_length']**2
    p['estimated_key_strain'] = 1.5 * p['key_arm_thickness'] * p['insertion_deflection'] / (p['key_shoulder_x'] - (p['key_head_x']+p.get('key_head_length',2)) - p['key_root_radius'])**2
    if p.get('sample_number'):
        if p['sample_number'] not in list(range(1,19))+[20,21,22] and not tight_key:
            raise ValueError('Numbered key trials use 1 through 18 and 20 through 22')
        if not 0 < p['number_depth'] <= 1 or not 3 <= p['number_size'] <= 6:
            raise ValueError('Keep the recessed number shallow and within the rail grip')
        min_wall = p.get('key_slot_min_wall',1.5) if key_extension else 1.5
        if min_wall < 1 or p['key_height']+2*p['connector_clearance'] > p['rail_height']-2*min_wall:
            raise ValueError('Key slot must retain material above and below')
    if 'through_taper_length' in p:
        if not -0.025 <= p['through_seat_interference'] <= 0.05:
            raise ValueError('Through fit must stay between 0.025 mm clearance and 0.05 mm interference per side')
        if not 0.1 <= p['through_clearance'] <= 0.3 or not 5 <= p['through_taper_length'] <= p['plate_thickness']:
            raise ValueError('Keep a gentle taper confined to the plate engagement')
    return p


def get_ai_version_5_views(p):
    if p['connector_design'] == 'recessed_twin_fit_suite':
        return {'assembled':'assembled', **{
            f"{name}_{t['sample_number']:02d}":f"{name}_{t['sample_number']:02d}"
            for t in p['latch_trials'] for name in ['trial','plate','rail','assembled']
        }}
    if p['connector_design'] == 'tiled_hybrid':
        from working_scad_tiling import views
        return views(p)
    if p['connector_design'] == 'key_size_fit_suite':
        views = {'assembled':'assembled'}
        for trial in p['key_trials']:
            for name in ['trial','plate','rail','key','assembled']:
                view = f"{name}_{trial['sample_number']:02d}"
                views[view] = view
        return views
    if p['connector_design'] == 'connector_suite':
        return {'assembled': 'assembled'}
    views = {n:n for n in ['plate', 'rail', 'assembled']}
    if p['connector_design'] == 'snap_key':
        views['key'] = 'key'
    return views


def get_ai_version_5(thing, **kwargs):
    if kwargs.get('connector_design') == 'tiled_hybrid':
        return get_ai_version_5_tiled(thing, **kwargs)
    import working_scad_container_cutout as cuts
    p = get_ai_version_5_parameters(**kwargs)
    view = p['connector_view']
    design = p['connector_design']
    origin = p.get('pos', [0,0,0])
    if design == 'recessed_twin_fit_suite':
        if view not in ['print_layout','assembled']:
            name, number = view.rsplit('_',1)
            trial = next(t for t in p['latch_trials'] if t['sample_number']==int(number))
            get_ai_version_5(thing, **{**p,**trial,'connector_design':'snap_recessed_twin',
                                     'connector_view':'print_layout' if name=='trial' else name})
            return
        for index, trial in enumerate(p['latch_trials']):
            sub = oobb.get_default_thing(type='latch_thickness_pair')
            get_ai_version_5(sub, **{**p,**trial,'connector_design':'snap_recessed_twin','pos':[0,0,0]})
            shift = [-24 if index%2==0 else 24,27 if index<2 else -27,0]
            thing['components'].append({
                'type':'rotation','typetype':'positive','rot':[0,0,0],
                'pos':[origin[i]+shift[i] for i in range(3)],'objects':sub['components'],
            })
        thing['ai_design'] = {
            'style':'ai_version_5','view':view,'expected_bodies':8,
            'printable':view!='assembled','part_role':'connector_test',
            'connector_design':design,'material':'PETG','numbered_trials':p['latch_trials'],
        }
        return
    if design == 'key_size_fit_suite':
        if view not in ['print_layout','assembled']:
            name, number = view.rsplit('_',1)
            trial = next(t for t in p['key_trials'] if t['sample_number'] == int(number))
            get_ai_version_5(thing, **{**p, **trial, 'connector_design':'snap_key',
                                     'connector_view':'print_layout' if name == 'trial' else name})
            return
        total = 0
        for index, trial in enumerate(p['key_trials']):
            shift = [(index%3-1)*48, p.get('trial_layout_y_offset',54)-(index//3)*54, 0]
            sub = oobb.get_default_thing(type='numbered_key_trial')
            get_ai_version_5(sub, **{**p, **trial, 'connector_design':'snap_key', 'pos':[0,0,0]})
            thing['components'].append({
                'type':'rotation', 'typetype':'positive', 'rot':[0,0,0],
                'pos':[origin[i]+shift[i] for i in range(3)], 'objects':sub['components'],
            })
            total += sub['ai_design']['expected_bodies']
        thing['ai_design'] = {'style':'ai_version_5','view':view,'expected_bodies':total,
                              'printable':view != 'assembled','part_role':'connector_test',
                              'connector_design':design,'material':'PETG',
                              'numbered_trials':p['key_trials']}
        return
    if design == 'connector_suite':
        total = 0
        for index, name in enumerate(['snap_single', 'snap_twin', 'snap_key', 'screw_reference']):
            shift = [-28 if index % 2 == 0 else 28, 30 if index < 2 else -30, 0]
            sub = oobb.get_default_thing(type='connector_trial')
            get_ai_version_5(sub, **dict(p, connector_design=name, pos=[0,0,0]))
            thing['components'].append({
                'type':'rotation', 'typetype':'positive', 'rot':[0,0,0],
                'pos':[origin[i]+shift[i] for i in range(3)], 'objects':sub['components'],
            })
            total += sub['ai_design']['expected_bodies']
        thing['ai_design'] = {'style':'ai_version_5', 'view':view, 'expected_bodies':total,
                              'printable':view != 'assembled', 'part_role':'connector_test',
                              'connector_design':design, 'material':'PETG'}
        return

    def component(kind, shift, assembled=False):
        sub = oobb.get_default_thing(type='connector_component')
        if design == 'screw_reference':
            from working_oomp_populate import get_ai_version_4_options
            control = copy.deepcopy(next(o for o in get_ai_version_4_options() if o['part_role'] == 'modular_test'))
            control.update(joint_test_depth=p['test_rail_length']+2*p['plate_thickness'],
                           modular_view='front' if kind == 'plate' else 'rail', pos=[0,0,0])
            get_ai_version_4(sub, **control)
            rot = [-90,0,0] if assembled and kind == 'rail' else [0,0,0]
            if kind == 'plate':
                shift = [shift[0],shift[1]+5,shift[2]]
            elif assembled:
                shift = [shift[0],shift[1],shift[2]+p['test_rail_length']/2]
        else:
            q = {**copy.deepcopy(p), 'connector_component':kind}
            q.pop('pos', None)
            if kind == 'plate':
                size = [p['coupon_width'],p['coupon_height'],p['plate_thickness']]
                base = [-p['coupon_width']/2, (p['rail_height']-p['coupon_height'])/2, 0]
            elif kind == 'rail':
                size = [p['rail_width'],p['rail_height'],p['test_rail_length']]
                base = [-p['rail_width']/2,0,0]
                if design == 'snap_recessed_twin':
                    # Carve both tabs from one solid envelope; no coplanar
                    # positive-tab unions that can leave degenerate STL seams.
                    size[2] -= p['hook_tip_z']
                    base[2] = p['hook_tip_z']
            else:
                # One solid envelope, carved into the fork by the cutout.
                size = [p['key_shoulder_x']+p['hook_ramp_length']-p['key_head_x'],
                        p['key_height'],2*(p['key_half_width']+p['hook_projection'])]
                base = [p['key_head_x'],0,-size[2]/2]
            p3 = {
                **copy.deepcopy(q),
                'type':'positive', 'shape':'cube', 'm':'',
                'size':size, 'pos':base,
            }
            oobb.append_full(sub, **p3)
            cuts.get_container_cutout_ai_version_5([0,0,0], sub, **q)
            rot = [0,0,0] if assembled or kind == 'plate' else [90,0,0]
            if design == 'snap_recessed_twin' and kind == 'plate' and not assembled:
                # Narrow entry on the bed; larger internal catch pocket above.
                # Material retreats at the ledge, so there is no hanging roof.
                rot = [0,180,0]
                shift = [shift[0],shift[1],shift[2]+p['plate_thickness']]
            if not assembled and kind == 'rail':
                tip = -p['key_tongue_depth'] if design == 'snap_key' else p['hook_tip_z']
                shift = [shift[0],shift[1]+(p['test_rail_length']+tip)/2,shift[2]]
        thing['components'].append({
            'type':'rotation', 'typetype':'positive', 'rot':rot,
            'pos':[origin[i]+shift[i] for i in range(3)], 'objects':sub['components'],
        })

    count = 1
    if view == 'print_layout':
        component('plate',[-12,-5,0])
        component('rail',[12,0,0])
        count = 2
        if design == 'snap_key':
            component('key',[-12,-18,0]); count += 1
    elif view == 'assembled':
        component('plate',[0,0,0],assembled=True)
        component('rail',[0,0,p['plate_thickness']],assembled=True)
        count = 2
        if design == 'snap_key':
            component('key',[0,(p['rail_height']-p['key_height'])/2,
                             p['plate_thickness']+p['key_z']],assembled=True)
            count += 1
    elif view in ['plate','rail','key']:
        if view == 'key' and design != 'snap_key':
            raise ValueError('Only the locking-key trial has a separate key')
        component(view,[0,-5 if view == 'plate' else 0,0])
    else:
        raise ValueError(f'Unknown connector view: {view}')
    thing['ai_design'] = {
        'style':'ai_version_5', 'view':view, 'connector_design':design,
        'expected_bodies':count, 'printable':view != 'assembled',
        'part_role':'connector_test', 'material':'PETG',
        'insertion_deflection_mm':p['insertion_deflection'],
        'screening_cantilever_strain':p['estimated_key_strain'] if design == 'snap_key' else p['estimated_arm_strain'],
        'hardware':{'M3_countersunk_16_mm':1,'M3_nut':1} if design == 'screw_reference' else {},
    }
    if p.get('sample_number'):
        thing['ai_design']['sample_number'] = p['sample_number']

def get_ai_version_5_tiled(thing, **kwargs):
    import math
    import working_scad_container_cutout as cuts
    from working_scad_tiling import bed_pose
    p = get_ai_version_5_parameters(**kwargs)
    view = p['connector_view']
    origin = p.get('pos',[0,0,0])
    p.pop('pos',None)

    def place(sub, shift, rot=(0,0,0)):
        thing['components'].append({
            'type':'rotation', 'typetype':'positive', 'rot':list(rot),
            'pos':[origin[i]+shift[i] for i in range(3)], 'objects':sub['components'],
        })

    def tile_component(tile, rear=False, assembled=False, overview=None):
        q = copy.deepcopy(p)
        q.pop('pos',None)
        q['include_forward_lip'] = p['rear_lip'] if rear else p['front_lip']
        layers = copy.deepcopy(tile['layers'])
        notches = copy.deepcopy(tile['notches'])
        if rear:
            layers = [[-b[2],b[1],-b[0],b[3]] for b in layers]
            notches = [[[-b[2],b[1],-b[0],b[3]] for b in group] for group in notches]
            for rail in q['rail_positions']:
                rail['x'] = -rail['x']
        bounds = [min(b[0] for b in layers),min(b[1] for b in layers),
                  max(b[2] for b in layers),max(b[3] for b in layers)]
        body = oobb.get_default_thing(type='tiled_plate')
        p3 = {
            **copy.deepcopy(q), 'type':'positive', 'shape':'rounded_rectangle', 'm':'',
            'size':[p['width_total'],p['height_total'],p['plate_thickness']],
            'radius':p['outer_radius'], 'pos':[0,0,0],
        }
        oobb.append_full(body, **p3)
        cuts.get_container_cutout_ai_version_5_tiled([0,0,0],body,
            **dict(q,tiled_component='plate',tile_bounds=bounds))
        # Crop AFTER catches/keys are unioned, so no off-tile positive features survive.
        sub = oobb.get_default_thing(type='tile_crop')
        sub['components'].append({'type':'rotation','typetype':'positive',
                                  'rot':[0,0,0],'pos':[0,0,0],'objects':body['components']})
        cuts.get_container_cutout_ai_version_5_tiled([0,0,0],sub,
            **dict(q,tiled_component='tile_mask',tile_layers=layers,tile_notches=notches))
        if assembled:
            place(sub,[0,0,p['assembled_depth'] if rear else 0],[0,180,0] if rear else [0,0,0])
            return
        cropped = sub
        sub = oobb.get_default_thing(type='tile_with_ears')
        flip = tile['bed_layer'] == 1
        sub['components'].append({
            'type':'rotation','typetype':'positive','rot':[180,0,0] if flip else [0,0,0],
            'pos':[0,0,p['plate_thickness'] if flip else 0],'objects':cropped['components'],
        })
        if flip:
            layers = [[b[0],-b[3],b[2],-b[1]] for b in layers]
            bounds = [bounds[0],-bounds[3],bounds[2],-bounds[1]]
        # Four 12 mm ears, joined by 0.2 mm thick removable necks. The ends sit
        # within the full-thickness core so both lap directions attach to the bed.
        core = layers[tile['bed_layer']]
        radius = p['tile_ear_diameter']/2
        # At an internal lap the bed-side land can be under 1 mm wide. Put
        # its ear neck directly on that land, never in the neighbouring opening.
        inset = p['tile_lap_x']/2-p['tile_seam_clearance']/2+5.8
        xs = [bounds[0]+8 if abs(bounds[0]+p['width_total']/2)<1e-6 else bounds[0]+inset,
              bounds[2]-8 if abs(bounds[2]-p['width_total']/2)<1e-6 else bounds[2]-inset]
        xs = [max(bounds[0]+radius,min(bounds[2]-radius,x)) for x in xs]
        for x in xs:
            for sign in [-1,1]:
                edge = bounds[1] if sign == -1 else bounds[3]
                core_edge = core[1] if sign == -1 else core[3]
                y = edge+sign*(p['tile_ear_gap']+radius)
                p3 = {
                    **copy.deepcopy(q),'type':'positive','shape':'cylinder','m':'',
                    'r':radius,'h':p['tile_ear_height'],'pos':[x,y,0],
                }
                oobb.append_full(sub,**p3)
                low,high = sorted([core_edge-sign*0.1,y])
                p3 = {
                    **copy.deepcopy(q),'type':'positive','shape':'cube','m':'',
                    'size':[p['tile_ear_link_width'],high-low,p['tile_ear_link_height']],
                    'pos':[x-p['tile_ear_link_width']/2,low,0],
                }
                oobb.append_full(sub,**p3)
        center = [(bounds[0]+bounds[2])/2,(bounds[1]+bounds[3])/2]
        target = overview if overview is not None else tile['bed_center']
        place(sub,[target[0]-center[0],target[1]-center[1],0])

    def rail_component(kind, shift, assembled=False):
        sub = oobb.get_default_thing(type='hybrid_rail')
        snap = kind.startswith('snap_')
        tip = p['plate_thickness'] if snap else 0
        p3 = {
            **copy.deepcopy(p),'type':'positive','shape':'cube','m':'',
            'size':[p['rail_width'],p['rail_height'],p['rail_length']+2*tip],
            'pos':[-p['rail_width']/2,0,-tip],
        }
        oobb.append_full(sub,**p3)
        cuts.get_container_cutout_ai_version_5_tiled([0,0,0],sub,
            **dict(p,tiled_component=kind))
        if assembled:
            place(sub,shift)
        else:
            place(sub,[shift[0],shift[1]+p['rail_length']/2,0],[90,0,0])

    def batch(kinds, target=None):
        cols = min(p['rails_per_line'],len(kinds))
        rows = math.ceil(len(kinds)/cols)
        pitch_x = p['rail_width']+p['rail_layout_gap']
        length = p['rail_length']+2*p['plate_thickness']
        pitch_y = length+p['rail_layout_gap']
        width,height = cols*pitch_x-p['rail_layout_gap'],rows*pitch_y-p['rail_layout_gap']
        center = target if target is not None else bed_pose(width,height,p)
        if center is None:
            raise ValueError('Rail batch intersects the printer exclusion')
        for i,kind in enumerate(kinds):
            rail_component(kind,[center[0]-width/2+p['rail_width']/2+(i%cols)*pitch_x,
                                 center[1]-height/2+length/2+(i//cols)*pitch_y,0])

    count = 0
    if '_tile_' in view:
        side, number = view.split('_tile_')
        tile_component(p['tiles'][int(number)-1],rear=side=='back')
        count = 1
    elif view in ['front','back','assembled']:
        for rear in ([False,True] if view=='assembled' else [view=='back']):
            for tile in p['tiles']:
                tile_component(tile,rear=rear,assembled=True)
                count += 1
        if view == 'assembled':
            for rail in p['rail_positions']:
                rail_component(rail['file'],[rail['x'],rail['y'],p['plate_thickness']],True)
                count += 1
    elif view in set(p['rail_kinds']):
        rail_component(view,[0,0,0]); count = 1
    elif view.startswith('rails_plate_'):
        index = int(view.rsplit('_',1)[-1])-1
        kinds = p['rail_kinds'][index*p['rails_per_plate']:(index+1)*p['rails_per_plate']]
        batch(kinds); count = len(kinds)
    elif view == 'print_layout':
        for side,rear in enumerate([False,True]):
            for i,tile in enumerate(p['tiles']):
                tile_component(tile,rear=rear,overview=[tile['column']*270,(tile['row']+side*2)*280])
                count += 1
        for i in range(p['rail_plate_count']):
            kinds=p['rail_kinds'][i*p['rails_per_plate']:(i+1)*p['rails_per_plate']]
            batch(kinds,[i*270,-280]); count += len(kinds)
    else:
        raise ValueError(f'Unknown tiled view: {view}')
    thing['ai_design'] = {
        'style':'ai_version_5','part_role':'frame','connector_design':'tiled_hybrid',
        'view':view,'expected_bodies':count,'bom':p['bom'],
        'printable':view not in ['front','back','assembled'],
        'fits_one_bed':view not in ['front','back','assembled','print_layout'],
        'assembled_envelope_mm':[p['width_total'],p['height_total'],p['assembled_depth']],
        'tile_count_per_face':len(p['tiles']), 'physical_fit':'Unverified PETG demo',
    }
