"""Generate current V7 units, export and validate manufacturing meshes."""
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


def main(build_root=None,skip_generation=False,variant=None):
    build=Path(build_root).resolve() if build_root else ROOT
    build.mkdir(exist_ok=True)
    from working_oomp_populate import get_current_options
    options=get_current_options()
    if variant and variant not in {o['variant'] for o in options}:
        raise ValueError('Unknown current variant: '+variant)
    side_revision=options[0].get('beam_revision')=='side_printed_runner'
    balanced=bool(options[0].get('runner_alignment'))
    out=build/('validation_v7_balanced_runner' if balanced else 'validation_v7_side_runner' if side_revision else 'validation_current_v7');out.mkdir(exist_ok=True)
    if variant:
        out=(out/('selected_'+variant) if balanced else build/'validation_v7_2x2'
             if variant=='unit_2_wide_2_tall' else out/('selected_'+variant))
        out.mkdir(exist_ok=True)
    previous=Path.cwd()
    try:
        os.chdir(build)
        if not skip_generation:
            working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                        generate_stl=False,scad_navigation=False,scad_filter=variant or 'ai_version_7',
                        parts_directory=str(build/'parts'))
    finally:os.chdir(previous)
    folders=sorted((build/'parts').glob('*/working.yaml'))
    assert len(folders)==len(options),('Expected current population records',len(folders),len(options))
    assert len(list((build/'parts_source').glob('*/working.yaml')))==len(options)
    if variant:
        folders=[path for path in folders if yaml.safe_load(path.read_text(encoding='utf-8'))['oobb_details']['variant']==variant]
        assert len(folders)==1,('Expected one selected variant',variant)
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
                if name=='clip_reinforcements':expected=len(p['reinforcement_pads'])
                if name=='front_3mm_test_layout':expected=1+len(p['reinforcement_pads'])
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
        front=meshes['front'];back=meshes['back'].copy()
        back.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,q['assembled_depth']],[0,0,0,1]])
        # Test both interchangeable beam types at every actual receiver on both faces.
        for mount in p['frame_mounts']:
            hole=box(mount['x']-2.599,mount['hole_y']-2.599,mount['x']+2.599,mount['hole_y']+2.599)
            assert flat.intersection(hole).area<1e-6 and printed.intersection(hole).area<1e-6
            for kind in ['snap_beam','screw_beam']:
                beam=meshes[kind].copy()
                beam.apply_transform(drawing.v7_beam_to_frame(p,mount,kind))
                collision=max(overlap(face,beam) for face in [front,back])
                assert collision<.015,(p['variant'],mount,kind,collision)
                entry['mounts'].append(dict(**mount,beam_tested=kind,both_faces_clear=True,collision_mm3=collision))
        for name,profile in [('front_laser_2d',flat),('receiver_laser',section(meshes['receiver_6_0'],.1))]:
            entry['dxf'].append(check_dxf(folder/f'{name}.dxf',profile))
        if p.get('laser_face_test'):
            from action_validate_v7_3mm_front import validate
            entry['laser_face_test']=validate(folder,p,meshes)
        # Shared parts must retain the existing validated sample geometry byte-for-byte.
        archived=next((ROOT/'parts_old_1').glob('*ai_version_7_style_unit_1_wide_2_tall'))
        unchanged=['screw_adapter','receiver_6_0'] if side_revision else ['snap_beam','screw_beam','front_plug','screw_adapter','sample_71','receiver_6_0']
        for name in unchanged:
            assert (folder/f'{name}.stl').read_bytes()==(archived/f'{name}.stl').read_bytes(),(name,'shared geometry changed')
        if side_revision:
            from action_validate_v7_side_runner import validate
            entry['side_runner']=validate(folder,p,meshes)
        # Presentation sources are generated from the same geometry.
        upright=logs/'upright.scad'
        upright.write_text('rotate([-90,0,0]) { include <'+(folder/'assembled.scad').as_posix()+'>; }\n',encoding='utf-8')
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o',
            '--viewall','--autocenter','--camera=210,-330,220,0,0,0','--colorscheme=Tomorrow',
            '-o',str(folder/'assembly_preview.png'),str(upright)],capture_output=True,text=True,timeout=240)
        (logs/'preview.log').write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()
        if side_revision:
            comparison=logs/'beam_comparison.scad'
            comparison.write_text('translate([-16,0,0]) { include <'+(folder/'snap_beam.scad').as_posix()+'>; }\n'
                'translate([16,0,0]) { include <'+(folder/'screw_beam.scad').as_posix()+'>; }\n',encoding='utf-8')
            result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o',
                '--viewall','--autocenter','--camera=120,-280,170,0,0,0','--colorscheme=Tomorrow',
                '-o',str(folder/'beam_preview.png'),str(comparison)],capture_output=True,text=True,timeout=240)
            (logs/'beam_preview.log').write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()
        if p.get('laser_face_test'):
            for image_name,source,camera in [('front_3mm_preview','front_3mm_test.scad','100,-140,170,0,0,0'),
                                            ('front_3mm_layout','front_3mm_test_2d.scad','0,0,500,0,0,0')]:
                result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o',
                    '--viewall','--autocenter','--camera='+camera,'--colorscheme=Tomorrow',
                    '-o',str(folder/(image_name+'.png')),str(folder/source)],capture_output=True,text=True,timeout=240)
                (logs/(image_name+'.log')).write_text(result.stdout+result.stderr,encoding='utf-8');result.check_returncode()
        names=['front.stl','back.stl',*[n+'.stl' for n in p['print_batches']],
               'front_laser_2d.dxf','receiver_laser.dxf','assembly.json','printing.txt','assembly_preview.png']
        names += [n+'.stl' for n in ['snap_beam','screw_beam','front_plug','screw_adapter','sample_71','receiver_6_0']]
        if p.get('laser_face_test'):
            names += [name+'_2d'+suffix for name in [*p['reinforcement_types'],
                      'clip_reinforcements','front_3mm_test'] for suffix in ['.scad','.dxf']]
            # The 2D SCADs include these reproducible 3D sources.
            names += [name+'.scad' for name in [*p['reinforcement_types'],
                      'clip_reinforcements','front_3mm_test_layout','front_3mm_test']]
            names += ['front_3mm_test.stl','front_3mm_preview.png','front_3mm_layout.png']
        with zipfile.ZipFile(folder/'print_files.zip','w',zipfile.ZIP_DEFLATED) as archive:
            for name in names:archive.write(folder/name,name)
        if side_revision:
            batches=[name for name,batch in p['print_batches'].items() if batch['component'] in ['snap_beam','screw_beam','front_plug']]
            instructions=['V7 SIDE-PRINTED RUNNER REPLACEMENT KIT',
                f"{p['variant']}: {p['bom']['snap_beam']} snaps, {p['bom']['screw_beam']} screw beams, {p['bom']['front_plug']} NEW covers.",
                'Print EACH listed STL ONCE, in the supplied orientation; SCADs reproduce them.']
            instructions += [name+'.stl' for name in batches]
            instructions += [('Use revised faces from face_alignment_files.zip; these beams match the preceding kit.'
                if balanced and p['column']>1 else 'Reuse existing faces, screw adapters, screws and nuts.'),
                'NEW 9.8 x 8 mm covers are included: fit turned 90 degrees from the preceding covers.',
                'Side-load M3 nuts from the beam bed-side opening BEFORE assembling faces.',
                '8 x 3 mm runners are offset 1.5 mm; 5 mm clip slots replace the old 7 mm slots.',
                'Centre stops reach into each drawer from its left-hand beam. Keep the supplied orientation.',
                'Full-unit stiffness, narrow-side lip bearing, insertion effort and creep require physical tests.']
            (folder/'beam_replacement_printing.txt').write_text('\n'.join(instructions)+'\n',encoding='utf-8')
            replacement=['beam_replacement_printing.txt','assembly.json','beam_preview.png','assembly_preview.png']
            replacement += [name+ext for name in batches for ext in ['.stl','.scad']]
            with zipfile.ZipFile(folder/'beam_replacement_files.zip','w',zipfile.ZIP_DEFLATED) as archive:
                for name in replacement:archive.write(folder/name,name)
        if balanced and p['column']>1:
            instructions=['CENTRED SHARED RUNNERS / REVISED FACES',
                'Reuse the existing beams, friction covers, screw adapters and hardware.',
                'PRINT front.stl ONCE and back.stl ONCE, outside face DOWN, instead of the preceding faces.',
                'The printed faces are HANDED: use both different files, not two copies of front.stl.',
                'Alternatively cut front_laser_2d.dxf TWICE from measured 6 mm sheet.',
                'For flat laser faces keep their shifted holes horizontally aligned through the unit; do not mirror their hole locations.',
                'Shared-divider receiver holes move +1.5 mm in front-face CAD X; outer receivers retain their positions.',
                'The shift centres the 8 mm running strip, with nominal 2.35 mm lip bearing on each side.',
                'Optional 3 mm test: cut revised front_3mm_test_2d.dxf ONCE per face; its complete pad set is nested.',
                'Use the OFFSET-hole pads at the shared dividers; keep the pad square centred on its divider.',
                'The pad hole is +1.5 mm in front-face CAD X. Plain/handed pads are for the outer receivers.',
                'Do not also cut pads-only sets when using the nested full-face layout.',
                'Do not enlarge the preceding receiver holes to combine both locations; use the revised faces.',
                'Print fit, lateral play, loading and creep still require physical testing.']
            (folder/'face_alignment_printing.txt').write_text('\n'.join(instructions)+'\n',encoding='utf-8')
            updated=['front.stl','back.stl','front_laser_2d.dxf','assembly.json','assembly_preview.png',
                     'face_alignment_printing.txt','printing.txt']
            updated += [name+suffix for name in ['front','back','front_laser','front_laser_2d'] for suffix in ['.scad']]
            if p.get('laser_face_test'):
                updated += [n for n in names if n.startswith(('front_3mm','clip_reinforcement'))]
            with zipfile.ZipFile(folder/'face_alignment_files.zip','w',zipfile.ZIP_DEFLATED) as archive:
                for name in dict.fromkeys(updated):archive.write(folder/name,name)
        entry['all_checks_passed']=True;report.append(entry)
        (logs/'report.json').write_text(json.dumps(entry,indent=2),encoding='utf-8')
        print('PASS',p['variant'],flush=True)
    (out/'report.json').write_text(json.dumps(dict(units=report,all_checks_passed=True),indent=2),encoding='utf-8')
    # Populate navigation only after validated STL/ZIP generation.
    import scad_help
    try:
        os.chdir(build);scad_help.generate_navigation(sort=scad_help.get_navigation_sort())
    finally:os.chdir(previous)
    print(f'PASS: {len(report)} V7 unit(s) generated and validated in',build,flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--build-root');parser.add_argument('--skip-generation',action='store_true')
    parser.add_argument('--variant',help='Generate/export only this current variant; population still emits the full current catalogue.')
    main(**vars(parser.parse_args()))
