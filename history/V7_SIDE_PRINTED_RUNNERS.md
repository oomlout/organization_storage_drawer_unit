# V7 side-printed runners — 2026-11-01

Superseded face alignment: `V7_BALANCED_SHARED_RUNNERS.md` centres these
same beam shapes at shared dividers by shifting the receiver holes 1.5 mm.
Multi-column printed faces are now handed, and shared-divider 3 mm pads
have offset holes. Reuse the existing beams/caps/adapters with revised faces.

The current units use a thin running strip with short clip or screw
ends. Dimensions are owned by `get_current_options()` in
`working_oomp_populate.py`. Historical V7 options remain unchanged.

## Geometry and orientation

- Running strip: **8 mm wide x 3 mm thick**, offset **1.5 mm** in +X from the
  receiver axis. The inward limit remains the previous +5.5 mm, avoiding an
  intrusion into the pot-body space. The opposite edge is -2.5 mm.
- The user's proposed off-centre clip permits this wider strip while keeping
  the snap's broad face and runner edge on the same bed plane. The confirmed
  relative turn is **90 degrees**. Manufacturing STLs already have that
  orientation; keep it in the slicer.
- Both beam roofs remain **8 mm above the receiver axis** in service. Existing
  5.2 x 5.2 mm receivers and all three face envelopes are retained. Either
  beam type fits every receiver position.
- The strip stops 0.2 mm short of each inside face. The clip seating strips
  and screw bosses still seat on the faces. This prevents a thin running
  edge coinciding with the existing corner-bore surface in assembly exports.
- Clip grip length is 12 mm. Slot penetration is **5 mm instead of 7 mm**;
  radiused roots, 1.2 mm arms, hook overlap, full-squeeze fit, and friction
  stem dimensions are retained. Conservative free span within the beam is
  2.6 mm, and effective root-to-shoulder span is 8.7 mm (previously 4.6 and
  10.7 mm). These are geometric lengths, not a measured force or strain rating.
- Screw bosses are 12 mm long and 12 mm high. The **OOBB version 5
  `oobb_nut`** gets explicit M3 size, depth, bottom anchor, local position,
  rotation and `clearance='right'`, opening toward local -X / the bed side.
  The axial bore shares the nut's X/Z centre. Part-level transforms and
  anchors are not passed to the nut primitive. Overhang wedges are omitted;
  the side-print orientation has an open loading path and short pocket span.
- The centre stop is 12 mm wide x 3 mm along the beam, extending from -2.5
  to +9.5 mm. Its +X reach stops each drawer column from that column's
  left-hand beam, in both banks. This avoids an unsupported wing below the
  print bed. Keep the supplied assembly orientation.

An offset **11 mm** strip would encroach on one pot-body channel. The selected
8 mm strip retains the old inner limit. Nominal lip bearing on its narrower
side is approximately **0.85 mm**, so lateral play and loading particularly
need physical checks. There is no measured load rating.

## Covers and printing

The turned snap needs its friction cover turned 90 degrees in the panel
plane. A rotated old 11 x 8 mm cover crowds the corner fixing head at some
receivers. The new cover is **9.8 x 8 mm**, with the same depth, 2.6 mm fitted
stem, 0.8 mm pointed nose and friction-only retention. Its narrow rim wall
is nominally 0.7 mm away from the four circular corner reliefs. Those reliefs
clear the corner mounting-head envelope at the lowest plywood receivers.
Print the NEW covers supplied with this revision.
The unchanged external screw adapters, faces, screws and nuts can be reused.

Each active part folder has:

- `beam_replacement_files.zip`: only the required snap, screw and NEW cover
  batches, their self-contained SCADs, assembly metadata, previews and
  `beam_replacement_printing.txt`. Print **each listed STL once**.
- `print_files.zip`: the full manufacturing kit, including faces and the
  existing laser alternatives.
- `sample_71.stl`: optional **revised 5 mm-slot** fit coupon. Its filename
  denotes the original mechanism reference; historical sample 71 remains
  unchanged in the immutable archive.

| Unit | Snap beams | Screw beams | NEW covers | Reused screw adapters |
| --- | ---: | ---: | ---: | ---: |
| 2 wide x 7 tall | 17 | 4 | 34 | 8 |
| 4 wide x 12 tall | 56 | 4 | 112 | 8 |
| 1 wide x 2 tall sample | 4 | 2 | 8 | 4 |
| 2 wide x 2 tall inspection sample | 6 | 3 | 12 | 6 |

The 2x2 inspection sample was added after the original three-unit validation.
It uses the same beams and shows their shared centre positions between
side-by-side drawers: four pots per face, eight total. Generate it with
`python action_generate_current_v7.py --variant unit_2_wide_2_tall`.
Its 19 closed mesh views, five DXFs and 18 mounting combinations pass;
see `validation_v7_2x2/report.json`. The original three units' CAD files
and packages remain unchanged.

Side-load nuts through the bed-side openings **before fitting faces**. Fit
covers from outside in their new orientation. Keep the beam orientation
provided in the files; the one-sided stop reach is intentional. Individual
component files are spares, not extra quantities on top of the batches.

## Regeneration and checks

Run `python action_generate_current_v7.py`. It runs
`working_oomp_populate -> working_oomp -> working_scad`, then binary STL/DXF
exports, fit checks, previews, ZIPs and navigation. Bodies remain in
`working_scad`; all negative tools remain in `working_scad_container_cutout`.
`action_validate_v7_side_runner.validate` extends the full generator with
nut loading/capture and screw alignment, actual 3 mm strip sections, bed
contact, shorter-arm insertion/full squeeze, unchanged friction stem,
drawer-stop reach and outside-part/corner-head clearance. The new covers
clear a 6 mm-diameter mounting-head envelope at every receiver. For the
unchanged screw adapters the validator records non-regression: their
preceding flanges already intersect that generic head envelope at the
lowest outer plywood receivers. Actual enclosure fixing-head dimensions
must suit that existing layout; complete clearance is not claimed there.

Reports are in `validation_v7_side_runner`, including per-unit reports and
the aggregate `report.json`. The preceding active files (223 files) and
their SHA-256 manifest are preserved in `previous_current` and
`previous_current_manifest.json`, with preceding sources alongside. Existing
archives, release locks, historical validation/delivery folders and user
results.csv files remain protected.

The exporter can remove exactly zero-area facets caused by binary float32
rounding only when doing so restores a closed, consistently wound mesh.
This does not change the generated geometry or substitute for source fixes.

CAD checks establish nominal clearance, not insertion effort, friction hold,
printability on a particular machine, runner stiffness, loading or creep.
Test the new short arms, narrower lip bearing and cover rim before a full
cabinet print. The enclosure still supplies drawer-floor support.

Completed validation: **122 source tests, nine comparison tests, 71 closed
mesh views, 19 DXFs, and 174 interchangeable beam/mount combinations (348
ends)** pass. Nut loading and axial capture pass at both ends, as do the
shorter arms' prescribed full squeeze/insertion and unchanged friction-stem
fit. Strip sections, stop reach, bed contact, batch counts/volumes and
full-kit/assembly volumes pass. Faces, adapters and receiver STLs are
byte-identical to the preceding catalogue. All six shared component STLs
are byte-identical across the three new units. All three assembly previews
and the beam comparison were inspected; replacement ZIP counts, bytes,
integrity and self-contained SCADs were checked. Archives and release locks
pass. Solid CAD volume reductions versus the preceding windowed beams are
**53.96% snap / 69.26% screw**; these are not slicer consumption figures.
