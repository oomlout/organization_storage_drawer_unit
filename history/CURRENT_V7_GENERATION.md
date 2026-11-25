# Current V7 generation

Latest finishing revision: stops rise **6 mm above** the runner; screw
beam/adapter share the 6 mm receiver depth **3 + 3 mm nominally** (2.95 mm
actual each with a 0.1 mm gap); new offset-stem covers are centred on the
runners and clear the drawer passage. Print the new beams, covers and
adapters from `finishing_upgrade_files.zip`; reuse balanced faces and
hardware. Reports now go to `validation_v7_finishing`. The two small
samples' top stops project 1 mm above the faces (100.8 mm overall height).
See `V7_FINISHING.md` for details and orientation.

The centred shared receivers remain 1.5 mm in front-face CAD +X, giving
2.35 mm nominal bearing on each side. Multi-column printed faces are
HANDED: use front.stl once and back.stl once. These face shapes are unchanged
by the finishing revision. See `V7_BALANCED_SHARED_RUNNERS.md` for laser
orientation and offset pads. `face_alignment_files.zip` supplies those faces.

Current validation: 128 source tests, nine comparison tests, 93 closed mesh
views, 27 DXFs and 192 beam/mount combinations (384 ends) pass. All 384
outside-fitting/passage checks and 192 cover-centre checks pass. Face/pad/
coupon STLs are unchanged; the four new end components match across units.
See `validation_v7_finishing/report.json`.

Beams retain the side-printed 8 x 3 mm running strip, 5 mm clip slots and
explicit side-clearance OOBB v5 nut pockets. New 9.8 mm square offset covers
and half-depth adapters are required. `beam_replacement_files.zip` is the
same complete beam/lock/adapter upgrade as `finishing_upgrade_files.zip`.
Preceding reports remain in `validation_v7_side_runner` and
`validation_v7_balanced_runner`; their volume figures refer to those revisions.

Taxonomy order is `drawer_unit / container size / column / row / style / variant`.
Active part/source IDs and navigation put the pot before the unit's grid size.

Optional `front_3mm_test_2d.scad/dxf` supplies a 3 mm face with its complete
set of 3 mm inside reinforcing squares nested in the opening waste. It covers
all snap and screw positions and retains 6 mm locally. Shared-divider pads
have +1.5 mm offset holes while their squares stay centred on the dividers. See
`V7_3MM_FRONT_TEST.md` for handed corner pieces, quantities and assembly.

These four units are active in `parts` and `parts_source`:

| Variant | Grid per face | Frame W x H x D (mm) | Drawers total | Snap beams | Screw beams | Friction plugs | Screw adapters / M3 screws / nuts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| double_sided_plywood_250_max | 2 x 7 | 197.8 x 220.3 x 224 | 28 | 17 | 4 | 34 | 8 each |
| double_sided_plywood_395_max | 4 x 12 | 376.4 x 376.8 x 224 | 96 | 56 | 4 | 112 | 8 each |
| unit_1_wide_2_tall | 1 x 2 | 108.5 x 99.8 x 224 | 4 | 4 | 2 | 8 | 4 each |
| unit_2_wide_2_tall | 2 x 2 | 197.8 x 99.8 x 224 | 8 | 6 | 3 | 12 | 6 each |

The samples are one-wide/two-tall and two-wide/two-tall. The 2x2 addition
shows the common beam design at shared centres for side-by-side inspection.
All units have two
opposing banks of Systempak 209 / 100 ml takeaway containers. Overall depth
including friction covers is 233.2 mm. The plywood sizes preserve their
existing face envelopes and use four screw beams at the outer first/last
working-row positions. The samples have two / three separate upper braces.

All use the sample-71 mechanism with shortened 5 mm slots, friction-only
covering plugs with the .8 mm pointed nose, and interchangeable thin-runner
snap/M3 beams. Faces and receiver coupons retain preceding balanced geometry;
beams, covers and screw adapters use the finishing revision.
The new plywood faces have V7 5.2 x 5.2 mm receiver holes; V6 faces are historical.

Run from this project directory:

```powershell
python action_generate_current_v7.py
```

This runs population -> OOMP -> SCAD, exports and validates meshes and DXFs,
renders previews, packages print files and updates navigation. Historical
source functions remain for tests, but normal population and downstream
generation select only the four active units.

To generate/export just the new inspection sample through the same pipeline:

```powershell
python action_generate_current_v7.py --variant unit_2_wide_2_tall
```

The selected finishing report is
`validation_v7_finishing/selected_unit_2_wide_2_tall/report.json`: 20 closed
mesh views, six DXFs and 18 beam/mount combinations (36 ends) pass.
`validation_v7_2x2/report.json` remains the historical inspection-addition
report from before the face-alignment and finishing revisions.

Each part folder contains `print_files.zip`, `printing.txt`, `assembly.json`,
an assembly preview, individual spare parts, and manufacturing batches.
Print front and back once each, and EACH listed numbered batch ONCE.
Do not print spare individual files in addition to the batches. `3dpr` and
`assembled` are reference overviews, not single-bed prints. Large faces and
their batches use the declared 400 mm planning bed; smaller units use the
declared 256 mm bed. Orientations are already supplied.

Alternatively, cut `front_laser_2d.dxf` twice from measured 6 mm MDF. DXFs
declare mm and nominal finished CUT contours; apply measured kerf once in
CAM. MDF does not provide printed inward floor tabs. An enclosure must
support drawer floors, including the lowest level. Enclosure thickness and
joinery are not specified.

The immutable archives are `parts_old_1` (2,552 files), `parts_source_old_1`
(88 records) and `navigation_oobb_old_1` (2,551 files). Their SHA-256 hashes
are in `parts_old_1_manifest.json`; `python action_archive_parts_1.py` verifies
them without changing them. User results.csv files remain in the archives.
The original Windows folders could not be retired automatically; the user
cleared the active locations before the new build was installed. No archived
geometry, release manifest or historical delivery was replaced.

Preceding windowed-beam validation including the optional 3 mm face test: 118 source tests; nine comparison
tests; 71 closed mesh exports; 19 audited DXFs;
174 beam/mount combinations covering 348 ends; bed contact and bounds;
batch counts/volumes; complete kit and assembly volumes; unchanged shared
component STLs and plywood envelopes; all release locks. See
`validation_current_v7/report.json` and `validation_v7_3mm_front/report.json`.
All cut-layout and reinforced-face previews inspected. The 116 preceding active
SCAD/STL files remain byte-identical; test squares clear the bins and corner
bores, cover every receiver, and maintain the nominal 6 mm local stack.
These are CAD checks; assembled loads, print fit and creep need physical tests.
