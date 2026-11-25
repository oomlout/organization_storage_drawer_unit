# Configurable shorter V7 beams

The 2026-11-03 revision removes 15 mm from the span of both beam types,
allowing 7.5 mm more of each opposing bin to project outside its face.
The current four units now have a 197 mm rail span between inside faces
and a 209 mm outside-face frame depth. Width, height and face shapes stay
the same. Move the faces 15 mm closer together when assembling these beams.

Configure `V7_BEAM_DEPTH_REDUCTION_PER_END` near the top of `working_scad.py`
(default **7.5 mm**). A SCAD-stage input named
`beam_depth_reduction_per_end` overrides the default; **0** restores full
depth. The default applies to current side-printed V7 frames only. The
container dimensions in population are unchanged. Both beam ends and all
end fittings retain their full engagement lengths; material is removed
from the running span, and the centre stop follows its midpoint.

Regenerate through the normal pipeline:

```powershell
python action_generate_current_v7.py
```

This runs population, OOMP and SCAD in order, exports meshes and DXFs,
checks assembly fit, and refreshes the previews and manufacturing ZIPs in
each active `parts` folder. Source checks:

```powershell
python -m unittest discover -s tests -q
```

For an existing finishing-revision unit, use `shorter_beam_files.zip` in
its active part folder: print each listed snap/screw beam batch once.
Reuse its faces, friction covers, adapters and hardware.
The full and finishing upgrade kits still include their complete listed
batches; avoid printing spare individual beams in addition to batches.
Enclosure spacing must suit the new depth. Physical bin fit, loading and
creep require testing.

The original shorter-beam report is `validation_v7_shorter_beams/report.json`;
the current mixed-cap kit reports to `validation_v7_caps/report.json`.
See `V7_PUSH_IN_CAPS.md` for the two cap styles and four relieved caps per unit.
The preceding
active files are under `previous_current`, source copies are under
`previous_sources`, and `preceding_active_manifest.json` protects both.
Earlier validation folders and archived releases remain historical.
