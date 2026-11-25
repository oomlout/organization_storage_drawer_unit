# Current V7 generation

Taxonomy order is `drawer_unit / container size / column / row / style / variant`.
Active part/source IDs and navigation put the pot before the unit's grid size.

Optional `front_3mm_test_2d.scad/dxf` supplies a 3 mm face with its complete
set of 3 mm inside reinforcing squares nested in the opening waste. It covers
all snap and screw positions and retains 6 mm locally. See
`V7_3MM_FRONT_TEST.md` for handed corner pieces, quantities and assembly.

Only these three units are active in `parts` and `parts_source`:

| Variant | Grid per face | Frame W x H x D (mm) | Drawers total | Snap beams | Screw beams | Friction plugs | Screw adapters / M3 screws / nuts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| double_sided_plywood_250_max | 2 x 7 | 197.8 x 220.3 x 224 | 28 | 17 | 4 | 34 | 8 each |
| double_sided_plywood_395_max | 4 x 12 | 376.4 x 376.8 x 224 | 96 | 56 | 4 | 112 | 8 each |
| unit_1_wide_2_tall | 1 x 2 | 108.5 x 99.8 x 224 | 4 | 4 | 2 | 8 | 4 each |

The sample is the existing one-wide/two-tall design. All units have two
opposing banks of Systempak 209 / 100 ml takeaway containers. Overall depth
including friction covers is 233.2 mm. The plywood sizes preserve their
existing face envelopes and use four screw beams at the outer first/last
working-row positions. The sample retains its two separate upper braces.

All use the selected sample-71 interface, friction-only covering plugs with
the .8 mm pointed nose, and interchangeable windowed snap/M3 beams. Shared
individual component STLs are byte-identical to the archived current sample.
The new plywood faces have V7 5.2 x 5.2 mm receiver holes; V6 faces are historical.

Run from this project directory:

```powershell
python action_generate_current_v7.py
```

This runs population -> OOMP -> SCAD, exports and validates meshes and DXFs,
renders previews, packages print files and updates navigation. Historical
source functions remain for tests, but normal population and downstream
generation select only the three active units.

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

Validation including the optional 3 mm face test: 118 source tests; nine comparison
tests; 71 closed mesh exports; 19 audited DXFs;
174 beam/mount combinations covering 348 ends; bed contact and bounds;
batch counts/volumes; complete kit and assembly volumes; unchanged shared
component STLs and plywood envelopes; all release locks. See
`validation_current_v7/report.json` and `validation_v7_3mm_front/report.json`.
All cut-layout and reinforced-face previews inspected. The 116 preceding active
SCAD/STL files remain byte-identical; test squares clear the bins and corner
bores, cover every receiver, and maintain the nominal 6 mm local stack.
These are CAD checks; assembled loads, print fit and creep need physical tests.
