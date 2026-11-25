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
    out=root/"validation_tiled_v5_six_mm"
    out.mkdir(exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter="tiled_")
    check_previous_versions(root)
    baseline=json.loads((root/"validation_tiled_v5_print_revision/previous_coupons_baseline.json").read_text())
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
                half=np.array([p["bed_width"],p["bed_height"]])/2
                assert np.all(lo[:2]>=-half+p["bed_margin"]-.001) and np.all(hi[:2]<=half-p["bed_margin"]+.001),(name,"bed boundary",mesh.bounds)
                assert lo[0]>=-half[0]+p["bed_exclusion"][0]+p["bed_margin"]-.001 or lo[1]>=-half[1]+p["bed_exclusion"][1]+p["bed_margin"]-.001,(name,"cutter exclusion",mesh.bounds)
            if "_tile_" in name:
                assert abs(mesh.bounds[1,2]-p["plate_thickness"])<.001,(name,"not flat")
                down=(mesh.face_normals[:,2]<-.9)&(mesh.triangles[:,:,2].max(axis=1)>.05)
                for face in np.flatnonzero(down & (mesh.area_faces>=3.3)):
                    # Only the explicitly requested M6 nut-seat bridges may
                    # exceed the small snap ledge limit. Locate them in the
                    # actual mirrored/flipped, bed-offset print coordinates.
                    assert name.startswith("back_tile_"),(name,"large unsupported flat face")
                    tile=p["tiles"][int(name.rsplit("_",1)[1])-1]
                    flip=tile["bed_layer"]==1
                    bounds=tile["bounds"]
                    cx=-(bounds[0]+bounds[2])/2
                    cy=(bounds[1]+bounds[3])/2*(-1 if flip else 1)
                    centres=[[-a["x"]+tile["bed_center"][0]-cx,
                              a["y"]*(-1 if flip else 1)+tile["bed_center"][1]-cy]
                             for a in p["rear_attachments"]]
                    centre=mesh.triangles_center[face,:2]
                    assert min(np.linalg.norm(centre-c) for c in centres)<6.2,(name,"bridge outside M6 seat")
                    assert mesh.area_faces[face]<25,(name,"excessive M6 bridge",mesh.area_faces[face])
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
        # Check actual exported opening edges, rather than trusting derived
        # dimensions: every adjacent pair must retain the extra 1 mm gap.
        cx=-p["natural_width"]/2+p["drawer_border_edge"]+p["opening_width"]/2
        bottom=-p["natural_height"]/2+p["drawer_border_edge"]
        for row in range(p["row"]-1):
            top=bottom+row*p["pitch_y"]+p["opening_height"]
            next_bottom=bottom+(row+1)*p["pitch_y"]
            assert abs(next_bottom-top-2.8)<1e-6
            for name in ["front","back"]:
                z=p["plate_thickness"]/2 if name=="front" else p["assembled_depth"]-p["plate_thickness"]/2
                assert not any(occupied(name,[[cx,top-.1,z],[cx,next_bottom+6.2,z]])),("opening edge",row,name)
                assert all(occupied(name,[[cx,top+.1,z],[cx,next_bottom-.1,z]])),("row separation",row,name)
        # M6 through bores and 1.5 mm hex seats are only on the rear. Test
        # either side of the nominal seat floor, away from OOBB bridge relief.
        attachment_points={(a["x"],a["y"]) for a in p["rear_attachments"]}
        assert attachment_points=={(-x,y) for x,y in attachment_points}
        seat_floor=p["plate_thickness"]-p["attachment_nut_depth"]
        for x,y in attachment_points:
            assert not any(occupied("back",[[x,y,p["assembled_depth"]-z] for z in [.2,seat_floor-.1,seat_floor+.1,p["plate_thickness"]-.2]]))
            assert all(occupied("back",[[x+4.7,y,p["assembled_depth"]-z] for z in [.75,seat_floor-.1]])),("M6 seat floor",x,y)
            assert not any(occupied("back",[[x+4.7,y,p["assembled_depth"]-z] for z in [seat_floor+.1,p["plate_thickness"]-.2]])),("M6 recess depth",x,y)
            assert all(occupied("back",[[x+6.9,y,p["assembled_depth"]-z] for z in [.75,p["plate_thickness"]-.5]])),("M6 outside wall",x,y)
            assert all(occupied("front",[[x,y,z] for z in [.75,2.5]])),("unexpected front attachment hole",x,y)
        paired=meshes["back"].copy()
        paired.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,2*p["assembled_depth"]],[0,0,0,1]])
        assert overlap(paired,meshes["assembled"])<.02,"back-to-back interference"
        # Retain the 6 mm stop projection and keep its full thickness in the panel.
        cx=-p["natural_width"]/2+p["drawer_border_edge"]+p["opening_width"]/2
        cy=-p["natural_height"]/2+p["drawer_border_edge"]
        assert all(occupied("front",[[cx,cy+5.8,p["stop_thickness"]/2],[cx,cy+3,.1],[cx,cy+3,p["stop_thickness"]-.1]]))
        assert not any(occupied("back",[[cx,cy+3,p["assembled_depth"]-1.5]]))
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
            strip=[[x+dx,rail["y"]+1,z] for dx in [-.5,0,.5]
                   for z in [p["plate_thickness"]/4,3*p["plate_thickness"]/4]]
            assert all(occupied("front",strip)),("snap cross-tie missing",rail)
            assert all(occupied("back",[[a,b,p["assembled_depth"]-c] for a,b,c in strip])),("rear cross-tie missing",rail)
        # Check both actual rail ends: bevelled tabs fit the full-plate opening,
        # recover behind its catch land and resist withdrawal.
        snap=meshes["snap_rail"].copy()
        snap.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,p["rail_length"]/2],[0,0,0,1]])
        for z in [-.5,p["rail_length"]+.5]:
            cross=section(snap,z)
            floor=max(0,.5-p["plate_thickness"]+p["snap_tip_floor"])
            assert abs(cross.bounds[1]-floor)<.001 and abs(cross.bounds[3]-p["rail_height"])<.001
            assert abs(cross.area-2*p["snap_profile"]["twin_arm_thickness"]*(p["rail_height"]-floor))<.01,("tab section",cross.area)
        for z in [-p["snap_tip_length"]+.1,p["rail_length"]+p["snap_tip_length"]-.1]:
            cross=section(snap,z)
            assert abs(cross.bounds[1]-(p["snap_tip_floor"]-.1))<.001
        # The root extension must really remain a flexible 1.8 mm arm.
        # Retain the outer bearing strips, with empty relief slots between.
        root_probe=p["snap_root_distance"]*.1
        for z in [root_probe,p["rail_length"]-root_probe]:
            cross=section(snap,z)
            for sign in [-1,1]:
                for x in [1.65,2.5,3.35,4.05,5.4]:
                    assert cross.contains(Point(sign*x,5)),("spring arm/bearing edge",z,x)
                for x in [0,1.5,3.7]:
                    assert not cross.contains(Point(sign*x,5)),("root slot obstructed",z,x)
        # A seam snap checks both adjoining tile halves, unlike isolated coupons.
        rail=next(r for r in p["rail_positions"] if r["connection"]=="snap" and r["seam"])
        fitted=moved(snap,[rail["x"],rail["y"],p["plate_thickness"]])
        assert overlap(fitted,meshes["front"])<.02
        assert overlap(moved(fitted,[0,0,.5]),meshes["front"])>.1,("front snap retention",rail)
        assert overlap(moved(fitted,[0,0,-.5]),meshes["back"])>.1,("rear snap retention",rail)
        q={"root_distance":p["snap_root_distance"],"insertion_deflection":p["snap_hook_projection"]-p["snap_clearance"],
           "hook_shoulder_z":-p["snap_shoulder_depth"],"guide_half_width":0,
           "rigid_outer_half_width":p["snap_profile"]["snap_arm_outer"]}
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
