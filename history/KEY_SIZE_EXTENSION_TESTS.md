# Larger locking-key tests 20–22

The user selected **27 as the separate-key standard** on 2026-10-20.
Population exposes it through `get_ai_version_5_selected_connector("key")`.
Its original standalone files remain unchanged. Sample 28 is the main direct
snap style used by the tiled units.

## Follow-up: tighter replacement key 27

The user reports **22 is best** and requests a tight latch against the far
face where the key emerges. The standalone `ai_version_5_style_tight_key_27`
folder in `parts/` provides:

- **`key.stl`**: print this alone for the existing 22 beam and plate.
- `3dpr.stl`: key, numbered 27 beam and plate on one bed (39.475 × 47.738 mm).
- `rail.stl` and `plate.stl`: same interfaces as 22, with recessed number 27.
- `assembled.stl`: assembly reference.

The head stop extends toward the tongue and the hook shoulders move inward.
They now capture the 8.75 mm tongue with 0.10 mm clearance on each face,
reducing sideways key travel from 2.45 to 0.20 mm. This is key capture clearance;
the existing through-piece and transverse-slot fits are unchanged.
`key_latch_clearance` lives in population and can be adjusted independently.
Original 22 remains available unchanged.

Use the supplied flat orientation and the successful sample-22 PETG settings.
Seat the beam in the plate, insert the key sideways until its head reaches
the tongue, and check that **both hooks spring back behind the far face**.
Arm thickness remains 1.4 mm; the shorter flexing span will feel stiffer.
The key is unmarked to preserve its section; companion coupons are numbered.

`python action_validate_tight_key.py` runs the normal generation pipeline and
checks five meshes plus compatibility with the original 22 files. Both stops
are clear at 0.09 mm travel and engaged at 0.15 mm; prescribed-flex insertion
has zero mesh collision. The simple cantilever screening estimate is 2.28%
strain, not a material safety limit or force prediction. Physical PETG
insertion, retention, and durability still require a print.

## Original size progression

The user reports that **sample 9 was closest but still loose**, while
**sample 1 was much too loose**. They requested three more examples following
the size progression **3 → 6 → 9**, leaving finer adjustment until later.
This feedback is a qualitative physical fit report, not a measured load rating.

The new samples continue the same **15 percentage-point** size steps.
Clearance stays at sample 9's setting:

| Sample | Key size relative to original | Key slot clearance per side | Key arm thickness | Material above/below key slot |
| --- | --- | --- | --- | --- |
| 9, existing reference | 130% | 0.40 mm | 1.04 mm | 2.00 mm |
| **20** | **145%** | **0.40 mm** | **1.16 mm** | **1.70 mm** |
| **21** | **160%** | **0.40 mm** | **1.28 mm** | **1.40 mm** |
| **22** | **175%** | **0.40 mm** | **1.40 mm** | **1.10 mm** |

This increases key size and changes spring stiffness/engagement. It does
**not** reduce nominal clearance gaps: through-tongue fit stays at 0.25 mm
per side and axial catch clearance stays at 0.20 mm. Record whether the
remaining looseness is sideways, axial, or at the key itself so the next
round can adjust the appropriate dimension.

The rail remains 11 × 10 mm, with a 32 mm grip and 7.5 mm receiver.
The fork, its hooks/root radii, and the matching tongue and key slot scale
together. Sample 22 leaves only 1.1 mm above and below the slot: inspect
these walls in the slicer and treat this as a local fit coupon, not a proven
full-size cabinet joint.

## Files and printing

Find the new folder under `parts/` ending in
`ai_version_5_style_key_size_extension_suite`.

- `3dpr.stl` / `3dpr.scad`: all **three complete sets**, nine separate pieces.
- `trial_20`, `trial_21`, `trial_22`: individual three-piece print layouts.
- `plate_XX`, `rail_XX`, `key_XX`: individual parts for reprinting.
- `assembled` and `assembled_XX`: reference assemblies, not print layouts.
- `trial_index.csv`: exact dimensions and sample numbers.

Numbers **20, 21 and 22** are recessed 0.6 mm into the long rails and matching
plates, readable from above on the print bed. Keep each loose key with its
numbered pair. Print each matched set; larger keys are not intended as
drop-in replacements for sample 9's rail slot.

Use the same PETG and print settings as the earlier trials so the comparison
is useful. Keep the supplied orientation. Compare insertion effort, hook
recovery, sideways/axial play and any whitening or layer damage. The new
samples have not yet been physically tested.

## Source and checks

`get_ai_version_5_key_extension_trials()` in population owns this set.
It copies sample 9's clearances and independently scales the same dimensions
as the original 3/6/9 progression. The original eight v5 records, including
the revised flush twin-tab sample 19, remain unchanged.

Generation remains populate → OOMP → SCAD. Bodies/layouts stay in
`working_scad`; complete cuts and recessed labels remain in the single v5
cutout routine. All 17 views stay in the new main folder.

Run `python action_validate_key_size_fit.py --variant key_size_extension_suite`.
It checks the 17 exported views, three connections, quantities, bed contact,
recessed labels, retained slot walls and prescribed key-flex passage.
It checks earlier version locks and all eight prior v5 input/SCAD records
against `validation_key_extension/previous_v5_baseline.json`.
Never overwrite that baseline to hide a regression.
The report is `validation_key_extension/report.json`.

These are mesh and geometric flex checks, not FEA, measured insertion forces
or physical strength qualification.

Verification passes all **17 CAD views**, the three connection checks,
**48 geometry tests** and **seven comparison tests**, plus the earlier
release/CAD baselines. The nine pieces lie on Z=0 in a **134 × 48 mm** layout.
The enlarged tip reliefs continue past the body envelope to avoid tiny
coincident-edge STL slivers; the intended tip profile is retained.
