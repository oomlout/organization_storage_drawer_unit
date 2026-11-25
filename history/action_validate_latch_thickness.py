"""Export/check sample-19 thickness trials via the normal generation pipeline."""
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
from action_validate_ai_version_5 import check_previous_versions, compressed, local_rail, moved, overlap, section


def main(skip_generation=False, heavy=False):
    root=Path(__file__).resolve().parent
    assert Path.cwd().resolve()==root
    out=root/("validation_latch_heavy" if heavy else "validation_latch_thickness")
    variant="recessed_twin_heavy_suite" if heavy else "recessed_twin_fit_suite"
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter=variant)
    check_previous_versions(root)
    baseline=json.loads((out/"previous_v5_baseline.json").read_text())
    for name,expected in baseline.items():
        folder=root/"parts"/name
        assert yaml.safe_load((folder/"working.yaml").read_text())["oobb_details"]==expected["inputs"],name
        for filename,digest in expected["scad"].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    folder=next((root/"parts").glob(f"*ai_version_5_style_{variant}"))
    inputs=yaml.safe_load((folder/"working.yaml").read_text())["oobb_details"]
    exe=shutil.which("openscad.com")
    meshes={}
    report={"meshes":[],"trials":[],"previous_records_unchanged":len(baseline)}
    for name in ["3dpr",*drawing.get_ai_version_5_views(inputs)]:
        print("Exporting",name,flush=True)
        result=subprocess.run([exe,"--backend=Manifold","--hardwarnings","--export-format=binstl",
                               "-o",str(folder/f"{name}.stl"),str(folder/f"{name}.scad")],
                              capture_output=True,text=True,timeout=300)
        (folder/f"validation_{name}.log").write_text(result.stdout+result.stderr)
        result.check_returncode()
        mesh=trimesh.load_mesh(folder/f"{name}.stl")
        meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,name
        if not name.startswith("assembled"):
            bodies=list(mesh.split())
            expected=8 if name=="3dpr" else 2 if name.startswith("trial") else 1
            assert len(bodies)==expected,(name,len(bodies))
            assert all(abs(b.bounds[0,2])<0.001 for b in bodies),name
            assert np.all(mesh.extents[:2]+4<=180),name
            downward=(mesh.face_normals[:,2]<-0.708)&(mesh.triangles[:,:,2].max(axis=1)>0.05)
            assert mesh.area_faces[downward].sum()<0.02,(name,"unsupported face")
        report["meshes"].append({"file":name,"bounds":mesh.bounds.tolist(),"passed":True})
    total=0
    control=None
    for trial in inputs["latch_trials"]:
        n=trial["sample_number"]
        p=drawing.get_ai_version_5_parameters(**{**inputs,**trial,"connector_design":"snap_recessed_twin"})
        plate=meshes[f"plate_{n}"].copy()
        plate.apply_transform([[-1,0,0,0],[0,1,0,5],[0,0,-1,p["plate_thickness"]],[0,0,0,1]])
        beam=local_rail(meshes[f"rail_{n}"],p)
        rail=moved(beam,[0,0,p["plate_thickness"]])
        arm_section=section(beam,-2)
        assert len(list(arm_section.geoms))==2,n
        assert abs(arm_section.area-2*p["arm_thickness"]*p["rail_height"])<0.001,n
        assert arm_section.intersection(box(-1,0.1,1,9.9)).area<0.001,n
        assert abs(rail.bounds[0,2]-plate.bounds[0,2])<0.001,n
        assert overlap(plate,rail)<0.02,n
        assert overlap(plate,moved(rail,[0,0,0.5]))>1,(n,"withdrawal catch")
        assert overlap(plate,moved(rail,[0,0,-0.3]))>1,(n,"bearing stop")
        assert overlap(plate,moved(rail,[0.6,0,0]))>0.1,(n,"side restraint")
        flex=compressed(beam,{**p,"root_distance":0})
        collisions=[overlap(plate,moved(flex,[0,0,p["plate_thickness"]+d]))
                    for d in [0,.25,.5,1,2,3,4,5,6,7,8]]
        assert flex.is_watertight and flex.is_winding_consistent,n
        assert max(collisions)<0.03,(n,"prescribed insertion",max(collisions))
        for z in [.8,2.5,5,7]:
            if control is not None:
                assert section(plate,z).symmetric_difference(section(control,z)).area<0.001,(n,"receiver changed")
        if control is None:
            control=plate
            old_variant="recessed_twin_fit_suite" if heavy else "snap_recessed_twin"
            old_folder=next((root/"parts").glob(f"*ai_version_5_style_{old_variant}"))
            old=local_rail(trimesh.load_mesh(old_folder/("rail_25.stl" if heavy else "rail.stl")),p)
            for z in [-7,-6.2,-5,-2,.1,2,5,15]:
                assert section(beam,z).symmetric_difference(section(old,z)).area<0.001,("control unchanged",z)
        if heavy and n in [25,26]:
            old_folder=next((root/"parts").glob("*ai_version_5_style_recessed_twin_fit_suite"))
            for name in ["trial","plate","rail","assembled"]:
                filename=f"{name}_{n}.scad"
                assert (folder/filename).read_bytes()==(old_folder/filename).read_bytes(),filename
        y=(p["test_rail_length"]+p["hook_tip_z"])/2-p["number_rail_z"]
        region=box(-4,y-4,4,y+4)
        full=section(meshes[f"rail_{n}"],9.39).intersection(region).area
        engraved=section(meshes[f"rail_{n}"],9.7).intersection(region).area
        assert abs(full-64)<.01 and full-engraved>1,(n,"rail number")
        region=box(-7.3,2,-4.9,5)
        assert (section(meshes[f"plate_{n}"],6.89).intersection(region).area-
                section(meshes[f"plate_{n}"],7.2).intersection(region).area)>.2,(n,"plate number")
        volume=plate.volume+rail.volume
        assert abs(meshes[f"trial_{n}"].volume-volume)<.05,n
        assert abs(meshes[f"assembled_{n}"].volume-volume)<.05,n
        total+=volume
        report["trials"].append({"number":n,"arm_thickness_mm":p["arm_thickness"],
            "centre_gap_mm":2*p["open_center_half_width"],"max_prescribed_insertion_overlap_mm3":max(collisions),
            "passed":True})
    assert abs(meshes["3dpr"].volume-total)<.1
    assert abs(meshes["assembled"].volume-total)<.1
    report["limitations"]=["Prescribed deflection is a geometric check, not an insertion-force or stress simulation.",
                          "Original 19 has positive user feedback; the thicker samples still require physical trials."]
    (out/"report.json").write_text(json.dumps(report,indent=2))
    for name,camera in [("preview","90,-120,180,0,0,0"),("top_preview","0,0,0,0,0,0,180")]:
        subprocess.run([exe,"--backend=Manifold","--render","--imgsize=1400,1200","--projection=o","--viewall",
                        f"--camera={camera}","--colorscheme=Tomorrow","-o",str(folder/f"{name}.png"),
                        str(folder/"3dpr.scad")],check=True,capture_output=True,text=True)
    import scad_help
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print(f"PASS: 18 mesh views, four latch pairs; all {len(baseline)} previous v5 records unchanged",flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--skip-generation",action="store_true")
    parser.add_argument("--heavy",action="store_true")
    args=parser.parse_args()
    main(args.skip_generation,args.heavy)
