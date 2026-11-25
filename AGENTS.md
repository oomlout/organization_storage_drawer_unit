# Drawer unit project guidance

The preferred online name is Martin McDoozle. Preserve actual paths and technical identifiers.

V8 includes three double-sided Systempak 209 frames, independent module joiners, a frame-to-plywood joint and the nine-frame cabinet. All four outer mounts use screw beams. The 3 mm plates replace the outside adapters and reuse the M3 x 20 beam screws. At each plywood side, use a single-beam plate at an outside corner and a two-beam plate at a tier seam. Their outer edges finish flush with the plywood.

Always generate in the order `working_oomp_populate` → `working_oomp` → `working_scad` using `python action_make_all.py`. The population source owns the container for every frame, the active grids and accessory compatibility. Edit the responsible source stage, then regenerate the output. Keep solids in `working_scad.py` and subtractive geometry in `working_scad_container_cutout.py`. Use OOBB primitives for fasteners. The shared interface and manufacturing dimensions are in `v8_profile.yaml`.

Run `python -m unittest discover -s tests` for catalogue regressions. Make-all runs actual-mesh fit and kit checks. Each part folder carries its `assembly.json`, `printing.txt`, `validation.json` and loose manufacturing files. Machine setup, build selection and printing instructions are in [BUILD.md](BUILD.md). Make-all generates the landing README and the illustrated guides in the canonical part folders. Edit their sources in [presentation](presentation) before rebuilding.

Keep former version code, releases, tests, prior generated parts and original design notes under [history](history/README.md). Active population, OOMP and SCAD select current V8 records explicitly. The archive is independent of manufacturing and must stay reproducible for historical comparisons.

Publish individual files in their part folders. Keep ZIP archives out of generation and Git.
