# Version 3 development

Created 2026-10-19 as an independent copy of the completed version 2 with
interlocks at every front/back mating junction. Version 2 is now locked in
`releases/ai_version_2/`; version 1 remains locked in `releases/ai_version_1/`.
Future refinements belong in version 3. Do not update either release manifest.

## Intermediate lower supports removed — 2026-10-19

Only the outer top and bottom unscrewed rails now connect front to back.
Intermediate lower rails and their round pegs/sockets are removed. Every
tray retains its lip shelf with M3 screw/nut and rectangular mating tongue.
The user confirmed four connections per vertical grid boundary for two rows,
and nine for seven rows (`row + 2`); multiply by `column + 1` for the unit total.
Thus the 2 x 2 has twelve connections and the P1P 2 x 7 has twenty-seven.

The cuts start after each half's outer face band and run to the seam. Front
catches and the face grids remain, as do the top/bottom rails and their pegs.
This revision applies to all multirow v3 frames, including the solid reference.
Single-row and shallow samples remain unchanged. Population's
`remove_internal_lower_supports=True` controls it without changing taxonomy.
The complete cut stays inside `get_container_cutout_ai_version_3()`.

Validation now checks absence of intermediate supports and pegs, retained
outer face grids and the exact mating-island count on lightened frames.
The frozen-v2 interface comparison permits only these removed rail bands;
remaining hardware/outer interlocks and an outer face section must match.
Historical material figures below describe the preceding taper revision.

This revision passes 42 mesh views, ten mating pairs, 33 unit tests, six
comparison tests and both release locks. All twenty half-interface comparisons
pass with only the authorized rail bands removed from the expected sections.

| Changed full frame | CAD reduction versus locked v2 | Estimated solid PLA saved |
| --- | ---: | ---: |
| 100 ml 2 x 2 | 23.70% | 64.1 g |
| 100 ml A1 mini 1 x 4 | 36.98% | 103.3 g |
| 100 ml P1P 2 x 7 | 42.80% | 308.8 g |
| 100 ml large 4 x 12 | 46.50% | 951.5 g |
| 550 ml P1P 2 x 2 | 20.16% | 56.4 g |
| 100 ml solid reference 2 x 2 | 12.98% | 66.0 g |

Savings include the earlier tapered-shelf refinement and adhesion ears.
Single-row variants retain their previous figures. Actual filament usage and
load capacity still require slicing and a physical print test.

## Conservative material refinement — 2026-10-19

Version 3 now opens the upper side relief farther alongside the running shelf.
Its nominal thickness above the lip step is 4 mm away from the joint; the
existing 10 mm thickness remains for the last 12 mm before the mating plane.
A 7.2 mm-long, approximately 50-degree transition grows into this reinforced region. The rear
half uses its 6 mm outer face band; the front retains 7.5 mm for the complete
catch. Wall thicknesses, corner rails, mating features, outside dimensions,
drawer clearances and screw/nut positions are retained.

Population controls `running_shelf_thickness=4`, `hardware_boss_band=12` and
`hardware_boss_slope=1.2` (print-height rise per millimetre of sideways growth).
Guardrails retain at least 3 mm nominal running shelf, slopes of 45 degrees or
steeper, and a full boss around the hardware seats. The existing axial access
bores interrupt the nominal shelf cross-section; their original material below
the bore and the lip bearing face remain. Mesh checks explicitly sample that
material and the side webs, rather than treating the nominal 4 mm as a solid
uncut rectangle.

The flat socket-cap and nut bearing faces remain because they provide the
clamping surfaces. OOBB's existing localized seat-bridge geometry remains;
this revision does not claim to eliminate all bridging. The enlarged relief
grows the surrounding reinforcement gradually instead of adding a broad roof.
Solid-reference, joint-fit and shallow layout samples retain their geometry.
Use a standard 1 x 1 frame to trial the thinner rails and taper; the short
joint-fit sample still checks hardware and mating fit.

The validator checks the rail thickness at three depths, the transition, all
original hardware/interlock checks, print-face angles and mating intersections.
`validation_ai_version_3/material_comparison.json` compares exported CAD volumes
with the locked version 2 release, including ears. These are solid-volume PLA
estimates, not slicer consumption or measured strength.

The approximately 50-degree revision passed all 42 mesh views, ten mating
pairs, 32 unit tests, six comparison tests and both release locks. Sampled
sections through all twenty front/back interfaces match frozen version 2,
including the hardware seats and interlocks; see `interface_comparison.json`.
The steeper slope gives margin over the 45-degree print-face threshold.

| Full frame | CAD material reduction versus v2 | Estimated solid PLA saved |
| --- | ---: | ---: |
| 100 ml 1 x 1 | 8.40% | 9.1 g |
| 100 ml 2 x 2 | 10.36% | 28.0 g |
| 100 ml A1 mini 1 x 4 | 11.78% | 32.9 g |
| 100 ml P1P 2 x 7 | 12.79% | 92.3 g |
| 100 ml large 4 x 12 | 13.53% | 276.8 g |
| 550 ml 1 x 1 (including A1 mini) | 9.00% | 10.4 g |
| 550 ml P1P 2 x 2 | 11.14% | 31.2 g |

The solid reference, short joint-fit and two layouts have zero geometry change.
Printability, fit and stiffness still need a physical trial with the actual
filament and slicing settings. Localized flat hardware-seat bridges remain.

## Starting design (before refinement)

The twelve active version 2 options are copied: nine full-frame variants, two
shallow layout samples and the short joint-fit pair. The A1 mini, P1P,
large bank, both container sizes and solid reference remain.
IDs retain the existing taxonomy with `ai_version_3_style` instead of
`ai_version_2_style`.

The starting dimensions, openings, shelves, catches, ears, screw/nut features,
rectangular interlocks and corner pegs are identical to the version 2 release.
The 550 ml opening retains its extra 1.5 mm per row. Half bodies have equal
depth; front interlocks extend 3 mm. Corner pegs are 2.8 mm diameter with
3.3 mm sockets and 0.2 mm end clearance. Hardware remains M3 x 16 socket-cap
screws with M3 nuts. See the frozen `releases/ai_version_2/AI_VERSION_2.md`
for the inherited design and physical trial instructions.

## Clearance setting

The user subsequently retired the three clearance-fit records from every
version, including the separate default-clearance fit sample. They are archived
in `retired_clearance_part_records/`; frozen release snapshots remain intact.
`container_clearance` stays adjustable in each version's defaults and is
currently 1.5 mm overall. Only the default is populated, and clearance does not
appear in taxonomy or IDs. Joint-fit and layout samples remain available.

## Edit and generate

Keep the sequence `working_oomp_populate` -> `working_oomp` -> `working_scad`.

- Options and adjustable defaults: `get_ai_version_3_options()` and
  `get_ai_version_3_defaults()` in `working_oomp_populate.py`.
- Positive body, parameter checks, grid layout, ears and container mapping:
  the independent `get_ai_version_3*()` functions in `working_scad.py`.
- All per-cell openings, reliefs, catches, hardware and interlocks:
  `get_container_cutout_ai_version_3()` in `working_scad_container_cutout.py`.
  Keep the explicit multiline dictionaries together in this routine.
- Full regeneration/export/mesh validation:
  `python action_validate_ai_version_3.py`.
- Update comparison images and measured costs after geometry changes:
  `python action_prepare_drawer_comparison.py`.

Each full frame retains one `parts/<id>/` folder with `3dpr.scad`/STL for the
flat pair, `front.scad`/STL, `back.scad`/STL and `assembled.scad`/STL. Maximum
pairs need separate plates. Comparisons use the assembled reference dimensions.
The joint-fit sample ends in `ai_version_3_style_joint_fit`.

## Release and validation checks

The version 3 validator checks 42 active meshes and ten mating pairs, and runs both
release lock checks after the pipeline. Independent test helpers are in
`validation_ai_version_3_checks.py`; reports/previews go to
`validation_ai_version_3/`. Unit checks are
`python -m unittest discover -s tests -v`.

`python action_check_version_2_lock.py --compare-version-3` verifies the initial
copy: all 42 active SCAD views must be identical and all drawing inputs must match
after normalizing the version name. Its evidence is saved in
`releases/version_2_to_3_copy_check.json`. This equality is a starting-copy
check, not a restriction on future version 3 refinement. Continue running
`python action_check_version_1_lock.py` and
`python action_check_version_2_lock.py` after changes.

CAD checks do not establish physical fit, strength, shrinkage or print success.

Initial verification before clearance retirement completed on 2026-10-19: all fifteen pairs of drawing
inputs match after version-name normalization, and all 45 version 3 SCAD views
are identical to their version 2 counterparts. All 45 exported version 3 mesh
checks and ten mating pairs passed, as did 30 unit tests, six comparison tests
and both release locks.

After the clearance retirement, 31 unit tests pass. Both lock checkers retain
strict checks for surviving models and explicitly report the three retired
clearance variants. Their frozen manifests are not rewritten.
