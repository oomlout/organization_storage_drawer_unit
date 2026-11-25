# Larger keys 20–22 - 2026-10-20

User feedback: 9 closest but still loose; 1 much too loose.
One new hidden sample kit contains three matched sets at 145%, 160% and
175% key scale, continuing 3/6/9's size progression with sample 9's
0.40 mm key clearance. Its nine print pieces occupy about 134 x 48 mm.
Catalogue: 57 printed + 15 purchased, 52 complete units shown by default
and 20 samples hidden. The new record counts no pots/drawers or hardware,
and uses PETG density 1.27 g/cm³ for CAD mass.
The new samples are untested physically. Seventeen CAD views, three
connection checks, 48 geometry tests, seven comparison tests and the
earlier release/CAD checks pass. See KEY_SIZE_EXTENSION_TESTS.md.

# Internal twin-tab coupon 19 - 2026-10-20

One additional hidden PETG coupon adds two aggressive tabs, an open centre
and internal receiver catches. It contributes no pots/drawers or hardware.
Current catalogue: 56 printed + 15 purchased records; 52 complete units
remain visible by default and 19 samples are hidden.
Its revised CAD print layout has two pieces and occupies 37 x 39.5 mm.
The short tabs end flush with the front; full-width beam shoulders now seat
directly against the receiver and prevent over-insertion. The exposed neck
and its separate tab stops have been removed.
All four exported views, mechanical geometry checks, earlier CAD/lock
checks, 47 geometry tests and seven comparison tests pass.
See RECESSED_TWIN_TAB_TEST.md; physical fit and strength remain unverified.

# Numbered key and through-piece trials - 2026-10-20

Two additional hidden sample kits compare key size/slot clearance (1–9) and
gently tapered through-piece fits (10–18). Each kit holds nine matched
three-piece tests with recessed numbers. The catalogue has 55 printed and
15 purchased records: 52 complete units remain visible by default, with
18 samples hidden. No full v5 cabinets are emitted.

Both are PETG connector samples with zero pots/drawers. Their costs use
the print-layout CAD volume, including each separate key. The assembled
reference of an interference sample deliberately overlaps at the taper;
that reduced union volume must not be used as its material estimate.
See KEY_SIZE_FIT_TESTS.md and validation_key_size_fit/report.json.

# Original version 5 connector trials - 2026-10-20

Five new hidden samples provide three PETG snap candidates, the current screw
joint reference and a combined nine-piece kit. No full v5 cabinets exist.
The catalogue now has 53 printed and fifteen purchased records: 52 complete
units remain visible by default, with sixteen samples hidden.

Connector records have no drawers or pots and no per-drawer/litre ratios.
Their CAD mass uses an explicit assumed PETG density of 1.27 g/cm3; the
reference screw/nut price is excluded. Costs describe printed coupons only.
Seven comparison tests pass. Geometry checks pass all nineteen v5 views and
four connections; older release locks and the v4 regression baseline pass.
See `AI_VERSION_5_CONNECTOR_TESTS.md` for physical testing; reliability and
load capacity have not been measured.

# Version 4 modular units - 2026-10-20

Current correction: complete units use one front plate with the catch lip and
one clear rear plate, replacing the initial identical pair. `face_plate` is
the front alias only. Costs and kit quantities must use the distinct front
and back geometries. Face-fit samples additionally export a rear test file;
their priced `3dpr` remains one front plate. Mesh checks verify rear-lip absence,
retained mounts and that adding only the catch geometry to the rear recovers
the front plate.

Version 4 has eight complete modular units, one short hardware joint kit and
two one-plate face-fit samples. Complete-unit costs use assembled geometry;
samples use their actual printed contents and exclude pots. Hardware costs
remain excluded. The full comparison pipeline has refreshed images and
measurements for all 48 printed records; no cache fingerprints are stale.
Together with fifteen purchased records there are 63 catalogue records:
52 complete units shown by default and eleven hidden samples.

All 81 exported v4 views, eleven assembly/sample records, 38 geometry unit
tests, six comparison tests and the v1/v2/v3 release locks pass. Front/back
plates are distinct. Rail batches contain the exact BOM quantities and
fit their declared beds. CAD checks cover nominal nut insertion samples,
keys, countersinks, guides and assembly interference. Physical tray fit,
rail stiffness and successful printing are unverified.
See `AI_VERSION_4.md` for the test sequence and print-file conventions.

# Version 3 internal lower rail removal - 2026-10-19

Multirow v3 frames now retain only the top/bottom unscrewed front-to-back rails.
The user confirmed four connections per vertical grid boundary for two rows
and nine for seven. Screwed shelves, catches and outer face grids remain.
All 42 mesh views, ten mating pairs, 33 unit tests, six comparison tests and
both release locks pass. Twenty half-interface comparisons pass, allowing
only the explicitly removed intermediate rail bands. CAD reductions versus
locked v2 are 23.70% for 100 ml 2 x 2, 36.98% for A1 mini, 42.80% for P1P,
46.50% for 4 x 12 and 20.16% for 550 ml 2 x 2. These include the earlier
taper change, exclude hardware costs and do not measure physical strength.
Catalogue counts and IDs are unchanged; the normal comparison regeneration
refreshes assembled meshes, images and measured costs through the pipeline.

# Earlier version 3 material refinement - 2026-10-19

Version 3 full frames now use thinner running shelves and approximately
50-degree growth into the unchanged screw/nut reinforcement. CAD material
falls 8.40-13.53% versus locked version 2, including adhesion ears. Comparison
measurements/images use the regenerated assembled files. Existing catalogue
counts and filters remain unchanged. Validation passed all 42 mesh views,
ten mating pairs, 32 unit tests, six comparison tests and both release locks;
twenty half interfaces also match the frozen v2 sections. Hardware costs remain
excluded. Physical strength and slicer material use have not been measured.

# Version 2 release and version 3 starting copy - 2026-10-19

The user subsequently retired all nine clearance-fit variants across the three
versions. There are now 37 active printed records and fifteen purchased records
(52 total), with 44 complete units in the default view and eight joint/layout
samples hidden. Clearance remains a settable 1.5 mm default and is absent from
taxonomy. The release archives/manifests retain the original fit records; only
the active catalogue changes. Thirty-one unit tests pass after this revision.
The initial copy counts below precede the clearance retirement.

Version 2 is locked and version 3 starts with the same fifteen models and
45 identical CAD views. Comparison rendering uses the assembled reference for
both split versions. There are 46 printed records and fifteen purchased
records; the default view contains 29 full printed units and fifteen purchased
units, with seventeen samples hidden. The initial version 3 validation passed
45 meshes, ten mating pairs, 30 unit tests, six comparison tests and both
release locks. The measurements are CAD estimates, not slicer or print results.

# Historical consolidated split-frame files - 2026-10-19

The subsequent interlock revision adds locating pegs/sockets at all corner-rail
junctions. Comparison masses and images must come from the regenerated assembled
meshes. These include the socket clearances as internal cavities, not extra
solid parts. Catalogue counts and default filtering remain unchanged.

Each full version 2 model now has one catalogue folder containing the flat
two-half `3dpr` layout, individual `front` and `back` files, and an `assembled`
reference, all as SCAD and STL. Comparison rendering and measurement use the
assembled reference, so dimensions describe the complete unit. The short
joint-fit sample excludes pots. Oversized pairs require separate print plates.

The full populate -> OOMP -> SCAD comparison refresh completed successfully.
There are 31 printed and 15 purchased records; the default comparison shows
35 complete units, with eleven samples hidden. All 31 printed records have
current measurements and comparison images. All 45 mesh checks, ten mating-pair
checks, 22 geometry unit tests and six comparison tests passed. The 14-model
version 1 release lock also passed. Physical fit and printability still require
printing the trial parts.

# Historical split-frame update before consolidation - 2026-10-19

Version 2 now includes assembled references and separately printable front/back
halves, including a short joint-fit pair. There are 50 printed records and 15
purchased records. Separate halves are hidden by default and exclude pots from
cost/mass; assembled unit estimates exclude M3 screws/nuts. Six comparison tests
pass, including the half-component cost/ratio check. The current geometry report
has 34 passing meshes and ten passing mating pairs; version 1 remains locked.
The comparison regeneration uses the unchanged populate -> OOMP -> SCAD flow
and actual CSG meshes for images and costs. Historical browser checks below
refer to the earlier catalogue size.

# Drawer comparison validation — 2026-10-18

- All 31 current parts have comparison images: 15 cached seller photographs and
  16 PNGs rendered from current SCAD with the Manifold backend.
- Every generated mesh has positive volume and is watertight. These checks are
  for material estimation; they do not validate physical fit or strength.
- All 31 image URLs returned HTTP 200 through the running webserver.
- Browser review checked the cards, comparison table, numeric price sorting,
  and the purchased filter (15 records). Default view has 26 records: 11 full
  printed units and 15 purchased units. Five fit/layout samples are opt-in.
- Geometry tests: 13 passed. Comparison tests cover mass/cost/VAT calculations,
  numeric sorting, unknown values last, capacity filtering, samples, stale
  measurements, route rendering, filter-preserving sort links and the homepage.
- The broader pre-existing webserver suite has five failing expectations in
  unchanged file-action/manual-editor behavior: expected `delete-file` and
  launch action IDs are absent, one printer URL expectation is outdated, and
  the detail template no longer contains the expected “Collapsed by default”
  text. These are not changes to drawer comparisons. See `web_tests.log`.

Pot price evidence: live variant selection in the in-app browser, 500-pot
cartons, first quantity tier. Systempak 209: £60.95 ex VAT, £73.14 inc VAT,
£0.14628 per pot; 214: £80.95 ex VAT, £97.14 inc VAT, £0.19428 per pot.
Both live variants show backorder. Lids are included in purchase prices but
excluded from assembled mass. Manufacturer technical sheets give pot masses
of 8 g and 16 g. See URLs in `working_oomp_populate_comparison.py`.

Photos are sourced from each seller's product page/CDN, not generated images.
RS product pages 2675610/2675611 intermittently denied page access; their
product-number image assets were retrieved from the same RS media CDN and
visually checked (30- and 24-drawer cabinets). `photo_contact_sheet.png` records
the image review in proposal-number order.
