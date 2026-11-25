"""Check regenerated v1 against the release; optionally compare the v2 starting copy.

Run the normal pipeline first, then python action_check_version_1_lock.py.
Use --compare-version-2 only while checking the initial clone, before development.
"""
import argparse
import hashlib
import json
from pathlib import Path

import yaml


def main(compare_version_2=False):
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "releases/ai_version_1/manifest.json").read_text())
    results = []
    current = {p.parent.name for p in (root / "parts").glob("*ai_version_1_style*/working.yaml")}
    assert current == set(manifest["parts"]), "Version 1 release model set changed"
    for name, expected in manifest["parts"].items():
        folder = root / "parts" / name
        scad = (folder / "3dpr.scad").read_text()
        details = yaml.safe_load((folder / "working.yaml").read_text(encoding="utf-8"))["oobb_details"]
        checks = {
            "released_geometry_unchanged": hashlib.sha256(scad.encode()).hexdigest() == expected["scad_sha256"],
            "released_inputs_unchanged": details == expected["oobb_details"],
        }
        if compare_version_2:
            other = root / "parts" / name.replace("ai_version_1", "ai_version_2")
            checks["version_2_identical_scad"] = scad == (other / "3dpr.scad").read_text()
            other_details = yaml.safe_load((other / "working.yaml").read_text(encoding="utf-8"))["oobb_details"]
            normalized = json.loads(json.dumps(other_details).replace("ai_version_2", "ai_version_1"))
            checks["version_2_identical_inputs"] = details == normalized
        results.append({"id": name, "checks": checks})
    report = {"parts": results, "all_checks_passed": all(all(p["checks"].values()) for p in results)}
    (root / "releases/version_check.json").write_text(json.dumps(report, indent=2))
    print(f"Checked {len(results)} released models; all checks passed: {report['all_checks_passed']}")
    if not report["all_checks_passed"]:
        raise RuntimeError("Release check failed; see releases/version_check.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--compare-version-2", action="store_true")
    main(parser.parse_args().compare_version_2)
