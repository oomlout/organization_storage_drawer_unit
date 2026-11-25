# Drawer unit project guidance

## User intent and required pipeline

This project makes drawer units whose removable drawers/inserts are takeaway
containers. The container type for each unit/shelf definition belongs in
`working_oomp_populate.py`.

Always preserve the generation sequence requested by the user:

`working_oomp_populate` -> `working_oomp` -> `working_scad`

Make changes in the responsible source stage and carry them through the pipeline.
Do not substitute hand-edited generated YAML, SCAD, or STL files for source changes.
Keep these notes current as the design evolves. The baseline below was inspected
on 2026-10-18; it records existing behavior, not a requirement to retain every
dimension or experimental feature.

## Structure and data flow

- `working_oomp_populate_purchased.py`: editable UK purchased-drawer research
  records, called by normal population after the generated-frame options are
  prepared. The user has approved inclusion of the 15 current small-component
  records; their approval flags are true and normal population emits them.
  Keep future research proposals unapproved until authorized. The latest additions are Barton 20/40 drawer
  multipacks and Treston 291-4ESD. The reusable one-off research brief is in
  `drawer_research_agent_instructions.txt`; it requests GPT-6 Luna at low
  reasoning and in-app-browser evidence, with parent-assisted browser reading
  if the subagent browser is unavailable. Only
  `approved_for_oomp=True` entries are emitted; wait for the user's shortlist
  and taxonomy approval before enabling them. These are catalogue records with
  no `oobb_details`, so the existing SCAD loader skips them. Taxonomy 4 is
  `small_drawers`, 5 per-drawer ml capacity (explicitly marked when estimated),
  6 drawer count, 7-9 complete-unit W/H/D, 14 manufacturer, 15 sanitized part
  number; 10-13 are blank. Raaco uses its numeric manufacturer part number,
  with cabinet model stored separately. All shortlisted units have uniform
  drawers around 200-300 ml. Drawer dimensions retain their published basis;
  nominal capacity and calculated rectangular volume are separate fields.
  Capacity taxonomy and capacity_ml fields round to the nearest 25 ml using
  half-up rounding; preserve original values in *_unrounded_ml fields and
  keep rectangular_volume_ml unchanged. Rounded capacity is a comparison label.
  Raaco nominal capacity is inferred from cabinet litres and drawer family.
  Sealey capacity is an estimate from dimensions whose internal status is
  unconfirmed. Treston nominal capacities follow its drawer catalogue. Costs use GBP
  including VAT excluding delivery; per-kg is for the complete empty unit.
  Preserve weight/source qualifications and unknown values; never substitute
  shipping weight or load capacity for product weight. Large, paper-sized and
  mixed-drawer units have been removed from the active shortlist. Preserve the
  approval gate; do not generate purchased OOMP records before user approval.
  Preserve multipack price/count and minimum required spend alongside derived
  per-cabinet price. The ESD drawer L-61-4ESD is rated 200 ml by Treston despite
  its 469.2 ml external rectangular envelope; do not substitute envelope volume.
- `working.py`: orchestrates population, OOMP enrichment, SCAD generation, then
  optional SVG/action stages, controlled by keyword flags.
- `working_oomp_populate.py`: builds option dictionaries (`container`,
  `container_short`, `column`, `row`, `style`), adds taxonomy fields, copies
  drawing inputs into `oobb_details`, and sets `oobb_name` from `style`.
  Generated designs start with taxonomy 1 `oobb`, followed by 2 `organization`,
  3 `storage`, 4 `drawer_unit`, 5 column, 6 row, 7 container, 8 style, 9 variant.
  Purchased units keep taxonomy 1 `organization`. This separation is defined
  in population and copied into drawing inputs, so it persists on every run.
  Calls the extra-detail hook and the shared `write_extras()` helper, which writes
  `parts_source/<taxonomy-derived-id>/working.yaml`.
- `working_oomp_populate_extra_detail.py`: hook for annotations keyed by generated
  ID. Its example annotation is currently disabled.
- `working_oomp.py`: reads source YAML, adds names, directories, optional per-part
  manual overrides and action metadata, then calls `oomp.add_parts()` to produce
  enriched records under `parts/<id>/`.
- `working_scad.py`: reads `parts/*/working.yaml`; combines build kwargs, stored
  kwargs, and `oobb_details` (in that precedence order). Contains the body/grid
  geometry in `get_basic()` and the dimension mapping in `get_container_details()`.
  Its `get_container_cutout()` wrapper delegates to
  `working_scad_container_cutout.get_base(pos, thing, **kwargs)`.
- `scad_help.py`: dispatches `oobb_name` to `working_scad.get_<oobb_name>()`, with
  `get_base()` as fallback; writes `3dpr.scad`, optional exported artifacts,
  updated `working.yaml`, and `thing.yaml`. Copies generated part folders into
  `navigation_oobb/` using taxonomy order.
  Navigation includes catalogue records without drawing kwargs and uses all
  15 taxonomy levels, preserving purchased manufacturer/part-number identity.
  During the prefix migration existing generated folders were renamed to their
  new IDs; old navigation was preserved in `taxonomy_migration_backup/`.
- `working_scad_container_cutout.py`: owns the active cutout and catch-tab code,
  including all AI material-saving shelf and side-wall windows.
  Its `get_base()` dispatches by style: `ai_version_1` now uses the user's
  stepped-profile `get_container_cutout_ai_version_2()`; other styles use
  `get_container_cutout_version_1()`. Make cutout
  changes here; retain the call from `working_scad` and the full generation pipeline.
- `working_scad.get_base()` and `get_hole_cover()` are other/template geometry;
  the current `basic` definitions select `get_basic()`.
- `webserver/`: ancillary Flask browser for generated parts. Its add form writes
  root `working_manual.yaml`, but population of that file is currently disabled
  by `if False` in `working_oomp_populate.py`. Root manual options and per-part
  manual overrides in `working_oomp.py` are different mechanisms.
- `source_file/`, `template/`, `roboclick/`, and `working_action.py` support
  labels, artwork, and other actions outside the core drawer geometry.

## Build entry points

### Drawer comparison webserver

`webserver/app.py` serves product cards at `/drawers` (the homepage) and a
sortable table at `/compare`. Both use `webserver/services/drawer_comparison.py`.
Purchased photos are cached in `webserver/static/drawer_photos/`; original image
and seller URLs are explicit fields in `working_oomp_populate_purchased.py`.

`working_oomp_populate_comparison.py` is called by ordinary population. It owns
the editable Systempak 209/214 carton prices, VAT, lidless pot masses, and the
filament rate of GBP 0.01/g. It prefers explicit VAT-inclusive local container
price records if available. The current fallback prices were checked on the
live Systempak site on 2026-10-18: GBP 60.95/80.95 ex VAT per 500 pots and lids,
respectively, both on backorder. Pots are used without lids but the purchase
cost includes them. Source URLs and all assumptions persist in generated YAML.

Run `python action_prepare_drawer_comparison.py` after geometry changes to run
populate -> OOMP -> SCAD, export and measure the actual CSG meshes, render
`comparison.png` for all 16 printed designs, and run the same pipeline again
to carry costs into records and navigation. `drawer_comparison/cad_measurements.json`
is derived cache data, keyed by CAD source and drawing-parameter fingerprints.
Ordinary population refuses stale measurements. Edit population inputs, never
the generated YAML or measurement cache. Filament mass assumes solid PLA at
1.24 g/cm3 including ears; it is not slicer-measured mass. Empty assembled weight
adds lidless pots (209: 8 g, 214: 16 g). Printing energy/labour/waste and delivery
are excluded. Fit and shallow layout samples are hidden by default and labelled
when enabled; 11 full frames and 15 purchased units form the default comparison.

Comparison checks: `python -m unittest webserver.tests.test_drawer_comparison -v`.
The broader webserver suite also contains legacy file-action and manual-editor
expectations unrelated to comparison; see `drawer_comparison/validation.md`.

Run from the project root so relative input and output paths resolve correctly.

- `python action_make_scad_no_stl.py`: complete populate -> OOMP -> SCAD sequence;
  fast SCAD generation and navigation copying, with action execution disabled.
- `python action_make_scad.py`: same sequence with full export (`typ="all"`,
  `save_type="all"`), including STL generation.
- `action_make_all.py`, `action_make_all_no_stl.py`, and default `working.py`
  also run the action stage. Prefer the SCAD entry points for geometry work.
  `working_action.py` includes label regeneration, another OOMP pass, and
  Roboclick actions.
- Running `working_scad.py` alone consumes existing part records and skips the
  preceding source stages; it is not the complete required regeneration path.

Shared Python dependencies are outside this folder. At inspection, `oomp` and
`oomp_populate_helper` resolve under `C:/gh/oomlout_oomp_version_5/`, and `oobb`
and `opsc` under `C:/gh/oomlout_oobb_version_5/`. Python 3.12 and OpenSCAD Nightly
are available. Check the current environment if imports or exports fail.
This directory was not a Git checkout at inspection.

## Basic-style geometry baseline and coordinate conventions

- Basic variants: 1 column x 1 row and 2 columns x 2 rows.
  Each option currently uses one container type across its entire grid.
- Container: Systempak 209, rectangular 100 ml tamper-evident takeaway container.
  The full identifier includes `109_mm_width_86_mm_height_29_mm_depth`.
- Drawing dimensions are mapped explicitly in `get_container_details()`:
  X/across = 86 mm, Y/rows = 26 mm, Z/insertion depth = 109 mm.
  Do not infer the drawing axes directly from the identifier's width/height/depth
  labels. The user confirmed that 26 mm is the container height without its lid;
  the identifier's 29 mm includes the lid, which this project does not use.
- Clearance is 1.5 mm added to each opening's overall X and Y dimension
  (0.75 mm per side for a centered opening), not 1.5 mm per side.
  `get_container_details()` currently overwrites the clearance with 1.5.
- Wall, outside border, and divider thicknesses are all hardcoded to 1 mm in
  `get_basic()`.
- Overall dimensions are:
  `X = (container_width + clearance) * column + divider * (column - 1) + 2 * border`;
  `Y = (container_height + clearance) * row + divider * (row - 1) + 2 * border`;
  `Z = container_depth + clearance + wall`.
  Thus the baseline bodies are 89.5 x 29.5 x 111.5 mm and
  178 x 58 x 111.5 mm respectively.
- Start with one positive rounded-rectangle body. Place a negative
  rounded-rectangle cutout in every grid cell. Grid positions are centered about
  the supplied X/Y position; rows and columns advance in positive Y and X.
- Body and cutouts both start at the supplied Z and extend 111.5 mm in the
  baseline. The cutouts therefore go through the full body; the extra wall term
  in the depth formula does not currently create a back wall.
- The user confirmed that the open back is intentional because the unit is
  printed face down. A partially or fully closed back is a future possibility
  if the drawer stop can be designed to print without supports. Preserve this
  printing constraint when developing stop or back geometry.
- Existing generated SCAD uses a 5 mm outer corner radius and a 4 mm cutout
  radius (`5 - thickness_wall`).
- Each opening has an added catch tab at its lower Y edge and the starting Z
  end: currently 56 mm wide (`catch_tab_minus = 30`), 7 mm high, 1.5 mm deep,
  radius 2.5 mm. It is added using
  `positive_positive`, which unions it after the main subtraction.
- An enabled, highlighted M3 countersunk test feature is also appended in
  `get_basic()`. Its intended role has not been confirmed.

## Local coding style

- Use procedural Python geometry functions with `thing` and `**kwargs`.
- Read parameters with `kwargs.get(...)`; use descriptive snake_case names such
  as `container_width`, `thickness_wall`, and `drawer_divider`.
- For a component, copy kwargs into `p3` with `copy.deepcopy`, set its `type`,
  `shape`, dimensions and position, then call `oobb.append_full(thing, **p3)`.
- Copy positions into `pos1` before offsetting them; preserve the caller's input.
- Geometry uses millimetres, `size = [wid, hei, dep]`, and `pos = [x, y, z]`.
- `positive`/`p` adds geometry; `negative`/`n` subtracts it;
  `positive_positive` adds geometry after subtraction.
- `m = "#"` is a preview highlight, not a disabled component. Highlighted
  cutouts still subtract and highlighted positive features still contribute.
- Existing scripts group work in commented `if True` / `if False` blocks. Keep
  focused edits compatible with this style; avoid unrelated cleanup during
  geometry changes.
- The user explicitly prefers a solid body in `working_scad` and one complete
  per-container cutout routine with explicit multiline dictionary definitions.
  Keep the AI opening, floor/ceiling reliefs, both side-wall reliefs and catch
  together in the active `get_container_cutout_ai_version_2()`; do not split them back out
  into frame-wide relief/window helpers. Some repetition is intentional.
  `working_scad` supplies each cell's `row_index` and `column_index` so the
  cutout knows which walls are outside borders. Shared-wall cuts are repeated
  by neighbouring cells and unioned during subtraction. Module-level adhesion
  ears remain in `working_scad`.
- Preserve taxonomy/ID conventions and style-based dispatch. Carry new per-option
  inputs from population through `oobb_details` to the drawing kwargs.
- Validate future geometry changes through the full pipeline and inspect the
  resulting dimensions/geometry. Use `action_validate_ai_version_1.py` for the
  AI trial set; see its report for the checks actually run. Mesh checks do not
  establish physical fit, shrinkage, strength or successful slicing/printing.

## AI version 1 development

The user requested a material-saving, printable large drawer bank on 2026-10-18.
The bed is 400 x 400 mm; multiple units should sit side by side as a larger bank.
Filament, nozzle and target loading remain unspecified. The original 400 mm
printer's usable Z height is unspecified; additional A1 mini and P1P options use
their published 180 mm and 256 mm Z limits respectively.

Read `AI_VERSION_1.md` for the design, parameters, test-piece IDs, verification
results and physical test sequence. All AI options and defaults are declared in
`working_oomp_populate.py`, carried through `oobb_details`, and rendered via
`working_scad.get_ai_version_1()` plus the dedicated cutout module.

The current implementation is a single-piece face-down frame with stepped
through-openings, front catches, continuous lip shelves and relief windows closing at >=45 degrees
to the bed. It has no clamshell or fastening hardware. Do not claim the adjacent
modules are mechanically joined. The sample bank gap is 0.4 mm, and the seam is
wider than an internal divider. The large option is 4 x 12 drawers, with a
360.2 x 354.6 x 110.5 mm finished frame envelope. With removable adhesion ears,
the current print envelope is 360.2 x 395.6 x 110.5 mm.

After reported bed-adhesion trouble, the user requested a 4.5 mm catch angled
up from the base and sizeable removable corner ears. The subsequent stop revision
increased AI catches to 6 mm into the opening over 6 mm of print height, with a
further 1.5 mm tip thickness. The front band is now 7.5 mm (rear remains 6 mm).
Both shallow layout options now use `test_depth=7.5` to contain the complete
ramp and tip; full-frame envelopes and printer grids are unchanged. These
population defaults apply to both 100 ml and 550 ml AI frames.
Four 20 mm diameter x 0.6 mm thick pads are attached outside each module's
top/bottom corners by 5 mm wide x 0.3 mm high breakaway necks, with a 0.5 mm gap
elsewhere. `adhesion_ears` and `ear_*` controls are in population. Bed checks
include the ears, with a 2 mm margin beyond them. Neck height must suit the
actual first layer; attachment/removal and adhesion remain physical test items.
All AI trials include these features. The basic-style geometry is unchanged.

The user subsequently introduced `get_container_cutout_ai_version_2()` and routed
the existing `ai_version_1` style to it. Preserve the two-piece opening: a full-width
12 mm high channel plus a full-height body channel inset 5.5 mm on each side.
`depth_lip=12`, `inset_lip=5.5`, and `lip_cutout_radius=1` are now population
parameters; nominal container clearance remains 1.5 mm. The active revision keeps
a 3 mm thick continuous shelf above the step (`lip_shelf_thickness`) and 1 mm
below it at the root. Separate side windows remove material above and below this
protected band, including through the thick shoulder above it. Edge rails are
10 mm; `middle_rib_width=0` produces one wide floor/ceiling window, with no centre
support. Positive middle_rib_width remains an optional trial setting. The old
AI version 1 function is an inactive historical reference, not the active design.

Validation includes sampled exported-mesh sections checking shelf/root material,
clearance below the bearing face, open side reliefs, and absence of the centre
rail. Ten unit tests and all eleven mesh checks passed. Compared with the user's
unrefined stepped profile, CAD volume falls 9.83% for 2 x 2, 13.87% for P1P,
and 16.03% for 4 x 12. These are material measurements, not measured strength.
See `validation_ai_version_1/lip_refinement_comparison.json` and the saved
`before_lip_refinement.json`; all eleven variants were regenerated through the
full pipeline. Fit/strength require physical verification.

Eleven AI variants cover 1 x 1 / 2 x 2 / 4 x 12 frames, three clearance samples,
a paired module layout, a large shallow layout, a continuous-wall reference,
and two printer-specific maximum grids. The population `experiments` list defines
`a1_mini_max` (1 x 4 drawers, 180 x 180 x 180 mm build volume) and `p1p_max`
(2 x 7 drawers, 256 x 256 x 256 mm). Including ears, their print envelopes are
92.3 x 161.2 x 110.5 mm and 181.6 x 249.1 x 110.5 mm respectively. These retain
current clearances, walls, ears and 2 mm bed margins; do not call them maximum
independently of those parameters. The A1 mini cannot fit two current columns
(181.6 mm wide). Printer variants carry `printer` and `build_height` through
OOMP, and validation checks XY margins and Z limits. Ten unit tests and eleven
mesh checks passed this revision. Source specification links are in AI_VERSION_1.md.
Keep test variants in the same pipeline, with distinct taxonomy_9 values to avoid
ID collisions. Derived AI parameters and validation live in `working_scad.py`;
AI clearance does not inherit the basic helper's hardcoded override.

`python action_validate_ai_version_1.py` regenerates the full pipeline, exports
the AI STLs and previews, checks meshes, and refreshes navigation. Unit checks:
`python -m unittest discover -s tests -v`. Reports are in
`validation_ai_version_1/report.json` and per-part `validation.json`.
`3dpr` files are print-oriented; generated `preview_scene.scad` is presentation
only. Material-saving percentages compare equal-envelope AI frames, not the
thinner original basic frame. Shrinkage compensation must follow measurements;
none is assumed or baked into CAD.

## Systempak 214 / 550 ml addition

Added 2026-10-18 at the user's request. Three further `ai_version_1` options in
`working_oomp_populate.py` use container
`packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214`:
standard 1 x 1, `a1_mini_max` 1 x 1, and `p1p_max` 2 x 2. The mini stays a
separate printer-tagged record even though its geometry matches the standard.
The 550 ml container maps to X=86, Y=95-3=92 (lid removed), Z=108 mm in
`get_container_details()`. The user confirmed the same top/lip profile as the
100 ml container, so reuse the active complete stepped cutout with unchanged
lip supports, catches, relief rules and ears. Do not scale the lip profile with
the taller container height. Including ears the 1 x 1 envelope is
92.3 x 139.3 x 109.5 mm and the 2 x 2 envelope is 181.6 x 234.6 x 109.5 mm.
Printer maxima include the existing 2 mm bed margins and Z limits. There are
now fourteen AI variants and twelve unit tests; all twelve unit tests and all
fourteen exported-mesh validations passed. Historical eleven/ten counts above
describe earlier revisions. See `AI_VERSION_1.md` for the new models.

The user then requested that thick lip shoulders stop at the same height as on
the 100 ml design, instead of continuing down the entire taller body. Population
now carries `lip_support_reference_height=26` (lidless reference body height).
The support region includes clearance: 27.5 mm total, or 15.5 mm beyond the
12 mm lip step. The active per-container cutout opens the remaining 66 mm of
the 550 ml cavity to full width for the complete insertion depth, including
front/rear bands, retaining thin side walls and rounded far corners. Keep the
3 mm bearing shelf/root protected and all 100 ml geometry unchanged. The new
unit test checks reference height across clearances; mesh section checks also
sample front/rear bands for removed shoulders and retained thin walls.
All thirteen unit tests and fourteen mesh validations passed after the full
pipeline. CAD volume including ears fell 32.10% for each 550 ml 1 x 1 and
38.88% for its P1P 2 x 2; all eleven 100 ml volumes stayed unchanged. The
comparison is saved in `validation_ai_version_1/shoulder_height_limit_comparison.json`.

## User confirmations from the initial review

Confirmed on 2026-10-18: use containers without lids (26 mm body height), retain
the intentional open back in the current face-down print design, and consider
future partial/full back closure only with a drawer stop that needs no supports.
No geometry changes were requested or made during this initial review.
