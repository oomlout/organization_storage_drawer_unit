"""Checks on exported split-frame meshes, not just their input dictionaries."""
import numpy as np
import oobb
import working_scad
from shapely.geometry import Point, Polygon, box


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


def check_tapered_rails(mesh, p):
    if not p["shelf_relief_active"] or p["assembly_half"] in ["assembled", "print_layout"]:
        return {}
    checks = {"thin_running_rail_retained": True, "rail_material_removed": True,
              "sloped_boss_profile_present": True, "full_joint_boss_retained": True}
    samples = [(p["relief_start_depth"] + p["boss_taper_start"]) / 2,
               (p["boss_taper_start"] + p["boss_taper_end"]) / 2,
               p["body_depth"] - p["interlock_depth"] - p["interlock_end_clearance"] - 0.3]
    for index, z in enumerate(samples):
        section = mesh.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
        shape = Polygon()
        if section is not None:
            for loop in section.discrete:
                shape = shape.symmetric_difference(Polygon(loop[:, :2]))
        thickness = min(p["lip_shelf_thickness"], p["running_shelf_thickness"] + max(0, z - p["boss_taper_start"]) / p["hardware_boss_slope"])
        for x, y in hardware_centres(p):
            for sign in [-1, 1]:
                # Beside the unchanged axial head/nut access passages.
                sx = x + sign * (p["interlock_width"] / 2 + 0.6)
                below = shape.contains(Point(sx, y - p["hardware_axis_height"] + thickness - 0.2))
                above = shape.contains(Point(sx, y - p["hardware_axis_height"] + thickness + 0.2))
                if index == 0:
                    checks["thin_running_rail_retained"] &= below
                    checks["rail_material_removed"] &= not above
                elif index == 1:
                    checks["sloped_boss_profile_present"] &= below and not above
                else:
                    checks["full_joint_boss_retained"] &= below
    return {key: bool(value) for key, value in checks.items()}


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
    if p["internal_lower_supports_removed"]:
        checks["internal_lower_supports_and_pegs_removed"] = True
        checks["outer_face_grid_retained"] = True
        face = section_shape(0.1)
        middle = section_shape((p["relief_start_depth"] + seam) / 2)
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
            if row not in p["corner_interlock_rows"]:
                checks["internal_lower_supports_and_pegs_removed"] &= not any(s.contains(centre) for s in [base, joint, middle])
                checks["outer_face_grid_retained"] &= face.contains(centre)
                continue
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
        # Ignore zero-area linework from polygon section Boolean operations.
        islands = [g for g in (list(base.geoms) if hasattr(base, "geoms") else [base]) if g.area > 0.001]
        checks["every_mating_island_has_an_interlock"] = all(island.intersection(joint).area > 0.1 for island in islands)
        if p["lightening"]:
            checks["expected_mating_connection_count"] = len(islands) == (p["column"] + 1) * (p["row"] + len(p["corner_interlock_rows"]))
    if p["internal_lower_supports_removed"]:
        for row in range(1, p["row"]):
            lower = start_y + row * p["pitch_y"] - p["thickness_wall"] - p["side_rail_width"]
            removed = box(-p["width_total"], lower + 0.03, p["width_total"],
                          lower + p["thickness_wall"] + 2 * p["side_rail_width"] - 0.03)
            checks["internal_lower_supports_and_pegs_removed"] &= all(s.intersection(removed).area < 0.001 for s in [base, joint, middle])
    return {key: bool(value) for key, value in checks.items()}


def check_lip_sections(mesh, part):
    """Inspect the exported mesh, including shelf roots and the former centre rail."""
    p = getattr(working_scad, f"get_{part['style']}_parameters")(**part["oobb_details"])
    if p.get("split_frame") and p["assembly_half"] in ["assembled", "print_layout"]:
        # Both printable halves receive these section checks individually.
        return {}
    has_reliefs = p["part_role"] == "frame" and p["lightening"]
    z_samples = [20, 55, 90] if p["part_role"] == "frame" else [p["depth_total"] / 2]
    if p.get("split_frame"):
        z_samples = [p["body_depth"] * fraction for fraction in [0.25, 0.5, 0.7]]
    # Include end bands: the old excess shoulders persisted there even where
    # relief windows removed them at intermediate insertion depths.
    shoulder_end_samples = [2, p["depth_total"] - 2] if p["body_extension_height"] > 0 else []
    if p.get("split_frame") and shoulder_end_samples:
        # The outer face retains its band; split-frame reliefs deliberately
        # open at the mating plane, so there is no inner end band to retain.
        shoulder_end_samples = [2]
    module_offsets = [0]
    if p["part_role"] == "bank_layout":
        pitch = p["width_total"] + p["module_gap"]
        module_offsets = [-pitch / 2, pitch / 2]
    checks = {"lip_shelf_and_root_present": True, "lip_bearing_face_clear_below": True}
    if p["body_extension_height"] > 0:
        checks["shoulders_limited_to_reference_height"] = True
        checks["thin_side_walls_retained_at_end_bands"] = True
    if has_reliefs:
        checks["side_reliefs_open_above_and_below_shelf"] = True
        if p["middle_rib_width"] == 0:
            checks["centre_support_removed"] = True
    for z in sorted(set(z_samples + shoulder_end_samples)):
        section = mesh.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
        if section is None:
            return {key: False for key in checks}
        loops = [Polygon(loop[:, :2]) for loop in section.discrete]

        def solid(x, y):
            # Even/odd containment handles both cavities and disconnected modules.
            point = Point(x, y)
            return sum(polygon.contains(point) for polygon in loops) % 2 == 1

        for shift in module_offsets:
            for row in range(p["row"]):
                cy = -p["height_total"] / 2 + p["drawer_border_edge"] + p["opening_height"] / 2 + row * p["pitch_y"]
                for column in range(p["column"]):
                    cx = shift - p["width_total"] / 2 + p["drawer_border_edge"] + p["opening_width"] / 2 + column * p["pitch_x"]
                    for sign in [-1, 1]:
                        inset_x = cx + sign * (p["opening_width"] / 2 - p["inset_lip"] / 2)
                        outside = (sign == -1 and column == 0) or (sign == 1 and column == p["column"] - 1)
                        wall = p["drawer_border_edge"] if outside else p["thickness_wall"]
                        root_x = cx + sign * (p["opening_width"] / 2 + wall / 2)
                        if p["body_extension_height"] > 0:
                            for y in [p["lip_support_end_y"] + 0.2,
                                      p["lip_support_end_y"] + p["body_extension_height"] / 2,
                                      p["opening_height"] / 2 - p["opening_radius"] - 0.2]:
                                checks["shoulders_limited_to_reference_height"] &= not solid(inset_x, cy + y)
                                if z in shoulder_end_samples:
                                    checks["thin_side_walls_retained_at_end_bands"] &= solid(root_x, cy + y)
                        for x in [inset_x, root_x]:
                            # The access bores already cross the shelf. Check the
                            # continuous material beneath their lowest edge.
                            thickness = p["lip_shelf_thickness"]
                            if p["shelf_relief_active"] and z >= p["relief_start_depth"]:
                                thickness = min(thickness, p["running_shelf_thickness"] + max(0, z - p["boss_taper_start"]) / p["hardware_boss_slope"])
                                thickness = min(thickness, p["hardware_axis_height"] - max(oobb.gv("nut_radius_m3", "3dpr"), oobb.gv("screw_socket_cap_radius_m3", "3dpr")))
                            for dy in [0.2, thickness - 0.2]:
                                checks["lip_shelf_and_root_present"] &= solid(x, cy + p["lip_step_y"] + dy)
                        checks["lip_bearing_face_clear_below"] &= not solid(inset_x, cy + p["lip_step_y"] - 0.2)
                        if has_reliefs and z in z_samples:
                            lower_y = cy + (-p["opening_height"] / 2 + p["side_rail_width"] + p["lip_step_y"] - p["lip_cutout_radius"]) / 2
                            upper_y = cy + (p["lip_step_y"] + p["lip_shelf_thickness"] + p["opening_height"] / 2 - p["side_rail_width"]) / 2
                            checks["side_reliefs_open_above_and_below_shelf"] &= not solid(root_x, lower_y) and not solid(inset_x, upper_y)
                    if has_reliefs and z in z_samples and p["middle_rib_width"] == 0:
                        thickness = p["drawer_border_edge"] if row == 0 else p["thickness_wall"]
                        floor_y = cy - p["opening_height"] / 2 - thickness / 2
                        checks["centre_support_removed"] &= not solid(cx, floor_y)
    return {key: bool(value) for key, value in checks.items()}

