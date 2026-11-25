# V6 latch clearance test: samples 30-38

These address reported looseness after the latch clicks in. The receiving
hole is unchanged. Sample **37 has now been selected for full-length rails**
in both cabinet sizes. This numbered kit retains its original geometry;
sample 30 represents the rail fit before that selection.

Print `3dpr.stl` in the `ai_version_6_style_latch_clearance_suite` part folder.
It contains all nine numbered rail ends in a **43 x 70 x 10 mm** layout.
Each sample is **11 x 20 x 10 mm**, with a 14 mm solid grip and 6 mm snap tip.
Use the supplied orientation, numbers up, and the same PETG and slicing
settings as the current rails. No receiver needs printing. Individual
`sample_*.stl` files are supplied for replacements.

Numbers map to the nominal CAD clearances below. Side clearance is between
the recovered hook and its pocket wall, per side. End play is between the
hook's retaining shoulder and the plate's retaining ledge.

| Hook side clearance | 0.20 mm end play | 0.10 mm end play | 0.05 mm end play |
|---|---:|---:|---:|
| 0.25 mm | **30: original fit** | 31 | 32 |
| 0.15 mm | 33 | 34 | 35 |
| 0.05 mm | 36 | **37: selected** | **38: tightest** |

The hook projection grows from 1.2 to 1.3 to 1.4 mm, while the shoulder depth
changes from 4.5 to 4.4 to 4.35 mm. The arms stay 1.8 mm thick, with the same
root relief, outer arm faces, bearing strips and tip position. Arm-body side
clearance and vertical clearance both remain 0.25 mm. These samples therefore
isolate recovered hook fit; they do not establish stronger arms or eliminate
all possible movement in every direction. Tighter hooks require more insertion
flex, so compare insertion effort as well as seated play.

Insert each sample from inside your existing V6 face plate, as with a normal
rail. Seat the broad shoulder fully, confirm both hooks click, and compare
sideways wiggle and pull/push movement. Report the preferred number, whether
it clicks reliably, and whether insertion requires excessive effort. Release
both hooks from the outside to withdraw it. `results.csv` has blank fields for
your observations and is never overwritten by regeneration.

Sample 30 matches the original production end apart from its grip number.
Current production rails match sample 37 at both ends.
`control_rail.stl` is the unnumbered baseline used for CAD verification; it is
not an extra piece to print.

The source pipeline remains `working_oomp_populate -> working_oomp ->
working_scad`. All trial inputs belong to
`get_ai_version_6_clearance_trials()` and
`get_ai_version_6_clearance_options()` in population. Bodies are in
`working_scad`; complete removals are in the v6 cutout. The normal SCAD stage
writes the trial index and printing instructions through
`working_scad_v6_clearance.py`.

Run `python action_validate_v6_clearance.py`. The validator protects the
seventeen prior v5/v6 records and their SCAD, checks older releases, exports
eleven meshes, and compares all nine samples with the actual unchanged plate.
Checks include seating, retaining contact, the specified free travel, unchanged
arm/root sections, prescribed-flex insertion, engraving, quantities and bed
contact. The control is compared with a cropped production rail. Results are
in `validation_v6_clearance/report.json`; the immutable pre-change snapshot is
`previous_models_baseline.json` in that folder.

Original kit validation: **83 source tests, nine comparison tests and all eleven mesh
views pass**. Both previews were inspected. Solid CAD kit volume is about
13.96 cm³, or 17.7 g at PETG density 1.27 g/cm³; actual slicing and print time
depend on your settings. The user subsequently reported 37 as the best fit;
the current assembly validator preserves this kit and checks both long-rail
ends against it. The original kit validator and its snapshot describe the
pre-selection frames; use `action_validate_double_sided_v6.py` for current
production geometry. Full-unit loading and retention durability remain untested.
