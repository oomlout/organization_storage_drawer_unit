# AI version 1: locked release

On 2026-10-19 the user retired the three clearance-fit catalogue variants from
all versions. Eleven version 1 models remain active; the fourteen-model release
snapshot and manifest are unchanged. Clearance is still an adjustable 1.5 mm
default and is not included in taxonomy. The release checker explicitly permits
only these retired records while checking every retained model unchanged.

Implemented 2026-10-18 for a 400 x 400 mm print bed. These are prototype parts for
physical testing, with adjustable dimensions. The user reported bed-adhesion
trouble with the previous version. This revised ramp/ear geometry has not yet
been physically verified or load tested. No filament, nozzle or shrinkage
calibration has been specified yet. The original 400 mm printer's usable Z height
is unspecified; the A1 mini and P1P variants use their published build volumes.

## Release locked 2026-10-19

The released design includes an additional 1.5 mm vertical space per 550 ml
row, declared as `opening_height_extra` in population. Opening height is now
95 mm, with ear-inclusive heights of 140.8 mm (1 row) and 237.6 mm (2 rows).
The 100 ml geometry is unchanged. Dimensions/results below describe earlier
iterations unless stated otherwise. The final baseline is archived under
`releases/ai_version_1/`; future development uses the independent version 2
functions described in AI_VERSION_2.md. Check the release after regeneration
with `python action_check_version_1_lock.py`.

## Design

The body is still one positive solid with container openings subtracted from it.
The released cutout is the user's stepped `get_container_cutout_ai_version_1()`:
a full-width 12 mm high channel and a full-height channel inset 5.5 mm on each
side. The step forms the shelf that engages the container's moulded lip. Those
profile dimensions and the nominal 1.5 mm container clearance are preserved.

Side reliefs now lie below and above that shelf, retaining 3 mm of material above
the step and a further 1 mm below at the wall attachment. Upper reliefs extend
through the thick shoulder, not just the outside wall. The shelf is continuous
along insertion depth; its connection to the wall is no longer interrupted by
the old generic side hole. This is intended to improve support at the shelf root,
but stiffness/load capacity still require physical tests.

One broad floor/ceiling opening replaces the two smaller openings, removing the
centre support. The retained edge rails are 10 mm wide to protect the stepped
profile and its rounded corners. Side walls retain 5 mm corner rails. Continuous
7.5 mm front and 6 mm rear bands tie the structure together. All dimensions are millimetres.

Each window closes with a pointed roof at 45 degrees to the bed. This is intended
to avoid long unsupported bridges while printing the unit front-face down. The
front catches grow from the shelf at the bed, ramping 6 mm into the opening
over 6 mm of print height (45 degrees), followed by a 1.5 mm thick tip. They
are added after the opening subtraction. The
back remains open. The existing `basic` design remains available for comparison.

The 6 mm stop revision applies to all fourteen AI variants, for both container
sizes. Shallow layout depths increased from 6 to 7.5 mm to contain the ramp
and tip. Full-depth frame envelopes and printer maxima are unchanged. All
thirteen unit tests and fourteen mesh validations passed after full pipeline
regeneration; the trial table below reflects this revision's CAD volumes.

The first iteration uses a single piece rather than a clamshell. This avoids
introducing mating tolerances and screw loads before container fit and the ribbed
frame have been tested. A screwed clamshell remains a possible later version; no
clamshell, screw holes, mounting system, or structural module connectors are
implemented in this version.

After removing the adhesion ears, outside faces are flat apart from small corner radii.
Modules can sit side by side. The paired layout test includes a configurable
0.4 mm gap. Across that seam, two 2.4 mm outside borders plus the gap make a
5.2 mm separator, compared with 1.8 mm internal dividers. Row positions match
between identical modules; the seam is intentionally wider than an internal
divider. A mechanically joined bank and a completely uniform seam need a later
joint design. Do not interpret the layout model as an assembled load-bearing bank.

Four 20 mm diameter, 0.6 mm thick adhesion ears sit beyond the top and bottom
corners of each module's front face. Each pad has a 0.5 mm gap to the frame,
bridged only by a 5 mm wide, 0.3 mm high neck. The neck overlaps the frame by
0.4 mm and the pad by 0.8 mm for a real, connected solid. Bend or clip the neck
after cooling and trim the small remaining nub; the frame wall itself is not
scored or thinned. Removal force and adhesion need a physical trial.

Use a first-layer height no greater than the 0.3 mm link height, or increase
`ear_link_height` to suit the chosen first layer. Inspect that the links appear
in the slicer's first-layer view. `adhesion_ears=False` disables all four pads.
The large model's complete footprint is now 360.2 x 395.6 mm, with 2.2 mm spare
on each Y edge when centred on a fully usable 400 mm bed. `bed_margin` is now
2 mm measured outside the ears; any slicer brim/skirt needs additional room.

## Files and reproduction

All models, including test pieces, follow:

`working_oomp_populate.py` -> `parts_source/<id>/working.yaml` ->
`working_oomp.py` -> `parts/<id>/working.yaml` -> `working_scad.py` -> SCAD/STL.

- Edit option sizes/variants and `get_ai_version_1_defaults()` in
  `working_oomp_populate.py`.
- `working_scad.get_ai_version_1()` declares the solid body, places each cell's
  complete cutout, and adds the module-level adhesion ears. Parameter validation
  and design summaries remain in nearby `get_ai_version_1_*` helpers.
- `working_scad_container_cutout.get_base()` dispatches each AI cell to the single
  `get_container_cutout_ai_version_2()` routine under the existing `ai_version_1`
  style and IDs. That routine contains the stepped opening,
  both floor and ceiling reliefs, both side-wall reliefs, and the catch, using
  explicit multiline component dictionaries. `row_index` and `column_index`
  identify exterior borders. Neighbouring cells deliberately repeat shared-wall
  cuts; they remove the same space and keep each cell's cutout self-contained.
  There are no separate frame-wide relief/window drawing helpers. The original style continues
  to use `get_container_cutout_version_1()`.
- `python action_make_scad_no_stl.py` regenerates all source records and SCAD.
- `python action_validate_ai_version_1.py` runs the complete pipeline, exports all
  fourteen AI STLs with OpenSCAD Manifold, checks their meshes, renders previews, and
  refreshes taxonomy navigation copies. It requires numpy/trimesh/PyYAML/Shapely in
  addition to the existing project dependencies.
- `python -m unittest discover -s tests -v` runs thirteen focused design/dispatch tests.

Each generated part is under `parts/`, with its matching taxonomy copy under
`navigation_oobb/organization/storage/drawer_unit/`. `3dpr.stl` and `3dpr.scad`
use the print orientation: front on Z=0, increasing Z toward the open back.
`preview.png` presents the same geometry standing upright. `preview_scene.scad`
is generated presentation-only rotation; do not use that scene for print orientation.

## Trial set

The common part ID prefix is
`organization_storage_drawer_unit_<column>_column_<row>_row_rectangle_100_ml_tamper_evident_systempak_209_container_ai_version_1_style`.
Variants append the indicated suffix. An unsuffixed AI part is a full-depth frame.

| Model | ID suffix | Print envelope including ears X x Y x Z | CAD volume, cm3 | Purpose |
| --- | --- | --- | ---: | --- |
| 1 x 1 fit | `_fit_clearance_0d75` | 91.55 x 72.55 x 12 | 11.06 | Tightest total opening clearance, 0.75 mm |
| 1 x 1 fit | `_fit_clearance_1d5` | 92.3 x 73.3 x 12 | 11.25 | Default total clearance, 1.5 mm |
| 1 x 1 fit | `_fit_clearance_2d25` | 93.05 x 74.05 x 12 | 11.43 | Loosest total opening clearance, 2.25 mm |
| 1 x 1 frame | none | 92.3 x 73.3 x 110.5 | 44.96 | Full insertion, lip shelves, catch and roof trial |
| 2 x 2 frame | none | 181.6 x 102.6 x 110.5 | 137.87 | Shared dividers and small load trial |
| 2 x 2 reference | `_solid_reference` | 181.6 x 102.6 x 110.5 | 257.75 | Same stepped profile and catches, relief windows disabled |
| Two 2 x 2 layouts | `_bank_layout` | 363.6 x 102.6 x 7.5 | 47.67 | Side-by-side alignment, seam and long-axis shrinkage |
| 4 x 12 layout | `_layout` | 360.2 x 395.6 x 7.5 | 229.38 | Bed footprint, two-axis shrinkage and 48-drawer spacing |
| 4 x 12 frame | none | 360.2 x 395.6 x 110.5 | 1304.30 | Large 48-drawer module after smaller trials pass |

After removal, each frame is 41 mm shorter along Y than its ear-inclusive footprint.
Volumes above include the ears and are the exported solid geometry, not slicer filament consumption or
an assumed material mass. Clearance is added to the overall opening width/height,
so a 1.5 mm value means nominally 0.75 mm on each opposing side. Container body
dimensions are 86 x 26 x 109 mm in drawing axes; the lid is not used.

## Maximum printer-specific grids

Two additional full-depth frame options are defined directly in the population
`experiments` list. They retain the current 6 mm ramped catch, 20 mm ears,
container clearance, ribs, walls, and 2 mm margin beyond the complete footprint.
Their unique `variant` values form `taxonomy_9` and keep them separate from the
other generated parts. The drawing checks their specified Z build height too.

| Printer | Grid / drawers | Variant suffix | Finished frame, mm | Print envelope with ears, mm | Build volume, mm |
| --- | --- | --- | --- | --- | --- |
| A1 mini | 1 x 4 / 4 | `_a1_mini_max` | 92.3 x 120.2 x 110.5 | 92.3 x 161.2 x 110.5 | 180 x 180 x 180 |
| P1P | 2 x 7 / 14 | `_p1p_max` | 181.6 x 208.1 x 110.5 | 181.6 x 249.1 x 110.5 | 256 x 256 x 256 |

These are maximum grids for the current face-down design and parameters: adding
one column or one row exceeds the corresponding bed constraint. Two columns
already make a 181.6 mm wide frame, exceeding the A1 mini's 180 mm bed before any
margin. Five rows on the mini need 190.5 mm including ears. On the P1P, three
columns need 270.9 mm and eight rows need 278.4 mm including ears. No fit or wall
dimensions were reduced to squeeze in another drawer.

Use `3dpr.stl` in the matching `parts/` directory, in its supplied face-down
orientation. Centre it on the bed; the P1P has 3.45 mm spare at each Y edge
including the existing 2 mm reserved margin. Extra slicer skirts/brims consume
additional space. The files include ears already. This is a geometric fit check,
not a printer-specific sliced toolpath.

Build-volume sources, verified 2026-10-18:
[Bambu A1 mini specifications](https://uk.store.bambulab.com/products/a1-mini?from=navigation)
and [Bambu P1P specifications](https://public-cdn.bambulab.com/store/bambulab-P1P-tech-specs.pdf).

## Systempak 214: 550 ml container

Added 2026-10-18 from the user's
[OOMP container record](http://oomp.bv/parts/packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214).
The catalogue dimensions are 108 x 86 x 95 mm. Drawing axes are explicitly
X/across = 86 mm, Y/container height = **95 - 3 = 92 mm without the lid**,
and Z/insertion depth = 108 mm. With the unchanged 1.5 mm clearance, each opening
is 87.5 x 93.5 mm and the frame insertion depth is 109.5 mm.

The user confirmed the same top/lip design as the 100 ml container. These options
reuse the active stepped cutout, 12 mm lip channel, 5.5 mm side shoulders,
3 mm continuous lip shelves, relief windows, ramped catches and removable ears.
The taller body extends away from the lip; the support profile is unchanged.
Following the user's material-saving correction, the thick shoulders stop at
the same height as the 100 ml profile. `lip_support_reference_height=26` is the
lidless reference body height; adding the active clearance gives a 27.5 mm
support region at default clearance, or 15.5 mm beyond the 12 mm lip step.
The remaining 66 mm of the 550 ml cavity opens to full width along the entire
insertion depth, including the front and rear bands. Thin outer/divider walls
and the far rounded opening corners remain. The 3 mm continuous bearing shelf
is retained, and all 100 ml variants keep their previous geometry.
Options are declared in `working_oomp_populate.py`; dimensions are mapped in
`working_scad.get_container_details()`.

| Model | Grid / drawers | Finished frame X x Y x Z, mm | Print envelope with ears, mm |
| --- | --- | --- | --- |
| Standard | 1 x 1 / 1 | 92.3 x 98.3 x 109.5 | 92.3 x 139.3 x 109.5 |
| A1 mini maximum | 1 x 1 / 1 | 92.3 x 98.3 x 109.5 | 92.3 x 139.3 x 109.5 |
| P1P maximum | 2 x 2 / 4 | 181.6 x 193.6 x 109.5 | 181.6 x 234.6 x 109.5 |

The standard and mini have identical geometry but distinct IDs and printer limits.
The common ID suffix is
`rectangle_550_ml_tamper_evident_systempak_214_container_ai_version_1_style`,
with `_a1_mini_max` and `_p1p_max` appended for the printer variants.
These maxima retain the current ears and 2 mm margins: a second mini column
needs 181.6 mm and a second row needs 234.6 mm; a third P1P column needs
270.9 mm and a third row needs 329.9 mm. Print Z is 109.5 mm in all three cases.
Physical container fit and loaded shelf strength still require a print trial.

Initial verification: all twelve unit tests and all fourteen exported-mesh validations
passed after regeneration through population -> OOMP -> SCAD. The new frames
passed envelope, bed/Z fit, connected-body, watertightness, downward-face angle,
lip shelf/root, bearing clearance, side relief and centre-rail removal checks.
Reports and previews are in the generated part folders; the combined report is
`validation_ai_version_1/report.json`.

After the shoulder-height correction, all thirteen unit tests and all fourteen
mesh validations passed, including new sections checking the front/rear bands.
CAD volume including ears fell from 77.04 to 52.32 cm3 (32.10%) for both 1 x 1
variants, and from 254.38 to 155.47 cm3 (38.88%) for the P1P 2 x 2. All eleven
100 ml exported volumes are unchanged. These are geometric material savings,
not measured load capacity or slicer consumption. Before/after evidence is in
`validation_ai_version_1/before_shoulder_height_limit.json` and
`validation_ai_version_1/shoulder_height_limit_comparison.json`.

## Adjustment controls

| Population field | Default | Effect |
| --- | ---: | --- |
| `column`, `row` | Per option | Number of containers |
| `container_clearance` | 1.5 | Total extra opening width/height; also changes pitch and envelope |
| `depth_clearance` | 1.5 | Extra frame length beyond the mapped container depth (109 mm for 209, 108 mm for 214) |
| `thickness_wall` | 1.8 | Interior shelf/divider thickness |
| `drawer_border_edge` | 2.4 | Outside wall thickness; must be at least the divider thickness |
| `runner_width` | 10 | Edge material retained outside the broad floor/ceiling opening; protects stepped corners |
| `middle_rib_width` | 0 | No centre rail; positive values restore two smaller windows for optional trials |
| `depth_lip` | 12 | Height of the full-width section of the user's opening |
| `inset_lip` | 5.5 | Shoulder width on each side of the narrower body channel |
| `lip_cutout_radius` | 1 | Radius of the full-width channel; also protects material immediately below the step |
| `lip_shelf_thickness` | 3 | Continuous shelf material above the step, protected from side reliefs |
| `lip_support_reference_height` | 26 | Lidless reference body height limiting thick shoulders; add active clearance, then open taller bodies to full width |
| `side_rail_width` | 5 | Rails retained at the top/bottom of a side-wall window |
| `front_band`, `rear_band` | 7.5, 6 | Continuous frame depth at each end |
| `roof_slope` | 1 | Rise/run of closing window roofs; values below 1 are rejected |
| `opening_radius`, `outer_radius` | 4, 2.4 | Opening and external corner radii |
| `catch_tab_width` | 56 | Width of the retaining lip |
| `catch_tab_height` | 6 | Maximum projection into the opening from its bottom edge |
| `catch_tab_ramp_depth` | 6 | Print-height run of the ramp; must be >= projection for a supportable slope |
| `catch_tab_depth` | 1.5 | Tip thickness after the ramp; ramp plus tip stay within front band |
| `adhesion_ears` | true | Four removable corner pads per module |
| `ear_diameter`, `ear_height` | 20, 0.6 | Pad size in the bed plane and print thickness |
| `ear_gap` | 0.5 | Air gap between pad and frame except at the neck |
| `ear_link_width`, `ear_link_height` | 5, 0.3 | Breakaway neck dimensions; set height to suit first layer |
| `lightening` | true | Disable for a reference frame with continuous walls |
| `part_role` | `frame` | `frame`, `fit`, `layout`, or `bank_layout` |
| `test_depth` | Per trial | Depth for fit/layout pieces; never used for full frames |
| `module_gap` | 0.4 | Gap in the paired layout only; no attached connector implied |
| `bed_width`, `bed_height`, `bed_margin` | 400, 400, 2 | Check the complete footprint, including ears, with margin on all sides |
| `build_height` | Printer-specific | Maximum allowed print Z: 180 for A1 mini, 256 for P1P |

Example: change `lip_shelf_thickness` from 3 to 4 for a thicker shelf trial, add a copied
option with a distinct `variant`, and regenerate. Keep all changes in population
and drawing source. Do not edit generated part YAML or SCAD to adjust a model.
Variant taxonomy is necessary to prevent trials overwriting one another.

## Physical test order and recording

1. Slice and print the three small fit samples using the intended filament,
   nozzle and production settings. Keep each associated with its clearance ID.
   Test several actual lidless containers; check rim passage, catch engagement
   and removal. Check pad adhesion and ease of clipping/bending the thin links.
   A short sleeve cannot validate full-depth taper or bottom shape.
2. Copy the preferred clearance to the full-depth 1 x 1 option. Check insertion,
   sliding, the retaining lip, and the roof surfaces at the rear of the reliefs.
   Check the slicer layer view before printing. Face-down orientation matters.
3. Print the 2 x 2 frame. Gradually trial the intended drawer contents; record
   weight per drawer, shelf deflection, twisting, and any layer separation.
   Compare with the same-envelope reference if stiffness is inadequate. There
   is no established load rating. Adjust rails, ribs, dividers or bands based on
   observed flex; larger banks still need their own load test.
4. Print the paired shallow layout to check seam alignment and long-span cooling.
   Then use the 4 x 12 layout for the full bed footprint. Measure after cooling,
   including width/height at more than one location and flatness/corner lift.
5. Only then print a large full-depth module. Recheck distortion at full height,
   container movement and deflection under the intended load. A shallow layout
   cannot prove that the tall frame will remain flat or strong.

Record the model ID, date, printer, nozzle, filament, layer height, line widths,
perimeters, bed/chamber temperatures, brim, measured X/Y, corner lift, container
sample, loaded mass per drawer, and fit/deflection observations together. Preserve
failed tests as evidence when selecting the next parameter values.

The machine's usable Z height must allow at least 110.5 mm for this design. Actual
slicer settings must suit the selected nozzle; the CAD checks do not verify that
wall thicknesses resolve into the desired extrusion lines.

## Shrinkage approach and limits

The reliefs remove broad continuous sheets and keep material concentrated in
runners and ribs. They are a design hypothesis for reducing material and thermal
stress, not proof that a large frame cannot warp. The outer bands still span the
whole module. Smaller modules remain an option if full-bed trials distort.

Do not guess a universal shrinkage percentage. For a repeatable, approximately
uniform dimensional error, measure a known cooled span and use correction factor
`nominal / measured` in a documented slicer scale setting. For example, use the
layout's measured frame dimensions after ear removal against 360.2 x 354.6 mm. Investigate corner
lift/bowing separately: scaling cannot correct nonuniform warping. Scaling also
changes openings and walls, so repeat the fit checks after any adjustment and do
not apply the same compensation again elsewhere. No scale compensation is baked
into these models.

Prusa's [warping guidance](https://help.prusa3d.com/article/warping_2011) describes
corner lifting on large prints and the role of thermal conditions. Its
[support guidance](https://help.prusa3d.com/article/failing-supports_1807) notes
that changing orientation or splitting a model can reduce support requirements.
These are background considerations; physical trials must establish this design's
performance on the user's printer and material.

## Verification from this implementation

The initial empty AI stubs completed the full pipeline before implementation;
their output was empty geometry as expected (`initial_pipeline_check.log`).

The revised trial set passed ten unit tests plus OpenSCAD export and mesh
checks for all eleven AI parts. Each frame/fit/layout is one connected body; the
paired layout contains exactly two. All are watertight, have consistent winding,
positive volume, the expected envelope within 0.03 mm, and begin at Z=0. The
downward-face-angle check found no faces above the bed steeper than the allowed
45-degree support threshold (with numerical tolerance). This is a geometric
screen, not an actual slicing or print test. Mesh checks also check the print
footprint plus margin and the Z build limit where supplied. Unit tests verify
that an additional row or column fails for each printer-specific maximum grid.

Exported-mesh cross-sections at Z=20, 55 and 90 mm check the shelf and its wall
attachment, clearance immediately below the step, open side reliefs, and removal
of the centre rail in full-depth relieved frames. Shallow test pieces are sampled
at half their depth. These checks use actual mesh contours, not just parameter
values. The wide closing roof and end bands remain; removing the centre rail does
not mean removing the entire front/back frame.

The 2 x 2 relieved frame has **47.74% less CAD material volume** than the AI
reference with identical walls, envelope, catches and ears. This comparison is not
against the thinner original `basic` frame and does not establish equal strength.
See `validation_ai_version_1/report.json`, per-part `validation.json`, and the
generated previews for reproducible measurements.

The user's unrefined stepped cutout was first regenerated and measured as a
separate baseline. Compared with that shape, this refinement reduces volume
from 148.05 to 133.50 cm3 for 2 x 2 (9.83%), from 463.38 to 399.10 cm3 for P1P
(13.87%), and from 1498.95 to 1258.67 cm3 for 4 x 12 (16.03%). Fit/layout
profiles and external envelopes match that baseline. See
`validation_ai_version_1/lip_refinement_comparison.json` and
`before_lip_refinement.json`. The earlier straight-sided design's lower volume
is not a like-for-like comparison with the user's new shoulder geometry.
