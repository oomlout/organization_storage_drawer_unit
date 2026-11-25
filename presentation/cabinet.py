"""Render the physical cabinet, its globally addressed pots, and a case-joint detail."""

import json
import os
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

import manifold3d as m3d
import numpy as np
import trimesh

from . import drawer_labels, scenes, stocked
from .scenes import pose, item
from .sync_packaging import model_folder


def render(folder, host_folder, p, record, parts, units, params):
    with TemporaryDirectory() as tmp:
        scratch = Path(tmp)
        source = scratch / "host"
        source.mkdir()
        for stl in host_folder.glob("*.stl"):
            try:
                os.link(stl, source / stl.name)
            except OSError:
                shutil.copyfile(stl, source / stl.name)
        # Match the assembled/face meshes to the cabinet host with its corner adapters removed.
        for a, b in [("array_unit", "assembled"), ("array_front", "front"), ("array_back", "back")]:
            (source / (b + ".stl")).unlink()
            shutil.copyfile(folder / (a + ".stl"), source / (b + ".stl"))
        scenes.write_hardware(p, scratch)
        structure = scenes.frame_views(source, dict(p,omit_corner_adapters=True), scratch, structure_only=True)
        nx, ny = record["cabinet"]["units_across"], record["cabinet"]["units_high"]
        cols, rows = p["column"], p["row"]
        grid = dict(column=nx * cols, row=ny * rows, variant=record["variant"])
        labels, art = drawer_labels.generate(folder, scratch, grid)
        slots = {(v["side"], v["x"], v["y"]): v for v in labels}
        complete = []
        exploded = []
        joint = []
        for piece in parts:
            if piece.name == "array_unit":
                continue
            mesh = folder / (piece.name + ".stl")
            complete.append(item(mesh, piece.material, piece.matrix))
            exploded.append(item(mesh, piece.material, pose(*piece.shift) @ piece.matrix))
        for i, (x, y) in enumerate(units):
            col, row = i % nx, i // nx
            local = []
            for side in ("F", "R"):
                for iy in range(1, rows + 1):
                    for ix in range(1, cols + 1):
                        block = col if side == "F" else nx - 1 - col
                        local.append(dict(slots[side, block * cols + ix, row * rows + iy], x=ix, y=iy))
            view = stocked.frame_pots(source, scratch, p, p, structure, labels=(local, art), joined_above=row>0)[1][0]
            complete.extend((path, role, (pose(x, y) @ matrix).tolist()) for path, role, matrix in view)
            offset = pose(x + (col - (nx - 1) / 2) * 20, y + (row - (ny - 1) / 2) * 20, 0)
            exploded.extend((path, role, (offset @ matrix).tolist()) for path, role, matrix in structure)
        # Cut away only the distant panel areas; include all five real fixings.
        iw, ih, t, d = (params[k] for k in ("inside_w", "inside_h", "t", "depth"))
        top = next(v.matrix[1, 3] for v in parts if v.name == "cap" and v.matrix[1, 1] < 0)
        box = m3d.Manifold.cube((80, 105, d + 4)).translate((iw / 2 - 45, top - 20, -2))
        for piece in parts:
            x, y = piece.matrix[:2, 3]
            if (piece.name == "cap" and y == top) or (piece.name == "side" and x > 0):
                obj = stocked.solid(folder / (piece.name + ".stl")).transform(piece.matrix[:3]) ^ box
                raw = obj.to_mesh()
                path = scratch / (piece.name + "-corner.stl")
                trimesh.Trimesh(raw.vert_properties[:, :3], raw.tri_verts, process=False).export(path)
                joint.append(item(path, piece.material, pose(y=-52 if piece.name == "cap" else 0)))
            elif x > 0 and y < top + 25 and piece.name in ("wood_30", "dowel"):
                joint.append(
                    item(
                        folder / (piece.name + ".stl"),
                        piece.material,
                        pose(y=-75 if piece.name == "wood_30" else -24) @ piece.matrix,
                    )
                )
        views = [
            ("presentation", complete, (0.58, -2, 0.62), [2000, 1600]),
            ("exploded", exploded, (0.95, -2, 1.00), [1700, 1350]),
            ("joint-detail", joint, (2.0, -0.75, 0.9), [1400, 1050]),
        ]
        job = scratch / "cabinet.json"
        job.write_text(
            json.dumps(
                {
                    "views": [
                        dict(
                            output=str((folder / (name + ".jpg")).resolve()),
                            items=items,
                            eye=eye,
                            resolution=res,
                        )
                        for name, items, eye, res in views
                    ]
                }
            )
        )
        blender = shutil.which("blender")
        if not blender:
            raise RuntimeError("Blender is needed to render the cabinet")
        result = subprocess.run(
            [
                blender,
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
        if result.returncode or not all((folder / (n + ".jpg")).is_file() for n, *_ in views):
            raise RuntimeError((result.stdout + result.stderr)[-5000:])
