"""Studio photographs of the production meshes and their installation sections."""

from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess

from .scenes import item, pose


def render_views(views):
    exe = shutil.which("blender")
    if not exe:
        raise RuntimeError("Install Blender and add it to PATH")
    with TemporaryDirectory() as tmp:
        job = Path(tmp) / "views.json"
        job.write_text(json.dumps({"views": views}), encoding="utf-8")
        run = subprocess.run(
            [
                exe,
                "-b",
                "--factory-startup",
                "--python-exit-code",
                "1",
                "-P",
                str(Path(__file__).with_name("blender_render.py")),
                "--",
                str(job),
            ],
            capture_output=True,
            text=True,
            errors="replace",
            timeout=1500,
        )
        if run.returncode or not all(Path(v["output"]).is_file() for v in views):
            raise RuntimeError((run.stdout + run.stderr)[-4000:])


def view(path, items, eye, size=(1200, 880)):
    return dict(output=str(path.resolve()), items=items, eye=eye, resolution=size, samples=32)


def plywood_geometry(holes, wood, thickness):
    x, y = wood
    h = max(p[1] for p in holes) + 28
    return [
        (
            "ply_side",
            f"difference() {{translate([{x-6},-14,0]) cube([12,{h},27]); translate([{x},{y},-.05]) cylinder(d=2.5,h=16.05,$fn=64);}}",
        ),
        ("metal", f"translate([{x},{y},{-thickness}]) wood_screw(16);"),
    ]


def render_joints(folder, shapes, thickness, reference_pitch):
    import trimesh
    from v8_manufacturing import openscad
    import working_scad as cad

    views = []
    gallery = []
    flat = pose(rotation=(90, 0, 0))
    offset = 0
    for name in shapes:
        stl = folder / (name + ".stl")
        bounds = trimesh.load_mesh(stl).bounds
        width = bounds[1, 0] - bounds[0, 0]
        center = (bounds[0] + bounds[1]) / 2
        part = flat @ pose(rotation=(180, 0, -12)) @ pose(*(-center))
        views.append(
            view(folder / (name + ".jpg"), [item(stl, "joint", part)], (0.45, -1.25, 1.95), (820, 640))
        )
        if "_" + reference_pitch in name or name in ("edge_across", "plywood_joint"):
            gallery.append(
                item(
                    stl,
                    "joint",
                    flat @ pose(offset + width / 2, 0, 0) @ pose(rotation=(180, 0, 0)) @ pose(*(-center)),
                )
            )
            offset += width + 8
    views.append(view(folder / "presentation.png", gallery, (0.32, -1.0, 2.05), (1440, 900)))
    with TemporaryDirectory() as tmp:
        scratch = Path(tmp)
        for prefix in ("", "double_"):
            if not (folder / (prefix + "detail_face.stl")).is_file():
                continue
            pieces = [
                item(folder / (prefix + "detail_" + name + ".stl"), role)
                for name, role in (
                    ("face", "frame"),
                    ("rail", "rail"),
                    ("hardware", "metal"),
                    ("bracket", "joint"),
                )
            ]
            if "plywood_joint" in shapes:
                name = "plywood_double_" + reference_pitch if prefix else "plywood_joint"
                holes, _, wood = shapes[name]
                for role, body in plywood_geometry(holes, wood, thickness):
                    source = scratch / (prefix + role + ".scad")
                    source.write_text(cad.CABINET_SOLIDS + "\n" + body)
                    mesh = source.with_suffix(".stl")
                    openscad(source, mesh, "--export-format=binstl")
                    pieces.append(item(mesh, role))
            views.append(view(folder / (prefix + "installed.png"), pieces, (0.85, -1.85, 0.8)))
        render_views(views)
