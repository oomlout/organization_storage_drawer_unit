"""The active V8 manufacturing catalogue. Dimensions in mm, grids per face."""
from copy import deepcopy
from pathlib import Path

import yaml
from oomp_populate_helper import build_oomp_id, write_extras

PROFILE = Path(__file__).with_name("v8_profile.yaml")
CONTAINER = "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209"
SIZES = {"1x1": (1, 1), "2x2": (2, 2), "2x7": (2, 7)}
JOINER = "joiners"


def get_current_options():
    profile = yaml.safe_load(PROFILE.read_text(encoding="utf-8"))
    common = dict(style="ai_version_8", version=8, container=CONTAINER,
                  container_short="rectangle_100_ml_tamper_evident_systempak_209",
                  taxonomy_1="oobb", taxonomy_2="organization", taxonomy_3="storage",
                  taxonomy_4="drawer_unit", taxonomy_5="systempak_209_100_ml")
    parts = []
    for variant, (cols, rows) in SIZES.items():
        compact = variant != "2x7"
        frame = dict(deepcopy(profile["components"]), **common, variant=variant,
                     taxonomy_6=f"{cols}_column", taxonomy_7=f"{rows}_row", taxonomy_8="v8",
                     column=cols, row=rows, part_role="frame", drawer_sides=2,
                     drawer_count=2*cols*rows, drawer_capacity_ml=100,
                     record_type="printed_drawer_unit", product_name=f"V8 {variant} Systempak 209 drawer unit",
                     frame_definition=dict(profile["face"], face_edge_y=20 if compact else 2),
                     container_dimensions_mm=dict(across=86, height=26, depth=109),
                     frame_mount_layout="top_braces" if compact else "four_corner_replacements",
                     snap_beam_count=(cols+1)*rows-(0 if compact else 4),
                     screw_beam_count=cols+1 if compact else 4)
        if compact:
            frame.update(face_stop_profile="inside_flat", corner_fixing=deepcopy(profile["corner_fixing"]))
        parts.append(frame)
    parts.append(dict(common, part_role="accessory", variant=JOINER, taxonomy_6="joiners",
                      taxonomy_7="v8", product_name="V8 M3 x 25 joining brackets and backers",
                      reference_frame="2x2", compatible_frames=["1x1", "2x2"],
                      corner_fixing={**profile["corner_fixing"], **profile["joiner"]}))
    return parts


def selected_options(part=None):
    options = get_current_options()
    if part is None:
        return options
    if part not in (*SIZES, JOINER):
        raise ValueError(f"Unknown V8 part {part!r}")
    wanted = {part}
    if part == JOINER:
        wanted.update(next(o["compatible_frames"] for o in options if o["variant"] == JOINER))
    return [o for o in options if o["variant"] in wanted]


def record_id(option):
    return build_oomp_id(option.copy())


def main(part=None, **kwargs):
    records = [dict(option, oobb_details=deepcopy(option))
               for option in selected_options(part)]
    write_extras(records)
