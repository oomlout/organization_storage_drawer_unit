# V7 selected sample 71 unit, one wide by two tall

The user selected sample 71's clip style and tolerance on 1 November 2026.
They requested a slightly sharper plug and a unit with four snap beams and
two M3 screw beams, confirming **one drawer wide by two drawers tall**.
This retains the established two-sided cabinet: two drawers per face,
four Systempak 209 / 100 ml containers total.

The new population option is `unit_1_wide_2_tall`. All six previous V7 inputs
and their 150 SCAD/STL/ZIP files were saved before changes and remain protected
by `validation_v7_unit_1x2/previous_v7_baseline.json`. Source and part copies
are in the same validation directory. Never refresh this baseline to accept
geometry changes. Preserve every user-owned results.csv and all V1–V6 locks.

## Selected interface and pointed plug

The beam ends retain sample 71's 7 mm nominal slots, radiused roots, 1.2 mm
spring tips, 1.4 mm hooks, 0.1 mm axial allowance, top support and 5.2 x 5.2 mm
receiver. Both inner arms must touch fully to pass through the hole. The
fitted plug remains a smooth **2.6 mm friction stem**, spreading each arm
0.1 mm, with the same cover and seating skirt. There are no detents or arm
pockets. Only the nose width changes from 1.8 to 0.8 mm; nose depth and the
full-width transition station remain unchanged. The small flat avoids a
needle-like printable end. The original 70/71 plugs remain untouched.

Full beams omit the coupon's recessed number. The first 20 mm inside each
end and the entire external interface otherwise match sample 71. The
centre running shelf rises from the 7 mm grip to 10.5 mm over 3.5 mm and
retains the original drawer bearing elevation. Its centre wings provide
the 3 mm stop between opposite drawers. The two M3 braces are above the
openings and have no drawer stop; nut pockets are side loaded at both ends.

## Layout and quantities

The frame is **108.5 x 99.8 x 224 mm**. The top/bottom bands are 20 mm so the
two upper screw braces fit clear of the drawer openings and the external
adapters leave the corner fixing screws accessible. These bands serve the
additional beams; the drawer openings and row pitch are unchanged.
External snap covers increase overall depth to 233.2 mm.

For the printable version, print each file below once:

| File | Contents |
| --- | --- |
| front.stl | One face with angled stops and inward floor tabs |
| back.stl | One identical face |
| snap_beams.stl | Four complete beams, eight snap ends |
| screw_beams.stl | Two complete upper braces |
| front_plugs.stl | Eight pointed friction covers |
| screw_adapters.stl | Four outside M3 countersunk guides |

Supply four M3 x 20 countersunk screws and four M3 nuts, one per screw-brace
end. Corner fixing hardware depends on the surrounding enclosure.
Beam batches need a P1P-size bed: snap beams include their projecting tips
and measure about 229 mm long. Keep the supplied long-face-down orientations.
Plugs print cover face down, stem up. Adapters print outside face down.
Individual part STLs are spares; the optional sample and receiver are coupons.
The assembled and full-kit overviews are reference files, not single prints.

For laser faces, cut `front_laser_2d.dxf` twice from measured 6 mm MDF instead
of printing front/back. It has solid 6 mm stops, matching rectangular receivers
and corner holes. Units are mm and contours are finished dimensions on CUT;
apply measured kerf compensation once in CAM. MDF does not reproduce the
12 mm inward printed floor tabs. The enclosure must supply floor support;
the physical bottom drawer also requires the established plywood support.

## Generation and verification

Always run population → OOMP → SCAD. Bodies are in `working_scad.py`;
removals are in `working_scad_container_cutout.py`; `working_scad_v7_unit.py`
writes views, DXF sources and assembly/printing metadata in the ordinary
SCAD stage. Run `python action_validate_v7_unit.py`. Reports are under
`validation_v7_unit_1x2`, delivery under `output_v7_unit_1x2`.

The validator checks closed meshes, bed contact, exact batch quantities,
volume conservation, both complete beam ends against sample 71, full arm
contact, plug insertion and expansion, all twelve ends at the actual faces,
nut loading and capture at both screw-brace ends, screw shank paths,
external guide insertion, accessible corner fixings and matching flat DXFs.
The assembly reference shows the prescribed expanded clip state with an
extra 0.001 mm opening per arm to keep coincident plug/arm contact surfaces
from producing degenerate STL triangles. Manufacturing files retain the
exact selected fit. This is a geometric illustration, not an elastic
simulation or strength rating.

The user's selection is fit/design feedback. Complete-unit force, loaded
deflection, PETG creep, MDF edge wear, floor support and long-term loading
still require physical testing.

Completed verification: 110 source tests and nine comparison tests pass.
All 15 mesh views are closed, the full print overview contains 20 pieces,
and the two DXFs match their flat meshes (13 face contours, two coupon
contours). Both complete snap-beam ends match the approved interface.
Full-closure arm gap is below 0.000001 mm with zero overlap; 95% closure
is blocked. Plug drive interference is below 0.00015 mm³. All twelve beam
ends fit the actual faces. Both screw-brace ends pass nut loading/capture,
and the screw shank and countersunk head paths pass. All earlier locks
and six V7 inputs / 150 geometry/package files remain unchanged. Assembly,
face, beam-batch and pointed-plug previews were visually inspected.
