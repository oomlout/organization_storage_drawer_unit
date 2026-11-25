# V6 screw rails using the existing plate holes

Four screw-fastened rails replace four snap rails in each cabinet, at the
left/right outermost mounts on the uppermost and lowermost working shelf rows.
The existing face plates and holes are unchanged. All remaining snaps retain
the physically preferred sample-37 fit.

| Per cabinet | 250 version | 395 version |
|---|---:|---:|
| Snap rails | 17 | 56 |
| Screw rails | 4 | 4 |
| External screw adapters | 8 | 8 |
| M3 x 20 mm countersunk screws, supplied separately | 8 | 8 |
| M3 nuts, supplied separately | 8 | 8 |
| Front/back face plates | 1 each | 1 each |

Each screw rail is 212 mm long, retains the running shelf and central drawer
stop, and has reinforced 13 mm-high ends. At each end the screw axis is 8 mm
above the rail's flat print face. An OOBB M3 nut pocket sits 7-10 mm inward,
with an overhang-aware cut and a local +X side-loading clearance. The screw
passes 1.6 mm beyond the nominal nut-pocket end into a clearance bore.

The small adapter has an **11 x 10 x 2.4 mm** rounded external flange with an
OOBB M3 countersink. Two **1.5 mm-wide cheeks** extend **5.5 mm into the 6 mm
plate**, stopping 0.5 mm short of the beam. The guide stays narrow enough to
pass the receiver's outer throat throughout insertion; its leading tip has
0.5 mm chamfers. Its central opening avoids thin, fragile bore walls, while
the circular flange bore locates the screw.

The adapter flanges sit **2.4 mm proud of each plate**. The original 224 mm
frame depth remains, with **228.8 mm overall plastic depth** including adapters.
Screw heads seat flush with the adapter faces. Plywood dimensions and the
optional corner-joining plates remain separate.

For a new unit:

1. Print one `front.stl`, one identical `back.stl`, and every mixed
   `rails_plate_*.stl` batch once.
2. Print `screw_adapters.stl` once for all eight adapters. Keep their supplied
   outside flange/countersink faces on the bed and cheeks pointing up.
3. Side-load eight M3 nuts into the four screw rails before closing the cabinet.
   Rails print on their long flat face. Inspect the nut-pocket bridges in the
   slicer with your usual PETG settings.
4. Put screw rails at the four marked outer upper/lower positions shown in
   `assembly.json`. Fit the remaining snap rails and the second face plate.
5. Insert adapters from outside, cheeks into the existing snap openings and
   flange against the plate. Fit the eight M3 x 20 countersunk screws through
   them and into the beam nuts.

For an already printed all-snap cabinet, `screw_upgrade.stl` contains exactly
**four screw rails and eight adapters** in one **157.5 x 212 mm** layout. It is
identical for both sizes. Print this alternative once and replace four rails;
do not also print it on top of the full mixed rail batches. Existing plates
remain compatible. `screw_rail.stl` and `screw_adapter.stl` are individual spares.

Each part folder has `print_files_screw_adapter.zip` with the faces, mixed rail
batches, adapter batch, individual spares, alternative upgrade, optional
joining plates and assembly/printing instructions. The oversized `3dpr.stl`
overview and `assembled.stl` reference are excluded from that archive.

Population owns the design inputs in `screw_rail_settings`. The mandatory
pipeline is `working_oomp_populate -> working_oomp -> working_scad`. Bodies
remain in `working_scad`, complete removals in the v6 cutout, and the normal
SCAD stage emits metadata. No generated design file is hand-patched.

Run `python action_validate_double_sided_v6.py --variant
double_sided_plywood_250_max` or the `double_sided_plywood_395_max` variant.
Reports and the immutable pre-change snapshot are under
`validation_double_sided_v6_screw_adapter/`. Validation checks closed solids,
counts, bed envelopes, unchanged plates and sample-37 snaps, all mixed rail
fits, assembly volume, external adapter insertion, countersink flare, complete
head/shank clearance, nut side-loading and axial capture, retained nut walls,
guide cheeks and seating stops. OOBB true hardware dimensions probe the
OOBB 3dpr clearance geometry.

All **88 source tests, nine comparison tests and 27 exported mesh views pass**.
The new parts and joint previews were inspected. Physical screw fit, torque,
bridging, PETG strength and cabinet loading still require a print trial.
