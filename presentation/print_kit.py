"""Pack the actual printed BOM into independently editable Bambu Studio objects."""

from collections import Counter
from copy import deepcopy
from hashlib import sha256
from io import BytesIO
from math import ceil, sqrt
from pathlib import Path
from tempfile import TemporaryDirectory
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile
import json
import os
import shutil
import subprocess

import trimesh
from PIL import Image, ImageDraw
from .p1s_print_kit import CORE, add_printable_copy, validate_kit_archive

STARTER = Path(__file__).resolve().parents[1] / "source_file/default.3mf"
STARTER_SHA = "2dbe41cec9ed16e34dbe2c74a136f2b2d7bc7ec4a4ba0353d2cfd04c581c8d9e"
COLOURS = {1: "Black", 2: "Teal", 3: "Yellow"}
GAP = 3
MARGIN = 4


def inventory(folder, record):
    data = json.loads((folder / "assembly.json").read_text())
    kind = record["part_role"]
    if kind == "accessory":
        return {folder / (name + ".stl"): (1, 3) for name in data["parts"]}
    grouped = kind in ("array", "cabinet")
    host = folder.parent / data["frame"] if grouped else folder
    frame = json.loads((host / "assembly.json").read_text()) if grouped else data
    count = data["quantities"]["array_unit"] if grouped else 1
    bom = Counter(front=count, back=count)
    for batch in frame["print_batches"].values():
        bom[batch["component"]] += count * batch["count"]
    if grouped:
        # A joining plate takes the place of one adapter at each beam screw.
        contacts = {"edge_across": 2, "edge_upright": 2, "tee4": 4, "plywood_joint": 1, "plywood_double": 2}
        for name, axes in contacts.items():
            bom["screw_adapter"] -= axes * data["quantities"].get(name, 0)
    if bom["screw_adapter"] < 0:
        raise ValueError("More bracket contacts than available screw adapters")
    slots = {
        "front": 2,
        "back": 2,
        "screw_beam": 2,
        "snap_beam": 1,
        "front_plug_square": 1,
        "front_plug": 1,
        "screw_adapter": 3,
    }
    pieces = {host / (name + ".stl"): (qty, slots[name]) for name, qty in bom.items() if qty}
    if grouped:
        for name in contacts:
            if data["quantities"].get(name):
                pieces[folder / (name + ".stl")] = (data["quantities"][name], 3)
    return pieces


def core(tag):
    return "{" + CORE + "}" + tag


def geometry(mesh):
    node = ET.Element(core("mesh"))
    vertices = ET.SubElement(node, core("vertices"))
    triangles = ET.SubElement(node, core("triangles"))
    for x, y, z in mesh.vertices:
        ET.SubElement(vertices, core("vertex"), x=f"{x:.6f}", y=f"{y:.6f}", z=f"{z:.6f}")
    for a, b, c in mesh.faces:
        ET.SubElement(triangles, core("triangle"), v1=str(a), v2=str(b), v3=str(c))
    return node


def place(width, height, boxes):
    xs = sorted({MARGIN, *(b[2] + GAP for b in boxes)})
    ys = sorted({MARGIN, *(b[3] + GAP for b in boxes)})
    for x in xs:
        for y in ys:
            right, top = x + width, y + height
            if max(right, top) > 256 - MARGIN:
                continue
            if all(
                right + GAP <= a + 0.00001
                or x >= c + GAP - 0.00001
                or top + GAP <= b + 0.00001
                or y >= d + GAP - 0.00001
                for a, b, c, d in boxes
            ):
                return (x, y, right, top)
    return None


def layout(bom, meshes):
    plates = []
    for file in sorted(bom, key=lambda p: (-meshes[p].extents[:2].prod(), p.name)):
        qty, slot = bom[file]
        for i in range(qty):
            for plate in plates:
                if plate["slot"] == slot:
                    box = place(*meshes[file].extents[:2], plate["boxes"])
                    if box:
                        break
            else:
                plate = dict(slot=slot, boxes=[(0, 0, 18, 28)], items=[])
                plates.append(plate)
                box = place(*meshes[file].extents[:2], plate["boxes"])
                if box is None:
                    raise ValueError(f"{file.name} exceeds the usable P1S bed")
            plate["boxes"].append(box)
            plate["items"].append((file, i + 1, box))
    return plates


def write_entry(archive, name, payload):
    # Streaming entries use the fixed DOS epoch, so rebuilding adds no timestamp churn.
    with archive.open(name, "w") as entry:
        entry.write(payload.encode("utf-8") if isinstance(payload, str) else payload)


def generate(folder, record):
    ET.register_namespace("", CORE)
    bom = inventory(folder, record)
    meshes = {}
    for file in bom:
        mesh = trimesh.load_mesh(file)
        # OpenSCAD can emit zero-area facets along coincident relief edges.
        mesh.update_faces(mesh.nondegenerate_faces(height=1e-8))
        mesh.remove_unreferenced_vertices()
        if not mesh.is_volume or len(mesh.split()) != 1:
            raise ValueError(f"Expected one closed production piece in {file}")
        mesh.apply_translation(-mesh.bounds[0])
        meshes[file] = mesh
    plates = layout(bom, meshes)
    if sha256(STARTER.read_bytes()).hexdigest() != STARTER_SHA:
        raise ValueError("Unexpected P1S template")
    with ZipFile(STARTER) as base:
        settings = base.read("Metadata/project_settings.config")
        colours = json.loads(settings)["filament_colour"]
        plate_template = ET.fromstring(base.read("Metadata/model_settings.config")).find("plate")
        headers = {
            n: base.read(n) for n in ("[Content_Types].xml", "_rels/.rels", "Metadata/slice_info.config")
        }
    model = ET.Element(core("model"), unit="millimeter", attrib={"xml:lang": "en-US"})
    for k, v in {
        "Application": "BambuStudio-02.09.02.62",
        "BambuStudio:3mfVersion": "1",
        "Title": record["product_name"],
    }.items():
        ET.SubElement(model, core("metadata"), name=k).text = v
    resources = ET.SubElement(model, core("resources"))
    build = ET.SubElement(model, core("build"))
    config = ET.Element("config")
    geom = {f: geometry(m) for f, m in meshes.items()}
    rows = []
    serial = 0
    columns = ceil(sqrt(len(plates)))
    with TemporaryDirectory(dir=folder) as tmp:
        archive = Path(tmp) / "working.3mf"
        with ZipFile(archive, "w", ZIP_DEFLATED, compresslevel=5) as out:
            for name, data in headers.items():
                write_entry(out, name, data)
            write_entry(out, "Metadata/project_settings.config", settings)
            for idx, plate in enumerate(plates):
                n = idx + 1
                slot = plate["slot"]
                cfg = deepcopy(plate_template)
                counts = Counter(f.stem for f, _, _ in plate["items"])
                label = COLOURS[slot] + " - " + ", ".join(k.replace("_", " ") for k in counts)
                for m in list(cfg):
                    key = m.get("key")
                    if key in ("top_file", "pick_file", "thumbnail_no_light_file"):
                        cfg.remove(m)
                    elif key in ("plater_id", "plater_name", "thumbnail_file"):
                        m.set(
                            "value",
                            {
                                "plater_id": str(n),
                                "plater_name": label,
                                "thumbnail_file": f"Metadata/plate_{n}.png",
                            }[key],
                        )
                config.append(cfg)
                im = Image.new("RGB", (512, 512), "#eeeee8")
                draw = ImageDraw.Draw(im)
                for file, copy, box in plate["items"]:
                    serial += 1
                    x, y = box[:2]
                    ox = (idx % columns) * 307.2
                    oy = -(idx // columns) * 307.2
                    add_printable_copy(
                        serial=serial,
                        name=f"{file.stem.replace('_',' ')} ({copy} of {bom[file][0]})",
                        mesh=geom[file],
                        resources=resources,
                        build=build,
                        settings=config,
                        plate=cfg,
                        transform=f"1 0 0 0 1 0 0 0 1 {x+ox:.6f} {y+oy:.6f} 0",
                        filament=slot,
                    )
                    mesh = meshes[file]
                    for tri in mesh.triangles[mesh.face_normals[:, 2] > 0.001]:
                        draw.polygon(
                            [(round(2 * (x + v[0])), round(512 - 2 * (y + v[1]))) for v in tri],
                            fill=colours[slot - 1],
                        )
                for suffix, size in [("", 512), ("_small", 128)]:
                    buf = BytesIO()
                    im.resize((size, size), Image.Resampling.LANCZOS).save(buf, format="PNG")
                    write_entry(out, f"Metadata/plate_{n}{suffix}.png", buf.getvalue())
                rows.append(dict(plate=n, colour=COLOURS[slot], filament_slot=slot, pieces=dict(counts)))
            for name, node in [("3D/3dmodel.model", model), ("Metadata/model_settings.config", config)]:
                with out.open(name, "w") as stream:
                    ET.ElementTree(node).write(stream, encoding="utf-8", xml_declaration=True)
            write_entry(
                out,
                "Metadata/filament_sequence.json",
                json.dumps({f"plate_{i+1}": {"sequence": []} for i in range(len(plates))}),
            )
        del model, resources, build
        verified = validate_kit_archive(archive, count=sum(q for q, _ in bom.values()))
        # Compare the serialized production triangles and vertices for every physical copy.
        signatures = {file: sha256(ET.tostring(node)).digest() for file, node in geom.items()}
        serial = 0
        for plate in plates:
            for file, _, _ in plate["items"]:
                serial += 1
                if sha256(ET.tostring(verified[str(2 * serial)])).digest() != signatures[file]:
                    raise ValueError(f"Geometry mismatch for {file.name}, copy {serial}")
        del verified
        with ZipFile(archive) as chk:
            assert chk.read("Metadata/project_settings.config") == settings
            bindings = ET.fromstring(chk.read("Metadata/model_settings.config"))
            if any(
                obj.find("part/metadata[@key='extruder']") is not None for obj in bindings.findall("object")
            ):
                raise ValueError("A child part overrides its editable object filament")
            assignments = {
                o.get("id"): int(o.find("metadata[@key='extruder']").get("value"))
                for o in bindings.findall("object")
            }
            for cfg, row in zip(bindings.findall("plate"), rows, strict=True):
                ids = [m.get("value") for m in cfg.findall("model_instance/metadata[@key='object_id']")]
                assert len(ids) == sum(row["pieces"].values()) and all(
                    assignments[i] == row["filament_slot"] for i in ids
                )
        os.replace(archive, folder / "working.3mf")
    manifest = dict(template_sha256=STARTER_SHA, object_count=serial, plates=rows)
    (folder / "print-plates.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def validate_slice(folder):
    exe = shutil.which("bambu-studio") or str(
        Path(os.environ.get("ProgramFiles", "")) / "Bambu Studio/bambu-studio.exe"
    )
    manifest = json.loads((folder / "print-plates.json").read_text())
    with TemporaryDirectory() as tmp:
        with open(Path(tmp) / "slice.log", "w+", encoding="utf-8") as log:
            proc = subprocess.run(
                [exe, "--slice", "0", "--outputdir", tmp, str((folder / "working.3mf").resolve())],
                stdout=log,
                stderr=subprocess.STDOUT,
            )
            result_file = Path(tmp) / "result.json"
            if proc.returncode or not result_file.is_file():
                log.seek(0)
                raise RuntimeError(
                    f"{folder.name}: Bambu Studio exited {proc.returncode}: "
                    + log.read()[-6000:]
                    + (result_file.read_text() if result_file.exists() else "")
                )
        data = json.loads(result_file.read_text(encoding="utf-8"))
        plates = data["sliced_plates"]
        if data["return_code"] or sorted(p["id"] for p in plates) != list(
            range(1, len(manifest["plates"]) + 1)
        ):
            raise ValueError("Incomplete slice")
        for plate in plates:
            plate_id = plate["id"]
            expected = manifest["plates"][plate_id - 1]
            sliced = Counter(o["name"].rsplit(" (", 1)[0].replace(" ", "_") for o in plate["objects"])
            slots = {f["id"] for f in plate["filaments"] if f["main_used_g"] > 0}
            if sliced != expected["pieces"] or slots != {expected["filament_slot"]}:
                raise ValueError(f"Plate {plate_id} sliced with unexpected pieces or filament: {sliced}, {slots}")
            if not (Path(tmp) / f"plate_{plate_id}.gcode").stat().st_size:
                raise ValueError(f"Empty G-code on plate {plate_id}")
        report = dict(
            project_sha256=sha256((folder / "working.3mf").read_bytes()).hexdigest(),
            sliced_plates=len(plates),
            sliced_objects=sum(len(p["objects"]) for p in plates),
            checked_filament_slots=sorted({row["filament_slot"] for row in manifest["plates"]}),
            warnings={str(p["id"]): p["warning_message"] for p in plates if p["warning_message"]},
        )
        (folder / "slice-validation.json").write_text(json.dumps(report, indent=2) + "\n")
