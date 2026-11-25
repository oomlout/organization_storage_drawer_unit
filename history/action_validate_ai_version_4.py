"""Export modular v4 from its source pipeline and check parts, layouts and joints."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import numpy as np
import trimesh
import yaml
from shapely.geometry import Point, Polygon
import working
import working_scad as drawing
import scad_help


def section(mesh, z):
    result = mesh.section(plane_origin=[0,0,z], plane_normal=[0,0,1])
    shape = Polygon()
    if result is not None:
        for loop in result.discrete:
            shape = shape.symmetric_difference(Polygon(loop[:,:2]))
    return shape


def overlap(a,b):
    mesh = trimesh.boolean.intersection([a,b],engine='manifold')
    return 0.0 if mesh.is_empty else abs(float(mesh.volume))


def rail_local(mesh,p):
    result=mesh.copy()
    result.apply_transform([[1,0,0,0],[0,0,1,0],[0,-1,0,p['rail_length']/2],[0,0,0,1]])
    return result


def main(skip_generation=False):
    root=Path(__file__).resolve().parent
    assert Path.cwd().resolve()==root
    out=root/'validation_ai_version_4'; out.mkdir(exist_ok=True)
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,generate_stl=False)
    for v in [1,2,3]:
        __import__(f'action_check_version_{v}_lock').main()
    report={'meshes':[],'assemblies':[], 'limitations':[
        'CAD checks do not establish physical nut fit, drawer clearance, guide deflection, stiffness or print success.',
        'Rail screw bores and lateral nut entries require short bridges; overhang=True is passed to OOBB.',
        'The complete kit overview can exceed one bed; individual faces and numbered rail plates are bed checked.']}
    for path in sorted((root/'parts').glob('*ai_version_4_style*/working.yaml')):
        part=yaml.safe_load(path.read_text(encoding='utf-8')); folder=path.parent
        p=drawing.get_ai_version_4_parameters(**part['oobb_details'])
        views={'3dpr':'print_layout',**drawing.get_ai_version_4_views(p)}
        models={}; summaries={}; cache={}
        for name,view in views.items():
            print(f'Validating {folder.name}/{name}',flush=True)
            src=folder/f'{name}.scad'; dst=folder/f'{name}.stl'
            digest=hashlib.sha256(src.read_bytes()).hexdigest()
            if digest in cache:
                shutil.copy2(cache[digest],dst)
            else:
                r=subprocess.run([exe,'--backend=Manifold','--hardwarnings','--export-format=binstl','-o',str(dst),str(src)],capture_output=True,text=True,timeout=600)
                (folder/f'validation_{name}_openscad.log').write_text(r.stdout+r.stderr,encoding='utf-8'); r.check_returncode()
                cache[digest]=dst
            mesh=trimesh.load_mesh(dst,process=True); models[name]=mesh
            t=__import__('oobb').get_default_thing(type='validation_summary')
            drawing.get_ai_version_4(t,**dict(part['oobb_details'],modular_view=view))
            summary=t['ai_design']; summaries[name]=summary
            printable=summary['printable']
            bodies=[b for b in mesh.split(only_watertight=False) if b.volume>0.001]
            checks={'watertight':bool(mesh.is_watertight),'consistent_winding':bool(mesh.is_winding_consistent),
                    'positive_volume':bool(mesh.volume>0)}
            if printable:
                checks['expected_body_count']=len(bodies)==summary['expected_bodies']
                checks['all_bodies_on_bed']=all(abs(b.bounds[0,2])<0.01 for b in bodies)
                if name!='3dpr' or p['part_role']=='face_fit':
                    checks['fits_declared_bed']=bool(mesh.extents[0]+2*p['bed_margin']<=p['bed_width']+0.03 and mesh.extents[1]+2*p['bed_margin']<=p['bed_height']+0.03 and mesh.extents[2]<=p.get('build_height',float('inf')))
                bad=(mesh.face_normals[:,2]<-0.708)&(mesh.triangles[:,:,2].max(axis=1)>0.05)
                if view in ['face_plate','front','back'] or p['part_role']=='face_fit':
                    checks['plate_has_no_unexpected_overhangs']=float(mesh.area_faces[bad].sum())<0.02
                if view in ['rail','bottom_rail']:
                    centres=mesh.triangles_center
                    ends=np.abs(centres[:,1])>=p['rail_length']/2-p['rail_end_band']
                    checks['bridges_localized_to_end_hardware']=float(mesh.area_faces[bad & ~ends].sum())<0.02
            row={'id':part['id'],'file':name,'checks':checks,'volume_mm3':float(mesh.volume),'bounds_mm':mesh.bounds.tolist(),'design':summary}
            report['meshes'].append(row)
            (folder/f'validation_{name}.json').write_text(json.dumps(row,indent=2),encoding='utf-8')
        checks={}
        plate=models['face_plate']
        checks['outer_plate_grid_and_mounts_connected']=len([b for b in plate.split(only_watertight=False) if b.volume>0.001])==1
        head=section(plate,0.25); seat=section(plate,2.5); key=section(plate,p['plate_thickness']+1)
        checks['countersinks_and_key_walls_present']=all(
            not head.contains(Point(r['x']+3.2,r['y']+5)) and seat.contains(Point(r['x']+2.5,r['y']+5))
            and key.contains(Point(r['x']+3,r['y']+3)) for r in p['rail_positions'])
        if p['part_role']!='modular_test':
            outer=section(plate,3); inner=section(plate,p['plate_thickness']+p['inner_guide_depth']/2)
            checks['both_catch_ramps_present']=True
            rear_outer=section(models['back'],3)
            rear_inner=section(models['back'],p['plate_thickness']+p['inner_guide_depth']/2)
            checks['rear_opening_has_no_catch']=True
            lips=[]
            for row in range(p['row']):
                for col in range(p['column']):
                    x=-p['width_total']/2+p['drawer_border_edge']+p['opening_width']/2+col*p['pitch_x']
                    y=-p['height_total']/2+p['drawer_border_edge']+row*p['pitch_y']
                    checks['both_catch_ramps_present'] &= all(s.contains(Point(x,y+2.8)) and not s.contains(Point(x,y+3.2)) for s in [outer,inner])
                    checks['rear_opening_has_no_catch'] &= all(not s.contains(Point(x,y+2.8)) for s in [rear_outer,rear_inner])
                    profile=[[-p['thickness_wall'],0],[0,0],
                             [p['catch_tab_height'],p['catch_tab_ramp_depth']],
                             [p['catch_tab_height'],p['plate_thickness']],
                             [0,p['plate_thickness']+p['inner_guide_depth']],
                             [-p['thickness_wall'],p['plate_thickness']]]
                    lips.append(trimesh.convex.convex_hull([
                        [x+dx,y+dy,z] for dx in [-p['catch_tab_width']/2,p['catch_tab_width']/2]
                        for dy,z in profile]))
            # Compare geometry, accounting for the root's overlap with the
            # rounded plate surface rather than assuming a rectangular root.
            expected_front=trimesh.boolean.union(
                [models['back'],trimesh.util.concatenate(lips)],engine='manifold')
            unmatched=plate.volume+expected_front.volume-2*overlap(plate,expected_front)
            checks['only_catch_volume_removed_from_rear']=abs(unmatched)<0.1
        checks['face_plate_alias_is_front']=(folder/'front.scad').read_bytes()==(folder/'face_plate.scad').read_bytes()
        back_key=section(models['back'],p['plate_thickness']+1)
        back_head=section(models['back'],0.25); back_seat=section(models['back'],2.5)
        checks['rear_mounts_preserved']=all(
            not back_head.contains(Point(r['x']+3.2,r['y']+5)) and back_seat.contains(Point(r['x']+2.5,r['y']+5))
            and back_key.contains(Point(r['x']+3,r['y']+3)) for r in p['rail_positions'])
        if p['part_role']!='face_fit':
            checks['correct_front_back_geometry']=(
                ((folder/'front.scad').read_bytes()==(folder/'back.scad').read_bytes()) == (p['part_role']=='modular_test'))
            rear=models['back'].copy(); rear.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,p['assembled_depth']],[0,0,0,1]])
            local={kind:rail_local(models[kind],p) for kind in ['rail','bottom_rail']}
            checks['nuts_insert_from_side']=True; checks['nut_slot_retains_roof_and_opposite_wall']=True
            for kind,rail in local.items():
                for z in [p['nut_near']+p['nut_depth']/2,p['rail_length']-p['nut_far']+p['nut_depth']/2]:
                    shape=section(rail,z)
                    sign=1 if p['nut_side_clearance']=='left' else -1
                    checks['nut_slot_retains_roof_and_opposite_wall'] &= shape.contains(Point(-sign*(p['rail_width']/2-0.3),5)) and shape.contains(Point(0,9.5)) and shape.contains(Point(0,0.5))
                    for x in [0,1.5,3,6,9]:
                        nut=trimesh.creation.cylinder(radius=3.175,height=2.4,sections=6)
                        nut.apply_translation([sign*x,5,z])
                        checks['nuts_insert_from_side'] &= overlap(rail,nut)<0.01
            pieces=[plate,rear]; max_collision=0.0; shift_collision=0.0
            for r in p['rail_positions']:
                rail=local[r['kind']].copy(); rail.apply_translation([r['x'],r['y'],p['plate_thickness']]); pieces.append(rail)
                max_collision=max(max_collision,overlap(rail,plate),overlap(rail,rear))
                if shift_collision==0:
                    moved=rail.copy(); moved.apply_translation([0.6,0,0]); shift_collision=overlap(moved,plate)
            expected=sum(m.volume for m in pieces)
            checks['no_plate_rail_interference']=max_collision<0.02
            checks['keys_resist_sideways_shift']=shift_collision>0.1
            checks['assembled_contains_exact_bom']=abs(models['assembled'].volume-expected)<0.15
            checks['kit_contains_exact_bom']=abs(models['3dpr'].volume-expected)<0.15
            rail_batches=sum(m.volume for n,m in models.items() if n.startswith('rails_plate_'))
            checks['rail_batches_contain_exact_bom']=abs(rail_batches-(expected-plate.volume-rear.volume))<0.15
        report['assemblies'].append({'id':part['id'],'checks':{k:bool(v) for k,v in checks.items()},'bom':p['bom']})
        scene=folder/'preview_scene.scad'; scene.write_text('include <3dpr.scad>;\n',encoding='utf-8')
        r=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900','--projection=o','--viewall','--camera=150,-200,230,0,0,0','--colorscheme=Tomorrow','-o',str(folder/'preview.png'),str(scene)],capture_output=True,text=True,timeout=600); r.check_returncode()
    report['all_checks_passed']=all(all(row['checks'].values()) for row in report['meshes']+report['assemblies'])
    (out/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    scad_help.generate_navigation(sort=scad_help.get_navigation_sort(oobb_style=False))
    print(json.dumps({'meshes':len(report['meshes']),'assemblies':len(report['assemblies']),'all_checks_passed':report['all_checks_passed']}),flush=True)
    if not report['all_checks_passed']:
        failures=[(r['id'],r.get('file','assembly'),[k for k,v in r['checks'].items() if not v]) for r in report['meshes']+report['assemblies'] if not all(r['checks'].values())]
        print(json.dumps(failures,indent=2)); raise RuntimeError('Modular validation failed')


if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--skip-generation',action='store_true')
    main(parser.parse_args().skip_generation)
