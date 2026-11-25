"""Regenerate and validate split frames, hardware seats and assembled interlocks."""
import json
from pathlib import Path
import shutil
import subprocess

import numpy as np
import trimesh
import yaml

import working
import working_scad
import scad_help
from action_check_version_1_lock import main as check_release
from action_validate_ai_version_1 import check_lip_sections
from validation_ai_version_2_checks import check_hardware, check_print_faces, check_corner_interlocks


def main():
    root = Path(__file__).resolve().parent
    if Path.cwd().resolve() != root:
        raise RuntimeError("Run from the project root")
    executable = shutil.which("openscad.com") or shutil.which("openscad")
    if not executable:
        raise RuntimeError("OpenSCAD is required")
    report_dir = root / "validation_ai_version_2"
    report_dir.mkdir(exist_ok=True)
    working.run(run_oomp_populate=True, run_oomp=True, run_scad=True,
                run_action=False, generate_stl=False)
    check_release()
    report = {"parts": [], "joint_pairs": [], "limitations": [
        "CAD checks do not establish physical fit, torque capacity, warping or successful slicing.",
        "OOBB hardware seats have small bridging regions; broad window roofs are eliminated.",
        "3dpr holds both halves flat; use front/back files for separate plates when the pair exceeds the bed.",
    ]}
    models = {}
    for path in sorted((root / "parts").glob("*ai_version_2_style*/working.yaml")):
        part = yaml.safe_load(path.read_text(encoding="utf-8"))
        folder = path.parent
        views = {"3dpr": part["oobb_details"].get("assembly_half", "print_layout")}
        if part.get("part_role") == "frame":
            views.update(front="front", back="back", assembled="assembled")
        for filename, view in views.items():
            print(f"Validating {folder.name}/{filename}", flush=True)
            result = subprocess.run([executable, "--backend=Manifold", "--hardwarnings",
                                     "--export-format=binstl", "-o", str(folder / f"{filename}.stl"), str(folder / f"{filename}.scad")],
                                    capture_output=True, text=True, timeout=600)
            (folder / f"validation_{filename}_openscad.log").write_text(result.stdout + result.stderr)
            result.check_returncode()
            view_part = dict(part, oobb_details=dict(part["oobb_details"], assembly_half=view))
            p = working_scad.get_ai_version_2_parameters(**view_part["oobb_details"])
            copies = 2 if p["part_role"] == "bank_layout" else 1
            design = working_scad.get_ai_version_2_summary(p, copies)
            mesh = trimesh.load_mesh(folder / f"{filename}.stl", process=True)
            checks = {
                "watertight": bool(mesh.is_watertight),
                "consistent_winding": bool(mesh.is_winding_consistent),
                "positive_volume": bool(mesh.volume > 0),
                # Assembled blind sockets enclose air around the pegs. Their
                # inward-wound shells have negative volume, not extra parts.
                "expected_connected_bodies": sum(1 for body in mesh.split(only_watertight=False) if body.volume > 0) == design["expected_bodies"],
                "expected_envelope": bool(np.allclose(mesh.extents, design["envelope_mm"], atol=0.03, rtol=0)),
                "on_print_bed": bool(abs(mesh.bounds[0, 2]) < 0.01),
                "individual_halves_fit_printer_volume" if p["split_frame"] and view == "print_layout" else "fits_printer_volume": bool(
                    (p["width_total"] if p["split_frame"] and view == "print_layout" else mesh.extents[0]) + 2 * p["bed_margin"] <= p["bed_width"] + 0.03
                    and (p["print_height_total"] if p["split_frame"] and view == "print_layout" else mesh.extents[1]) + 2 * p["bed_margin"] <= p["bed_height"] + 0.03
                    and mesh.extents[2] <= p.get("build_height", float("inf")) + 0.03),
            }
            checks.update(check_lip_sections(mesh, view_part))
            checks.update(check_hardware(mesh, p))
            checks.update(check_corner_interlocks(mesh, p))
            face_checks, face_info = check_print_faces(mesh, p)
            checks.update(face_checks)
            row = {"id": part["id"], "file": filename, "design": design, "volume_mm3": float(mesh.volume),
                   "mesh_envelope_mm": mesh.extents.tolist(), "checks": checks, **face_info}
            report["parts"].append(row)
            models[(folder.name, filename)] = (mesh, p)
            (folder / f"validation_{filename}.json").write_text(json.dumps(row, indent=2))
            if filename == "3dpr":
                (folder / "validation.json").write_text(json.dumps(row, indent=2))
            if filename == "3dpr":
                scene = folder / "preview_scene.scad"
                scene.write_text('include <3dpr.scad>;\n')
                dimension = max(mesh.extents)
                camera = f"{dimension*1.5},{-dimension*2},{dimension*1.5},0,0,{mesh.extents[2]/2}"
                result = subprocess.run([executable, "--backend=Manifold", "--render", "--imgsize=1200,900", "--projection=o", "--viewall",
                                         f"--camera={camera}", "--colorscheme=Tomorrow", "-o", str(folder / "preview.png"), str(scene)],
                                        capture_output=True, text=True, timeout=600)
                result.check_returncode()

    for (name, filename), (front, p) in models.items():
        if not p["split_frame"] or p["assembly_half"] != "front":
            continue
        back_name = name
        back = models[(name, "back")][0].copy()
        matrix = np.diag([-1., 1., -1., 1.])
        matrix[2, 3] = p["assembled_depth"]
        back.apply_transform(matrix)
        intersection = trimesh.boolean.intersection([front, back], engine="manifold")
        volume = abs(float(intersection.volume)) if not intersection.is_empty else 0.0
        layout = models[(name, "3dpr")][0]
        assembled = models[(name, "assembled")][0]
        paired_volume = front.volume + back.volume
        checks = {
            "no_assembly_interference": volume < 0.05,
            "print_layout_has_both_halves": abs(layout.volume - paired_volume) < 0.1,
            "assembled_has_both_halves": abs(assembled.volume - paired_volume) < 0.1,
            "print_layout_halves_on_bed": all(abs(body.bounds[0, 2]) < 0.01 for body in layout.split()),
        }
        moved = back.copy()
        moved.apply_translation([0.5, 0, 0])
        collision = trimesh.boolean.intersection([front, moved], engine="manifold")
        shifted_volume = abs(float(collision.volume)) if not collision.is_empty else 0.0
        checks["interlock_resists_lateral_sliding"] = shifted_volume > 0.1
        checks = {key: bool(value) for key, value in checks.items()}
        report["joint_pairs"].append({"front": name + "/front.stl", "back": back_name + "/back.stl",
                                      "interference_mm3": volume, "shifted_interference_mm3": shifted_volume,
                                      "checks": checks})
    report["all_checks_passed"] = all(all(row["checks"].values()) for row in report["parts"] + report["joint_pairs"])
    (report_dir / "report.json").write_text(json.dumps(report, indent=2))
    trial = "oobb_organization_storage_drawer_unit_1_column_1_row_rectangle_100_ml_tamper_evident_systempak_209_container_ai_version_2_style_joint_fit"
    scene = report_dir / "joint_pair.scad"
    scene.write_text(
        f'translate([-55,0,0]) {{ include <../parts/{trial}/front.scad>; }}\n'
        f'translate([55,0,0]) {{ include <../parts/{trial}/back.scad>; }}\n')
    result = subprocess.run([executable, "--backend=Manifold", "--render", "--imgsize=1400,800",
                             "--projection=o", "--viewall", "--camera=100,-170,170,0,0,4",
                             "--colorscheme=Tomorrow", "-o", str(report_dir / "joint_pair.png"), str(scene)],
                            capture_output=True, text=True, timeout=600)
    result.check_returncode()
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print(json.dumps({"parts_checked": len(report["parts"]), "joint_pairs_checked": len(report["joint_pairs"]),
                      "all_checks_passed": report["all_checks_passed"]}, indent=2))
    if not report["all_checks_passed"]:
        raise RuntimeError("Split-frame validation failed; see validation_ai_version_2/report.json")


if __name__ == "__main__":
    main()
