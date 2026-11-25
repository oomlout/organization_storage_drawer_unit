# Drawer unit project guidance

The preferred online name is Martin McDoozle. Preserve actual paths and technical identifiers.

The active manufacturing catalogue is V8. The three double-sided Systempak 209 100 ml frames are 1×1, 2×2 and 2×7 per face. The M3 × 25 joiner is a fourth catalogue part, with its own taxonomy, output folder and kit. Its supported hosts are 1×1 and 2×2.

Always generate in the order `working_oomp_populate` → `working_oomp` → `working_scad` using `python action_make_all.py`. The population source owns the container for every frame, the active grids and accessory compatibility. Edit the responsible source stage, then regenerate the output. Keep solids in `working_scad.py` and subtractive geometry in `working_scad_container_cutout.py`. Use OOBB primitives for fasteners. The shared interface and manufacturing dimensions are in `v8_profile.yaml`.

Run `python -m unittest discover -s tests` for catalogue regressions. Make-all runs actual-mesh fit and kit checks. Each part folder carries its `assembly.json`, `printing.txt`, `validation.json` and `print_files.zip`. Machine setup, build selection and printing instructions are in [README.md](README.md).

Keep former version code, releases, tests, prior generated parts and original design notes under [history](history/README.md). Active population, OOMP and SCAD select current V8 records explicitly. The archive is independent of manufacturing and must stay reproducible for historical comparisons.

The V8 joiner fronts are 8.4 mm deep. Both front styles bridge the installed clip caps. Nominal clearance above the caps is 0.8 mm (standard) or 1.1 mm (loose). Deeper head recesses retain the original M3 × 25 countersunk fixings and V8 backers.
