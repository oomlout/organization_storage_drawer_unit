"""Manufacture a free-standing array of populated frames joined at the beam screws."""

from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

import numpy as np

import v8_beam_joints as joints
import v8_cabinet as shared
import working_scad as cad
from working_oomp_populate import get_current_options, record_id
from presentation import scenes
from presentation.scenes import pose


def plan(record, host):
    cfg = record["array"]
    p = cad.frame_parameters(**host)
    units, vertices, strips = shared.array_grid(cfg, p)
    q = p["frame"]
    depth = q["assembled_depth"]
    params = dict(face_t=q["plate_thickness"], tie_t=joints.JOINT_PLATE_MM)
    _, _, _, inset = joints.dimensions(p)
    profiles = [
        cad.frame_parameters(**r)
        for r in get_current_options()
        if r["part_role"] == "frame" and r["taxonomy_5"] == host["taxonomy_5"]
    ]
    defs = dict(
        floor_strip=f"cube([{cfg['runner_width_mm']},{cfg['runner_mm']},{depth}]);",
        screw_adapter="include <array_adapter_source.scad>",
    )
    parts = []

    def add(name, matrix, material, shift=(0, 0, 0)):
        parts.append(shared.Piece(name, matrix, shift, material))

    for x, y in units:
        add("array_unit", pose(x, y), "frame")
    for mat in strips:
        add("floor_strip", mat, "aluminium")
    for (vx, _), points in vertices.items():
        anchor = np.array(points[0])
        local = np.round(np.array(points) - anchor, 5)
        pitch = round(float(np.ptp(local[:, 1])), 5)
        name = "screw_adapter"
        thickness = p["screw"]["flange_size"][2]
        sign = -1 if vx == 0 else 1
        if len(points) > 1:
            name = "tee4" if len(points) == 4 else ("edge_upright" if pitch else "edge_across")
            shape = joints.pattern(name, inset, pitch)
            if sorted((round(x * sign, 5), y) for x, y in shape[0]) != sorted(map(tuple, local)):
                raise ValueError(f"{name} misses a beam screw at {anchor}")
            defs[name] = joints.expression(shape, profiles)
            thickness = joints.JOINT_PLATE_MM
        for rear in (False, True):
            face = pose(z=depth if rear else 0) @ shared.mirror(z=-1 if rear else 1)
            shift = (0, 0, 50 if rear else -50)
            mount = face @ pose(*anchor, -thickness) @ shared.mirror(x=sign)
            if name == "screw_adapter":
                mount = pose(
                    *anchor,
                    depth + thickness if rear else -thickness,
                    cad.v8_external_part_rotation(p, "screw_beam", rear),
                )
            add(name, mount, "cap", shift)
            for x, y in points:
                add("beam_screw", face @ pose(x, y, -thickness + 0.55), "metal", shift)
                add(
                    "beam_nut", face @ pose(x, y, params["face_t"] + p["screw"]["nut_near"]), "metal", shift
                )
    return p, params, defs, parts, units


def render(folder, hf, p, parts, units):
    from presentation.joint_studio import render_views, view

    with TemporaryDirectory() as tmp:
        structure = scenes.frame_views(
            hf, dict(p, omit_corner_adapters=True), Path(tmp), structure_only=True
        )
        objects = [
            scenes.item(
                folder / (a.name + ".stl"), "joint" if a.material == "cap" else a.material, a.matrix
            )
            for a in parts
            if a.name != "array_unit"
        ]
        for x, y in units:
            for path, role, matrix in structure:
                if Path(path).stem == "screw_beam":
                    role = "frame"
                if role == "cap":
                    role = "rail"
                objects.append((path, role, (pose(x, y) @ matrix).tolist()))
        render_views([view(folder / "presentation.jpg", objects, (0.60, -2, 0.61), (1640, 1280))])


def build(folder, record, host, export):
    p, params, defs, parts, units = plan(record, host)
    hf = folder.parent / record_id(host)
    shutil.copyfile(hf / "screw_adapter.scad", folder / "array_adapter_source.scad")
    shared.component_files(folder, hf, params, defs, export, host, p)
    shared.beam_hardware(folder, p, export)
    shared.assembly_source(folder, parts, False, export)
    shared.assembly_source(folder, parts, True, export)
    write_guide(folder, record, host, p, parts, export)
    if export:
        shared.validate(folder, parts, units, params, p, host)
        render(folder, hf, p, parts, units)


def write_guide(folder, record, host, p, parts, export):
    qty = Counter(a.name for a in parts)
    cfg = record["array"]
    shared.save_json(folder / "assembly.json", dict(frame=record_id(host), layout=cfg, quantities=qty))
    nx, ny = cfg["units_across"], cfg["units_high"]
    columns, rows = p["column"], p["row"]
    depth = p["frame"]["assembled_depth"]
    instructions = [
        f"# {nx} × {ny} drawer array",
        "",
        f"{nx*ny} double-sided {columns} × {rows} frames make {nx*columns} columns and {ny*rows} rows on each face. "
        f"The array holds {2*nx*ny*columns*rows} {host['tray_name']} pots.",
        "",
        "[![Assembled array](presentation.jpg)](presentation.jpg)",
        "",
        "[Complete Bambu Studio print kit](working.3mf) · [Plate contents](print-plates.json) · [Frame assembly guide](../"
        + record_id(host)
        + "/README.md) · [Fit checks](validation.json)",
        "",
        "The print kit groups faceplates and screw beams on teal plates, snap beams and caps on black plates, and joiners and corner adapters on yellow. Each piece has its own editable filament assignment in Bambu Studio.",
        "",
        "## Assembly",
        "",
        "1. Print the complete kit once. Load the captive nuts into the four corner screw beams on each frame before seating the faces.",
        f"2. Lay out {nx} frames across and {ny} high. At each tier seam, fit four "
        f"{cfg['runner_width_mm']} × {cfg['runner_mm']} × {depth:g} mm aluminium strips under each frame, "
        f"{qty['floor_strip']} strips in total.",
        "3. On each face, fit the two-hole horizontal brackets along the top and bottom and the two-hole upright brackets along the sides. Fit a four-hole plate at each interior crossing. The upright and four-hole brackets match the tier gap.",
        "4. Fit a standard adapter at each exposed outer corner. Drive one M3 × 20 countersunk screw into each beam end. Repeat at the rear.",
        "",
        "| Fitting | Quantity across both faces |",
        "| --- | ---: |",
    ]
    for name, label in [
        ("edge_across", "Horizontal two-hole joiner"),
        ("edge_upright", "Upright two-hole joiner"),
        ("tee4", "Four-hole joiner"),
        ("screw_adapter", "Single corner adapter"),
        ("beam_screw", "M3 × 20 countersunk screw"),
        ("beam_nut", "M3 nut"),
    ]:
        instructions.append(f"| {label} | {qty[name]} |")
    instructions += [
        "",
        "Supply the aluminium strips, screws, nuts and pots separately.",
        "",
        "[Assembled CAD](assembled.scad) · [Exploded CAD](exploded.scad) · [Assembly BOM](assembly.json)",
        "",
    ]
    if not export:
        instructions = [
            instructions[0],
            "",
            "[Assembled CAD](assembled.scad) · [Exploded CAD](exploded.scad) · [Assembly BOM](assembly.json)",
            "",
        ]
    (folder / "README.md").write_text("\n".join(instructions), encoding="utf-8")
    (folder / "printing.txt").write_text(
        "Print working.3mf once for the full array. Per-plate quantities are in print-plates.json.\n"
        if export
        else "Run the full make-all build to generate the print kit.\n"
    )
