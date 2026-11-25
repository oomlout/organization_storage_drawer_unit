"""Restore optional V7 joiners through populate -> OOMP -> SCAD.

Use an isolated build, then install validated accessories into current parts.
Existing manufacturing geometry must remain byte-identical.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
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
    shaft=oobb.gv('hole_radius_m3','3dpr')
    head=oobb.gv('screw_countersunk_radius_m3','3dpr')
    depth=oobb.gv('screw_countersunk_depth_m3','3dpr')
    report=dict(variant=p['variant'],pieces=[],placements=[])
    q=p['frame']
    for body,part in zip(bodies,p['joiners']):
        assert np.allclose(body.extents,part['size'],atol=.015)
        assert abs(body.bounds[0,2])<.001 and abs(body.bounds[1,2]-6)<.001
        for z in [.1,depth/2,depth+.1,5.9]:
            cross=section(body,z)
            polygons=list(cross.geoms) if cross.geom_type=='MultiPolygon' else [cross]
            assert sum(len(poly.interiors) for poly in polygons)==len(part['holes'])
            radius=shaft if z>=depth else head-(head-shaft)*z/depth
            for hx,hy in part['holes']:
                x=hx+part['print_center'][0];y=hy+part['print_center'][1]
                assert not cross.intersects(Point(x,y).buffer(radius-.04)),('Blocked hole',part['name'],z)
                assert cross.contains(Point(x+radius+.12,y)),('Oversize countersink',part['name'],z)
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
    return report


def package(folder,p):
    """Keep a named joiners folder and a portable accessory ZIP with each unit."""
    folder=Path(folder);dest=folder/'joiners';dest.mkdir(exist_ok=True)
    for suffix in ['.scad','.stl','.png']:
        shutil.copy2(folder/('joiners'+suffix),dest/('joiners'+suffix))
    text='\n'.join([
        f"OPTIONAL SCREW JOINERS / {p['variant']}",
        'joiners.stl contains ONE two-unit strip (20 x 10 x 6 mm) and ONE four-unit corner plate (20 x 20 x 6 mm).',
        'Print outside faces DOWN, countersinks on the bed, raised seating pads UP. Choose quantities for your arrangement.',
        'Place on OUTSIDE faces over existing corner mounting holes, raised seating pads against the face.',
        'The 2.6 mm back recess clears current 2.4 mm screw-adapter flanges. Circular seating pads are 6 mm diameter.',
        'Two-hole strip: join two adjacent units; turn 90 degrees for vertical neighbours.',
        'Four-hole plate: join a 2 x 2 group at its shared corner.',
        'Use M3 countersunk screws with suitable backing/nuts. Each strip takes two screws; each corner plate takes four.',
        'Screw length depends on the 6 mm joiner, face thickness, backing/washers and nut engagement; screws are purchased separately.',
        '10 mm hole pitch assumes plastic face edges TOUCH. Spaced enclosures require changing joining_plate_unit_gap in population and regenerating.',
        'These are optional accessories; the individual unit BOM, beam hardware and print batches remain separate.',
        'joiners.scad is self-contained and reproduces this combined STL. Dimensions are mm.',
        'Print fit, screw-head seating and joining strength require physical testing.'
    ])+'\n'
    (dest/'printing.txt').write_text(text,encoding='utf-8')
    names=[f'joiners/{name}' for name in ['joiners.scad','joiners.stl','joiners.png','printing.txt']]
    with zipfile.ZipFile(folder/'joiners.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for name in names:archive.write(folder/name,name)
    return names


def export_accessory(folder,p,logs):
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    for args,log in [(['--hardwarnings','--export-format=binstl','-o',str(folder/'joiners.stl')],'export.log'),
                     (['--render','--imgsize=1000,700','--projection=o','--viewall','--autocenter',
                       '--camera=0,0,0,35,0,25,100','--colorscheme=Tomorrow','-o',str(folder/'joiners.png')],'preview.log')]:
        result=subprocess.run([exe,'--backend=Manifold',*args,str(folder/'joiners.scad')],
            capture_output=True,text=True,timeout=180)
        (logs/log).write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()


def refresh_kit(folder,names):
    path=folder/'print_files.zip'
    if not path.exists():return
    replacements=['assembly.json','printing.txt',*names]
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
    shutil.copytree(folder/'joiners',destination/'joiners',dirs_exist_ok=True)
    for name in ['joiners.scad','joiners.stl','joiners.png','joiners.zip',
                 'assembly.json','printing.txt','print_files.zip','working.yaml']:
        shutil.copy2(folder/name,destination/name)


def main(variant=None):
    out=ROOT/'validation_v7_joiners';out.mkdir(exist_ok=True)
    # OpenSCAD cannot open some nested taxonomy paths at MAX_PATH on Windows.
    with tempfile.TemporaryDirectory(prefix='v7j_') as location:
        return build_and_install(out,Path(location),variant)


def build_and_install(out,build,variant):
    previous=Path.cwd()
    try:
        os.chdir(build)
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
            generate_stl=False,scad_navigation=False,scad_filter=variant or 'unit_',
            parts_directory=str(build/'parts'))
    finally:os.chdir(previous)
    reports=[]
    for path in sorted((build/'parts').glob('*/working.yaml')):
        inputs=yaml.safe_load(path.read_text(encoding='utf-8'))['oobb_details']
        if not inputs.get('optional_joiners') or (variant and inputs['variant']!=variant):continue
        generated=path.parent;active=ROOT/'parts'/generated.name
        assert active.exists(),active
        p=drawing.get_ai_version_7_frame_parameters(**inputs)
        logs=out/p['variant'];logs.mkdir(exist_ok=True)
        # Only new accessory views may alter manufacturing geometry.
        unchanged=[]
        for source in generated.glob('*.scad'):
            if source.name=='joiners.scad':continue
            target=active/source.name
            assert target.read_bytes()==source.read_bytes(),('Existing geometry changed',source.name)
            unchanged.append(source.name)
        assert unchanged,'SCAD stage did not generate the manufacturing sources'
        export_accessory(generated,p,logs)
        # Fit checks use preceding actual production meshes, never mirrored stand-ins.
        for source in active.glob('*.stl'):shutil.copy2(source,generated/source.name)
        report=validate(generated,p)
        for name in ['joiners.scad','joiners.stl','joiners.png','assembly.json','printing.txt']:
            shutil.copy2(generated/name,active/name)
        source=build/'parts_source'/generated.name
        for path in source.iterdir():
            if path.is_file():shutil.copy2(path,ROOT/'parts_source'/generated.name/path.name)
        names=package(active,p);refresh_kit(active,names)
        report['unchanged_manufacturing_scads']=unchanged
        report['folder']=str(active/'joiners')
        report['files']={name:hashlib.sha256((active/name).read_bytes()).hexdigest() for name in names}
        (logs/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
        reports.append(report)
        print('PASS',p['variant'],report['folder'],flush=True)
    assert len(reports)==(1 if variant else 2)
    # Publish generated source records through OOMP, keeping temporary build
    # paths out of the active YAML. Geometry has already passed SCAD checks.
    import working_oomp
    try:
        os.chdir(ROOT)
        working_oomp.main(parts_directory=str(ROOT/'parts'))
    finally:os.chdir(previous)
    for report in reports:sync_navigation(Path(report['folder']).parent)
    manifest_path=out/'preceding_active_manifest.json'
    if manifest_path.exists():
        manifest=json.loads(manifest_path.read_text())
        for name,digest in manifest.items():
            assert hashlib.sha256((out/'previous_current'/name).read_bytes()).hexdigest()==digest
            if name.startswith('parts') and Path(name).suffix in ['.scad','.stl','.png']:
                assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,('Existing production geometry changed',name)
    (out/'report.json').write_text(json.dumps(dict(units=reports,all_checks_passed=True),indent=2),encoding='utf-8')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--variant',choices=['unit_1_wide_2_tall','unit_2_wide_2_tall'])
    main(**vars(parser.parse_args()))
