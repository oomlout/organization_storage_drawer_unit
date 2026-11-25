# Version 2 development

Created 2026-10-19 as an independent copy of the locked version 1 release,
including the last requested 1.5 mm extra opening height per 550 ml drawer row.
Version 1 retains its existing IDs; version 2 uses `ai_version_2_style`.
Each version has fourteen models, covering both containers and all fit/layout,
reference and printer variants. Basic models and purchased catalogue records
are unchanged.

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

Both versions start with 95 mm opening height for the 550 ml container:
92 mm lidless body + 1.5 mm normal clearance + 1.5 mm extra vertical space.
The extra is an option input `opening_height_extra`, not a change to the pot's
physical dimensions. One-row frame height increases 1.5 mm; two-row height
increases 3 mm. Ear-inclusive envelopes become 92.3 x 140.8 x 109.5 mm
and 181.6 x 237.6 x 109.5 mm. The 100 ml models remain unchanged.

Locking a CAD release does not establish physical fit, printability or strength;
the existing physical test sequence in AI_VERSION_1.md still applies.

## Initial verification

All sixteen geometry/unit checks and five drawer-comparison tests passed.
Both sets of fourteen exported meshes passed validation. All fourteen paired
SCAD files are identical, and paired mesh volumes agree within 0.01 mm3.
All eleven 100 ml SCAD files are unchanged from the pre-release snapshot.
The final comparison pipeline refreshed all thirty printed designs.
