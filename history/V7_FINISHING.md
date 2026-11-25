# Upward stops, split-depth screw joints and offset locks — 2026-11-01

This revision changes the current printed beams, friction covers and screw
adapters. Reuse the preceding balanced/handed faces, laser faces/pads, M3
screws and nuts. The frame holes and equal shared-divider bearing stay as
in `V7_BALANCED_SHARED_RUNNERS.md`. Historical options/releases are unchanged.

## Centre stop

Both snap and screw beams have a stop rising **6 mm above the running
surface** at the existing central axial station. Stop width and thickness
remain 12 mm across the beam and 3 mm along it. The previous downward stop
extension is removed. A 0.05 mm overlap into the runner produces a reliable
union; the exposed rise above the runner is exactly 6 mm.

The running strip stays 8 x 3 mm, with the same 8 mm bearing elevation above
the receiver axis and the same side-print orientation. The clip arms still
print flat and retain the current 5 mm slots and full-squeeze/friction fit.

On the one-wide and two-wide small samples, the separate top screw braces'
stops rise 1 mm above the faces: nominal overall height is **100.8 mm**,
while the face remains 99.8 mm high. The two plywood units' overall height
is unchanged. No face envelope has been enlarged.

## Screw beam and outside adapter

The user confirmed a split of the **6 mm receiver depth**, not its
cross-section. Each side has **3 mm nominal engagement**. Actual beam and
adapter locating projections are **2.95 mm each**, leaving **0.1 mm** between
their tips when both shoulders seat on a nominal 6 mm panel.

The beam now has a 5 x 5 mm locating tongue extending into its half of the
5.2 x 5.2 mm opening. Its M3 bore continues through the new tongue on the
same axis as the existing side-loading OOBB v5 nut pocket. The adapter keeps
the open locating cheeks and lead-in chamfers, shortened to its half depth.
M3 x 20 countersunk screws, nut positions and 1.6 mm nominal projection
beyond the nut remain unchanged.

The new adapter flange is 10.3 x 10 x 2.4 mm, offset -0.35 mm in its local
X. Its trimmed edge clears the configured drawer-body passage at shifted
shared receivers by 0.1 mm nominally. Corner reliefs clear the generic
6 mm-diameter corner fixing-head envelope, resolving the preceding flange
constraint. The screw bore and countersink stay on the receiver axis.

At the rear, turn the adapter over without reversing its trimmed edge
between cabinet sides: keep trimmed edges toward the same cabinet side at
both ends. The assembly source and validation use the same orientation.
Print the outside countersink face down, cheeks up, as supplied.

The depth split assumes a measured nominal 6 mm interface. Sheet thickness,
bondline and print error affect the small mating gap and must be checked
physically before tightening. Do not reuse the preceding long-guide adapters.

## Off-centre push-in lock

The friction stem stays at the existing snap/hole axis, with its unchanged
2.6 mm fitted width, 0.8 mm nose and 0.1 mm spreading per arm. The covering
cup is now a nominal **9.8 x 9.8 mm** square, shifted **1.5 mm** around that
stem. In the assembled unit its cover centre lines up with the runner
centre on both faces. The cavity remains centred on the hooks, so changing
the cover does not change the friction fit.

The minimum straight rim wall is 0.6 mm away from the deliberate corner
reliefs. The complete receiver opening remains covered. The offset cover
clears the configured lip/body drawer passage, including the outer mounts.
The nominal passage is a clearance envelope, not a measured physical pot.

Print outside face down, stem up. Orient the head so its centre matches
the runner centre; the stem sits off to one side to enter the receiver.
Use the assembly preview to check the front and rear orientation. Reusing
the preceding centred-stem covers does not provide the new cover alignment.

## Files, source and checks

Each active part folder has **`finishing_upgrade_files.zip`** with the
required snap beam, screw beam, new lock and new adapter batches. Print
**each listed STL once**, in its supplied orientation. Individual component
files are spares; no extra quantities are required. `print_files.zip` is
the complete kit. `beam_replacement_files.zip` contains the same upgrade
content. `face_alignment_files.zip` remains available for the unchanged
balanced faces on multi-column units.

| Unit | New snap beams | New screw beams | New offset locks | New adapters |
| --- | ---: | ---: | ---: | ---: |
| 1 wide x 2 tall | 4 | 2 | 8 | 4 |
| 2 wide x 2 tall | 6 | 3 | 12 | 6 |
| 2 wide x 7 tall | 17 | 4 | 34 | 8 |
| 4 wide x 12 tall | 56 | 4 | 112 | 8 |

Population owns `finishing_revision`, `side_runner.stop_height`, the screw
depth split and clearance, flange dimensions/reliefs and cover offset.
Bodies stay in `working_scad`; all negative tools stay in
`working_scad_container_cutout`. Run `python action_generate_current_v7.py`
for **populate -> OOMP -> SCAD**, exports, validation, previews and ZIPs.
`--variant unit_2_wide_2_tall` selects the inspection sample.

Reports are in `validation_v7_finishing`. The preceding active catalogue,
sources and immutable SHA-256 manifest are preserved there in
`previous_current`, `previous_sources` and `previous_current_manifest.json`.
The earlier output and validation folders remain historical.

`action_validate_v7_finishing.validate` checks both actual guide depths and
their gap, both upward stops and absence of the downward extension, head
and screw paths, cover centring, corner heads and intrusion into configured
lip/body passages at every mount on both faces. Existing checks retain
actual handed-back fit, pad seating, shared bearing, bed contact, counts
and kit volumes. Face, reinforcement and clip-coupon geometry is compared
byte-for-byte with the preceding active files. The friction stem remains
unchanged above the cup.

`python action_preview_v7_finishing.py` reproduces the offset-lock, stop and
screw-joint cutaway images from the generated manufacturing SCADs. These
presentation references do not replace manufacturing sources.

Fit, force, lip support under lateral play/load, stop strength, sheet stack
thickness and creep still require physical testing. No load rating is implied.

Completed: **128 source tests, nine comparison tests, 93 closed mesh views,
27 DXFs and 192 beam/mount combinations (384 ends)** pass. There are 384
outside-fitting/passage checks and 192 actual cover-centre checks. Both
stops measure 6 mm above the runner; both screw ends measure 2.95 mm
engagement and a 0.1 mm mating gap. Shank/head paths, nut loading/capture,
unchanged friction stem, actual handed backs, pad seating, bed contact,
shared bearing and kit volumes pass. Face, pad and coupon STLs are
byte-identical to the preceding active files. All six common component
STLs are byte-identical across the current units. Assembly and detail
previews were inspected; upgrade/full ZIP counts, bytes, integrity and SCAD
dependencies were checked. The 317-file preceding snapshot, immutable
archives and V6 aggregate release lock verify. See
`validation_v7_finishing/report.json` and `delivery_checks.log`.
