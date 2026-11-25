"""Check all released v2 inputs/views; optionally compare the initial v3 clone.

Run the full pipeline first. --compare-version-3 is for the starting copy only,
not a permanent requirement for version 3 development.
"""
import argparse
import hashlib
import json
from pathlib import Path

import yaml
from catalogue_archive import historical_parts
from release_retirements import active_release_parts


def main(compare_version_3=False):
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "releases/ai_version_2/manifest.json").read_text(encoding="utf-8"))
    active, retired = active_release_parts(manifest["parts"])
    current = {p.parent.name for p in (historical_parts(root)).glob("*ai_version_2_style*/working.yaml")}
    assert current == set(active), "Version 2 active release model set changed"
    if compare_version_3:
        copied = {p.parent.name.replace("ai_version_3", "ai_version_2") for p in (historical_parts(root)).glob("*ai_version_3_style*/working.yaml")}
        assert copied == current, "Version 3 starting model set differs"
    results = []
    for name, expected in active.items():
        folder = historical_parts(root) / name
        details = yaml.safe_load((folder / "working.yaml").read_text(encoding="utf-8"))["oobb_details"]
        checks = {"released_inputs_unchanged": details == expected["oobb_details"]}
        for filename, digest in expected["scad_sha256"].items():
            scad = (folder / filename).read_text(encoding="utf-8")
            checks[f"released_{filename}_unchanged"] = hashlib.sha256(scad.encode()).hexdigest() == digest
            if compare_version_3:
                other = historical_parts(root) / name.replace("ai_version_2", "ai_version_3")
                checks[f"version_3_identical_{filename}"] = scad == (other / filename).read_text(encoding="utf-8")
        if compare_version_3:
            other_details = yaml.safe_load((other / "working.yaml").read_text(encoding="utf-8"))["oobb_details"]
            normalized = json.loads(json.dumps(other_details).replace("ai_version_3", "ai_version_2"))
            checks["version_3_identical_inputs"] = details == normalized
        results.append({"id": name, "checks": checks})
    report = {"parts": results, "retired_clearance_variants": retired, "all_checks_passed": all(all(p["checks"].values()) for p in results)}
    filename = "version_2_to_3_copy_check.json" if compare_version_3 else "version_2_check.json"
    (root / "releases" / filename).write_text(json.dumps(report, indent=2), encoding="utf-8")
    views = sum(len(p["scad_sha256"]) for p in active.values())
    print(f"Checked {len(results)} released models / {views} CAD views; all checks passed: {report['all_checks_passed']}")
    if not report["all_checks_passed"]:
        raise RuntimeError(f"Release/copy check failed; see releases/{filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--compare-version-3", action="store_true")
    main(parser.parse_args().compare_version_3)
