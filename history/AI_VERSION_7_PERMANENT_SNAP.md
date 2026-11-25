# V7 permanent full-squeeze snap trial, samples 60–62

Physical feedback: the previous clip-in hooks were insufficiently aggressive,
and all tested receiving holes were too large. The user requests hooks that
force the two middle arms completely together during insertion, intended as
**a permanent, one-time push-in fitting**. No fracture, pull-out force or other
measured result was reported.

## What changed

| Feature | Previous mechanism card | New permanent trial |
| --- | --- | --- |
| Receiver opening | 6.0 × 4.6 mm | **5.2 × 4.2 mm** |
| Free neck width | 5.5 mm | 4.8 mm |
| Hook projection per arm | 0.8 mm | **1.4 mm** |
| Recovered hook-head width | 7.1 mm | **7.6 mm** |
| Retaining overlap per side | 0.55 mm | **1.2 mm** |
| Inward travel per arm | 0.55 mm geometrically, plus simulation margin | **1.2 mm to full contact** |
| Axial allowance | 0.25 mm | 0.10 mm |
| Retaining land | 0.35 mm | 0.8 mm |

The 1.2 mm-thick arm tips begin with 2.4 mm between them. Each moves inward
1.2 mm, leaving **zero gap at the hook section**. The closed head is exactly
5.2 mm wide, matching the new receiver. This is intentional nominal contact;
the validation must not force the arms through each other to make it pass.
The reduced hole height leaves 0.1 mm nominal clearance above and below the
4.0 mm-high tongue. All three receiver holes share this one revised fit.

Retaining faces have a 0.15 mm back-rake: the outer corner is closer to the
panel than the neck corner. They have no reverse withdrawal ramp or release
pads. The broad lands give the larger heads more material. The 45° entry
ramp and 0.8 mm land make tip exposure about 2.4 mm outside a 6 mm panel.

## Three mechanisms, same aggressive latch

- **60:** straight 1.2 mm arms.
- **61:** 1.8 mm roots tapering to the same 1.2 mm tips.
- **62:** S-shaped 1.2 mm spring arms.

The four-finger layout remains: two hooked inner arms and thicker rigid outer
seating strips. The outside strips are about 2.1 mm wide. There is no centre
tongue. The narrowed receiver and new barbs are not applied to a full cabinet
before these tests. The previous loop, screw and removable-key experiments
remain separately available; this card concentrates on the permanent snaps.

## Print and test

Download `output_v7_permanent_snap/v7_permanent_snap_test.zip`. Print
**`3dpr.stl` once** for the three numbered specimens and
**`receiver_6_0.stl` once** for their three-hole card. Here `6_0` denotes the
receiver's 6 mm panel thickness; its holes are **5.2 × 4.2 mm**. Use this new
receiver rather than an older card. Individual sample files are spares.
Use the supplied long-face-down PETG orientation and normal production settings.

Insert each sample from inside until the beam shoulders seat and the hooks
recover outside. Observe whether the arm tips meet, whether it clicks and
how much play remains. Record the outcome in results.csv, which regeneration
preserves. Expect removal testing to sacrifice a clip or its receiving card.
Record what fails and where during a destructive withdrawal attempt.

If the tips meet but the printed head still will not enter, record that result
rather than forcing it beyond the contact stop. Nominal zero clearance at
maximum squeeze makes print-size error consequential. The arms cannot move
farther without contact deformation. This is a mechanism/retention trial,
not a claim that every print will assemble.

The intended use is permanent assembly under normal withdrawal. **CAD cannot
establish that removal necessarily causes damage**. The exposed hooks may
still be reachable with a tool; there is no designed service-release action.
Physical pull tests, creep and MDF edge damage determine whether it behaves
as a satisfactory one-time-use fitting. No retention force or material strength
rating is assigned.

`receiver_laser.dxf` provides the same three holes in nominal 6 mm MDF, in mm,
with closed CUT contours. Apply measured kerf compensation once in CAM.

## Source and validation

Population owns `permanent_full_squeeze_snap_test`, the fourth V7 option.
Bodies remain in `working_scad`; removals stay in its V7 container cutout.
Run **`python action_validate_v7_permanent_snap.py`** for
populate → OOMP → SCAD → exports and checks.

The validator checks actual mesh head width, complete tip contact, no arm
interpenetration, failure to pass at 95% closure, passage at full closure,
recovered seating/retaining contact and the smaller holes in both axes.
Prescribed flex is a kinematic collision screen, not a force/stress simulation.
Reports go in `validation_v7_permanent_snap/`.

`previous_v7_baseline.json` protects all three preceding V7 records and their
118 SCAD/STL/ZIP files, with copies under `previous_parts/`. Existing V1–V6
release checks remain mandatory. Never update an old baseline to pass a new
design, and never rewrite historical results to claim later geometry passed.

Completed on 2026-10-31: **102 source tests, nine comparison tests, five closed
mesh exports and one DXF pass**. All three actual meshes close to within
0.000001 mm at the arm tips, with zero measured arm-intersection volume. Their
closed heads measure 5.2 mm; full closure passes the insertion sweep, while
95% closure produces about 0.397 mm³ receiver interference. Recovered seating,
back-raked retaining contact and reduced vertical clearance pass. The DXF has
four closed contours, declares mm and matches the printed receiver section.
All three prior V7 records / 118 files and V1–V6 locks remain unchanged. Clip,
receiver and corrected full-contact diagram previews were visually inspected.
Physical one-time retention and destructive-removal results are still pending.
