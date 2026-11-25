"""V5 tile planning only. Bodies stay in working_scad; cuts in its cutout module."""
import copy
import math


def bed_pose(width, height, p):
    """Centre relative to bed centre. Keep the complete rectangle off the cutter."""
    margin = p["bed_margin"]
    bw, bh = p["bed_width"], p["bed_height"]
    ex, ey = p["bed_exclusion"]
    if width > bw-2*margin+1e-7 or height > bh-2*margin+1e-7:
        return None
    # Right/top placement preserves the actual corner exclusion, not a reduced
    # square bed. Every ear/link lies within the rectangle checked here.
    x, y = bw-margin-width/2, bh-margin-height/2
    if x-width/2 < ex+margin and y-height/2 < ey+margin:
        return None
    return [x-bw/2, y-bh/2]


def parameters(inputs):
    import working_scad as drawing
    p = drawing.get_ai_version_4_parameters(**{
        **inputs, "bed_width": 2000, "bed_height": 2000,
    })
    p.update(copy.deepcopy(inputs))
    p["style"] = "ai_version_5"
    p["natural_width"], p["natural_height"] = p["width_total"], p["height_total"]
    p["width_total"], p["height_total"] = p["target_width"], p["target_height"]
    if p["width_total"] < p["natural_width"] or p["height_total"] < p["natural_height"]:
        raise ValueError("Requested envelope is too small for these unchanged tray openings")
    p["plate_width"], p["plate_height"] = p["width_total"], p["height_total"]
    outer_x = max(r["x"] for r in p["rail_positions"])
    for rail in p["rail_positions"]:
        if abs(abs(rail["x"])-outer_x)<1e-6:
            rail["x"] += math.copysign(p["outer_mount_offset"],rail["x"])
        rail["axis_y"] = rail["y"]+p["nut_axis_height"]
    p["x_mounts"] = sorted({r["x"] for r in p["rail_positions"]})
    p["y_mounts"] = sorted({r["axis_y"] for r in p["rail_positions"]})
    pocket_wall = (p["thickness_wall"]+2*p["inset_lip"])/2 - (
        p["snap_profile"]["snap_arm_outer"]+p["snap_hook_projection"]+p["snap_clearance"])
    if pocket_wall < 1.2:
        raise ValueError("Snap receiver must retain at least 1.2 mm of the lip shoulder on each side")
    outside_wall = p["inset_lip"]+p["outer_mount_offset"]-(
        p["snap_profile"]["snap_arm_outer"]+p["snap_hook_projection"]+p["snap_clearance"])
    if outside_wall < 1.2 or p["outer_mount_offset"] > 1.2:
        raise ValueError("Outside mounts must retain snap walls and at least 4.3 mm of tray support")
    clearance = p["tile_seam_clearance"]
    if not 0 <= clearance <= 0.3 or not 0 <= p["tile_layer_clearance"] <= 0.2:
        raise ValueError("Tile gaps are limited to 0.3 mm sideways / 0.2 mm through thickness")
    if not 10 <= p["tile_lap_x"] <= 11 or not 8 <= p["tile_lap_y"] <= 9:
        raise ValueError("Keep laps inside the mounting lands and wider than countersinks")
    if not isinstance(p["additional_screw_every"], int) or p["additional_screw_every"] < 0:
        raise ValueError("Additional screw interval must be a nonnegative integer")
    if not 5.5 <= p["snap_tip_floor"] <= 6.0:
        raise ValueError("The bevel must retain a web in both lap layers and at least 4 mm-high tab tips")
    if not 0.4 <= p["snap_ledge_land"] <= 0.5:
        raise ValueError("Keep a small printable retaining land behind each hook")
    if not isinstance(p["seam_middle_screw"],bool) or p["seam_middle_min_span"] < 60:
        raise ValueError("Middle seam anchors need a boolean switch and a sensible span")
    ear = p["tile_ear_diameter"]+p["tile_ear_gap"]

    def partition(low, high, candidates, maximum, lap, extra):
        points = [low]
        while True:
            left = points[-1]
            left_extension = lap/2 if left != low else 0
            if high-left+left_extension+extra <= maximum+1e-7:
                points.append(high)
                return points
            possible = [v for v in candidates if v > left and
                        v-left+left_extension+lap/2+extra <= maximum+1e-7]
            if not possible:
                return None
            points.append(max(possible))

    plans = []
    # Either stay right of the cutter or above it. Greedy partitions take the
    # farthest available beam joint; no arbitrary cuts through tray openings.
    for xmax, ymax in [
        (p["bed_width"]-p["bed_exclusion"][0]-2*p["bed_margin"], p["bed_height"]-2*p["bed_margin"]),
        (p["bed_width"]-2*p["bed_margin"], p["bed_height"]-p["bed_exclusion"][1]-2*p["bed_margin"]),
    ]:
        xs = partition(-p["width_total"]/2,p["width_total"]/2,p["x_mounts"][1:-1],xmax,p["tile_lap_x"],0)
        ys = partition(-p["height_total"]/2,p["height_total"]/2,p["y_mounts"][1:-1],ymax,p["tile_lap_y"],2*ear)
        if xs and ys:
            plans.append((len(xs)*len(ys), -(xs[1]-xs[0])*(ys[1]-ys[0]), xs, ys))
    if not plans:
        raise ValueError("No beam-aligned tiling fits this printer with its ears/exclusion")
    _, _, xs, ys = min(plans)
    p["tile_x_edges"], p["tile_y_edges"] = xs, ys
    p["tiles"] = []
    for iy in range(len(ys)-1):
        for ix in range(len(xs)-1):
            layers = []
            bed_layer = (ix+iy)%2
            for layer in [0,1]:
                # Every lap on this tile occupies the SAME half of the plate.
                # Adjacent tiles alternate. The larger layer always prints down.
                expanded = layer == bed_layer
                bounds = [xs[ix],ys[iy],xs[ix+1],ys[iy+1]]
                for axis, edges, index, lap in [(0,xs,ix,p["tile_lap_x"]),(1,ys,iy,p["tile_lap_y"])]:
                    if index > 0:
                        bounds[axis] += (-1 if expanded else 1)*lap/2+clearance/2
                    if index+1 < len(edges)-1:
                        bounds[axis+2] += (1 if expanded else -1)*lap/2-clearance/2
                layers.append(bounds)
            bounds = [min(v[0] for v in layers),min(v[1] for v in layers),
                      max(v[2] for v in layers),max(v[3] for v in layers)]
            size = [bounds[2]-bounds[0],bounds[3]-bounds[1]+2*ear]
            pose = bed_pose(*size,p)
            if pose is None:
                raise ValueError("Tile including ears enters the bed exclusion")
            p["tiles"].append({"number":len(p["tiles"])+1,"column":ix,"row":iy,
                               "layers":layers,"notches":[[],[]],"bed_layer":bed_layer,
                               "print_face":"inside" if bed_layer else "outside",
                               "bounds":bounds,"footprint":size,"bed_center":pose})
    # Diagonally adjacent expanded layers meet at four-way crossings. Assign
    # each small crossing to one tile; notch its diagonal neighbour. This keeps
    # each tile's two layers nested instead of creating an unsupported corner.
    for layer in [0,1]:
        for i,a in enumerate(p["tiles"]):
            for b in p["tiles"][i+1:]:
                aa,bb=a["layers"][layer],b["layers"][layer]
                overlap=[max(aa[0],bb[0]),max(aa[1],bb[1]),min(aa[2],bb[2]),min(aa[3],bb[3])]
                if overlap[2]-overlap[0]>1e-7 and overlap[3]-overlap[1]>1e-7:
                    b["notches"][layer].append([overlap[0]-clearance/2,overlap[1]-clearance/2,
                                                overlap[2]+clearance/2,overlap[3]+clearance/2])
    anchors=set()
    def select_anchors(rails, coordinate):
        rails=sorted(rails,key=lambda r:r[coordinate])
        if not rails:
            return
        chosen=[rails[0],rails[-1]]
        span=rails[-1][coordinate]-rails[0][coordinate]
        if p["seam_middle_screw"] and len(rails)>2 and span>=p["seam_middle_min_span"]:
            midpoint=(rails[0][coordinate]+rails[-1][coordinate])/2
            chosen.append(min(rails,key=lambda r:abs(r[coordinate]-midpoint)))
        anchors.update((r["x"],r["axis_y"]) for r in chosen)
    # Top/bottom anchors for each actual tile-to-tile edge, with a middle screw
    # on long edges. Horizontal seams use the equivalent left/right positions.
    for x in xs[1:-1]:
        for lo,hi in zip(ys,ys[1:]):
            select_anchors([r for r in p["rail_positions"] if abs(r["x"]-x)<1e-6
                            and lo-1e-6<=r["axis_y"]<=hi+1e-6],"axis_y")
    for y in ys[1:-1]:
        for lo,hi in zip(xs,xs[1:]):
            select_anchors([r for r in p["rail_positions"] if abs(r["axis_y"]-y)<1e-6
                            and lo-1e-6<=r["x"]<=hi+1e-6],"x")
    for index, rail in enumerate(p["rail_positions"]):
        seam = any(abs(rail["x"]-x)<1e-6 for x in xs[1:-1]) or any(abs(rail["axis_y"]-y)<1e-6 for y in ys[1:-1])
        interval = p["additional_screw_every"]
        rail["seam_anchor"] = (rail["x"],rail["axis_y"]) in anchors
        rail["connection"] = "screw" if rail["seam_anchor"] or (interval and index%interval == 0) else "snap"
        rail["seam"] = seam
        rail["file"] = rail["connection"]+"_"+rail["kind"]
    p["rail_kinds"] = [r["file"] for r in p["rail_positions"]]
    # Two rows of full-depth rails fit above the cutter. Use exact bed checks.
    gap = p["rail_layout_gap"]
    length = p["rail_length"]+2*p["plate_thickness"]
    cols = int((p["bed_width"]-p["bed_exclusion"][0]-2*p["bed_margin"]+gap)//(p["rail_width"]+gap))
    rows = int((p["bed_height"]-2*p["bed_margin"]+gap)//(length+gap))
    p["rails_per_line"], p["rails_per_plate"] = cols, cols*rows
    p["rail_plate_count"] = math.ceil(len(p["rail_kinds"])/p["rails_per_plate"])
    screws = sum(r["connection"]=="screw" for r in p["rail_positions"])
    p["bom"] = {kind:p["rail_kinds"].count(kind) for kind in sorted(set(p["rail_kinds"]))}
    p["bom"].update(front_tiles=len(p["tiles"]),back_tiles=len(p["tiles"]),
                    M3_countersunk_screw_16_mm=2*screws,M3_nut=2*screws)
    return p


def views(p):
    names = ["assembled","front","back"]
    names += [f"{side}_tile_{t['number']:02d}" for side in ["front","back"] for t in p["tiles"]]
    names += sorted(set(p["rail_kinds"]))
    names += [f"rails_plate_{i+1:02d}" for i in range(p["rail_plate_count"])]
    return {n:n for n in names}


def write_outputs(folder, thing, kwargs, save_type, overwrite):
    import csv
    import json
    from pathlib import Path
    import oobb
    import working_scad as drawing
    p = parameters(kwargs)
    files = views(p)
    thing['ai_files'] = {'3dpr':thing['ai_design']}
    for filename,view in files.items():
        sub = oobb.get_default_thing(type='tiled_view')
        drawing.get_ai_version_5(sub,**dict(kwargs,connector_view=view))
        oobb.opsc_make_object(f'{folder}/{filename}.scad',sub['components'],mode='3dpr',save_type=save_type,overwrite=overwrite)
        thing['ai_files'][filename] = sub['ai_design']
    placements=[]
    for side in ["front","back"]:
        for tile in p["tiles"]:
            placements.append({
                "file":f"{side}_tile_{tile['number']:02d}.stl",
                "centre_x_from_bed_left_mm":tile["bed_center"][0]+p["bed_width"]/2,
                "centre_y_from_bed_front_mm":tile["bed_center"][1]+p["bed_height"]/2,
                "maximum_width_including_ears_mm":tile["footprint"][0],
                "maximum_height_including_ears_mm":tile["footprint"][1],
                "rotate_z_degrees":0,
            })
    for index in range(p["rail_plate_count"]):
        count=min(p["rails_per_plate"],len(p["rail_kinds"])-index*p["rails_per_plate"])
        cols=min(p["rails_per_line"],count)
        rows=math.ceil(count/cols)
        gap=p["rail_layout_gap"]
        width=cols*(p["rail_width"]+gap)-gap
        height=rows*(p["rail_length"]+2*p["plate_thickness"]+gap)-gap
        centre=bed_pose(width,height,p)
        placements.append({
            "file":f"rails_plate_{index+1:02d}.stl",
            "centre_x_from_bed_left_mm":centre[0]+p["bed_width"]/2,
            "centre_y_from_bed_front_mm":centre[1]+p["bed_height"]/2,
            "maximum_width_including_ears_mm":width,
            "maximum_height_including_ears_mm":height,
            "rotate_z_degrees":0,
        })
    with Path(folder,"bed_layout.csv").open("w",newline="",encoding="utf-8") as output:
        writer=csv.DictWriter(output,fieldnames=list(placements[0]))
        writer.writeheader()
        writer.writerows(placements)
    Path(folder,'assembly.json').write_text(json.dumps({
        'finished_size_mm':[p['width_total'],p['height_total'],p['assembled_depth']],
        'tray_grid':[p['column'],p['row']], 'bom':p['bom'], 'tiles':p['tiles'],
        'rails':p['rail_positions'],'views':files,'bed_size_mm':[256,256],
        'print_placements':placements,
        'bed_exclusion_mm':[0,0,*p['bed_exclusion']], 'bed_margin_mm':p['bed_margin'],
        'bed_coordinates':'SCAD origin is bed centre; supplied print offsets are intentional',
        'half_lap_thickness_mm':p['plate_thickness']/2,
        'seam_clearance_mm':p['tile_seam_clearance'],
        'front_lip':p['front_lip'],'rear_lip':p['rear_lip'],
        'snap_tip_height_mm':p['rail_height']-p['snap_tip_floor'],
        'snap_outer_hole_height_mm':p['rail_height']-p['snap_tip_floor']+2*p['snap_clearance'],
        'snap_retaining_land_mm':p['snap_ledge_land'],
        'main_connector_sample':p['main_connector_sample'],
        'separate_key_sample':p['separate_key_sample'],
        'snap_arm_thickness_mm':p['snap_profile']['twin_arm_thickness'],
        'snap_side_clearance_mm':p['snap_clearance'],
        'snap_axial_clearance_mm':p['snap_profile']['catch_end_clearance'],
        'seam_middle_screw':p['seam_middle_screw'],
        'physical_fit':'Revised bevelled tabs/receivers require a PETG fit print',
    },indent=2),encoding='utf-8')
    Path(folder,'printing.txt').write_text(
        'V5 TILED PETG DEMO - dimensions in mm. Finished size excludes removable ears.\n'
        'Print ONE of EACH front_tile_*.stl and back_tile_*.stl, and ONE of EACH rails_plate_*.stl.\n'
        '3dpr.stl is a complete kit overview on Z=0, too large for one bed.\n'
        'front.stl, back.stl and assembled.stl are assembled REFERENCES; do not print them whole.\n'
        'Individual screw_rail / snap_rail and bottom variants are spare parts, not extra kit quantities.\n'
        'Tiles alternate outside/inside face down; each STL already has its wider lap face on the bed.\n'
        'Rear has NO forward catch lip. Rails lie on their long face.\n'
        'Keep generated XY orientation. Bed origin in CAD is the P1P bed CENTRE.\n'
        'Files are intentionally offset toward the right/top to clear the 18 x 28 mm cutter corner\n'
        'with 2 mm margin. Disable automatic centering/rotation or verify placement against the mask.\n'
        'bed_layout.csv gives object-centre X/Y from the bed left/front if the slicer recentres imports.\n'
        'Do not add a brim outside the supplied 12 mm ears without rechecking the bed exclusion.\n'
        'Remove the ears at their 0.2 mm necks before assembling the tile laps.\n'
        'Each tile has all 3.75 mm laps on the SAME face; adjacent tiles use the opposite face.\n'
        'Four-way crossing notches prevent diagonal laps from colliding.\n'
        'Seam ends and long-edge middles use screws; remaining joins use snaps. Load M3 nuts sideways first.\n'
        'Screw rails have flat bearing seats; tile laps and snap mounts provide alignment.\n'
        'Use M3 x 16 countersunk screws from the outside; check head seating before tightening PETG.\n'
        'Snap undersides and receiver floors have matching 45-degree bevels, retaining the vertical plate web.\n'
        f'Main snap: sample {p["main_connector_sample"]}, {p["snap_profile"]["twin_arm_thickness"]} mm arms, '
        f'{p["snap_clearance"]} mm side clearance, {p["snap_profile"]["catch_end_clearance"]} mm axial clearance.\n'
        'Tab tips are 4 mm high; outside openings 4.5 mm high. Height increases toward the rail root.\n'
        'The front catch still projects 6 mm into the opening; its inner face now ends flush with the plate.\n'
        'Build the front tile grid loosely, fit rails, then progressively fit rear tiles and tighten.\n'
        'The lap footprints are nested in the supplied poses: no raised lap cantilevers remain.\n'
        'Snap pockets retain a 0.5 mm catch land with the rest of the roof at 45 degrees.\n'
        'Inspect these small ledges and screw/nut bridges in the slicer.\n'
        'Keep supports OUT of tab spring slots. The connector force/retention is not load-tested.\n'
        'Trial a seam and snap rail before committing to the full cabinet. See AI_VERSION_5_TILED.md.\n',encoding='utf-8')
