"""Build printable joints around the same OOBB adapter used on a free-standing frame."""

import json
from copy import deepcopy
from pathlib import Path

import manifold3d as m3d
import oobb

import working_scad as cad
import working_scad_container_cutout as cuts
from working_oomp_populate import CABINET_DESIGN, JOINT_PLATE_MM, PLYWOOD_JOINT, record_id
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
    vertical = kind in {"edge_upright", "tee4", "plywood_double"}
    paired_columns = kind in {"edge_across", "tee4"}
    to_wood = kind in {"plywood_joint", "plywood_double"}
    if vertical and pitch <= 0:
        raise ValueError("Vertical joints need the centre distance between tiers")
    height = pitch if vertical else 0
    holes = [
        [x, y]
        for x in ([0, across] if paired_columns else [0])
        for y in ([0, height] if vertical else [0])
    ]
    wood = [round(inset + plywood / 2, 5), height / 2] if to_wood else []
    # Leave the drawer-side edge inside the face margin. Local bosses surround each screw.
    right = inset
    if to_wood:
        right += plywood
    elif paired_columns:
        right = across + 0.9
    end = 3.9 if vertical else 7.2
    return holes, [-0.9, -end, right, height + end], wood


def face_slots(shape, profiles):
    """Access to the spare faceplate bores, including when a plate is turned end-for-end."""
    holes, bounds, _ = shape
    height = max(y for _, y in holes)
    centres = {}
    for p in profiles:
        hx, upper, lower, _ = dimensions(p)
        q = p["frame"]
        flush_pitch = q["height_total"] - lower + upper
        if (
            height
            and abs(height - flush_pitch) > 0.001
            and not (
                p["variant"] == CABINET_DESIGN["host"]
                and abs(height - flush_pitch - CABINET_DESIGN["runner_mm"]) < 0.001
            )
        ):
            continue
        radius = oobb.gv("hole_radius_" + q["corner_hole_size"], "3dpr") + 0.25
        face_x = max(v["x"] for v in q["corner_holes"])
        top = min(v["y"] for v in q["corner_holes"]) - upper
        bottom = max(v["y"] for v in q["corner_holes"]) - lower
        for x in sorted({x for x, _ in holes}):
            bore_x = round(x + (face_x - hx) * (1 if x == 0 else -1), 5)
            ys = [bottom, height + top] if height else [bottom, top]
            for y in ys + [height - y for y in ys]:
                if bounds[1] - radius <= y <= bounds[3] + radius:
                    centres.setdefault((bore_x, radius), set()).add(round(y, 5))
    slots = []
    for (x, r), ys in sorted(centres.items()):
        for y in sorted(ys):
            if slots and slots[-1][0] == x and slots[-1][3] == r and y - slots[-1][2] < 2 * r:
                slots[-1][2] = y
            else:
                slots.append([x, y, y, r])
    return slots


def expression(shape, profiles):
    args = [*shape, face_slots(shape, profiles)]
    return "beam_joint(" + ",".join(json.dumps(v) for v in args) + ");"


def library(folder, p):
    from v8_manufacturing import write_solid

    screw = deepcopy(p["screw"])
    screw["flange_size"][2] = JOINT_PLATE_MM
    adapter = oobb.get_default_thing(type="v8_joint_adapter")
    cad.draw_component(adapter, **dict(p, screw=screw, connector_view="screw_adapter"))
    write_solid(folder, "native_adapter", adapter, False)
    (folder / "beam_joint_geometry.scad").write_text(
        f"$fn=64;\ntie_t={JOINT_PLATE_MM};\n"
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
    t = JOINT_PLATE_MM
    native_t = p["screw"]["flange_size"][2]
    # Compare the entire receiver-engaging portion with the known fitting,
    # and its countersink at each axis with the standard adapter.
    adapter = solid(hf / "screw_adapter.stl")
    for x, y in holes:
        guide = m3d.Manifold.cube((8, 8, 5)).translate((x - 4, y - 4, t + 0.001))
        head = m3d.Manifold.cylinder(native_t, 3.49, 3.49, 64).translate((x, y, 0))
        ref = adapter.translate((x, y, 0))
        for zone, reference in [(guide, ref.translate((0, 0, t - native_t))), (head, ref)]:
            if (
                abs(((joint - reference) ^ zone).volume()) + abs(((reference - joint) ^ zone).volume())
                > 0.005
            ):
                raise ValueError(f"Changed guide or M3 seat in {path.name}")
    # The transition from the entire plate to just its locating cheeks is at 3 mm.
    xmin, ymin, xmax, ymax = shape[1]
    plate_area = joint.slice(t - 0.01).area()
    guide_area = adapter.slice(native_t + 0.01).area() * len(holes)
    if abs(joint.slice(t + 0.01).area() - guide_area) > 0.01 or plate_area < 0.55 * (xmax - xmin) * (
        ymax - ymin
    ):
        raise ValueError(f"Insufficient full-thickness plate area in {path.name}: {plate_area:.2f} mm2")
    if wood and abs(joint.bounding_box()[3] - xmax) > 0.001:
        raise ValueError(f"{path.name} misses the plywood outer edge")
    if wood:
        probe = m3d.Manifold.cylinder(t, 1.99, 1.99, 64).translate((*wood, 0))
        if (joint ^ probe).volume() > 0.001:
            raise ValueError("Obstructed wood screw clearance")
    return dict(
        single_printed_body=True,
        plate_mm=t,
        plate_section_mm2=round(plate_area, 2),
        outer_edge_from_beam_mm=xmax if wood else None,
        original_m3_seats_and_guides=len(holes),
        wood_clearance_mm=4 if wood else None,
    )


def build(folder, record, frames, export):
    from v8_manufacturing import openscad, write_json

    hosts = {key: cad.frame_parameters(**frames[key]) for key in record["compatible_frames"]}
    ref = frames[record["reference_frame"]]
    hf = folder.parent / record_id(ref)
    p = hosts[record["reference_frame"]]
    library(folder, p)
    shapes = {}
    use = {}
    ply = record["variant"] == PLYWOOD_JOINT
    cfg = CABINET_DESIGN
    for name, params in hosts.items():
        _, upper, lower, inset = dimensions(params)
        for gap in ([0, cfg["runner_mm"]] if name == cfg["host"] else [0]):
            pitch = round(params["frame"]["height_total"] - lower + upper + gap, 5)
            for kind in (
                ["plywood_joint", "plywood_double"] if ply else ["edge_across", "edge_upright", "tee4"]
            ):
                shape = pattern(kind, inset, pitch, cfg["plywood_mm"])
                stem = kind
                if kind in ("tee4", "edge_upright", "plywood_double"):
                    stem += "_" + f"{pitch:g}".replace(".", "p")
                if stem in shapes and shapes[stem] != shape:
                    raise ValueError(f"Incompatible {stem} dimensions")
                shapes[stem] = shape
                label = name + (f" with {gap:g} mm tier gap" if gap else " flush")
                use.setdefault(stem, []).append(label)
    report = {}
    for stem, shape in shapes.items():
        source = folder / (stem + ".scad")
        source.write_text(
            "include <beam_joint_geometry.scad>\n" + expression(shape, hosts.values()) + "\n"
        )
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
            face_bore_clearances={k: face_slots(v, hosts.values()) for k, v in shapes.items()},
            flange_mm=JOINT_PLATE_MM,
            beam_screw="M3 x 20 countersunk",
        ),
    )
    intro = (
        "Use the single-contact plate at an outside corner. Use the two-contact plate where two stacked frames meet the same plywood side. Both 3 mm plates finish flush with the outside edge of the plywood. "
        "The 3.5 × 16 mm countersunk wood screw is centred 6 mm from either plywood face."
        if ply
        else "The solid 3 mm plates join adjacent modules using the M3 × 20 countersunk screws and captive nuts already in their outer corner beams. Fit a plate at each shared junction on both faces. The reliefs keep the spare faceplate holes accessible."
    )
    steps = (
        "Remove the screw and adapter at each participating corner. Seat one pair of guide cheeks in each exposed beam receiver. "
        "Refit each M3 screw into its captive beam nut. Mark the plywood through the other hole, "
        "drill a Ø2.5 mm pilot 16 mm deep in the centre of the edge, then fit the wood screw. Test the pilot in an offcut."
        if ply
        else "Remove the individual adapters and screws from the corners being joined. Leave each nut in its beam. "
        "Press the bracket guides into those receivers and reinstall the same screws. For a two-hole upright, place the long straight edge toward the outside of the frame. Rotate the bracket in its own plane to fit the opposite side. "
        "Use the across strip for a left-to-right seam and a four-hole bracket where four frames meet. On a 2x7 below a vertical joint, centre its first two fixed location labels 9.65 and 20.85 mm below the top corner beam axis."
    )
    lines = [
        f"# {record['product_name']}",
        "",
        intro,
        "",
        f"The plate sits {JOINT_PLATE_MM:g} mm proud of the frame. The locating cheeks extend "
        f"{p['screw']['adapter_engagement']:g} mm into the original receivers.",
        "",
        "Print flat with the guide cheeks facing up. " + steps,
        "",
        "| Part | Applications | Editable CAD |",
        "| --- | --- | --- |",
    ]
    for stem in shapes:
        link = f"[{stem}]({stem}.stl)" if export else stem
        if export:
            link = f'<img src="{stem}.jpg" width="120" alt="{stem}"> {link}'
        lines.append(f"| {link} | {', '.join(use[stem])} | [SCAD]({stem}.scad) |")
    if export:
        from presentation.joint_studio import render_joints
        _,top,bottom,_ = dimensions(p)
        ref_pitch = f"{p['frame']['height_total']+top-bottom:g}".replace(".","p")
        render_joints(folder,shapes,JOINT_PLATE_MM,ref_pitch)
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
    if export:
        lines += ["","[Editable print kit for Bambu Studio](working.3mf) · [Plate contents](print-plates.json)"]
    if ply:
        lines += [
            "",
            "On a 2×7 immediately below a two-contact plate, centre the first two fixed labels 9.65 mm and 20.85 mm below its upper beam axis. Keep each label centred on the faceplate margin.",
        ]
    if ply and export:
        lines += [
            "",
            "![Two frames attached to the plywood side](double_installed.png)",
            "",
            "[Two-contact installed CAD](double_installed.scad)",
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
