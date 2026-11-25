"""Verify the pre-migration catalogue without modifying archived files."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
expected = json.loads((root / "v7_catalogue_sha256.json").read_text(encoding="utf-8"))
expected = {path: sha for path, sha in expected.items() if not path.lower().endswith(".zip")}
actual = {}
for subtree in ("parts", "parts_source", "navigation_oobb"):
    for file in (root / subtree).rglob("*"):
        if file.is_file():
            with file.open("rb") as stream:
                actual[file.relative_to(root).as_posix()] = hashlib.file_digest(stream, "sha256").hexdigest()
if actual != expected:
    changed = sorted(key for key in actual.keys() | expected.keys() if actual.get(key) != expected.get(key))
    raise SystemExit("Archive mismatch\n" + "\n".join(changed))
print(f"Verified {len(actual)} archived catalogue files")
