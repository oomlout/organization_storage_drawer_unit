"""Checks on exported split-frame meshes, not just their input dictionaries."""
import numpy as np
from shapely.geometry import Point, Polygon


def hardware_centres(p):
    start_x = -p["width_total"] / 2 + p["drawer_border_edge"]
    start_y = -p["height_total"] / 2 + p["drawer_border_edge"]
    points = []
    for row in range(p["row"]):
        y = start_y + row * p["pitch_y"] + p["depth_lip"] + p["hardware_axis_height"]
        for divider in range(p["column"] + 1):
            if divider == 0:
                x = start_x - (p["drawer_border_edge"] - p["inset_lip"]) / 2
            elif divider == p["column"]:
                x = start_x + (divider - 1) * p["pitch_x"] + p["opening_width"] + (p["drawer_border_edge"] - p["inset_lip"]) / 2
            else:
                x = start_x + divider * p["pitch_x"] - p["thickness_wall"] / 2
            points.append((x, y))
    return points


def check_hardware(mesh, p):
    if not p["split_frame"] or p["assembly_half"] in ["assembled", "print_layout"]:
        return {}
    sections = {}

    def solid(x, y, z):
        if z not in sections:
            section = mesh.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
            sections[z] = [] if section is None else [Polygon(loop[:, :2]) for loop in section.discrete]
        return sum(poly.contains(Point(x, y)) for poly in sections[z]) % 2 == 1

    checks = {"hardware_access_open": True, "hardware_seat_retained": True,
              "shaft_open": True, "interlock_profile_present": True}
    seam = p["body_depth"]
    front = p["assembly_half"] == "front"
    seat = seam - (p["screw_head_seat_offset"] if front else p["nut_seat_offset"])
    for x, y in hardware_centres(p):
        checks["hardware_access_open"] &= not solid(x + 2.5, y, seat - 1)
        checks["hardware_seat_retained"] &= solid(x + 2.5, y, seat + 1)
        checks["shaft_open"] &= not solid(x, y, seat + 1)
        if front:
            checks["shaft_open"] &= not solid(x, y, seam + 1)
            checks["interlock_profile_present"] &= solid(x + 3.8, y, seam + 1) and not solid(x + 4.15, y, seam + 1)
        else:
            checks["interlock_profile_present"] &= (
                not solid(x + 3.8, y, seam - 1)
                and solid(x + 4.6, y, seam - 1)
                and solid(x + 3.8, y, seam - p["interlock_depth"] - p["interlock_end_clearance"] - 0.2))
    return {key: bool(value) for key, value in checks.items()}


def check_print_faces(mesh, p):
    if p["split_frame"] and p["assembly_half"] in ["assembled", "print_layout"]:
        return {}, {"print_face_check": "Faces checked on the separate front/back files generated from the same source"}
    above_bed = mesh.triangles[:, :, 2].max(axis=1) > 0.05
    downward = above_bed & (mesh.face_normals[:, 2] < -0.708)
    allowed = np.zeros(len(mesh.faces), dtype=bool)
    if p["split_frame"]:
        seat = p["body_depth"] - (p["screw_head_seat_offset"] if p["assembly_half"] == "front" else p["nut_seat_offset"])
        for x, y in hardware_centres(p):
            in_bore = np.linalg.norm(mesh.triangles[:, :, :2] - [x, y], axis=2).max(axis=1) < 4.5
            near_seat = np.abs(mesh.triangles[:, :, 2] - seat).max(axis=1) < 1.0
            allowed |= in_bore & near_seat
    area = float(mesh.area_faces[downward & ~allowed].sum())
    bridge_area = float(mesh.area_faces[downward & allowed].sum())
    return {"no_unsupported_faces_outside_hardware_seats": area < 0.01}, {
        "unexpected_downward_area_mm2": area,
        "hardware_seat_bridge_area_mm2": bridge_area,
        "bridge_note": "Only localized socket-cap/nut seat bridges are allowed; inspect OOBB bridging in the slicer.",
    }


def check_corner_interlocks(mesh, p):
    if not p["split_frame"] or p["assembly_half"] in ["assembled", "print_layout"]:
        return {}

    def section_shape(z):
        section = mesh.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
        shape = Polygon()
        if section is not None:
            for loop in section.discrete:
                shape = shape.symmetric_difference(Polygon(loop[:, :2]))
        return shape

    seam = p["body_depth"]
    front = p["assembly_half"] == "front"
    base = section_shape(seam - p["interlock_depth"] - p["interlock_end_clearance"] - 0.2)
    joint = section_shape(seam + 1 if front else seam - 1)
    radius = p["corner_interlock_diameter"] / 2
    checks = {"all_corner_interlocks_present": True, "corner_socket_walls_retained": True}
    start_x = -p["width_total"] / 2 + p["drawer_border_edge"]
    start_y = -p["height_total"] / 2 + p["drawer_border_edge"]
    for column in range(p["column"] + 1):
        x = (-(p["width_total"] - p["drawer_border_edge"]) / 2 if column == 0 else
             (p["width_total"] - p["drawer_border_edge"]) / 2 if column == p["column"] else
             start_x + column * p["pitch_x"] - p["thickness_wall"] / 2)
        for row in range(p["row"] + 1):
            y = (-(p["height_total"] - p["drawer_border_edge"]) / 2 if row == 0 else
                 (p["height_total"] - p["drawer_border_edge"]) / 2 if row == p["row"] else
                 start_y + row * p["pitch_y"] - p["thickness_wall"])
            centre = Point(x, y)
            checks["all_corner_interlocks_present"] &= base.contains(centre)
            checks["all_corner_interlocks_present"] &= joint.contains(centre) == front
            if front:
                checks["all_corner_interlocks_present"] &= joint.contains(centre.buffer(radius - 0.03))
            else:
                socket_radius = radius + p["interlock_clearance"]
                checks["all_corner_interlocks_present"] &= joint.intersection(centre.buffer(socket_radius - 0.03)).area < 0.001
                ring = centre.buffer(socket_radius + p["corner_interlock_min_wall"] - 0.03).difference(centre.buffer(socket_radius + 0.03))
                checks["corner_socket_walls_retained"] &= ring.difference(joint).area < 0.001
    if front:
        checks["tongues_stay_inside_existing_contact_material"] = joint.difference(base).area < 0.001
        islands = list(base.geoms) if hasattr(base, "geoms") else [base]
        checks["every_mating_island_has_an_interlock"] = all(island.intersection(joint).area > 0.1 for island in islands)
    return {key: bool(value) for key, value in checks.items()}
