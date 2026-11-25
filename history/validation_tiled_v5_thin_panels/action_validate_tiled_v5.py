"""Regenerate through populate -> OOMP -> SCAD; export/check the tiled demos."""
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
from action_validate_ai_version_5 import check_previous_versions, moved, overlap, compressed
from action_validate_ai_version_4 import section
from shapely.geometry import Point, box


def main(skip_generation=False):
    root=Path(__file__).resolve().parent
    assert Path.cwd().resolve()==root
    out=root/"validation_tiled_v5_print_revision"
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter="tiled_")
    check_previous_versions(root)
    baseline=json.loads((out/"previous_coupons_baseline.json").read_text())
    for name,expected in baseline.items():
        folder=root/"parts"/name
        assert yaml.safe_load((folder/"working.yaml").read_text())["oobb_details"]==expected["inputs"]
        for filename,digest in expected["scad"].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    report={"meshes":[],"assemblies":[],"prior_v5_records_unchanged":len(baseline),
            "limitations":["Not sliced or physically printed; small snap lands and screw/nut bridges remain.",
                           "Shortened snaps need a PETG fit test; prescribed flex is not an insertion-force simulation."]}
    exe=shutil.which("openscad.com")
    for folder in sorted((root/"parts").glob("*ai_version_5_style_tiled_*")):
        part=yaml.safe_load((folder/"working.yaml").read_text())
        p=drawing.get_ai_version_5_parameters(**part["oobb_details"])
        meshes={}
        for name in ["3dpr",*drawing.get_ai_version_5_views(p)]:
            print("Exporting",p["variant"],name,flush=True)
            result=subprocess.run([exe,"--backend=Manifold","--hardwarnings","--export-format=binstl",
                                   "-o",str(folder/f"{name}.stl"),str(folder/f"{name}.scad")],
                                  capture_output=True,text=True,timeout=600)
            (folder/f"validation_{name}.log").write_text(result.stdout+result.stderr)
            result.check_returncode()
            mesh=trimesh.load_mesh(folder/f"{name}.stl")
            meshes[name]=mesh
            assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,(name,"mesh")
            printable=name not in ["front","back","assembled"]
            expected=1
            if name=="3dpr":
                expected=2*len(p["tiles"])+len(p["rail_positions"])
            elif name.startswith("rails_plate_"):
                index=int(name.rsplit("_",1)[1])-1
                expected=min(p["rails_per_plate"],len(p["rail_positions"])-index*p["rails_per_plate"])
            if printable:
                bodies=len(mesh.split())
                assert bodies==expected,(p["variant"],name,bodies,expected)
                assert abs(mesh.bounds[0,2])<0.001,(name,"bed contact")
            if printable and name!="3dpr":
                lo,hi=mesh.bounds
                assert min(lo[:2])>=-126.001 and max(hi[:2])<=126.001,(name,"bed boundary",mesh.bounds)
                assert lo[0]>=-108.001 or lo[1]>=-98.001,(name,"cutter exclusion",mesh.bounds)
            if "_tile_" in name:
                assert abs(mesh.bounds[1,2]-p["plate_thickness"])<.001,(name,"not flat")
                down=(mesh.face_normals[:,2]<-.9)&(mesh.triangles[:,:,2].max(axis=1)>.05)
                assert max(mesh.area_faces[down],default=0)<3.3,(name,"large unsupported flat face")
            report["meshes"].append({"variant":p["variant"],"view":name,
                                      "bounds":mesh.bounds.tolist(),"volume_mm3":float(mesh.volume),"passed":True})
        # Volume conservation detects unintended interference across EVERY mount,
        # including mirrored rear mounts and tile junctions. Bearing contact is OK.
        total=meshes["front"].volume+meshes["back"].volume
        total+=sum(meshes[k].volume*n for k,n in p["bom"].items() if k in set(p["rail_kinds"]))
        error=total-meshes["assembled"].volume
        assert abs(error)<0.25,("assembly collision/volume",p["variant"],error)
        assert np.allclose(meshes["assembled"].extents,
                           [p["width_total"],p["height_total"],p["assembled_depth"]],atol=0.015)
        # Cut planes through both halves of the lap show exactly the planned seam
        # allocation. All seam rails must be screws at both ends.
        assert all(r["connection"]=="screw" for r in p["rail_positions"] if r["seam_anchor"])
        assert any(r["seam"] and r["connection"]=="snap" for r in p["rail_positions"])
        # Probe retained walls and the inside catch ledge at every snap position.
        # The floor/roof next to the drawer opening is not assumed to be a wall.
        sections={}
        def occupied(name, points):
            result=[]
            for a,b,c in points:
                key=(name,c)
                if key not in sections:
                    sections[key]=section(meshes[name],c)
                result.append(sections[key].contains(Point(a,b)))
            return result
        for rail in p["rail_positions"]:
            if rail["connection"]!="snap":
                continue
            x,y=rail["x"],rail["axis_y"]
            retained=[[x-5.8,y,0.8],[x+5.8,y,0.8],
                      [x-4.2,y,2.5],[x+4.2,y,2.5]]
            empty=[[x-4.2,y,0.8],[x+4.2,y,0.8],[x,y,5]]
            assert all(occupied("front",retained)),("receiver wall/ledge",rail)
            assert not any(occupied("front",empty)),("receiver pocket",rail)
            retained_back=[[a,b,p["assembled_depth"]-c] for a,b,c in retained]
            empty_back=[[a,b,p["assembled_depth"]-c] for a,b,c in empty]
            assert all(occupied("back",retained_back)),("rear receiver wall",rail)
            assert not any(occupied("back",empty_back)),("rear receiver pocket",rail)
            # Probe the previously severed vertical spine in BOTH lap layers.
            # Each layer must retain a connection below the bevelled opening.
            strip=[[x+dx,rail["y"]+1,z] for dx in [-.5,0,.5] for z in [1,4.5]]
            assert all(occupied("front",strip)),("snap cross-tie missing",rail)
            assert all(occupied("back",[[a,b,p["assembled_depth"]-c] for a,b,c in strip])),("rear cross-tie missing",rail)
        # Check both actual rail ends: bevelled tabs fit the full-plate opening,
        # recover behind its catch land and resist withdrawal.
        snap=meshes["snap_rail"].copy()
        snap.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,p["rail_length"]/2],[0,0,0,1]])
        for z in [-3,p["rail_length"]+3]:
            cross=section(snap,z)
            floor=max(0,3-p["plate_thickness"]+p["snap_tip_floor"])
            assert abs(cross.bounds[1]-floor)<.001 and abs(cross.bounds[3]-p["rail_height"])<.001
            assert abs(cross.area-2*p["snap_profile"]["twin_arm_thickness"]*(p["rail_height"]-floor))<.01,("tab section",cross.area)
        for z in [-7.4,p["rail_length"]+7.4]:
            cross=section(snap,z)
            assert abs(cross.bounds[1]-(p["snap_tip_floor"]-.1))<.001
        # A seam snap checks both adjoining tile halves, unlike isolated coupons.
        rail=next(r for r in p["rail_positions"] if r["connection"]=="snap" and r["seam"])
        fitted=moved(snap,[rail["x"],rail["y"],p["plate_thickness"]])
        assert overlap(fitted,meshes["front"])<.02
        assert overlap(moved(fitted,[0,0,.5]),meshes["front"])>.1,("front snap retention",rail)
        assert overlap(moved(fitted,[0,0,-.5]),meshes["back"])>.1,("rear snap retention",rail)
        q={"root_distance":0,"insertion_deflection":p["snap_hook_projection"]-p["snap_clearance"],
           "hook_shoulder_z":-p["snap_profile"]["recessed_shoulder_depth"],"guide_half_width":0}
        flex=compressed(snap,q)
        collisions=[overlap(moved(flex,[rail["x"],rail["y"],p["plate_thickness"]+d]),meshes["front"])
                    for d in [0,.25,.5,1,2,3,4,5,6,7,8]]
        assert max(collisions)<.03,("front insertion",max(collisions))
        report["assemblies"].append({"variant":p["variant"],"bom":p["bom"],
                                     "interference_volume_mm3":float(error),"passed":True})
        for name in ["assembled","3dpr","front_tile_01","front_tile_02"]:
            result=subprocess.run([exe,"--backend=Manifold","--render","--imgsize=1600,1200",
                                   "--projection=o","--viewall","--autocenter",
                                   "--camera=0,0,0,55,0,25,1500","--colorscheme=Tomorrow",
                                   "-o",str(folder/f"{name}.png"),str(folder/f"{name}.scad")],
                                  capture_output=True,text=True,timeout=180)
            result.check_returncode()
    (out/"report.json").write_text(json.dumps(report,indent=2))
    import scad_help
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print("PASS",len(report["meshes"]),"mesh views;",len(report["assemblies"]),"assemblies",flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--skip-generation",action="store_true")
    main(parser.parse_args().skip_generation)
