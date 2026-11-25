"""Mechanical geometry checks and source-derived previews for the V6 screw kit."""
import subprocess
import numpy as np
import trimesh
from shapely.geometry import Point
import oobb
from action_validate_ai_version_5 import overlap,moved,section
from action_validate_v6_clearance import clip


def check_screw_geometry(meshes,p,adapter,beam):
    s=p['screw_rail']
    mount=min(p['rail_positions'],key=lambda r:abs(r['x'])+abs(r['y']))
    receiver=clip(meshes['front'],[mount['x']-10,mount['y']-3,-.1],
                  [mount['x']+10,mount['y']+14,6.1])
    receiver.apply_translation([-mount['x'],-mount['y'],0])
    seated_beam=moved(beam,[0,0,6])
    # Check the ENTIRE insertion path from outside, including the narrow
    # mouth; a guide that expands to match the inner bevel would fail here.
    insertion=[overlap(moved(adapter,[0,0,d]),receiver) for d in [-8,-6,-5.5,-5,-4,-3,-2,-1,-.5,0]]
    assert max(insertion)<.02,('Rigid adapter insertion blocked',insertion)
    assert overlap(adapter,seated_beam)<.02,'Adapter prevents beam seating'
    assert overlap(moved(adapter,[0,0,.25]),receiver)>1,'No outer flange seating stop'
    assert overlap(moved(seated_beam,[0,0,-.25]),receiver)>1,'No broad beam seating shoulder'
    # $fn=50 rounded corners undershoot nominal Y by about .003 mm.
    assert np.allclose(meshes['screw_adapter'].extents,[11,10,7.9],atol=.005)
    # Probe actual countersink flare and a continuous through bore.
    near=section(adapter,-s['flange_size'][2]+.05)
    inner=section(adapter,-.45)
    assert not near.contains(Point(2.8,s['axis_height'])),'Head mouth is too narrow'
    assert inner.contains(Point(2.8,s['axis_height'])),'Countersink does not taper'
    for z in [-2.35,-1.5,-.1,.1,3,5.4]:
        assert not section(adapter,z).contains(Point(0,s['axis_height'])),'Screw path blocked'
    for z,area in [(.1,12),(4.9,12),(5.25,10.5)]:
        cross=section(adapter,z)
        assert len(list(cross.geoms))==2,'Guide must have two substantial cheeks'
        assert abs(cross.area-area)<.01,('Guide cheek/profile differs',z,cross.area)
    down=(meshes['screw_adapter'].face_normals[:,2]<-.709)&(meshes['screw_adapter'].triangles[:,:,2].max(axis=1)>.05)
    assert float(meshes['screw_adapter'].area_faces[down].sum())<.02,'Adapter has an unsupported flat underside'
    # OOBB TRUE dimensions probe hardware fit, while the actual cut uses OOBB
    # 3dpr clearance dimensions and its side-opening/overhang primitives.
    nut_radius=oobb.gv('nut_radius_m3','true')
    nut_depth=oobb.gv('nut_depth_m3','true')
    nut=trimesh.creation.cylinder(radius=nut_radius,height=nut_depth,sections=6)
    nut.apply_translation([0,s['axis_height'],s['nut_near']+s['nut_depth']/2])
    nut_paths=[]
    for rear in [False,True]:
        test=nut.copy()
        if rear:
            test.apply_transform([[1,0,0,0],[0,1,0,0],[0,0,-1,p['rail_length']],[0,0,0,1]])
        side=1 if s['nut_side_clearance']=='left' else -1
        path=[overlap(moved(test,[side*d,0,0]),beam) for d in [12,10,8,6,4,2,0]]
        assert max(path)<.02,('Nut side-loading blocked',rear,path)
        assert overlap(moved(test,[0,0,1]),beam)>1,'Nut can escape axially'
        assert overlap(moved(test,[0,0,-1]),beam)>1,'Nut can escape axially'
        nut_paths.extend(path)
    for z in [s['nut_near']+s['nut_depth']/2,p['rail_length']-s['nut_near']-s['nut_depth']/2]:
        cross=section(beam,z)
        assert cross.contains(Point(-5,s['axis_height'])),'Opposite nut wall is missing'
        assert cross.contains(Point(0,12.3)) and cross.contains(Point(0,3)),'Nut floor or roof is missing'
        assert not cross.contains(Point(5,s['axis_height'])),'Requested side clearance is missing'
    # Model a countersunk M3 x 20 envelope using OOBB's true head/shank values.
    shaft=oobb.gv('hole_radius_m3','true')
    head=oobb.gv('screw_countersunk_radius_m3','true')
    depth=oobb.gv('screw_countersunk_depth_m3','true')
    screw=trimesh.creation.revolve(np.array([[0,0],[head,0],[shaft,depth],[shaft,s['screw_length']],[0,s['screw_length']],[0,0]]))
    screw.apply_translation([0,s['axis_height'],-s['flange_size'][2]])
    hardware_collisions={name:overlap(screw,part) for name,part in
                         [('adapter',adapter),('receiver',receiver),('beam',seated_beam)]}
    assert max(hardware_collisions.values())<.02,('Screw/head path blocked',hardware_collisions)
    assert abs(section(beam,p['middle_stop_z']).area-19*10)<.001,'Screw rail centre stop differs'
    return dict(screw_rails=4,adapters=8,countersunk_M3_x_20=8,M3_nuts=8,
        unchanged_receiver=True,maximum_adapter_insertion_collision_mm3=max(insertion),
        maximum_nut_side_loading_collision_mm3=max(nut_paths),hardware_collision_mm3=hardware_collisions,
        nominal_screw_beyond_nut_pocket_mm=s['screw_penetration']-s['nut_far'],
        broad_flange_and_beam_seating_stops=True,closed_connected_parts=True,
        two_guide_cheeks_mm=(s['guide_width']-s['guide_open_slot_width'])/2,
        external_adapter_projection_per_face_mm=s['flange_size'][2],
        physical_fit='Not yet physically tested')


def render_screw_previews(folder,exe,p):
    s=p['screw_rail'];m=p['screw_rail_positions'][0]
    x,y=m['x'],m['y']
    scene=folder/'screw_joint_preview_scene.scad'
    scene.write_text(
        'rotate([-90,0,0]) intersection() {\n'
        f'translate([{x-8},{y-3},-3]) cube([16,18,29]);\n'
        'union() {\ncolor("teal") { include <front.scad>; }\n'
        f'color("gold") translate([{x},{y+s["axis_height"]},{-s["flange_size"][2]}]) import("screw_adapter.stl");\n'
        f'color("steelblue") translate([{x},{y},6]) multmatrix([[1,0,0,0],[0,0,1,0],[0,-1,0,{p["rail_length"]/2}],[0,0,0,1]]) import("screw_rail.stl");\n'
        '}\n}\n')
    adapter_scene=folder/'screw_adapter_preview_scene.scad'
    adapter_scene.write_text(
        'translate([-9,0,0]) import("screw_adapter.stl");\n'
        f'translate([9,0,{s["adapter_depth"]}]) rotate([0,180,0]) import("screw_adapter.stl");\n')
    for name,source,camera in [('screw_joint',scene,'600,-800,400,0,0,0'),
                               ('screw_adapter',adapter_scene,'60,-85,120,0,0,0'),
                               ('screw_upgrade',folder/'screw_upgrade.scad','0,0,0,0,0,0,500')]:
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1400,1100','--projection=o',
            '--viewall','--autocenter',f'--camera={camera}','--colorscheme=Tomorrow',
            '-o',str(folder/f'{name}.png'),str(source)],capture_output=True,text=True,timeout=180)
        result.check_returncode()
