"""Check the aggressive open-centre, internally retained twin-tab coupon."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import numpy as np
import trimesh
import yaml
from shapely.geometry import box
import working
import working_scad as drawing
import scad_help
from action_validate_ai_version_5 import (
    check_previous_versions, compressed, local_rail, moved, overlap, section,
)


def check_previous_connectors(root):
    baseline=json.loads((root/"validation_recessed_tabs/previous_v5_baseline.json").read_text(encoding="utf-8"))
    for name,expected in baseline.items():
        folder=root/"parts"/name
        assert yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))["oobb_details"]==expected["oobb_details"],name
        for filename,digest in expected["scad_sha256"].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    print("All seven earlier v5 records and CAD unchanged",flush=True)


def main(skip_generation=False):
    root=Path(__file__).resolve().parent
    assert Path.cwd().resolve()==root
    output=root/"validation_recessed_tabs";output.mkdir(exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter="ai_version_5")
    check_previous_versions(root)
    check_previous_connectors(root)
    folder=next((root/"parts").glob("*ai_version_5_style_snap_recessed_twin"))
    p=drawing.get_ai_version_5_parameters(**yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))["oobb_details"])
    exe=shutil.which("openscad.com") or shutil.which("openscad")
    models={};report={"meshes":[]}
    for name in ["3dpr","plate","rail","assembled"]:
        result=subprocess.run([exe,"--backend=Manifold","--hardwarnings","--export-format=binstl",
            "-o",str(folder/f"{name}.stl"),str(folder/f"{name}.scad")],
            capture_output=True,text=True,timeout=600)
        (folder/f"validation_{name}_openscad.log").write_text(result.stdout+result.stderr,encoding="utf-8")
        result.check_returncode()
        mesh=trimesh.load_mesh(folder/f"{name}.stl");models[name]=mesh
        checks={"watertight":mesh.is_watertight,"winding_consistent":mesh.is_winding_consistent,"positive_volume":mesh.volume>0}
        if name!="assembled":
            bodies=list(mesh.split(only_watertight=False))
            downward=(mesh.face_normals[:,2]<-0.708)&(mesh.triangles[:,:,2].max(axis=1)>0.05)
            checks.update(exact_body_count=len(bodies)==(2 if name=="3dpr" else 1),
                all_bodies_on_bed=all(abs(b.bounds[0,2])<0.01 for b in bodies),
                fits_a1_mini=np.all(mesh.extents[:2]+4<=180),
                no_unsupported_downward_faces=float(mesh.area_faces[downward].sum())<0.02)
        report["meshes"].append({"file":name,"checks":{k:bool(v) for k,v in checks.items()},
            "bounds_mm":mesh.bounds.tolist(),"volume_mm3":float(mesh.volume)})
    plate=models["plate"].copy()
    plate.apply_transform([[-1,0,0,0],[0,1,0,5],[0,0,-1,p["plate_thickness"]],[0,0,0,1]])
    rail_local=local_rail(models["rail"],p)
    rail=moved(rail_local,[0,0,p["plate_thickness"]])
    center=box(-1,0.1,1,p["rail_height"]-0.1)
    checks={
        "seated_clear":overlap(plate,rail)<0.02,
        "no_middle_piece":all(section(rail_local,z).intersection(center).area<0.001 for z in [-7,-5,-2,-0.1]),
        "two_tabs_at_each_section":all(len(list(section(rail_local,z).geoms))==2 for z in [-7,-5,-2,-0.1]),
        "hook_tips_flush_with_front":abs(rail.bounds[0,2]-plate.bounds[0,2])<0.001,
        "full_width_beam_at_entry":abs(section(rail_local,0.01).bounds[2]-section(rail_local,0.01).bounds[0]-p["rail_width"])<0.001,
        "short_root_relief_closes_inside_beam":section(rail_local,3).intersection(center).area>19,
        "retaining_edges_inside_plate":0<p["receiver_shoulder_z"]<p["plate_thickness"],
        "relaxed_hooks_block_withdrawal":overlap(plate,moved(rail,[0,0,0.5]))>1,
        "beam_shoulder_blocks_over_insertion":overlap(plate,moved(rail,[0,0,-0.3]))>1,
        "sideways_motion_blocked":overlap(plate,moved(rail,[0.6,0,0]))>0.1,
    }
    for side in [-1,1]:
        a,b=sorted([side*3.8,side*4.5])
        band=box(a,1,b,9)
        checks[f"recess_clear_{side}"]=section(plate,p["receiver_shoulder_z"]-0.1).intersection(band).area<0.001
        checks[f"retaining_ledge_present_{side}"]=abs(section(plate,p["receiver_shoulder_z"]+0.1).intersection(band).area-band.area)<0.001
        # Broad beam shoulders contact the plate at Z=0; no exposed tab neck.
        checks[f"beam_bearing_face_{side}"]=abs(section(rail_local,0.01).intersection(band).area-band.area)<0.001
    flex=compressed(rail_local,{**p,"root_distance":0.0})
    collisions=[overlap(plate,moved(flex,[0,0,p["plate_thickness"]+d]))
                for d in [0,0.25,0.5,1,2,3,4,5,6,7,8]]
    checks["prescribed_flex_passes_rectangle"]=max(collisions)<0.03
    checks["flex_mesh_valid"]=flex.is_watertight and flex.is_winding_consistent
    total=plate.volume+rail.volume
    checks["kit_exact_quantity"]=abs(models["3dpr"].volume-total)<0.05
    checks["assembly_exact_quantity"]=abs(models["assembled"].volume-total)<0.05
    y=(p["test_rail_length"]+p["hook_tip_z"])/2-p["number_rail_z"]
    region=box(-4,y-4,4,y+4)
    full=section(models["rail"],9.39).intersection(region).area
    engraved=section(models["rail"],9.7).intersection(region).area
    checks["rail_number_recessed_0d6_mm"]=abs(full-64)<0.01 and full-engraved>1
    region=box(-7.3,2,-4.9,5)
    full=section(models["plate"],6.89).intersection(region).area
    engraved=section(models["plate"],7.2).intersection(region).area
    checks["plate_number_recessed_on_print_top"]=full-engraved>0.2
    report.update(connection_checks={k:bool(v) for k,v in checks.items()},
        max_prescribed_insertion_overlap_mm3=max(collisions),
        nominal_deflection_per_tab_mm=p["insertion_deflection"],
        limitations=["Geometry and prescribed flex checks only; no physical printing, FEA, force rating or PETG durability test."])
    report["all_checks_passed"]=all(checks.values()) and all(all(m["checks"].values()) for m in report["meshes"])
    (output/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    for name,cad,camera in [
        ("preview","3dpr","90,-120,140,0,0,0"),
        ("top_preview","3dpr","0,0,0,0,0,0,100"),
        ("assembled_preview","assembled","40,-65,-75,0,5,10"),
    ]:
        result=subprocess.run([exe,"--backend=Manifold","--render","--imgsize=1200,1000",
            "--projection=o","--viewall",f"--camera={camera}","--colorscheme=Tomorrow",
            "-o",str(folder/f"{name}.png"),str(folder/f"{cad}.scad")],
            capture_output=True,text=True,timeout=600)
        result.check_returncode()
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print(json.dumps(report,indent=2),flush=True)
    assert report["all_checks_passed"],"Inspect validation_recessed_tabs/report.json"


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--skip-generation",action="store_true")
    main(parser.parse_args().skip_generation)
