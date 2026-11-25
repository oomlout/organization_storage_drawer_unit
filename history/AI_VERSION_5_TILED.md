# Version 5 tiled PETG demonstrations

The user authorized full v5 demonstrations after the connector trials and selected
the 100 ml Systempak 209 trays. The current finished dimensions below include the
requested extra row spacing and 6 mm plates. These demonstrations are experimental.

| Finished plate | Tray grid | Tiles per face | Screw rails | Snap rails | M3 × 16 countersunk screws / M3 nuts |
|---|---:|---:|---:|---:|---:|
| 767 × 308 mm | 8 × 9 (72 trays) | 8 | 18 | 81 | 36 / 36 |
| 362 × 308 mm | 3 × 9 (27 trays) | 4 | 7 | 37 | 14 / 14 |
| 205.8 × 268.6 mm, A1 mini | 2 × 8 (16 trays) | 4 | 6 | 24 | 12 / 12 |

Assembled depth is 110.5 mm. Removable ears are outside the finished dimensions.
Tray openings are now **87.5 × 28.5 mm**, adding 1 mm of vertical room to
each 100 ml tray while retaining the stepped lip shoulders. The user then
requested **another 1 mm between rows**: `row_spacing_extra=1.0` makes the
row pitch **31.3 mm** and the gap between openings **2.8 mm**. Openings and
rails use the same pitch. Nine-row units grow to **308 mm tall** to retain
their grids and M6 border bands. A1 mini grows to **268.6 mm** and uses
**11 mm removable ears** to keep four tiles per face on its 180 mm bed.
Legacy variant/folder names ending `by_300` remain stable identifiers;
the generated assembly metadata records the new finished dimensions.
Four columns cannot fit within 362 mm with the current rail/border geometry.
The unused side margins have rectangular windows between mounting cross-ties;
container cavities are not scaled to fill the requested envelope.
Outside rail centres move 0.9 mm into the spare border to retain 1.55 mm of
material beside the snap pockets.

## Tiles and connections

Plates are now **6 mm thick**. Their seams follow beam mounts, with complementary
**3 mm half-thickness laps**, 11 mm across vertical seams and 9 mm across
horizontal seams. Nominal lateral seam gap is 0.15 mm. The flat lap faces bear
directly together. Each tile now has **all its laps in the same half** of the
plate, alternating with neighbouring tiles in a checkerboard. The wider layer
prints against the bed; alternate tiles are already flipped in their STL files.
Small corner notches allocate each four-way overlap to one diagonal tile.
The upper printed footprint stays within the lower footprint.

Only the ends of each tile-to-tile seam and the middle of long seams use
M3 × 16 countersunk screws and side-loaded M3 nuts at **both** beam ends.
Horizontal seams use left/right anchors. A middle anchor is added when the
mount span is at least 120 mm. Nuts still use OOBB's `overhang=True` and
left-side insertion. Screw beams now have flat end seats: the projecting
plate keys and their rail sockets are removed so inside-down tiles can lie
flat. Tile laps and neighbouring snap mounts locate the parts.
The matching rails are 98.5 mm between the plates. Nut pockets are
7–10 mm from each rail end to retain M3 × 16 screws; solid end bands remain
to 14.5 mm to leave material beyond the nuts.

Other rails, including intermediate seam mounts, use short twin tabs at both
ends. Their undersides rise at **45 degrees**, ending in **4 mm-high tips**.
The matching receiver floor slopes the same way, with a **4.5 mm-high outside
opening** that grows toward the entry face. This retains the narrow vertical
spine below the 100 ml shelf in both halves of the lap, instead of cutting it
across with a rectangular hole. The underside grows from the rail's flat
printing face; there is no floating tab or added sacrificial support.
The main snap now uses the user-selected **sample 28**: **1.8 mm arms**,
1.2 mm hook projection, 0.25 mm per-side clearance and 0.2 mm axial clearance.
The user confirmed **recessed clips at both ends**, superseding the initial
request for protruding front clips. Tips extend 6 mm from the rail end and
finish flush with the panel's outside face. Hook shoulders are 4.5 mm from
the rail end; slots extend 2 mm into the beam to preserve the original
6.5 mm root-to-shoulder span. Two 0.6 mm outer relief slots keep these extended
arms 1.8 mm thick, with 1.5 mm rigid bearing strips outside them. The relief
ends are rounded. This is an adaptation of sample 28, not a change
to its historical coupon. Printable bevels remain.
Sample **27** is the selected standard for the separate-key style; the tiled
demo continues to use direct snaps at its non-screw mounts.
Population's `get_ai_version_5_selected_connector()` owns both profiles.
The original numbered coupon files remain available unchanged.
Print the new rails with the new plates;
the original full-height tabs cannot pass the new bevelled floors.
The receiver retains a 0.5 mm catch land, with the rest of its pocket roof
sloping at 45 degrees. These revised joints need a physical PETG fit print.

Front tiles retain **6 mm of stop projection**, now **6 mm thick**, with
0.75 mm, 45-degree top-edge chamfers. Both faces lie within the panel
thickness so either tile orientation sits flat. Rear tiles have no forward lip.
Rear tile masks and mount positions are mirrored before assembly rotation,
so even the asymmetric three-column tile pattern lines up with the front.

## Back-to-back M6 attachments

Rear panels have M6 through-holes and **1.5 mm-deep hex seats on the inside**:
22 locations on the 767 mm unit, 12 on the 362 mm unit and six on the A1 mini
unit. These are screw/nut fittings, not magnet recesses. Each location has its
X mirror so two identical units turned back-to-back line up. Neither clips
nor fittings project beyond the outer rear mating face.

Use an M6 hex-head screw from one cabinet and an M6 nut inside the other.
The shallow seats capture the hex hardware; most of the nut/head remains
inside the cabinet. There is 9 mm between the two recessed bearing faces;
select screw length for that distance, your nut and the required thread
engagement. Fasteners are optional and excluded from the cabinet's M3 BOM.
OOBB M6 nut primitives retain their local bridge relief.

The 14.5 mm attachment bands keep the pockets clear of tray openings and
rail hardware. No seat crosses a tile seam. The A1 mini side margins are
widened by 4 mm per side to accommodate these bands; its top/bottom borders
have no M6 seats.

## P1P layouts

The [official Bambu Studio P1P profile](https://github.com/bambulab/BambuStudio/blob/master/resources/profiles/BBL/machine/Bambu%20Lab%20P1P%200.4%20nozzle.json)
defines an excluded corner from (0,0) to (18,28) mm. The bed is 256 × 256 mm.
The planner keeps a further 2 mm margin, including all 12 mm ears and links.
It considers rectangles above or to the right of the excluded corner, selects
the fewest tiles, and takes the farthest feasible beam-aligned seam.

The largest complete footprints are approximately 210.33 × 242.78 mm for
the large demonstration and 231.08 × 242.78 mm for the smaller one. The current
tray pitch prevents adding another column or row to those leading tiles.

## A1 mini four-plate layout

The [official A1 mini specification](https://uk.store.bambulab.com/products/a1-mini)
gives a 180 × 180 mm bed. This option uses a 2 mm margin and 11 mm removable
ears. The [official Bambu Studio A1 mini profile](https://github.com/bambulab/BambuStudio/blob/master/resources/profiles/BBL/machine/Bambu%20Lab%20A1%20mini%200.4%20nozzle.json)
has an empty bed-exclusion area, so the P1P cutter mask is not applied.
It has **four tiles per face**, arranged
2 × 2: four front tiles and four rear tiles, plus three rail batches.
The largest footprint including ears is approximately 108.33 × 174.63 mm.
The grid contains 2 × 8 trays; a ninth row requires another tile row with the
current beam-aligned seams and ears. Tile sizes follow complete tray bays;
they are not stretched to fill the unused bed width.

CAD coordinates use the **bed centre** as origin. Print files have deliberate
right/top offsets; centering or rotating them in the slicer can invalidate the
cutter clearance. Check placement against the actual printer profile. Avoid
adding external brims without checking the resulting footprint.

## Files and assembly

Each model's ordinary `parts` folder contains:

- `front_tile_*.stl` and `back_tile_*.stl`: print each once.
- `rails_plate_*.stl`: print each numbered batch once (four / two / three batches).
- `screw_rail`, `screw_bottom_rail`, `snap_rail`, `snap_bottom_rail`: individual
  replacement parts; these are not additional required kit quantities.
- `3dpr.stl`: complete kit overview, all pieces on the bed plane, **too large
  for one printer bed**.
- `front`, `back`, `assembled`: assembled reference views, **not one-piece prints**.
- `assembly.json`: tile coordinates, footprint offsets, rail positions and BOM.
- `bed_layout.csv`: object-centre X/Y from the printer's left/front corner,
  for restoring placement if the slicer automatically centres an imported STL.
- `printing.txt`: orientation, fit and assembly instructions.

Use the supplied alternating tile orientations and long-flat-face rail
orientation. The former 11/9 mm unsupported lap cantilevers are removed.
The small 0.5 mm catch lands and screw/nut bridges still need slicer inspection;
mesh checks are not a guarantee of printing success. Keep supports out of
the rail spring slots.

Remove ears at their 0.2 mm necks. Dry-fit tile overlaps, load nuts from the
sides, assemble the front grid loosely, insert rails and progressively install
rear tiles. Tighten the seam screws only after the overlaps seat. Trial the
snap force and a tile seam before printing the entire set.

## Source and verification

`get_ai_version_5_tiled_options()` in `working_oomp_populate.py` owns all three
definitions, dimensions, printer exclusion and fit settings.
`additional_screw_every=0` uses only the seam anchors; setting N adds every Nth
rail to the screw set. `seam_middle_screw` and `seam_middle_min_span` control
middle anchors. Seam ends always remain screwed.
`working_scad_tiling.py` plans tiles and writes generated print metadata.
Solid bodies are drawn in `working_scad.get_ai_version_5_tiled`; all removals
route through `get_container_cutout_ai_version_5_tiled`.

Run `python action_validate_tiled_v5.py`. It invokes the complete
populate → OOMP → SCAD pipeline, exports the views, checks watertight meshes,
print-piece counts, Z=0 contact, the full printer envelope and cutter mask,
assembled dimensions and volume conservation across every rail joint.
It checks all frozen releases, v4, and all twelve current v5 coupon records
against `validation_tiled_v5_print_revision/previous_coupons_baseline.json`.
Older validation snapshots containing the previous tiled demos remain historical;
the two original tiled records are intentionally revised and the A1 mini record added.
`--skip-generation` checks current
generated CAD only. Ordinary generation can now filter by variant as well as style.

Mesh checks establish geometry, not insertion force, creep, load capacity or
print success. PETG mass estimates use solid CAD volume and exclude the removable
tile ears and any slicer supports.

The validator checks every tile is one connected printable body at Z=0, nested
lap footprints, both assembled envelopes, all mating volumes, the restored
vertical spines at every snap, actual tab bevels, and seam-snap insertion/retention.
The current validator also checks M6 through-holes, seat depth, surrounding
material, mirrored back-to-back alignment and retained 6 mm tray stops.
The current report is `validation_tiled_v5_six_mm/report.json`;
the preceding thin-panel and print revision reports are retained separately. All twelve
existing connector-test records and their SCAD files must remain unchanged.
These checks establish geometry and printing poses; actual PETG fit and
printing still need a trial.

The six mm plate / extra spacing revision passes 65 exported mesh views,
three assembly checks, 66 geometry tests and eight drawer comparison tests.
Release checks pass; all twelve prior connector records and 175 coupon SCAD
views remain unchanged. Revised tiles and assembly previews were visually
reviewed. A broader webserver run has five unrelated failures in file-action
tests; details are retained in `validation_tiled_v5_six_mm/webserver_tests.log`.
