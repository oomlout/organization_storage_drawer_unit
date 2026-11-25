# 19: aggressive twin tabs with internal catches

This PETG test adds the requested two-tab push-in alternative to the separate
locking-key experiments. It has **no middle guide and no loose key**.
Both tabs enter one rectangular throat and spring outward into a wider
receiver pocket. Retaining edges stay inside; the tips finish flush with
the front face. The receiver seats directly against the full-width beam,
without the earlier exposed flexible neck or separate tab seating stops.
No full version 5 drawer unit is generated.

**Reprint both pieces for this revision.** The receiver's catch depth has
changed as well as the rail. Do not mix the earlier long-neck coupon 19
receiver with this revised rail.

The folder under `parts/` ends in
`ai_version_5_style_snap_recessed_twin`.

| File | Purpose |
| --- | --- |
| `3dpr.stl` / `3dpr.scad` | Both pieces positioned for printing |
| `plate.stl` / `plate.scad` | Matching rectangular receiver |
| `rail.stl` / `rail.scad` | Two-tab rail coupon |
| `assembled.stl` / `assembled.scad` | Assembly reference; not a print layout |

Both pieces have a recessed **19** on their print-top faces. Keep the supplied
orientation: the rail lies on its long face, while the receiver prints with
its **smaller entry face on the bed**. The larger pocket then opens above it:
the retaining ledges do not form unsupported roofs. The outside opening
remains accessible for inspection of hook recovery.

## Geometry

The rail retains the existing 11 × 10 mm section and 32 mm grip length.
The receiver is 15 × 14 × 7.5 mm.

| Feature | Dimension |
| --- | --- |
| Tabs | Two, 1.0 mm thick × 10 mm tall |
| Free tab length to hook shoulders | 6 mm, rooted at the beam face |
| Open centre gap | 4.8 mm, with a 2.4 mm-radius rounded end |
| Shallow slot root | Round-end centre 0.5 mm inside beam; closes by 2.9 mm |
| Hook projection | 1.2 mm per tab |
| Nominal inward flex to pass the throat | 0.95 mm per tab |
| Hook lead-in length | 1.5 mm |
| Throat | 7.3 × 10.5 mm rectangle |
| Wider catch pocket | 9.7 × 10.5 mm |
| Internal receiver shoulder | 1.7 mm from the front face |
| Seated hook shoulder | 1.5 mm from the front face |
| Seated tip inset from front face | 0 mm — flush |
| Seating stop | Full-width beam shoulders directly against receiver entry |
| Side clearance | 0.25 mm |
| Axial catch clearance | 0.20 mm |
| Recessed label depth | 0.60 mm |

The larger hooks and full-height tabs make this a more aggressive candidate
than the original direct snaps. The retaining shoulders are square.
The open slot lets both tabs move inward without a central spine. The user
requested a much shorter joint: free length has reduced from 15.5 to 6 mm
and the exposed neck has gone. The tabs have been thinned from 1.4 to 1.0 mm
to help them bend, but this remains a substantially stiffer, more demanding
snap than the long-neck coupon. Its PETG behavior needs a physical trial.

## Print and try

Use the same established PETG profile as the earlier coupons. Preserve
the supplied orientations and check that the slicer keeps the tab walls
and lead-in tips. These are small solid comparison coupons, not a cabinet.

Push the tabs into the **smaller** receiver opening until the beam's broad
shoulders seat directly against the entry face. These prevent over-insertion.
The tips should then be level with the front face, and no flexible neck
should remain exposed between the receiver and beam.
Look through the larger outside opening to confirm that **both**
hooks have recovered behind the internal ledges. A tight partial insertion
is not a lock. Record seating effort, sideways/axial play, whitening,
layer damage and pull-out behavior against the key design.

This is intended mainly as a permanent connection. Strong insertion
resistance alone does not establish retention strength. Printed fit,
insertion force, sustained-load creep and failure loads are not yet measured.

## Source and validation

Population owns this independent `snap_recessed_twin` option and its settings.
`working_scad` supplies a single solid rail envelope and the receiver body,
plus printing/assembly transforms. The single v5 cutout routine carves the
open centre, round root, hook contours, rectangular throat, internal pocket
and recessed labels. No generated CAD is hand edited.

Run `python action_validate_recessed_tabs.py` for the full
populate → OOMP → SCAD pipeline, four STL views and previews.
Checks cover closed solid meshes, exactly two print pieces, bed contact,
unsupported downward faces, absent middle material, two distinct tabs,
flush tip placement, internal shoulders, beam-to-plate contact, seated clearance,
over-insertion stops, withdrawal
interference and sampled insertion with prescribed inward flex.
This flex check is geometric, not FEA or an insertion-force prediction.

Earlier v1/v2/v3 locks, the v4 baseline, and all seven previous v5 records
and SCAD views are checked unchanged. The saved pre-change v5 baseline is
`validation_recessed_tabs/previous_v5_baseline.json`; do not overwrite it.
The result report is `validation_recessed_tabs/report.json`.

Verification passes all four exported views, all connection checks,
47 geometry tests and seven comparison tests. Earlier release/input/CAD
checks pass too. Both print pieces are closed solids, sit at Z=0 and have
no airborne downward-facing surfaces in the supplied orientation. The kit
occupies **37 × 39.5 mm**. CAD material estimates use 1.27 g/cm³ for PETG;
they are not slicer measurements.
