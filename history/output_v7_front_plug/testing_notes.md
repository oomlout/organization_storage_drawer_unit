# V7 sample 70: upper bearing support and a front expansion cover

Current revision: **friction-only**, at the user's explicit request. The
retaining ribs and matching arm pockets have been removed. The superseded
detented sample-70 files and source are preserved under
`validation_v7_front_plug/superseded_detent_70/`.

The user requested taller vertical support that bears above the receiver,
a slightly taller hole, and a front plug that covers the opening and presses
the arms wider. They confirmed that the new support should reach the top of
the hole as well. This test uses the straight-arm permanent snap as its control.

## Print and assembly

Print `3dpr.stl` once for **one sample-70 beam end plus one front plug**.
Print the **new `receiver_6_0.stl`** once. Its hole is **5.2 × 5.2 mm**, in a
6 mm-thick panel; the previous 4.2 mm-tall hole is too short. Individual
`sample_70.stl` and `front_plug.stl` files are spares.

The tongue is now 5.0 mm high, with 0.1 mm nominal top/bottom clearance. The
two outer columns and rear grip rise to **7.0 mm**, providing inside bearing
material above the hole. Orient that extra column height upward in service.
There is no roof over the free spring arms; every print starts on the bed.

1. Push the snap through from inside until its shoulders seat and the barbs
   recover outside. The aggressive hooks still require full arm-tip closure.
2. Align the front plug with the gap between the arms and press it inward
   **from outside**, along the beam axis.
3. The smooth tapered stem spreads each arm 0.1 mm outward. Friction alone
   holds it in place. The neck is 5.0 mm wide during insertion and when seated;
   there is no extra spreading step for a retaining bump.
4. The hollow covering skirt overlaps the complete hole and encloses the
   exposed barbs. Its rim stops against the outside panel face.

The plug is an **expanding brace**, not simply the old removable blocking key.
Its 11 × 8 mm cap has a 2 mm front wall and hollow skirt. Overall front
projection is 4.6 mm beyond the nominal panel face. The cap covers the hooks,
and blocks normal access to them. The arms retain their full section, without
interlock pockets. The preload may creep. Physical tests must establish whether the joint is
sturdier, whether the plug stays seated and whether removal requires damage.

Print the cap's outside face down, with stem upward, as supplied. Print the
beam on its long face, as supplied. Use the production PETG settings. Record
snap effort, plug insertion/pull-out effort, upper bearing, play before/after
and any pull failure in results.csv; it must never be overwritten. If it has
the earlier `detent_click` column, leave that blank for friction tests and
record the revision in notes; the old results remain user-owned.

`receiver_laser.dxf` cuts the same square through-hole in nominal 6 mm MDF.
It declares millimetres and finished CUT contours. Apply measured kerf once
in CAM. This is a connector coupon; no full cabinet rail has been selected.

## Source and verification

Population owns `front_spreader_plug_test`, the fifth V7 record. Geometry
remains in `working_scad`, with complete removals in the V7 container cutout.
Regenerate using:

`python action_validate_v7_front_plug.py`

It runs populate → OOMP → SCAD, exports meshes/DXF and checks actual upper
bearing, top/bottom location, full-squeeze snap insertion, outward spreading,
cover clearance/seating, smooth insertion/withdrawal and blocked recompression.
It checks the actual mesh for removed bumps and restored arm-pocket material.
Reports go in `validation_v7_front_plug/`; delivery files go in
`output_v7_front_plug/`.

The prescribed spreading motion is a geometric screen, not a material model
or insertion-force prediction. Force, stiffness, fatigue, creep, MDF wear and
permanent retention remain physical test questions.

`previous_v7_baseline.json` preserves all four preceding V7 inputs and their
130 SCAD/STL/ZIP files, with copies in `previous_parts/`. V1–V6 release locks
remain mandatory. Never replace an immutable baseline to pass a new design.

Completed on 2026-10-31: **105 source tests, nine comparison tests, four closed
mesh exports and one DXF pass**. Actual upper bearing, top/bottom tongue
location, full-contact snap insertion, the seated 5.0 mm neck, .1 mm outward
spread per arm pass. The smooth plug drive is clear, its cover rim has a seating stop, and the stem
blocks hook recompression. Cap, clip, receiver and engineering previews were
visually inspected. All four earlier V7 records / 130 files and V1–V6 locks
remain unchanged. Physical stiffness improvement, force and permanence remain
unverified.
