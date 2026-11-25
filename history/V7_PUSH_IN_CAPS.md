# Square and corner-clearance push-in caps

Each complete two-sided drawer unit now includes **four corner-clearance
caps**, with full-square caps for its remaining snap locks. Both are the
current push-in, friction-only clip lock; stem, spreading, cup cavity,
offset and pointed nose retain the preceding fit.

| Unit | Corner-clearance caps | Full-square caps | Total |
| --- | ---: | ---: | ---: |
| Small plywood, 2 x 7 per face | 4 | 30 | 34 |
| Large plywood, 4 x 12 per face | 4 | 108 | 112 |
| Sample, 1 x 2 per face | 4 | 4 | 8 |
| Sample, 2 x 2 per face | 4 | 8 | 12 |

`front_plug.stl` is the existing single cap with corner reliefs.
`front_plug_square.stl` is the new single cap without those reliefs.
The square has the same small outer corner rounding as the existing cover.
These individual files are spares. Both print outside face down, stem up.

For a complete cap set, use `push_in_cap_files.zip` in the relevant active
part folder. Print each listed `front_plugs_corner_clearance` and
`front_plugs_square` batch once, including all numbered square batches.
Four means four across BOTH faces, not four per face or per container.
The assembly uses two relieved caps per face on the outer snap positions
nearest the corner fixings. `cap_component` in `assembly.json` identifies
each position. The other snap positions receive full-square caps.

The old all-relieved `front_plugs` batches have been retired from active
part folders and retained in the preceding snapshot. Do not add old batches
to the new mixed batches. Full print kits and finishing upgrade kits include
the mixed cap counts. `cap_preview.png` shows square on the left and relieved
on the right.

The shortened beams remain 15 mm shorter overall (7.5 mm per drawer bank),
with the configurable reduction in `working_scad.py`. Face geometry,
beam geometry, screw adapters, pads and hardware are unchanged by this cap
revision. Current cap counts originate in `working_oomp_populate.py`;
cap geometry and assembly are generated in `working_scad`.

Regenerate with `python action_generate_current_v7.py`, preserving
population -> OOMP -> SCAD. Current reports are in `validation_v7_caps`.
Its immutable `preceding_active_manifest.json` protects the preceding
active files and original source copies. CAD checks cover quantities,
stem identity, restored corner material, assembly volume and configured
drawer/fixing-head clearance. Physical fit and frictional hold still need
testing.

Validation completed: 133 source tests, nine comparison tests, 100 closed
mesh views, 27 DXFs, 192 interchangeable beam/mount combinations (384 ends),
and all 166 actual cap placements pass. Both cap variants have matching
stems; full-square caps restore corner material and clear the configured
drawer and fixing-head paths. All existing individual part STLs remain
byte-identical to the preceding shortened-beam revision. All 23 ZIPs and
the 346-file preceding snapshot verify. Assembly and cap previews inspected.
