# V7 interchangeable beams with material-saving windows

On 1 November 2026 the user corrected the screw beams to be **drop-in
replacements for the snap beams**, and requested rounded rectangular
cutouts in the middle of the beams. The active `unit_1_wide_2_tall` option
now supplies four windowed snap beams and two windowed screw beams.

## Interchangeability

Both beam types seat 212 mm between the same inside panel faces and use the
same 5.2 x 5.2 mm through-hole. Their running roof is 8 mm above the hole
centre in service. Both have a 19 mm-wide, 3 mm-thick centre stop at the
same axial position, separating the two opposing drawer banks. Either
beam may occupy any of the six receiver positions; the default assembly
keeps four snaps at the working shelf levels and two screw beams at the top.

The screw beam's M3 nut needs more material beneath the bore than the snap
tongue does. It prints with a 6.5 mm-high screw axis and 14.5 mm running roof;
the snap prints with a 2.5 mm-high tongue axis and 10.5 mm roof. Those print
heights differ by the same 4 mm, so the roof aligns when each axis locates in
the same receiver. The screw beam has reinforced 13 mm-high ends, rising to
the running roof behind the ends. Its additional lower reinforcement remains
2 mm above the nominal drawer floor at the working levels. This is a fit
and functional replacement; the reinforced screw beam has a deeper section.

The snap ends remain sample 71, including 7 mm slots, full-squeeze hooks,
upper bearing and the selected tolerance. The pointed friction plug, screw
adapters, coupons and face plates are unchanged from the preceding unit.

## Rounded cutouts

Each beam has two **5 x 63 mm rounded rectangular through-windows**, with
2 mm corner radii. Each side retains a continuous 3 mm rail. The first
35 mm at each beam end remains solid, beyond the spring roots/nut pockets
and roof transitions. A 16 mm-wide axial island remains solid around the
3 mm-thick centre stop. All parts still print on their long flat faces.

These holes reduce solid CAD material. Force, stiffness, sag under load,
print bridging, creep and long-term durability need physical evaluation;
no strength rating is inferred from the volume reduction.

## Files and assembly

Use `output_v7_unit_interchangeable/v7_unit_interchangeable_beams.zip`.
Print front, back, snap_beams (four), screw_beams (two), front_plugs (eight)
and screw_adapters (four), **each file once**. Individual beam STLs are spares.
For upgrading the preceding unit, print only the beam batches needed;
reuse the same face plates, pointed plugs and M3 adapters.

Supply four M3 x 20 countersunk screws and four M3 nuts. The unit remains
one wide x two tall on each of two faces: four Systempak 209 containers.
Frame size is 108.5 x 99.8 x 224 mm, 233.2 mm including the snap covers.
Use a P1P-size bed for the 228.8 mm snap beams. The matching laser DXF is
included for cutting two alternative 6 mm MDF faces. Printed stops remain
angled; MDF stops remain solid through the sheet. The enclosure must still
supply floor support, especially for the bottom drawer and the MDF option.

## Source and checks

Always population -> OOMP -> SCAD. Population owns the window dimensions and
the replacement selection. `working_scad.py` composes the positive beam bodies;
`working_scad_container_cutout.py` owns all complete removals. Metadata and
print instructions come from `working_scad_v7_unit.py`. Run
`python action_validate_v7_unit.py`; reports are now in
`validation_v7_unit_interchangeable`.

The preceding solid unit was preserved before editing in
`validation_v7_unit_interchangeable/previous_unit`, alongside its input/hash
manifest, delivery files and source snapshot. Its historical output/report
folders remain intact. The six earlier V7 records and all V1–V6 locks remain
mandatory. Never refresh their baselines or overwrite user results.csv files.

Validation checks both beam types at every receiver on both actual faces,
matching bearing roofs and centre stops, full-depth rounded windows, side
rail thickness, volume reduction, unchanged snap ends and ancillary parts,
nut loading/capture at both ends, screw/head paths, print quantities, closed
meshes, bed envelopes and matching flat DXFs. The assembly reference retains
the previously documented 0.001 mm visual clearance at expanded snap arms.

Completed: **112 source tests and nine comparison tests pass**, along with
15 closed mesh exports and two matching DXFs. Both beam types fit all six
positions on both faces (24 ends), and their actual bearing roofs and centre
stops align. The windows are through-cuts with retained rounded corners,
3 mm side rails, solid ends and a solid centre. Snap interfaces, full squeeze,
friction plug drive, M3 nut loading/capture and screw/head paths pass. The
existing face, plug, adapter and coupon STLs are byte-identical. All six
earlier V7 inputs / 150 files and the V1–V6 locks remain unchanged. Updated
beam comparison and complete assembly previews were visually inspected.

Measured solid CAD volume reductions versus the preceding delivered parts:
**29.70% snap / 20.88% screw**. The screw result includes the added running
roof and centre stop. Against the same new beams with their windows filled,
the windows save 29.70% / 27.76%. These figures exclude slicer infill, walls,
supports and purge, and do not establish a strength or stiffness rating.
