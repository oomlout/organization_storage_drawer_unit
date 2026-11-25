"""Materialize only the current population allowlist, synchronously."""
from pathlib import Path

import oomp
import yaml
from working_oomp_populate import record_id, selected_options


def main(part=None, **kwargs):
    for option in selected_options(part):
        key = record_id(option)
        path = Path("parts_source") / key / "working.yaml"
        source = yaml.safe_load(path.read_text(encoding="utf-8"))
        if source["oobb_details"] != option or record_id(source) != key:
            raise ValueError(f"Stale part definition in {path}. Run population first.")
        oomp.add_parts([source], wait_for_completion=True)
        if not (Path("parts") / key / "working.yaml").is_file():
            raise RuntimeError(f"OOMP did not publish {key}")
