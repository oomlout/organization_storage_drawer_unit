"""Archive retired clearance-fit records from all active catalogue trees.

This is reversible housekeeping, not a geometry generator. Run the normal
populate -> OOMP -> SCAD pipeline afterwards. Re-running this migration is safe.
"""
import json
from pathlib import Path
import shutil

import yaml
from release_retirements import RETIRED_CLEARANCE_VARIANTS


def main():
    root = Path(__file__).resolve().parent
    archive = (root / "retired_clearance_part_records").resolve()
    if not archive.is_relative_to(root):
        raise RuntimeError("Archive must remain in the project")
    moves = []
    for path in sorted((root / "parts").glob("*ai_version_*_style*/working.yaml")):
        part = yaml.safe_load(path.read_text(encoding="utf-8"))
        if part.get("style") not in ["ai_version_1", "ai_version_2", "ai_version_3"] or part.get("part_role") != "fit" or part.get("variant") not in RETIRED_CLEARANCE_VARIANTS:
            continue
        name = path.parent.name
        if not name.endswith("_" + part["variant"]):
            raise RuntimeError(f"Unexpected clearance-fit identity: {name}")
        navigation = root / "navigation_oobb"
        for level in range(1, 16):
            value = part.get(f"taxonomy_{level}")
            if value:
                navigation /= str(value).replace(".", "d")
        for source in [path.parent, root / "parts_source" / name, navigation]:
            source = source.resolve()
            if not source.exists():
                continue
            if not source.is_relative_to(root) or source == root:
                raise RuntimeError(f"Refusing move outside the project: {source}")
            category = source.relative_to(root).parts[0]
            destination = (archive / name / category).resolve()
            if not destination.is_relative_to(archive) or destination.exists():
                raise RuntimeError(f"Refusing overwrite or unexpected archive path: {destination}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            moves.append({"from": str(source), "to": str(destination)})
    if moves:
        archive.mkdir(exist_ok=True)
        (archive / "migration.json").write_text(json.dumps(moves, indent=2), encoding="utf-8")
    print(f"Archived {len(moves)} retired clearance-fit directories; originals remain recoverable.")


if __name__ == "__main__":
    main()
