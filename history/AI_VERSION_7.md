# Version 7 — rectangular through-panel connector development

Development version advanced from 6 to 7 on 2026-10-31 at the user's request.
The immutable pre-development release is `releases/ai_version_6/manifest.json`;
run `python action_lock_version_6.py` to verify it. Existing V6 cabinets remain
available. V7 begins with physical connector coupons, before cabinet adoption.

Intent: common rectangular through-holes for printed and flat laser-cut faces,
small exposed snap heads, easier insertion and tolerance of imperfect printing,
and a screw beam with an outside adapter using that same hole. Printed drawer
stops retain their angled slide-on surfaces; laser-cut stop outlines are solid
through the sheet thickness. Sheet thickness and laser kerf need calibration.

The user confirmed **6 mm MDF**, and explicitly requested a printable receiver.

## First physical trial

Population owns the `through_panel_mdf_6_test_card` record. Run
`python action_validate_v7.py` for populate → OOMP → SCAD → mesh/DXF exports
and validation. Its part folder contains `v7_test_card.zip` and a separate
`v7_prototype_faces.zip`. Tests are hidden from complete-cabinet comparisons.
Short-path copies of the deliverables are in `output_v7/`. The SCAD stage
also emits all three laser DXFs directly, with explicit millimetre units in
DXF R2010 and closed polylines on a CUT layer.

Print `3dpr.stl` once for all nine clips, `receiver_6_0.stl` once and
`screw_test.stl` once. Optional `receiver_5_8.stl` and `receiver_6_2.stl`
simulate sheet variation. `receiver_laser.dxf` cuts the same receiver from MDF;
the SVG maps its five holes. Keep supplied print orientations and production
PETG settings. Numbers face upward. Separate sample files are spares.

Start at **44 in the centre 7.6 × 4.6 mm hole**, then compare 41 and 47 for
spring effort. Compare the neighbouring numbers for axial play. Then compare
the five holes to find the closest reliable lateral fit on your printer/laser.
Do not force a clip that cannot recover behind a thicker panel.

| Samples | Arm thickness | Axial clearances across each group |
| --- | ---: | --- |
| 40 / 41 / 42 | 1.2 mm | 0.10 / 0.25 / 0.40 mm |
| 43 / 44 / 45 | 1.5 mm | 0.10 / 0.25 / 0.40 mm |
| 46 / 47 / 48 | 1.8 mm | 0.10 / 0.25 / 0.40 mm |

All five receiver holes are 4.6 mm high. Widths are 7.2 / 7.4 / 7.6 / 7.8 /
8.0 mm, giving nominal neck clearance of 0.05 / 0.15 / 0.25 / 0.35 / 0.45 mm
**per side** around a 7.1 mm neck. Smaller holes reduce wiggle and increase
insertion deflection; wider holes tolerate more print error but increase play.
The central hole is a starting point, not a selected production fit.

Measured stock thickness changes the end clearance directly: shoulder reach
minus actual thickness. For example, sample 43 has 6.10 mm reach and cannot
fully recover behind a true 6.20 mm panel at its hard seating stop. Sample 44
has 6.25 mm reach: 0.25 mm play on 6.00 mm stock, 0.05 on 6.20 and 0.45 on
5.80. Record thickness, hole width, insertion effort, click, side/end play,
removal, cycle count and damage in `results.csv`; regeneration preserves it.

## Research and design reasoning

The current sample-37 feedback establishes a preferred *seated fit*. The latest
feedback says installation is difficult and print variation is poorly tolerated;
it does not establish a material strength or fracture result.

The new joint puts both retaining shoulders **outside** a straight rectangular
hole. The sheet needs no internal recess, taper, flexible tab, countersink or
post-machined pocket. Two spring arms extend into the beam; rigid outer bearing
strips provide the inside axial stop, and a centre pilot carries vertical
locating contact. Arms flex sideways in the XY print plane, with generous open
slots and rounded ends. Relief cuts overlap by 0.05 mm to avoid coincident faces.
The arms are 0.05 mm thinner within their outside root-relief region; labels
specify their nominal tongue thickness. Rounded inner slot roots are 0.6–0.9 mm.

The conservative free spring length is about 16–17 mm, measured after the
rounded roots, instead of the old 6.5 mm root-to-shoulder span. A 35° entry
ramp reduces the geometric wedging factor; a square retaining face resists
withdrawal until the hooks are squeezed. At the central hole the hook overlap
is 0.55 mm per side. Tip exposure is approximately **1.69 / 1.84 / 1.99 mm**,
depending on axial allowance. These are trial dimensions, not proven minimums.

[Protolabs' own design guidance](https://www.hubs.com/knowledge-base/how-design-snap-fit-joints-3d-printing/)
supports reducing root stress, choosing layer orientation, providing locating
features and avoiding sustained latch deflection. Its nominal FDM clearance
recommendation is general guidance, not a guarantee for this PETG process.
Its suggested root radius of at least half the arm thickness is met by the
softest trial; the two thicker trials have smaller ratios because they share
the compact pilot/neck envelope. This is an explicit prototype compromise to
assess in cycling, not a claim of optimal fatigue design.

[Formlabs' enclosure example](https://formlabs.com/blog/designing-3d-printed-snap-fit-enclosures/)
also shows external openings as a way to gain cantilever length and separate
alignment lugs. Its resin/process examples do not supply PETG force ratings.

For a uniform cantilever, the screening relations are
`strain ≈ 1.5 × thickness × deflection / length²` and
`stiffness ∝ width × thickness³ / length³`. The metadata records these proxies
for each trial. They explain why more spring length is preferable to relying
only on thinner, fragile arms. They omit root compliance, contact friction,
anisotropic printing, nonlinear material behaviour and fatigue. No numerical
proxy here is a measured force, permissible PETG strain or safety rating.

Tapered arms, folded/U springs and a separate replaceable latch were considered.
The first card keeps constant nominal arm sections to isolate thickness and
fit effects. Folded springs and separate latches add slots, pieces and uncertain
printing behaviour. A self-adjusting sloped retaining face could take up stock
variation but introduces sustained flex and a possible pull-out ramp. The
first card therefore uses square retaining shoulders with explicit thickness
trials. If the loose-hole fit still rattles, the next experiment should test
separate light preload features rather than making the main hooks harder to fit.

[BRM Lasers explains](https://support.brmlasers.com/en/materials-and-parameters/materials/kerf-and-kerf-compensation)
that uncompensated holes grow with kerf, and that kerf varies with stock,
focus and settings. DXFs describe **finished nominal geometry** in millimetres.
Measure actual MDF thickness and cut width; apply compensation once in CAM.
Do not pre-offset this file and also apply a CAM offset. No universal kerf or
laser power/speed is assumed. Mark hole widths by hand from the supplied map.

## Screw option

The separate coupon retains the V6 approach: a beam with side-loaded OOBB M3
nut and an external OOBB countersunk adapter. It uses the same centre rectangle.
Two guide cheeks enter from outside and fit within the hole for their entire
depth; the flange stops outside, the beam stops inside. The centre is open
between the cheeks, avoiding fragile bore slivers. Print the countersink face
down and the cheeks up. Use one M3 × 20 countersunk screw and one M3 nut.
The 2.4 mm flange, 6 mm sheet and 7–10 mm nut pocket leave nominally 1.6 mm
of screw beyond the nut. MDF compression, head seating, torque and edge
durability need physical checks.

## Front-panel manufacturing prototypes

Both current grid sizes have V7 prototype face outputs. Their envelopes stay
197.8 × 220.3 and 376.4 × 376.8 mm; “square layout” refers to this development
family and does not silently restore the superseded 300 mm square or pad grids.

`front_small/large_laser_2d.dxf` have only closed flat CUT contours. The drawer
stops are solid across the 6 mm sheet. The matching `front_small/large_printed`
files keep the existing angled slide-on stops and 12 mm inward floor-support
extensions, reaching 18 mm overall face depth. Their rectangular receivers
share the candidate interface. These are manufacturing/fit prototypes: no
full-length V7 rail or final latch is adopted before the user's tests.

A flat MDF sheet cannot reproduce the printed 12 mm inward floor supports.
The surrounding enclosure or a later separate support must supply any required
floor bearing; that dependency needs resolution before complete-unit release.
V6 rails do not fit the new rectangular receivers. Existing V6 files and kits
remain protected by the release lock.

## Verification scope

The validator checks watertight meshes, component counts, bed contact, coupon
bed limits, exact receiver openings, nominal seated fits, retaining and seating
contact, prescribed insertion flex, thickness sensitivity, rigid adapter
insertion, screw path and side-loaded nut capture. It checks both face types,
constant laser thickness and the exported DXF contours against flat mesh
sections. See `validation_v7/report.json` for completed results.

These checks do not establish physical insertion force, repeated-cycle life,
MDF edge wear, printing quality, creep or full-unit load capacity. Select a
clip only after physical feedback, then carry that selection from population
through OOMP and SCAD into full rails and cabinet validation.

Completed on 2026-10-31: **93 source tests, nine comparison tests, 20 watertight
mesh views and three DXFs pass**. All nine nominal joints pass seating,
retaining contact, prescribed insertion and thickness-response probes. Sample
44 also passes geometric insertion and retention in all five calibration holes.
The screw guide inserts rigidly from outside; beam/flange seating stops,
the full bore path, side-loaded nut and axial nut capture pass. Both prototype
face grids have all 21 / 60 rectangular receivers. DXF contours agree with mesh
boundaries within 0.0011 mm (export rounding), with explicit mm units, closed
contours and no duplicate segments. All 64 previous models / 613 geometry files
remain locked. Clip, receiver, screw, printed-face, laser-face and overview
previews were visually inspected. Physical test results are still pending.
