"""Build and verify the selected 1 x 2 V7 unit through the normal source pipeline."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import zipfile
import numpy as np
import trimesh
import yaml
from shapely.geometry import box,Polygon,LineString
import working
import working_scad as drawing
import oobb
from working_scad_v7 import views
from action_validate_v7 import export,check_dxf,prescribed_flex
from action_validate_v7_permanent_snap import region_clip
from action_validate_v7_front_plug import to_panel,plug_to_clip,spread,full_contact_check
from action_validate_ai_version_5 import overlap,moved,section,check_previous_versions
from action_lock_version_6 import check as check_release

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'validation_v7_unit_interchangeable'


def previous_check():
    records=json.loads((ROOT/'validation_v7_unit_1x2/previous_v7_baseline.json').read_text(encoding='utf-8'))
    for name,entry in records.items():
        folder=ROOT/'parts'/name
        assert yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details']==entry['inputs'],name
        for filename,digest in entry['files'].items():
            assert hashlib.sha256((folder/filename).read_bytes()).hexdigest()==digest,(name,filename)
    previous=json.loads((OUT/'previous_unit_baseline.json').read_text(encoding='utf-8'))
    snapshot=OUT/'previous_unit'
    assert yaml.safe_load((snapshot/'working.yaml').read_text(encoding='utf-8'))['oobb_details']==previous['inputs']
    for filename,digest in previous['files'].items():
        assert hashlib.sha256((snapshot/filename).read_bytes()).hexdigest()==digest,('Previous unit snapshot',filename)
    check_release();check_previous_versions(ROOT)
    return dict(records=len(records),files=sum(len(r['files']) for r in records.values()))


def reverse_end(mesh,length):
    result=mesh.copy()
    result.apply_transform([[-1,0,0,0],[0,-1,0,-length],[0,0,1,0],[0,0,0,1]])
    return result


def main(skip_generation=False):
    OUT.mkdir(exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter='ai_version_7',scad_navigation=False)
    report=dict(previous=previous_check(),meshes=[],joints=[],dxf=[])
    folder=next((ROOT/'parts').glob('*ai_version_7_style_unit_1_wide_2_tall'))
    inputs=yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details']
    p=drawing.get_ai_version_7_frame_parameters(**inputs);q=p['frame'];s=p['screw'];length=p['rail_length']
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    meshes={}
    expected={'3dpr':20,'snap_beams':4,'screw_beams':2,'front_plugs':8,'screw_adapters':4}
    for name in ['3dpr',*views(p)]:
        print('Exporting',name,flush=True);export(exe,folder,OUT,name)
        mesh=trimesh.load_mesh(folder/f'{name}.stl');meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,(name,'closed mesh')
        parts=list(mesh.split(only_watertight=False))
        if name!='assembled':
            assert len(parts)==expected.get(name,1),(name,len(parts))
            assert all(abs(part.bounds[0,2])<.001 for part in parts),(name,'bed contact')
        if name not in ['3dpr','assembled']:
            assert max(mesh.extents[:2])+4<256,(name,'P1P bed')
        report['meshes'].append(dict(view=name,bodies=len(parts),closed=True,extents_mm=mesh.extents.tolist(),volume_mm3=float(mesh.volume)))
    for batch,single,n in [('snap_beams','snap_beam',4),('screw_beams','screw_beam',2),
                            ('front_plugs','front_plug',8),('screw_adapters','screw_adapter',4)]:
        assert abs(meshes[batch].volume-n*meshes[single].volume)<.25,(batch,'batch volume')
    kit_volume=sum(meshes[name].volume for name in ['front','back','snap_beams','screw_beams','front_plugs','screw_adapters'])
    assert abs(meshes['3dpr'].volume-kit_volume)<.25,'Overview contains duplicates or overlaps'
    assert abs(meshes['front'].volume-meshes['back'].volume)<1e-6
    assert abs(meshes['front'].extents[2]-18)<.001
    laser=meshes['front_laser'];flat=section(laser,.1)
    assert abs(laser.extents[2]-6)<.001
    for z in [3,5.9]:assert flat.symmetric_difference(section(laser,z)).area<.001
    for r in p['frame_mounts']:
        hole=box(r['x']-2.599,r['hole_y']-2.599,r['x']+2.599,r['hole_y']+2.599)
        assert flat.intersection(hole).area<1e-6
        assert section(meshes['front'],.1).intersection(hole).area<1e-6
    old_folder=next((ROOT/'parts').glob('*ai_version_7_style_front_spreader_plug_short_test'))
    old=trimesh.load_mesh(old_folder/'sample_71.stl')
    sample=meshes['sample_71'];receiver=meshes['receiver_6_0'];snap=meshes['snap_beam']
    def interface(mesh):return region_clip(mesh,[-6,-20,-.1],[6,9,7.1])
    reference=interface(old)
    for label,beam in [('new coupon',sample),('front end',snap),('back end',reverse_end(snap,length))]:
        part=interface(beam)
        assert abs(reference.volume-part.volume)<.005,(label,'changed volume')
        assert reference.difference(part,engine='manifold').volume<.005,(label,'changed interface')
    report['approved_interface']=dict(sample=71,both_ends_match=True,engraving_omitted=True,slots_mm=7)
    baseline=json.loads((OUT/'previous_unit_baseline.json').read_text(encoding='utf-8'))
    for name in ['front','back','front_laser','front_plug','front_plugs','screw_adapter','screw_adapters','sample_71','receiver_6_0']:
        assert hashlib.sha256((folder/f'{name}.stl').read_bytes()).hexdigest()==baseline['files'][f'{name}.stl'],(name,'unchanged part altered')
    report['unchanged_unit_parts']=dict(faces=True,plugs=True,adapters=True,coupons=True)
    report['beam_lightening']=[]
    for name,axis,height in [('snap_beam',p['tongue_height']/2,p['beam_running_height']),
                              ('screw_beam',s['axis_height'],s['running_height'])]:
        mesh=meshes[name];profile=section(mesh,1);removed=0.0
        for window in p['beam_windows']:
            cy=window['y'];lo=cy-window['length']/2;hi=cy+window['length']/2
            loops=[Polygon(ring) for ring in profile.interiors if Polygon(ring).contains(box(-.01,cy-.01,.01,cy+.01).centroid)]
            assert len(loops)==1,(name,'window missing')
            hole=loops[0]
            assert abs(hole.bounds[0]+2.5)<.001 and abs(hole.bounds[2]-2.5)<.001
            # The shared fn=50 circle tessellation misses each Y extremum
            # of an R2 rounded corner by about .004 mm.
            assert abs(hole.bounds[1]-lo)<.005 and abs(hole.bounds[3]-hi)<.005
            expected_area=window['width']*window['length']-(4-np.pi)*window['radius']**2
            assert abs(hole.area-expected_area)<.1,(name,'rounded corner area')
            # The corner must retain material, unlike a plain rectangular cut.
            corner=box(-2.49,lo+.01,-2.3,lo+.2)
            assert profile.intersection(corner).area>.02,(name,'corner radius missing')
            for z in [.1,height/2,height-.1]:
                shape=section(mesh,z)
                assert shape.intersection(box(-2.49,lo+2.1,2.49,hi-2.1)).area<1e-6,(name,'window is blind')
                line=shape.intersection(LineString([(-5.5,cy),(5.5,cy)]))
                assert abs(line.length-6)<.001,(name,'side rails changed')
            removed+=hole.area*height
        roof=region_clip(mesh,[3.1,-85,0],[5.4,-80,20]).bounds[1,2]
        assert abs(roof-axis-8)<.001,(name,'different bearing height')
        stop=region_clip(mesh,[7,-109,0],[9,-103,20])
        assert abs(stop.extents[1]-3)<.001 and abs(stop.bounds[1,2]-axis-8)<.001,(name,'centre stop changed')
        old_beam=trimesh.load_mesh(OUT/'previous_unit'/f'{name}.stl')
        if name=='snap_beam':assert abs(old_beam.volume-mesh.volume-removed)<.1,'Extra snap material changed'
        report['beam_lightening'].append(dict(beam=name,windows=2,window_size_mm=[5,63],radius_mm=2,
            side_rails_mm=3,solid_end_land_mm=35,solid_centre_land_mm=16,
            removed_window_volume_mm3=float(removed),
            reduction_vs_same_beam_without_windows_percent=float(100*removed/(mesh.volume+removed)),
            reduction_vs_previous_beam_percent=float(100*(old_beam.volume-mesh.volume)/old_beam.volume),
            running_roof_above_receiver_axis_mm=float(roof-axis),centre_stop=True))
    contact=full_contact_check(sample,receiver,p)
    closed=prescribed_flex(sample,p,p['trials'][0])
    collisions=[overlap(receiver,to_panel(moved(closed,[0,-d,0]),p)) for d in np.linspace(0,9,25)]
    assert max(collisions)<.015
    seated=spread(sample,p,p['front_plug']['seated_spread'])
    plug=plug_to_clip(meshes['front_plug'],p)
    assert overlap(sample,plug)>.05
    assert overlap(seated,plug)<.015
    assert overlap(closed,plug)>.1
    drives=[overlap(seated,moved(plug,[0,d,0])) for d in np.linspace(0,16,43)]
    assert max(drives)<.015
    assert overlap(receiver,to_panel(moved(plug,[0,-.1,0]),p))>.01
    tip_width=section(meshes['front_plug'],p['front_plug']['stem_depth']-.01).bounds[2]*2
    assert .79<tip_width<.82
    report['snap_and_plug']=dict(**contact,insertion_max_collision_mm3=max(collisions),
        plug_drive_max_collision_mm3=max(drives),tip_width_near_end_mm=tip_width,
        fitted_stem_mm=2.6,retention='friction',seated_spread_per_arm_mm=.1)
    # Test every complete beam against BOTH actual face meshes. The raw snap
    # seats freely; the expanded coupon checks the plugged state at each end.
    front=meshes['front'];back=front.copy()
    back.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,q['assembled_depth']],[0,0,0,1]])
    for mount in p['frame_mounts']:
      for kind in ['snap_beam','screw_beam']:
        r=dict(mount,kind=kind);is_snap=kind=='snap_beam';beam=meshes[kind].copy()
        offset=p['tongue_height']/2 if is_snap else s['axis_height']
        beam.apply_transform([[-1,0,0,r['x']],[0,0,-1,r['hole_y']+offset],[0,-1,0,6],[0,0,0,1]])
        values=[overlap(face,beam) for face in [front,back]]
        assert max(values)<.015,(r,values)
        for rear in [False,True]:
            part=meshes['front_plug' if is_snap else 'screw_adapter'].copy()
            extension=p['front_plug']['outer_y']-6 if is_snap else s['flange_size'][2]
            part.apply_transform([[-1 if rear else 1,0,0,r['x']],[0,1,0,r['hole_y']],
                                  [0,0,-1 if rear else 1,q['assembled_depth']+extension if rear else -extension],[0,0,0,1]])
            assert max(overlap(face,part) for face in [front,back])<.015,(r,'outside part')
            if not is_snap:assert overlap(beam,part)<.015,(r,'guide hits beam')
            for distance in [0,1,3,6,10,16]:
                moving=moved(part,[0,0,distance if rear else -distance])
                assert max(overlap(face,moving) for face in [front,back])<.015,(r,'outside insertion',distance)
            # The independent corner fixing holes must remain usable beside
            # the external caps/adapters, including a standard M3 head envelope.
            for corner in q['corner_holes']:
                head=trimesh.creation.cylinder(radius=3,height=3,sections=32)
                head.apply_translation([corner['x'],corner['y'],q['assembled_depth']+1.5 if rear else -1.5])
                assert overlap(part,head)<.015,(r,'corner screw blocked')
        report['joints'].append(dict(**r,both_faces_clear=True,maximum_collision_mm3=max(values)))
    # Side-loaded OOBB nut and full screw shank at BOTH brace ends.
    beam=meshes['screw_beam']
    for rear in [False,True]:
        local=reverse_end(beam,length) if rear else beam
        nut=trimesh.creation.cylinder(radius=s['nut_radius']-.03,height=s['nut_depth']-.08,sections=6)
        nut.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
        nut.apply_translation([0,-s['nut_near']-s['nut_depth']/2,s['axis_height']])
        for d in np.linspace(0,10,21):assert overlap(local,moved(nut,[d,0,0]))<.02,('nut insertion',rear,d)
        for d in [-.3,.3]:assert overlap(local,moved(nut,[0,d,0]))>.01,('nut axial capture',rear)
        bore=trimesh.creation.cylinder(radius=s['bore_radius']-.04,height=s['length'],sections=32)
        bore.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
        bore.apply_translation([0,6+s['flange_size'][2]-s['length']/2,s['axis_height']])
        assert overlap(local,bore)<.02,('screw shank',rear)
    adapter=meshes['screw_adapter']
    shank=trimesh.creation.cylinder(radius=s['bore_radius']-.04,height=20,sections=48)
    shank.apply_translation([0,0,10])
    assert overlap(adapter,shank)<.02,'Adapter shank path blocked'
    head_r=oobb.gv('screw_countersunk_radius_m3','3dpr')-.04
    head_d=oobb.gv('screw_countersunk_depth_m3','3dpr')
    head=trimesh.creation.revolve([[0,.02],[head_r,.02],[s['bore_radius']-.04,head_d-.02],[0,head_d-.02]],sections=48)
    assert overlap(adapter,head)<.02,'Countersunk head blocked'
    assert overlap(adapter,moved(head,[0,0,.3]))>.02,'Countersink has no head seating stop'
    report['screw']=dict(nuts=4,screws=4,size='M3 x 20 countersunk',both_ends_side_load=True,
                         clear_shank=True,axial_nut_capture=True,projection_after_nut_mm=s['projection_after_nut'])
    for name,profile in [('front_laser_2d',flat),('receiver_laser',section(receiver,.1))]:
        report['dxf'].append(check_dxf(folder/f'{name}.dxf',profile))
    # A separate preview source gives an upright service view without changing
    # manufacturing geometry. Negative CAD Y is up in service.
    (OUT/'upright.scad').write_text('rotate([-90,0,0]) { include <'+(folder/'assembled.scad').as_posix()+'>; }\n',encoding='utf-8')
    # Presentation only: align the two receiver axes to show the common roof.
    (OUT/'beam_comparison.scad').write_text(
        'translate([-16,0,4]) { include <'+(folder/'snap_beam.scad').as_posix()+'>; }\n'
        'translate([16,0,0]) { include <'+(folder/'screw_beam.scad').as_posix()+'>; }\n',encoding='utf-8')
    for name,source,camera in [('assembly_preview',OUT/'upright.scad','210,-330,220,0,0,0'),
                               ('face_preview',folder/'front.scad','100,-140,170,0,0,0'),
                               ('beams_preview',folder/'snap_beams.scad','80,-250,220,0,0,0'),
                               ('plug_preview',folder/'front_plug.scad','25,-35,32,0,0,0'),
                               ('beam_comparison',OUT/'beam_comparison.scad','80,-250,220,0,0,0')]:
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o',
            '--viewall','--autocenter','--camera='+camera,'--colorscheme=Tomorrow',
            '-o',str(folder/f'{name}.png'),str(source)],capture_output=True,text=True,timeout=240)
        (OUT/f'{name}.log').write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()
    delivery=ROOT/'output_v7_unit_interchangeable';delivery.mkdir(exist_ok=True)
    names=[f'{name}.stl' for name in ['front','back','snap_beams','screw_beams','front_plugs','screw_adapters',
                                     'snap_beam','screw_beam','front_plug','screw_adapter','sample_71','receiver_6_0']]
    names+=['front_laser_2d.dxf','receiver_laser.dxf','assembly.json','printing.txt',
            'assembly_preview.png','face_preview.png','beams_preview.png','plug_preview.png','beam_comparison.png']
    for name in names:shutil.copy2(folder/name,delivery/name)
    shutil.copy2(ROOT/'AI_VERSION_7_INTERCHANGEABLE_BEAMS.md',folder/'design_notes.md')
    shutil.copy2(folder/'design_notes.md',delivery/'design_notes.md');names+=['design_notes.md']
    with zipfile.ZipFile(delivery/'v7_unit_interchangeable_beams.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for name in names:archive.write(folder/name,name)
    shutil.copy2(delivery/'v7_unit_interchangeable_beams.zip',folder/'v7_unit_interchangeable_beams.zip')
    shutil.copy2(delivery/'v7_unit_interchangeable_beams.zip',folder/'v7_unit_1_wide_2_tall.zip')
    report.update(all_checks_passed=True,limitations='Prescribed CAD fit only; full-unit force, strength, MDF wear and creep require physical testing.')
    (OUT/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('PASS selected V7 unit:',len(meshes),'closed mesh views, BOTH beam types at ALL six positions, two DXFs',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--skip-generation',action='store_true')
    main(**vars(parser.parse_args()))
