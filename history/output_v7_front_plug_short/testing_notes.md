# V7 sample 71: half-depth spring slots with the preferred friction cover

The user endorsed the friction-plug direction and requested half the bending
distance inside the beam. This is a geometry preference, not a new measured
fit or strength result. Sample 71 halves the nominal slot depth behind the
inner panel face from **14 mm to 7 mm**. Preferred sample 70 remains intact.

The hook, 1.2 mm arm tips, full-squeeze insertion requirement, upper bearing,
5.2 × 5.2 mm receiver, and smooth friction cover are retained. There are no
plug detent bumps or matching arm pockets. The plug still spreads each arm
0.1 mm and covers the front; the inner shoulders still reach 7 mm high.

The radius at each slot root is retained. Consequently, the conservative free
span inside the beam changes from 11.6 to 4.6 mm; the total free span to the
retaining shoulder changes from 17.7 to 10.7 mm. The *slot penetration into
the beam* is halved; the panel thickness and projecting hook length are not.
The shorter arm should be stiffer and may need more insertion force. The
existing strain/stiffness proxies are only geometry screens, not PETG limits.

## Print

If you already have sample 70, print **only `sample_71.stl`**. Reuse its friction
plug and 5.2 × 5.2 mm receiver. Otherwise print `3dpr.stl` once for the new
clip plus its plug, and `receiver_6_0.stl` once. Individual files are spares.
Keep the supplied long-face-down clip and cover-face-down plug orientations.

Push the clip in from inside, then press the smooth cap in from outside.
Compare effort, any root damage, play and frictional plug retention against 70.
Record results in the new part's results.csv, which is never overwritten.

## Source and verification

Population owns `front_spreader_plug_short_test`, the sixth V7 option, with
`spring_root_y=-7.0`. Regenerate using:

`python action_validate_v7_front_plug.py --short`

This runs population → OOMP → SCAD and verifies actual shortened slots, full
arm-tip contact, insertion/capture, upper bearing, friction-only cap insertion,
no arm pockets and no plug bumps. It also checks that the existing friction
plug STL is byte-identical. Reports go in `validation_v7_front_plug_short/`;
deliverables go in `output_v7_front_plug_short/`.

`previous_sample_70.json` and `previous_sample_70/` preserve the preferred
friction sample's inputs, CAD, meshes, archive and source. Earlier V7 and
V1–V6 locks remain mandatory. Physical force, failure, creep and frictional
retention of the shorter spring remain unverified. No full rail is selected.

Completed: **106 source tests, four closed mesh views and one DXF pass**.
Actual sections show the old slot region at 10 mm depth filled and four
fingers within the new 7 mm region. Full contact, 95%-closure rejection,
insertion, upper bearing and friction-cap seating pass. The plug STL is
byte-identical to 70; that preferred sample and all earlier locked geometry
remain unchanged. Print and engineering previews were visually inspected.
