# Version 2 locked release

Locked 2026-10-19 after the all-junction-interlock revision. The immutable
snapshot is `releases/ai_version_2/`; check it with
`python action_check_version_2_lock.py`. Future development starts from the
independent copy documented in `AI_VERSION_3.md`. Do not rewrite the manifest.

Created 2026-10-19 as an independent copy of the locked version 1 release,
including the last requested 1.5 mm extra opening height per 550 ml drawer row.
Version 1 retains its existing IDs; version 2 uses `ai_version_2_style`.
Version 1 has fourteen models in its frozen snapshot (eleven active).
Version 2 has twelve active catalogue folders: nine full-frame variants, two
shallow layout samples and one joint-fit pair. The three clearance-fit variants
were retired from every version at the user's request; frozen snapshots remain.
Clearance remains a settable 1.5 mm default and does not appear in taxonomy.
Basic models and purchased catalogue records are unchanged.

## Files in each main folder - 2026-10-19

All split-frame files now live together in `parts/<main-id>/`:

| File | Contents |
| --- | --- |
| `3dpr.scad` / `3dpr.stl` | Both halves flat at Z=0, separated by an 8 mm footprint gap |
| `front.scad` / `front.stl` | Front half alone, ready to print |
| `back.scad` / `back.stl` | Back half alone, ready to print |
| `assembled.scad` / `assembled.stl` | Assembled reference only |
| `printing.txt` | File guide and whether the pair fits the declared bed |

The main layout chooses X or Y separation to fit the bed where possible.
Maximum-size pairs require separate plates; their individual halves still fit.
`print_layout_fits_single_bed` in the generated design summary records this.
The default population `assembly_half` is `print_layout`; `print_layout_gap`
controls the spacing, including removable ears. This is a packaging/layout
change: the individual half geometries are retained.

`scad_help` writes all four views from `working_scad` in the ordinary pipeline.
Separate-half catalogue records have been retired; recoverable originals are
in `retired_split_part_records/`. `action_consolidate_split_parts.py` is the
one-time, repeat-safe migration for an older checkout. Do not recreate those
half records. The joint trial is now one folder ending `_joint_fit`.
Comparisons render and measure `assembled.scad` so dimensions, mass and cost
remain for one completed unit; the main print layout is not a cabinet envelope.

## Split front/back revision — 2026-10-19

### Interlocks at every mating junction — 2026-10-19

The front now also has a round 2.8 mm locating peg at each corner-rail grid
junction, including shared row/column intersections and all outside corners.
Each enters the rear half by the existing 3 mm interlock depth. Rear sockets
are 3.3 mm diameter and 3.2 mm deep, retaining the existing 0.25 mm radial and
0.2 mm end allowances. The larger rectangular screw-bearing tongues remain.
There are `(columns + 1) * (rows + 1)` additional pegs; screw counts do not change.

The smaller diameter fits inside existing contact material, including the
550 ml internal junctions. It does not widen borders or reduce the container
opening. Internal row pegs sit half a divider thickness below the grid line;
outside pegs are centred in the border. Population owns
`corner_interlock_diameter` and `corner_interlock_min_wall` (0.6 mm), with
dimension guards and exported-mesh checks for socket walls. All geometry stays
in the complete per-container cutout routine. The shallow unsplit fit/layout
samples and version 1 are unchanged.

Validation now checks that every distinct mating island in a lightened front
has an interlock, that tongues stay within the existing contact footprint, and
that all corner sockets retain material around them. Actual fit and the small
pegs' printed strength still need the physical trials.

Completed checks for this revision: all 45 exported meshes, ten mating pairs,
22 geometry unit tests and six comparison tests passed. The version 1 lock
passed. Assembled blind socket air gaps are inward-wound cavity shells and are
excluded from the count of solid bodies; they remain included in volume checks.

Print the front/back files or combined `3dpr` layout from each main folder.
All are generated through population -> OOMP -> SCAD. Each full-frame option,
including A1 mini/P1P and the continuous-wall reference, has all four views. The 100 ml/550 ml openings and the extra
1.5 mm height per 550 ml row are retained. Version 1 is unchanged.

| Feature | Current version 2 |
| --- | --- |
| 100 ml half bodies | 55.25 mm each; front including tongue 58.25 mm |
| 550 ml half bodies | 54.75 mm each; front including tongue 57.75 mm |
| Interlock | 8 x 7 mm screw-bearing tongues plus 2.8 mm round corner pegs, all with 3 mm engagement |
| Socket allowance | 0.25 mm per side, 0.2 mm extra depth |
| Shelf support thickness | 10 mm above the existing lip step |
| Outside border | 5.5 mm, to surround hardware and sockets |
| Fixings | M3 socket-cap x 16 mm, one M3 nut each |
| Fixing count | (columns + 1) x rows; shared dividers get one fixing |
| Screw head seat | 6 mm in front of the centre joint |
| Near nut face | 7 mm behind the joint (3 mm OOBB nut-pocket depth) |
| Adhesion ears | 16 mm diameter, existing thin breakaway links |

The screw length is measured below its head: 6 + 7 + 3 = 16 mm through the
clamp and nominal OOBB nut pocket. Real M3 nut thickness and thread engagement
must be checked on the test pair. Access channels reach from the front and
back surfaces to these recessed seats; a long hex key and a way to seat the
rear nuts are needed. The nut channels are hexagonal to resist rotation.

Hardware uses the OOBB `oobb_screw_socket_cap` primitive with `include_nut`,
`top_clearance=True` and `bottom_clearance=True`. The installed OOBB API reads
`clearance=["top", "bottom"]`, so that is passed as well; the nut is generated
by OOBB's nested `oobb_nut` primitive. `overhang=True` uses its bridge feature.
The socket-cap and nut seats still have small bridging regions; this is not
claimed to be entirely free of bridging or physically print-validated.

The tongue is on the front half. The back half contains the socket. Both print
with their outside face on the bed and the joint pointing up. Turn the back
half 180 degrees about Y to assemble. Material-saving windows open at the
mating plane instead of closing with broad roofs. Continuous lip shelves and
corner rails carry across the joint; the original front catch appears only on
the front half. The taller 550 ml shoulders still stop at the 100 ml reference
height. The hardware uses that thick region rather than entering the pot cavity.

With ears, XY print envelopes are 98.5 x 159.4 mm for the 100 ml A1 mini,
187.8 x 247.3 mm for the 100 ml P1P, 366.4 x 393.8 mm for the large bank,
98.5 x 139 mm for the 550 ml A1 mini, and 187.8 x 235.8 mm for the 550 ml P1P.
All retain the 2 mm bed margin. Smaller ears accommodate the wider borders.

### Print the joint trial first

Use `front.stl` and `back.stl` in the 100 ml 1 x 1 folder ending
`ai_version_2_style_joint_fit`, or its combined `3dpr.stl`. They keep the full opening and real hardware
seats with a 24 mm assembled depth, no lightening and no ears; front print height
is 15 mm, back is 12 mm. Use two M3 x 16 socket-cap screws and two M3 nuts.

1. Print both with their supplied flat outside faces at Z=0.
2. Clear any bridge strands in the hardware passages; verify the head/nut seats.
3. Slide the tongues into their sockets before tightening. Check for full seam
   closure without forcing; tune `interlock_clearance` from the measured result.
4. Seat the nuts from the back, insert screws from the front, then tighten gently.
5. Check container fit, lip support, catch action and movement across the seam.

The assembled files are retained for comparison and inspection. Individual
halves no longer have separate catalogue/price entries. The joint-fit sample
is hidden from the default comparison and omits pot costs. Version 2
assembled material costs include both halves/ear sets; screw/nut costs and mass
are excluded because no hardware price or weight has been specified.

## Where to edit

- `working_oomp_populate.get_ai_version_2_options()`: model/container definitions.
- `working_oomp_populate.get_ai_version_2_defaults()`: version 2 defaults.
- `working_scad.get_ai_version_2()` and its `_parameters`, `_summary`, `_ears`
  and `_container_details` functions: version 2 drawing and derived values.
- `working_scad_container_cutout.get_container_cutout_ai_version_2()`: the
  complete per-container opening, all reliefs and catch, with multiline dicts.

These are separate implementations, not wrappers around version 1. Preserve
the solid body and complete per-cell cutout convention. Version 1 now dispatches
to `get_container_cutout_ai_version_1()`, which contains the released stepped
profile; the obsolete straight-opening routine is named
`get_container_cutout_ai_legacy_straight()`.

## Build and verify

Run `python action_validate_ai_version_2.py` for populate -> OOMP -> SCAD,
STLs and mesh validation. Run `python action_prepare_drawer_comparison.py`
after geometry changes to refresh comparison images and measured costs for
both versions. Run `python -m unittest discover -s tests -v` for guardrails.

Version 1 is archived in `releases/ai_version_1/`, including source snapshots,
fourteen generated model records/SCAD/STLs and a checksum manifest. Do not
update this baseline while developing version 2. After regeneration, run
`python action_check_version_1_lock.py` to catch changes to its drawing inputs
or generated geometry. Both mesh validators also run this release check
automatically once the manifest exists. The initial clone can additionally be checked with
`--compare-version-2`; stop using that flag once deliberate v2 changes begin.
The earlier `releases/ai_version_1_2026_10_19/` folder is a pre-release recovery
snapshot taken before the final 550 ml height request, not the locked release.

The released starting point used 95 mm opening height for the 550 ml container:
92 mm lidless body + 1.5 mm normal clearance + 1.5 mm extra vertical space.
The extra is an option input `opening_height_extra`, not a change to the pot's
physical dimensions. One-row frame height increases 1.5 mm; two-row height
increases 3 mm. Ear-inclusive envelopes become 92.3 x 140.8 x 109.5 mm
and 181.6 x 237.6 x 109.5 mm. The 100 ml models remain unchanged.

Locking a CAD release does not establish physical fit, printability or strength;
the existing physical test sequence in AI_VERSION_1.md still applies.

## Initial copy verification (before the split revision)

All sixteen geometry/unit checks and five drawer-comparison tests passed.
Both sets of fourteen exported meshes passed validation. All fourteen paired
SCAD files are identical, and paired mesh volumes agree within 0.01 mm3.
All eleven 100 ml SCAD files are unchanged from the pre-release snapshot.
The final comparison pipeline refreshed all thirty printed designs.

## Split validation before folder consolidation

`action_validate_ai_version_2.py` regenerates the complete pipeline and exports
all 34 version 2 STLs. It checks connected/watertight meshes, printer envelopes,
shelf sections, head/nut access and bearing seats, shaft passages, tongue/socket
profiles and print face angles. Only local hardware-seat bridges are allowed;
assembled references do not receive a print-overhang claim. Ten front/back pairs
are checked for zero interference using Manifold mesh intersection, and for
interlock engagement by a 0.5 mm lateral displacement. The 20 unit tests include
hardware clearances, paired definitions, retained walls and version isolation.
Reports and the side-by-side joint preview are in `validation_ai_version_2/`.
Use the current report for pass/fail status. No physical test has been performed.

Completed split revision checks: 20 geometry/unit tests, six comparison tests,
34 exported meshes and ten mating pairs passed. The version 1 lock also passed.

## Consolidated-folder validation

The validator now exports 45 meshes across 15 version 2 folders: four views for
each of ten split-frame models and one view for each of five shallow samples.
It checks ten mating pairs, verifies that every combined layout has two bodies
on the bed and the same volume as its individual halves, and retains hardware,
shelf and printer checks on the separate files. For maximum pairs the report
explicitly distinguishes individual-half bed fit from combined-layout bed fit.
The 22 unit tests cover layout mode, single-record routing, unique grid-junction
pegs and their dimension guardrails.
The version 1 release check remains active.
