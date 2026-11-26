"""SCAD stage: draw from materialized OOMP records, export, validate and package."""
import json
import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

import ezdxf
import oobb
import trimesh
import yaml

from presentation import catalogue, scenes
import working_scad as cad
from working_oomp_populate import record_id, selected_options
from v8_validation import validate_frame


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def openscad(source, output, *options):
    exe = shutil.which("openscad.com") or shutil.which("openscad")
    if exe is None:
        raise RuntimeError("Install OpenSCAD with the Manifold backend and add it to PATH")
    result = subprocess.run([exe, "--backend=Manifold", "--hardwarnings", *options,
                             "-o", str(output.resolve()), str(source.resolve())],
                            capture_output=True, text=True, timeout=300)
    if result.returncode or not output.is_file() or not output.stat().st_size:
        raise RuntimeError(f"{source.name} -> {output.name} failed\n{result.stderr}")


def write_solid(folder, name, thing, export, mode="3dpr"):
    source = folder / (name + ".scad")
    oobb.opsc_make_object(str(source), thing["components"], mode=mode, save_type="none", overwrite=True)
    if export:
        target = source.with_suffix(".stl")
        openscad(source, target, "--export-format=binstl")
        mesh = trimesh.load_mesh(target)
        if not mesh.is_watertight and (mesh.area_faces == 0).any():
            mesh.update_faces(mesh.area_faces > 0)
            mesh.remove_unreferenced_vertices()
            if mesh.is_volume:
                mesh.export(target)
        if not mesh.is_volume:
            raise ValueError(f"Open or inverted mesh in {target.name}")


def draw_view(folder, name, inputs, export):
    thing = oobb.get_default_thing(type="drawer_unit_v8")
    cad.draw_frame(thing, **dict(inputs, connector_view="print_layout" if name=="3dpr" else name))
    write_solid(folder, name, thing, export)
    return thing["ai_design"]["expected_bodies"]


def laser_drawings(folder, p):
    targets = [("front_laser_2d", "front_laser"), ("receiver_laser", "receiver_6_0")]
    targets += [(n+"_2d", n) for n in [*p["reinforcement_types"], "clip_reinforcements"]]
    targets.append(("front_3mm_test_2d", "front_3mm_test_layout"))
    for name, source in targets:
        cut = "projection(cut=true) translate([0,0,-0.1])" if name=="receiver_laser" else "projection(cut=false)"
        scad = folder / (name+".scad")
        scad.write_text(cut+" { include <"+source+".scad>; }\n")
        dxf = scad.with_suffix(".dxf")
        openscad(scad, dxf)
        doc = ezdxf.readfile(dxf)
        doc.dxfversion="AC1024"
        doc.units=4
        doc.header["$MEASUREMENT"]=1
        doc.layers.new("CUT", dxfattribs={"color":1})
        for entity in doc.modelspace():
            entity.dxf.layer="CUT"
        doc.saveas(dxf)
    return targets


def frame_outputs(folder, inputs, export, joiner_id):
    p=cad.frame_parameters(**inputs)
    q=p["frame"]
    names=["3dpr","assembled","front","back","front_laser","front_plug","front_plug_square",
           "screw_adapter","snap_beam","screw_beam","receiver_6_0","sample_71",
           *p["print_batches"],*p["reinforcement_types"],"clip_reinforcements","front_3mm_test","front_3mm_test_layout"]
    counts={n:draw_view(folder,n,inputs,export) for n in names}
    cuts=laser_drawings(folder,p)
    meta=dict(version=8,variant=p["variant"],part_role="frame",container=p["container"],
              grid_per_face=[p["column"],p["row"]],drawer_sides=2,drawer_count=q["drawer_count"],
              frame_envelope_mm=[q["width_total"],q["height_total"],q["assembled_depth"]],
              printed_face_depth_mm=max(f["envelope"][2] for f in q["floor_support_features"]),
              inside_span_mm=p["rail_length"],bom=p["bom"],print_batches=p["print_batches"],
              cap_quantities=p["cap_quantities"],frame_mounts=p["frame_mounts"],
              laser_reinforcements=p["reinforcement_pads"],stop_profile=p.get("face_stop_profile","plywood_floor_support"))
    if inputs["taxonomy_5"] == "systempak_209_100_ml":
        meta["compatible_joiner_part"]=joiner_id
    write_json(folder/"assembly.json",meta)
    lines=[f"V8 {p['tray_name']} / {p['variant']} per face / {q['drawer_count']} pots total",
           "Print front.stl and back.stl once each, outside face down. Keep the handed faces in their supplied orientations.",
           "Print each of these batches ONCE, in the supplied orientation:"]
    lines += [f"  {n}.stl  ({b['count']} x {b['component']})" for n,b in p["print_batches"].items()]
    lines += ["Individual component STLs are spares. 3dpr is a quantity overview; assembled is a reference.",
              "Fit M3 nuts through the side openings in the screw beams before closing the frame.",
              "Seat beams on the inside face. Fit the friction caps and screw adapters from outside.",
              f"Use {p['bom']['M3_nut']} M3 nuts and {p['bom']['M3_countersunk_screw_20_mm']} M3 x 20 countersunk screws for the beam mounts.",
              "Fit square caps to any snap mounts. The four outer screw beams accept the joining brackets.",
              "The enclosure supplies the bottom floor. Install identical pots from both faces.",
              "Laser alternative: cut front_laser_2d.dxf twice from measured 6 mm sheet. Keep receiver X positions aligned.",
              "3 mm trial: cut front_3mm_test_2d.dxf once per face and bond the included 3 mm doublers on the inside. Align each receiver.",
              "Laser catches have square edges. Print fit, bond strength, clamping and load capacity require physical testing."]
    if inputs["taxonomy_5"] == "systempak_209_100_ml":
        lines.append(f"Use the beam-mounted joining brackets from the separate {joiner_id} part.")
    (folder/"printing.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
    if export:
        report=validate_frame(folder,p,counts,cuts)
        write_json(folder/"validation.json",report)
        scene=folder/"assembly_preview.scad"
        scene.write_text("rotate([-90,0,0]) { import(\"assembled.stl\"); }\n")
        openscad(scene,folder/"assembly_preview.png","--render","--viewall","--autocenter",
                 "--imgsize=1000,750","--projection=o","--camera=210,-330,220,0,0,0")
        scenes.render(folder,p,inputs,meta)


def publish(stage, folder):
    for entry in list(stage.iterdir()):
        dest = folder / entry.name
        if entry.is_dir() and dest.is_dir():
            previous = stage / (entry.name + ".previous")
            os.replace(dest, previous)
            try:
                os.replace(entry, dest)
            except OSError:
                os.replace(previous, dest)
                raise
            shutil.rmtree(previous)
        else:
            os.replace(entry, dest)


def retire_previous_outputs(folder, record):
    """Remove only known generated files superseded by the beam-interface revision."""
    patterns = []
    if record["part_role"] == "frame":
        patterns = ["front_plugs_corner_clearance.*"]
        if record["snap_beam_count"] == 0:
            patterns += ["snap_beams.*", "front_plugs_square.*"]
    if record["variant"] == "joiners":
        patterns = ["joiner_*.scad", "joiner_*.stl", "joiners*.scad", "joiners*.stl",
                    "joiners*.png", "assembly-step-*.jpg", "assembly.html", "assembly.pdf", "presentation.jpg"]
    if record["part_role"] == "cabinet":
        patterns = ["frame_drill.dxf", "host_assembled.*", "host_front.*", "host_back.*",
                    "m3_socket.*", "m3_nut.*", "retainer.*", "*_outline.scad",
                    "edge_across.dxf", "edge_upright.dxf", "edge_upright.scad", "edge_upright.stl", "tee4.dxf"]
    for pattern in patterns:
        for path in folder.glob(pattern):
            if path.is_file():
                path.unlink()


def generate(part=None,generate_stl=True):
    if generate_stl and not __debug__:
        raise RuntimeError("Run without python -O to enable the manufacturing checks")
    options=selected_options(part)
    from working_oomp_populate import get_current_options
    joiner_id=record_id(next(o for o in get_current_options() if o["part_role"]=="accessory"))
    records={}
    for opt in options:
        folder=Path("parts")/record_id(opt)
        record=yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))["oobb_details"]
        if record!=opt:
            raise ValueError(f"Stale OOMP record for {folder.name}")
        records[record["variant"]]=record
        print(f"Building V8 {record['variant']}",flush=True)
        with TemporaryDirectory(prefix=".v8-",dir=folder.parent) as tmp:
            stage=Path(tmp)
            if record["part_role"]=="frame":
                frame_outputs(stage,record,generate_stl,joiner_id)
            elif record["part_role"]=="array":
                from v8_array import build
                build(stage,record,records[record["array"]["host"]],generate_stl)
            elif record["part_role"]=="cabinet":
                from v8_cabinet import build
                build(stage,record,records[record["cabinet"]["host"]],generate_stl)
            else:
                from v8_beam_joints import build
                build(stage,record,records,generate_stl)
            if generate_stl:
                from presentation.print_kit import generate as write_kit, validate_slice
                write_kit(stage, record)
                validate_slice(stage)
            publish(stage, folder)
            retire_previous_outputs(folder,record)
        nav=Path("navigation_oobb").joinpath(*(opt[f"taxonomy_{i}"] for i in range(1,9) if f"taxonomy_{i}" in opt))
        nav.mkdir(parents=True,exist_ok=True)
        retire_previous_outputs(nav,record)
        if record["part_role"] in {"cabinet","array","accessory"}:
            for legacy in ("printing.txt","validation.json","assembly.json"):
                (nav/legacy).unlink(missing_ok=True)
            shutil.copyfile(folder/"working.yaml",nav/"working.yaml")
            rel=Path(os.path.relpath(folder,nav)).as_posix()
            (nav/"README.md").write_text(f"[Part files and assembly guide]({rel}/README.md)\n")
            print(f"Built {folder}",flush=True)
            continue
        shutil.copytree(folder,nav,dirs_exist_ok=True,ignore=shutil.ignore_patterns(
            "working.3mf","print-plates.json","slice-validation.json","README.md","presentation.jpg","assembly-step-*.jpg","assembly.pdf","assembly.html","stocked-*.jpg","labels*.pdf","labels","label-map.json","pot-fit.json"))
        print(f"Built {folder}",flush=True)
    if generate_stl:
        published = [r for r in get_current_options() if (Path("parts")/record_id(r)/"README.md").is_file()]
        catalogue.write_index(Path.cwd(), published)
