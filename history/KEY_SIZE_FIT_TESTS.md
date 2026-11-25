# Numbered locking-key and through-piece fit tests

**Next size round:** the user found 9 closest but still loose and 1 much too
loose. [Samples 20–22](KEY_SIZE_EXTENSION_TESTS.md) continue the 3/6/9 size
progression at 145%, 160% and 175%, keeping sample 9's clearance settings.
The original two beds below are unchanged.

2026-10-20. PETG; mainly permanent locking. These are connector coupons only.
The separate locking key is the chosen direction; the complete v5 cabinet is
still deferred. The original five connector records and all v1–v4 units remain
unchanged.

Print the two `3dpr.stl` files in the `parts/` folders ending in
`ai_version_5_style_key_size_fit_suite` and
`ai_version_5_style_through_fit_suite`. Each holds nine matching
plate/rail/key sets (27 separate pieces), arranged for an A1 mini bed.
The same files fit the P1P and larger printers. The checked footprints are
approximately **133 × 154 mm**, with all pieces starting at Z=0.

Each long rail has its number **recessed 0.6 mm** into the face visible from
above on the print bed. Each plate has the matching recessed number.
The loose keys are deliberately unmarked to preserve their small sections:
keep them alongside their numbered pair when removing the print.
Each folder includes a generated `trial_index.csv` with exact settings.

## Bed 1: key size and slot clearance, numbers 1–9

Numbers read left to right, top to bottom:

| Key size | 0.20 mm key clearance | 0.30 mm key clearance | 0.40 mm key clearance |
| --- | --- | --- | --- |
| 100% | 1 | 2 | 3 |
| 115% | 4 | 5 | 6 |
| 130% | 7 | 8 | 9 |

Clearances are **per side**. Size scales the fork, its hooks/root radii and
matching tongue/slot. The rail remains 11 × 10 mm, its grip 32 mm long, and
the plate remains 7.5 mm thick. Through-piece clearance stays at 0.25 mm per
side, with straight sides, so this bed compares the locking key itself.
The original fork is 100% size with 0.25 mm slot clearance, between 1 and 2.

## Bed 2: gently tapered through piece, numbers 10–18

All nine use the same 115% key and 0.30 mm key slot clearance as sample 5.
This isolates the rail tongue's fit through the receiver plate.

| Entry clearance per side, X | 0.025 mm final clearance per side | 0.025 mm interference per side | 0.050 mm interference per side |
| --- | --- | --- | --- |
| 0.10 mm | 10 | 11 | 12 |
| 0.20 mm | 13 | 14 | 15 |
| 0.30 mm | 16 | 17 | 18 |

The final **6 mm** of the tongue widens gently towards the rail shoulder.
The entry and exposed key region stay parallel. The taper acts across X only;
height clearance stays at 0.25 mm per side. Taper angles are approximately
0.72–3.34 degrees per side. Maximum interference is 0.10 mm across the
complete width, confined to the last part of seating. Samples 10, 13 and 16
retain a 0.025 mm per-side gap as snug sliding-fit controls, avoiding exact
line contact in the assembled reference. Negative interference in the
generated CSV means clearance.

Interference is intentionally modeled as a small overlap between rigid CAD
parts. Printed PETG may take this up by local deformation, or printer
dimensional error may make a sample tighter or looser. These are trial values,
not established fit tolerances. Do not force a sample that visibly damages
the plate; record it as too tight.

## Printing and comparing

Use the same PETG profile, supplied orientations and first-layer compensation
for both beds. A starting comparison profile is a 0.4 mm nozzle, 0.2 mm
layers, four walls and solid infill for these small coupons. Inspect the
short bridge over each key slot in the slicer. Keep supports and brims out
of the slots and fork gaps.

1. Keep each numbered plate and rail together, with its key.
2. Try the tongue through the plate **before adding the key**. Compare entry,
   final seating effort and sideways play. The rail shoulder should seat
   against the plate; a tight but unseated tongue is not a successful fit.
3. Insert the key sideways until both retaining shoulders recover. Compare
   key insertion effort and whether the assembled joint stays secure.
4. Record the preferred key number from bed 1 and through-fit number from
   bed 2. Inspect whitening, split layers and damaged hooks. Compare retained
   fit after sustained loading before choosing a cabinet joint.

Axial catch clearance is 0.2 mm throughout. These coupons do not compare or
eliminate that axial play. Keep insertion effort separate from retention:
a tight fit alone does not establish a reliable lock or load capacity.

`trial_XX.stl` prints one three-piece set. `rail_XX.stl`, `plate_XX.stl` and
`key_XX.stl` allow individual reprints. `assembled*.stl` files are visual
references, **not print layouts**.

## Source and verification

`get_ai_version_5_key_trials()` and `get_ai_version_5_through_trials()` in
`working_oomp_populate.py` own the matrices. These are two test-suite records;
clearance values do not enter taxonomy IDs and no retired drawer clearance
variants are restored.

Solid bodies and bed layouts are in `working_scad.py`. Complete receiver,
tongue, key, notch and numeral geometry remains in the single
`get_container_cutout_ai_version_5()` routine with multiline dictionaries.
`scad_help.py` generates the views, CSV and printing instructions.

Run `python action_validate_key_size_fit.py` to run
populate → OOMP → SCAD and export/check 94 views across both suites.
Checks cover closed meshes, bed placement, quantities, recessed rail numbers,
key retention and prescribed flex passage. Through-taper checks independently
measure sections and verify the analytically expected seated interference
volume, with clear entry before the final interference zone. Intentional
interference is accounted for when checking assembled volumes.

The validator also checks v1/v2/v3 locks, the v4 baseline and all five original
v5 records against their saved inputs/SCAD. It writes
`validation_key_size_fit/report.json`. These checks are geometry checks,
not force simulation, physical printing or a PETG strength rating.

Current verification passes all **94 exported views, 18 connector checks,
46 geometry unit tests and seven comparison tests**, plus the earlier version
locks and original v5 input/CAD regression checks. Preview inspection confirms
upright, recessed rail numbers and matching plate numbers.
