"""Regenerate through the project pipeline, export AI trials, and check their meshes.

Run from the project root: python action_validate_ai_version_1.py
Requires the existing OOMP/OOBB environment, OpenSCAD, numpy, trimesh, Shapely and PyYAML.
This checks geometry, not real material shrinkage, container fit or load capacity.
"""
import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import trimesh
import yaml
from shapely.geometry import Point, Polygon

import working
import scad_help
import working_scad


def check_lip_sections(mesh, part):
    """Inspect the exported mesh, including shelf roots and the former centre rail."""
    p = getattr(working_scad, f"get_{part['style']}_parameters")(**part["oobb_details"])
    has_reliefs = p["part_role"] == "frame" and p["lightening"]
    z_samples = [20, 55, 90] if p["part_role"] == "frame" else [p["depth_total"] / 2]
    # Include end bands: the old excess shoulders persisted there even where
    # relief windows removed them at intermediate insertion depths.
    shoulder_end_samples = [2, p["depth_total"] - 2] if p["body_extension_height"] > 0 else []
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
                            for dy in [0.2, p["lip_shelf_thickness"] - 0.2]:
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


def main(style="ai_version_1"):
    root = Path(__file__).resolve().parent
    if Path.cwd().resolve() != root:
        raise RuntimeError("Run this script from the project root")
    executable = shutil.which("openscad.com") or shutil.which("openscad")
    if not executable:
        raise RuntimeError("OpenSCAD must be on PATH")
    report_dir = root / f"validation_{style}"
    report_dir.mkdir(exist_ok=True)
    # Never bypass population or OOMP enrichment when rebuilding trials.
    working.run(run_oomp_populate=True, run_oomp=True, run_scad=True,
                run_action=False, generate_stl=False)

    report = {"parts": [], "limitations": [
        "Mesh checks do not establish load capacity, physical fit or freedom from warping.",
        "Overhang check tests exposed face angles in the supplied print orientation; verify in the slicer.",
        "No calibrated filament shrinkage or printer-specific slicing profile is assumed.",
    ]}
    for folder in sorted((root / "parts").iterdir()):
        yaml_path = folder / "working.yaml"
        if not yaml_path.exists():
            continue
        part = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        if part.get("style") != style:
            continue
        print(f"Validating {folder.name}", flush=True)
        scad_file = folder / "3dpr.scad"
        stl_file = folder / "3dpr.stl"
        result = subprocess.run([executable, "--backend=Manifold", "--hardwarnings",
                                 "--export-format=binstl", "-o", str(stl_file), str(scad_file)],
                                capture_output=True, text=True, timeout=600)
        (folder / "validation_openscad.log").write_text(result.stdout + result.stderr, encoding="utf-8")
        if result.returncode != 0:
            raise RuntimeError(f"OpenSCAD failed for {folder.name}: {result.stderr}")
        thing = yaml.safe_load((folder / "thing.yaml").read_text(encoding="utf-8"))["thing"]
        design = thing["ai_design"]
        mesh = trimesh.load_mesh(stl_file, process=True)
        bodies = len(mesh.split(only_watertight=False))
        # Undersides above the bed must slope >=45 degrees from horizontal.
        # A small tolerance admits tessellation/float noise at exactly 45 degrees.
        above_bed = mesh.triangles[:, :, 2].max(axis=1) > 0.05
        unsupported = above_bed & (mesh.face_normals[:, 2] < -0.708)
        unsupported_area = float(mesh.area_faces[unsupported].sum())
        checks = {
            "watertight": bool(mesh.is_watertight),
            "consistent_winding": bool(mesh.is_winding_consistent),
            "positive_volume": bool(mesh.volume > 0),
            "expected_connected_bodies": bodies == design["expected_bodies"],
            "expected_envelope": bool(np.allclose(mesh.extents, design["envelope_mm"], atol=0.03, rtol=0)),
            "on_print_bed": bool(abs(mesh.bounds[0, 2]) < 0.01),
            "no_steep_downward_faces_above_bed": unsupported_area < 0.01,
            "fits_printer_volume": bool(
                mesh.extents[0] + 2 * design["bed_margin_mm"] <= design["build_volume_mm"][0] + 0.03
                and mesh.extents[1] + 2 * design["bed_margin_mm"] <= design["build_volume_mm"][1] + 0.03
                and (design["build_volume_mm"][2] is None
                     or mesh.extents[2] <= design["build_volume_mm"][2] + 0.03)),
        }
        checks.update(check_lip_sections(mesh, part))
        row = {"id": part["id"], "variant": part.get("variant", "frame"),
               "column": part["column"], "row": part["row"],
               "design": design, "mesh_envelope_mm": mesh.extents.tolist(),
               "volume_mm3": float(mesh.volume), "surface_area_mm2": float(mesh.area),
               "connected_bodies": bodies, "steep_downward_area_mm2": unsupported_area,
               "checks": checks}
        report["parts"].append(row)
        (folder / "validation.json").write_text(json.dumps(row, indent=2), encoding="utf-8")

        # Render the actual CSG result, including relief windows, not a concept sketch.
        if part.get("variant", "frame") in ["frame", "bank_layout", "a1_mini_max", "p1p_max"]:
            dimension = max(design["envelope_mm"])
            # Stand the drawer bank upright for presentation only. 3dpr.stl
            # retains its face-down print orientation and bed-zero placement.
            preview_scene = folder / "preview_scene.scad"
            preview_scene.write_text('rotate([90, 0, 0]) {\n    include <3dpr.scad>;\n}\n', encoding="utf-8")
            camera = f"{dimension * 1.5},{dimension * 2.0},{dimension * 1.2},0,{-design['envelope_mm'][2] / 2},0"
            render = subprocess.run([executable, "--backend=Manifold", "--hardwarnings", "--render",
                                     "--imgsize=1400,1000", "--projection=o", "--viewall",
                                     f"--camera={camera}", "--colorscheme=Tomorrow",
                                     "-o", str(folder / "preview.png"), str(preview_scene)],
                                    capture_output=True, text=True, timeout=600)
            if render.returncode != 0:
                raise RuntimeError(f"Preview failed for {folder.name}: {render.stderr}")

    reference = next(p for p in report["parts"] if p["variant"] == "solid_reference")
    relieved = next(p for p in report["parts"] if p["variant"] == "frame" and p["column"] == 2 and p["row"] == 2)
    report["same_envelope_material_saving_percent"] = 100 * (1 - relieved["volume_mm3"] / reference["volume_mm3"])
    report["all_checks_passed"] = all(all(p["checks"].values()) for p in report["parts"])
    (report_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    # Keep taxonomy navigation copies consistent with the newly exported files.
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print(json.dumps({"parts_checked": len(report["parts"]),
                      "all_checks_passed": report["all_checks_passed"],
                      "same_envelope_material_saving_percent": report["same_envelope_material_saving_percent"]}, indent=2))
    if not report["all_checks_passed"]:
        raise RuntimeError(f"Mesh validation failed; see validation_{style}/report.json")
    # Both version validators regenerate the complete catalogue. Guard the
    # released version even when only version 2 meshes are being exported.
    if (root / "releases/ai_version_1/manifest.json").exists():
        from action_check_version_1_lock import main as check_release
        check_release()


if __name__ == "__main__":
    main()
