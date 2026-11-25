# V7: compare mechanisms before tuning clearance

The user rejected the fixed centre tongue and requested thicker outside fingers,
a narrower hole, and a variety of techniques rather than more size variants.
This second card follows that direction. V7 remains experimental; no complete
cabinet latch has been selected. The first card (40–48) is preserved separately,
with its inputs and 45 CAD/mesh/archive files protected by
`validation_v7_four_finger/previous_five_finger_baseline.json`.

## Print and compare

`output_v7_four_finger/v7_mechanism_card.zip` contains the printable kit,
printable receiver, MDF DXF, screw reference, instructions and results sheet.

Print `3dpr.stl` once: **four numbered clips plus one separate locking key**.
Print `receiver_6_0.stl` once and `screw_test.stl` once. Keep the supplied flat
orientations; numbers face up. Use the production PETG settings. Separate
sample and key files are spares. None of the parts needs designed supports.

| Sample | Technique | What to compare |
| --- | --- | --- |
| 50 | Straight cantilever arms | Control for ordinary push-to-snap and squeeze-to-release |
| 51 | Tapered arms: 1.8 mm root, 1.2 mm tip | How distributing the bend changes insertion, release and durability |
| 52 | S-shaped arms | A curved spring path within the beam, with the same interface |
| 53 | Snap plus a removable blocking key | Separate locking action that prevents the hooks squeezing inward |
| M3 | Beam and outside adapter with screw/nut | Positive screw fastening through the same hole |

The four clips share the same hook, neck, axial fit and nominal panel opening.
This is **a mechanism comparison**, not a clearance matrix. All five receiver
holes are identical **6.0 × 4.6 mm**, labelled 50 / 51 / 52 / 53 / M3. There is
no need to use a different hole size for each technique. The neck is 5.5 mm
wide, nominal side clearance is 0.25 mm per side, axial play is 0.25 mm on a
true 6.00 mm sheet, and hook overlap is 0.55 mm per side. The clip tips project
approximately 1.84 mm beyond that sheet.

Each clip has two inner hooked arms and two outer seating strips. **There is
no fixed centre tongue.** The opening narrows from 7.6 to 6.0 mm, a 1.6 mm
reduction. Keeping the 11 mm beam width makes the outside strips about 1.75 mm
wide instead of 0.95 mm; the rounded root cut reduces their local minimum
slightly. The outer strips stop at the inside face and carry the axial seating
contact. Only the inner hooks pass through. The hooks also locate vertically
in this prototype; a centre pilot no longer carries that contact.

Insert from the unlabelled inside of the receiver. For 50–52, squeeze the
exposed hooks to remove. For 53, snap it in first, then slide the separate key
between the arms from outside. Pull the key out before squeezing the hooks.
The key blocks inward movement but is intentionally removable and loose:
captive/anti-loss retention is not developed. This is not a force-free
insertion mechanism. Its head reaches about 3.2 mm outside, trading a separate
locking action for more protrusion. It is an optional moving component, not
a permanent fifth finger. Compare 53 with and without its key.

The M3 reference uses one M3 × 20 countersunk screw and one M3 nut, not supplied.
Side-load the nut, seat the beam inside and put the adapter through the hole
from outside. Its guide is narrowed to 5.7 mm. The two guide cheeks are about
0.95 mm wide; they locate the screw adapter while the flange and beam carry
the clamping load. Their print quality needs checking. Print the countersink
face down and cheeks up. Nominal screw projection beyond the nut remains 1.6 mm.

Record insertion effort, release effort, play, repeated-use behaviour and any
damage in `results.csv`; regeneration must never overwrite it. Use the same
receiver and print settings for all concepts and avoid tuning individual fits
during this first comparison. If a concept cannot be tested because of an
obvious print defect, record that as useful feedback.

## Manufacturing and rationale

The printable receiver and MDF DXF have the same five nominal holes. DXF uses
closed CUT contours and explicit millimetres; apply measured kerf once in CAM.
Measure actual MDF thickness. Nominal CAD clearance is not measured fit.

The first card's sourced research is in `AI_VERSION_7.md`. The tapered concept
follows the general design principle of spreading bending along a cantilever.
The S-shaped concept explores a different spring path; its benefit over the
straight version is a hypothesis, not a measured reduction in effort. The
key concept adds a separate positive obstruction to hook release. The screw
reference provides the existing alternative locking method. No material-specific
force or fatigue rating is inferred from general snap-fit literature.

Prototype face outputs for both current grids use the narrower opening.
Printed versions retain the angled stops and inward floor extensions; MDF
versions retain solid stop outlines across the sheet. These are demonstrations,
not a complete-unit release: full rails and MDF floor support remain unresolved.

## Regeneration and validation

Run from the project root:

`python action_validate_v7.py --variant four_finger_mechanism_card`

This runs population → OOMP → SCAD, exports meshes and DXFs, checks the old V7
card and all V1–V6 release locks, probes the nominal joints, verifies four-finger
sections and the absent centre tongue, and checks the key and screw paths.
Reports go in `validation_v7_four_finger/`; deliverables go in
`output_v7_four_finger/`. Curved-arm deflection is prescribed kinematics for
collision screening, not an elastic or force simulation. Physical PETG fit,
force, fatigue, MDF wear, key retention and full-unit loading remain unverified.

Completed on 2026-10-31: **96 source tests, nine comparison tests, 14 watertight
mesh views and three DXFs pass**. All four snaps pass nominal seating,
retaining/seating contact and prescribed insertion probes. Actual sections
show four fingers, an open centre and 1.75 mm outside strips at the checked
beam section. Mesh sections confirm that 51 and 52 differ from the control,
while 53 uses the control snap plus its separate key. The key seats and inserts
without collision and blocks the prescribed release compression. The screw
adapter seats and inserts rigidly; the screw bore and side-loaded nut path and
capture pass. Both prototype face grids have their 21 / 60 narrower holes.
DXFs pass structural audits and contour matching. All V1–V6 locks and the first
V7 card's 45 protected files pass. Clip, receiver, screw, printed-face,
laser-face and mechanism overview previews were visually inspected.
