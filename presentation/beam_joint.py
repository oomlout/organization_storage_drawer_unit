"""Test installed beam joints at both faces and export a small, real assembly detail."""

import json

import manifold3d as m3d
import numpy as np
import trimesh

from .scenes import pose, write_hardware
import working_scad as cad


def save(mesh, path):
    raw = mesh.to_mesh()
    trimesh.Trimesh(raw.vert_properties[:, :3], raw.tri_verts, process=False).export(path)


def render_installation(folder, holes, wood, a_faces, a_rails, hardware, joint, t, prefix):
    from v8_manufacturing import openscad

    # Small section of each actual face and beam, plus the seated fixings.
    x1 = max(v[0] for v in holes + ([wood] if wood else []))
    y1 = max(v[1] for v in holes)
    crop = m3d.Manifold.cube((x1 + 30, y1 + 28, 30)).translate((-15, -14, -3))
    lines = ["rotate([-90,0,0]) {"]
    for tag, objs, color in [
        ("face", a_faces, "teal"),
        ("rail", a_rails, "darkslategray"),
        ("hardware", hardware, "silver"),
        ("bracket", [joint], "orange"),
    ]:
        result = m3d.Manifold.batch_boolean(objs, m3d.OpType.Add) ^ crop
        save(result, folder / (prefix + "detail_" + tag + ".stl"))
        lines.append(f'color("{color}") import("{prefix}detail_{tag}.stl");')
    if wood:
        px, py = wood
        lines += [
            f'color("burlywood") difference() {{translate([{px-6},-14,0]) cube([12,{y1+28},27]); translate([{px},{py},-.05]) cylinder(d=2.5,h=16.05,$fn=48);}}',
            f'color("silver") translate([{px},{py},{-t}]) wood_screw(16);',
        ]
    lines.append("}")
    if wood:
        lines.append(cad.CABINET_SOLIDS)
    source = folder / (prefix + "installed.scad")
    source.write_text("\n".join(lines))
    openscad(
        source,
        folder / (prefix + "installed.png"),
        "--preview",
        "--viewall",
        "--autocenter",
        "--imgsize=900,625",
        "--projection=o",
        "--camera=60,-100,76,0,0,4",
    )


def withdrawal_sweeps(p):
    from presentation.sync_packaging import model_folder
    from v8_cabinet import solid

    model = model_folder(p["container"])
    cfg = json.loads((model / "model.json").read_text())
    pot = solid(model / "body.stl")
    q = p["frame"]
    travel = q["bank_depth"] + cfg["length"] / 2
    hull = m3d.Manifold.batch_hull([pot, pot.translate((0, -travel, 0))])
    sweeps = []
    for col in range(p["column"]):
        x = -q["width_total"] / 2 + q["drawer_border_edge"] + q["opening_width"] / 2 + col * q["pitch_x"]
        for row in range(p["row"]):
            y = q["opening_origin_y"] + row * q["pitch_y"] + (q["opening_height"] + cfg["height"]) / 2
            seated = pose(x, y, q["bank_depth"] - 1.5 - cfg["length"] / 2, (90, 0, 0))
            sweeps.append(hull.transform(seated[:3]))
    return sweeps


def fit_cases(folder, hosts, frames, applications, shapes, reference, scratch):
    from v8_beam_joints import dimensions, JOINT_PLATE_MM
    from presentation.drawer_labels import LOCATION_MM
    from presentation.stocked import edge_label_y
    from v8_cabinet import solid, mirror
    from working_oomp_populate import record_id

    write_hardware(hosts[reference], scratch)
    screw = solid(scratch / "screw.stl")
    nut = solid(scratch / "nut.stl")
    report = {}
    illustrated = set()
    for name, p in hosts.items():
        hf = folder.parent / record_id(frames[name])
        q = p["frame"]
        hx, upper, lower, _ = dimensions(p)
        sweeps = withdrawal_sweeps(p)
        beam = solid(hf / "screw_beam.stl")
        assembled = solid(hf / "assembled.stl")
        adapter = solid(hf / "screw_adapter.stl")
        native_t = p["screw"]["flange_size"][2]
        lw, lh = LOCATION_MM
        label = m3d.Manifold.cube((lw, lh, 6)).translate((-lw / 2, -lh / 2, -6.001))
        bore = m3d.Manifold.cylinder(6, 1.8, 1.8, 64).translate((0, 0, -5.99))
        t = JOINT_PLATE_MM
        for back in (False, True):
            face = solid(hf / ("back.stl" if back else "front.stl"))
            if back:
                face = face.transform(mirror(x=-1)[:3])
            visible = (
                assembled.transform((mirror(z=-1) @ pose(z=-q["assembled_depth"]))[:3])
                if back
                else assembled
            )
            original = adapter.transform(mirror(y=-1 if back else 1)[:3]).translate((0, 0, -native_t))
            corners = {}
            roi = m3d.Manifold.cube((44, 106, 37)).translate((-22, -53, 0))
            for m in p["frame_mounts"]:
                if not m["corner_beam"]:
                    continue
                x, y = m["x"], m["hole_y"]
                native = cad.v8_beam_to_frame(p, m, "screw_beam")
                inward = mirror(z=-1) @ pose(z=-q["assembled_depth"]) if back else np.eye(4)
                rail = beam.transform((pose(-x, -y) @ inward @ native)[:3])
                outside = m3d.Manifold.cube((44, 106, t)).translate((-22, -53, -t))
                fittings = (visible.translate((-x, -y, 0)) ^ outside) - original
                corners[x, y] = (face.translate((-x, -y, 0)) ^ roi, rail ^ roi, fittings)
            for stem, (holes, _, wood) in shapes.items():
                if not any(v.split()[0] == name for v in applications[stem]):
                    continue
                bracket = solid(folder / (stem + ".stl")).translate((0, 0, -t))
                worst = 0
                fits = 0
                pot_checks = 0
                face_checks = 0
                for sx in ((-1, 1) if len({v[0] for v in holes}) == 1 else (1,)):
                    for end in ((upper, lower) if len({v[1] for v in holes}) == 1 else (lower,)):
                        joint = bracket.transform(mirror(x=sx)[:3])
                        a_faces = []
                        a_rails = []
                        hardware = []
                        for x, y in holes:
                            corner_x = (sx if x == 0 else -sx) * hx
                            corner_y = end if y == 0 else upper
                            in_host = joint.translate((corner_x - sx * x, corner_y - y, 0))
                            for sweep in sweeps:
                                worst = max(worst, abs((in_host ^ sweep).volume()))
                                pot_checks += 1
                            joined_above = name == "2x7" and y > 0
                            margin = (q["width_total"] - q["drawer_border_edge"]) / 2
                            for row in range(p["row"]):
                                for sign in (-1, 1):
                                    sticker = label.translate(
                                        (sign * margin, edge_label_y(p, row, joined_above), 0)
                                    )
                                    worst = max(worst, abs((in_host ^ sticker).volume()))
                            for axis in q["corner_holes"]:
                                worst = max(
                                    worst,
                                    abs((in_host ^ bore.translate((axis["x"], axis["y"], 0))).volume()),
                                )
                            f, r, fittings = corners[corner_x, corner_y]
                            worst = max(worst, abs((joint ^ fittings.translate((sx * x, y, 0))).volume()))
                            face_checks += 1
                            xy = (sx * x, y, 0)
                            a_faces.append(f.translate(xy))
                            a_rails.append(r.translate(xy))
                            hardware += [
                                screw.translate((sx * x, y, -t + 0.55)),
                                nut.translate((sx * x, y, p["panel_thickness"] + p["screw"]["nut_near"])),
                            ]
                        for obj in a_faces + a_rails + hardware:
                            worst = max(worst, abs((joint ^ obj).volume()))
                        fits += 1
                        if worst > 0.025:
                            raise ValueError(
                                f"{stem} interferes on {name} ({back=}, {sx=}, {end=}) by {worst:.3f} mm3"
                            )
                        showcase = bool(wood) or stem.startswith("tee4")
                        example = (bool(wood), len(holes))
                        if (
                            example not in illustrated
                            and showcase
                            and name == reference
                            and not back
                            and sx == 1
                        ):
                            illustrated.add(example)
                            prefix = "double_" if wood and len(holes) == 2 else ""
                            render_installation(
                                folder, holes, wood, a_faces, a_rails, hardware, joint, t, prefix
                            )
                report.setdefault(name, {}).setdefault(stem, {})["rear" if back else "front"] = dict(
                    placements=fits,
                    face_hole_cap_and_label_checks=face_checks,
                    withdrawal_paths=pot_checks,
                    max_intersection_mm3=round(worst, 5),
                )
    return report
