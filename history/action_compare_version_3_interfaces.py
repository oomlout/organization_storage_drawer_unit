"""Compare current v3 mesh interfaces with the frozen v2 mating geometry.

Run action_validate_ai_version_3.py first. This reads exported meshes; it does
not generate or edit CAD and does not require v3's running rails to match v2.
"""
import json
from pathlib import Path

import trimesh
import yaml
from shapely.geometry import Polygon, box

import working_scad


def section_shape(mesh, z):
    section = mesh.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
    shape = Polygon()
    if section is not None:
        for loop in section.discrete:
            shape = shape.symmetric_difference(Polygon(loop[:, :2]))
    return shape


def main():
    root = Path(__file__).resolve().parent
    rows = []
    for path in sorted((root / "parts").glob("*ai_version_3_style*/working.yaml")):
        part = yaml.safe_load(path.read_text(encoding="utf-8"))
        if part.get("part_role") != "frame":
            continue
        original = root / "releases/ai_version_2/parts" / path.parent.name.replace("ai_version_3", "ai_version_2")
        for half in ["front", "back"]:
            p = working_scad.get_ai_version_3_parameters(**dict(part["oobb_details"], assembly_half=half))
            current_mesh = trimesh.load_mesh(path.parent / f"{half}.stl")
            original_mesh = trimesh.load_mesh(original / f"{half}.stl")
            samples = []
            for z in [2] + [p["body_depth"] + offset for offset in [-10.5, -4, -1] + ([1] if half == "front" else [])]:
                expected = section_shape(original_mesh, z)
                # The only permitted interface change is the explicitly requested
                # removal of internal lower rails and their locating pegs.
                if p["internal_lower_supports_removed"] and z >= p["relief_start_depth"]:
                    start_y = -p["height_total"] / 2 + p["drawer_border_edge"]
                    for row in range(1, p["row"]):
                        lower = start_y + row * p["pitch_y"] - p["thickness_wall"] - p["side_rail_width"]
                        expected = expected.difference(box(-p["width_total"], lower - 0.1, p["width_total"],
                                                           lower + p["thickness_wall"] + 2 * p["side_rail_width"] + 0.1))
                area = section_shape(current_mesh, z).symmetric_difference(expected).area
                samples.append({"z_mm": z, "difference_mm2": area, "matches": area < 0.01})
            rows.append({"id": part["id"], "half": half, "sections": samples})
    report = {"permitted_change": "Internal lower rails and their pegs removed; retained interfaces and outer face unchanged",
              "halves": rows, "all_checks_passed": all(s["matches"] for row in rows for s in row["sections"])}
    (root / "validation_ai_version_3/interface_comparison.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Checked {len(rows)} half interfaces against frozen v2: {report['all_checks_passed']}")
    if not report["all_checks_passed"]:
        raise RuntimeError("Version 3 mating interface changed")


if __name__ == "__main__":
    main()
