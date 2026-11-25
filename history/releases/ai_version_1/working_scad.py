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
        kwargs["filter"] = build_variables["filter"]
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


# Version 2 is an independent development copy of the released version 1.
def get_ai_version_2(thing, **kwargs):
    kwargs = get_ai_version_2_parameters(**kwargs)
    pos = copy.deepcopy(kwargs.pop("pos", [0, 0, 0]))

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


def get_ai_version_2_summary(kwargs, copies=1):
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

    
if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)
