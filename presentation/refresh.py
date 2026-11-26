"""Refresh the OOBB guides from a complete set of previously exported meshes."""

import argparse
import json
import yaml
from pathlib import Path

import working_scad as cad
from working_oomp_populate import get_current_options, record_id
from . import catalogue, scenes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--render", action="store_true", help="Also rebuild the five studio views per part")
    parser.add_argument("--part", choices=[o["variant"] for o in get_current_options()])
    args = parser.parse_args()
    root = args.output_dir.resolve()
    records = get_current_options()
    for opt in records:
        role = opt["part_role"]
        if role in ("cabinet", "array"):
            if args.part == opt["variant"]:
                from v8_cabinet import rebuild
                rebuild(root, opt, records)
            continue
        if args.part and opt["variant"] != args.part:
            continue
        folder = root / "parts" / record_id(opt)
        saved = yaml.safe_load((folder / "working.yaml").read_text(encoding="utf-8"))
        if saved["oobb_details"] != opt:
            raise ValueError(
                f"{folder.name} has changed in population. Run make-all before refreshing its guide."
            )
        meta = json.loads((folder / "assembly.json").read_text(encoding="utf-8"))
        if opt["part_role"] == "accessory":
            from v8_beam_joints import build
            from .print_kit import generate, validate_slice
            build(folder,opt,{r["variant"]:r for r in records},True)
            generate(folder, opt)
            validate_slice(folder)
        else:
            scenes.render(folder, cad.frame_parameters(**opt), opt, meta, images=args.render)
    published = [r for r in records if (root / "parts" / record_id(r) / "README.md").is_file()]
    catalogue.write_index(root, published)


if __name__ == "__main__":
    main()
