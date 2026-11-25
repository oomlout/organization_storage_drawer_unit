"""Place OOMP reference pots, permanent frame addresses and removable part labels."""

import json
from pathlib import Path

import numpy as np
import trimesh
import manifold3d
import oobb

from . import drawer_labels
from .sync_packaging import model_folder


def solid(file):
    mesh = trimesh.load_mesh(file)
    return manifold3d.Manifold(manifold3d.Mesh(mesh.vertices.astype("float32"), mesh.faces.astype("uint32")))


def edge_label_y(p, row, joined_above=False):
    q = p["frame"]
    if joined_above and row < 2:
        top_beam = min(m["hole_y"] for m in p["frame_mounts"] if m["corner_beam"])
        # Both 10.8 mm stickers share the clear margin between the bracket and the next cap.
        return top_beam + (9.65, 20.85)[row]
    return q["opening_origin_y"] + row*q["pitch_y"] + 6.6


def frame_pots(folder, scratch, p, record, frame, *, labels=None, joined_above=False):
    from .scenes import item, pose
    from v8_manufacturing import write_solid
    import working_scad as cad

    model = model_folder(record["container"])
    cfg = json.loads((model / "model.json").read_text(encoding="utf-8"))
    body = model / cfg["body_file"]
    q = p["frame"]
    rows, images = labels if labels is not None else drawer_labels.generate(folder, scratch, record)
    hull = solid(body)
    host = solid(folder / "assembled.stl")
    loaded = []
    display = []
    all_pots = []
    overlap = 0
    # The removable lid exceeds the 28.5 mm opening on the 209 frames.
    # Keep it off, with the open tub centred vertically in each opening.
    w, l, h = (cfg[k] for k in ("width", "length", "height"))
    seat = q["bank_depth"] - 1.5 - l / 2

    def decal(png, matrix, size):
        return item(images / png, "decal", matrix @ np.diag([*size, 1, 1]))

    for entry in rows:
        rear = entry["side"] == "R"
        col = (record["column"] - entry["x"]) if rear else entry["x"] - 1
        row = entry["y"] - 1
        x = -q["width_total"] / 2 + q["drawer_border_edge"] + q["opening_width"] / 2 + col * q["pitch_x"]
        y = q["opening_origin_y"] + row * q["pitch_y"]
        face = pose(z=q["assembled_depth"], rotation=(0, 180, 0)) if rear else pose()
        # Local X always increases towards the viewer's right.
        local_x = -x if rear else x
        place = face @ pose(local_x, y + (q["opening_height"] + h) / 2, seat, (90, 0, 0))
        instance = hull.transform(place[:3, :])
        overlap = max(overlap, (host ^ instance).volume())
        all_pots.append(instance)
        loaded.append(item(body, "pp", place))
        if not rear and col < 2 and row == min(col, record["row"] - 1):
            display.append(item(body, "pp", pose(z=-l * (0.32 if col == 0 else 0.08)) @ place))
        # The end wall slopes outwards. Mount the content sticker to that surface.
        base_inset = cfg["shoulder"] + cfg["draft"]
        slope = cfg["draft"] / (h - cfg["collar_height"] - 0.75 - 1.2)
        label_z = (h - cfg["collar_height"]) / 2
        short_end = -l / 2 + base_inset - slope * (label_z - 1.2) - 0.15
        angle = 90 + np.degrees(np.arctan(slope))
        loaded.append(
            decal(
                entry["content_png"],
                place @ pose(0, short_end, label_z, (angle, 0, 0)),
                drawer_labels.CONTENTS_MM,
            )
        )
        # Outer columns use solid face margins. Interior columns use the fixed cap face.
        if col in (0, record["column"] - 1):
            edge = (1 if col else -1) * (q["width_total"] - q["drawer_border_edge"]) / 2
            fixed = face @ pose(-edge if rear else edge, edge_label_y(p,row,joined_above), -0.12, (180, 0, 0))
        else:
            # Grid row receivers sit at the vertical divider nearest the slot.
            mount = min(
                p["frame_mounts"],
                key=lambda m: abs(m["x"] - (x - q["pitch_x"] / 2))
                + abs(m["hole_y"] - (y + q["depth_lip"] + 8)),
            )
            fixed = face @ pose(-mount["x"] if rear else mount["x"], mount["hole_y"], -4.74, (180, 0, 0))
        loaded.append(decal(entry["location_png"], fixed, drawer_labels.LOCATION_MM))
        length = entry["part"].get("length_mm")
        if (
            length
            and entry["part"]["id"]
            == f"hardware_screw_countersunk_hex_head_black_m3_diameter_{length}_mm_length"
        ):
            screw = scratch / f"stock-screw-{length}.stl"
            if not screw.exists():
                thing = oobb.get_default_thing(type="purchased_hardware")
                cad.draw_hardware(thing, dict(p, corner_fixing={"screw_length": length}), "screw")
                write_solid(scratch, screw.stem, thing, True, mode="true")
            for sx, sy, turn in [(-13, -23, 12), (4, -7, 42), (-8, 11, -30), (9, 24, 75)]:
                loaded.append(
                    item(screw, "stock_metal", place @ pose(sx, sy, 4, (0, 90, turn)) @ pose(z=-length / 2))
                )
    if overlap > 0.02:
        raise ValueError(f"Installed {record['variant']} pot collides with frame by {overlap:.3f} mm³")
    pots = manifold3d.Manifold.batch_boolean(all_pots, manifold3d.OpType.Add)
    shared = max(0.0, sum(m.volume() for m in all_pots) - pots.volume())
    if shared > 0.02:
        raise ValueError(f"Installed pots overlap by {shared:.3f} mm³")
    (folder / "pot-fit.json").write_text(
        json.dumps(
            dict(
                model=cfg["id"],
                installed="open body",
                slots=len(rows),
                frame_intersection_max_mm3=round(overlap, 5),
                pot_intersection_mm3=round(shared, 5),
                opening_height_mm=q["opening_height"],
                open_pot_height_mm=h,
                closed_height_mm=cfg["closed_height"],
            ),
            indent=2,
        )
        + "\n"
    )
    return [
        ([*frame, *display], (0.88, -2, 0.8)),
        ([*frame, *loaded], (0.34, -2, 0.52)),
        ([*frame, *loaded], (-0.34, 2, 0.52)),
        ([*frame, *loaded], (0.025, -2, 0.12)),
    ]
