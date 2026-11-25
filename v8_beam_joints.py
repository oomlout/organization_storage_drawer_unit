"""Build printable joints around the same OOBB adapter used on a free-standing frame."""

import json
import shutil
from pathlib import Path

import manifold3d as m3d
import numpy as np

import working_scad as cad
import working_scad_container_cutout as cuts
from working_oomp_populate import CABINET_DESIGN, PLYWOOD_JOINT, record_id
from presentation.scenes import pose


def dimensions(p):
    q = p["frame"]
    corners = [m for m in p["frame_mounts"] if m["corner_beam"]]
    xs = sorted({m["x"] for m in corners})
    ys = sorted({m["hole_y"] for m in corners})
    if (
        len(corners) != 4
        or len(xs) != 2
        or len(ys) != 2
        or any(m["kind"] != "screw_beam" for m in corners)
    ):
        raise ValueError("A joint host needs a screw beam at each outer corner")
    return xs[1], ys[0], ys[1], round(q["width_total"] / 2 - xs[1], 5)


def pattern(kind, inset, pitch=0, plywood=12):
    across = round(2 * inset, 5)
    if kind == "plywood_joint":
        return [[0, 0]], [], [round(inset + plywood / 2, 5), 0]
    if kind == "edge_across":
        return [[0, 0], [across, 0]], [], []
    spine_x = round(inset - 3.1, 5) if kind == "edge_upright" else inset
    holes = [[0, 0], [0, pitch]]
    if kind == "tee4":
        holes += [[across, 0], [across, pitch]]
    return holes, [[spine_x, 0], [spine_x, pitch]], []


def expression(shape):
    return "beam_joint(" + ",".join(json.dumps(v) for v in shape) + ");"


def library(folder, p, host_folder):
    shutil.copyfile(host_folder / "screw_adapter.scad", folder / "native_adapter.scad")
    (folder / "beam_joint_geometry.scad").write_text(
        f"$fn=64;\ntie_t={p['screw']['flange_size'][2]};\n"
        "module native_adapter(){\ninclude <native_adapter.scad>\n}\n"
        + cuts.BEAM_JOINT_CUTS
        + cad.BEAM_JOINT_SOLIDS
    )


def verify(path, shape, p, hf):
    from v8_cabinet import solid

    holes, _, wood = shape
    joint = solid(path)
    if len(joint.decompose()) != 1:
        raise ValueError(f"Disconnected joint {path}")
    t = p["screw"]["flange_size"][2]
    # Compare the entire receiver-engaging portion with the known fitting,
    # and its countersink at each axis with the standard adapter.
    adapter = solid(hf / "screw_adapter.stl")
    for x, y in holes:
        guide = m3d.Manifold.cube((8, 8, 5)).translate((x - 4, y - 4, t + 0.001))
        head = m3d.Manifold.cylinder(t, 3.49, 3.49, 64).translate((x, y, 0))
        ref = adapter.translate((x, y, 0))
        for zone in [guide, head]:
            if abs(((joint - ref) ^ zone).volume()) + abs(((ref - joint) ^ zone).volume()) > 0.005:
                raise ValueError(f"Changed guide or M3 seat in {path.name}")
    if wood:
        probe = m3d.Manifold.cylinder(t, 1.99, 1.99, 64).translate((*wood, 0))
        if (joint ^ probe).volume() > 0.001:
            raise ValueError("Obstructed wood screw clearance")
    return dict(
        single_printed_body=True,
        original_m3_seats_and_guides=len(holes),
        wood_clearance_mm=4 if wood else None,
    )


def build(folder, record, frames, export):
    from v8_manufacturing import openscad, write_json

    hosts = {key: cad.frame_parameters(**frames[key]) for key in record["compatible_frames"]}
    ref = frames[record["reference_frame"]]
    hf = folder.parent / record_id(ref)
    p = hosts[record["reference_frame"]]
    library(folder, p, hf)
    shapes = {}
    use = {}
    ply = record["variant"] == PLYWOOD_JOINT
    cfg = CABINET_DESIGN
    for name, params in hosts.items():
        _, upper, lower, inset = dimensions(params)
        for gap in ([0, cfg["runner_mm"]] if name == cfg["host"] and not ply else [0]):
            pitch = round(params["frame"]["height_total"] - lower + upper + gap, 5)
            for kind in (["plywood_joint"] if ply else ["edge_across", "edge_upright", "tee4"]):
                shape = pattern(kind, inset, pitch, cfg["plywood_mm"])
                stem = kind
                if kind in ("tee4", "edge_upright"):
                    stem += "_" + f"{pitch:g}".replace(".", "p")
                if stem in shapes and shapes[stem] != shape:
                    raise ValueError(f"Incompatible {stem} dimensions")
                shapes[stem] = shape
                label = name + (f" with {gap:g} mm tier gap" if gap else " flush")
                use.setdefault(stem, []).append(label)
    report = {}
    for stem, shape in shapes.items():
        source = folder / (stem + ".scad")
        source.write_text("include <beam_joint_geometry.scad>\n" + expression(shape) + "\n")
        if export:
            openscad(source, source.with_suffix(".stl"), "--export-format=binstl")
            report[stem] = verify(source.with_suffix(".stl"), shape, p, hf)
    if export:
        from tempfile import TemporaryDirectory
        from presentation.beam_joint import fit_cases

        with TemporaryDirectory() as tmp:
            report["installed"] = fit_cases(
                folder, hosts, frames, use, shapes, record["reference_frame"], Path(tmp)
            )
        write_json(folder / "validation.json", report)
    write_json(
        folder / "assembly.json",
        dict(
            compatible_frames=list(hosts),
            parts=shapes,
            applications=use,
            flange_mm=p["screw"]["flange_size"][2],
            beam_screw="M3 x 20 countersunk",
        ),
    )
    intro = (
        "Connect an outside corner beam to the front or rear edge of a 12 mm plywood side. "
        "The 3.5 × 16 mm countersunk wood screw is centred 6 mm from either plywood face."
        if ply
        else "Join adjacent modules using the M3 × 20 countersunk screws and captive nuts already in their outer corner beams. Fit a bracket at each shared junction on both faces."
    )
    steps = (
        "Remove the corner screw and its individual adapter. Seat the joint's two guide cheeks in the same receiver. "
        "Refit the same screw into the nut inside the beam. Mark the plywood through the other hole, "
        "drill a Ø2.5 mm pilot 16 mm deep in the centre of the edge, then fit the wood screw. Test the pilot in an offcut."
        if ply
        else "Remove the individual adapters and screws from the corners being joined. Leave each nut in its beam. "
        "Press the bracket guides into those receivers and reinstall the same screws. For a two-hole upright, point the narrow spine toward the outside edge. Rotate the bracket in its own plane to fit the opposite side. "
        "Use the across strip for a left-to-right seam and a four-hole bracket where four frames meet. On a 2x7 below a vertical joint, centre its first two fixed location labels 9.65 and 20.85 mm below the top corner beam axis."
    )
    lines = [
        f"# {record['product_name']}",
        "",
        intro,
        "",
        "Print flat with the guide cheeks facing up. " + steps,
        "",
        "| Part | Applications | Editable CAD |",
        "| --- | --- | --- |",
    ]
    for stem in shapes:
        link = f"[{stem}]({stem}.stl)" if export else stem
        lines.append(f"| {link} | {', '.join(use[stem])} | [SCAD]({stem}.scad) |")
    if export:
        hero = next(iter(shapes)) if ply else next(s for s in shapes if s.startswith("tee4"))
        openscad(
            folder / (hero + ".scad"),
            folder / "presentation.png",
            "--render",
            "--viewall",
            "--autocenter",
            "--imgsize=850,550",
            "--projection=o",
            "--camera=50,-70,85,0,0,0",
        )
        lines += [
            "",
            "![Joint fitted to the screw beam](installed.png)",
            "",
            "[Installed CAD detail](installed.scad)",
            "",
            "![Printed bracket with its receiver guides](presentation.png)",
            "",
            "[CAD fit checks](validation.json)",
        ]
    (folder / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (folder / "printing.txt").write_text(
        intro
        + "\n"
        + steps
        + "\n"
        + "\n".join(f"{k}.stl  {', '.join(v)}" for k, v in use.items())
        + "\n",
        encoding="utf-8",
    )
