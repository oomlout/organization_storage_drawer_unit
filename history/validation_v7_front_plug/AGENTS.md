# Drawer unit project guidance

## User intent and required pipeline

This project makes drawer units whose removable drawers/inserts are takeaway
containers. The container type for each unit/shelf definition belongs in
`working_oomp_populate.py`.

Always preserve the generation sequence requested by the user:

`working_oomp_populate` -> `working_oomp` -> `working_scad`

Make changes in the responsible source stage and carry them through the pipeline.
Do not substitute hand-edited generated YAML, SCAD, or STL files for source changes.
Keep these notes current as the design evolves. The baseline below was inspected
on 2026-10-18; it records existing behavior, not a requirement to retain every
dimension or experimental feature.

## V7 permanent full-squeeze snaps, physical feedback revision (2026-10-31)

The user reports all clip-in hooks insufficiently aggressive and all tested
receiver holes too large. They explicitly request that the TWO MIDDLE ARMS
press COMPLETELY TOGETHER when passing the hole, for a PERMANENT ONE-TIME USE
fitting. No failure load or fracture result was reported. Population's fourth
V7 record, `permanent_full_squeeze_snap_test`, owns samples 60 straight,
61 tapered and 62 S-shaped. This is one common revised fit, not a size matrix.

New holes are 5.2 x 4.2 mm (previous 6.0 x 4.6); neck is 4.8 x 4.0. Hooks
project 1.4 mm per side (previous .8), giving 7.6 mm recovered head width and
1.2 mm retaining overlap per side. The 1.2 mm-thick tips have a 2.4 mm centre
gap; each MUST close inward 1.2 mm until actual contact. Closed head width
equals the 5.2 mm opening. Do not reuse the older +.1 mm prescribed-flex
margin: that would interpenetrate the arms. The .8 mm lands and .15 mm
back-raked shoulders have no designed release ramp or release pads. Nominal
axial allowance is .1 mm; tip exposure is about 2.4 mm. Intended one-time use
is NOT proof that removal requires damage: tools may still reach exposed hooks.

Print `3dpr.stl` once (three specimens) plus NEW `receiver_6_0.stl` once. `6_0`
means 6 mm panel thickness; its openings are now 5.2 x 4.2. Old receivers are
not the revised fit. Receiver has three identical numbered holes and matching
MDF DXF. Individual samples are spares. Record arm contact, click/effort, play,
destructive-pull outcome and failure location; preserve results.csv.

Bodies/removals remain in the ordinary source stages. Always populate -> OOMP
-> SCAD. Use `python action_validate_v7_permanent_snap.py`; reports go in
`validation_v7_permanent_snap/`, delivery in `output_v7_permanent_snap/`.
Read `AI_VERSION_7_PERMANENT_SNAP.md`. Its immutable `previous_v7_baseline.json`
protects all three earlier V7 inputs and 118 SCAD/STL/ZIP files; copies live in
`previous_parts/`. All V1–V6 locks remain mandatory. No full cabinet fit is
selected. Physical force, permanence, PETG creep and MDF damage remain open.

Completed: 102 source tests, nine comparison tests, five closed mesh exports
and one DXF pass. Actual arm-tip gap is below .000001 mm at full closure,
with zero measured arm-intersection volume. All three closed heads measure
5.2 mm and pass insertion; 95% closure is blocked by about .397 mm³ of receiver
interference. Seated fit, retaining/seating contact, tighter vertical fit,
piece counts, bed contact, kit volume and DXF contours/units pass. Three prior
V7 records / 118 files and V1–V6 locks are unchanged. All new previews were
inspected, including the two closed arms shown independently before 2D union.
Physical destructive pull tests must establish permanent retention.

## V7 rigid loop with a vertical drop key, sample 54 (2026-10-31)

The user also requested a simple loop with a key dropped into it FROM ABOVE.
Population's third V7 option is `loop_drop_key_mechanism_card`: it retains
50–53 and the screw reference, then adds rigid sample 54 and a separate T key.
54 has NO snap arms. Its 5.5 x 4.0 mm neck passes through the SAME 6.0 x 4.6 mm
hole; the exposed eye takes the key vertically, perpendicular to the beam.
The head stops the key falling through; the stem crosses the panel opening
and bears against the outside face to prevent withdrawal. Lift UP to release.

Loop eye is 2.4 x 2.2 mm, side walls 1.55 mm, nose 1.5 mm. The key stem is
2 x 2 x 7 mm, head 7 x 2 x 1.6 mm. Nominal axial play is .25 mm and loop
projection is 3.75 mm. The key is loose/gravity-seated, with no anti-loss
detent; overhead access and drawer/front clearance need checking before adoption.
There is no load rating or measured insertion/retention result.

The combined `3dpr.stl` contains five numbered samples plus TWO keys: seven
pieces. Its receiver is 150 x 32 mm with SIX identical holes, 50/51/52/53/54/M3.
Existing four-finger receivers remain compatible. For an existing tester,
`loop_key_addon.stl` contains ONLY sample 54 and its T key, two pieces; do not
also print these from the full combined card. Both keys print flat, then are
turned to their different service orientations. Results.csv stays user-owned.

Always populate -> OOMP -> SCAD. Run `python action_validate_v7.py --variant
loop_drop_key_mechanism_card`; reports go in `validation_v7_loop_key/`, files
in `output_v7_loop_key/`. `loop_key_addon.zip` is the quick addition;
`v7_mechanism_card_with_loop_key.zip` is the full comparison. Read
`AI_VERSION_7_LOOP_KEY.md`. Prior four-finger inputs and SCAD/STL/ZIP files
are preserved by `previous_four_finger_baseline.json` and `previous_four_finger/`;
never refresh those to pass changes. First V7 and V1–V6 locks also remain.

Completed: 99 source tests, nine comparison tests, 17 closed mesh exports and
three DXFs pass. Rigid loop insertion, vertical key drop/lift, head fall-through
stop, outside-panel bearing and positive withdrawal capture pass. Add-on and
full-card piece counts, bed contact and volume conservation pass. All previous
V7 files (45 five-finger / 33 four-finger) and 64 prior AI records / 613 geometry
files remain unchanged. New loop, combined-print and receiver previews were
inspected. Physical fit, force, key retention, MDF wear and loading remain open.

## V7 four-finger mechanism comparison (2026-10-31)

The user rejected the fixed middle tongue and requested thicker outer fingers,
a narrower hole, and DIFFERENT TECHNIQUES rather than a size/clearance matrix.
The second V7 option is `four_finger_mechanism_card`; the original 40–48 record
remains historical and unchanged. Its original inputs and 45 SCAD/STL/ZIP files
are protected by `validation_v7_four_finger/previous_five_finger_baseline.json`
and copied to `previous_five_finger/`. Never refresh that baseline to pass changes.

Population owns four techniques: 50 straight cantilevers, 51 tapered arms
(1.8 mm root / 1.2 mm tip), 52 S-shaped spring arms, and 53 straight snaps with
a separate removable blocking key. Keep the interface common while comparing
mechanisms: all five holes are IDENTICAL 6.0 x 4.6 mm, labelled 50/51/52/53/M3;
necks are 5.5 mm, axial clearance .25 mm, hook overlap .55 mm per side and
clip tip exposure about 1.84 mm. There is NO permanent centre tongue. Two
hooked inner arms pass through; two outer seating strips stop inside. The
strips grow from about .95 to 1.75 mm (slightly thinner at rounded roots).
Do not add another clearance matrix until the mechanism comparison is done.

`3dpr.stl` contains FOUR clips + ONE separate key, five print bodies. Print
`receiver_6_0.stl` and `screw_test.stl` once each. Individual sample/key files
are spares. Receiver is also supplied as the matching MDF DXF. The optional
key is inserted AFTER snapping 53 in and blocks inward hook movement; remove
it before release. It is a loose removable key with no captive/anti-loss
retention, not a force-free expansion mechanism, and projects about 3.2 mm.
The screw adapter uses the SAME narrower hole, with 5.7 mm guide width,
OOBB M3 countersink/nut and M3 x 20 screw. Verify its narrower cheeks physically.

Always populate -> OOMP -> SCAD. Run `python action_validate_v7.py --variant
four_finger_mechanism_card`. Reports/deliverables are separate under
`validation_v7_four_finger/` and `output_v7_four_finger/`. Protect results.csv.
See `AI_VERSION_7_FOUR_FINGER.md`. Front-face prototypes retain the two earlier
manufacturing paths but use the common narrower hole. No full rail is selected.
Geometry probes do not establish force, fatigue, MDF wear or key retention.

Completed: 96 source tests, nine comparison tests, 14 watertight mesh views and
three DXFs pass. All four nominal snaps, four-finger/open-centre sections,
seating and retaining contact, prescribed insertion, key insertion/release
blocking and screw/nut paths pass. Mesh sections distinguish tapered/curved
concepts from the control; 53 retains the control snap with a separate key.
Both grids have all 21/60 narrower receivers. DXF audits and contour matching
pass. V1–V6 locks and all 45 first-card files remain unchanged. All six preview
types were visually inspected. Physical fit, force and durability await tests.

## V7 first five-finger clearance trials, historical (2026-10-31)

The user explicitly requested locking the current design and advancing one
version BEFORE new work. `releases/ai_version_6/manifest.json` now locks the
64 preceding AI records and 613 geometry files, including current V6 STL/ZIP
files. It also hashes copied V6 source/part snapshots. Run
`python action_lock_version_6.py` to verify; NEVER refresh that manifest to
accommodate later geometry. V7 is independent experimental development.

The user confirmed 6 mm MDF and explicitly requested a printable receiver.
Population owns `get_ai_version_7_options()`: one connector-test record,
samples 40–48 crossing 1.2/1.5/1.8 mm nominal arm thickness with .10/.25/.40 mm
axial allowance. Straight 7.6 x 4.6 mm holes replace internal latch pockets.
Arms extend into the beam, with rounded reliefs, rigid bearing strips and a
centre pilot. External hooks project about 1.69–1.99 mm; their actual physical
minimum/strength is unverified. No sample is selected for complete V7 rails.

`3dpr.stl` has nine numbered clips. `receiver_6_0.stl` is the requested printable
receiver; optional 5.8/6.2 mm receivers check thickness sensitivity. Its five
hole widths are 7.2/7.4/7.6/7.8/8.0 mm, all 4.6 mm high. `receiver_laser.dxf`
cuts the corresponding card from MDF. DXFs use nominal finished mm contours;
apply measured kerf once in CAM. `screw_test.stl` has one beam end plus outside
adapter for the SAME hole, with side-loaded OOBB M3 nut and M3 x 20 countersunk
screw. `results.csv` belongs to the user and must never be overwritten.

Prototype front faces for BOTH current grids demonstrate the two fabrication
paths: laser faces have solid stop outlines across 6 mm; printed faces retain
the angled slide-on stops and 12 mm floor extensions (18 mm total). Flat MDF
cannot supply those inward floor extensions; enclosure/support design remains
an explicit dependency. These are prototypes, not a full V7 cabinet release.
Do not pad the current rectangular grids into a square without clarification.

Bodies live in `working_scad.get_ai_version_7`; complete removals live in
`get_container_cutout_ai_version_7`; metadata/projection sources live in
`working_scad_v7.py`. Always populate -> OOMP -> SCAD. Use
`python action_validate_v7.py`; reports go in `validation_v7/`. The test-card
ZIP and prototype-face ZIP are separate. See `AI_VERSION_7.md` for research,
tradeoffs, test sequence and limitations. Preserve all V1–V6 inputs, releases,
historical tests and generated CAD. Continue testing before selecting a clip.

Completed validation: 93 source tests, nine comparison tests, 20 closed mesh
views and three DXFs pass. Nine seated joints, thickness response, sample 44
in all five calibration holes, prescribed insertion, retaining/seating contact,
rigid screw adapter insertion, full bore path and side-loaded nut capture pass.
Both prototype grids have all 21/60 receiver holes. DXF boundaries agree with
flat meshes within .0011 mm of export rounding; files declare mm, use closed
CUT contours and have no duplicate segments. All 64 previous models / 613
geometry files remain locked. All six new preview types were inspected.
Physical PETG fit/force, cycling, MDF edge durability, creep and full cabinet
support/loading remain unverified.

## V6 four screw rails with external countersunk adapters (2026-10-23)

The user requests a beam fastened through the SAME snap receiver using a
small front adapter and side-loaded OOBB nut, with FOUR screw rails replacing
four snaps in EACH active kit. Population owns `screw_rail_settings`; the
four locations are the outermost X mounts at first/last working shelf rows.
Small unit: 17 sample-37 snaps + 4 screw rails. Large: 56 snaps + 4 screw rails.
Each screw rail fastens at BOTH ends: eight adapters, eight M3 x 20 countersunk
screws and eight M3 nuts per cabinet. Never cut the old direct-screw receiver:
these positions use connection `screw_adapter`, preserving the snap hole.

Front/back plates, sample-37 snap rails and optional joiners remain
byte-identical. The new screw rail is 212 mm long between the plate faces,
with the same running shelf and centre stop. Its ends are 13 mm high around
the nut pockets. OOBB M3 nut pockets are 7-10 mm inward, with `overhang=True`
and `clearance='left'` (local +X side-loading). The screw bore extends past
the full M3 x 20 shank; nominal screw projection beyond the nut pocket is
1.6 mm. Retained channel roof/floor and opposite wall are checked.

Each adapter has an 11 x 10 x 2.4 mm external rounded flange, standard OOBB
M3 countersink and two 1.5 mm-wide locating cheeks projecting 5.5 mm into the
6 mm plate. The rigid guide stays within the narrow OUTSIDE throat for its
whole depth, with .5 mm tip chamfers. Do NOT expand it to match the inside
bevel: such a nose cannot be inserted from outside. The centre is open through
the cheeks to avoid fragile top/bottom bore slivers; the flange's circular
bore guides the screw. Print outside flange/countersink face DOWN, cheeks UP.
The flange adds 2.4 mm outside each face: structural frame depth stays 224 mm,
but the full plastic assembly including adapters is 228.8 mm deep.

Bodies remain in `working_scad`; all removals remain in the v6 cutout, using
OOBB countersink/nut primitives. Metadata/printing instructions are emitted
by `working_scad_double_sided`. Historical 30-38 kit inputs and CAD remain
unchanged: its population reference removes both selection and screw settings.
Always populate -> OOMP -> SCAD. `action_validate_double_sided_v6.py` now
writes to `validation_double_sided_v6_screw_adapter/<variant>/`; its immutable
`previous_models_baseline.json` preserves eighteen preceding v5/v6 records,
and `previous_parts/` stores the old faces and snap rails. Prior reports,
snapshots and releases remain intact.

`rails_plate_*.stl` now contain the MIXED rail quantities; print each batch
once, plus `screw_adapters.stl` once for eight adapters. Individual screw rail
and adapter files are spares. Alternative `screw_upgrade.stl` contains exactly
four screw rails + eight adapters in one 157.5 x 212 mm print, identical for
both sizes, to retrofit an existing all-snap unit. Do NOT print it on top of
the full mixed kit. `print_files_screw_adapter.zip` contains all print files,
the alternative upgrade, optional joiners and assembly/printing metadata.
The older sample-37 ZIP remains a historical all-snap kit.

Validation passes 88 source tests, nine comparison tests and 27 mesh exports.
All 81 actual rail positions and eight adapters per unit fit. Closed meshes,
piece counts, bed limits, unchanged faces/snaps/old models and assembly volume
conservation pass. `validation_v6_screw_geometry.py` probes rigid adapter
insertion from outside, flange/beam seating stops, countersink flare, full
screw/head paths using OOBB true dimensions, both nut side-loading paths and
axial capture, guide cheeks, retained nut walls and centre stops. New adapter,
joint and kit previews were inspected. Physical screw fit, tightening torque,
print bridging, PETG strength and full-unit loading remain unverified.
See `V6_SCREW_RAILS.md`.

## V6 adopts physically preferred sample 37 on full rails (2026-10-23)

The user selected sample 37 as best and requested all full-length latches
updated plus regenerated face plates for BOTH active sizes. Population now
sets `selected_latch_sample=37` on the 250/395 frame definitions. This means
.05 mm hook-pocket side clearance and .10 mm axial end play, with 1.4 mm
hook projection and 4.4 mm shoulder depth. Apply to BOTH ends of every long
rail and every rail batch. The 1.8 mm arms, root reliefs, tip position,
bearing strips, 212 mm rail length, centre stops and cabinet sizes remain.
Record the user's preference as qualitative physical fit feedback only.

The receiver remains the one used in the successful test: do not alter
`snap_hook_projection`, `snap_shoulder_depth`, `snap_clearance` or the frozen
profile just to apply the rail adjustment. `get_ai_version_6_parameters`
derives a separate `selected_rail_fit`; only rail cuts consume its hook/shoulder
values. Front/back SCAD and regenerated STL are byte-identical to the prior
solid-web plates. Existing plates remain compatible. The requested face
files, assemblies and batches are regenerated through populate -> OOMP -> SCAD.

Keep the numbered 30-38 kit unchanged, including its nested original frame
reference. Its population function explicitly removes the new selection field
from that reference; otherwise adopting 37 would silently move the historical
baseline. The fifteen v5 records, numbered coupons and old releases remain
unchanged. Earlier per-phase validators/reports describe their historical
geometry; do not rewrite their immutable snapshots to pass a later revision.

Current main validation is `action_validate_double_sided_v6.py`, with each
`--variant`, writing under `validation_double_sided_v6_selected_37/<variant>/`.
Its immutable `previous_models_baseline.json` preserves all eighteen prior
v5/v6 inputs and SCAD; `previous_parts/` holds the prior full rails and faces.
It checks unchanged plates/joiners and historical kit, both rail ends against
the actual sample-37 mesh (only filling its number), unchanged rail bodies and
stops, selected free travel/retention against both faces, all seated rail
positions, batches, web/support geometry and prescribed-flex insertion.
`print_files_sample_37.zip` in each active part folder contains front/back,
all rail batches, a spare rail, optional joiners and printing/assembly metadata;
it excludes oversized overview and assembled reference files.

Validation passes 84 source tests, nine comparison tests and nineteen exported
mesh views across both sizes. All 81 seated rail positions, both matching
sample-37 ends, free travel, retaining contact and prescribed insertion pass.
Both regenerated face STLs match their previous hashes. Rail/assembly previews
were inspected. Full-assembly PETG fit, loading and creep remain unverified.

## V6 quick numbered latch-clearance suite, unchanged receiver (2026-10-23)

The user reports that the current v6 latch is LOOSE AFTER CLICKING IN; no
fracture or strength result was reported. They request quick numbered
clearance trials while leaving the receiving hole unchanged. Population adds
one `latch_clearance_suite` connector-test record, separately from the two
frame options. `get_ai_version_6_clearance_trials()` owns samples 30-38:
hook-pocket side clearance .25 / .15 / .05 mm crossed with axial end play
.20 / .10 / .05 mm. Sample 30 matches the production v6 rail end. Sample 38
is tightest in both directions. All values are nominal CAD clearances.

Only recovered hook reach (1.2 / 1.3 / 1.4 mm) and retaining shoulder depth
(4.5 / 4.4 / 4.35 mm) vary. Arm-body side and vertical clearance stay .25 mm;
1.8 mm arms, outer arm faces, root slots, bearing strips and flush tips stay
unchanged. Wider hooks require more prescribed insertion flex (.95-1.15 mm).
This is a fit experiment, not a strength improvement claim. Do not adopt a
sample in full rails until the user selects it. Both cabinets and receivers
remain unchanged.

`3dpr.stl` contains nine 11 x 20 x 10 mm single-ended rail grips in one
43 x 70 mm bed layout, with .5 mm recessed numbers on the solid grip. Test
against an existing v6 plate; no receiver needs printing. `sample_30.stl`
through `sample_38.stl` allow individual replacements. `control_rail.stl`
is an unnumbered CAD-validation reference, excluded from the nine-piece kit.
Print the supplied long-face-down orientation with the production PETG
settings. `results.csv` is never overwritten by regeneration.

Bodies remain in `working_scad`; all cuts are in the v6 cutout, reusing the
selected tiled cuts. A flagged rail-only hook override occurs AFTER reading
the locked v5 profile and does not change historical coupons. Metadata lives
in `working_scad_v6_clearance.py`. Always populate -> OOMP -> SCAD. Run
`python action_validate_v6_clearance.py`. Its immutable
`validation_v6_clearance/previous_models_baseline.json` protects all seventeen
preceding v5/v6 inputs and SCAD views, alongside existing release locks.

Validation passes 83 source tests, nine comparison tests and eleven mesh
views. The unnumbered control matches a clipped production rail; sample 30
differs only by its number. All nine samples seat without collision in the
actual existing front-plate mesh, retain the same spring/root sections,
have the prescribed free side/end travel and then positive retaining contact,
and pass prescribed-flex insertion. The nine-piece count, bed contact,
engraving depth and small envelope are checked. Both previews were inspected.
Solid CAD PETG mass is about 17.7 g for the kit, not a slicer estimate or
print-time prediction. Physical fit/retention await the user's results.
See `V6_LATCH_CLEARANCE_TESTS.md`. Catalogue: 66 printed and 15 purchased
records; the new connector kit is hidden from complete-unit comparisons.

## V6 solid lower opening web and matched radii, BOTH sizes (2026-10-23)

The user clarified that the unwanted gap was the full-width 1 mm relief at
the bottom of each opening, BELOW the snap catches. This is separate from
the receiver-floor web correction below. Both active v6 sizes now set
`body_extension_height=0.0`, joining the lower shoulders to the crossbar.
Population also owns `body_cutout_radius=1.0`; the lower body cutout now
matches the upper rounded rectangle's 1 mm radius, replacing its 4 mm radius.
Keep the inherited R4 planning input until the frozen v4/v3 reference mapping
has been read; `get_ai_version_6_parameters` then applies the v6-only radius.
Do not change frozen geometry to implement this correction.

Both compact envelopes, floor tabs, 18 mm overall faces and corner holes
remain. Rails and optional joining plates are byte-identical to the preceding
floor-tab revision; that revision's matching rails remain compatible.
Continue populate -> OOMP -> SCAD. Current reports are under
`validation_double_sided_v6_solid_lower_web/<variant>/`; its immutable
`previous_v6_baseline.json` and `previous_parts/` preserve the preceding v6
inputs and geometry. Older reports and baselines remain unchanged.
Actual mesh probes check the filled former slit at every mount and distinguish
the R1 lower corners from the old R4 corners. `receiver_detail.png` shows the
solid lower web. Validation passes 79 source tests, nine comparison tests,
19 exported mesh views and all 81 seated rail fits, including prescribed snap
insertion/retention. Prior releases and all fifteen v5 records remain unchanged.
Both face previews and the receiver close-up were inspected. Physical PETG fit
and loading remain unverified.

## V6 twin floor tabs and continuous snap web, BOTH sizes (2026-10-22)

The latest user request supersedes the earlier solid face catches for BOTH
`double_sided_plywood_250_max` and `double_sided_plywood_395_max`. Keep their
compact XY dimensions, 28 / 96 pot counts, 224 mm outside depth, corner holes,
and optional joining plates. The face WEB is still 6 mm; integral supports
project 12 mm inward, giving 18 mm OVERALL printed face depth. Do not make the
entire base slab 18 mm or change the rail length/cabinet depth to accommodate it.

Each original 56 mm-wide stop is now TWO 15 mm-wide tabs at the original
outer ends, with the middle 26 mm removed. Tabs underneath a drawer floor
have flat service bearing roofs, bed-rooted 45-degree undersides, 2 mm thin
inner sections and 0.75 mm tip tapers. The 6.8 mm root ramp narrows upward
from the bed. Each successive rib layer is nested, with no floating underside.
No added extension sits under the PHYSICAL BOTTOM drawer floor; plywood
supports that floor. A tab rooted at the next row's top bears on the floor
above. Topmost stops are split/tapered but only 6 mm deep because there is no
drawer above the cabinet top. Floor-tab counts per face are 24 / 88.

The wide T is the TOP of every drawer: CAD NEGATIVE Y is service UP. Earlier
assembly previews were upside down. Presentation scenes now rotate -90 degrees
about X (not +90); the source print files remain flat, outside face on the bed.
`support_detail.png` shows the two tab profiles and open centre.

The user also requested eliminating the tiny web gap at the snap mounts.
The old inner receiver floor reached below the lip shelf and cut its web away.
V6 now keeps a continuous 1 mm strip at every snap across the entire 6 mm web.
The receiver floor runs from 5.75 mm at the outside to 1.0 mm at the inside;
matching rail undersides run from 6.0 mm at the tip to 1.25 mm at the root,
retaining 0.25 mm vertical clearance. Tips still finish flush, with 4 mm tip
height; arm thickness, 6.5 mm root-to-shoulder span and relief slots remain.
Use matching NEW rails with the new plates; previous rails hit the added web.
This is v6-only: v5/coupon bevels and historical geometry stay unchanged.

All controls belong to population: `floor_support_tab_width=15`,
`floor_support_projection=12`, `floor_support_thickness=2`,
`floor_support_tip_chamfer=.75`, `snap_inner_web_height=1`. Positive envelopes
live in `working_scad`; complete rib and matching receiver/rail cuts live in
the v6 cutout, with v6-only conditional floors in the shared tiled primitives.
Always populate -> OOMP -> SCAD. Current reports live under
`validation_double_sided_v6_floor_supports/<variant>/`. The immutable
`previous_v6_baseline.json` and `previous_parts/` preserve both preceding v6
inputs/CAD/previews. Prior validation reports and all old baselines remain
historical; the earlier '250 CAD unchanged' rule does not apply to this
explicitly requested change to BOTH units. Joining plates remain unchanged.

Validation passes 78 source tests, nine comparison tests, nineteen unit mesh
views across both sizes and the two unchanged optional joining components.
All 81 rail joints, new receiver webs, floor tabs, corner holes, prescribed
insertion/retention and release locks pass. Front/back SCAD is identical in
each size. Correctly oriented assembly, face and support-detail previews were
inspected. The validator checks actual tab widths/clear centres,
flat bearing roofs, tapered profiles, bottom omission, no new floating flat
undersides, 18 mm envelopes, continuous webs at every mount and matching
rail insertion/retention. All v1-v5 releases/records remain protected. CAD
face volumes fall approximately 12.7% / 14.0%; this is solid geometry, not a
slicer mass or strength claim. Physical PETG fit, floor contact, snap force,
loading and slicing still need verification.

## V6 compact 395 mm maximum addition (2026-10-22)

The user requested another unit for a 395 x 395 mm maximum face, retaining the
compact style instead of adding a border to make it square. Population adds
`double_sided_plywood_395_max` alongside the unchanged 250 mm record. Its
largest upright grid is four columns x twelve rows PER FACE: 96 Systempak
209 / 100 ml pots total. Finished face plates are 376.4 x 376.8 x 6 mm;
assembled frame depth remains 224 mm. There is no scaled tray geometry or
extra square padding. Five columns need 465.7 mm; thirteen rows need 408.1 mm.

Both faces retain the compact 2 mm top/bottom edges, 10.5 mm side bands and
four plain M3 corner holes, 5 mm from adjacent outside edges (centres X
+/-183.2, Y +/-183.4 mm). There are sixty identical snap rails, supplied in
four batches of 16 + 16 + 16 + 12. Individual rail and combined four-/two-unit
joining-plate SCAD/STL are byte-identical to the 250 mm version. Keep the same
middle stops, flush snaps, 1.8 mm arms, relief slots and retaining clearances.
Joiner pitch still assumes touching plastic unit edges, not unknown plywood
gaps. Plywood thickness is additional to the plastic frame dimensions.

The large record uses a generic 400 x 400 mm planning area, 2 mm margin and
no machine-specific exclusion; this is not a verified printer profile. Largest
rail batch is 379 x 224 mm; faces are 376.4 x 376.8 mm. Every individual print
file fits inside 395 x 395 mm. The one-piece faces exceed the P1P and A1 mini;
use an appropriate larger printer. No tiles or ears. The oversized complete
kit overview uses wider spacing so its 62 components do not merge.

Always populate -> OOMP -> SCAD. Run
`python action_validate_double_sided_v6.py --variant double_sided_plywood_395_max`.
This writes to `validation_double_sided_v6_395_max/`, whose immutable
`previous_250_baseline.json` protects all smaller-unit inputs and SCAD. Keep
all prior snapshots unchanged. The default validator still selects the 250 mm
unit explicitly. Older v5 and release locks remain mandatory. See
`AI_VERSION_6_DOUBLE_SIDED.md`. Validation passes 76 source tests, nine drawer
comparison tests, ten mesh exports, all sixty rail fits, 96 pot positions and
eight corner holes. Individual files also fit within 395 mm with 2 mm margins.
Smaller v6 input/SCAD, all fifteen v5 records and earlier releases are unchanged.
Assembly and face previews were inspected. Physical PETG fit, loading and
slicing remain unverified.

## V6 optional countersunk joining plates (2026-10-22)

The user requested a 6 mm-thick four-hole component joining four units at a
corner, a two-unit version, and BOTH pieces in the same file. The active v6
folder now includes `joining_plates.scad` / `joining_plates.stl`, containing
one 20 x 20 x 6 mm four-unit plate and one 20 x 10 x 6 mm two-unit plate.
The print layout is 45 x 20 mm with a 5 mm gap between the two separate solids.
Print flat backs down and countersinks up. Both use plain M3 through-clearance
and OOBB countersinks: 3.6 mm bores, 7.2 mm head mouths, 1.9 mm head depth.

Holes are on a 10 mm pitch, matching the 5 mm-inset existing cabinet corner
holes when plastic unit face edges touch. A 2 x 2 group uses four holes at
X/Y +/-5 mm; the two-unit strip uses X +/-5, Y=0. Rotate the strip 90 degrees
for vertically adjacent units. Their 10 mm reach into each cabinet stays
inside the 10.5 mm side bands, keeping drawer openings clear. Mount these
on the outside faces with countersunk M3 screws and suitable backing/nuts.
Physical head seating, PETG strength and screw length remain to be verified.

Population owns thickness, edge distances, layout gap and `joining_plate_unit_gap`
(default zero). Plywood spacing BETWEEN plastic faces would require increasing
this gap; do not claim the default bridges unknown plywood wall thicknesses.
Bodies are in `working_scad.get_ai_version_6`, cuts in the v6 cutout, and view/
print metadata stays in `working_scad_double_sided.py`. These are optional
accessories, not extra pieces in the single-unit BOM, `3dpr` kit or assembled
reference. Keep both optional joiners together in their one STL.

`action_validate_v6_joining_plates.py` runs populate -> OOMP -> SCAD and checks
both closed connected meshes, 6 mm thickness, bed contact, six through-bores
and flaring countersinks, corner alignment and material around the seats.
Its immutable `validation_v6_joining_plates/previous_v6_scad.json` preserves
all nine existing v6 SCAD views; all prior v5 inputs/CAD and release checks
also pass unchanged. The combined print preview was inspected. Current
source tests: 74 pass. The main v6 validator also exports the optional file.

## V6 compact plywood-mounted unit, 250 mm maximum (2026-10-22)

The user corrected the 300 mm square: all frame dimensions must be below
250 mm, and the enclosure must shrink around the actual drawer grid rather
than padding it to a square. Population's `get_ai_version_6_options()` now owns
`double_sided_plywood_250_max`: two columns x seven rows PER FACE, 28 Systempak
209 / 100 ml pots total. Finished plastic frame is 197.8 x 220.3 x 224 mm.
The 6 mm face plates are identical. This is a rectangular plywood enclosure,
not an enforced geometric cube. Plywood thickness/joinery and its resulting
outer dimensions are not included; the user is supplying the surrounding box.

Openings remain 87.5 x 28.5 mm at 31.3 mm row pitch. Top/bottom structural
bands are reduced to 2 mm, retaining the original 1.8 mm wall minimum. The
10.5 mm side bands enclose the outside snaps, stop wings and corner fittings.
There is no surplus square border. Three columns need 287.1 mm; eight rows
need 251.6 mm at the current compact edges (251.2 mm at minimum 1.8 mm edges).
Do not reduce the established clearances or row spacing to squeeze in a row
without an explicit request.

Four plain OOBB M3 clearance holes go through EACH plate, 5 mm from both
adjacent outside edges. Hole centres are X +/-93.9, Y +/-105.15 mm, measured
from plate centre. These eight external mounting holes secure the plates to
plywood. They are separate from the snap joints; no countersinks or nut seats
are added. Screw length and plywood construction remain user supplied.

There are 21 identical rails: three column boundaries x seven working shelf
levels. Rails remain 212 mm between plates, with flush 6 mm sample-28 tips,
1.8 mm arms and all existing bevels/relief slots/bearing strips unchanged.
Each rail's integral stop is now 19 x 10 x 3 mm so the outside wings stay
inside the narrower frame. It reaches past the body shoulders into the pot
channel. Stop faces remain at 110.5 and 113.5 mm from one outer face, leaving
109 mm pot depth plus 1.5 mm allowance for EACH opposing bank. Both exterior
tray catches remain. Top/bottom brace rails remain omitted.

Planning reuses the established P1P 256 mm bed, 2 mm margin and 18 x 28 mm
cutter exclusion. Front/back plates and the 9 + 9 + 3 rail batches each fit
this envelope. Keep generated rail poses and check brim additions. The face
plates still exceed the A1 mini bed. There are no tiles, ears or filler panels.

Always populate -> OOMP -> SCAD. Bodies live in `working_scad.py`, removals
in `get_container_cutout_ai_version_6`, and metadata in
`working_scad_double_sided.py`. `action_validate_double_sided_v6.py` writes to
`validation_double_sided_v6_250_max/` and keeps checking the original immutable
`validation_double_sided_v6/previous_v5_baseline.json`. Do not overwrite it.
The superseded 300 mm part and source records are recoverable under
`validation_double_sided_v6/superseded_300_mm/`; they are removed from the active
catalogue. Earlier v5 and release geometry must remain unchanged.
Validation passes 72 source/geometry tests, nine comparison tests and eight
exported mesh views. All 21 seated joints, snap insertion/retention, 28 pot
positions, eight corner through-holes and P1P envelopes pass. The 15 previous
v5 records and all earlier release checks pass unchanged. Assembly and face
previews were visually inspected. Hole diameter is OOBB M3 clearance, 3.6 mm.
See `AI_VERSION_6_DOUBLE_SIDED.md`. Fit, stop contact, strength, creep and slicing
still need physical PETG testing.

## V5 six mm plates and additional row spacing (2026-10-20)

The user requested another 1 mm between 100 ml rows and restored both plates
to 6 mm. Population owns `row_spacing_extra=1.0` independently of the existing
`opening_height_extra=1.0`. Openings stay 87.5 x 28.5 mm; row pitch is 31.3 mm,
with 2.8 mm between openings. Tiled planning rebuilds rail Y coordinates from
that pitch so openings and shelves move together. Never change the frozen v4
mapping for this adjustment.

Nine-row units are now 767 x 308 and 362 x 308 mm, retaining M6 border bands.
Legacy `tiled_*_by_300` identifiers remain stable; read dimensions from metadata.
A1 mini stays 2 x 8 with four tiles per face, now 205.8 x 268.6 mm. The user
approved reducing its removable ears to 11 mm to fit the 180 mm bed; P1P ears
remain 12 mm. Preserve printer-specific bed and ear metadata.

Plates and stop blades are 6 mm thick, with 3 mm half-laps. Full-depth stop
blades preserve bed support in both alternating print poses. Stop projection
stays 6 mm with 0.75 mm chamfers. Matching rails are 98.5 mm between plates;
M3 x 16 pockets lie 7–10 mm inward, with the 14.5 mm end bands retained.
Both snap tips remain flush/recessed: 6 mm tips, 4.5 mm shoulder depth and
2 mm root extension preserve the 6.5 mm root-to-shoulder span. Keep the 1.8 mm
arms, 0.6 mm relief slots, 1.5 mm bearing strips and 0.05 mm slot overlap.
Rear M6 seats remain 1.5 mm deep inside the 6 mm plates, giving 9 mm between
back-to-back bearing faces. Use matching new plates AND rails.

Run `action_validate_tiled_v5.py` through populate -> OOMP -> SCAD. Current
output is `validation_tiled_v5_six_mm/`; earlier reports/baselines stay intact.
Checks now probe exported row separation and thickness-dependent M6 seat floors.
Keep all releases, v4 and the twelve historical connector records unchanged.
Validation passes 66 geometry tests, eight drawer comparison tests, 65 mesh
views and all three assemblies. Twelve old connector inputs/175 coupon SCAD
views and releases remain unchanged. Tile and assembly previews were inspected.
A broader webserver run found five unrelated file-action failures; its log is
`validation_tiled_v5_six_mm/webserver_tests.log`.
Physical PETG fit, strength and slicing still require verification.

## Previous V5 thin panels, taller 100 ml openings and rear M6 seats (2026-10-20)

Active v5 tiled units now have `opening_height_extra=1.0`: openings are
87.5 x 28.5 mm. The 767 x 300 and 362 x 300 mm outside envelopes and 8x9/3x9
grids remain; spare vertical margins absorb the extra row pitch. Older releases
and all twelve numbered connector-test records stay unchanged.

Front/rear panels are 3 mm, with 1.5 mm half-laps. The 6 mm tray-stop projection
is retained in a 3 mm-thick blade with 0.75 mm edge chamfers; rear has no stop.
The user clarified that BOTH snap ends should remain recessed, superseding
their initial suggestion to let the front clips protrude. Tiled snaps retain
sample 28's 1.8 mm arms, 0.25 mm side and 0.2 mm axial clearances, and 1.2 mm
hooks. Tips are 3 mm long, hook shoulders 1.5 mm from the rail end. Extend the
slot root 5 mm inside the beam to preserve its 6.5 mm root-to-shoulder span.
Two 0.6 mm rounded-ended outer relief slots retain 1.8 mm spring thickness
inside the beam; the remaining 1.5 mm outer strips carry the bearing load.
The straight/root-circle cuts overlap by 0.05 mm to prevent zero-area mesh
faces at coincident slot planes; retain that overlap.
This adaptation belongs only to tiled drawing, not the locked sample profile.
The matching 45-degree undersides/floors still retain both lap-layer spines.
Rails are 104.5 mm between plates; M3 x 16 nut pockets are now 10–13 mm inward
with 14.5 mm end reinforcement. Do not use the old 7.5 mm-panel rails.

The user confirmed rear fittings mean M6 screws/nuts, NOT magnets. Rear
through-holes use OOBB M6 clearance and 1.5 mm-deep OOBB hex seats with local
overhang bridge relief on the INSIDE of the rear panel. Outer mating faces
stay flat. All locations occur in X-mirrored pairs; turning identical units
180 degrees about upright Y aligns them back-to-back. Use hex-head screws
and nuts inside the cabinets; shallow seats do not bury the whole hardware.
There are 22 / 12 / 6 optional attachment locations for large/small/A1 units.
14.5 mm border bands and seam/hardware exclusions protect the seats.
Attachment hardware is separate from the unit's M3 BOM.

Population adds `tiled_a1_mini_four_plate`: 2 columns x 8 rows, finished
205.8 x 261.6 x 110.5 mm, with four tiles PER FACE (eight tiles total) and
three rail batches. It uses a 180 x 180 mm bed, 2 mm margin, no P1P cutter
mask, and the same removable ears. Maximum footprint is about 108.33 x
172.63 mm. Its side borders are widened 4 mm per side for M6 seats; top and
bottom have none. A ninth row requires an extra tile row with these seams.
Keep this printer's bed metadata dynamic; don't hardcode the P1P dimensions.

The normal populate -> OOMP -> SCAD pipeline remains mandatory. The current
validator is `action_validate_tiled_v5.py`, writing to
`validation_tiled_v5_thin_panels/`; the previous report and coupon baseline
remain in `validation_tiled_v5_print_revision/`. It checks all three layouts,
recessed clips, M6 seat depth/through-holes, mirrored attachment positions,
back-to-back mating, retained stops, both lap-layer spines and printing poses.
Actual PETG fit, strength and slicing remain unverified.
Validation passes: 65 geometry tests, eight comparison tests, 65 exported
mesh views and three assembly checks. Both snap ends and the extended
1.8 mm spring sections are checked, including prescribed insertion with
rigid outer bearing edges. V1–v3 release locks, v4 and all twelve historical
coupon records/175 coupon SCAD views remain unchanged.

## Selected connector standards 27 and 28 (2026-10-20)

The user selected latch 27 as the separate-key standard and sample 28 as the
main direct snap. These are connector sample numbers, not new cabinet versions.
`get_ai_version_5_selected_connector()` in population owns the selected
profiles; its default is `"snap"` (28), with `"key"` selecting 27.
Keep the twelve historical coupon records and all frozen releases unchanged.

Sample 27 retains its 175% key, 0.4 mm slot clearance, 0.25 mm through-piece
side/height clearance, and 0.1 mm latch clearance at each tongue face.
Sample 28 uses 1.8 mm arms, 0.25 mm per-side receiver clearance, 0.2 mm axial
clearance, 1.2 mm hook projection, 1.5 mm ramp and 6 mm shoulder depth.
Both tiled demos now consume the selected snap profile, including the thicker
arms. Keep the matching 45-degree tab/receiver bevels and 0.5 mm retaining
lands from the printability revision below. The coupon itself remains unchanged.
The tiled adaptation still needs a physical fit print.

`tests/test_selected_connectors.py` checks the selected profiles against their
numbered originals and locks the chosen fit values. The tiled mesh validator
checks actual arm thickness, front/rear mating and retained plate spines.
No clearance variants or extra taxonomy fields are introduced. Clearances
remain source parameters for future explicitly requested refinement.
Validation: 62 geometry tests, eight comparison tests, all 46 exported tiled
views and both mating assemblies pass. All twelve historical coupon records
and 175 coupon SCAD files remain unchanged; prior release checks pass.

## Tiled v5 print-face and snap-opening revision (2026-10-20)

The user requested all laps on one face of each tile, alternating high/low
between neighbours, and reported that the snap holes stopped the inner 100 ml
pieces locking. The two tiled demos are now intentionally revised; historical
baselines in later coupon validators still describe the previous demos and
must not be rewritten. All twelve connector-test records remain unchanged.
The dedicated new baseline is
`validation_tiled_v5_print_revision/previous_coupons_baseline.json`.

Tile layers now nest, with the larger layer on the bed and alternate tiles
pre-flipped inside-face-down. Four-way diagonal overlaps have explicit corner
notches. All masking remains in the single tiled cutout. Plate features finish
at 7.5 mm: front catch/ramp remains 6 mm high, but its protruding inner reverse
guide is trimmed flush. Projecting screw-mount keys are removed; screw rails
have flat seats instead of empty key sockets. Laps and snap mounts align the
assembly. OOBB M3 x 16 countersunk screws, side-loaded nuts and nut positions
remain. These changes are confined to v5 tiled models.

Snap undersides and receiver floors now have matching 45-degree bevels,
retaining the vertical spine below the 100 ml shelf in BOTH lap layers.
The original rectangular holes severed middle tiles into horizontal strips.
The tabs grow from the rail's flat print face and end in 4 mm-high tips;
outside openings are 4.5 mm high and grow toward the inner entry face.
This revision originally used 1 mm arms; the selected sample 28 above now
supersedes that with 1.8 mm arms. Hook depth/projection remain unchanged.
A 0.5 mm retaining land plus 45-degree pocket roof replaces the broad square
ledge. New controls live in population: `snap_tip_floor`, `snap_ledge_land`,
`seam_middle_screw`, `seam_middle_min_span`.

Screw anchors are at the ends of each actual tile-to-tile seam, with a middle
anchor when the mount span reaches 120 mm; horizontal seams use left/right.
Intermediate seam mounts now snap. Large demo: 18 screw and 81 snap rails,
36 screws/nuts. Small demo: seven screw and 37 snap rails, 14 screws/nuts.
Finished dimensions, tray grids and P1P footprint/exclusion remain unchanged.
See AI_VERSION_5_TILED.md and run `python action_validate_tiled_v5.py`.
Use matching new rails/plates; old full-height tabs will not clear the bevel.
Physical fit/strength of the revised tabs remains untested.
Validation passes for all 46 exported views, both assemblies, 59 geometry
tests and eight comparison tests. Every tile is one connected mesh, with
the restored spine checked in both lap layers at every snap. Seam snaps
pass prescribed-flex insertion and front/rear retention checks. Both
opposite tile print orientations and the new rail were visually inspected.
Frozen releases, v4 and all twelve connector-test records remain unchanged.

## Heavier flush twin-tab bed: 25, 26, 28, 29 (2026-10-20)

The user reports 23 and 24 too narrow and requests two heavier samples above
26, combined with 25 onward in one file. New `recessed_twin_heavy_suite` keeps
25/26 unchanged (1.4/1.6 mm arms) and adds 28/29 (1.8/2.0 mm). Number 27 remains
the separate-key design. `get_ai_version_5_heavy_latch_trials()` owns the inputs.
Only flagged trials 28/29 may use the 2.0 mm upper limit; original guards remain.

`3dpr.stl` is one bed of four matched pairs in 25 26 / 28 29 order. Recessed
numbers, separate pair/rail/plate views and assembled references follow the
existing suite. Outside faces, hook geometry, receiver, clearance and 6 mm
free length remain unchanged; arms grow inward, leaving 3.2/2.8 mm centre gaps
for 28/29. The rounded slot roots follow the gap. This remains a physical PETG
fit experiment; do not infer strength from thickness or prescribed flex checks.
No cabinet connectors change.

Run `python action_validate_latch_thickness.py --heavy` for the normal pipeline,
18 mesh views, four insertion/retention checks and byte-identical 25/26 views.
The baseline `validation_latch_heavy/previous_v5_baseline.json` preserves all
13 previous v5 records and 203 SCAD files. Current catalogue is 62 printed plus
15 purchased, with 54 complete units and 23 hidden samples.
All 18 exported views/four pair checks, 59 geometry tests and eight comparison
tests pass. The combined bed preview has been inspected. Physical fit of
28/29 remains untested.

## Sample-22 tighter separate key, sample 27 (2026-10-20)

The user reports 22 best among the separate-key trials and requests a tighter
latch where the key emerges. Population adds standalone `tight_key_27`, copied
from 22 with `tight_key_trial=True` and `key_latch_clearance=0.1` mm per tongue
face. Drawing derives the head bearing face and latch shoulder from the tongue
width: -4.475 and +4.475 mm around the existing 8.75 mm tongue. Total sideways
key travel drops from 2.45 to 0.20 mm. Head bearing length grows from 3.5 to
5.5 mm; hook shoulder moves inward 0.25 mm. Arms remain 1.4 mm thick with the
same hook projection/root radius, but their shorter free length makes them
stiffer. Clearance remains adjustable (guarded 0.05–0.20 mm per face).

`key.stl` is the standalone replacement for an existing 22 beam/plate.
The new folder also contains `3dpr`, `rail`, `plate`, and `assembled` files;
beam and plate differ from 22 only in recessed ID 27. Keep sample 22 and
all earlier designs unchanged. Neither the key slot nor beam/plate clearances
change. Complete cabinets still use their current connectors.

`action_validate_tight_key.py` checks five exported meshes against the original
22 receiver: seating, both 0.1 mm stops, retention, plate bearing, prescribed
flex insertion, unchanged interface sections, bed contact and quantities.
`validation_tight_key/previous_v5_baseline.json` preserves twelve older v5
records and 198 SCAD files. The normal populate -> OOMP -> SCAD pipeline owns
all outputs. Five mesh views, all twelve interface/quantity checks, 58 geometry
tests and eight comparison tests pass. No physical result yet for 27.
The catalogue now has 61 printed and 15 purchased records, with 54 complete
units and 22 hidden samples. See KEY_SIZE_EXTENSION_TESTS.md.

## Sample-19 latch thickness fit suite (2026-10-20)

The user reports that the flush twin-tab sample 19 worked well and requests
thicker latch arms for mainly permanent PETG use. Preserve this as qualitative
physical-fit feedback; it does not establish force/load/durability ratings.
Population now adds `recessed_twin_fit_suite`, with `get_ai_version_5_latch_trials()`:
23 = 1.0 mm control, 24 = 1.2 mm, 25 = 1.4 mm, 26 = 1.6 mm arms.
Both pieces carry recessed numbers. The complete bed has eight pieces in
23 24 / 25 26 order, with separate pair/rail/plate and assembled views.

Arms thicken inward. Hook/receiver/clearance/free length stay as in 19; the
rounded slot-end radius follows the centre half-gap (2.4 down to 1.8 mm).
Print receivers entry-face-down and rails on the long flat face, as for 19.
The 1.6 mm allowance is scoped to explicitly flagged trials 23–26 only.
Neither original 19 nor any complete drawer unit adopts the thicker arms.
The single complete coupon cutout and ordinary populate -> OOMP -> SCAD
pipeline are retained. See RECESSED_TWIN_FIT_TESTS.md.

`action_validate_latch_thickness.py` checks the 18 views and four mechanical
pairs, including actual section thickness, unchanged receiver fit, prescribed
flex passage, flush catches, bearing stops, labels, bed contact and quantities.
The immutable baseline in `validation_latch_thickness/previous_v5_baseline.json`
protects eleven older v5 records and 180 SCAD files; all older releases remain
protected too. Catalogue now has 60 printed plus 15 purchased records, with
54 complete units and 21 hidden samples. No new physical result exists for 23–26.
All 18 mesh views/four pair checks, 57 geometry unit tests and eight comparison
tests pass. The numbered bed preview was inspected; previous v5 inputs and all
180 CAD files are unchanged. Actual force, fracture and retention remain for
the user's physical trials.

## Version 5 tiled hybrid demonstrations (2026-10-20)

The user now authorizes full v5 demonstrations, superseding the earlier
coupon-only restriction. Confirmed finished outside sizes are 767 x 300 and
362 x 300 mm with 100 ml trays. Population owns two `tiled_hybrid` frame
records, 8 x 9 and 3 x 9 trays respectively. Depth is 110.5 mm. Existing
coupon records and all earlier releases remain unchanged.

Plates are split at beam mounts into eight / four tiles per face, using
3.75 mm half-thickness laps in the 7.5 mm plate. X/Y lap spans are 11/9 mm;
lateral seam clearance is 0.15 mm and layer clearance defaults to zero.
Every seam rail has the existing pointed key and M3 x 16 countersunk screw
with side-loaded overhang-aware M3 nut at both ends. Other rails use the
short flush twin tabs from sample 19, with no central guide or separate key.
`additional_screw_every=0` means seams only; a positive N adds every Nth
rail, retaining mandatory seam screws. Counts: 39 screw + 60 snap rails /
14 screw + 30 snap rails; 78 / 28 screws and nuts.

Fronts retain their catch and reverse guide; backs have no forward lip.
Rear tile masks and mount positions are mirrored so asymmetric layouts align.
Openings/pitches retain v4 dimensions; spare side margins have lightening
windows. Outside rail centres shift 0.9 mm outward into the border to retain
1.55 mm beside snap pockets (unchanged drawer openings). Full-depth rails
retain the 4 mm running shelf / 6 mm bottom reinforcement.

The P1P bed planner includes 12 mm ears, 0.2 mm removable necks, a 2 mm margin
and the official profile's 18 x 28 mm cutter exclusion at the bed origin.
It chooses the farthest feasible beam seams with the fewest rectangular tiles.
Print files use the bed CENTRE as origin and deliberate right/top offsets;
automatic centering/rotation can invalidate cutter clearance. Do not silently
disable the exclusion. The half-lap cantilevers can require local slicer
supports; neither these plates nor the aggressive snaps are physically proven.

`working_scad_tiling.py` owns planning and generated metadata, while solid
bodies remain in `working_scad.get_ai_version_5_tiled()` and complete removals
route through `get_container_cutout_ai_version_5_tiled()`. Existing v4 profile/
hardware and coupon-19 cuts are reused unchanged. `scad_help` supports variant
filters as well as style filters. Continue populate -> OOMP -> SCAD.

Each main folder has front/back tile print files, four / two numbered rail
batches, individual spare rails, complete-kit 3dpr overview and assembled
front/back/unit references. Print every tile and batch ONCE; references and
the oversized kit overview are not single-bed prints. See assembly.json,
printing.txt and AI_VERSION_5_TILED.md. Comparison uses assembled geometry
with PETG density 1.27, includes pots, excludes removable ears/hardware/supports.
New planner changes are included in the tiled-record geometry fingerprint.

Run `action_validate_tiled_v5.py` for pipeline, mesh exports, piece counts,
bed/cutter envelopes, retained snap walls/ledges, assembly volume conservation,
and older-release checks. The immutable pre-change snapshot in
`validation_tiled_v5/previous_v5_baseline.json` protects nine earlier v5
records and 134 SCAD views. Do not rewrite it. Catalogue: 59 printed plus
15 purchased, 54 complete units visible and 20 samples hidden.
The 46 mesh views and both assemblies pass, along with 54 geometry/unit tests
and eight comparison tests. Rendered tile/assembly views were inspected.
`bed_layout.csv` supplies slicer object-centre coordinates if imports are
automatically centred. Snap force, load capacity and print success remain untested.

## Larger key samples 20–22 after physical feedback (2026-10-20)

The user reports sample 9 closest but still loose, and 1 much too loose.
They requested three larger samples following 3/6/9's SIZE progression,
not 1/2/3's clearance progression. Population adds key_size_extension_suite
with get_ai_version_5_key_extension_trials(): 20=145%, 21=160%, 22=175%.
All retain sample 9's 0.40 mm key clearance, 0.25 mm through clearance and
0.20 mm axial catch clearance. Size/stiffness changes do not eliminate
nominal clearance play. Record this as qualitative fit feedback only.

These remain matched three-piece coupons: nine print pieces and 17 views
in one new main folder. Recessed numbers identify rails and receivers.
Print each matched set, not an enlarged key in the old #9 rail.
Rail/plate stay 11 x 10 / 7.5 mm. Sample 22 leaves 1.1 mm slot walls above
and below; a bounded 1.0 mm minimum applies only to these new coupons.
Key deflection allowance scales with key size for samples 20–22; free
fork gap, retained walls and actual prescribed-flex passage remain checked.
Old records keep their original limits and dimensions.

Run action_validate_key_size_fit.py --variant key_size_extension_suite
for the normal pipeline and new-suite checks. Its output goes to
validation_key_extension. The original eight v5 records (including the
flush revision of 19) are protected by previous_v5_baseline.json there.
Do not rewrite any baseline/release manifest. See KEY_SIZE_EXTENSION_TESTS.md.
Without --variant the validator checks all three numbered suites.
All 17 exported views, three joint checks, 48 geometry tests and seven
comparison tests pass, with all earlier input/CAD baselines unchanged.
The print layout is about 134 x 48 mm. Enlarged key-tip ramp cuts extend
past the envelope to avoid sub-STL-resolution coincident-edge slivers;
leave old key geometry unchanged. Current catalogue has 57 printed and
15 purchased records: 52 complete units visible and 20 samples hidden.

## Recessed aggressive twin tabs, coupon 19 (2026-10-20)

The user also requested two tabs, no middle piece, a rectangular entry and
aggressive catches whose retaining edges remain inside the receiver.
Population adds one independent `snap_recessed_twin` v5 test record,
numbered 19. Keep all seven previous v5 records/SCAD unchanged; their
baseline is validation_recessed_tabs/previous_v5_baseline.json.

The user then requested flush tips and a much shorter bend joint, with the
receiver tight against the solid beam. This supersedes the earlier long-neck
coupon. Tips now end exactly at the front face; the full-width beam begins
at the receiver entry face (local rail Z=0). It supplies broad seating
shoulders instead of the earlier separate tab stops. No exposed neck remains.

Tabs are now 1.0 x 10 mm with the same 1.2 mm hooks, 0.25 mm side clearance
and nominal 0.95 mm inward movement each. Free length to the hook shoulders
is 6 mm instead of 15.5 mm. The open 4.8 mm centre slot has its round-end
centre 0.5 mm inside the beam and a 2.4 mm radius, closing by 2.9 mm.
There is no central guide or loose key. Receiver throat remains 7.3 x 10.5 mm,
pocket 9.7 x 10.5 mm. The square retaining ledge is now 1.7 mm from the
front face; hook shoulders sit at 1.5 mm and the 1.5 mm lead-in ends flush.
Rail/receiver section and thickness remain 11 x 10 mm and 7.5 mm.
Shortening substantially increases stiffness and strain; thinner tabs help
but physical PETG insertion/retention must still be trialled.

Print the receiver ENTRY FACE DOWN (180 degrees about Y); its larger
catch pocket opens above the narrow throat, avoiding an unsupported ledge.
The rail prints on its long face. Both have recessed 19 on their print-top
faces. Keep 3dpr/plate/rail/assembled views in the same main folder.
Main drawing supplies a single solid rail envelope through the tab tips;
the complete v5 cutout carves both hook outlines, centre slot, round root,
receiver and labels. Do not union coplanar tab bodies: this produced
degenerate STL seams in an early export.

action_validate_recessed_tabs.py runs the normal pipeline and checks four
views, two printable solids, print-facing ledges, absence of a central guide,
internal catches, flush tip position, beam-to-plate seating, clearance,
retention, over-insertion stops and prescribed flex passage. Flex screening
fixes the beam at Z=0; do not count the shallow root relief as free arm length.
Physical PETG behavior is unverified. See RECESSED_TWIN_TAB_TEST.md.
The four exported views, all connection checks, 47 geometry tests and
seven comparison tests pass, as do all earlier locks and saved CAD checks.
The kit occupies 37 x 39.5 mm and both print pieces have no airborne
downward faces. Current catalogue: 56 printed plus 15 purchased records;
52 complete units show by default and 19 samples are hidden.
The original v5 validator skips this later coupon, as it skips the numbered
key suites; each has its own appropriate mechanical checks.

## Numbered key and tapered through-piece trials (2026-10-20)

The user selected the separate locking key, requested size/clearance coupons
with recessed numbers on the long pieces, then requested independent
through-piece clearance and a gentle taper with modest interference.
Keep this work as test coupons; do not generate a full v5 cabinet yet.

Population now adds two nine-set records, `key_size_fit_suite` and
`through_fit_suite`, both using `connector_design="key_size_fit_suite"`.
`get_ai_version_5_key_trials()` defines samples 1–9: 100/115/130% keys
crossed with 0.20/0.30/0.40 mm per-side key slot clearance. Their straight
through fit stays at 0.25 mm per side. `get_ai_version_5_through_trials()`
defines samples 10–18: fixed sample-5 key, 0.10/0.20/0.30 mm X entry
clearance crossed with -0.025/0.025/0.05 mm per-side final interference.
Negative interference means 0.025 mm final clearance for the sliding controls;
avoid exact zero-interference line contact, which creates nonmanifold reference
unions. Actual interference columns remain modest and deliberate.
Only the last 6 mm inside the plate tapers in X; Y clearance stays 0.25 mm.
Keys and shoulders beyond the plate retain their original fit. Axial catch
clearance stays 0.2 mm. These requested experiments are an explicit exception
for test kits only; keep drawer clearance variants retired and values out
of taxonomy IDs. All settings remain in population.

Each suite's 3dpr contains 27 pieces; each rail and plate has its number
recessed 0.6 mm, visible from above on the print bed. Keep keys alongside
their numbered pairs; do not weaken keys with text. Individual trial, plate,
rail, key and assembled views stay in the same main folder. Each suite has
47 views and generated trial_index.csv/printing.txt/connector_test.json.
All cutouts, tapered tongue and recessed text stay together in
get_container_cutout_ai_version_5; bodies/layouts stay in working_scad.

`action_validate_key_size_fit.py` runs populate -> OOMP -> SCAD, exports both
suites and checks meshes, fit envelopes, recessed rail labels, retention,
prescribed key flex passage and the analytically expected taper interference.
Seated CAD overlap on interference samples is intentional and must be
accounted for; do not weaken checks to allow other collisions. Physical fit
and strength are still unverified. Preserve the original five v5 inputs/CAD
baseline in validation_key_size_fit/previous_v5_baseline.json, the existing
v4 baseline and all three release manifests. See KEY_SIZE_FIT_TESTS.md.
Validation passes 94 exported views, 18 connector checks, 46 geometry tests
and seven comparison tests, plus all earlier locks/baselines. Both print
footprints are approximately 133 x 154 mm. The current catalogue has
55 printed plus 15 purchased records; 52 complete units show by default
and 18 samples are hidden.

## Version 5 original connector trials (2026-10-20)

The user requested snap-fit experiments before any complete v5 cabinet, using
PETG and mainly permanent locks. V4 remains the current complete drawer unit.
`get_ai_version_5_options()` emits ONLY five `connector_test` records: single
cantilever, twin cantilevers, separate captive fork key, the unchanged v4
countersunk screw reference, and a combined nine-piece print suite. Do not
emit full v5 frames or implement a cabinet screw/snap distribution yet.
Future screw count/positions must be configurable after connector selection.

Coupons retain 11 x 10 mm rails and 7.5 mm plates, with 32 mm rail grips.
All positive bodies/layouts live in `working_scad`; complete openings, spring
reliefs, guide tongues, hooks, fillets, key slots and identifying notches live
in `get_container_cutout_ai_version_5()` as multiline dictionaries. Population
owns all settings, including one default 0.25 mm per-side connector clearance.
There are no clearance taxonomy variants. Single/twin/key pairs have one,
two or three edge notches respectively; the screw reference has none.

Direct snaps use 1.1 mm filleted roots and 0.65 mm hooks, with nominal 0.4 mm
insertion deflection and 0.2 mm axial catch clearance. Their hooks emerge
2.6 mm beyond the outside plate face. The key concept is a separate planar
fork through a rigid tongue; its rail has a short transverse slot bridge.
Keep flexure in the bed plane. These are not interchangeable v4 receivers.

`action_validate_ai_version_5.py` runs the normal pipeline, exports printable
and assembled views, and checks meshes, bed fit, quantities, seated clearance,
retention interference and prescribed-deflection insertion paths. These are
geometric checks, not FEA, force ratings or physical tests. Preserve
`validation_ai_version_5/version_4_baseline.json`; it records pre-experiment
v4 inputs/SCAD, while the existing v1/v2/v3 release locks stay authoritative.
See `AI_VERSION_5_CONNECTOR_TESTS.md` and `connector_tests/results_template.csv`
for the physical PETG test protocol. Never overwrite completed test results.
Comparison hides these samples, counts no pots/drawers and estimates solid
PETG mass at 1.27 g/cm3. Reference hardware cost is excluded.
Current checks pass 19 exported CAD views, four connections, 43 geometry
unit tests and seven comparison tests. All nine suite pieces are closed and
lie on the bed, in an approximately 93 x 104 mm layout. No physical result
has been claimed. Round v5 polygon coordinates at six decimals and carve the
separate key from one solid envelope to avoid degenerate translated STL faces.
`scad_filter="ai_version_5"` allows quick connector redraws while retaining
populate -> OOMP -> SCAD. The comparison action accepts `--scad-filter`;
omit it when changing other styles. Default unfiltered builds are unchanged.

## Version 4 front-only catch correction (2026-10-20)

The user reversed the identical-plate requirement after seeing the catch on
both ends. Current v4 has one front plate WITH the catch and its reverse ramp,
and one rear plate WITHOUT the catch/ramp. Population owns `front_lip=True`
and `rear_lip=False`. Rails, mounting keys, countersinks and dimensions stay
unchanged. Keep the complete opening/catch logic in the existing v4 cutout;
the component assembly passes `include_forward_lip` for the selected end.

`front.scad` and `back.scad` are distinct print-ready parts; `face_plate.scad`
is now the front alias only. The kit and assembled views use one of each.
The BOM now names `front: 1` and `back: 1`, not `face_plate: 2`. Joint-fit
coupons still happen to match because they contain no tray opening/catch.
Face-fit kits still contain one front only, but also export front/back files
for optional individual testing. Update printing instructions and comparison
measurements through the pipeline. Validate rear catch absence, unchanged
mounts, the exact removed geometry and correct one-front/one-back kit quantities.
The correction passes 81 exported mesh views, eleven assembly/sample checks,
38 geometry unit tests and all three release locks. The lip comparison unions
an independent catch profile with the rear mesh and compares it to the front;
this accounts for the catch root overlapping the rounded plate surface.

## Version 4 initial modular plates and rails (2026-10-20)

Development now belongs in version 4. The completed v3 was preserved at
`releases/ai_version_3/`; `action_check_version_3_lock.py` protects its twelve
active records and 42 SCAD views. Do not rewrite any v1/v2/v3 release manifest.

The user confirmed front AND rear plates with removable rails, and then
required identical plates. V4 uses one plate printed twice, one universal
rail for shelves/top/top corners, and a thicker bottom-row rail. The user
also requested angled rear guidance: both identical plates have the existing
6 mm catch with a 6 mm reverse slope on its inside. Real rear tray clearance
must be trialled; do not claim that a bounding-box check proves container fit.

Population owns eleven v4 records: eight full units, one short joint-fit kit
and one face-fit plate for each container. V4 reads the frozen v3 dimension
mapping, but its bodies/layouts and complete cutout are separate. Main drawing
adds solid plate/rail bodies. Keep all opening/guide/key/hardware/rail cuts in
`get_container_cutout_ai_version_4()` with explicit multiline dictionaries.
Continue the normal populate -> OOMP -> SCAD pipeline; never patch output CAD.

Plate thickness is 7.5 mm; border 10.5 mm; removable ears 12 mm. These retain
the previous maximum grids on declared beds with 2 mm margins. Rails are
11 x 10 mm at their ends, 95.5 mm long for 100 ml and 94.5 mm for 550 ml.
Regular running thickness is 4 mm; bottom is 6 mm. One rail works at all
standard/top/corner positions within that container depth. Top/bottom mounts
are now screwed too: total rails `(column + 1) * (row + 2)`, two screws/nuts
per rail. The plate outside dimensions differ from v3; cavities/pitches do not.

Each plate carries a 3 mm pointed key; rail sockets use 0.25 mm side and
0.2 mm end clearance. Use OOBB `oobb_screw_countersunk` for M3 x 16 from the
outer face, and `oobb_nut` with `overhang=True` and `clearance="left"` or
`"right"`. Current OOBB left opens toward local +X, right toward -X. Default
is left. Nuts sit 5.5–8.5 mm inward from each rail end. Rails print on their
long flat faces; small screw bores/side nut slots retain short bridges.

Each main folder has a complete-kit `3dpr`, `face_plate`, identical `front`
and `back` aliases, `rail`, `bottom_rail`, `assembled`, and numbered bed-sized
`rails_plate_*` views, with matching STL exports. `assembly.json` and
`printing.txt` are generated from source. The overview may exceed one bed;
print the plate twice and each numbered rail batch once. Face-fit samples
contain one plate only. Comparison uses assembled geometry for complete
units and actual sample contents without pots for tests. Hardware is excluded
from cost. Active catalogue: 48 printed + 15 purchased, 52 complete units
shown by default, eleven samples hidden.

See `AI_VERSION_4.md`. `action_validate_ai_version_4.py` passed 77 mesh views
and eleven assembly/sample checks, including side nut insertion samples,
identical plates, preserved mounting walls, both catch slopes, collision-free
interfaces and exact kit/batch quantities. All three release locks and 38
geometry unit tests pass. Physical fit/strength/printing remain unverified.

## Version 3 intermediate lower supports removed (2026-10-19)

The user requested removal of the repeated lower front-to-back rails, retaining
the outer top/bottom rails and every screwed lip shelf. They clarified the
counts as four connections per vertical grid boundary for two rows and nine
for seven rows. Default `remove_internal_lower_supports=True` lives in v3
population; disabling it restores the intermediate rails/pegs for experiments.
Versions 1 and 2 remain locked.

The single v3 cell cutout removes each internal row-boundary rail from the
outer face band to the seam, including rounded-corner remnants. It also omits
the corresponding peg/socket. Front catches, front/rear face grids, outer
top/bottom rails, screwed shelves, taper, hardware and dimensions remain.
This applies to all multirow v3 frames, including the solid reference; the
single-row joint-fit sample and shallow layouts are unchanged. Each vertical
grid boundary has `row + 2` connections: `row` screwed and two round interlocks.
The removal overlaps adjoining reliefs by 0.1 mm to avoid coincident slivers.

Mesh checks verify absent internal rails/pegs, retained face grids, remaining
interlocks and (for lightened frames) the exact contact-island count. The v2
interface comparison permits only the explicit removed rail bands and checks
the remaining interface plus the original outer face section unchanged.
All 42 mesh views, ten mating pairs, 33 unit tests, six comparison tests and
both release locks pass. Twenty half-interface comparisons pass with only the
authorized removed bands excluded. CAD reductions against locked v2 are now
23.70% for the 100 ml 2 x 2, 36.98% for A1 mini, 42.80% for P1P and 46.50%
for 4 x 12; the 550 ml 2 x 2 saves 20.16%. These include the earlier taper
revision and adhesion ears, and do not establish printed strength or slicing.

## Version 3 tapered hardware reinforcement (2026-10-19)

Version 3 now reduces the nominal running lip shelf from 10 to 4 mm away from
the joint, retaining 10 mm for a 12 mm band beside the seam. Upper side reliefs
close into this band over a 7.2 mm, approximately 50-degree transition. Rear outer face band
uses its existing 6 mm setting; front stays 7.5 mm to contain the catch.
Population owns `running_shelf_thickness`, `hardware_boss_band` and
`hardware_boss_slope`. Keep the taper in the single version 3 per-cell cutout;
the main drawing remains one solid body. Versions 1 and 2 stay locked.

Mating features, screws/nuts, flat bearing seats, rail widths, outer border,
walls, clearances and outer envelopes are unchanged. Existing axial hardware
passages interrupt the nominal shelf cross-section, so check the bearing/root
material below the bores and side webs explicitly. The OOBB seat bridges remain
localized; do not claim the flat fastener seats are entirely support-free.
The short joint-fit sample and solid reference have lightening disabled, and
the shallow layout samples remain unchanged. Trial an ordinary 1 x 1 frame to
check the new long rails and taper physically.

Version 3 now has its own lip-section check in
`validation_ai_version_3_checks.py`, alongside tapered-rail section checks.
The validator writes `material_comparison.json` against the frozen v2 CAD
volumes. Preserve the original release checkers; version 3 is intentionally
no longer an exact geometry copy after this refinement.
The approximately 50-degree revision passed 42 mesh views, ten mating pairs,
32 unit tests, six comparison tests and both release locks. All twenty sampled
front/back interface sets match the frozen v2 geometry, including the hardware
seats and interlocks (`action_compare_version_3_interfaces.py`). CAD reductions
are 8.40-13.53% for lightened full frames; the 4 x 12 saves about 276.8 g at
1.24 g/cm3 solid PLA. Solid-reference/joint-fit/layout geometry is unchanged.
These are CAD comparisons, not measured slicer savings or physical strength.

## Clearance-fit catalogue variants retired (2026-10-19)

The user explicitly removed all clearance-fit variants from ALL versions.
Population no longer emits `fit_clearance_0d75`, `fit_clearance_1d5` or
`fit_clearance_2d25`, including the separate fit sample at default clearance.
Keep `container_clearance` adjustable in each version's defaults, currently
1.5 mm overall opening clearance. Generate only that default; do not put
clearance in taxonomy/IDs. Ordinary frames, joint-fit and layout samples remain.

`action_retire_clearance_variants.py` moved the nine records from parts,
parts_source and navigation into `retired_clearance_part_records/` (27 folders).
It is repeat-safe and recoverable. Frozen release snapshots/manifests remain
unchanged. `release_retirements.py` records the explicit exception to the
active model set; both release checkers still validate every retained input
and drawing. Version 1 now checks eleven models; version 2 checks twelve
models/42 SCAD views. Do not broadly relax release checks for other variants.

Active population now has eleven v1, twelve v2, twelve v3 and two basic printed
records, plus fifteen purchased records (52 total). Default comparison still
shows 44 complete units; eight joint/layout samples are hidden. The v2/v3
validators now cover 42 views and ten mating pairs each. Initial 45-view copy
verification below predates the user-authorized retirement. Thirty-one unit
tests pass, including default-only population and independently settable
clearance. Future refinements still belong in version 3.

## Locked version 2 and independent version 3 (2026-10-19)

The user locked the completed all-junction-interlock version 2 and requested
version 3 as an exact starting copy. This supersedes earlier statements that
version 2 is the active development version. Future refinement belongs in
version 3 unless the user explicitly requests a release change. Both version
1 and version 2 are frozen; never rewrite their release manifests.

`releases/ai_version_2/` holds the original source, all fifteen generated
model folders, 45 CAD views, passing mesh report and `manifest.json`.
`action_check_version_2_lock.py` compares all released drawing inputs and
all SCAD views after regeneration. `--compare-version-3` additionally checks
the initial clone; use that flag only before development diverges. The initial
comparison report is `releases/version_2_to_3_copy_check.json`.

Version 3 has independent options/defaults in `working_oomp_populate.py`, five
`get_ai_version_3*` body/parameter/summary/ear/container functions in
`working_scad.py`, and a complete `get_container_cutout_ai_version_3()` routine.
Keep every cell's cutouts, reliefs, hardware and interlocks together there.
The usual solid body and populate -> OOMP -> SCAD pipeline remain. Shared
`scad_help` routes each version to its own drawing function for all four views.
Comparison rendering/measurement uses `assembled.scad` for both split styles.

See `AI_VERSION_3.md`. Run `python action_validate_ai_version_3.py` for the
45 meshes and ten pairs; it checks both locked releases. Independent mesh
helpers are in `validation_ai_version_3_checks.py`. All fifteen version 2
options have version 3 equivalents with new IDs. There are now 46 printed
records plus fifteen purchased records; the default comparison shows 29
complete printed units plus fifteen purchased units, with seventeen samples
hidden. Older counts below are historical.
The initial clone passed equality checks for all fifteen inputs and 45 SCAD
views, 45 exported-mesh checks, ten mating pairs, 30 unit tests, six comparison
tests and both release locks. Refine version 3 freely; preserve both releases.

## Version 2 interlocks at every mating junction (2026-10-19)

The active split cutout now adds a 2.8 mm diameter front peg at every unscrewed
corner-rail grid junction, including internal intersections and outside corners.
Existing rectangular hardware tongues remain; screw counts are unchanged.
Additional peg count is `(column + 1) * (row + 1)`. Pegs use the same 3 mm
engagement, 0.25 mm radial clearance and 0.2 mm end clearance as the other
interlocks. Population controls `corner_interlock_diameter` and
`corner_interlock_min_wall` (0.6 mm). Internal row junctions are shifted down
half a divider thickness into the existing rounded-corner material; outside
junctions are centred in the border. One cell owns each junction to avoid
duplicate geometry. Keep these features in the single active cell cutout.
No opening, outer envelope, screw or version 1 dimensions change.

The mesh validator checks every junction's peg/socket, retained socket walls,
that tongues stay inside the original contact footprint, and that every
distinct mating island has an interlock. Mesh checks do not establish printed
fit or strength. The existing joint-fit pair includes its four corner pegs.
All 45 exported meshes, ten mating pairs, 22 geometry unit tests and six
comparison tests passed for this revision; the version 1 lock passed too.
Assembled peg clearance cavities are negative-volume shells, not extra solid
bodies, when counting connected solids in the exported reference mesh.

## Version 2 consolidated output folders (2026-10-19)

This supersedes the separate-half catalogue scheme described below. Each full
version 2 frame now has one main folder with `3dpr.scad` (both halves flat at
Z=0), `front.scad`, `back.scad` and `assembled.scad`, plus matching STL exports.
`printing.txt` explains these and whether the pair fits one bed. Main population
sets `assembly_half="print_layout"`; an 8 mm `print_layout_gap` separates full
footprints including ears. Automatic X/Y arrangement prefers a single-bed fit.
Maximum pairs need separate plates; individual front/back files still fit.
Do not mistake the combined layout dimensions for the finished unit dimensions.

The normal scad_help output stage generates all four files from working_scad;
no output CAD is hand-edited. Main drawing remains solid-minus-per-cell-cutouts.
Comparison rendering/measurement uses assembled.scad for completed dimensions
and costs. Geometry of the individual halves is unchanged by consolidation.
The old 20 half records were archived from parts, parts_source and navigation
into `retired_split_part_records/`; `action_consolidate_split_parts.py` performs
the recoverable migration once on older checkouts. Do not regenerate those IDs.
The joint test now has one `_joint_fit` folder. There are 15 version 2 records,
31 printed records overall and 15 purchased records; default comparison still
shows twenty full printed units and fifteen purchased units. The new joint-fit
record is a hidden sample with no pots in its cost.

`action_validate_ai_version_2.py` exports/checks 45 meshes in those 15 folders
and ten mating pairs. It verifies that combined layouts retain both halves and
that each body starts on the bed. Hardware/face checks run on individual files.
The release checker still protects version 1. See AI_VERSION_2.md for current
file names; counts/paths in the older revision notes below are historical.

## Version 2 split-frame revision (2026-10-19)

The user requested front/back halves, M3 x 16 socket-cap screws from the front,
M3 nuts from the back and a 3 mm interlock. This supersedes version 2's initial
exact-copy state; version 1 stays locked. See AI_VERSION_2.md for assembly and
print instructions. Both halves are generated directly from source through the
required pipeline, not cut from generated meshes.

Version 2 population emits 34 records: nine assembled frame references,
eighteen printable halves with `_front`/`_back` variants, five existing shallow
samples, and `joint_fit_front`/`joint_fit_back` test pieces. Assembled references
are not printable; print the two halves. `assembly_half` selects the route.
Body depth is half the original insertion depth; front tongues extend 3 mm.
Rear prints outside-face-down and rotates 180 degrees about Y for assembly.

All cell reliefs, interlock geometry and OOBB screw/nut cutouts stay in the one
active version 2 cutout routine with explicit dictionaries. Main drawing keeps
a solid body; assembled references combine two independently cut halves.
Reliefs open at the seam, avoiding broad closing roofs. Small hardware-seat
bridges remain and are separately bounded by the mesh validator. The lip shelf
is thickened to 10 mm, outside border to 5.5 mm, side rails to 4 mm. Tongues are
8 x 7 x 3 mm with 0.25 mm per-side socket clearance and 0.2 mm end clearance.
Hardware seats are -6/+7 mm from the seam with a 3 mm OOBB nut pocket: 16 mm
under-head length. One screw/nut is used per grid boundary per row. Use
`oobb_screw_socket_cap` with `include_nut=True`, both clearance booleans true,
AND `clearance=["top", "bottom"]` for the current library's actual API.

Version 2 ears are 16 mm to retain all previous maximum grids despite the
wider borders. The 550 ml extra height and reference-limited shoulders remain.
The short 24 mm assembled-depth joint test has no ears or lightening. All
parameters live in population. `action_validate_ai_version_2.py` checks the
34 meshes, ten mating pairs and the v1 lock. The locked release manifest must
not be rewritten. Comparison costs use assembled references, hide separate
halves by default, omit pots for separate halves and exclude hardware costs.
Validation passed: 20 geometry/unit tests, six comparison tests, all 34 meshes,
all ten mating pairs and the version 1 lock. There are now 50 printed records
plus the 15 purchased records; default
comparisons still show twenty complete printed units and fifteen purchased.

## Locked version 1 and independent version 2 (2026-10-19)

The current version 1 is locked after adding `opening_height_extra=1.5` to
all three 550 ml options. This adds 1.5 mm per row; actual container height
remains 92 mm, opening height is now 95 mm, and the lip profile/reference
height stays unchanged. New ear-inclusive 550 ml envelopes are
92.3 x 140.8 x 109.5 mm (1 x 1) and 181.6 x 237.6 x 109.5 mm (2 x 2).
The 100 ml models are unchanged. Historical dimensions below precede this release.

Both versions have separate options/defaults in `working_oomp_populate.py`,
separate body/parameter/ear/summary/container-mapping functions in
`working_scad.py`, and separate complete cutouts in the cutout module.
Version 1 now calls `get_container_cutout_ai_version_1()` containing the
current stepped design; version 2 calls `get_container_cutout_ai_version_2()`.
The old straight-profile function is `get_container_cutout_ai_legacy_straight()`.
This supersedes the historical dispatch description below. Future development
belongs in version 2 unless the user explicitly asks to revise the release.
Keep all changes in the existing three-stage pipeline.

See `AI_VERSION_2.md`. The locked baseline is `releases/ai_version_1/`;
`releases/ai_version_1_2026_10_19/` is only the earlier recovery snapshot.
Do not rewrite the lock manifest during v2 work. Run
`python action_check_version_1_lock.py` after regeneration. Version 2 validation
uses `python action_validate_ai_version_2.py`. Both styles have fourteen parts;
with two basic parts there are thirty printed models, and fifteen purchased
records. Comparison defaults show eighteen full AI frames plus two basic
frames (twenty printed units), alongside the fifteen purchased units. Refresh measured costs through
`action_prepare_drawer_comparison.py` after drawing changes.

## Structure and data flow

- `working_oomp_populate_purchased.py`: editable UK purchased-drawer research
  records, called by normal population after the generated-frame options are
  prepared. The user has approved inclusion of the 15 current small-component
  records; their approval flags are true and normal population emits them.
  Keep future research proposals unapproved until authorized. The latest additions are Barton 20/40 drawer
  multipacks and Treston 291-4ESD. The reusable one-off research brief is in
  `drawer_research_agent_instructions.txt`; it requests GPT-6 Luna at low
  reasoning and in-app-browser evidence, with parent-assisted browser reading
  if the subagent browser is unavailable. Only
  `approved_for_oomp=True` entries are emitted; wait for the user's shortlist
  and taxonomy approval before enabling them. These are catalogue records with
  no `oobb_details`, so the existing SCAD loader skips them. Taxonomy 4 is
  `small_drawers`, 5 per-drawer ml capacity (explicitly marked when estimated),
  6 drawer count, 7-9 complete-unit W/H/D, 14 manufacturer, 15 sanitized part
  number; 10-13 are blank. Raaco uses its numeric manufacturer part number,
  with cabinet model stored separately. All shortlisted units have uniform
  drawers around 200-300 ml. Drawer dimensions retain their published basis;
  nominal capacity and calculated rectangular volume are separate fields.
  Capacity taxonomy and capacity_ml fields round to the nearest 25 ml using
  half-up rounding; preserve original values in *_unrounded_ml fields and
  keep rectangular_volume_ml unchanged. Rounded capacity is a comparison label.
  Raaco nominal capacity is inferred from cabinet litres and drawer family.
  Sealey capacity is an estimate from dimensions whose internal status is
  unconfirmed. Treston nominal capacities follow its drawer catalogue. Costs use GBP
  including VAT excluding delivery; per-kg is for the complete empty unit.
  Preserve weight/source qualifications and unknown values; never substitute
  shipping weight or load capacity for product weight. Large, paper-sized and
  mixed-drawer units have been removed from the active shortlist. Preserve the
  approval gate; do not generate purchased OOMP records before user approval.
  Preserve multipack price/count and minimum required spend alongside derived
  per-cabinet price. The ESD drawer L-61-4ESD is rated 200 ml by Treston despite
  its 469.2 ml external rectangular envelope; do not substitute envelope volume.
- `working.py`: orchestrates population, OOMP enrichment, SCAD generation, then
  optional SVG/action stages, controlled by keyword flags.
- `working_oomp_populate.py`: builds option dictionaries (`container`,
  `container_short`, `column`, `row`, `style`), adds taxonomy fields, copies
  drawing inputs into `oobb_details`, and sets `oobb_name` from `style`.
  Generated designs start with taxonomy 1 `oobb`, followed by 2 `organization`,
  3 `storage`, 4 `drawer_unit`, 5 column, 6 row, 7 container, 8 style, 9 variant.
  Purchased units keep taxonomy 1 `organization`. This separation is defined
  in population and copied into drawing inputs, so it persists on every run.
  Calls the extra-detail hook and the shared `write_extras()` helper, which writes
  `parts_source/<taxonomy-derived-id>/working.yaml`.
- `working_oomp_populate_extra_detail.py`: hook for annotations keyed by generated
  ID. Its example annotation is currently disabled.
- `working_oomp.py`: reads source YAML, adds names, directories, optional per-part
  manual overrides and action metadata, then calls `oomp.add_parts()` to produce
  enriched records under `parts/<id>/`.
- `working_scad.py`: reads `parts/*/working.yaml`; combines build kwargs, stored
  kwargs, and `oobb_details` (in that precedence order). Contains the body/grid
  geometry in `get_basic()` and the dimension mapping in `get_container_details()`.
  Its `get_container_cutout()` wrapper delegates to
  `working_scad_container_cutout.get_base(pos, thing, **kwargs)`.
- `scad_help.py`: dispatches `oobb_name` to `working_scad.get_<oobb_name>()`, with
  `get_base()` as fallback; writes `3dpr.scad`, optional exported artifacts,
  updated `working.yaml`, and `thing.yaml`. Copies generated part folders into
  `navigation_oobb/` using taxonomy order.
  Navigation includes catalogue records without drawing kwargs and uses all
  15 taxonomy levels, preserving purchased manufacturer/part-number identity.
  During the prefix migration existing generated folders were renamed to their
  new IDs; old navigation was preserved in `taxonomy_migration_backup/`.
- `working_scad_container_cutout.py`: owns the active cutout and catch-tab code,
  including all AI material-saving shelf and side-wall windows.
  Its `get_base()` dispatches by style: `ai_version_1` now uses the user's
  stepped-profile `get_container_cutout_ai_version_2()`; other styles use
  `get_container_cutout_version_1()`. Make cutout
  changes here; retain the call from `working_scad` and the full generation pipeline.
- `working_scad.get_base()` and `get_hole_cover()` are other/template geometry;
  the current `basic` definitions select `get_basic()`.
- `webserver/`: ancillary Flask browser for generated parts. Its add form writes
  root `working_manual.yaml`, but population of that file is currently disabled
  by `if False` in `working_oomp_populate.py`. Root manual options and per-part
  manual overrides in `working_oomp.py` are different mechanisms.
- `source_file/`, `template/`, `roboclick/`, and `working_action.py` support
  labels, artwork, and other actions outside the core drawer geometry.

## Build entry points

### Drawer comparison webserver

`webserver/app.py` serves product cards at `/drawers` (the homepage) and a
sortable table at `/compare`. Both use `webserver/services/drawer_comparison.py`.
Purchased photos are cached in `webserver/static/drawer_photos/`; original image
and seller URLs are explicit fields in `working_oomp_populate_purchased.py`.

`working_oomp_populate_comparison.py` is called by ordinary population. It owns
the editable Systempak 209/214 carton prices, VAT, lidless pot masses, and the
filament rate of GBP 0.01/g. It prefers explicit VAT-inclusive local container
price records if available. The current fallback prices were checked on the
live Systempak site on 2026-10-18: GBP 60.95/80.95 ex VAT per 500 pots and lids,
respectively, both on backorder. Pots are used without lids but the purchase
cost includes them. Source URLs and all assumptions persist in generated YAML.

Run `python action_prepare_drawer_comparison.py` after geometry changes to run
populate -> OOMP -> SCAD, export and measure the actual CSG meshes, render
`comparison.png` for all 16 printed designs, and run the same pipeline again
to carry costs into records and navigation. `drawer_comparison/cad_measurements.json`
is derived cache data, keyed by CAD source and drawing-parameter fingerprints.
Ordinary population refuses stale measurements. Edit population inputs, never
the generated YAML or measurement cache. Filament mass assumes solid PLA at
1.24 g/cm3 including ears; it is not slicer-measured mass. Empty assembled weight
adds lidless pots (209: 8 g, 214: 16 g). Printing energy/labour/waste and delivery
are excluded. Fit and shallow layout samples are hidden by default and labelled
when enabled; 11 full frames and 15 purchased units form the default comparison.

Comparison checks: `python -m unittest webserver.tests.test_drawer_comparison -v`.
The broader webserver suite also contains legacy file-action and manual-editor
expectations unrelated to comparison; see `drawer_comparison/validation.md`.

Run from the project root so relative input and output paths resolve correctly.

- `python action_make_scad_no_stl.py`: complete populate -> OOMP -> SCAD sequence;
  fast SCAD generation and navigation copying, with action execution disabled.
- `python action_make_scad.py`: same sequence with full export (`typ="all"`,
  `save_type="all"`), including STL generation.
- `action_make_all.py`, `action_make_all_no_stl.py`, and default `working.py`
  also run the action stage. Prefer the SCAD entry points for geometry work.
  `working_action.py` includes label regeneration, another OOMP pass, and
  Roboclick actions.
- Running `working_scad.py` alone consumes existing part records and skips the
  preceding source stages; it is not the complete required regeneration path.

Shared Python dependencies are outside this folder. At inspection, `oomp` and
`oomp_populate_helper` resolve under `C:/gh/oomlout_oomp_version_5/`, and `oobb`
and `opsc` under `C:/gh/oomlout_oobb_version_5/`. Python 3.12 and OpenSCAD Nightly
are available. Check the current environment if imports or exports fail.
This directory was not a Git checkout at inspection.

## Basic-style geometry baseline and coordinate conventions

- Basic variants: 1 column x 1 row and 2 columns x 2 rows.
  Each option currently uses one container type across its entire grid.
- Container: Systempak 209, rectangular 100 ml tamper-evident takeaway container.
  The full identifier includes `109_mm_width_86_mm_height_29_mm_depth`.
- Drawing dimensions are mapped explicitly in `get_container_details()`:
  X/across = 86 mm, Y/rows = 26 mm, Z/insertion depth = 109 mm.
  Do not infer the drawing axes directly from the identifier's width/height/depth
  labels. The user confirmed that 26 mm is the container height without its lid;
  the identifier's 29 mm includes the lid, which this project does not use.
- Clearance is 1.5 mm added to each opening's overall X and Y dimension
  (0.75 mm per side for a centered opening), not 1.5 mm per side.
  `get_container_details()` currently overwrites the clearance with 1.5.
- Wall, outside border, and divider thicknesses are all hardcoded to 1 mm in
  `get_basic()`.
- Overall dimensions are:
  `X = (container_width + clearance) * column + divider * (column - 1) + 2 * border`;
  `Y = (container_height + clearance) * row + divider * (row - 1) + 2 * border`;
  `Z = container_depth + clearance + wall`.
  Thus the baseline bodies are 89.5 x 29.5 x 111.5 mm and
  178 x 58 x 111.5 mm respectively.
- Start with one positive rounded-rectangle body. Place a negative
  rounded-rectangle cutout in every grid cell. Grid positions are centered about
  the supplied X/Y position; rows and columns advance in positive Y and X.
- Body and cutouts both start at the supplied Z and extend 111.5 mm in the
  baseline. The cutouts therefore go through the full body; the extra wall term
  in the depth formula does not currently create a back wall.
- The user confirmed that the open back is intentional because the unit is
  printed face down. A partially or fully closed back is a future possibility
  if the drawer stop can be designed to print without supports. Preserve this
  printing constraint when developing stop or back geometry.
- Existing generated SCAD uses a 5 mm outer corner radius and a 4 mm cutout
  radius (`5 - thickness_wall`).
- Each opening has an added catch tab at its lower Y edge and the starting Z
  end: currently 56 mm wide (`catch_tab_minus = 30`), 7 mm high, 1.5 mm deep,
  radius 2.5 mm. It is added using
  `positive_positive`, which unions it after the main subtraction.
- An enabled, highlighted M3 countersunk test feature is also appended in
  `get_basic()`. Its intended role has not been confirmed.

## Local coding style

- Use procedural Python geometry functions with `thing` and `**kwargs`.
- Read parameters with `kwargs.get(...)`; use descriptive snake_case names such
  as `container_width`, `thickness_wall`, and `drawer_divider`.
- For a component, copy kwargs into `p3` with `copy.deepcopy`, set its `type`,
  `shape`, dimensions and position, then call `oobb.append_full(thing, **p3)`.
- Copy positions into `pos1` before offsetting them; preserve the caller's input.
- Geometry uses millimetres, `size = [wid, hei, dep]`, and `pos = [x, y, z]`.
- `positive`/`p` adds geometry; `negative`/`n` subtracts it;
  `positive_positive` adds geometry after subtraction.
- `m = "#"` is a preview highlight, not a disabled component. Highlighted
  cutouts still subtract and highlighted positive features still contribute.
- Existing scripts group work in commented `if True` / `if False` blocks. Keep
  focused edits compatible with this style; avoid unrelated cleanup during
  geometry changes.
- The user explicitly prefers a solid body in `working_scad` and one complete
  per-container cutout routine with explicit multiline dictionary definitions.
  Keep the AI opening, floor/ceiling reliefs, both side-wall reliefs and catch
  together in the active `get_container_cutout_ai_version_2()`; do not split them back out
  into frame-wide relief/window helpers. Some repetition is intentional.
  `working_scad` supplies each cell's `row_index` and `column_index` so the
  cutout knows which walls are outside borders. Shared-wall cuts are repeated
  by neighbouring cells and unioned during subtraction. Module-level adhesion
  ears remain in `working_scad`.
- Preserve taxonomy/ID conventions and style-based dispatch. Carry new per-option
  inputs from population through `oobb_details` to the drawing kwargs.
- Validate future geometry changes through the full pipeline and inspect the
  resulting dimensions/geometry. Use `action_validate_ai_version_1.py` for the
  AI trial set; see its report for the checks actually run. Mesh checks do not
  establish physical fit, shrinkage, strength or successful slicing/printing.

## AI version 1 development

The user requested a material-saving, printable large drawer bank on 2026-10-18.
The bed is 400 x 400 mm; multiple units should sit side by side as a larger bank.
Filament, nozzle and target loading remain unspecified. The original 400 mm
printer's usable Z height is unspecified; additional A1 mini and P1P options use
their published 180 mm and 256 mm Z limits respectively.

Read `AI_VERSION_1.md` for the design, parameters, test-piece IDs, verification
results and physical test sequence. All AI options and defaults are declared in
`working_oomp_populate.py`, carried through `oobb_details`, and rendered via
`working_scad.get_ai_version_1()` plus the dedicated cutout module.

The current implementation is a single-piece face-down frame with stepped
through-openings, front catches, continuous lip shelves and relief windows closing at >=45 degrees
to the bed. It has no clamshell or fastening hardware. Do not claim the adjacent
modules are mechanically joined. The sample bank gap is 0.4 mm, and the seam is
wider than an internal divider. The large option is 4 x 12 drawers, with a
360.2 x 354.6 x 110.5 mm finished frame envelope. With removable adhesion ears,
the current print envelope is 360.2 x 395.6 x 110.5 mm.

After reported bed-adhesion trouble, the user requested a 4.5 mm catch angled
up from the base and sizeable removable corner ears. The subsequent stop revision
increased AI catches to 6 mm into the opening over 6 mm of print height, with a
further 1.5 mm tip thickness. The front band is now 7.5 mm (rear remains 6 mm).
Both shallow layout options now use `test_depth=7.5` to contain the complete
ramp and tip; full-frame envelopes and printer grids are unchanged. These
population defaults apply to both 100 ml and 550 ml AI frames.
Four 20 mm diameter x 0.6 mm thick pads are attached outside each module's
top/bottom corners by 5 mm wide x 0.3 mm high breakaway necks, with a 0.5 mm gap
elsewhere. `adhesion_ears` and `ear_*` controls are in population. Bed checks
include the ears, with a 2 mm margin beyond them. Neck height must suit the
actual first layer; attachment/removal and adhesion remain physical test items.
All AI trials include these features. The basic-style geometry is unchanged.

The user subsequently introduced `get_container_cutout_ai_version_2()` and routed
the existing `ai_version_1` style to it. Preserve the two-piece opening: a full-width
12 mm high channel plus a full-height body channel inset 5.5 mm on each side.
`depth_lip=12`, `inset_lip=5.5`, and `lip_cutout_radius=1` are now population
parameters; nominal container clearance remains 1.5 mm. The active revision keeps
a 3 mm thick continuous shelf above the step (`lip_shelf_thickness`) and 1 mm
below it at the root. Separate side windows remove material above and below this
protected band, including through the thick shoulder above it. Edge rails are
10 mm; `middle_rib_width=0` produces one wide floor/ceiling window, with no centre
support. Positive middle_rib_width remains an optional trial setting. The old
AI version 1 function is an inactive historical reference, not the active design.

Validation includes sampled exported-mesh sections checking shelf/root material,
clearance below the bearing face, open side reliefs, and absence of the centre
rail. Ten unit tests and all eleven mesh checks passed. Compared with the user's
unrefined stepped profile, CAD volume falls 9.83% for 2 x 2, 13.87% for P1P,
and 16.03% for 4 x 12. These are material measurements, not measured strength.
See `validation_ai_version_1/lip_refinement_comparison.json` and the saved
`before_lip_refinement.json`; all eleven variants were regenerated through the
full pipeline. Fit/strength require physical verification.

Eleven AI variants cover 1 x 1 / 2 x 2 / 4 x 12 frames, three clearance samples,
a paired module layout, a large shallow layout, a continuous-wall reference,
and two printer-specific maximum grids. The population `experiments` list defines
`a1_mini_max` (1 x 4 drawers, 180 x 180 x 180 mm build volume) and `p1p_max`
(2 x 7 drawers, 256 x 256 x 256 mm). Including ears, their print envelopes are
92.3 x 161.2 x 110.5 mm and 181.6 x 249.1 x 110.5 mm respectively. These retain
current clearances, walls, ears and 2 mm bed margins; do not call them maximum
independently of those parameters. The A1 mini cannot fit two current columns
(181.6 mm wide). Printer variants carry `printer` and `build_height` through
OOMP, and validation checks XY margins and Z limits. Ten unit tests and eleven
mesh checks passed this revision. Source specification links are in AI_VERSION_1.md.
Keep test variants in the same pipeline, with distinct taxonomy_9 values to avoid
ID collisions. Derived AI parameters and validation live in `working_scad.py`;
AI clearance does not inherit the basic helper's hardcoded override.

`python action_validate_ai_version_1.py` regenerates the full pipeline, exports
the AI STLs and previews, checks meshes, and refreshes navigation. Unit checks:
`python -m unittest discover -s tests -v`. Reports are in
`validation_ai_version_1/report.json` and per-part `validation.json`.
`3dpr` files are print-oriented; generated `preview_scene.scad` is presentation
only. Material-saving percentages compare equal-envelope AI frames, not the
thinner original basic frame. Shrinkage compensation must follow measurements;
none is assumed or baked into CAD.

## Systempak 214 / 550 ml addition

Added 2026-10-18 at the user's request. Three further `ai_version_1` options in
`working_oomp_populate.py` use container
`packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214`:
standard 1 x 1, `a1_mini_max` 1 x 1, and `p1p_max` 2 x 2. The mini stays a
separate printer-tagged record even though its geometry matches the standard.
The 550 ml container maps to X=86, Y=95-3=92 (lid removed), Z=108 mm in
`get_container_details()`. The user confirmed the same top/lip profile as the
100 ml container, so reuse the active complete stepped cutout with unchanged
lip supports, catches, relief rules and ears. Do not scale the lip profile with
the taller container height. Including ears the 1 x 1 envelope is
92.3 x 139.3 x 109.5 mm and the 2 x 2 envelope is 181.6 x 234.6 x 109.5 mm.
Printer maxima include the existing 2 mm bed margins and Z limits. There are
now fourteen AI variants and twelve unit tests; all twelve unit tests and all
fourteen exported-mesh validations passed. Historical eleven/ten counts above
describe earlier revisions. See `AI_VERSION_1.md` for the new models.

The user then requested that thick lip shoulders stop at the same height as on
the 100 ml design, instead of continuing down the entire taller body. Population
now carries `lip_support_reference_height=26` (lidless reference body height).
The support region includes clearance: 27.5 mm total, or 15.5 mm beyond the
12 mm lip step. The active per-container cutout opens the remaining 66 mm of
the 550 ml cavity to full width for the complete insertion depth, including
front/rear bands, retaining thin side walls and rounded far corners. Keep the
3 mm bearing shelf/root protected and all 100 ml geometry unchanged. The new
unit test checks reference height across clearances; mesh section checks also
sample front/rear bands for removed shoulders and retained thin walls.
All thirteen unit tests and fourteen mesh validations passed after the full
pipeline. CAD volume including ears fell 32.10% for each 550 ml 1 x 1 and
38.88% for its P1P 2 x 2; all eleven 100 ml volumes stayed unchanged. The
comparison is saved in `validation_ai_version_1/shoulder_height_limit_comparison.json`.

## User confirmations from the initial review

Confirmed on 2026-10-18: use containers without lids (26 mm body height), retain
the intentional open back in the current face-down print design, and consider
future partial/full back closure only with a drawer stop that needs no supports.
No geometry changes were requested or made during this initial review.
