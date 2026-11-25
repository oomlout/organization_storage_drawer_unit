"""Export connector coupons through the normal pipeline; check geometry, not strength."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import numpy as np
import trimesh
import yaml
from catalogue_archive import historical_parts
import working
import working_scad as drawing
import scad_help
from shapely.geometry import box
from action_validate_ai_version_4 import section


def overlap(a, b):
    result = trimesh.boolean.intersection([a, b], engine="manifold")
    return 0.0 if result.is_empty else abs(float(result.volume))


def moved(mesh, translation):
    result = mesh.copy()
    result.apply_translation(translation)
    return result


def local_rail(mesh, p):
    tip = -p["key_tongue_depth"] if p["connector_design"] == "snap_key" else p["hook_tip_z"]
    offset = p["test_rail_length"]/2 if p["connector_design"] == "screw_reference" else (p["test_rail_length"]+tip)/2
    result = mesh.copy()
    result.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,offset],[0,0,0,1]])
    return result


def compressed(mesh, p, key=False):
    # Prescribed geometric deflection, NOT a stress/force simulation.
    # Subdivision prevents a long flat edge from bypassing the curved motion.
    vertices, faces = trimesh.remesh.subdivide_to_size(mesh.vertices, mesh.faces, max_edge=0.8)
    vertices = vertices.copy()
    delta = p["insertion_deflection"]+0.05
    if key:
        root = p["key_head_x"]+p.get("key_head_length",2)
        t = np.clip((vertices[:,0]-root)/(p["key_shoulder_x"]-root),0,1)
        vertices[:,2] -= np.sign(vertices[:,2])*delta*t*t*(3-t)/2
    else:
        t = np.clip((p["root_distance"]-vertices[:,2])/(p["root_distance"]-p["hook_shoulder_z"]),0,1)
        active = np.abs(vertices[:,0]) > p["guide_half_width"]+0.05
        if "rigid_outer_half_width" in p:
            # Thin-panel rails have rigid outer bearing strips beside the
            # recessed spring arms. Only the arms and exposed hooks flex.
            active &= (vertices[:,2] < -0.001) | (np.abs(vertices[:,0]) < p["rigid_outer_half_width"]+0.01)
        vertices[active,0] -= np.sign(vertices[active,0])*delta*t[active]**2*(3-t[active])/2
    return trimesh.Trimesh(vertices=vertices,faces=faces,process=True)


def check_previous_versions(root):
    for version in [1,2,3]:
        __import__(f"action_check_version_{version}_lock").main()
    baseline=json.loads((root/"validation_ai_version_5/version_4_baseline.json").read_text(encoding="utf-8"))
    actual={f.parent.name for f in (historical_parts(root)).glob("*ai_version_4_style*/working.yaml")}
    assert actual == set(baseline), "V4 catalogue changed"
    for name, expected in baseline.items():
        folder=historical_parts(root)/name
        assert yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))["oobb_details"] == expected["oobb_details"]
        for filename,digest in expected["scad_sha256"].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest() == digest, (name,filename)
    print("Version 4 inputs and CAD unchanged",flush=True)


def main(skip_generation=False):
    root=Path(__file__).resolve().parent
    assert Path.cwd().resolve() == root
    out=root/"validation_ai_version_5"; out.mkdir(exist_ok=True)
    exe=shutil.which("openscad.com") or shutil.which("openscad")
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter="ai_version_5")
    check_previous_versions(root)
    report={"meshes":[],"connections":[],"limitations":[
        "Prescribed deflection checks passage and recovery space only; not FEA, insertion force, pull-out rating or PETG durability.",
        "All candidates require printed fit, creep and destructive pull tests before choosing a cabinet connector.",
    ]}
    kits={}
    for path in sorted((root/"parts").glob("*ai_version_5_style*/working.yaml")):
        part=yaml.safe_load(path.read_text(encoding="utf-8")); folder=path.parent
        p=drawing.get_ai_version_5_parameters(**part["oobb_details"])
        if p.get("tight_key_trial",False) or p["connector_design"] in ["key_size_fit_suite","snap_recessed_twin","tiled_hybrid","recessed_twin_fit_suite"]:
            # Later coupons have separate validators for their different interfaces.
            continue
        models={}
        for filename,view in {"3dpr":"print_layout",**drawing.get_ai_version_5_views(p)}.items():
            print(f"Exporting {p['connector_design']}/{filename}",flush=True)
            result=subprocess.run([exe,"--backend=Manifold","--hardwarnings","--export-format=binstl",
                                   "-o",str(folder/f"{filename}.stl"),str(folder/f"{filename}.scad")],
                                  capture_output=True,text=True,timeout=600)
            (folder/f"validation_{filename}_openscad.log").write_text(result.stdout+result.stderr,encoding="utf-8")
            result.check_returncode()
            mesh=trimesh.load_mesh(folder/f"{filename}.stl"); models[filename]=mesh
            thing=__import__("oobb").get_default_thing(type="validation")
            drawing.get_ai_version_5(thing,**dict(part["oobb_details"],connector_view=view))
            design=thing["ai_design"]
            checks={"watertight":bool(mesh.is_watertight),"winding":bool(mesh.is_winding_consistent),
                    "positive_volume":bool(mesh.volume>0)}
            if design["printable"]:
                bodies=[b for b in mesh.split(only_watertight=False) if b.volume>0.001]
                checks.update(
                    exact_piece_count=len(bodies)==design["expected_bodies"],
                    every_piece_on_bed=all(abs(b.bounds[0,2])<0.01 for b in bodies),
                    fits_a1_mini=bool(np.all(mesh.extents[:2]+2*p["bed_margin"] <= 180)),
                )
                # Direct snaps/plates/loose key have no airborne downward faces.
                # Screw reference and the C rail keep localized short bridges.
                if p["connector_design"] in ["snap_single","snap_twin"] or filename in ["plate","key"]:
                    bad=(mesh.face_normals[:,2]<-0.708)&(mesh.triangles[:,:,2].max(axis=1)>0.05)
                    if p["connector_design"] != "screw_reference":
                        checks["no_unsupported_downward_faces"]=float(mesh.area_faces[bad].sum())<0.02
            report["meshes"].append({"design":p["connector_design"],"file":filename,"checks":checks,
                                     "volume_mm3":float(mesh.volume),"bounds_mm":mesh.bounds.tolist()})
        kits[p["connector_design"]]=models["3dpr"].volume
        if p["connector_design"] != "connector_suite":
            plate=moved(models["plate"],[0,5,0])
            rail_local=local_rail(models["rail"],p)
            rail=moved(rail_local,[0,0,p["plate_thickness"]])
            pieces=[plate,rail]
            checks={"seated_plate_rail_clear":overlap(plate,rail)<0.02}
            details={}
            if p["connector_design"] in ["snap_single","snap_twin"]:
                cross_section=section(plate,5)
                bands=[box(-2,1,-1.4,3)]
                if p["connector_design"] == "snap_twin":
                    bands.append(box(1.4,1,2,3))
                checks["no_thin_web_between_receiver_openings"]=all(cross_section.intersection(band).area<0.001 for band in bands)
                checks["relaxed_hooks_block_withdrawal"]=overlap(plate,moved(rail,[0,0,0.5]))>0.1
                checks["rigid_guide_limits_sideways_play"]=overlap(plate,moved(rail,[0.6,0,0]))>0.1
                flex=compressed(rail_local,p)
                collisions=[overlap(plate,moved(flex,[0,0,p["plate_thickness"]+distance]))
                            for distance in [0,0.5,1,2,4,6,8,10,12]]
                checks["compressed_hooks_can_pass"]=max(collisions)<0.03
                checks["compressed_rail_is_valid"]=flex.is_watertight and flex.is_winding_consistent
                details["max_prescribed_insertion_collision_mm3"]=max(collisions)
            elif p["connector_design"] == "snap_key":
                key=models["key"].copy()
                key.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]])
                offset=[0,(p["rail_height"]-p["key_height"])/2,p["plate_thickness"]+p["key_z"]]
                assembled_key=moved(key,offset); pieces.append(assembled_key)
                checks["key_seats_without_interference"]=overlap(assembled_key,rail)+overlap(assembled_key,plate)<0.02
                checks["key_catches_tongue_on_side_withdrawal"]=overlap(moved(assembled_key,[-0.5,0,0]),rail)>0.1
                checks["key_blocks_rail_withdrawal"]=overlap(moved(rail,[0,0,0.6]),assembled_key)>0.1
                checks["key_bears_against_plate"]=overlap(moved(assembled_key,[0,0,0.5]),plate)>0.1
                flex=compressed(key,p,key=True)
                collisions=[overlap(rail,moved(flex,[offset[0]+distance,offset[1],offset[2]]))
                            for distance in [-12,-10,-8,-6,-4,-2,0]]
                checks["compressed_key_can_pass"]=max(collisions)<0.03
                details["max_prescribed_insertion_collision_mm3"]=max(collisions)
            expected=sum(piece.volume for piece in pieces)
            checks["kit_has_exact_components"]=abs(models["3dpr"].volume-expected)<0.05
            checks["assembled_has_exact_components"]=abs(models["assembled"].volume-expected)<0.05
            report["connections"].append({"design":p["connector_design"],
                                           "checks":{k:bool(v) for k,v in checks.items()},**details})
            print(json.dumps(report["connections"][-1]),flush=True)
        result=subprocess.run([exe,"--backend=Manifold","--render","--imgsize=1200,1000","--projection=o",
                               "--viewall","--camera=130,-180,250,0,0,0","--colorscheme=Tomorrow",
                               "-o",str(folder/"preview.png"),str(folder/"3dpr.scad")],
                              capture_output=True,text=True,timeout=600)
        result.check_returncode()
        result=subprocess.run([exe,"--backend=Manifold","--render","--imgsize=1200,1000","--projection=o",
                               "--viewall","--camera=80,-100,-100,0,5,12","--colorscheme=Tomorrow",
                               "-o",str(folder/"assembled_preview.png"),str(folder/"assembled.scad")],
                              capture_output=True,text=True,timeout=600)
        result.check_returncode()
    report["suite_exact_quantity"]=bool(abs(kits["connector_suite"]-sum(v for k,v in kits.items() if k!="connector_suite"))<0.1)
    report["all_checks_passed"]=report["suite_exact_quantity"] and all(all(r["checks"].values()) for r in report["meshes"]+report["connections"])
    (out/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print(json.dumps(report["connections"],indent=2),flush=True)
    print("All checks passed:",report["all_checks_passed"],flush=True)
    if not report["all_checks_passed"]:
        raise RuntimeError("Connector validation failed; inspect validation_ai_version_5/report.json")


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--skip-generation",action="store_true")
    main(parser.parse_args().skip_generation)
