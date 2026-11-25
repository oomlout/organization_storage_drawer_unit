"""Build presentation views from the same mesh coordinates used in the V8 fit tests."""

import json
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
import oobb
import trimesh

import working_scad as cad
from v8_validation import region_clip

HERE = Path(__file__).resolve().parent


def pose(x=0, y=0, z=0, rotation=(0, 0, 0)):
    matrix = trimesh.transformations.euler_matrix(*np.radians(rotation))
    matrix[:3, 3] = (x, y, z)
    return matrix


def item(path, role, matrix=None):
    return (str(path.resolve()), role, (np.eye(4) if matrix is None else np.asarray(matrix)).tolist())


def tray_reference(path, dims, inset):
    """Open tapered pot and lip for illustration; only the envelope is specified by the record."""
    w, h, d = (dims[k] for k in ("across", "height", "depth"))
    rings = [
        (w * 0.5 - inset - 2, d * 0.5 - 4, h),
        (w * 0.5 - inset, d * 0.5 - 2, 2),
        (w * 0.5, d * 0.5, 2),
        (w * 0.5, d * 0.5, 0),
        (w * 0.5 - inset - 0.7, d * 0.5 - 2.7, 0),
        (w * 0.5 - inset - 2.7, d * 0.5 - 4.7, h - 0.7),
    ]
    vertices = [(sx * a, y, sz * b) for a, b, y in rings for sx, sz in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
    triangles = [(0, 1, 2), (0, 2, 3), (20, 22, 21), (20, 23, 22)]
    for r in range(len(rings) - 1):
        for n in range(4):
            a, b = 4 * r + n, 4 * r + (n + 1) % 4
            triangles.extend([(a, b, b + 4), (a, b + 4, a + 4)])
    mesh = trimesh.Trimesh(vertices=vertices, faces=triangles)
    mesh.fix_normals()
    mesh.export(path)


def write_hardware(p, scratch):
    from v8_manufacturing import write_solid

    for kind in ("screw", "nut"):
        thing = oobb.get_default_thing(type="presentation_hardware")
        cad.draw_hardware(thing, dict(p, corner_fixing={"screw_length": p["screw"]["length"]}), kind)
        write_solid(scratch, kind, thing, True, mode="true")


def frame_views(folder, p, scratch):
    q = p["frame"]

    def part(name, role, matrix=None):
        return item(folder / (name + ".stl"), role, matrix)

    front = part("front", "frame")
    rear = pose(z=q["assembled_depth"], rotation=(0, 180, 0))
    beams, nuts, finish, exploded = [], [], [], []
    typical = None
    for m in p["frame_mounts"]:
        kind = m["kind"]
        snap = kind == "snap_beam"
        beam = part(kind, "rail", cad.v8_beam_to_frame(p, m, kind))
        beams.append(beam)
        for back in (False, True):
            depth = q["assembled_depth"] if back else 0
            sign = -1 if back else 1
            extension = (
                p["front_plug"]["outer_y"] - p["panel_thickness"] if snap else p["screw"]["flange_size"][2]
            )
            fitting = m.get("cap_component", "front_plug") if snap else "screw_adapter"
            x, y = m["x"], m["hole_y"]
            trans = pose(x, y, depth - sign * extension, cad.v8_external_part_rotation(p, kind, back))
            finish.append(part(fitting, "cap", trans))
            exploded.append(part(fitting, "cap", pose(z=-sign * 10) @ trans))
            if not snap:
                rot = (0, 180 if back else 0, 0)
                nut = pose(x, y, depth + sign * (p["panel_thickness"] + p["screw"]["nut_near"]), rot)
                nuts.append(item(scratch / "nut.stl", "metal", nut))
                screw = pose(x, y, depth + sign * (-extension + 0.55), rot)
                finish.append(item(scratch / "screw.stl", "metal", screw))
                exploded.append(item(scratch / "screw.stl", "metal", pose(z=-sign * 23) @ screw))
                if typical is None:
                    typical = (m, beam, nut)
    m, beam, nut = typical
    # Show the actual end with its nut outside the side-loading slot.
    mesh = trimesh.load_mesh(beam[0])
    mesh.apply_transform(beam[2])
    center = np.array([m["x"], m["hole_y"], p["panel_thickness"]])
    region_clip(mesh, center + [-17, -16, -9], center + [17, 16, 34]).export(scratch / "end.stl")
    # The front end opens towards +X in assembled coordinates.
    end = [item(scratch / "end.stl", "rail"), item(scratch / "nut.stl", "metal", pose(x=12) @ nut)]
    open_frame = [front, *beams, *nuts]
    closed = [*open_frame, part("back", "frame", rear)]
    complete = [*closed, *finish]
    tray_reference(scratch / "pot.stl", p["container_dimensions_mm"], q["inset_lip"])
    drawers = []
    for col in range(min(2, p["column"])):
        row = min(col, p["row"] - 1)
        x = -q["width_total"] / 2 + q["drawer_border_edge"] + q["opening_width"] / 2 + col * q["pitch_x"]
        y = q["opening_origin_y"] + row * q["pitch_y"] + 0.7
        d = p["container_dimensions_mm"]["depth"]
        drawers.append(
            item(scratch / "pot.stl", "tray", pose(x, y, d / 2 - (d * 0.40 if col == 0 else d * 0.12)))
        )
    return [
        (end, (1.35, -1.3, 0.85)),
        (open_frame, (0.9, 1.65, 0.85)),
        ([*open_frame, part("back", "frame", pose(z=35) @ rear)], (0.95, 1.7, 0.85)),
        ([*closed, *exploded], (0.85, -1.8, 0.85)),
        ([*complete, *drawers], (0.88, -2, 0.8)),
    ]


def joiner_views(folder, p, scratch, host):
    part = p["joiners"][0]
    depth = part["size"][2]
    j = p["corner_fixing"]
    for file in ("joiners", "joiner_backers"):
        body = min(trimesh.load_mesh(folder / (file + ".stl")).split(), key=lambda m: m.centroid[0])
        body.apply_translation(-np.array(part["print_center"]))
        body.export(scratch / (file + ".stl"))
    frame = trimesh.load_mesh(host / "assembled.stl")
    faces = []
    for i, xy in enumerate(cad.v8_joiner_layout(p)["units"]):
        shifted = frame.copy()
        shifted.apply_translation(xy)
        region_clip(shifted, [-23, -22, -6], [23, 22, 29]).export(scratch / f"corner{i}.stl")
        faces.append(item(scratch / f"corner{i}.stl", "frame"))

    def front(offset=0):
        return item(scratch / "joiners.stl", "frame", pose(z=-depth - offset))

    def back(offset=0, y=0):
        return item(scratch / "joiner_backers.stl", "backer", pose(y=y, z=end + offset, rotation=(180, 0, 0)))

    def hardware(name, z, dy=0):
        return [
            item(folder / f"joiner_{name}_reference.stl", "metal", pose(x, y + dy, z))
            for x, y in part["holes"]
        ]

    end = p["panel_thickness"] + j["backer_depth"]
    seat = end - j["nut_recess"]
    screw = -depth + j["screw_reference_recess"]
    seated = [*faces, back(), *hardware("nut", seat)]
    return [
        ([back(), *hardware("nut", seat + 6)], (0.65, 1.8, 1.15)),
        ([*faces, back(10, -8), *hardware("nut", seat + 10, -8)], (0.9, 1.6, 0.9)),
        ([*seated, front(10)], (0.85, -1.55, 1.05)),
        ([*seated, front(), *hardware("screw", screw - 9)], (0.85, -1.55, 1.05)),
        ([*seated, front(), *hardware("screw", screw)], (0.6, -1.6, 0.9)),
    ]


def render(folder, p, record, meta, host=None, *, images=True):
    exe = shutil.which("blender")
    if images and not exe:
        raise RuntimeError("Install Blender 5 and add its executable to PATH to build the assembly manuals")
    with TemporaryDirectory() as tmp:
        scratch = Path(tmp)
        if host is None:
            write_hardware(p, scratch)
        if images:
            views = (
                frame_views(folder, p, scratch) if host is None else joiner_views(folder, p, scratch, host)
            )
            outputs = [folder / f"assembly-step-{n}.jpg" for n in range(1, 5)] + [folder / "presentation.jpg"]
            data = {
                "views": [
                    dict(output=str(out.resolve()), items=items, eye=eye)
                    for out, (items, eye) in zip(outputs, views)
                ]
            }
            job = scratch / "views.json"
            job.write_text(json.dumps(data), encoding="utf-8")
            result = subprocess.run(
                [
                    exe,
                    "--background",
                    "--factory-startup",
                    "--python-exit-code",
                    "1",
                    "--python",
                    str(HERE / "blender_render.py"),
                    "--",
                    str(job),
                ],
                capture_output=True,
                text=True,
                errors="replace",
                timeout=1200,
            )
            if result.returncode or not all(out.is_file() for out in outputs):
                raise RuntimeError(
                    "Blender presentation render failed\n" + (result.stdout + result.stderr)[-3000:]
                )
        from .catalogue import guide, inventory, write_part
        from .manual import make

        steps = guide(record, meta)
        items = inventory(record, meta)
        meshes = {key: folder / (key + ".stl") for _, _, key, _ in items}
        for key in ("screw", "nut"):
            meshes[key] = (
                scratch / (key + ".stl") if host is None else folder / ("joiner_" + key + "_reference.stl")
            )
        make(folder, record, meta, steps, items, meshes)
        write_part(folder, record, meta, steps, items)
