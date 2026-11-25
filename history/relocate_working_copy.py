"""Refresh location fields in a writable copy of a historical parts catalogue."""
import argparse
import re
from pathlib import Path, PureWindowsPath

# The original OOMP records emitted these three plain YAML scalars. Limit the
# rewrite to them so comments, tags, line endings and other values survive.
LOCATION = re.compile(rb"(?m)^(?P<label>[ ]*(?:file_template|project_name|parts_directory):[ ]+)(?P<path>[A-Za-z]:[\\/][^\r\n]+)")


def relocate(project):
    project = Path(project).resolve(strict=True)
    archive = Path(__file__).resolve().parent
    if project.is_relative_to(archive):
        raise ValueError("Select a working copy outside the preserved archive")
    files = [f for tree in ("parts", "parts_source") for name in ("working.yaml", "thing.yaml", "*_working.yaml")
             for f in (project / tree).glob("*/" + name)]
    if not files:
        raise ValueError("Expected part records under parts or parts_source")

    def local_path(match):
        old = PureWindowsPath(match["path"].decode("utf-8"))
        if old.is_relative_to(PureWindowsPath(project)):
            return match[0]
        pieces = old.parts
        names = [part.lower() for part in pieces]
        if "organization_storage_drawer_unit" not in names:
            return match[0]
        field = match["label"].strip().split(b":")[0]
        if field == b"file_template":
            if "source_file" not in names:
                raise ValueError(f"Unrecognized historical template: {old}")
            suffix = pieces[names.index("source_file"):]
        else:
            # Earlier runs also produced records under temporary staging roots.
            suffix = ("parts",) if field == b"parts_directory" else ()
        new = project.joinpath(*suffix)
        if ".." in suffix or not new.exists():
            raise ValueError(f"Missing working-copy target: {new}")
        return match["label"] + str(new).encode("utf-8")

    updates = {}
    for file in files:
        original = file.read_bytes()
        local = LOCATION.sub(local_path, original)
        if local != original:
            updates[file] = local
    for file, content in updates.items():
        file.write_bytes(content)
    return len(updates)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", help="Working copy containing parts and source_file")
    print(f"Updated {relocate(parser.parse_args().project)} working-copy records")
