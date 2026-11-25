"""Generate and verify the two numbered PETG coupon beds; no physical-fit claim."""
import argparse
from concurrent.futures import ThreadPoolExecutor
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


def check_original_connectors(root):
    baseline=json.loads((root/"validation_key_size_fit/previous_v5_baseline.json").read_text(encoding="utf-8"))
    for name, expected in baseline.items():
        folder=root/"parts"/name
        assert yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))["oobb_details"] == expected["oobb_details"], name
        for filename,digest in expected["scad_sha256"].items():
            cad=folder/(filename if filename.endswith(".scad") else filename+".scad")
            assert hashlib.sha256(cad.read_bytes()).hexdigest()==digest,(name,filename)
    print("Original five connector records unchanged",flush=True)


def main(skip_generation=False, variant=None):
    root=Path(__file__).resolve().parent
    assert Path.cwd().resolve()==root
    output=root/("validation_key_extension" if variant=="key_size_extension_suite" else "validation_key_size_fit")
    output.mkdir(exist_ok=True)
    exe=shutil.which("openscad.com") or shutil.which("openscad")
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter="ai_version_5")
    check_previous_versions(root)
    check_original_connectors(root)
    if variant=="key_size_extension_suite":
        baseline=json.loads((output/"previous_v5_baseline.json").read_text(encoding="utf-8"))
        for name,expected in baseline.items():
            folder=root/"parts"/name
            assert yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))["oobb_details"]==expected["oobb_details"],name
            for filename,digest in expected["scad_sha256"].items():
                assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
        print("All eight previous v5 records and CAD unchanged",flush=True)
    report={"meshes":[],"trials":[],"suites":[],"limitations":[
        "Interference trials deliberately overlap at the seated taper only.",
        "Prescribed key flex is a geometric passage check, not FEA or an insertion-force/strength rating.",
        "PETG print fit, layer adhesion, creep and retention require physical tests.",
    ]}
    paths=[path for path in (root/"parts").glob("*ai_version_5_style*/working.yaml")
           if yaml.safe_load(path.read_text(encoding="utf-8"))["oobb_details"]["connector_design"]=="key_size_fit_suite"]
    assert len(paths)==3
    if variant:
        paths=[path for path in paths if yaml.safe_load(path.read_text(encoding="utf-8"))["oobb_details"]["variant"]==variant]
        assert len(paths)==1
    for path in paths:
        folder=path.parent
        p=drawing.get_ai_version_5_parameters(**yaml.safe_load(path.read_text(encoding="utf-8"))["oobb_details"])
        views={"3dpr":"print_layout",**drawing.get_ai_version_5_views(p)}
        def export(filename):
            result=subprocess.run([exe,"--backend=Manifold","--hardwarnings","--export-format=binstl",
                "-o",str(folder/f"{filename}.stl"),str(folder/f"{filename}.scad")],
                capture_output=True,text=True,timeout=600)
            (folder/f"validation_{filename}_openscad.log").write_text(result.stdout+result.stderr,encoding="utf-8")
            result.check_returncode()
            return filename,trimesh.load_mesh(folder/f"{filename}.stl")
        print(f"Exporting {len(views)} views:",folder.name,flush=True)
        with ThreadPoolExecutor(max_workers=4) as pool:
            models=dict(pool.map(export,views))
        for name,mesh in models.items():
            checks={"watertight":bool(mesh.is_watertight),
                    "consistent_winding":bool(mesh.is_winding_consistent),"positive_volume":bool(mesh.volume>0)}
            if not name.startswith("assembled"):
                bodies=list(mesh.split(only_watertight=False))
                count=3*len(p["key_trials"]) if name=="3dpr" else 3 if name.startswith("trial_") else 1
                checks.update(exact_piece_count=len(bodies)==count,
                    every_piece_on_bed=all(abs(b.bounds[0,2])<0.01 for b in bodies),
                    fits_a1_mini=bool(np.all(mesh.extents[:2]+2*p["bed_margin"]<=180)))
            if name.startswith(("plate_","key_")):
                bad=(mesh.face_normals[:,2]<-0.708)&(mesh.triangles[:,:,2].max(axis=1)>0.05)
                checks["no_unsupported_downward_faces"]=float(mesh.area_faces[bad].sum())<0.02
            report["meshes"].append({"suite":p["variant"],"file":name,"checks":{k:bool(v) for k,v in checks.items()},
                "volume_mm3":float(mesh.volume),"bounds_mm":mesh.bounds.tolist()})
        for trial in p["key_trials"]:
            q=drawing.get_ai_version_5_parameters(**{**p,**trial,"connector_design":"snap_key"})
            number=trial["sample_number"]; suffix=f"_{number:02d}"
            plate=moved(models["plate"+suffix],[0,5,0])
            rail_local=local_rail(models["rail"+suffix],q)
            rail=moved(rail_local,[0,0,q["plate_thickness"]])
            key=models["key"+suffix].copy()
            key.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]])
            offset=[0,(q["rail_height"]-q["key_height"])/2,q["plate_thickness"]+q["key_z"]]
            assembled_key=moved(key,offset)
            interference=q.get("through_seat_interference",0)
            expected_overlap=(q["rail_height"]*q["through_taper_length"]*interference**2/
                              (q["through_clearance"]+interference)) if interference>0 else 0
            seated_overlap=overlap(plate,rail)
            checks={
                "only_expected_taper_interference":abs(seated_overlap-expected_overlap)<0.02,
                "key_seats_clear":overlap(assembled_key,rail)+overlap(assembled_key,plate)<0.02,
                "key_retained_sideways":overlap(moved(assembled_key,[-0.5,0,0]),rail)>0.1,
                "key_blocks_rail_withdrawal":overlap(moved(rail,[0,0,0.6]),assembled_key)>0.1,
                "key_bears_against_plate":overlap(moved(assembled_key,[0,0,0.5]),plate)>0.1,
            }
            if "through_taper_length" in q:
                # The first plate engagement and all but the final interference
                # zone must remain clear. Offset separates rail shoulder as well.
                start=max(0,q["through_taper_length"]*interference/(q["through_clearance"]+interference))+0.02
                checks["through_piece_clear_before_final_seating"]=overlap(plate,moved(rail,[0,0,start]))<0.02
                # Independently measure the tongue's width at entry, middle, root.
                for z in [-7.0,-3.0,-0.01]:
                    measured=section(rail_local,z).bounds
                    half=q["key_tongue_half_width"]+max(0,1+z/6)*(q["through_clearance"]+interference)
                    checks[f"taper_width_at_{z}_mm"]=abs((measured[2]-measured[0])-2*half)<0.002
            flex=compressed(key,q,key=True)
            collisions=[overlap(rail,moved(flex,[offset[0]+distance,offset[1],offset[2]]))
                        for distance in [-16,-12,-10,-8,-6,-4,-2,0]]
            checks["prescribed_flex_key_can_pass"]=max(collisions)<0.03
            checks["flex_mesh_valid"]=flex.is_watertight and flex.is_winding_consistent
            total=plate.volume+rail.volume+key.volume
            checks["trial_exact_quantity"]=abs(models["trial"+suffix].volume-total)<0.05
            checks["assembly_exact_quantity"]=abs(models["assembled"+suffix].volume-(total-seated_overlap))<0.05
            # Solid behind the numeral; recessed material begins 0.6 mm below top.
            center=(q["test_rail_length"]-q["key_tongue_depth"])/2-q["number_rail_z"]
            region=box(-4,center-4,4,center+4)
            solid=section(models["rail"+suffix],9.39).intersection(region).area
            engraved=section(models["rail"+suffix],9.7).intersection(region).area
            checks["number_recessed_0d6_mm"]=abs(solid-64)<0.01 and solid-engraved>1
            checks["number_not_raised"]=abs(models["rail"+suffix].bounds[1,2]-10)<0.001
            if number in [20,21,22]:
                # Independent transverse slot sections retain the top/bottom
                # material at both sides of the through-key opening.
                slot=section(rail_local,q["key_z"])
                wall=(q["rail_height"]-q["key_height"]-2*q["connector_clearance"])/2
                top=box(-1,q["rail_height"]-wall+0.01,1,q["rail_height"]-0.01)
                bottom=box(-1,0.01,1,wall-0.01)
                checks["slot_walls_at_least_1_mm"]=wall>=1 and all(
                    abs(slot.intersection(band).area-band.area)<0.001 for band in [top,bottom])
                label=box(-7.4,2,-4.9,5)
                full=section(models["plate"+suffix],6.89).intersection(label).area
                engraved=section(models["plate"+suffix],7.2).intersection(label).area
                checks["plate_label_is_recessed"]=full-engraved>0.2
            report["trials"].append({"number":number,"checks":{k:bool(v) for k,v in checks.items()},
                "intentional_overlap_mm3":seated_overlap,"expected_overlap_mm3":expected_overlap,
                "max_prescribed_key_insertion_collision_mm3":max(collisions)})
            print(json.dumps(report["trials"][-1]),flush=True)
        totals={name:sum(models[f"{name}_{t['sample_number']:02d}"].volume for t in p["key_trials"])
                for name in ["trial","assembled"]}
        checks={"print_layout_exact_quantity":abs(models["3dpr"].volume-totals["trial"])<0.1,
                "assembly_exact_quantity":abs(models["assembled"].volume-totals["assembled"])<0.1}
        report["suites"].append({"suite":p["variant"],"checks":{k:bool(v) for k,v in checks.items()},
            "print_bounds_mm":models["3dpr"].bounds.tolist()})
        for filename,camera in [("preview","130,-180,250,0,0,0"),("top_preview","0,0,0,0,0,0,250")]:
            result=subprocess.run([exe,"--backend=Manifold","--render","--imgsize=1600,1600","--projection=o",
                "--viewall",f"--camera={camera}","--colorscheme=Tomorrow",
                "-o",str(folder/f"{filename}.png"),str(folder/"3dpr.scad")],
                capture_output=True,text=True,timeout=600)
            result.check_returncode()
    report["all_checks_passed"]=all(all(item["checks"].values())
        for group in ["meshes","trials","suites"] for item in report[group])
    (output/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print("All checks passed:",report["all_checks_passed"],flush=True)
    if not report["all_checks_passed"]:
        raise RuntimeError(f"Numbered coupon checks failed; see {output/'report.json'}")


if __name__=="__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("--skip-generation",action="store_true")
    parser.add_argument("--variant",choices=["key_size_fit_suite","through_fit_suite","key_size_extension_suite"])
    args=parser.parse_args()
    main(args.skip_generation,args.variant)
