"""Regenerate V7, export tests/DXFs, and probe actual joint meshes."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import zipfile
import numpy as np
import trimesh
import yaml
import ezdxf
from shapely.geometry import LineString, Polygon, box
from shapely.ops import linemerge, unary_union
import working
import working_scad as drawing
from working_scad_v7 import views
from action_lock_version_6 import check as check_release
from action_validate_ai_version_5 import section, overlap, moved, check_previous_versions

ROOT=Path(__file__).resolve().parent


def to_receiver(mesh,p):
    result=mesh.copy()
    result.apply_transform([[1,0,0,0],[0,0,1,-p['tongue_height']/2],
                            [0,-1,0,p['panel_thickness']],[0,0,0,1]])
    return result


def prescribed_flex(mesh,p,t):
    vertices,faces=trimesh.remesh.subdivide_to_size(mesh.vertices,mesh.faces,max_edge=.8)
    result=trimesh.Trimesh(vertices=vertices,faces=faces,process=True)
    v=result.vertices.copy()
    # Kinematic screening only: do not interpret this as an elastic simulation.
    u=np.clip((v[:,1]-t['effective_root_y'])/t['spring_length'],0,1)
    bend=u*u*(3-u)/2
    arms=(np.abs(v[:,0])>p['pilot_half_width']+.05)&(np.abs(v[:,0])<p['outer']+p['hook_projection']+.01)
    v[arms,0]-=np.sign(v[arms,0])*p['deflection']*bend[arms]
    result.vertices=v
    return result


def export(exe,folder,out,name,suffix='stl'):
    command=[exe,'--backend=Manifold','--hardwarnings']
    if suffix=='stl': command+=['--export-format=binstl']
    command+=['-o',str(folder/f'{name}.{suffix}'),str(folder/f'{name}.scad')]
    r=subprocess.run(command,capture_output=True,text=True,timeout=240)
    (out/f'{name}_{suffix}.log').write_text(r.stdout+r.stderr,encoding='utf-8')
    if r.returncode:
        raise RuntimeError(f'{name} export failed: {r.stdout} {r.stderr}')


def check_dxf(path,profile):
    doc=ezdxf.readfile(path)
    assert doc.units==4, 'DXF must declare millimetres'
    audit=doc.audit()
    assert not audit.has_errors and not audit.fixes, 'DXF requires structural repair'
    lines=[]
    for entity in doc.modelspace():
        assert entity.dxf.layer=='CUT'
        if entity.dxftype()=='LINE':
            start,end=entity.dxf.start,entity.dxf.end
            assert abs(start.z)<1e-8 and abs(end.z)<1e-8
            lines.append(LineString([(start.x,start.y),(end.x,end.y)]))
        elif entity.dxftype()=='LWPOLYLINE':
            assert entity.closed and abs(entity.dxf.elevation)<1e-8
            points=list(entity.get_points())
            assert all(abs(point[4])<1e-8 for point in points), 'Unexpected curved DXF segment'
            for a,b in zip(points,points[1:]+points[:1]):
                lines.append(LineString([(a[0],a[1]),(b[0],b[1])]))
        else:
            raise AssertionError((path.name,'unexpected entity',entity.dxftype()))
    assert len(set(line.wkb for line in lines))==len(lines), 'Duplicate DXF lines'
    merged=linemerge(unary_union(lines))
    rings=list(merged.geoms) if hasattr(merged,'geoms') else [merged]
    region=Polygon()
    for ring in rings:
        assert ring.is_ring, (path.name,'open DXF contour')
        region=region.symmetric_difference(Polygon(ring.coords))
    # OpenSCAD's DXF writer rounds coordinates to six significant digits.
    # Compare boundaries within 1.1 microns, rather than accumulating an
    # absolute area error across the many metres of cabinet cut contour.
    contour_error=region.boundary.hausdorff_distance(profile.boundary)
    assert contour_error<.0011,(path.name,'DXF / flat mesh mismatch',contour_error)
    assert region.symmetric_difference(profile).area<profile.length*.0011
    return dict(file=path.name,closed_contours=len(rings),units='mm',layer='CUT',
                area_mm2=region.area,profile_difference_mm2=region.symmetric_difference(profile).area,
                maximum_contour_difference_mm=contour_error)


def main(skip_generation=False):
    out=ROOT/'validation_v7';out.mkdir(exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter='ai_version_7',scad_navigation=False)
    frozen=check_release(); check_previous_versions(ROOT)
    folder=next((ROOT/'parts').glob('*ai_version_7_style*'))
    p=drawing.get_ai_version_7_parameters(**yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details'])
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    meshes={};report=dict(version=7,released_models_unchanged=len(frozen['parts']),meshes=[],joints=[],dxf=[])
    for name in ['3dpr',*views(p)]:
        print('Exporting',name,flush=True)
        export(exe,folder,out,name)
        mesh=trimesh.load_mesh(folder/f'{name}.stl');meshes[name]=mesh
        assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,name
        bodies=list(mesh.split(only_watertight=False))
        expected=9 if name=='3dpr' else 2 if name=='screw_test' else 1
        assert len(bodies)==expected,(name,'body count',len(bodies))
        assert all(abs(b.bounds[0,2])<.001 for b in bodies),(name,'bed contact')
        if not name.startswith('front_'):
            assert max(mesh.extents[:2])+4<=180,(name,'small bed envelope')
        report['meshes'].append(dict(file=name+'.stl',bodies=expected,watertight=True,
            extents_mm=mesh.extents.tolist(),volume_mm3=float(mesh.volume)))
    assert abs(meshes['3dpr'].volume-sum(meshes[f"sample_{t['sample_number']}"].volume for t in p['trials']))<.05
    receiver=meshes['receiver_6_0']
    cross=section(receiver,.1)
    for i,width in enumerate(p['receiver_hole_widths']):
        x=(i-2)*24
        assert cross.intersection(box(x-width/2+.001,-2.299,x+width/2-.001,2.299)).area<1e-5
        assert cross.intersection(box(x+width/2+.01,-1,x+width/2+.1,1)).area>.17
    for t in p['trials']:
        print('Checking clip',t['sample_number'],flush=True)
        n=t['sample_number'];clip=meshes[f'sample_{n}']; seated=to_receiver(clip,p)
        collision=overlap(receiver,seated)
        assert collision<.005,(n,'seated collision',collision)
        for side in [-1,1]:
            assert overlap(receiver,moved(seated,[side*(p['side_clearance']-.02),0,0]))<.005
            assert overlap(receiver,moved(seated,[side*(p['side_clearance']+.1),0,0]))>.005
        assert overlap(receiver,moved(seated,[0,0,t['axial_clearance']-.02]))<.005
        assert overlap(receiver,moved(seated,[0,0,t['axial_clearance']+.08]))>.02,(n,'missing retaining shoulder')
        assert overlap(receiver,moved(seated,[0,0,-.1]))>.02,(n,'missing inside seating stop')
        flex=to_receiver(prescribed_flex(clip,p,t),p)
        collisions=[overlap(receiver,moved(flex,[0,0,d])) for d in np.linspace(0,t['tip_y']+1,25)]
        assert max(collisions)<.015,(n,'prescribed insertion collision',max(collisions))
        # Thinner sheet adds play, thicker sheet needs sufficient shoulder reach.
        thick_results={}
        for thick,key in [(5.8,'receiver_5_8'),(6.2,'receiver_6_2')]:
            shifted=moved(seated,[0,0,thick-p['panel_thickness']])
            actual=overlap(meshes[key],shifted)
            expected_fit=t['shoulder_y']>=thick
            assert (actual<.005)==expected_fit,(n,'thickness response',thick,actual)
            thick_results[str(thick)]=dict(can_recover_nominally=expected_fit,collision_mm3=actual)
        report['joints'].append(dict(sample_number=n,seated_collision_mm3=collision,
            prescribed_insertion_max_collision_mm3=max(collisions),
            exposed_tip_mm=t['tip_y']-p['panel_thickness'],retention_overlap_mm=p['retention_overlap'],
            axial_clearance_mm=t['axial_clearance'],thickness_response=thick_results))
    # The five-hole card must be useful across its entire calibration range.
    t=next(t for t in p['trials'] if t['sample_number']==44)
    clip=meshes['sample_44']; widths=[]
    for i,width in enumerate(p['receiver_hole_widths']):
        x=(i-2)*24; seated=moved(to_receiver(clip,p),[x,0,0])
        assert overlap(receiver,seated)<.005,('calibration seated',width)
        assert overlap(receiver,moved(seated,[0,0,t['axial_clearance']+.08]))>.02
        q=dict(p,deflection=p['hook_projection']-(width-p['neck_width'])/2+.1)
        flex=moved(to_receiver(prescribed_flex(clip,q,t),p),[x,0,0])
        collisions=[overlap(receiver,moved(flex,[0,0,d])) for d in np.linspace(0,t['tip_y']+1,17)]
        assert max(collisions)<.015,('calibration insertion',width,max(collisions))
        widths.append(dict(width_mm=width,prescribed_insertion_max_collision_mm3=max(collisions)))
    report['calibration_holes']=widths
    # Screw kit seats around the same centre hole; its guide inserts rigidly
    # from outside, stopping at the flange, and its beam shoulders seat inside.
    s=p['screw'];beam=meshes['screw_beam'].copy()
    beam.apply_translation([0,0,s['axis_height']-s['end_height']/2])
    adapter=meshes['screw_adapter'].copy()
    adapter.apply_transform([[1,0,0,0],[0,0,-1,p['panel_thickness']+s['flange_size'][2]],
                             [0,1,0,s['axis_height']],[0,0,0,1]])
    assembled_beam=to_receiver(beam,p);assembled_adapter=to_receiver(adapter,p)
    assert overlap(receiver,assembled_beam)<.005
    assert overlap(receiver,assembled_adapter)<.005
    assert overlap(assembled_beam,assembled_adapter)<.005
    for d in np.linspace(0,8,25):
        assert overlap(receiver,moved(assembled_adapter,[0,0,-d]))<.005,('adapter outside insertion',d)
    assert overlap(receiver,moved(assembled_adapter,[0,0,.1]))>.01,'missing flange seating stop'
    assert overlap(receiver,moved(assembled_beam,[0,0,-.1]))>.01,'missing beam seating stop'
    # Standard OOBB nut true envelope, side loaded on the local +X opening.
    nut=trimesh.creation.cylinder(radius=s['nut_radius']-.03,height=s['nut_depth']-.08,sections=6)
    nut.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
    nut.apply_translation([0,-s['nut_near']-s['nut_depth']/2,s['axis_height']])
    for d in np.linspace(0,10,21):
        assert overlap(beam,moved(nut,[d,0,0]))<.02,('nut loading path',d)
    assert overlap(beam,moved(nut,[0,.3,0]))>.01,'nut not axially captured'
    assert overlap(beam,moved(nut,[0,-.3,0]))>.01,'nut not axially captured'
    bore=trimesh.creation.cylinder(radius=s['bore_radius']-.04,height=s['length'],sections=32)
    bore.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))
    bore.apply_translation([0,p['panel_thickness']+s['flange_size'][2]-s['length']/2,s['axis_height']])
    assert overlap(beam,bore)<.02 and overlap(adapter,bore)<.02,'blocked screw path'
    report['screw']=dict(same_receiver=True,rigid_adapter_insertion=True,side_loaded_nut=True,
        seating_stops=True,screw_path_clear=True,projection_after_nut_mm=s['projection_after_nut'])
    for size in ['small','large']:
        laser=meshes[f'front_{size}_laser']; printed=meshes[f'front_{size}_printed']
        flat=section(laser,.1)
        assert flat.symmetric_difference(section(laser,3)).area<.001
        assert flat.symmetric_difference(section(laser,5.9)).area<.001
        assert abs(laser.extents[2]-6)<.001 and abs(printed.extents[2]-18)<.001
        q=drawing.get_ai_version_6_parameters(**p['face_references'][int(size=='large')])
        assert max(laser.extents[:2])+2*q['bed_margin']<=q['max_face_size']
        assert max(printed.extents[:2])+2*q['bed_margin']<=q['max_face_size']
        printed_cross=section(printed,.1)
        for mount in q['rail_positions']:
            hole=box(mount['x']-3.799,mount['y']+5.701,mount['x']+3.799,mount['y']+10.299)
            assert flat.intersection(hole).area<1e-5 and printed_cross.intersection(hole).area<1e-5
        report.setdefault('prototype_faces',[]).append(dict(size=size,receivers=len(q['rail_positions']),
            laser_depth_mm=6,printed_depth_mm=18,flat_laser_profile=True))
    for name,profile in [('receiver_laser',cross),
                         ('front_small_laser_2d',section(meshes['front_small_laser'],.1)),
                         ('front_large_laser_2d',section(meshes['front_large_laser'],.1))]:
        report['dxf'].append(check_dxf(folder/f'{name}.dxf',profile))
    for name,source in [('clips_preview','3dpr'),('receiver_preview','receiver_6_0'),
                         ('screw_preview','screw_test'),('face_printed_preview','front_small_printed'),
                         ('face_laser_preview','front_small_laser')]:
        r=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o',
            '--viewall','--autocenter','--camera=50,-70,120,0,0,0','--colorscheme=Tomorrow',
            '-o',str(folder/f'{name}.png'),str(folder/f'{source}.scad')],capture_output=True,text=True,timeout=240)
        r.check_returncode()
    report.update(all_checks_passed=True,limitations='Kinematic CAD checks only. No measured force, fatigue, PETG creep or loaded MDF performance.')
    (out/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    from action_preview_v7 import main as preview
    preview(folder,p)
    # Keep the default archive small and unambiguous: print-ready test parts,
    # receiver DXF, instructions and replaceable samples; prototype faces separate.
    files=['3dpr.stl','receiver_6_0.stl','receiver_5_8.stl','receiver_6_2.stl',
           'screw_test.stl','receiver_laser.dxf','receiver_map.svg','printing.txt',
           'connector_test.json','trial_index.csv','results.csv','test_card_overview.png']
    files += [f"sample_{t['sample_number']}.stl" for t in p['trials']]
    with zipfile.ZipFile(folder/'v7_test_card.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for name in files: archive.write(folder/name,name)
    with zipfile.ZipFile(folder/'v7_prototype_faces.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for name in ['front_small_laser_2d.dxf','front_large_laser_2d.dxf',
                     'front_small_printed.stl','front_large_printed.stl','printing.txt']:
            archive.write(folder/name,name)
    delivery=ROOT/'output_v7';delivery.mkdir(exist_ok=True)
    for name in ['v7_test_card.zip','v7_prototype_faces.zip','test_card_overview.png',
                 '3dpr.stl','receiver_6_0.stl','receiver_5_8.stl','receiver_6_2.stl',
                 'screw_test.stl','receiver_laser.dxf','printing.txt',
                 'clips_preview.png','receiver_preview.png','screw_preview.png',
                 'face_printed_preview.png','face_laser_preview.png']:
        shutil.copy2(folder/name,delivery/name)
    shutil.copy2(ROOT/'AI_VERSION_7.md',delivery/'research_and_testing.md')
    record=yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))
    taxonomy=[str(record.get(f'taxonomy_{i}','')) for i in range(1,16)]
    navigation=ROOT/'navigation_oobb'
    for value in taxonomy:
        if value and value!='default': navigation=navigation/value.replace('.','d')
    shutil.copytree(folder,navigation,dirs_exist_ok=True)
    check_release()
    print('PASS V7:',len(meshes),'mesh views, nine clips, three printable receivers, screw joint, three DXFs',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--skip-generation',action='store_true')
    main(parser.parse_args().skip_generation)
