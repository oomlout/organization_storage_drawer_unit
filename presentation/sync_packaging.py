"""Import a reproducible snapshot of one generated OOMP reference for offline builds."""

import argparse
import json
import os
import shutil
from pathlib import Path

MODELS = Path(__file__).with_name("packaging")


def model_folder(container):
    """Use a neighbouring built packaging catalogue, or the portable project snapshot."""
    explicit = os.environ.get("OOMP_PACKAGING_ROOT")
    packaging = Path(explicit) if explicit else MODELS.parents[2] / "oomp_packaging"
    external = packaging / "parts" / container
    if (external / "model.json").is_file():
        return external
    return MODELS / container


def sync(folder):
    data = json.loads((folder / "model.json").read_text(encoding="utf-8"))
    if data["id"] != folder.name or data["units"] != "mm":
        raise ValueError("The model manifest must match its OOMP part folder and use millimetres")
    dest = MODELS / folder.name
    files = [folder / name for name in ("model.json", "body.stl", "lid.stl")]
    for file in files:
        if not file.is_file():
            raise FileNotFoundError(file)
    dest.mkdir(parents=True, exist_ok=True)
    for file in files:
        shutil.copyfile(file, dest / file.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("part_folder", type=Path)
    sync(parser.parse_args().part_folder.resolve())
