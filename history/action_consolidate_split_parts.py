"""Archive obsolete separate-half catalogue records before rebuilding main folders.

This is reversible housekeeping, not a geometry generator. Run the normal
populate -> OOMP -> SCAD pipeline afterwards. Re-running this migration is safe.
"""
import json
from pathlib import Path
import shutil

import yaml


def main():
    root = Path(__file__).resolve().parent
    archive = (root / "retired_split_part_records").resolve()
    if not archive.is_relative_to(root):
        raise RuntimeError("Archive must remain in the project")
    moves = []
    for path in sorted((root / "parts").glob("*ai_version_2_style*/working.yaml")):
        part = yaml.safe_load(path.read_text(encoding="utf-8"))
        if part.get("style") != "ai_version_2" or part.get("assembly_half") not in ["front", "back"]:
            continue
        name = path.parent.name
        if not name.endswith("_" + part["assembly_half"]):
            raise RuntimeError(f"Unexpected half identity: {name}")
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
    print(f"Archived {len(moves)} obsolete half-record directories; originals remain recoverable.")


if __name__ == "__main__":
    main()
