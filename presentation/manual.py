"""Produce the print booklet and the OOBB page viewer from the same PDF pages."""

import base64
import io
import json
from pathlib import Path
from xml.sax.saxutils import escape

import fitz
import numpy as np
from PIL import Image, ImageDraw
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
import trimesh

from .catalogue import NOTICE, REPO, hardware_url, title

W, H = landscape(A4)
INK = HexColor("#182b31")
TEAL = HexColor("#08777a")


def icon(path, role):
    mesh = trimesh.load_mesh(path)
    if role in ("joiners", "joiner_backers"):
        mesh = min(mesh.split(), key=lambda m: m.centroid[0])
    if role in ("snap_beam", "screw_beam"):
        mesh.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [0, 0, 1]))
    cam = np.array([-0.65, -1, 1.6])
    cam /= np.linalg.norm(cam)
    right = np.cross([0, 0, 1], cam)
    right /= np.linalg.norm(right)
    projected = mesh.vertices @ np.stack([right, -np.cross(cam, right), cam]).T
    xy = projected[:, :2]
    xy = (xy - (xy.max(0) + xy.min(0)) / 2) * min(
        215 / max(np.ptp(xy[:, 0]), 0.01), 90 / max(np.ptp(xy[:, 1]), 0.01)
    ) + [120, 52]
    visible = np.flatnonzero(mesh.face_normals @ cam > 0)
    order = visible[np.argsort(projected[mesh.faces[visible], 2].mean(axis=1))]
    image = Image.new("RGB", (240, 104), "white")
    draw = ImageDraw.Draw(image)
    color = (20, 154, 158) if role in ("front", "back", "joiners") else (62, 72, 76)
    if role in ("screw", "nut"):
        color = (153, 160, 168)
    shades = np.clip(0.6 + 0.4 * mesh.face_normals @ np.array([-0.3, -0.6, 0.73]), 0.4, 1)
    for f in order:
        draw.polygon(
            [tuple(point) for point in xy[mesh.faces[f]]], fill=tuple(int(v * shades[f]) for v in color)
        )
    return image


def make(folder, record, meta, steps, items, mesh_paths):
    name = title(record)
    frame = record["part_role"] == "frame"
    subtitle = (
        f'{record["tray_name"]} · {record["drawer_capacity_ml"]} ml · {record["drawer_count"]} pots'
        if frame
        else "M3 × 25 countersunk · four-way junction"
    )
    pdf = folder / "assembly.pdf"
    c = Canvas(str(pdf), pagesize=(W, H), invariant=True)
    c.setTitle(name + " | Assembly")
    c.setAuthor("oomlout")

    def text(x, y, string, sz=12, font="Helvetica", color=INK):
        c.setFillColor(color)
        c.setFont(font, sz)
        c.drawString(x, y, string)

    def paragraph(x, top, width, string, sz=12):
        p = Paragraph(
            escape(string),
            ParagraphStyle("body", fontName="Helvetica", fontSize=sz, leading=sz * 1.38, textColor=INK),
        )
        _, height = p.wrap(width, H)
        p.drawOn(c, x, top - height)
        return top - height

    def picture(path, x, y, w, h):
        c.drawImage(str(path), x, y, w, h, preserveAspectRatio=True, anchor="c", mask="auto")

    def header(word):
        text(20 * mm, H - 24 * mm, name, 15)
        text(20 * mm, H - 43 * mm, word, 26, "Helvetica-Bold")

    def border(x, y, w, h):
        c.setStrokeColor(HexColor("#b4bfc0"))
        c.setLineWidth(0.5)
        c.rect(x, y, w, h)

    icons = {key: ImageReader(icon(mesh_paths[key], key)) for _, _, key, _ in items}
    by_key = {key: (label, n, hardware) for label, n, key, hardware in items}

    def thumb(key, x, y, w, h):
        c.drawImage(icons[key], x, y, w, h, preserveAspectRatio=True, anchor="c", mask="auto")

    # Cover, details, assembly, finished view, signature padding, inventory, back.
    text(18 * mm, H - 24 * mm, name, 29, "Helvetica-Bold")
    text(18 * mm, H - 35 * mm, subtitle, 13, color=TEAL)
    text(18 * mm, H - 45 * mm, REPO, 9)
    c.linkURL(REPO, (18 * mm, H - 47 * mm, 165 * mm, H - 40 * mm))
    picture(folder / "presentation.jpg", 13 * mm, 13 * mm, W - 26 * mm, H - 62 * mm)
    c.showPage()
    header("Before assembly")
    lead = (
        "Print one of each handed face and one of each batch in printing.txt. The enclosure supplies the bottom floor. "
        "Use the mount positions in assembly.json to identify screw receivers and the four relieved caps."
        if frame
        else "Print a front and a backer for each junction. Choose the standard or loose-clearance front. Seat caps or adapters before installing the outside joiner."
    )
    paragraph(20 * mm, H - 54 * mm, W - 40 * mm, lead)
    y = H - 82 * mm
    for i, (heading, body, _) in enumerate(steps, 1):
        text(20 * mm, y, f"{i}. {heading}", 14, "Helvetica-Bold")
        y = paragraph(28 * mm, y - 5 * mm, W - 53 * mm, body, 11) - 10 * mm
    c.showPage()
    pw, ph = 140.5 * mm, 97 * mm
    for i, (_, _, parts) in enumerate(steps):
        x = (6 + (i % 2) * 144.5) * mm
        y = (H - 6 * mm - ph) - (i // 2) * 101 * mm
        border(x, y, pw, ph)
        text(x + 4 * mm, y + ph - 11 * mm, str(i + 1), 23, "Courier-Bold")
        picture(folder / f"assembly-step-{i+1}.jpg", x + 2 * mm, y + 3 * mm, pw - 40 * mm, ph - 16 * mm)
        iy = y + ph - 14 * mm
        for key in parts:
            if key not in by_key:
                continue
            label, n, hardware = by_key[key]
            thumb(key, x + pw - 37 * mm, iy, 21 * mm, 10 * mm)
            if n > 1:
                text(x + pw - 15 * mm, iy + 1 * mm, f"x{n}", 7)
            paragraph(x + pw - 37 * mm, iy - 1 * mm, 34 * mm, label, 7)
            if hardware:
                c.linkURL(
                    hardware_url(hardware), (x + pw - 37 * mm, iy - 9 * mm, x + pw - 1 * mm, iy + 8 * mm)
                )
            iy -= 21 * mm
    c.showPage()
    border(6 * mm, 6 * mm, W - 12 * mm, H - 12 * mm)
    text(12 * mm, H - 20 * mm, "5", 25, "Courier-Bold")
    picture(folder / "presentation.jpg", 18 * mm, 19 * mm, W - 36 * mm, H - 44 * mm)
    text(
        15 * mm,
        12 * mm,
        "Completed frame with illustrative pots" if frame else "Completed four-way junction",
        11,
    )
    c.showPage()
    for _ in range(2):
        c.showPage()
    header("Parts inventory")
    for i, (label, n, key, hardware) in enumerate(items):
        col, row = i % 3, i // 3
        x = (18 + col * 89) * mm
        y = (121 - row * 39) * mm
        border(x, y, 84 * mm, 35 * mm)
        thumb(key, x + 4 * mm, y + 10 * mm, 47 * mm, 21 * mm)
        text(x + 57 * mm, y + 16 * mm, f"x{n}", 13, "Courier-Bold")
        text(x + 4 * mm, y + 5 * mm, label, 10)
        if hardware:
            c.linkURL(hardware_url(hardware), (x, y, x + 84 * mm, y + 35 * mm))
    text(
        18 * mm,
        14 * mm,
        (
            "Also supply the removable pots and enclosure."
            if frame
            else "One edge strip uses two screws and two nuts."
        ),
        11,
    )
    c.showPage()
    header("Design files")
    paragraph(20 * mm, H - 58 * mm, W - 50 * mm, NOTICE)
    paragraph(
        20 * mm,
        H - 81 * mm,
        W - 50 * mm,
        "Build from the source or open the part folder for its CAD, print kit, fit checks and printable trials.",
    )
    text(20 * mm, H - 112 * mm, REPO, 13, color=TEAL)
    c.linkURL(REPO, (20 * mm, H - 115 * mm, W - 20 * mm, H - 103 * mm))
    c.showPage()
    c.save()

    labels = [
        "Cover",
        "Before assembly",
        "Steps 1–4",
        "Completed assembly",
        "Booklet spacer",
        "Booklet spacer",
        "Parts inventory",
        "Design files",
    ]
    slides = []
    images = {}
    with fitz.open(pdf) as doc:
        for i, page in enumerate(doc):
            pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
            page_id = f"page-{i+1}"
            image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            buf = io.BytesIO()
            image.save(buf, "JPEG", quality=89, optimize=True)
            images[page_id] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
            links = []
            for link in page.get_links():
                if "uri" in link:
                    rect = link["from"]
                    links.append(
                        dict(
                            url=link["uri"], rect=[rect.x0 / W, rect.y0 / H, rect.width / W, rect.height / H]
                        )
                    )
            slides.append(
                dict(
                    id=page_id,
                    image=page_id,
                    number=i + 1,
                    label=labels[i],
                    links=links,
                    kind="summary" if i == 3 else "page",
                    steps=[1, 2, 3, 4] if i == 2 else [],
                )
            )
    data = dict(
        slides=slides,
        images=images,
        start="page-3",
        step_count=4,
        layout="a4-landscape-four-step",
        paper_mm=[297, 210],
    )
    html = Path(__file__).with_name("viewer.html").read_text(encoding="utf-8")
    (folder / "assembly.html").write_text(
        html.replace("__TITLE__", name)
        .replace("__PROJECT_URL__", REPO)
        .replace("__DATA__", json.dumps(data)),
        encoding="utf-8",
    )
