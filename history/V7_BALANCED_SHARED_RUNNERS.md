# Centred shared runners — 2026-11-01

The face/receiver alignment here is retained. `V7_FINISHING.md` supersedes
the end parts: print new upward-stop beams, half-depth screw adapters and
offset locks, and reuse these balanced/handed faces. Its adapter flange
also clears the configured drawer passage and corner-head envelope.

The user confirmed that the unequal support at shared dividers should be
corrected by centring the running strip and moving the snap receiver holes.
This revision keeps the existing printable beam shapes and moves the
**shared-divider receiver columns 1.5 mm in front-face CAD +X**. It applies
to snap and screw receivers at those columns so both beam types remain
interchangeable. The outer receiver columns retain their existing positions.

## Result

The existing runner is 8 mm wide and 3 mm thick, with its clip axis 1.5 mm
off the runner centre. In the assembled frame, its old support edges were
-5.5 / +2.5 mm from a shared divider. The new edges are **-4 / +4 mm**.
With the 89.3 mm drawer pitch and nominal 86 mm pot lip width:

| Shared-divider bearing | Left drawer | Right drawer |
| --- | ---: | ---: |
| Preceding face holes | 3.85 mm | 0.85 mm |
| Revised face holes | **2.35 mm** | **2.35 mm** |

The roof remains 8 mm above the receiver axis on both sides, and the
running strip remains 3 mm thick. These figures are measured from exported
beam sections and the nominal container envelope, not a physical loading
test. See `validation_v7_balanced_runner/shared_runner_comparison.png`.

The current snap/screw beam, friction cover, screw adapter and receiver
coupon STLs are unchanged. The shorter 5 mm clip slots and OOBB v5 nut
pockets remain as in the preceding side-printed revision. Reuse those
parts. The one-wide/two-tall sample has no shared dividers, so its face
geometry is unchanged too.

## Revised faces and laser pads

Multi-column units need the **revised faces**. Printed front and back are
now **handed**: the back's local hole pattern is mirrored so rotating it
into the rear position aligns both beam ends. Print `front.stl` ONCE and
`back.stl` ONCE, outside face down. Do not print two copies of the front.

For flat laser faces, cut `front_laser_2d.dxf` twice as before, then keep
the shifted holes at the **same global horizontal positions** through the
assembled unit. A flat through-cut sheet has no printed inward floor tabs;
choose its inside surface so the holes align. Do not mirror the horizontal
hole positions between the two assembled faces.

For the optional 3 mm face test, reinforcing squares remain centred on
their dividers. **Shared-divider squares have an offset hole**, 1.5 mm
from the square centre in front-face CAD +X; outer squares retain centred
holes and existing corner-bore reliefs. The minimum edge land around an
offset 5.2 mm hole is 1.9 mm. Moving the whole square would intrude into the
bin opening, so keep the square's divider datum and move only its hole.
The revised nested cut layout includes the proper quantities and hole
positions. Cut it once per face, without adding a pads-only set.

Do not combine the preceding and revised receiver positions by enlarging
the old holes: that changes snap retention. Use the revised face files.

Each multi-column part folder has `face_alignment_files.zip`, containing
the new printed faces, laser alternative, optional 3 mm layouts/pads,
assembly preview, metadata and printing instructions. Existing full kits
are refreshed too. `beam_replacement_files.zip` still contains unchanged
beams/covers and now directs users to the revised faces for centred support.

## Source and validation

Population owns `runner_alignment.shared_receiver_offset_x=1.5`.
`working_scad` derives shared-column mounting axes and pad hole offsets;
complete receiver and reinforcement removals stay in
`working_scad_container_cutout`. The printed back uses the handed pattern.

Run `python action_generate_current_v7.py` for
`working_oomp_populate -> working_oomp -> working_scad`, exports, validation,
previews and ZIPs. Use `--variant unit_2_wide_2_tall` to build just the
inspection unit. Reports now go to `validation_v7_balanced_runner`.
`action_preview_v7_balanced_runner.py` reproduces the before/after section
figure from the preserved preceding and current STLs.

The validator checks actual front **and handed back** meshes at both beam
ends, equal shared-divider bearing and roof height for both beam types,
stop reach, pad containment and seating, DXFs, bed contact and kit counts.
Shared component STLs are compared byte-for-byte with the preceding active
catalogue. That catalogue and its source copies are preserved in
`validation_v7_balanced_runner/previous_current`, `previous_sources` and
the immutable `previous_current_manifest.json`.

Physical lateral play, lip support under load, insertion force and creep
remain unmeasured. The preceding outer-corner screw-adapter/head constraint
remains unchanged. An enclosure still supplies drawer-floor support.
At a shifted working receiver, substituting an M3 beam brings the unchanged
adapter flange 0.6 mm into the configured body-clearance envelope. Shifted
M3 beams in the default small samples sit above the openings; test actual
pot travel before making that optional working-row substitution. Receiver
fit checks do not establish clearance for the complete moving pot.

Completed: **124 source tests, nine comparison tests, 93 closed mesh views,
27 DXFs and 192 mounting combinations (384 ends)** pass across all four
current units. All 92 shared-receiver/beam comparisons confirm 2.35 / 2.35 mm
nominal bearing and matching roof height. Actual handed rear meshes,
reinforcement placement/seating, bed contact, stop reach and kit volumes
pass. All six shared component STLs match the preceding active files
byte-for-byte. The one-wide sample's 47 CAD/STL/preview files are identical;
its five regenerated DXFs have identical entities. Assembly previews and
the before/after section figure were inspected. Full, replacement and face
ZIP contents and SCAD dependencies were verified, along with the 296-file
preceding snapshot, immutable archives and earlier release locks.
