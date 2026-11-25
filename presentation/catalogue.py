"""Generate the public catalogue and assembly instructions from the populated parts."""

import json
from urllib.parse import urlencode

from working_oomp_populate import VERSIONS, get_current_options, record_id

REPO = "https://github.com/oomlout/organization_storage_drawer_unit"
RAW = "https://raw.githubusercontent.com/oomlout/organization_storage_drawer_unit/main"


def hardware_url(part):
    repository = (
        "oomp_hardware_screw_version_5"
        if part.startswith("hardware_screw_")
        else "oomlout_oomp_version_1_messy"
    )
    return f"https://github.com/oomlout/{repository}/tree/main/parts/{part}"


# Switch to the hosted viewer only once the repository has a Pages deployment.
PAGES = ""
NOTICE = "This project was largely AI-generated. Editable CAD sources and print kits are included. AI-generated CAD images and instructions. Errors possible. Check fit on your printer before making a full set."
NUT = "hardware_nut_m3"


def title(record):
    if record["part_role"] == "accessory":
        return record["product_name"]
    return f'{record["column"]} × {record["row"]} drawer unit'


def tray_name(record):
    return f'{record["tray_name"]} · {record["drawer_capacity_ml"]} ml'


def inventory(record, meta):
    """Tuples of display name, quantity, mesh stem and optional OOMP hardware ID."""
    is_frame = record["part_role"] == "frame"
    length = 20 if is_frame else 25
    if is_frame:
        bom = meta["bom"]
        items = [
            ("Front face", 1, "front", None),
            ("Rear face", 1, "back", None),
            ("Snap beam", bom["snap_beam"], "snap_beam", None),
            ("Screw beam", bom["screw_beam"], "screw_beam", None),
            ("Relieved cap", meta["cap_quantities"]["front_plug"], "front_plug", None),
            ("Square cap", meta["cap_quantities"]["front_plug_square"], "front_plug_square", None),
            ("Screw adapter", bom["screw_adapter"], "screw_adapter", None),
        ]
        count = bom["M3_nut"]
    else:
        items = [("Four-hole front", 1, "joiners", None), ("Matching backer", 1, "joiner_backers", None)]
        count = 4
    items += [
        (
            f"M3 × {length} countersunk screw",
            count,
            "screw",
            f"hardware_screw_countersunk_hex_head_black_m3_diameter_{length}_mm_length",
        ),
        ("M3 hex nut", count, "nut", NUT),
    ]
    return [i for i in items if i[1]]


def guide(record, meta):
    if record["part_role"] == "accessory":
        return [
            (
                "Load the backer",
                "Press an M3 nut into each rear pocket. The four-way plate uses four nuts. Use two for an edge strip.",
                ["joiner_backers", "nut"],
            ),
            (
                "Align the faceplates",
                "Bring the frame edges together while the inside is accessible. Hold the nuts in place and offer the backer 8 mm above its seat, then slide it down into the rail relief.",
                [],
            ),
            (
                "Fit the front",
                "Seat the clip caps or screw adapters first. Match the pockets in the joiner front to those fittings and press its lands against the faceplates.",
                ["joiners"],
            ),
            (
                "Tighten the joint",
                "Start each M3 × 25 countersunk screw from outside. Tighten evenly by hand and check that the drawers and clasps move freely.",
                ["screw"],
            ),
        ]
    snaps = meta["bom"]["snap_beam"]
    beams = f"the {snaps} snap beams and the loaded screw beams" if snaps else "the four loaded screw beams"
    caps = "Press the square caps over the snap ends. " if snaps else ""
    return [
        (
            "Load the screw beams",
            f'Slide an M3 nut into the side pocket at each end of all {meta["bom"]["screw_beam"]} screw beams. The close-up shows one end. Align each nut with its axial bore.',
            ["screw_beam", "nut"],
        ),
        (
            "Seat the beams in the front",
            f'Place the front face outside-down. Seat {beams} from the inside. Use the mount map in assembly.json. The runner stops point up in service.',
            ["front", "snap_beam"],
        ),
        (
            "Close the rear face",
            "Match the handed rear face to the free beam ends. Press evenly so both ends of every beam enter their receivers. Keep the caps and adapters accessible from outside.",
            ["back"],
        ),
        (
            "Lock both faces",
            f'{caps}Seat the screw adapters and fit one M3 × 20 countersunk screw per adapter ({meta["bom"]["screw_adapter"]} total). Slide a pot into each bank to check travel.',
            ["front_plug", "front_plug_square", "screw_adapter", "screw"],
        ),
    ]


def viewer_link(record, prefix=""):
    key = record_id(record)
    return f"{PAGES}/{key}/" if PAGES else prefix + "assembly.pdf"


def manual_links(record, prefix=""):
    key = record_id(record)
    primary = "Open the assembly viewer" if PAGES else "View the illustrated manual"
    return f"[{primary}]({viewer_link(record,prefix)}) · [Download PDF]({RAW}/parts/{key}/assembly.pdf) · [Download offline HTML]({prefix}assembly.html?raw=true)"


def write_part(folder, record, meta, steps, items):
    frame = record["part_role"] == "frame"
    name = title(record)
    introduction = (
        f'{record["column"]} × {record["row"]} openings on each face. The two banks hold '
        f'{record["drawer_count"]} {record["drawer_capacity_ml"]} ml {record["tray_name"]} pots in total.'
        if frame
        else "Join two V8 frames along an edge, or join four at a corner. The standard and loose-clearance fronts share the same matching extruded backer for each shape."
    )
    lines = [
        f"# {name}",
        "",
        introduction,
        "",
        NOTICE,
        "",
        f"![{'Frame with removable pots' if frame else 'Installed four-way joiner'}](presentation.jpg)",
        "",
        "[Printing instructions](printing.txt) · [Assembly data](assembly.json)",
        "",
        manual_links(record),
        "",
        "## Details",
        "",
    ]
    if frame:
        w, h, d = meta["frame_envelope_mm"]
        lines += [
            f"Face size is {w:g} × {h:g} mm. The outside faces are {d:g} mm apart. "
            f'The kit uses a {meta["inside_span_mm"]:g} mm inside rail span. The enclosure supplies the bottom floor.',
            "",
            "Print each handed face and each listed batch once. Individual component files are spares. "
            "For a laser build, cut the 6 mm face pattern twice, or cut one complete 3 mm reinforced trial pattern per face.",
            "",
            "[6 mm laser face](front_laser_2d.dxf) · [3 mm reinforced trial](front_3mm_test_2d.dxf)",
        ]
        lines += ["", "**Print one of each file**", "",
                  "[Front face](front.stl), [rear face](back.stl), " +
                  ", ".join(f"[{name}]({name}.stl)" for name in meta["print_batches"]) + "."]
        if (folder / "stocked-front.jpg").is_file():
            from .sync_packaging import model_folder

            pack = json.loads((model_folder(record["container"]) / "model.json").read_text(encoding="utf-8"))
            fit = json.loads((folder / "pot-fit.json").read_text(encoding="utf-8"))
            lines += [
                "",
                "## Stocked unit",
                "",
                f"The modelled open pot is {pack['height']:g} mm high. The closed package is {pack['closed_height']:g} mm high "
                f"and the frame opening is {fit['opening_height_mm']:g} mm. Both banks are shown with lids removed. "
                f"[Manufacturer photos]({pack['source']}) · [Technical sheet]({pack['technical_sheet']}).",
                "",
                "The fixed frame label identifies the face, column and row. "
                "The larger label on the removable pot identifies its example OOMP contents. Each label has its own QR code.",
                "",
                "![Fully stocked unit with labelled pots](stocked-front.jpg)",
                "",
                "[Rear view](stocked-rear.jpg) · [Label close-up](stocked-detail.jpg) · [Fixed location labels](labels-location.pdf) · "
                "[Replaceable contents labels](labels-contents.pdf) · [Individual label artwork](labels/) · "
                "[Slot assignments](label-map.json) · [Reference model fit](pot-fit.json)",
            ]
        if "compatible_joiner_part" in meta:
            lines += ["", f"[Joining brackets](../{meta['compatible_joiner_part']}/README.md) and [frame-to-plywood joint](../{meta['compatible_joiner_part'].replace('_joiners_v8','_plywood_joint_v8')}/README.md)"]
    else:
        hosts = [o for o in get_current_options() if o["variant"] in record["compatible_frames"]]
        lines += [
            "Fits " + " and ".join(f"[{title(o)}](../{record_id(o)}/README.md)" for o in hosts) + ".",
            "",
            "Choose one outside front style. The standard pockets give 0.8 mm above the fitted cap and 0.6 mm at the sides. The looser option gives 1.1 mm above and 0.9 mm at the sides.",
            "",
            "[Standard fronts](joiners.stl) · [Looser fronts](joiners_clasp_clearance.stl) · [Backers](joiner_backers.stl) · [Seven-piece fit trial](joiner_fit_samples.stl)",
            "",
            "![Section through a fitted cap and the standard joiner](joiners_clip_clearance.png)",
        ]
    lines += [
        "",
        "## Parts",
        "",
        (
            "Quantities for one complete frame."
            if frame
            else "Quantities for one four-way junction. For a two-frame edge use the two-hole front, its matching backer and two screws and nuts."
        ),
        "",
        "| Part | Quantity |",
        "| --- | ---: |",
    ]
    for label, count, mesh, hardware in items:
        target = hardware_url(hardware) if hardware else mesh + ".stl"
        lines.append(f"| [{label}]({target}) | {count} |")
    if frame:
        lines.append(
            f'| {record["tray_name"]} pot, {record["drawer_capacity_ml"]} ml | {record["drawer_count"]} |'
        )
    lines += [
        "",
        "## Assembly",
        "",
        "Print in the supplied orientations. Clear loose filament from the screw bores and nut pockets before fitting hardware.",
        "",
    ]
    for i, (heading, text, _) in enumerate(steps, 1):
        lines += [f"### {i}. {heading}", "", text, "", f"![{heading}](assembly-step-{i}.jpg)", ""]
    lines += [
        "The [validation report](validation.json) records nominal CAD fit. Print tolerances, strength and long-term loading still need a physical trial.",
        "",
    ]
    (folder / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(root, records):
    frames = [r for r in records if r["part_role"] == "frame"]
    if not frames:
        return
    hero = next((r for r in frames if r.get("featured")), frames[0])

    def base(r):
        return f"parts/{record_id(r)}"

    lines = [
        "# Drawer units for takeaway pots",
        "",
        "Use a takeaway pot as the drawer. Two faceplates and a set of rails hold opposing banks of removable pots, so a frame can be opened from either side.",
        "",
        NOTICE,
        "",
        f"[![{title(hero)} with removable pots]({base(hero)}/presentation.jpg)]({base(hero)}/README.md)",
        "",
        f"**Featured build · [{title(hero)}]({base(hero)}/README.md).** "
        f'{hero["column"]*hero["row"]} pots per face, {hero["drawer_count"]} in total. '
        f'The removable {hero["tray_name"]} pots slide in from either side.',
        "",
        f'This build uses two handed faces, {hero["snap_beam_count"]} snap beams and {hero["screw_beam_count"]} screw beams. '
        "For a fastener cabinet, one bank can hold screws and the opposite bank their matching nuts.",
        "",
        manual_links(hero, base(hero) + "/"),
        "",
        "### Assemble the featured build",
        "",
        "| Load the nuts | Seat the beams | Fit the rear face | Lock both faces |",
        "| --- | --- | --- | --- |",
        "| "
        + " | ".join(
            f'[<img src="{base(hero)}/assembly-step-{i}.jpg" width="165" alt="{label}">]({base(hero)}/README.md#assembly)'
            for i, label in enumerate(["Nut pocket", "Front and rails", "Rear face", "Outside fixings"], 1)
        )
        + " |",
        "",
        "## Current version · V8",
        "",
    ]
    if (root / base(hero) / "stocked-front.jpg").is_file():
        before = lines.index("### Assemble the featured build")
        lines[before:before] = [
            f"[![Fully stocked {title(hero)} with fixed grid IDs and removable OOMP contents labels]({base(hero)}/stocked-front.jpg)]({base(hero)}/README.md#stocked-unit)",
            "",
            "Each slot has a permanent XY address. Each pot has a separate contents label. Scan either QR code or read the printed identifier.",
            "",
        ]
    for cabinet in (r for r in records if r["part_role"] == "cabinet"):
        path=base(cabinet)
        lines += [f"[![Nine-unit plywood cabinet]({path}/presentation.jpg)]({path}/README.md)", "", f"[3 × 3 cabinet of 2 × 7 units · cut list, drilling and assembly]({path}/README.md)", ""]
    for family in dict.fromkeys(r["taxonomy_5"] for r in frames):
        group = [r for r in frames if r["taxonomy_5"] == family]
        lines += [
            "### " + tray_name(group[0]),
            "",
            "| Build | Grid per face | Pots | Assembly | Print kit |",
            "| --- | --- | ---: | --- | --- |",
        ]
        for r in group:
            path = base(r)
            lines.append(
                f'| [<img src="{path}/presentation.jpg" width="150" alt="{title(r)}">]({path}/README.md) | [{title(r)}]({path}/README.md) | {r["drawer_count"]} | [Illustrated guide]({viewer_link(r,base(r)+"/")}) | [Print list]({path}/printing.txt) |'
            )
        lines.append("")
    for r in records:
        if r["part_role"] == "accessory":
            lines += [
                f'**[{r["product_name"]}]({base(r)}/README.md)** · [Print and installation instructions]({base(r)}/README.md)',
                "",
            ]
    lines += [
        "## Design versions",
        "",
        f"[Browse the archived source and manufacturing records]({REPO}/tree/main/history).",
        "",
        "| Version | Design notes |",
        "| --- | --- |",
        f"| [V8]({base(hero)}/README.md) | Current frame catalogue and assembly guides |",
    ]
    for ver, description, file in reversed(VERSIONS):
        lines.append(f"| [{ver}]({REPO}/blob/main/history/{file}) | {description} |")
    suggestion = (
        REPO
        + "/issues/new?"
        + urlencode(
            {
                "title": "Tray size suggestion",
                "body": "Tray manufacturer and model:\nCapacity (ml):\nRim width, depth and height (mm):\nBody width below the rim (mm):\nDesired columns and rows per face:\nPhoto or datasheet:",
            }
        )
    )
    lines += [
        "",
        "## Suggest a tray",
        "",
        f"[Suggest a tray size]({suggestion}) with its rim and body measurements and the grid you want. "
        "To build a variant locally, add its tray and layout to the population file and run make-all. "
        f"[Build and authoring guide]({REPO}/blob/main/BUILD.md).",
        "",
    ]
    (root / "README.md").write_text("\n".join(lines), encoding="utf-8")
