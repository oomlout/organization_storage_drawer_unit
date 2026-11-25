# Version 6: compact double sided frame for a plywood enclosure

There are now two compact frame sizes, both with opposing drawer banks:

| Maximum face size | Finished plastic frame (W x H x D) | Grid per face | Total drawers | Rails |
|---|---|---|---:|---:|
| 250 x 250 mm | 197.8 x 220.3 x 224 mm | 2 x 7 | 28 | 21 |
| 395 x 395 mm | 376.4 x 376.8 x 224 mm | 4 x 12 | 96 | 60 |

Both face plates now have a **6 mm base web plus 12 mm inward support tabs:
18 mm overall printed depth**. The actual enclosure follows the drawer grid
rather than filling a square with extra border. Plywood thickness and
joinery are additional to these plastic frame dimensions.

## Current kits: four screw rails and locating adapters

Both sizes now replace **four snap rails** with screw-fastened rails at the
outermost upper and lower rail positions. The 250 kit has **17 snaps + 4 screw
rails**; the 395 kit has **56 snaps + 4 screw rails**. Each includes **eight
small countersunk adapters**, one at each screw-rail end. Supply eight
**M3 x 20 mm countersunk screws** and eight M3 nuts.

The adapters enter the existing snap holes from outside. Their flanges guide
the screws into side-loaded OOBB nut pockets in the beams. Plate holes and
geometry remain unchanged, as do the remaining sample-37 snap rails. The
frame depth is still 224 mm; adapters add **2.4 mm outside each face**, giving
**228.8 mm overall plastic depth**. See [V6_SCREW_RAILS.md](V6_SCREW_RAILS.md).

For a new cabinet, print each mixed `rails_plate_*.stl` once and
`screw_adapters.stl` once, with one front and one back plate. For an existing
all-snap cabinet, print only `screw_upgrade.stl` to replace four rails; it
contains the four screw rails and eight adapters in one 157.5 x 212 mm layout.
It is identical for both sizes. Avoid printing this alternative in addition
to the complete mixed batches.

Use the new `print_files_screw_adapter.zip` in each active part folder.
The older `print_files_sample_37.zip` records the preceding all-snap kit.
Current validation reports are under `validation_double_sided_v6_screw_adapter/`:
**88 source tests, nine comparison tests and 27 mesh views pass**, including
both hardware paths, external adapter insertion, nut side-loading/capture and
all 81 rail locations. Geometry is checked; physical fastener fit and loads
still need a PETG trial.

## Remaining snap rail fit: selected sample 37

The user selected **37** from the physical fit suite. Both ends of the remaining
snap rails use **0.05 mm hook-pocket side clearance and 0.10 mm end play**.
The hook projection is 1.4 mm and its shoulder depth is 4.4 mm. All rail
batches for both sizes have been regenerated, with the original 1.8 mm arms,
root reliefs, flush tips, centre stops and cabinet dimensions.

The face plates have also been regenerated. Their receiving holes and all
plate geometry are **byte-identical to the preceding solid-web revision**,
so existing plates remain compatible. The preceding all-snap
`print_files_sample_37.zip` is preserved for reference; use the current
`print_files_screw_adapter.zip` for the mixed kit. Face files remain one front
plus one identical back.

Run `action_validate_double_sided_v6.py` with either size's `--variant`.
Reports for that all-snap revision and its immutable pre-change snapshot are under
`validation_double_sided_v6_selected_37/`. Both complete rail ends are checked
against the actual sample-37 mesh. Validation passes **84 source tests, nine
comparison tests and nineteen mesh views**, including all 81 rail positions.
The numbered trial kit remains unchanged. The selected trial has qualitative
physical fit feedback; full-unit loading and creep remain unverified.

## Historical numbered latch fit test

The user reported looseness after the previous latch clicked in. The
`latch_clearance_suite` provides nine short numbered tips, **30-38**, for
testing in the existing plate. The receiving hole and this historical test
kit remain unchanged after adopting 37 for full rails. Print its `3dpr.stl`
once: the nine-piece layout is **43 x 70 x 10 mm**. See
[V6_LATCH_CLEARANCE_TESTS.md](V6_LATCH_CLEARANCE_TESTS.md) for the clearance
matrix and testing instructions. Sample 30 reproduces the original fit.

## Plate revision: solid lower webs and matching cutout radii

Both sizes now remove the old **1 mm-high full-width relief below the snap
catches**. The lower opening shoulders join the crossbar as solid material.
The lower cutout also changes from R4 to **R1**, matching the upper rounded
rectangle. See `receiver_detail.png` for a close view. Overall dimensions,
floor tabs, corner holes and joining plates remain unchanged.

This plate correction originally kept the preceding floor-support rails;
the current rails now use sample 37 as described above. The source settings are `body_extension_height=0`
and `body_cutout_radius=1`; the frozen v4/v3 planning reference is read before
applying the v6-only radius. Continue populate -> OOMP -> SCAD.

Current reports are in
`validation_double_sided_v6_solid_lower_web/<variant>/`, with the preceding
v6 inputs, SCAD and previews preserved in `previous_v6_baseline.json` and
`previous_parts/`. Older validation folders record earlier revisions.
Validation passes **79 source tests, nine comparison tests and 19 mesh views**,
including all 81 seated rail fits and snap insertion/retention checks. Both
previews and the close-up were inspected. Physical PETG fit and loading remain
unverified.

## Paired floor supports and continuous receiver webs

Both sizes now use **two 15 mm-wide tabs** in the original 56 mm stop span,
leaving the middle **26 mm open**. Beneath each supported pot floor, the tabs
rise from the bed on 45-degree root slopes, carry a flat bearing roof and then
continue as thin 2 mm sections with tapered tips. They project 12 mm beyond the
6 mm plate web, giving **18 mm overall face depth**. The ribs have nested
print layers and no floating flat underside.

There is no added support beneath the physical bottom drawer floor: the
plywood takes that load. Inter-row tabs originate at the next drawer's top
and support the floor above. The topmost catches remain split/tapered but have
no 12 mm extension, because there is no drawer above them. There are **24 floor
tabs per face** on the small unit and **88 per face** on the large unit.

The wide T opening belongs at the TOP. CAD negative Y points up in service;
the assembly and face previews have been corrected accordingly. The primary
print files remain outside-face-down. See `support_detail.png` for a close view.

The old inner snap opening severed a narrow piece of web. Each receiver now
retains a continuous **1 mm web**, and its corresponding rail bevel is adjusted
for **0.25 mm clearance**. Use the newly regenerated rails with these plates.
Previous rails will collide with the retained web. Flush tips, snap-arm thickness,
centre stops, 212 mm rail length and 224 mm outside unit depth remain unchanged.
The M3 corner holes still pass through the 6 mm base web, and the optional
joining plates are unchanged.

The preceding floor-tab revision used approximately **12.7% less solid CAD material** for
the small unit and **14.0% less** for the large unit than the previous solid-stop
faces, despite extending inward. The current solid-web correction adds material
locally. Those historical figures are geometry volumes, not slicer weights
or strength ratings. Validation passes **78 source tests, nine comparison tests,
19 unit mesh views**, all 81 rail fits and all revised support/web checks.
The unchanged two-part joining plate file also passes its six-countersink
checks. Correctly oriented previews have been visually inspected. Inspect the
receiver lands and matching rail bevels in the
slicer, and physically trial PETG fit, bearing contact, snap force and loading.

Run the normal validator with `--variant double_sided_plywood_250_max` or
`--variant double_sided_plywood_395_max`. Reports for the preceding floor-tab revision are under
`validation_double_sided_v6_floor_supports/<variant>/`. The preceding v6 inputs,
SCAD and previews are preserved there in the immutable `previous_v6_baseline.json`
and `previous_parts/`; older reports stay intact. Changes are confined to the
two active v6 units; v1-v5 and the numbered coupons remain protected.

## Larger 395 mm maximum version

The `ai_version_6_style_double_sided_plywood_395_max` folder contains the
additional large model. Four columns x twelve rows is the maximum upright
uniform grid at the retained clearances and spacing. A fifth column needs
465.7 mm, and a thirteenth row needs 408.1 mm. The tight face size is therefore
**376.4 x 376.8 mm**, not 395 x 395 mm.

Print one `front.stl`, one identical `back.stl` and all four rail batches:
**16 + 16 + 16 + 12 rails**. Each plate has four plain M3 corner holes with
5 mm edge offsets, at X +/-183.2 mm and Y +/-183.4 mm from face centre.
The 212 mm rails, 19 x 10 x 3 mm middle stops and snap interfaces are unchanged.
`snap_rail.scad/stl` and `joining_plates.scad/stl` are byte-identical to the
250 mm version. The optional two- and four-unit joining plates remain together
in the one `joining_plates.stl` file and are excluded from the cabinet BOM.

One-piece faces require at least 376.4 x 376.8 mm usable area. The largest
rail batch is 379 x 224 mm. Every individual print file fits within 395 x
395 mm, with room for the configured 2 mm margin. The source uses a generic
400 x 400 mm planning bed without a printer-specific exclusion. No particular
large printer is verified; check its actual margins, exclusions and brim.
These face plates exceed the P1P and A1 mini beds.

The 62-piece `3dpr.stl` is an oversized kit overview, not a single-bed print.
`assembled.stl` is reference only. Use the supplied individual print files.
The enlarged overview spacing keeps the faces and rail batches separate.

Run `python action_validate_double_sided_v6.py --variant double_sided_plywood_395_max`.
Reports are in `validation_double_sided_v6_395_max/`; its immutable
`previous_250_baseline.json` protects the smaller unit. The default validator
continues to select the smaller unit. All v5 and earlier locks remain checked.
Validated on 2026-10-22: 76 source tests, nine comparison tests and ten mesh
exports pass. Checks include all sixty rail fits, snap insertion/retention,
central stops at all 96 pot positions, eight corner holes and individual print
bounds within 395 mm with 2 mm margins. Smaller v6 inputs and CAD, all fifteen
v5 records and earlier releases remain unchanged. Assembly and face previews
were visually inspected. Physical fit, large-face stiffness, loading, creep
and slicing need testing.

## Original 250 mm maximum version

The user corrected the maximum to **250 x 250 mm** and requested a compact
box around the actual drawer grid, with corner M3 mounting holes.
The revised plastic assembly is **197.8 x 220.3 x 224 mm**. It uses two
identical 197.8 x 220.3 mm plates (6 mm web, 18 mm overall depth) and **21 identical snap rails**.
Each face holds two columns x seven rows of lidless Systempak 209 / 100 ml
containers: **28 drawers total**.

No extra border is added to make the face square. Top/bottom structural bands
are 2 mm; the 10.5 mm side bands contain the outside snaps and mounting holes.
The existing 87.5 x 28.5 mm stepped openings, 31.3 mm row pitch and 1 mm extra
row separation remain. Three columns need 287.1 mm; eight rows need 251.6 mm
with 2 mm edges, or 251.2 mm even at the existing 1.8 mm wall minimum.
This is the maximum upright uniform grid with those retained dimensions.

## Plywood mounting

Each plate has four plain M3 clearance holes through its 6 mm thickness,
using the project's **3.6 mm OOBB M3 clearance diameter**. The centres lie 5 mm inward from
both adjacent outside edges: X +/-93.9 mm, Y +/-105.15 mm from plate centre.
There are eight mounting holes across the assembled front and rear plates.
They clear the tray openings, snap receivers and rail ends.

Use these to secure both plates to the plywood box wrapped around the frame.
Plywood thickness, joinery, screw length and any washers are user supplied.
The stated dimensions describe the plastic frame; adding plywood can increase
the enclosure's outside dimensions. No plywood thickness is assumed in CAD.
The enclosure follows the rectangular frame instead of filling a square face.
The axial face holes need plywood or corner backing cleats directly behind
them; a surround entirely outside the plate outline needs those backing lands.
Keep any internal cleats clear of the rails and drawer paths.

## Opposing drawers and stops

Rails remain 212 mm between the plates, with 6 mm snap tips ending flush with
both outer faces. Each rail has a 19 x 10 x 3 mm centre stop. Its wings reach
into the narrower pot-body channel and stay inside the compact frame width.
The stop faces lie 110.5 and 113.5 mm from the first outer plate face, so each
opposing bank has 109 mm nominal pot depth plus 1.5 mm insertion allowance.
Both outer tray catches remain.

The sample-28 snap interface retains 1.8 mm arms, 0.25 mm side clearance,
0.2 mm axial clearance, 1.2 mm hooks, rounded relief slots, rigid bearing strips
and bevelled receivers. Three rail boundaries support each of seven shelf
levels. There are no redundant top/bottom brace rails, loose keys or screws
in the rail-to-plate joints. Plywood mounting screws are separate.

## Print files

Use the `ai_version_6_style_double_sided_plywood_250_max` folder under `parts`:

- Print `front.stl` once and `back.stl` once, outside face on bed.
- Print every `rails_plate_*.stl` batch once: **9 + 9 + 3 rails**.
- `snap_rail.stl` is an individual spare, not an additional kit piece.
- `3dpr.stl` is the complete 23-piece kit overview and exceeds one bed.
- `assembled.stl` is a reference, not a one-piece print.
- `assembly.json` records the dimensions, exact BOM, holes, stops and batches.

The face plates and each rail batch fit the established P1P 256 x 256 mm
planning bed with a 2 mm margin and 18 x 28 mm cutter exclusion. Retain the
supplied poses; check any brim against the cutter envelope. The one-piece
plates exceed the A1 mini bed. There are no tile seams or removable ears.

Rails print on their long flat face, with their central stop wings directly
on the bed. Snap the rails into the first plate, progressively seat the
second plate, then use the corner holes to attach the plywood enclosure.
Inspect the small receiver lands and keep supports out of the spring slots.

## Joining adjacent units

**`joining_plates.stl` contains both joining components in the same file:**

- Four-unit plate: **20 x 20 x 6 mm**, four countersunk M3 holes on a 10 x 10 mm grid.
- Two-unit plate: **20 x 10 x 6 mm**, two countersunk M3 holes 10 mm apart.

Each combined file prints one of each, with 5 mm between the separate solids.
Flat backs sit on the bed and countersinks face upward. The total print
footprint is 45 x 20 mm. The OOBB M3 cutouts use 3.6 mm through-clearance,
7.2 mm countersink mouths and 1.9 mm countersink depth.

Fit the square across a junction of four cabinet corners, using one existing
corner hole from each cabinet. Fit the strip across two neighbouring corners;
rotate it 90 degrees for a vertical seam. Mount on the outside plate faces,
with the screw heads facing outward and suitable backing or nuts behind.
Supply countersunk M3 screws long enough for the joiner, cabinet face and your
chosen backing. The joiners are optional and excluded from the single-unit
BOM, kit overview and assembled reference.

The **10 mm pitch assumes touching plastic face edges**. If separate plywood
boxes leave a gap between those edges, their corner holes are farther apart;
set population's `joining_plate_unit_gap` to the measured gap and regenerate.
No plywood thickness is assumed. The 20 mm joiners stay within the side bands
and leave drawer openings clear at the intended corner positions.

Run `python action_validate_v6_joining_plates.py`. It generates the normal
pipeline, exports the combined STL and checks both solids, all six countersinks,
through-bores, flat bed contact and corner-hole alignment. Validation passed
with 74 source tests; all nine existing cabinet SCAD views and earlier designs
remain unchanged. The combined preview was visually inspected. Physical fit,
screw-head seating and joint strength still need a PETG trial.

## Sources and verification

`get_ai_version_6_options()` in `working_oomp_populate.py` owns the container,
compact dimensions, edge thickness and corner-hole settings. Bodies live in
`working_scad.py`, complete removals in `working_scad_container_cutout.py`, and
generated metadata in `working_scad_double_sided.py`.

Run `python action_validate_double_sided_v6.py` for populate -> OOMP -> SCAD,
STL exports and mesh checks. The current output directory is
`validation_double_sided_v6_250_max/`. The immutable previous-v5 baseline remains
in `validation_double_sided_v6/`; the earlier report is retained. The superseded
300 mm part/source folders are archived under its `superseded_300_mm/` directory
and removed from the active catalogue.

Geometry checks cover connected closed print meshes, bed contact, P1P bed and
cutter limits, compact dimensions, four through-holes and surrounding material
in each face, all seated rail joints, snap insertion/retention, assembly volume
conservation and central stops at every bay. Earlier v1-v5 geometry is protected.
Physical PETG fit, real tapered-pot contact, strength, creep and slicing still
require testing.

Validated on 2026-10-22: 72 source/geometry tests, nine comparison tests and
eight mesh views passed. All 21 seated rail joints, prescribed insertion and
retention, 28 pot positions, eight corner holes and P1P limits passed. The
assembly volume difference is 0.0211 mm3, within the mesh tolerance. All 15
previous v5 records and v1-v4 checks remain unchanged. Assembly and face
previews were visually inspected.
