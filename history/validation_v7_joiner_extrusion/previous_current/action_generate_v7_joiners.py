"""Restore optional V7 joiners through populate -> OOMP -> SCAD.

Draw directly through the standard project pipeline. Existing unit manufacturing
geometry must remain byte-identical; accessory geometry and previews may change.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import zipfile

import numpy as np
import oobb
import trimesh
import yaml
from shapely.geometry import Point

import working
import working_scad as drawing
from action_validate_ai_version_5 import section, overlap
from action_validate_v7_finishing import external_part, run_envelopes

ROOT=Path(__file__).resolve().parent


def validate(folder,p):
    mesh=trimesh.load_mesh(folder/'joiners.stl')
    assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0
    bodies=sorted(mesh.split(),key=lambda body:body.centroid[0])
    assert len(bodies)==2 and np.allclose(mesh.extents,[45,20,6],atol=.015)
    shaft=p['optional_joiners']['joiner_bore_radius']
    head=oobb.gv('screw_countersunk_radius_m3','3dpr')
    depth=oobb.gv('screw_countersunk_depth_m3','3dpr')
    report=dict(variant=p['variant'],pieces=[],placements=[])
    q=p['frame']
    for body,part in zip(bodies,p['joiners']):
        assert np.allclose(body.extents,part['size'],atol=.015)
        assert abs(body.bounds[0,2])<.001 and abs(body.bounds[1,2]-6)<.001
        for z in [.3,depth/2,depth+.4,5.9]:
            cross=section(body,z)
            polygons=list(cross.geoms) if cross.geom_type=='MultiPolygon' else [cross]
            assert sum(len(poly.interiors) for poly in polygons)==len(part['holes'])
            original_shaft=oobb.gv('hole_radius_m3','3dpr')
            radius=max(shaft,head-(head-original_shaft)*z/depth)
            for hx,hy in part['holes']:
                x=hx+part['print_center'][0]
                y=hy+part['print_center'][1]+np.tan(np.radians(p['optional_joiners']['screw_angle']))*(9-z)
                holes=[ring for poly in polygons for ring in poly.interiors]
                from shapely.geometry import Polygon
                hole=min((Polygon(ring) for ring in holes),key=lambda polygon:polygon.centroid.distance(Point(x,y)))
                assert hole.contains(Point(x,y)),('Blocked axis',part['name'],z)
                assert np.all(np.abs(np.array(hole.bounds)[2:]-np.array(hole.bounds)[:2]-2*radius)<.4),('Wrong OOBB countersink profile',z,hole.bounds,radius)
        down=(body.face_normals[:,2]<-.9)&(body.triangles[:,:,2].max(axis=1)>.05)
        assert not np.any(down),'Unsupported underside'
        report['pieces'].append(dict(name=part['name'],size_mm=part['size'],holes=len(part['holes']),
            through_diameter_mm=2*shaft,countersink_diameter_mm=2*head,countersink_depth_mm=depth))
        local=body.copy();local.apply_translation(-np.array(part['print_center']))
        assert part['hole_pitch_mm']==2*q['corner_hole_inset']
        # Test every corner, two-/four-way joins, front AND actual handed back.
        for rear in [False,True]:
            fittings=[external_part(trimesh.load_mesh(folder/(m.get('cap_component','front_plug')+'.stl'
                        if m['kind']=='snap_beam' else 'screw_adapter.stl')),p,m,m['kind'],rear)
                      for m in p['frame_mounts']]
            face=trimesh.load_mesh(folder/('back.stl' if rear else 'front.stl'))
            if rear:face.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,q['assembled_depth']],[0,0,0,1]])
            for sx in [-1,1]:
                for sy in [-1,1]:
                    centres=[(sx*q['width_total']/2,sy*q['height_total']/2,0)] if len(part['holes'])==4 else [
                        (sx*q['width_total']/2,sy*(q['height_total']/2-q['corner_hole_inset']),0),
                        (sx*(q['width_total']/2-q['corner_hole_inset']),sy*q['height_total']/2,90)]
                    for x,y,angle in centres:
                        placed=local.copy()
                        placed.apply_transform(trimesh.transformations.euler_matrix(
                            np.pi if rear else 0,0,np.radians(angle)))
                        placed.apply_translation([x,y,q['assembled_depth']+6 if rear else -6])
                        collision=max(overlap(placed,other) for other in [face,*fittings,*run_envelopes(p)])
                        assert collision<.015,(p['variant'],part['name'],rear,x,y,collision)
                        # Every occupied unit corner lies on one of this plate's bore axes.
                        axes=np.array(part['holes'])
                        rotation=trimesh.transformations.rotation_matrix(np.radians(angle),[0,0,1])[:2,:2]
                        axes=axes@rotation.T+np.array([x,y])
                        corner=np.array([sx*(q['width_total']/2-q['corner_hole_inset']),
                                         sy*(q['height_total']/2-q['corner_hole_inset'])])
                        assert np.min(np.linalg.norm(axes-corner,axis=1))<1e-6
                        report['placements'].append(dict(piece=part['name'],rear=rear,centre_mm=[x,y],
                            rotation_degrees=angle,intersection_mm3=collision))
    report.update(all_checks_passed=True,original_hole_grid_restored=True,
        adapter_clearance_depth_mm=p['optional_joiners']['adapter_clearance_depth'],
        seating_pad_radius_mm=p['optional_joiners']['seating_pad_radius'])
    from action_validate_v7_joiner_fit import validate_hardware_and_group
    report['hardware_and_group']=validate_hardware_and_group(folder,p,bodies)
    return report


def package(folder,p):
    """Keep a named joiners folder and a portable accessory ZIP with each unit."""
    folder=Path(folder);dest=folder/'joiners';dest.mkdir(exist_ok=True)
    for suffix in ['.scad','.stl','.png']:
        shutil.copy2(folder/('joiners'+suffix),dest/('joiners'+suffix))
    for suffix in ['.scad','.stl']:
        shutil.copy2(folder/('joiner_backers'+suffix),dest/('joiner_backers'+suffix))
    for name in ['joiners_in_use.png','joiners_detail.png','joiners_backing_detail.png']:
        shutil.copy2(folder/name,dest/name)
    text='\n'.join([
        f"OPTIONAL SCREW JOINERS / {p['variant']}",
        'joiners.stl contains ONE two-unit strip (20 x 10 x 6 mm) and ONE four-unit corner plate (20 x 20 x 6 mm).',
        'Print outside faces DOWN, countersinks on the bed, raised seating pads UP. Choose quantities for your arrangement.',
        'Place on OUTSIDE faces over existing corner mounting holes, raised seating pads against the face.',
        'The 2.6 mm back recess clears current 2.4 mm screw-adapter flanges. Circular seating pads are 6 mm diameter.',
        'Two-hole strip: join two adjacent units; turn 90 degrees for vertical neighbours.',
        'Four-hole plate: join a 2 x 2 group at its shared corner.',
        'Print joiner_backers.stl for one matching two-unit and one four-unit INSIDE backing piece; nut-pocket faces DOWN, legs UP.',
        'For CURRENT 6 mm printed faces: purchased M3 x 35 countersunk screws and M3 nuts. Fit backing pieces and nuts before closing the frame.',
        'Backing pieces seat on the INSIDE face; relieved legs clear the beams. Nuts are captured 16 mm behind the inside face, past the thick beam ends.',
        'Screws stay STRAIGHT through the existing corner holes. The faceplates are unchanged.',
        'Use REVISED beams: small screw paths and short nut recesses in the thin runners are required. Beam-end locking mechanisms are unchanged.',
        'For vertical strips, rotate toward the outside edge: +90 degrees at the right edge, -90 degrees at the left edge.',
        'At the REAR use front joiners turned about Y, and backing pieces turned 180 degrees about Z; keep relieved feet clear of the runners.',
        'Each strip takes two screws/nuts; each corner plate takes four. Different sheet/backing stacks need their screw lengths checked.',
        'The in-use render uses nominal OOBB true-size hardware. Actual seating and print fit need physical testing.',
        '10 mm hole pitch assumes plastic face edges TOUCH. Spaced enclosures require changing joining_plate_unit_gap in population and regenerating.',
        'These are optional accessories; the individual unit BOM, beam hardware and print batches remain separate.',
        'joiners.scad is self-contained and reproduces this combined STL. Dimensions are mm.',
        'Print fit, screw-head seating and joining strength require physical testing.'
    ])+'\n'
    (dest/'printing.txt').write_text(text,encoding='utf-8')
    upgrade=dest/'required_beam_update';upgrade.mkdir(exist_ok=True)
    beam_batches=[name for name,batch in p['print_batches'].items() if batch['component'] in ['snap_beam','screw_beam']]
    for name in beam_batches:
        for suffix in ['.scad','.stl']:shutil.copy2(folder/(name+suffix),upgrade/(name+suffix))
    (upgrade/'printing.txt').write_text('\n'.join([
        'REQUIRED ONLY IF YOUR EXISTING BEAMS DO NOT HAVE THE JOINER CORNER CLEARANCES.',
        'Print each listed batch ONCE; replace the existing beams, retaining faces, caps, adapters and beam hardware.',
        *[f"{name}.stl: {p['print_batches'][name]['count']} x {p['print_batches'][name]['component']}" for name in beam_batches],
        'Full print_files.zip already includes these beam batches at top level. Do NOT print those and this duplicate upgrade set.',
        'Original beam-end clips, locating guides and nut bosses are unchanged. New clearance is confined to the runners.'])+'\n',encoding='utf-8')
    names=[f'joiners/{name}' for name in ['joiners.scad','joiners.stl','joiners.png',
        'joiner_backers.scad','joiner_backers.stl','joiners_in_use.png','joiners_detail.png','joiners_backing_detail.png','printing.txt']]
    names += ['joiners/'+path.relative_to(dest).as_posix() for path in upgrade.iterdir()]
    with zipfile.ZipFile(folder/'joiners.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for name in names:archive.write(folder/name,name)
    return names


def export_accessory(folder,p,logs):
    logs.mkdir(parents=True,exist_ok=True)
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    for name in ['joiners','joiner_backers','joiner_screw_reference','joiner_nut_reference']:
        result=subprocess.run([exe,'--backend=Manifold','--hardwarnings','--export-format=binstl',
            '-o',str(folder/(name+'.stl')),str(folder/(name+'.scad'))],
            capture_output=True,text=True,timeout=180)
        (logs/(name+'_export.log')).write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()
    for name,camera in [('joiners','0,0,0,35,0,25,100'),
                        ('joiners_in_use',f"{p['frame']['width_total']*3.2},-{p['frame']['width_total']*5.7},450,0,100,0"),
                        ('joiners_detail','65,-130,55,0,12,0'),
                        ('joiners_backing_detail','55,105,45,0,14,0')]:
        framing=['--viewall','--autocenter'] if name=='joiners' else []
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1400,1000','--projection=o',
            *framing,'--camera='+camera,'--colorscheme=Tomorrow',
            '-o',str(folder/(name+'.png')),str(folder/('joiners_detail.scad' if name=='joiners_backing_detail' else name+'.scad'))],
            capture_output=True,text=True,timeout=180)
        (logs/(name+'_preview.log')).write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()


def refresh_kit(folder,names):
    path=folder/'print_files.zip'
    if not path.exists():return
    replacements=['assembly.json','printing.txt',*names]
    inputs=yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details']
    p=drawing.get_ai_version_7_frame_parameters(**inputs)
    beam_views=['snap_beam','screw_beam',*[name for name,batch in p['print_batches'].items()
        if batch['component'] in ['snap_beam','screw_beam']]]
    replacements += [name+'.stl' for name in beam_views]
    temp=folder/'print_files_joiners.tmp'
    with zipfile.ZipFile(path) as source,zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as target:
        for info in source.infolist():
            if info.filename not in replacements:target.writestr(info,source.read(info))
        for name in replacements:target.write(folder/name,name)
    temp.replace(path)
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        for name in replacements:assert archive.read(name)==(folder/name).read_bytes()


def sync_navigation(folder):
    inputs=yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details']
    destination=ROOT/'navigation_oobb'
    for index in range(1,10):destination=destination/inputs['taxonomy_'+str(index)]
    if not destination.exists():return
    shutil.copytree(folder,destination,dirs_exist_ok=True)


def main(variant=None):
    out=ROOT/'validation_v7_joiner_fit';out.mkdir(exist_ok=True)
    previous=Path.cwd()
    try:
        os.chdir(ROOT)
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
            generate_stl=False,scad_navigation=False,scad_filter=variant or 'unit_',
            parts_directory=str(ROOT/'parts'))
    finally:os.chdir(previous)
    reports=[]
    from working_oomp_populate import is_current_option
    for path in sorted((ROOT/'parts').glob('*/working.yaml')):
        inputs=yaml.safe_load(path.read_text(encoding='utf-8')).get('oobb_details',{})
        if not is_current_option(inputs):continue
        if not inputs.get('optional_joiners') or (variant and inputs['variant']!=variant):continue
        active=path.parent
        p=drawing.get_ai_version_7_frame_parameters(**inputs)
        logs=out/p['variant'];logs.mkdir(exist_ok=True)
        from action_validate_v7 import export
        exe=shutil.which('openscad.com') or shutil.which('openscad')
        for name in ['snap_beam','screw_beam','3dpr','assembled',*[n for n,b in p['print_batches'].items()
                if b['component'] in ['snap_beam','screw_beam']]]:
            export(exe,active,logs,name)
        export_accessory(active,p,logs)
        report=validate(active,p)
        names=package(active,p);refresh_kit(active,names)
        report['folder']=str(active/'joiners')
        report['files']={name:hashlib.sha256((active/name).read_bytes()).hexdigest() for name in names}
        (logs/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
        reports.append(report)
        print('PASS',p['variant'],report['folder'],flush=True)
    assert len(reports)==(1 if variant else 2)
    for report in reports:sync_navigation(Path(report['folder']).parent)
    manifest_path=out/'preceding_active_manifest.json'
    if manifest_path.exists():
        manifest=json.loads(manifest_path.read_text())
        for name,digest in manifest.items():
            assert hashlib.sha256((out/'previous_current'/name).read_bytes()).hexdigest()==digest
            updated={'snap_beam','screw_beam','snap_beams','screw_beams','3dpr','assembled','beam_preview','assembly_preview'}
            if name.startswith('parts') and Path(name).suffix in ['.scad','.stl','.png'] and not Path(name).name.startswith('joiners') and Path(name).stem not in updated:
                assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('Existing production geometry changed',name)
    (out/'report.json').write_text(json.dumps(dict(units=reports,all_checks_passed=True),indent=2),encoding='utf-8')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--variant',choices=['unit_1_wide_2_tall','unit_2_wide_2_tall'])
    main(**vars(parser.parse_args()))
