import copy
from turtle import position
import oobb
import yaml
import os
import scad_help


def get_base(pos, thing, **kwargs):
    if kwargs.get("style") == "ai_version_1":
        #get_container_cutout_ai_version_1(pos, thing, **kwargs)
        get_container_cutout_ai_version_2(pos, thing, **kwargs)
    else:
        get_container_cutout_version_1(pos, thing, **kwargs)

def get_container_cutout_ai_version_1(pos, thing, **kwargs):
    # Through opening; epsilon avoids coincident faces at both ends.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "n",
        "shape": "rounded_rectangle",
        "m": "#",
        "size": [kwargs["opening_width"], kwargs["opening_height"], kwargs["depth_total"] + 0.2],
        "radius": kwargs["opening_radius"],
        "pos": [pos[0], pos[1], pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # All material-saving cuts for this cell live here, relative to its centre.
    # Adjacent cells deliberately repeat shared-wall cuts: subtracting the same
    # space twice is harmless and keeps each cutout complete on its own.
    if kwargs["lightening"] and kwargs["part_role"] == "frame":
        wall = kwargs["thickness_wall"]
        border = kwargs["drawer_border_edge"]
        row_index = kwargs.get("row_index", 0)
        column_index = kwargs.get("column_index", 0)
        bottom = kwargs["front_band"]
        top = kwargs["depth_total"] - kwargs["rear_band"]

        # Two windows through BOTH the floor and ceiling of this drawer.
        # The pointed end retains the existing supportable closing roof.
        half = kwargs["shelf_window_width"] / 2
        shoulder = top - half * kwargs["roof_slope"]
        offset = (kwargs["middle_rib_width"] + kwargs["shelf_window_width"]) / 2
        for side_y in [-1, 1]:
            outside = (side_y == -1 and row_index == 0) or (side_y == 1 and row_index == kwargs["row"] - 1)
            thickness = border if outside else wall
            y = pos[1] + side_y * (kwargs["opening_height"] / 2 + thickness / 2)
            for side_x in [-1, 1]:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "n",
                    "shape": "polygon",
                    "m": "",
                    "height": thickness + 0.2,
                    "depth": thickness + 0.2,
                    "points": [
                        [-half, bottom],
                        [half, bottom],
                        [half, shoulder],
                        [0, top],
                        [-half, shoulder],
                    ],
                    "rot": [90, 0, 0],
                    "pos": [pos[0] + side_x * offset, y + thickness / 2 + 0.1, pos[2]],
                }
                oobb.append_full(thing, **p3)

        # One window through EACH side wall, retaining the corner rails.
        half = kwargs["side_window_width"] / 2
        shoulder = top - half * kwargs["roof_slope"]
        for side_x in [-1, 1]:
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            thickness = border if outside else wall
            x = pos[0] + side_x * (kwargs["opening_width"] / 2 + thickness / 2)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "n",
                "shape": "polygon",
                "m": "",
                "height": thickness + 0.2,
                "depth": thickness + 0.2,
                "points": [
                    [-half, bottom],
                    [half, bottom],
                    [half, shoulder],
                    [0, top],
                    [-half, shoulder],
                ],
                "rot": [90, 0, 90],
                "pos": [x - thickness / 2 - 0.1, pos[1], pos[2]],
            }
            oobb.append_full(thing, **p3)

    # A supportable ramp grows into the opening from the shelf at Z=0.
    # Local polygon coordinates are (projection into opening, print Z).
    # Extrude along X; add after subtraction so the cavity cannot erase it.
    if kwargs.get("catch_tab_height", 0) > 0:
        projection = kwargs["catch_tab_height"]
        ramp = kwargs["catch_tab_ramp_depth"]
        tip_end = ramp + kwargs["catch_tab_depth"]
        wall = kwargs["thickness_wall"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "positive_positive",
            "shape": "polygon",
            "m": "#",
            "height": kwargs["catch_tab_width"],
            "depth": kwargs["catch_tab_width"],
            "points": [
                [-wall, 0],
                [0, 0],
                [projection, ramp],
                [projection, tip_end],
                [-wall, tip_end],
            ],
            "rot": [90, 0, 90],
            "pos": [pos[0] - kwargs["catch_tab_width"] / 2,
                    pos[1] - kwargs["opening_height"] / 2, pos[2]],
        }
        oobb.append_full(thing, **p3)

def get_container_cutout_ai_version_2(pos, thing, **kwargs):
    # Preserve the user's two-piece stepped opening. The lip-bearing ledge is
    # at lip_step_y; the reliefs below deliberately avoid that entire shelf.
    opening_width = kwargs["opening_width"]
    opening_height = kwargs["opening_height"]
    depth_total = kwargs["depth_total"]
    depth_lip = kwargs["depth_lip"]
    inset_lip = kwargs["inset_lip"]
    step = kwargs["lip_step_y"]

    # Full-width, 12 mm high channel: same profile and position as the user edit.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width, depth_lip, depth_total + 0.2],
        "radius": kwargs["lip_cutout_radius"],
        "pos": [pos[0], pos[1] - (opening_height - depth_lip) / 2, pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Narrower body opening forms the 5.5 mm shoulders beside the lip.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width - 2 * inset_lip, opening_height, depth_total + 0.2],
        "radius": kwargs["opening_radius"],
        "pos": [pos[0], pos[1], pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Taller containers do not need thick shoulders all the way down the body.
    # Keep only the 100 ml support height, then open to full width for the rest
    # of the cavity, along the ENTIRE insertion depth including the end bands.
    # The small square-bottom cut makes the shoulder end exact; the rounded
    # rectangle preserves the two far corners of the enlarged opening.
    extension = kwargs["body_extension_height"]
    if extension > 0:
        radius = min(kwargs["opening_radius"], extension / 2)
        end_y = pos[1] + kwargs["lip_support_end_y"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "rounded_rectangle",
            "m": "",
            "size": [opening_width, extension, depth_total + 0.2],
            "radius": radius,
            "pos": [pos[0], end_y + extension / 2, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "cube",
            "m": "",
            "size": [opening_width, radius, depth_total + 0.2],
            "pos": [pos[0] - opening_width / 2, end_y, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)

    if kwargs["lightening"] and kwargs["part_role"] == "frame":
        wall = kwargs["thickness_wall"]
        border = kwargs["drawer_border_edge"]
        row_index = kwargs.get("row_index", 0)
        column_index = kwargs.get("column_index", 0)
        bottom = kwargs["front_band"]
        top = depth_total - kwargs["rear_band"]

        # One broad floor/ceiling window: no longitudinal centre support.
        # A nonzero middle_rib_width optionally restores two windows for trials.
        half = kwargs["shelf_window_width"] / 2
        shoulder = top - half * kwargs["roof_slope"]
        offsets = [0]
        if kwargs["middle_rib_width"] > 0:
            offset = (kwargs["middle_rib_width"] + kwargs["shelf_window_width"]) / 2
            offsets = [-offset, offset]
        for side_y in [-1, 1]:
            outside = (side_y == -1 and row_index == 0) or (side_y == 1 and row_index == kwargs["row"] - 1)
            thickness = border if outside else wall
            y = pos[1] + side_y * (opening_height / 2 + thickness / 2)
            for offset in offsets:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": thickness + 0.2,
                    "depth": thickness + 0.2,
                    "points": [
                        [-half, bottom],
                        [half, bottom],
                        [half, shoulder],
                        [0, top],
                        [-half, shoulder],
                    ],
                    "rot": [90, 0, 0],
                    "pos": [pos[0] + offset, y + thickness / 2 + 0.1, pos[2]],
                }
                oobb.append_full(thing, **p3)

        # Separate reliefs BELOW and ABOVE the shelf. The upper cut reaches
        # through the thick shoulder as well as the wall, instead of leaving
        # a large solid block behind a cosmetic outer-wall hole.
        # The shelf's full root is retained from step-1 to step+3 by default.
        zones = [
            {
                "low": -opening_height / 2 + kwargs["side_rail_width"],
                "high": step - kwargs["lip_cutout_radius"],
                "inset": 0,
            },
            {
                "low": step + kwargs["lip_shelf_thickness"],
                "high": opening_height / 2 - kwargs["side_rail_width"],
                "inset": inset_lip,
            },
        ]
        for side_x in [-1, 1]:
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            thickness = border if outside else wall
            for zone in zones:
                half = (zone["high"] - zone["low"]) / 2
                shoulder = top - half * kwargs["roof_slope"]
                cut_depth = thickness + zone["inset"] + 0.2
                x = pos[0] + side_x * (opening_width / 2 + (thickness - zone["inset"]) / 2)
                y = pos[1] + (zone["low"] + zone["high"]) / 2
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": cut_depth,
                    "depth": cut_depth,
                    "points": [
                        [-half, bottom],
                        [half, bottom],
                        [half, shoulder],
                        [0, top],
                        [-half, shoulder],
                    ],
                    "rot": [90, 0, 90],
                    "pos": [x - cut_depth / 2, y, pos[2]],
                }
                oobb.append_full(thing, **p3)

    # Front catch and 45-degree ramp use the population dimensions.
    if kwargs.get("catch_tab_height", 0) > 0:
        projection = kwargs["catch_tab_height"]
        ramp = kwargs["catch_tab_ramp_depth"]
        tip_end = ramp + kwargs["catch_tab_depth"]
        wall = kwargs["thickness_wall"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "positive_positive",
            "shape": "polygon",
            "m": "#",
            "height": kwargs["catch_tab_width"],
            "depth": kwargs["catch_tab_width"],
            "points": [
                [-wall, 0],
                [0, 0],
                [projection, ramp],
                [projection, tip_end],
                [-wall, tip_end],
            ],
            "rot": [90, 0, 90],
            "pos": [pos[0] - kwargs["catch_tab_width"] / 2,
                    pos[1] - opening_height / 2, pos[2]],
        }
        oobb.append_full(thing, **p3)

def get_container_cutout_version_1(pos, thing, **kwargs):
    container_depth = kwargs.get("container_depth", 0)
    container_width = kwargs.get("container_width", 0)
    container_height = kwargs.get("container_height", 0)
    container_clearance = kwargs.get("container_clearance", 0)
    thickness_wall = kwargs.get("thickness_wall", 2)
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"rounded_rectangle"
    wid = container_width+container_clearance
    hei = container_height+container_clearance
    dep = container_depth+container_clearance+thickness_wall
    size = [wid, hei, dep]
    p3["size"] = size
    p3["radius"] = 5 - thickness_wall
    pos1 = copy.deepcopy(pos)         
    pos1[2] += 0
    p3["pos"] = pos1
    p3["m"] = "#"
    oobb.append_full(thing,**p3)
    #catch tab
    catch_tab_depth = 1.5
    kwargs["catch_tab_depth"] = catch_tab_depth
    catch_tab_height = 6
    kwargs["catch_tab_height"] = catch_tab_height
    catch_tab_minus = 30
    kwargs["catch_tab_minus"] = catch_tab_minus
    p3["type"] = "positive_positive"
    p3["shape"] = f"rounded_rectangle"
    wid = container_width-catch_tab_minus
    hei = catch_tab_height + thickness_wall
    dep = catch_tab_depth
    size = [wid, hei, dep]
    p3["size"] = size
    p3["radius"] = 2.5
    pos1 = copy.deepcopy(pos)         
    pos1[1] += -container_height/2 - container_clearance/2 + catch_tab_height/2 - thickness_wall
    p3["pos"] = pos1
    p3["m"] = "#"
    oobb.append_full(thing,**p3)
        
