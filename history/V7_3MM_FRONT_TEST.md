# V7 3 mm laser-face reinforcement test

The optional test uses a 3 mm sheet face and separate 3 mm inside doublers.
Each doubler is nominally 12 x 12 mm with the existing 5.2 x 5.2 mm hole in
its centre. The resulting nominal thickness at every snap and screw receiver
is 6 mm. The inside beam seating plane, outside cover/adapter plane and
existing connectors remain at their established positions.

Every receiver is covered, including M3 beam positions:

| Face | Plain squares | Left corner relief | Right corner relief | Total per face |
| --- | --- | --- | --- | --- |
| 1 wide x 2 tall sample | 6 | 0 | 0 | 6 |
| 2 wide x 7 tall plywood | 19 | 1 | 1 | 21 |
| 4 wide x 12 tall plywood | 58 | 1 | 1 | 60 |

At the lowest outer receivers on the plywood sizes, a plain square would
partially cover the adjacent corner mounting bore. The two handed versions
have a small relief clearing that bore, with .1 mm radial allowance. Their central receiver hole and
nominal square size are the same. Orient the relieved corner towards the
nearby corner mounting hole. The original outside mounting-head plane stays
clear because the extra material is on the inside.

In each active part folder:

- `front_3mm_test_2d.scad` / `.dxf`: one complete face plus all its reinforcing
  pieces, nested in the bin-opening waste. Cut ONCE from measured 3 mm sheet
  for each face being tested. The nested pieces are loose parts after cutting.
- `clip_reinforcement_2d.scad` / `.dxf`: one plain spare square.
- `clip_reinforcement_corner_left_2d` and `...corner_right_2d`: handed spares
  on the two plywood sizes.
- `clip_reinforcements_2d.scad` / `.dxf`: the complete set of doublers only.
  This is an alternative to the nested pieces, not an additional quantity.
- `front_3mm_test.scad` / `.stl`: reference showing the bonded 3 + 3 mm face.
- `front_3mm_preview.png`: inside view of the assembled reinforcement.
- `front_3mm_layout.png`: flat cut layout.

Bond each reinforcement flat to the INSIDE of the face, centred on its
receiver. Align both receiver holes accurately. Actual sheet thickness and
the bondline determine the finished stack; compare it with the existing
6 mm receiver and test a connection before bonding a full face. The sample
71 snap, friction cover, screw adapter and M3 beam require their existing
6 mm local interface. The squares remain inside the upright's material and
clear the bin openings.

The standard `front_laser_2d` remains the 6 mm face alternative. Printed
faces, beams, covers, adapters and historical releases are unchanged. A
first trial can replace only the front face while retaining the existing
back. If testing both faces, cut the full layout twice. The thinner laser
stops and lowest drawer still require enclosure floor support; no enclosure
joinery or attachment method is supplied.

This is the requested physical experiment. CAD verifies placement, holes,
clearances and cut layouts; it does not establish 3 mm face stiffness or
bond strength. Record bowing, wobble, local damage and bond behaviour under
progressive load.

Dimensions live in `get_current_options()` in `working_oomp_populate.py`,
bodies in `working_scad.py`, and complete hole/relief removals in
`working_scad_container_cutout.py`. Regenerate with:

```powershell
python action_generate_current_v7.py
```

This preserves population -> OOMP -> SCAD and includes the new deliverables
in each `print_files.zip`. Original active geometry hashes/source are in
`validation_v7_3mm_front/`; detailed checks are under
`validation_current_v7/` in each unit's `laser_face_test` report.

Completed validation: 118 source tests, nine comparison tests, 71 closed
mesh views and 19 DXFs pass. All 87 reinforcements fit within existing
upright material; all snap/screw receiver combinations and outside parts
fit. Stack thickness, seating lands, nested piece counts, cut contours and
corner-bore clearances pass. The 116 prior active SCAD/STL files are
byte-identical. Previews inspected; ZIP contents and SCAD dependencies
verified. Summary: `validation_v7_3mm_front/report.json`.
