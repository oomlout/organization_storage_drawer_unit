"""Protect the completed version 3 while developing modular version 4."""
import argparse
import hashlib
import json
from pathlib import Path

import yaml
from catalogue_archive import historical_parts
from release_retirements import active_release_parts


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "releases/ai_version_3/manifest.json").read_text(encoding="utf-8"))
    active, retired = active_release_parts(manifest["parts"])
    current = {p.parent.name for p in (historical_parts(root)).glob("*ai_version_3_style*/working.yaml")}
    assert current == set(active), "Version 3 active release model set changed"
    results = []
    for name, expected in active.items():
        folder = historical_parts(root) / name
        details = yaml.safe_load((folder / "working.yaml").read_text(encoding="utf-8"))["oobb_details"]
        checks = {"released_inputs_unchanged": details == expected["oobb_details"]}
        for filename, digest in expected["scad_sha256"].items():
            scad = (folder / filename).read_text(encoding="utf-8")
            checks[f"released_{filename}_unchanged"] = hashlib.sha256(scad.encode()).hexdigest() == digest
        results.append({"id": name, "checks": checks})
    report = {"parts": results, "retired_clearance_variants": retired, "all_checks_passed": all(all(p["checks"].values()) for p in results)}
    filename = "version_3_check.json"
    (root / "releases" / filename).write_text(json.dumps(report, indent=2), encoding="utf-8")
    views = sum(len(p["scad_sha256"]) for p in active.values())
    print(f"Checked {len(results)} released models / {views} CAD views; all checks passed: {report['all_checks_passed']}")
    if not report["all_checks_passed"]:
        raise RuntimeError(f"Release/copy check failed; see releases/{filename}")


if __name__ == "__main__":
    main()
