# Version 5 tiled PETG demonstrations

The user authorized full v5 demonstrations after the connector trials, confirmed
**finished outside dimensions** of 767 × 300 and 362 × 300 mm, and selected the
100 ml Systempak 209 trays. These demonstrations are experimental.

| Finished plate | Tray grid | Tiles per face | Screw rails | Snap rails | M3 × 16 countersunk screws / M3 nuts |
|---|---:|---:|---:|---:|---:|
| 767 × 300 mm | 8 × 9 (72 trays) | 8 | 39 | 60 | 78 / 78 |
| 362 × 300 mm | 3 × 9 (27 trays) | 4 | 14 | 30 | 28 / 28 |

Assembled depth is 110.5 mm. Removable ears are outside the finished dimensions.
Tray openings remain 87.5 × 27.5 mm and retain the stepped lip shoulders.
Four columns cannot fit within 362 mm with the current rail/border geometry.
The unused side margins have rectangular windows between mounting cross-ties;
container cavities are not scaled to fill the requested envelope.
Outside rail centres move 0.9 mm into the spare border to retain 1.55 mm of
material beside the snap pockets; the drawer openings remain unchanged.

## Tiles and connections

Plates remain 7.5 mm thick. Their seams follow beam mounts, with complementary
**3.75 mm half-thickness laps**, 11 mm across vertical seams and 9 mm across
horizontal seams. Nominal lateral seam gap is 0.15 mm. The flat lap faces bear
directly together. At a crossing the two layers belong to diagonal tiles;
adjacent seam screws secure the other two tiles.

Every rail on either seam uses the existing pointed alignment key, M3 × 16
countersunk screw and side-loaded M3 nut at **both** ends. Nuts use OOBB's
`overhang=True` and the existing left-side insertion. Other rails use sample
19's short, aggressive twin tabs at both ends: no middle guide or loose key,
1 mm arms, 6 mm free length to the catches, 1.2 mm hook projection, 0.25 mm
side clearance, tips flush with the outer face. The rail seats directly against
the plate. These fit values are adjustable; physical tuning remains outstanding.

Front tiles have the catch lip and reverse guide. Rear tiles have no forward
lip. Rear tile masks and mount positions are mirrored before assembly rotation,
so even the asymmetric three-column tile pattern lines up with the front.

## P1P layouts

The [official Bambu Studio P1P profile](https://github.com/bambulab/BambuStudio/blob/master/resources/profiles/BBL/machine/Bambu%20Lab%20P1P%200.4%20nozzle.json)
defines an excluded corner from (0,0) to (18,28) mm. The bed is 256 × 256 mm.
The planner keeps a further 2 mm margin, including all 12 mm ears and links.
It considers rectangles above or to the right of the excluded corner, selects
the fewest tiles, and takes the farthest feasible beam-aligned seam.

The largest complete footprints are approximately 210.33 × 241.28 mm for
the large demonstration and 231.08 × 241.28 mm for the smaller one. The current
tray pitch prevents adding another column or row to those leading tiles.

CAD coordinates use the **bed centre** as origin. Print files have deliberate
right/top offsets; centering or rotating them in the slicer can invalidate the
cutter clearance. Check placement against the actual printer profile. Avoid
adding external brims without checking the resulting footprint.

## Files and assembly

Each model's ordinary `parts` folder contains:

- `front_tile_*.stl` and `back_tile_*.stl`: print each once.
- `rails_plate_*.stl`: print each numbered batch once (four / two batches).
- `screw_rail`, `screw_bottom_rail`, `snap_rail`, `snap_bottom_rail`: individual
  replacement parts; these are not additional required kit quantities.
- `3dpr.stl`: complete kit overview, all pieces on the bed plane, **too large
  for one P1P bed**.
- `front`, `back`, `assembled`: assembled reference views, **not one-piece prints**.
- `assembly.json`: tile coordinates, footprint offsets, rail positions and BOM.
- `bed_layout.csv`: object-centre X/Y from the printer's left/front corner,
  for restoring placement if the slicer automatically centres an imported STL.
- `printing.txt`: orientation, fit and assembly instructions.

Use the supplied outside-face-down tile orientation and long-flat-face rail
orientation. Use local slicer supports under the 11/9 mm half-lap cantilevers.
The 1.2 mm recessed snap ledges and small screw/nut
bridges also need slicer inspection. This is not claimed to be a support-free
plate. Keep supports out of the rail spring slots.

Remove ears at their 0.2 mm necks. Dry-fit tile overlaps, load nuts from the
sides, assemble the front grid loosely, insert rails and progressively install
rear tiles. Tighten the seam screws only after the overlaps seat. Trial the
snap force and a tile seam before printing the entire set.

## Source and verification

`get_ai_version_5_tiled_options()` in `working_oomp_populate.py` owns both
definitions, dimensions, printer exclusion and fit settings.
`additional_screw_every=0` uses screws at seams only; setting N adds every Nth
rail to the screw set. Seam screws cannot be turned off by that option.
`working_scad_tiling.py` plans tiles and writes generated print metadata.
Solid bodies are drawn in `working_scad.get_ai_version_5_tiled`; all removals
route through `get_container_cutout_ai_version_5_tiled`.

Run `python action_validate_tiled_v5.py`. It invokes the complete
populate → OOMP → SCAD pipeline, exports the views, checks watertight meshes,
print-piece counts, Z=0 contact, the full printer envelope and cutter mask,
assembled dimensions and volume conservation across every rail joint.
It checks all frozen releases, v4, and the 134 earlier v5 coupon SCAD files
against the saved pre-development baseline. `--skip-generation` checks current
generated CAD only. Ordinary generation can now filter by variant as well as style.

Mesh checks establish geometry, not insertion force, creep, load capacity or
print success. PETG mass estimates use solid CAD volume and exclude the removable
tile ears and any slicer supports.

Validation passed for 46 exported mesh views, both complete assemblies, 54
geometry/unit tests and eight comparison tests. All earlier release/input/CAD
baselines passed. Rendered tiles and assembled layouts were also inspected.
