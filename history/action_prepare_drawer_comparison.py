"""Rebuild the source pipeline, measure current CAD, render PNGs, then repopulate costs.

Run from the project root. Unchanged CAD is cached by source/parameter fingerprint.
"""
import json
import shutil
import subprocess
from pathlib import Path

import trimesh
import yaml

import working
import working_scad
from working_oomp_populate_comparison import geometry_fingerprint


def main(scad_filter="", skip_initial_generation=False):
    root = Path(__file__).resolve().parent
    if Path.cwd().resolve() != root:
        raise RuntimeError("Run from the project root")
    executable = shutil.which("openscad.com") or shutil.which("openscad")
    if not executable:
        raise RuntimeError("OpenSCAD is required")
    output = root / "drawer_comparison"
    output.mkdir(exist_ok=True)
    cache_path = output / "cad_measurements.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    if not skip_initial_generation:
        working.run(run_oomp_populate=True, run_oomp=True, run_scad=True, run_action=False, generate_stl=False, scad_filter=scad_filter)
    for path in sorted((root / "parts").glob("oobb*/working.yaml")):
        part = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not part.get("oobb_details"):
            continue
        folder = path.parent
        fingerprint = geometry_fingerprint(part)
        if cache.get(folder.name, {}).get("fingerprint") == fingerprint and (folder / "comparison.png").exists():
            continue
        print("Measuring/rendering", folder.name, flush=True)
        cad_filename = "assembled.scad" if part["style"] in ["ai_version_2", "ai_version_3"] and part.get("part_role") == "frame" else "3dpr.scad"
        if part["style"] in ["ai_version_4", "ai_version_5", "ai_version_6"] and part.get("part_role") in ["frame", "modular_test"]:
            cad_filename = "assembled.scad"
        result = subprocess.run([executable, "--backend=Manifold", "-o", str(folder / "comparison.stl"), str(folder / cad_filename)], capture_output=True, text=True, timeout=600)
        (folder / "comparison_export.log").write_text(result.stdout + result.stderr, encoding="utf-8")
        result.check_returncode()
        mesh = trimesh.load(folder / "comparison.stl", force="mesh")
        if not mesh.is_watertight or mesh.volume <= 0:
            raise RuntimeError(f"Invalid volume: {folder.name}")
        envelope = mesh.extents.tolist()
        if part["style"] in ["ai_version_1", "ai_version_2", "ai_version_3"]:
            inputs = dict(part["oobb_details"])
            if cad_filename == "assembled.scad":
                inputs["assembly_half"] = "assembled"
            parameters = getattr(working_scad, f"get_{part['style']}_parameters")(**inputs)
            copies = 2 if parameters["part_role"] == "bank_layout" else 1
            envelope = getattr(working_scad, f"get_{part['style']}_summary")(parameters, copies)["finished_envelope_mm"]
        if part["style"] == "ai_version_4":
            parameters = working_scad.get_ai_version_4_parameters(**part["oobb_details"])
            envelope = [parameters["plate_width"], parameters["plate_height"],
                        parameters["plate_print_depth"] if part.get("part_role") == "face_fit" else parameters["assembled_depth"]]
        if part["style"] == "ai_version_6":
            parameters = working_scad.get_ai_version_6_parameters(**part["oobb_details"])
            envelope = [parameters["width_total"], parameters["height_total"],
                        parameters["assembled_depth"]+2*parameters.get('screw_rail',{}).get('flange_size',[0,0,0])[2]]
        if part["style"] == "ai_version_5" and part.get("part_role") == "frame":
            parameters = working_scad.get_ai_version_5_parameters(**part["oobb_details"])
            envelope = [parameters["width_total"],parameters["height_total"],parameters["assembled_depth"]]
        scene = folder / "comparison_scene.scad"
        scene.write_text(f'rotate([90, 0, 0]) {{\n include <{cad_filename}>;\n}}\n')
        dimension = max(mesh.extents)
        camera = f"{dimension*1.5},{dimension*2},{dimension*1.2},0,{-envelope[2]/2},0"
        result = subprocess.run([executable, "--backend=Manifold", "--render", "--imgsize=1000,750", "--projection=o", "--viewall", f"--camera={camera}", "--colorscheme=Tomorrow", "-o", str(folder / "comparison.png"), str(scene)], capture_output=True, text=True, timeout=600)
        (folder / "comparison_render.log").write_text(result.stdout + result.stderr, encoding="utf-8")
        result.check_returncode()
        cache[folder.name] = {
            "fingerprint": fingerprint,
            "volume_mm3": float(mesh.volume),
            "finished_envelope_mm": [round(float(value), 3) for value in envelope],
        }
        cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")
    # Costs flow through population, enrichment and SCAD, not patched YAML.
    working.run(run_oomp_populate=True, run_oomp=True, run_scad=True, run_action=False, generate_stl=False, scad_filter=scad_filter)
    print("Comparison assets and costs refreshed", flush=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--scad-filter", default="", help="Redraw only this style; still populate/enrich all and measure every stale CAD record.")
    parser.add_argument("--skip-initial-generation", action="store_true",
                        help="Measure already regenerated CAD; still finish with populate -> OOMP -> SCAD for costs.")
    args = parser.parse_args()
    main(args.scad_filter, args.skip_initial_generation)
