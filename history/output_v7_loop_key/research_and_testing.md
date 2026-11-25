# V7 sample 54: rigid loop and a key dropped from above

Added at the user's request, alongside the existing techniques. The beam has
a closed rigid eye that passes through the panel. A separate T key drops
vertically through the exposed eye from above, across the panel opening. Its
head rests on the loop, preventing it falling through. The key bears against
the outside face when the beam is pulled. Lift the key upward to release.
There are no snap arms or prescribed spring deflection in this concept.

## Print only the addition

`output_v7_loop_key/loop_key_addon.zip` contains `loop_key_addon.stl`: one
sample-54 beam end and one short broad-headed T key, two separate solids.
Print it once, flat as supplied, using the production PETG settings. Individual
`sample_54.stl` and `drop_key.stl` files are spares. The key prints on its broad
face, then is turned upright for use. Source print Z does not mean service UP.

Use any existing **6.0 × 4.6 mm** hole from the four-finger card. No replacement
receiver is required. Push the loop through from inside, drop the key through
its eye from above, then compare insertion, axial play, withdrawal resistance
and release with 50–53. The key remains loose and removable; there is no
anti-loss detent. Use gravity to seat it, not a press fit or snap action.

## Combined card

`v7_mechanism_card_with_loop_key.zip` includes the full updated comparison:
50 straight, 51 tapered, 52 S spring, 53 snap + blocking key, **54 rigid loop +
vertical drop key**, and the M3 screw reference. `3dpr.stl` contains FIVE numbered
samples plus TWO different keys: seven pieces. Do not also print the add-on.
Print `receiver_6_0.stl` and `screw_test.stl` once each if needed.

The combined receiver is 150 × 32 mm, with SIX identical 6.0 × 4.6 mm holes,
labelled 50 / 51 / 52 / 53 / 54 / M3. A matching MDF DXF is included. DXF uses
finished nominal contours in mm; apply measured kerf once in CAM. Existing
6 mm receivers remain compatible with all these techniques. Results.csv is
never overwritten by regeneration.

## First nominal dimensions

The loop's through-neck is 5.5 × 4.0 mm. Its rounded eye is 2.4 × 2.2 mm,
with 1.55 mm side walls and a 1.5 mm nose. The T-key stem is 2 × 2 × 7 mm;
its head is 7 × 2 × 1.6 mm. In the nominal 6.00 mm panel, the loop projects
**3.75 mm** outside and the locked joint has about **0.25 mm nominal axial
allowance**, including the clearances between key, loop and panel. Rounded
eye corners can bring contact slightly earlier than that straight-wall stack.

This trades more exposed depth and a separate part for a rigid, low-effort
assembly action. The key needs space above for insertion/removal, and extends
above and below the opening. Check drawer and front-face clearance before a
full-cabinet design. A loose key may lift or fall out if inverted; no transport
or load rating is established. PETG strength, MDF wear and creep need physical
testing. Dimensions can be tuned after comparing mechanisms.

## Pipeline and history

Population owns `loop_drop_key_mechanism_card` and all loop/key dimensions.
Bodies remain in `working_scad`; all removals remain in the V7 container cutout.
Regenerate with:

`python action_validate_v7.py --variant loop_drop_key_mechanism_card`

The command runs populate → OOMP → SCAD, exports the combined and add-on meshes,
checks rigid loop insertion, vertical key insertion/removal, the head stop,
key-to-panel bearing and positive withdrawal capture. Reports go in
`validation_v7_loop_key/`; delivery files go in `output_v7_loop_key/`.

Original four-finger inputs and CAD/mesh/ZIP files are protected by
`validation_v7_loop_key/previous_four_finger_baseline.json` and copied into
`previous_four_finger/`. The initial five-finger card and V1–V6 locks remain
protected too. Do not refresh an old baseline to pass a new revision.

Completed on 2026-10-31: **99 source tests, nine comparison tests, 17 closed
mesh exports and three DXFs pass**. Sample 54 passes rigid insertion through
the shared receiver, vertical drop/lift paths, the T-head fall-through stop,
outside-panel bearing and positive withdrawal capture. The two-piece add-on
matches its individual meshes, and the full seven-piece print conserves their
combined volume. Both earlier V7 cards (45 and 33 protected files) and all
64 previous AI models / 613 geometry files remain unchanged. The new loop
diagram, combined print and receiver previews were inspected. These checks
do not establish physical force, printed fit, fatigue, accidental key lift,
MDF wear or loaded performance.
