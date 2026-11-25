"""Generate the three active V7 units, export and validate manufacturing meshes."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import zipfile
import numpy as np
import trimesh
import yaml
from shapely.geometry import box
import working
import working_scad as drawing
from working_scad_v7 import views
from action_validate_v7 import export,check_dxf
from action_validate_ai_version_5 import section,overlap

ROOT=Path(__file__).resolve().parent


def main(build_root=None,skip_generation=False):
    build=Path(build_root).resolve() if build_root else ROOT
    build.mkdir(exist_ok=True)
    out=build/'validation_current_v7';out.mkdir(exist_ok=True)
    previous=Path.cwd()
    try:
        os.chdir(build)
        if not skip_generation:
            working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                        generate_stl=False,scad_navigation=False,parts_directory=str(build/'parts'))
    finally:os.chdir(previous)
    folders=sorted((build/'parts').glob('*/working.yaml'))
    assert len(folders)==3,('Expected exactly three active units',len(folders))
    assert len(list((build/'parts_source').glob('*/working.yaml')))==3
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    report=[]
    for path in folders:
        folder=path.parent
        inputs=yaml.safe_load(path.read_text(encoding='utf-8'))['oobb_details']
        assert inputs['style']=='ai_version_7' and inputs['part_role']=='frame'
        p=drawing.get_ai_version_7_frame_parameters(**inputs);q=p['frame']
        logs=out/p['variant'];logs.mkdir(exist_ok=True)
        entry=dict(variant=p['variant'],grid=[p['column'],p['row']],drawer_count=q['drawer_count'],
                   bom=p['bom'],meshes=[],mounts=[],dxf=[])
        meshes={}
        for name in ['3dpr',*views(p)]:
            print('Exporting',p['variant'],name,flush=True)
            export(exe,folder,logs,name)
            mesh=trimesh.load_mesh(folder/f'{name}.stl');meshes[name]=mesh
            assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,(p['variant'],name,'closed mesh')
            pieces=list(mesh.split(only_watertight=False))
            if name!='assembled':
                expected=(2+3*(p['bom']['snap_beam']+p['bom']['screw_beam']) if name=='3dpr'
                          else p['print_batches'].get(name,{}).get('count',1))
                assert len(pieces)==expected,(p['variant'],name,len(pieces),expected)
                assert all(abs(part.bounds[0,2])<.001 for part in pieces),(name,'bed contact')
            if name not in ['assembled','3dpr']:
                assert mesh.extents[0]<=q['bed_width']-2*q['bed_margin']+.001,(name,'bed width')
                assert mesh.extents[1]<=q['bed_height']-2*q['bed_margin']+.001,(name,'bed height')
            entry['meshes'].append(dict(view=name,bodies=len(pieces),extents_mm=mesh.extents.tolist(),volume_mm3=float(mesh.volume)))
        for name,batch in p['print_batches'].items():
            assert abs(meshes[name].volume-batch['count']*meshes[batch['component']].volume)<.5,(name,'batch volume')
        kit=meshes['front'].volume+meshes['back'].volume+sum(meshes[n].volume for n in p['print_batches'])
        assert abs(meshes['3dpr'].volume-kit)<1,'Overview contains duplicates or overlaps'
        assert abs(meshes['front'].volume-meshes['back'].volume)<1e-6
        assert abs(meshes['assembled'].volume-kit)<3,'Assembly intersections or missing parts'
        flat=section(meshes['front_laser'],.1)
        assert abs(meshes['front_laser'].extents[2]-6)<.001
        printed=section(meshes['front'],.1)
        front=meshes['front'];back=front.copy()
        back.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,q['assembled_depth']],[0,0,0,1]])
        # Test both interchangeable beam types at every actual receiver on both faces.
        for mount in p['frame_mounts']:
            hole=box(mount['x']-2.599,mount['hole_y']-2.599,mount['x']+2.599,mount['hole_y']+2.599)
            assert flat.intersection(hole).area<1e-6 and printed.intersection(hole).area<1e-6
            for kind in ['snap_beam','screw_beam']:
                beam=meshes[kind].copy()
                axis=p['tongue_height']/2 if kind=='snap_beam' else p['screw']['axis_height']
                beam.apply_transform([[-1,0,0,mount['x']],[0,0,-1,mount['hole_y']+axis],
                                      [0,-1,0,p['panel_thickness']],[0,0,0,1]])
                collision=max(overlap(face,beam) for face in [front,back])
                assert collision<.015,(p['variant'],mount,kind,collision)
                entry['mounts'].append(dict(**mount,beam_tested=kind,both_faces_clear=True,collision_mm3=collision))
        for name,profile in [('front_laser_2d',flat),('receiver_laser',section(meshes['receiver_6_0'],.1))]:
            entry['dxf'].append(check_dxf(folder/f'{name}.dxf',profile))
        # Shared parts must retain the existing validated sample geometry byte-for-byte.
        archived=next((ROOT/'parts_old_1').glob('*ai_version_7_style_unit_1_wide_2_tall'))
        for name in ['snap_beam','screw_beam','front_plug','screw_adapter','sample_71','receiver_6_0']:
            assert (folder/f'{name}.stl').read_bytes()==(archived/f'{name}.stl').read_bytes(),(name,'shared geometry changed')
        # Presentation sources are generated from the same geometry.
        upright=logs/'upright.scad'
        upright.write_text('rotate([-90,0,0]) { include <'+(folder/'assembled.scad').as_posix()+'>; }\n',encoding='utf-8')
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o',
            '--viewall','--autocenter','--camera=210,-330,220,0,0,0','--colorscheme=Tomorrow',
            '-o',str(folder/'assembly_preview.png'),str(upright)],capture_output=True,text=True,timeout=240)
        (logs/'preview.log').write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()
        names=['front.stl','back.stl',*[n+'.stl' for n in p['print_batches']],
               'front_laser_2d.dxf','receiver_laser.dxf','assembly.json','printing.txt','assembly_preview.png']
        names += [n+'.stl' for n in ['snap_beam','screw_beam','front_plug','screw_adapter','sample_71','receiver_6_0']]
        with zipfile.ZipFile(folder/'print_files.zip','w',zipfile.ZIP_DEFLATED) as archive:
            for name in names:archive.write(folder/name,name)
        entry['all_checks_passed']=True;report.append(entry)
        (logs/'report.json').write_text(json.dumps(entry,indent=2),encoding='utf-8')
        print('PASS',p['variant'],flush=True)
    (out/'report.json').write_text(json.dumps(dict(units=report,all_checks_passed=True),indent=2),encoding='utf-8')
    # Populate navigation only after validated STL/ZIP generation.
    import scad_help
    try:
        os.chdir(build);scad_help.generate_navigation(sort=scad_help.get_navigation_sort())
    finally:os.chdir(previous)
    print('PASS: three V7 units generated and validated in',build,flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--build-root');parser.add_argument('--skip-generation',action='store_true')
    main(**vars(parser.parse_args()))
