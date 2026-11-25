"""Nine standard V8 frames in a drilled plywood sleeve. Dimensions and exports are in mm."""

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
import v8_beam_joints as joints
import csv
import json
import os
import shutil
import subprocess

import ezdxf
import manifold3d as m3d
import numpy as np
import trimesh

import working_scad as cad
import working_scad_container_cutout as cuts
from working_oomp_populate import get_current_options, record_id
from presentation.scenes import pose


def save_json(path, obj):
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def mirror(x=1, y=1, z=1):
    return np.diag([x, y, z, 1.0])


@dataclass
class Piece:
    name: str
    matrix: np.ndarray
    shift: tuple
    material: str


def plan(record, host):
    cfg = record["cabinet"]
    p = cad.frame_parameters(**host)
    q = p["frame"]
    w, h, d = (q[k] for k in ("width_total", "height_total", "assembled_depth"))
    nx, ny = cfg["units_across"], cfg["units_high"]
    t, gap, top_gap, rt = cfg["plywood_mm"], cfg["side_gap_mm"], cfg["top_gap_mm"], cfg["runner_mm"]
    aw, ah = nx * w, ny * h + (ny - 1) * rt
    hx, upper, low, inset = joints.dimensions(p)
    iw, ih = aw + 2 * gap, ah + top_gap
    top = -ah / 2 - top_gap
    bottom = ah / 2
    params = dict(
        t=t,
        inside_w=iw,
        inside_h=ih,
        cap_w=iw + 2 * (t + cfg["cap_overhang_mm"]),
        depth=d,
        face_t=q["plate_thickness"],
        tie_t=joints.JOINT_PLATE_MM,
        hole_x=hx,
        low_y=low,
        stations=[22, round(d * 0.28, 1), d / 2, round(d * 0.72, 1), d - 22],
        retainer_y=[],
    )
    parts = []
    profiles = [
        cad.frame_parameters(**r)
        for r in get_current_options()
        if r["part_role"] == "frame" and r["taxonomy_5"] == host["taxonomy_5"]
    ]
    defs = {
        "cap": "cap_panel();",
        "side": "side_panel();",
        "floor_strip": f"cube([{cfg['runner_width_mm']},{rt},{d}]);",
        "dowel": "dowel();",
        "wood_30": "wood_screw(30);",
        "wood_16": "wood_screw(16);",
    }
    patterns = {}

    def add(name, mat, role, dx=0, dy=0, dz=0):
        parts.append(Piece(name, mat, (dx, dy, dz), role))

    for side in (-1, 1):
        add("side", pose(side * iw / 2, top) @ mirror(x=side), "ply_side", side * 115)
    for sign, level in [(-1, top), (1, bottom)]:
        cap = pose(y=level) @ mirror(y=sign)
        add("cap", cap, "ply_cap", 0, sign * 110)
        for side in (-1, 1):
            for i, z in enumerate(params["stations"]):
                axis = cap @ pose(side * (iw + t) / 2, 0, z, (-90, 0, 0))
                # +axial points outward from cap-to-side joint.
                if i % 2:
                    add("wood_30", axis @ pose(z=t, rotation=(180, 0, 0)), "metal", side * 15, sign * 150)
                else:
                    add("dowel", axis @ pose(z=-16.5), "dowel", side * 40, sign * 52)
    # Group fasteners by grid vertex, producing one plate at each shared junction.
    vertices = {}
    units = []
    for row in range(ny):
        for col in range(nx):
            cx = (col - (nx - 1) / 2) * w
            cy = (row - (ny - 1) / 2) * (h + rt)
            units.append((cx, cy))
            add("array_unit", pose(cx, cy), "frame")
            for sx in (-1, 1):
                for down, local_y in enumerate((upper, low)):
                    vertex = (col + int(sx > 0), row + down)
                    vertices.setdefault(vertex, []).append((cx + sx * hx, cy + local_y))
            if row < ny - 1:
                for aperture in (-1, 1):
                    for offset in (-20.5, 20.5):
                        add(
                            "floor_strip",
                            pose(
                                cx + aperture * q["pitch_x"] / 2 + offset - cfg["runner_width_mm"] / 2,
                                cy + h / 2,
                                0,
                            ),
                            "aluminium",
                        )
    for (vx, vy), points in vertices.items():
        anchor = np.array(points[0])
        local = np.round(np.array(points) - anchor, 5)
        side = vx in (0, nx)
        vertical = len(set(local[:, 1])) > 1
        if side:
            key = "plywood_double" if vertical else "plywood_joint"
        elif vertical:
            key = "tee4"
        else:
            key = "edge_across"
        sign = -1 if vx == 0 else 1
        pitch = round(float(np.ptp(local[:, 1])), 5)
        shape = joints.pattern(key, inset + gap if side else inset, pitch, t)
        installed = sorted((round(x * sign, 5), round(y, 5)) for x, y in shape[0])
        if installed != sorted(map(tuple, local)):
            raise ValueError(f"{key} does not align with the host beam axes")
        defs[key] = joints.expression(shape, profiles)
        patterns[key] = shape
        if side:
            wood_x = anchor[0] + sign * shape[2][0]
            wood_y = anchor[1] + shape[2][1]
            if vx == 0:
                params["retainer_y"].append(round(wood_y - top, 5))
        for back in (False, True):
            face = pose(z=d if back else 0) @ mirror(z=-1 if back else 1)
            push = 50 if back else -50
            add(
                key,
                face @ pose(*anchor, -params["tie_t"]) @ mirror(x=sign),
                "cap",
                sign * 45 if side else 0,
                0,
                push,
            )
            if side:
                add(
                    "wood_16", face @ pose(wood_x, wood_y, -params["tie_t"]), "metal", sign * 115, 0, push
                )
            for x, y in points:
                add("beam_screw", face @ pose(x, y, -params["tie_t"] + 0.55), "metal", 0, 0, push)
                add(
                    "beam_nut",
                    face @ pose(x, y, params["face_t"] + p["screw"]["nut_near"]),
                    "metal",
                    0,
                    0,
                    push,
                )
    params["retainer_y"].sort()
    return p, params, defs, patterns, parts, units


def component_files(folder, host_folder, params, defs, export, host, p):
    from v8_manufacturing import openscad

    joints.library(folder, p)
    lines = [f"{k}={json.dumps(v)};" for k, v in params.items()]
    (folder / "cabinet_geometry.scad").write_text(
        "\n".join(lines) + "\n$fn=64;\n" + cuts.CABINET_CUTS + cad.CABINET_SOLIDS
    )
    from v8_manufacturing import draw_view
    draw_view(folder, "assembled", dict(host, omit_corner_adapters=True), export)
    for ext in (["scad", "stl"] if export else ["scad"]):
        (folder/("assembled."+ext)).replace(folder/("array_unit."+ext))
    for key in ("front","back"):
        for ext in (["scad", "stl"] if export else ["scad"]):
            shutil.copyfile(host_folder/(key+"."+ext), folder/("array_"+key+"."+ext))
    library = ["include <cabinet_geometry.scad>", "include <beam_joint_geometry.scad>"]
    for name, expr in defs.items():
        library.append(f"module part_{name}() {{ {expr}\n}}")
    for name in ("array_unit", "beam_nut", "beam_screw"):
        library.append(f"module part_{name}() {{ include <{name}.scad>\n}}")
    (folder / "cabinet_parts.scad").write_text("\n".join(library) + "\n")
    for key, expr in defs.items():
        path = folder / (key + ".scad")
        path.write_text("include <cabinet_geometry.scad>\ninclude <beam_joint_geometry.scad>\n" + expr + "\n")
        if export:
            openscad(path, path.with_suffix(".stl"), "--export-format=binstl")


def assembly_source(folder, parts, exploded, export):
    text = [
        "include <cabinet_parts.scad>",
        "// X across, front at depth 0; rotate into Z-up for viewing.",
        "rotate([-90,0,0]) {",
    ]
    colors = dict(
        ply_cap="burlywood",
        ply_side="burlywood",
        frame="teal", cap="darkorange",
        dowel="tan",
        aluminium="silver",
        metal="dimgray",
    )
    for part in parts:
        mat = part.matrix if not exploded else pose(*part.shift) @ part.matrix
        geom = f'import("{part.name}.stl");' if export else f"part_{part.name}();"
        text.append(f'color("{colors[part.material]}") multmatrix({np.round(mat,7).tolist()}) {geom}')
    text.append("}")
    (folder / ("exploded.scad" if exploded else "assembled.scad")).write_text("\n".join(text) + "\n")


def solid(path):
    mesh = trimesh.load_mesh(path)
    obj = m3d.Manifold(m3d.Mesh(mesh.vertices.astype("float32"), mesh.faces.astype("uint32")))
    if obj.is_empty() or obj.status() != m3d.Error.NoError:
        raise ValueError(f"Invalid manufactured mesh: {path}")
    return obj


def validate(folder, parts, units, params, p, host):
    from presentation.sync_packaging import model_folder

    # Broad-phase AABBs, then exact manifold intersections for candidate pairs.
    models = {k: solid(folder / (k + ".stl")) for k in {part.name for part in parts}}
    objects = [(piece.name, models[piece.name].transform(piece.matrix[:3])) for piece in parts]
    pot_dir = model_folder(host["container"])
    pot = solid(pot_dir / "body.stl")
    cfg = json.loads((pot_dir / "model.json").read_text())
    q = p["frame"]
    pot_count = 0
    obstacles = [(name, obj, np.array(obj.bounding_box())) for name, obj in objects if name != "array_unit"]
    travel = q["bank_depth"] + cfg["length"] / 2
    local_sweep = m3d.Manifold.batch_hull([pot, pot.translate((0, -travel, 0))])
    swept_checks = 0
    for ux, uy in units:
        for back in (False, True):
            face = pose(ux, uy, q["assembled_depth"] if back else 0) @ pose(
                rotation=(0, 180 if back else 0, 0)
            )
            for col in (-1, 1):
                for row in range(p["row"]):
                    y = q["opening_origin_y"] + row * q["pitch_y"] + (q["opening_height"] + cfg["height"]) / 2
                    loc = face @ pose(
                        col * q["pitch_x"] / 2, y, q["bank_depth"] - 1.5 - cfg["length"] / 2, (90, 0, 0)
                    )
                    installed = pot.transform(loc[:3])
                    objects.append(("pot", installed))
                    sweep = local_sweep.transform(loc[:3])
                    bounds = np.array(sweep.bounding_box())
                    for name, obj, bb in obstacles:
                        if np.all(np.minimum(bounds[3:], bb[3:]) - np.maximum(bounds[:3], bb[:3]) > 0.001):
                            swept_checks += 1
                            if abs((sweep ^ obj).volume()) > 0.025:
                                raise ValueError(f"Added {name} intrudes into the pot withdrawal path")
                    pot_count += 1
    boxes = np.array([obj.bounding_box() for _, obj in objects])
    checked = 0
    for i, (key, obj) in enumerate(objects):
        overlap = np.minimum(boxes[i, 3:], boxes[:i, 3:]) - np.maximum(boxes[i, :3], boxes[:i, :3])
        for j in np.flatnonzero(np.all(overlap > 0.001, axis=1)):
            other, target = objects[j]
            pair = {key, other}
            if pair in ({"side", "wood_30"}, {"side", "wood_16"}, {"beam_nut", "beam_screw"}):
                continue  # Deliberate thread engagement.
            vol = abs((obj ^ target).volume())
            checked += 1
            if vol > 0.025:
                raise ValueError(f"Interference {key} #{i} / {other} #{j}: {vol:.3f} mm3")
    sides = [obj for key, obj in objects if key == "side"]
    for piece in (piece for piece in parts if piece.name in ("wood_30", "wood_16")):
        length = 30 if piece.name == "wood_30" else 16
        entry = params["t"] if length == 30 else params["tie_t"]
        probe = (
            m3d.Manifold.cylinder(length - entry - 0.4, 1.2, 1.2, 36)
            .translate((0, 0, entry + 0.2))
            .transform(piece.matrix[:3])
        )
        screw = models[piece.name].transform(piece.matrix[:3])
        if (
            any(abs((side ^ probe).volume()) > 0.01 for side in sides)
            or sum(abs((side ^ screw).volume()) for side in sides) < 1
        ):
            raise ValueError("Wood screw missed its side pilot or has no thread engagement")
    # All fasteners must still enter the captive beam nut after changing the outside fitting.
    beyond = p["screw"]["length"] + .55 - params["tie_t"] - (params["face_t"] + p["screw"]["nut_near"] + p["screw"]["nut_depth"])
    if beyond < 1:
        raise ValueError("Insufficient thread beyond the captive beam nut")
    from presentation.drawer_labels import LOCATION_MM
    from presentation.stocked import edge_label_y
    # Sight line from the complete sticker footprint to a plane beyond the bracket and clip faces.
    lw,lh = LOCATION_MM
    sticker = m3d.Manifold.cube((lw,lh,6)).translate((-lw/2,-lh/2,-6.001))
    fixed_objects = [(obj,np.array(obj.bounding_box())) for key,obj in objects if key != "pot"]
    label_count = 0
    for ux,uy in units:
        joined = uy > min(y for _,y in units) + .01
        for back in (False, True):
            face = pose(ux,uy,q["assembled_depth"] if back else 0) @ mirror(z=-1 if back else 1)
            for row in range(p["row"]):
                for side in (-1,1):
                    loc = pose(side*(q["width_total"]-q["drawer_border_edge"])/2,edge_label_y(p,row,joined))
                    sight = sticker.transform((face @ loc)[:3])
                    bb = np.array(sight.bounding_box())
                    for obj,other in fixed_objects:
                        if np.all(np.minimum(bb[3:],other[3:])-np.maximum(bb[:3],other[:3])>.001):
                            if (sight ^ obj).volume() > .01:
                                raise ValueError(f"Location sticker covered at {ux},{uy}, row {row+1}, side {side}")
                    label_count += 1
    lateral = {}
    for name in ("side", "cap", "array_unit"):
        bb = np.array([obj.bounding_box() for key, obj in objects if key == name])
        lateral[name] = np.array([-bb[:, 0].min(), bb[:, 3].max()])
    cap_beyond_side = lateral["cap"] - lateral["side"]
    expected = (params["cap_w"] - params["inside_w"]) / 2 - params["t"]
    if not np.allclose(cap_beyond_side, expected, atol=0.001):
        raise ValueError("Exported cap edges do not match the specified side faces")
    plywood_plates = [
        obj.bounding_box() for name, obj in objects if name in ("plywood_joint", "plywood_double")
    ]
    outside = params["inside_w"] / 2 + params["t"]
    edge_error = max(abs(max(abs(bb[0]), abs(bb[3])) - outside) for bb in plywood_plates)
    if edge_error > 0.001:
        raise ValueError(f"Plywood plate misses outside edge by {edge_error:.3f} mm")
    qty = Counter(v.name for v in parts)
    assert qty["dowel"] == 12 and qty["wood_30"] == 8 and qty["beam_screw"] == qty["beam_nut"] == 72
    assert pot_count == 252 and len(units) == 9 and qty["side"] == qty["cap"] == 2
    assert min(np.diff(params["stations"])) > 8 and params["t"] - 8 >= 4
    save_json(
        folder / "validation.json",
        dict(
            units=len(units),
            open_pots=pot_count,
            unobstructed_location_labels=label_count,
            mesh_pairs_checked=checked,
            allowed_intersection_mm3=0.025,
            withdrawal_paths_checked=pot_count,
            withdrawal_candidate_pairs=swept_checks,
            wood_pilots_with_thread_engagement=qty["wood_30"] + qty["wood_16"],
            cap_beyond_array_each_side_mm=np.round(lateral["cap"] - lateral["array_unit"], 3).tolist(),
            cap_beyond_plywood_sides_mm=np.round(cap_beyond_side, 3).tolist(),
            plywood_joints=4,
            dowels_per_joint=3,
            screws_per_joint=2,
            closed_end_plywood_above_dowels_mm=params["t"] - 8,
            m3_thread_beyond_nut_mm=round(beyond, 3),
            plywood_plate_edge_error_mm=round(edge_error, 4),
            additional_frame_drillings=0,
            plywood_pilot_centre_mm=params["t"] / 2,
            dowel_end_allowance_mm=1,
            permitted_contacts=["screw threads in side pilots", "M3 screws in their nuts"],
        ),
    )


def drill_drawings(folder, pa, p, patterns):
    q = p["frame"]

    def blank(name, a, b):
        doc = ezdxf.new("R2010")
        doc.units = 4
        for layer, color in [("OUTLINE", 7), ("DRILL", 1)]:
            doc.layers.new(layer, dxfattribs={"color": color})
        space = doc.modelspace()
        space.add_lwpolyline([(0, 0), (a, 0), (a, b), (0, b)], close=True, dxfattribs={"layer": "OUTLINE"})
        return doc, space

    drill = []

    def hole(space, view, x, y, diam, task):
        space.add_circle((x, y), diam / 2, dxfattribs={"layer": "DRILL"})
        drill.append((view, round(x, 3), round(y, 3), diam, task))

    cw, t, d, h = pa["cap_w"], pa["t"], pa["depth"], pa["inside_h"]
    doc, sp = blank("cap", cw, d)
    for sign in (-1, 1):
        x = (cw + sign * (pa["inside_w"] + t)) / 2
        for i, z in enumerate(pa["stations"]):
            hole(
                sp,
                "cap_inside",
                x,
                z,
                4 if i % 2 else 6.1,
                "Through; countersink outside to 7 mm at 90 degrees" if i % 2 else "8 mm blind from inside",
            )
    doc.saveas(folder / "cap_inside.dxf")
    doc, sp = blank("side_end", t, d)
    for i, z in enumerate(pa["stations"]):
        hole(
            sp,
            "side_top_and_bottom_end",
            t / 2,
            z,
            2.5 if i % 2 else 6.1,
            "21 mm pilot" if i % 2 else "17 mm blind",
        )
    doc.saveas(folder / "side_end.dxf")
    doc, sp = blank("side_edge", t, h)
    for y in pa["retainer_y"]:
        hole(sp, "side_front_and_rear_edge", t / 2, y, 2.5, "16 mm pilot for retaining tab")
    doc.saveas(folder / "side_front_edge.dxf")
    with (folder / "drilling.csv").open("w", newline="") as f:
        csv.writer(f).writerows([("view", "x_mm", "y_mm", "diameter_mm", "operation"), *drill])


def write_guide(folder, record, host, p, pa, parts):
    cfg = record["cabinet"]
    q = p["frame"]
    t = pa["t"]
    cw = pa["cap_w"]
    h = pa["inside_h"]
    d = pa["depth"]
    qty = Counter(x.name for x in parts)
    cuts_list = [
        ("Top / bottom", "Plywood", 2, cw, d, t),
        ("Left / right side", "Plywood", 2, h, d, t),
        (
            "Inter-tier floor strip",
            "Aluminium flat bar",
            qty["floor_strip"],
            d,
            cfg["runner_width_mm"],
            cfg["runner_mm"],
        ),
    ]
    with (folder / "cut-list.csv").open("w", newline="") as f:
        csv.writer(f).writerows(
            [
                ("piece", "material", "quantity", "length_mm", "width_mm", "thickness_mm"),
                *[(*v[:3], *(round(n, 3) for n in v[3:])) for v in cuts_list],
            ]
        )
    save_json(
        folder / "assembly.json",
        dict(
            version=8,
            frame=record_id(host),
            units=[3, 3],
            pots=252,
            plywood_envelope_mm=[round(cw, 3), round(h + 2 * t, 3), d],
            cap_projection_beyond_sides_mm=cfg["cap_overhang_mm"],
            quantities=dict(qty),
            parameters=pa,
        ),
    )
    rows = "\n".join(f"| {name} | {n} | {a:g} × {b:g} × {th:g} |" for name, _, n, a, b, th in cuts_list)
    edge = (
        "The top and bottom finish flush with the outer side faces (0 mm overhang). Cut them to the assembled outside width."
        if cfg["cap_overhang_mm"] == 0
        else f"The top and bottom project {cfg['cap_overhang_mm']:g} mm beyond the outer side faces."
    )
    side_fit = (
        "Seat the side panels directly against the array. Dry-fit the actual three-frame width before cutting the caps."
        if cfg["side_gap_mm"] == 0
        else f"Allow {cfg['side_gap_mm']:g} mm at each side of the array."
    )
    text = f"""# Nine-unit 2 × 7 drawer cabinet

Nine double-sided V8 frames make a six-column, twenty-one-row cabinet on each face. It holds 126 open SystemPAK 209 pots per face, 252 total.

![Stocked plywood cabinet](presentation.jpg)

[Editable assembly](assembled.scad) · [Stocked CAD](stocked.scad) · [Exploded CAD](exploded.scad) · [2 × 7 frame files](../{record_id(host)}/README.md)

## Cut and drill

The plywood case measures **{cw:g} mm wide × {h+2*t:g} mm high × {d:g} mm deep**. Both side panels fit between the top and bottom. {edge} The front and rear edges of the plywood align with the frame faceplates. Clip caps, fasteners and pots can project beyond those open edges.

| Piece | Quantity | Finished length × width × thickness, mm |
| --- | ---: | --- |
{rows}

{side_fit} Leave {cfg['top_gap_mm']:g} mm above the array. The two inter-tier gaps are {cfg['runner_mm']:g} mm each. Four narrow strips under each upper frame continue the floor support normally provided by the base. Position each pair 20.5 mm either side of its opening centre. Bond the strip ends to the lower frame's front and rear top edges before tightening the ties.

[Cut list](cut-list.csv) · [Drill schedule](drilling.csv) · [Cap inside face](cap_inside.dxf) · [Side top/bottom end](side_end.dxf) · [Side front/rear edge](side_front_edge.dxf)

## Screw the frames together

1. Assemble nine standard 2 × 7 frames. Use their normal faceplates and preload the original beam nuts. Fit the runner strips between tiers.
2. Remove the individual adapters at each outer corner of every module, front and rear. Keep the M3 × 20 countersunk beam screws. Seat each bracket in the exposed receivers and reinstall those screws in the beam nuts.
3. Print eight [across plates](edge_across.stl) and eight [four-way plates](tee4.stl) for the interior junctions. Each plate is 3 mm thick. The four-way pattern includes the 2 mm tier gap.
4. Print eight [single-contact plywood plates](plywood_joint.stl) for the outside corners and eight [two-contact plywood plates](plywood_double.stl) for the side junctions between tiers. The straight edge finishes flush with the outside of the plywood. Each plate uses one wood screw centred across the side panel. The two-contact plate reuses one M3 beam screw from each frame.

On the middle and bottom tiers, centre the first two rows of fixed location stickers **9.65 mm and 20.85 mm below the upper corner beam axis**, respectively. Keep them centred across the faceplate side margin. These positions clear the vertical brackets and the next row of caps. The other rows use the standard frame positions.

![Exploded case and frame array](exploded.jpg)

## Join the four plywood sheets

Each of the four plywood corners uses **three Ø6 × 24 mm dowels and two 3.5 × 30 mm countersunk wood screws**. Total twelve dowels and eight case screws. Along the {d:g} mm depth, measure {', '.join(f'{v:g}' for v in pa['stations'])} mm from the front edge. The sequence is dowel, screw, dowel, screw, dowel.

1. Centre all five bores on the side thickness, {t/2:g} mm from either side face. Use the inside cap drawing for the mating centres. Drill the Ø6.1 dowel bores 8 mm into the cap and 17 mm into the side end. This leaves 4 mm of plywood over each blind cap bore and 1 mm total axial allowance for the dowel.
2. Drill Ø4 clearance through the caps at the two screw stations. Countersink the **outside** to Ø7. Drill Ø2.5 pilots 21 mm deep into each side end. Match the countersink to the actual screw head and check the pilot in an offcut of the chosen plywood.
3. Dry-fit the dowels and panels around the array. Seat the dowels in the blind bores, clamp square, then drive the two case screws at each joint from the outside. Insert the array from an open face if the case was built separately.
4. Fasten each of the sixteen plywood plates into a side's front or rear edge with one **3.5 × 16 mm countersunk wood screw** in its Ø2.5 pilot. These plates keep the array from sliding out of the shell. Install the pots after tightening.

![Exploded top-to-side plywood joint](joint-detail.jpg)

The [fit report](validation.json) checks the produced CAD solids, both banks of pots and the added hardware. Structural load capacity, dowel fit and screw holding strength require a physical trial. The [location labels](labels-location.pdf) use a distinct address on each face of the full cabinet. [Contents labels](labels-contents.pdf) · [Label map](label-map.json).
"""
    (folder / "README.md").write_text(text, encoding="utf-8")
    (folder / "printing.txt").write_text(
        "Build nine standard 2x7 frames. Print eight of each bracket. Reuse the corner beam screws. See README.md for the plywood drawings, fasteners and assembly order.\n"
    )


def stocked_source(folder, p, units, host):
    from presentation.sync_packaging import model_folder

    ref = model_folder(host["container"])
    cfg = json.loads((ref / "model.json").read_text())
    shutil.copyfile(ref / "body.stl", folder / "pot_reference.stl")
    q = p["frame"]
    lines = ["include <assembled.scad>", "color([.78,.89,.88,.55]) rotate([-90,0,0]) {"]
    for x, y in units:
        for back in [False, True]:
            face = pose(x, y, q["assembled_depth"] if back else 0) @ pose(rotation=(0, 180 if back else 0, 0))
            for c in (-1, 1):
                for row in range(p["row"]):
                    base = (
                        q["opening_origin_y"] + row * q["pitch_y"] + (q["opening_height"] + cfg["height"]) / 2
                    )
                    mat = face @ pose(
                        c * q["pitch_x"] / 2, base, q["bank_depth"] - 1.5 - cfg["length"] / 2, (90, 0, 0)
                    )
                    lines.append(f'multmatrix({np.round(mat,7).tolist()}) import("pot_reference.stl");')
    (folder / "stocked.scad").write_text("\n".join(lines + ["}"]) + "\n")


def finish(folder, record, host, p, pa, defs, patterns, parts, units, export, *, render_images=True):
    hf = folder.parent / record_id(host)
    assembly_source(folder, parts, False, export)
    assembly_source(folder, parts, True, export)
    drill_drawings(folder, pa, p, patterns)
    write_guide(folder, record, host, p, pa, parts)
    stocked_source(folder, p, units, host)
    if not export:
        (folder / "README.md").write_text(
            "# Nine-unit cabinet CAD sources\n\nOpen [assembled.scad](assembled.scad), "
            "[stocked.scad](stocked.scad) or [exploded.scad](exploded.scad). "
            "[Cut list](cut-list.csv) · [Drilling schedule](drilling.csv). "
            "Run make-all with STL export for the checked workshop kit and illustrated guide.\n",
            encoding="utf-8",
        )
        return
    validate(folder, parts, units, pa, p, host)
    if render_images:
        from presentation.cabinet import render

        render(folder, hf, p, record, parts, units, pa)


def build(folder, record, host, export):
    from v8_manufacturing import write_solid

    p, pa, defs, patterns, parts, units = plan(record, host)
    component_files(folder, folder.parent / record_id(host), pa, defs, export, host, p)
    import oobb
    for kind in ("screw", "nut"):
        part = oobb.get_default_thing(type="beam_hardware_reference")
        cad.draw_hardware(part, dict(p, corner_fixing={"screw_length":p["screw"]["length"]}), kind)
        write_solid(folder, "beam_"+kind, part, export, mode="true")
    finish(folder, record, host, p, pa, defs, patterns, parts, units, export)


def rebuild(root, record, records):
    host = next(v for v in records if v["variant"] == record["cabinet"]["host"])
    folder = root / "parts" / record_id(record)
    with TemporaryDirectory(prefix=".cabinet-", dir=folder.parent) as tmp:
        stage = Path(tmp)
        build(stage, record, host, True)
        from v8_manufacturing import publish
        publish(stage,folder)
    from presentation.catalogue import write_index

    write_index(root, [r for r in records if (root / "parts" / record_id(r) / "README.md").is_file()])
