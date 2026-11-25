"""The active V8 manufacturing catalogue. Dimensions in mm, grids per face."""
from copy import deepcopy
from pathlib import Path

import yaml
from oomp_populate_helper import build_oomp_id, write_extras

PROFILE = Path(__file__).with_name("v8_profile.yaml")
CONTAINER = "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209"
# Layout keys are command-line selectors. Give each additional family unique keys.
TRAYS = {
    "systempak_209_100_ml": {
        "name": "Systempak 209", "capacity_ml": 100, "container": CONTAINER,
        "short": "rectangle_100_ml_tamper_evident_systempak_209",
        "dimensions_mm": {"across": 86, "height": 26, "depth": 109},
        "layouts": {
            "1x1": {"grid": (1, 1), "mounts": "top_braces"},
            "2x2": {"grid": (2, 2), "mounts": "top_braces"},
            "2x7": {"grid": (2, 7), "mounts": "four_corner_replacements", "featured": True},
        },
    },
}
JOINER = "joiners"
PLYWOOD_JOINT = "plywood-joint"
JOINT_PLATE_MM = 3.0
JOINER_REFERENCE = "2x2"
CABINET = "cabinet-3x3"
CABINET_DESIGN = dict(host="2x7", units_across=3, units_high=3, plywood_mm=12,
                      cap_overhang_mm=0, side_gap_mm=0, top_gap_mm=0.6,
                      runner_mm=2, runner_width_mm=15)
VERSIONS = [
    ("V1", "First locked frame", "AI_VERSION_1.md"),
    ("V2", "Interlocking junctions", "AI_VERSION_2.md"),
    ("V3", "Revised lower supports", "AI_VERSION_3.md"),
    ("V4", "Modular drawer units", "AI_VERSION_4.md"),
    ("V5", "Tiled PETG frames", "AI_VERSION_5_TILED.md"),
    ("V6", "Double-sided plywood enclosure", "AI_VERSION_6_DOUBLE_SIDED.md"),
    ("V7", "Through-panel clips and interchangeable beams", "AI_VERSION_7.md"),
]


def get_current_options():
    profile = yaml.safe_load(PROFILE.read_text(encoding="utf-8"))
    common = dict(style="ai_version_8", version=8, taxonomy_1="oobb",
                  taxonomy_2="organization", taxonomy_3="storage", taxonomy_4="drawer_unit")
    parts = []
    hosts = []
    for family, tray in TRAYS.items():
        for variant, layout in tray["layouts"].items():
            cols, rows = layout["grid"]
            if layout["mounts"] not in {"top_braces", "four_corner_replacements"}:
                raise ValueError(f"Unknown mount layout for {variant}")
            compact = layout["mounts"] == "top_braces"
            frame = dict(deepcopy(profile["components"]), **common, variant=variant,
                         container=tray["container"], container_short=tray["short"],
                         taxonomy_5=family, taxonomy_6=f"{cols}_column", taxonomy_7=f"{rows}_row",
                         taxonomy_8="v8", column=cols, row=rows, part_role="frame", drawer_sides=2,
                         drawer_count=2*cols*rows, drawer_capacity_ml=tray["capacity_ml"],
                         tray_name=tray["name"], featured=layout.get("featured", False),
                         record_type="printed_drawer_unit", product_name=f"V8 {cols}x{rows} {tray['name']} drawer unit",
                         frame_definition=dict(profile["face"], face_edge_y=20 if compact else 2),
                         container_dimensions_mm=deepcopy(tray["dimensions_mm"]), frame_mount_layout=layout["mounts"],
                         snap_beam_count=(cols+1)*rows-(2 if compact else 4),
                         screw_beam_count=cols+3 if compact else 4)
            if compact:
                frame["face_stop_profile"] = "inside_flat"
            if family == "systempak_209_100_ml":
                hosts.append(variant)
            parts.append(frame)
    selectors = [p["variant"] for p in parts] + [JOINER, PLYWOOD_JOINT, CABINET]
    if len(set(selectors)) != len(selectors) or len({record_id(p) for p in parts}) != len(parts):
        raise ValueError("Each layout needs a unique selector and a unique catalogue ID")
    ref = next(p for p in parts if p["variant"] == JOINER_REFERENCE)
    for selector, taxonomy, name in [
        (JOINER, "joiners", "Corner screw-beam joining brackets"),
        (PLYWOOD_JOINT, "plywood_joint", "Corner screw-beam to plywood joint"),
    ]:
        parts.append(dict(common, part_role="accessory", variant=selector, taxonomy_5=ref["taxonomy_5"],
                          taxonomy_6=taxonomy, taxonomy_7="v8", product_name=name,
                          reference_frame=JOINER_REFERENCE, compatible_frames=list(hosts)))
    host = next(p for p in parts if p["variant"] == CABINET_DESIGN["host"])
    parts.append(dict(common, part_role="cabinet", variant=CABINET, taxonomy_5=host["taxonomy_5"],
                      taxonomy_6="2x7_array", taxonomy_7="3_by_3_plywood_cabinet", taxonomy_8="v8",
                      product_name="Three by three 2x7 drawer cabinet", cabinet=deepcopy(CABINET_DESIGN)))
    return parts


def selected_options(part=None):
    options = get_current_options()
    if part is None:
        return options
    if part not in {opt["variant"] for opt in options}:
        raise ValueError(f"Unknown V8 part {part!r}")
    wanted = {part}
    if part in (JOINER, PLYWOOD_JOINT):
        wanted.update(next(o["compatible_frames"] for o in options if o["variant"] == JOINER))
    if part == CABINET:
        wanted.add(CABINET_DESIGN["host"])
    return [o for o in options if o["variant"] in wanted]


def record_id(option):
    return build_oomp_id(option.copy())


def main(part=None, **kwargs):
    records = [dict(option, oobb_details=deepcopy(option))
               for option in selected_options(part)]
    write_extras(records)
