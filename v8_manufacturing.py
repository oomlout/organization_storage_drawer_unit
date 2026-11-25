"""SCAD stage: draw from materialized OOMP records, export, validate and package."""
import json
import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile

import ezdxf
import oobb
import trimesh
import yaml

import working_scad as cad
from v8_joiner_section import render as render_joiner_section, render_cap_section
from working_oomp_populate import record_id, selected_options
from v8_validation import validate_frame, validate_hardware_and_group, validate_joiner_profile, validate_samples


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


def kit(folder, files):
    path=folder/"print_files.zip"
    with ZipFile(path,"w",ZIP_DEFLATED) as z:
        for name in dict.fromkeys(files):
            z.write(folder/name,name)
    with ZipFile(path) as z:
        if z.testzip() or any(z.read(n)!=(folder/n).read_bytes() for n in z.namelist()):
            raise IOError(f"Corrupt manufacturing kit in {folder}")


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
    if p.get("corner_fixing"):
        meta["compatible_joiner_part"]=joiner_id
    write_json(folder/"assembly.json",meta)
    lines=[f"V8 Systempak 209 / {p['variant']} per face / {q['drawer_count']} pots total",
           "Print front.stl and back.stl once each, outside face down. Keep the handed faces in their supplied orientations.",
           "Print each of these batches ONCE, in the supplied orientation:"]
    lines += [f"  {n}.stl  ({b['count']} x {b['component']})" for n,b in p["print_batches"].items()]
    lines += ["Individual component STLs are spares. 3dpr is a quantity overview; assembled is a reference.",
              "Fit M3 nuts through the side openings in the screw beams before closing the frame.",
              "Seat beams on the inside face. Fit the friction caps and screw adapters from outside.",
              f"Use {p['bom']['M3_nut']} M3 nuts and {p['bom']['M3_countersunk_screw_20_mm']} M3 x 20 countersunk screws for the beam mounts.",
              "Use the four corner-relieved caps at the front_plug mounts in assembly.json. Fit square caps at the other snap mounts.",
              "The enclosure supplies the bottom floor. Install identical pots from both faces.",
              "Laser alternative: cut front_laser_2d.dxf twice from measured 6 mm sheet. Keep receiver X positions aligned.",
              "3 mm trial: cut front_3mm_test_2d.dxf once per face and bond the included 3 mm doublers on the inside. Align each receiver.",
              "Laser catches have square edges. Print fit, bond strength, clamping and load capacity require physical testing."]
    if p.get("corner_fixing"):
        lines.append(f"Optional joining hardware and fit samples are in the separate {joiner_id} part.")
    (folder/"printing.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
    if export:
        report=validate_frame(folder,p,counts,cuts)
        write_json(folder/"validation.json",report)
        scene=folder/"assembly_preview.scad"
        scene.write_text("rotate([-90,0,0]) { import(\"assembled.stl\"); }\n")
        openscad(scene,folder/"assembly_preview.png","--render","--viewall","--autocenter",
                 "--imgsize=1000,750","--projection=o","--camera=210,-330,220,0,0,0")
        files=["front.stl","back.stl",*[n+".stl" for n in p["print_batches"]],
               *[n+".dxf" for n,_ in cuts],"printing.txt","assembly.json","assembly_preview.png"]
        kit(folder,files)


def joiner_outputs(folder, accessory, frames, export):
    ref=frames[accessory["reference_frame"]]
    ref_folder=Path("parts")/record_id(ref)
    inputs=dict(ref, draw_joiners=True, corner_fixing=accessory["corner_fixing"],
                assembly_reference_file="../"+ref_folder.name+"/assembled.stl")
    p=cad.frame_parameters(**inputs)
    names=["joiners","joiners_clasp_clearance","joiner_backers","joiner_fit_samples"]
    for n in names:
        draw_view(folder,n,inputs,export)
    for kind in ["screw","nut"]:
        thing=oobb.get_default_thing(type="purchased_hardware")
        cad.draw_hardware(thing,p,kind)
        write_solid(folder,"joiner_"+kind+"_reference",thing,export,mode="true")
    w=p["frame"]["width_total"]
    scenes=[("joiners_in_use",False,False,f"{w*3.2},-{w*5.7},450,0,100,0"),
            ("joiners_detail",True,False,"65,-130,55,0,12,0"),
            ("joiners_backing_detail",True,False,"55,105,45,0,14,0"),
            ("joiners_section",True,True,"17,40,98,0,11,-5")]
    for name,detail,section,camera in scenes:
        thing=oobb.get_default_thing(type="installed_joiner")
        cad.draw_joiners_scene(thing,p,detail,section)
        write_solid(folder,name,thing,False)
        if export and section:
            render_joiner_section(folder, ref_folder, p, folder/(name+".png"))
        elif export:
            openscad(folder/(name+".scad"),folder/(name+".png"),"--render",
                     "--imgsize=1000,750","--projection=o","--camera="+camera)
    write_json(folder/"assembly.json",dict(version=8,part_role="accessory",
        compatible_frames=accessory["compatible_frames"],reference_frame=ref_folder.name,
        pieces=p["joiners"],settings=p["corner_fixing"],hardware_per_hole="M3 x 25 countersunk screw and M3 nut"))
    instructions=Path(__file__).with_name("joiner_printing.txt").read_text(encoding="utf-8")
    (folder/"printing.txt").write_text(instructions,encoding="utf-8")
    if export:
        report={}
        for key in accessory["compatible_frames"]:
            host=frames[key]
            params=cad.frame_parameters(**dict(host, draw_joiners=True, corner_fixing=accessory["corner_fixing"]))
            report[key]=validate_hardware_and_group(folder,Path("parts")/record_id(host),params)
        render_cap_section(folder, ref_folder, p, folder/"joiners_clip_clearance.png")
        report["bracket_profiles"]=validate_joiner_profile(folder,ref_folder,p)
        report["sample_difference_mm3"]=validate_samples(folder,ref_folder,p)
        write_json(folder/"validation.json",report)
        kit(folder,[n+ext for n in names for ext in [".scad",".stl"]]+[n+".png" for n,*_ in scenes]+["joiners_clip_clearance.png","assembly.json","printing.txt"])


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
            else:
                joiner_outputs(stage,record,records,generate_stl)
            for file in sorted(stage.iterdir(),key=lambda f:f.name=="print_files.zip"):
                os.replace(file,folder/file.name)
        nav=Path("navigation_oobb").joinpath(*(opt[f"taxonomy_{i}"] for i in range(1,9) if f"taxonomy_{i}" in opt))
        nav.mkdir(parents=True,exist_ok=True)
        shutil.copytree(folder,nav,dirs_exist_ok=True)
        if record["part_role"] == "accessory":
            frame_folder = Path("parts") / record_id(records[record["reference_frame"]])
            canonical = "../" + frame_folder.name + "/assembled.stl"
            relative = Path(os.path.relpath(frame_folder/"assembled.stl", nav)).as_posix()
            for name in ("joiners_in_use", "joiners_detail", "joiners_backing_detail", "joiners_section"):
                scene = nav / (name+".scad")
                scene.write_text(scene.read_text().replace(canonical, relative))
        print(f"Built {folder}",flush=True)
