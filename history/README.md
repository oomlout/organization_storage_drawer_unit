# Drawer unit archive, V1–V7

This folder preserves the earlier source stages, generator entry points, manufactured files, release locks, test suites, previews and design notes. Relative paths used by the original historical tools are retained here. For ordinary production use the [V8 make-all instructions](../README.md).

| Location | Contents |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Original project history and instructions as they stood before migration |
| [parts](parts) and [parts_source](parts_source) | Final V7 parts and definitions, including the former 1×2 and 4×12 |
| [navigation_oobb](navigation_oobb) | Pre-migration catalogue navigation |
| [working_oomp_populate.py](working_oomp_populate.py) | Original historical part definitions |
| [releases](releases) and the versioned validation folders | Frozen releases, measurements, snapshots and fit reports |
| [parts_old_1_manifest.json](parts_old_1_manifest.json) | Original per-file checksums for the earlier archived catalogue, source and navigation |
| [v7_catalogue_sha256.json](v7_catalogue_sha256.json) | SHA-256 checksums for the 3,434 files in the pre-migration catalogue, source and navigation |

Run these commands **from this folder** to check the archive and run the historical geometry-source tests. To experiment with an older generator, work in a separate copy of the archive.

```powershell
python verify_v7_catalogue.py
python action_archive_parts_1.py
python -m unittest discover -s tests
```

## Using the archive after a move

The V7 validation preview SCADs carry the geometry from the matching revision inline. Open them directly in OpenSCAD. Their source comments identify the archived inputs.

Frozen OOMP records and run logs retain the locations recorded when they were created. To reuse an old record with a tool that reads its saved label template or parts directory, copy the desired part folders into `parts` in a separate working directory and copy `source_file` alongside it. Then run the following command using the script in this archive. It refreshes the three location fields in the working copy and checks that their destinations exist.

```powershell
python relocate_working_copy.py C:/path/to/working-copy
```
