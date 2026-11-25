# Flush twin-tab thickness trials: 23–26

The user selected **28 as the main snap standard** on 2026-10-20:
1.8 mm arms, 0.25 mm per-side clearance and 0.2 mm axial clearance.
The numbered trials remain unchanged. Tiled v5 rails use these settings with
the existing matching tab/receiver bevels; that adaptation needs a fit print.

## Heavier follow-up bed

The user reports **23 and 24 are too narrow**. The additional
`recessed_twin_heavy_suite` folder contains one `3dpr.stl` with:

| Bed position | Number | Arm thickness | Open centre gap |
|---|---:|---:|---:|
| Upper left | 25 | 1.4 mm | 4.0 mm |
| Upper right | 26 | 1.6 mm | 3.6 mm |
| Lower left | 28 | 1.8 mm | 3.2 mm |
| Lower right | 29 | 2.0 mm | 2.8 mm |

27 is already the separate locking-key test. Each of these four pairs has
recessed numbers on both pieces. 25 and 26 are unchanged controls. Print the
combined file once for all eight pieces, using the same poses and PETG profile
as the earlier suite. Individual `trial_XX`, `rail_XX`, and `plate_XX` files
remain available.

The added material grows inward; outer fit, hooks, receiver, clearances and
free arm length remain fixed. The slot-root radius follows the narrower gap.
Try 25, 26, 28, then 29 with fresh matching receivers. Check that both catches
recover and the beam seats flush. These thicker variants still need physical
fit testing.

Validate with `python action_validate_latch_thickness.py --heavy`: all 18 views,
four pairs, arm sections, centre clearance, prescribed-flex insertion, retention,
labels, quantities, bed contact, and unchanged 25/26 CAD are checked.

## Original suite

The user reports that **sample 19 worked well** and wants thicker latch arms
for mainly permanent PETG connections. This is qualitative fit feedback, not
a measured strength or load rating.

| Number | Arm thickness | Open centre gap | Purpose |
|---|---:|---:|---|
| 23 | 1.0 mm | 4.8 mm | Sample-19 geometry control, new number |
| 24 | 1.2 mm | 4.4 mm | First thickness increase |
| 25 | 1.4 mm | 4.0 mm | Second thickness increase |
| 26 | 1.6 mm | 3.6 mm | Thickest initial trial |

The outside tab faces, 1.2 mm hooks, 6 mm free length to the catches, 7.5 mm
receiver thickness, 0.25 mm side clearance and 0.2 mm axial catch clearance
stay unchanged. Each tab still needs nominally 0.95 mm inward movement during
insertion. Material grows into the centre gap. The rounded slot end follows
that narrower gap, so its radius also reduces; its centre remains 0.5 mm into
the beam. There is no middle guide or separate locking key.

The original 19, earlier connector trials and complete drawer demonstrations
retain their existing inputs and CAD. No cabinet adopts the thicker arms yet.

## Printing and choosing

The new `recessed_twin_fit_suite` folder under `parts` contains:

- `3dpr.stl` / `3dpr.scad`: eight pieces, four matched pairs, arranged **23 24 /
  25 26** on one bed. This fits the A1 mini as well as larger beds.
- `trial_23` through `trial_26`: one pair per file.
- `rail_XX` and `plate_XX`: individual replacements.
- `assembled` and `assembled_XX`: inspection references, not single-piece prints.
- `trial_index.csv` and `connector_test.json`: the numbered settings.

Numbers are recessed 0.6 mm into both the rail and receiver. Receivers have
identical functional geometry, but matched pairs make testing easy to record.
Use a fresh receiver for each insertion instead of wearing one receiver through
all four tests.

Keep the successful sample-19 PETG profile and the supplied orientation:
**receiver entry face down; rail on its long flat face**. Inspect the slicer
to confirm each arm is preserved. Do not place supports in the spring slot or
catch pocket.

Start with 23 as the control, then try 24, 25 and 26. Record:

| Number | Seating effort | Both hooks recovered? | Flush seating / play | Whitening or cracking | Retention |
|---|---|---|---|---|---|
| 23 | | | | | |
| 24 | | | | | |
| 25 | | | | | |
| 26 | | | | | |

Thicker arms can increase seating force and may break before they latch;
single-use intent does not remove the insertion-strain requirement. Choose
from observed seating and retention, not thickness alone.

## Source and checks

Population owns `get_ai_version_5_latch_trials()` and the suite option.
`working_scad` arranges the existing solid coupon bodies; the complete
`get_container_cutout_ai_version_5()` routine still carves the tabs and labels.
The wider arm-thickness allowance applies only to numbered trials 23–26;
sample 19 retains its original parameter limits.

Run `python action_validate_latch_thickness.py` for the complete
populate → OOMP → SCAD pipeline and validation. `--skip-generation` checks the
existing generated CAD. Checks cover 18 meshes, eight separate print pieces,
bed contact, unsupported downward faces, actual arm section thickness,
identical receivers, flush seating, retaining shoulders, prescribed deflected
insertion, engraved numbers and exact quantities. Prescribed flex checks
geometry only; they do not predict PETG forces, fracture, creep or durability.

`validation_latch_thickness/previous_v5_baseline.json` protects all eleven
prior v5 records and 180 SCAD files, including the tiled demonstrations.
Do not rewrite this baseline or any earlier release manifests.

Validation passed for all 18 mesh views and four pairs, 57 geometry unit tests,
eight comparison tests, and all prior release/input/CAD baselines. The rendered
numbered bed was inspected. These checks do not replace the physical trial.
