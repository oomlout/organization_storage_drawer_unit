"""Generate separate, printable position and OOMP contents stickers. Coordinates are face-relative."""

import json
import hashlib
from pathlib import Path
import shutil

import qrcode
import reportlab
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas

HERE = Path(__file__).resolve().parent
PX = 32  # pixels per millimetre in the downloadable stickers
LOCATION_MM = (8.4, 10.8)
CONTENTS_MM = (47, 13)
FONT = Path(reportlab.__file__).parent / "fonts"


def lettering(draw, xy, text, size, bold=False, width=None):
    face = str(FONT / ("VeraBd.ttf" if bold else "Vera.ttf"))
    font = ImageFont.truetype(face, size)
    while width and draw.textlength(text, font=font) > width and size > 10:
        size -= 1
        font = ImageFont.truetype(face, size)
    draw.text(xy, text, font=font, fill="black", anchor="lt")


def add_qr(image, payload, box, x, y):
    code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=4, box_size=1)
    code.add_data(payload)
    code.make(fit=True)
    qr = code.make_image().convert("RGB")
    factor = box // qr.width
    if factor < 1:
        raise ValueError("Label is too small for the QR payload")
    size = qr.width * factor
    image.paste(
        qr.resize((size, size), Image.Resampling.NEAREST), (x + (box - size) // 2, y + (box - size) // 2)
    )


def sticker(path, payload, location=None, part=None):
    w, h = LOCATION_MM if location else CONTENTS_MM
    image = Image.new("RGB", (round(w * PX), round(h * PX)), "white")
    draw = ImageDraw.Draw(image)
    if location:
        side, x, y = location
        add_qr(image, payload, image.width, 0, 0)
        lettering(draw, (8, image.width + 4), f"{side} {x},{y}", 49, True, image.width - 16)
    else:
        box = image.height - 16
        add_qr(image, payload, box, 8, 8)
        start = box + 23
        width = image.width - start - 15
        draw.rectangle((start, 18, start + width, 81), fill="black")
        draw.text(
            (start + 10, 24),
            "OOMP   /   " + part.get("category", "HARDWARE").upper(),
            font=ImageFont.truetype(str(FONT / "VeraBd.ttf"), 49),
            fill="white",
            anchor="lt",
        )
        lettering(draw, (start, 111), part["title"], 100, True, width)
        lettering(draw, (start, 240), part["detail"], 53, False, width)
        lettering(draw, (start, 323), part["code"], 50, True, width)
    image.save(path, dpi=(PX * 25.4, PX * 25.4))


def print_sheet(file, images, size):
    canvas = Canvas(str(file), pagesize=A4, invariant=True)
    canvas.setTitle(file.stem.replace("-", " ").title())
    w, h = size
    x, y = 12, 280
    for image in images:
        if x + w > 200:
            x = 12
            y -= h + 4
        if y - h < 10:
            canvas.showPage()
            x, y = 12, 280
        canvas.drawImage(str(image), x * mm, (y - h) * mm, w * mm, h * mm)
        canvas.setStrokeGray(0.65)
        canvas.setLineWidth(0.25)
        canvas.rect(x * mm, (y - h) * mm, w * mm, h * mm)
        x += w + 4
    canvas.showPage()
    canvas.save()


def generate(folder, scratch, record):
    examples = json.loads((HERE / "example_contents.json").read_text())
    for e in examples:
        e.update(title=f"M3 × {e['length_mm']} mm", detail="Countersunk · hex socket")
    source = HERE.parent / "label_assignments" / (record["variant"] + ".json")
    config = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else {}
    overrides = config.get("contents", {})
    unit = config.get("unit", record["variant"].upper())
    if not isinstance(unit, str) or not unit.strip():
        raise ValueError("Give the physical unit a non-empty location prefix")
    stickers = scratch / "stickers"
    stickers.mkdir()
    locations = []
    contents = []
    slots = []
    assigned = set()
    k = 0
    for side in ("F", "R"):
        for y in range(1, record["row"] + 1):
            for x in range(1, record["column"] + 1):
                address = f"{side}-X{x}-Y{y}"
                location = f"{unit}-{address}"
                part = overrides.get(address, examples[k % len(examples)])
                if address in overrides:
                    assigned.add(address)
                k += 1
                lp = stickers / ("location-" + address + ".png")
                # The content file belongs to the part and can be reused in any location.
                digest = hashlib.sha256(part["id"].encode()).hexdigest()[:16]
                cp = stickers / ("content-" + digest + ".png")
                sticker(lp, location, location=(side, x, y))
                if not cp.exists():
                    sticker(cp, part["id"], part=part)
                locations.append(lp)
                contents.append(cp)
                slots.append(
                    dict(
                        side=side,
                        x=x,
                        y=y,
                        address=address,
                        location_qr=location,
                        part=part,
                        content_qr=part["id"],
                        location_png=lp.name,
                        content_png=cp.name,
                    )
                )
    if assigned != set(overrides):
        raise ValueError(f"Unknown slot(s) in {source}: {set(overrides)-assigned}")
    manifest = folder / "label-map.json"
    manifest.write_text(
        json.dumps(
            dict(
                unit=unit,
                axes="X left to right and Y top to bottom as viewed from each face",
                location_size_mm=LOCATION_MM,
                contents_size_mm=CONTENTS_MM,
                slots=slots,
            ),
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print_sheet(folder / "labels-location.pdf", locations, LOCATION_MM)
    print_sheet(folder / "labels-contents.pdf", contents, CONTENTS_MM)
    shutil.copytree(stickers, folder / "labels", dirs_exist_ok=True)
    return slots, stickers
