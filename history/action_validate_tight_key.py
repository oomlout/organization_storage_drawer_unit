"""Generate sample 27 and check its latch against the original sample 22 beam."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

import numpy as np
import trimesh
import yaml
import working
import working_scad as drawing
from action_validate_ai_version_5 import check_previous_versions, compressed, local_rail, moved, overlap, section


def main(skip_generation=False):
    root=Path(__file__).resolve().parent
    assert Path.cwd().resolve()==root
    out=root/"validation_tight_key"
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter="tight_key_27")
    check_previous_versions(root)
    baseline=json.loads((out/"previous_v5_baseline.json").read_text())
    for name,expected in baseline.items():
        folder=root/"parts"/name
        assert yaml.safe_load((folder/"working.yaml").read_text())["oobb_details"]==expected["inputs"],name
        for filename,digest in expected["scad"].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    folder=next((root/"parts").glob("*ai_version_5_style_tight_key_27"))
    p=drawing.get_ai_version_5_parameters(**yaml.safe_load((folder/"working.yaml").read_text())["oobb_details"])
    exe=shutil.which("openscad.com")
    meshes={}
    report={"meshes":[],"previous_records_unchanged":len(baseline)}
    for name in ["3dpr",*drawing.get_ai_version_5_views(p)]:
        print("Exporting",name,flush=True)
        result=subprocess.run([exe,"--backend=Manifold","--hardwarnings","--export-format=binstl",
                               "-o",str(folder/f"{name}.stl"),str(folder/f"{name}.scad")],
                              capture_output=True,text=True,timeout=300)
        (folder/f"validation_{name}.log").write_text(result.stdout+result.stderr)
        result.check_returncode()
        mesh=trimesh.load_mesh(folder/f"{name}.stl")
        meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,name
        if name!="assembled":
            bodies=list(mesh.split())
            assert len(bodies)==(3 if name=="3dpr" else 1),(name,len(bodies))
            assert all(abs(b.bounds[0,2])<.001 for b in bodies),name
            assert np.all(mesh.extents[:2]+4<=180),name
        if name in ["plate","key"]:
            downward=(mesh.face_normals[:,2]<-.708)&(mesh.triangles[:,:,2].max(axis=1)>.05)
            assert mesh.area_faces[downward].sum()<.02,(name,"unsupported face")
        report["meshes"].append({"file":name,"bounds":mesh.bounds.tolist(),"passed":True})

    old_folder=next((root/"parts").glob("*ai_version_5_style_key_size_extension_suite"))
    old_rail=local_rail(trimesh.load_mesh(old_folder/"rail_22.stl"),p)
    old_plate=moved(trimesh.load_mesh(old_folder/"plate_22.stl"),[0,5,0])
    new_rail=local_rail(meshes["rail"],p)
    new_plate=moved(meshes["plate"],[0,5,0])
    # Interface sections avoid the intentionally different engraved ID.
    for z in [p["key_z"],-8,-4,-.1,1,10]:
        assert section(old_rail,z).symmetric_difference(section(new_rail,z)).area<.001,("beam changed",z)
    for z in [.1,3,6.8]:
        assert section(old_plate,z).symmetric_difference(section(new_plate,z)).area<.001,("plate changed",z)
    key=meshes["key"].copy()
    key.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]])
    offset=[0,(p["rail_height"]-p["key_height"])/2,p["plate_thickness"]+p["key_z"]]
    fitted=moved(key,offset)
    rail=moved(old_rail,[0,0,p["plate_thickness"]])
    checks={
        "seats_in_original_22_beam":overlap(fitted,rail)<.02,
        "seats_clear_of_original_22_plate":overlap(fitted,old_plate)<.02,
        "head_clear_before_stop":overlap(moved(fitted,[.09,0,0]),rail)<.02,
        "hooks_clear_before_stop":overlap(moved(fitted,[-.09,0,0]),rail)<.02,
        "head_stops_at_0d1_mm":overlap(moved(fitted,[.15,0,0]),rail)>.1,
        "hooks_stop_at_0d1_mm":overlap(moved(fitted,[-.15,0,0]),rail)>.1,
        "key_blocks_beam_withdrawal":overlap(moved(rail,[0,0,.6]),fitted)>.1,
        "key_bears_on_plate":overlap(moved(fitted,[0,0,.5]),old_plate)>.1,
    }
    flex=compressed(key,p,key=True)
    # Check the actual insertion direction, including the final recovery region.
    collisions=[overlap(rail,moved(flex,[distance,offset[1],offset[2]]))
                for distance in np.arange(-18,.051,.25)]
    checks["prescribed_flex_passes_original_slot"]=max(collisions)<.03
    checks["prescribed_flex_mesh_valid"]=flex.is_watertight and flex.is_winding_consistent
    total=sum(meshes[name].volume for name in ["plate","rail","key"])
    checks["kit_exact_quantity"]=abs(meshes["3dpr"].volume-total)<.05
    checks["assembly_exact_quantity"]=abs(meshes["assembled"].volume-total)<.05
    report.update({
        "checks":{k:bool(v) for k,v in checks.items()},
        "key_capture_play_mm":2*p["key_latch_clearance"],
        "max_prescribed_insertion_collision_mm3":float(max(collisions)),
        "screening_key_strain":p["estimated_key_strain"],
        "limitations":"Prescribed flex is a geometric passage check, not FEA or an insertion-force rating. Physical PETG fit remains to be tested.",
        "all_checks_passed":all(checks.values()),
    })
    (out/"report.json").write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2),flush=True)
    assert report["all_checks_passed"]
    for name in ["key","3dpr"]:
        result=subprocess.run([exe,"--backend=Manifold","--render","--imgsize=1200,900",
            "--projection=o","--viewall","--camera=0,0,0,0,0,0,100","--colorscheme=Tomorrow",
            "-o",str(folder/f"{name}_preview.png"),str(folder/f"{name}.scad")],
            capture_output=True,text=True,timeout=300)
        result.check_returncode()


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--skip-generation",action="store_true")
    main(parser.parse_args().skip_generation)
