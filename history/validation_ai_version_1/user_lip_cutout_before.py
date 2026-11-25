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
    depth_lip = 12
    inset_lip = 5.5
    # Through opening; epsilon avoids coincident faces at both ends.
    opening_width = kwargs["opening_width"]
    opening_height = kwargs["opening_height"]
    depth_total = kwargs["depth_total"]



    #main body_cutout
    if True:
        #piece_1
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = "rounded_rectangle"
            p3["m"] = ""
            wid = opening_width
            hei = depth_lip
            dep = depth_total
            size = [wid, hei, dep + 0.2]
            p3["size"] = size
            p3["radius"] = 1
            pos1 = copy.deepcopy(pos)
            pos1[1] -= (opening_height - depth_lip) / 2
            pos1[2] -= 0.1
            p3["pos"] = pos1
            #p3["m"] = "#"
            oobb.append_full(thing, **p3)
        #piece_2
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = "rounded_rectangle"
            p3["m"] = ""
            wid = opening_width - 2*inset_lip
            hei = opening_height
            dep = depth_total 
            size = [wid, hei, dep + 0.2]
            p3["size"] = size
            p3["radius"] = 1
            p3["radius"] = kwargs["opening_radius"]
            pos1 = copy.deepcopy(pos)
            pos1[2] -= 0.1
            p3["pos"] = pos1
            #p3["m"] = "#"
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
        
