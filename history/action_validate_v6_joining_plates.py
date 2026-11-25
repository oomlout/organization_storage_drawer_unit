"""Generate both optional joiners in one STL via populate -> OOMP -> SCAD."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import numpy as np
import oobb
import trimesh
import yaml
from shapely.geometry import Point
import working
import working_scad as drawing
from action_validate_ai_version_4 import section
from action_validate_ai_version_5 import check_previous_versions
from action_validate_double_sided_v6 import snapshot


def main(skip_generation=False):
    root=Path(__file__).resolve().parent
    out=root/'validation_double_sided_v6_floor_supports/joining_plates'; out.mkdir(parents=True,exist_ok=True)
    if not skip_generation:
        working.run(run_oomp_populate=True,run_oomp=True,run_scad=True,run_action=False,
                    generate_stl=False,scad_filter='ai_version_6')
    folder=next(root.glob('parts/*ai_version_6_style*250_max'))
    baseline=json.loads((root/'validation_double_sided_v6_floor_supports/previous_v6_baseline.json').read_text())['double_sided_plywood_250_max']
    assert hashlib.sha256((folder/'joining_plates.scad').read_bytes()).hexdigest()==baseline['scad']['joining_plates.scad'],'Joining plate CAD changed'
    assert snapshot(root)==json.loads((root/'validation_double_sided_v6/previous_v5_baseline.json').read_text())
    check_previous_versions(root)
    p=drawing.get_ai_version_6_parameters(**yaml.safe_load((folder/'working.yaml').read_text())['oobb_details'])
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    result=subprocess.run([exe,'--backend=Manifold','--hardwarnings','--export-format=binstl',
        '-o',str(folder/'joining_plates.stl'),str(folder/'joining_plates.scad')],capture_output=True,text=True,timeout=180)
    (out/'export.log').write_text(result.stdout+result.stderr)
    result.check_returncode()
    mesh=trimesh.load_mesh(folder/'joining_plates.stl')
    assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0
    bodies=sorted(mesh.split(),key=lambda b:b.centroid[0])
    assert len(bodies)==2 and np.allclose(mesh.extents,[45,20,6],atol=.015)
    shaft=oobb.gv('hole_radius_m3','3dpr')
    head=oobb.gv('screw_countersunk_radius_m3','3dpr')
    depth=oobb.gv('screw_countersunk_depth_m3','3dpr')
    report={'checks':[],'file':str(folder/'joining_plates.stl'),'joining_plate_cad_unchanged':True}
    for body,part in zip(bodies,p['joining_plates']):
        assert np.allclose(body.extents,part['size'],atol=.015)
        assert abs(body.bounds[0,2])<.001 and abs(body.bounds[1,2]-6)<.001
        for z in [.1,6-depth-.1,6-depth/2,5.9]:
            cross=section(body,z)
            assert cross.geom_type=='Polygon' and len(cross.interiors)==len(part['holes'])
            radius=shaft if z<=6-depth else shaft+(head-shaft)*(z-(6-depth))/depth
            for hx,hy in part['holes']:
                x=hx+part['print_center'][0]; y=hy+part['print_center'][1]
                assert not cross.intersects(Point(x,y).buffer(radius-.04)),(part['name'],'blocked hole',z)
                assert cross.contains(Point(x+radius+.12,y)),(part['name'],'oversize countersink',z)
        # Both pieces have only a bed-supported flat underside; holes flare upward.
        down=(body.face_normals[:,2]<-.9)&(body.triangles[:,:,2].max(axis=1)>.05)
        assert not np.any(down),'Unsupported underside'
        report['checks'].append(dict(name=part['name'],size_mm=part['size'],holes=len(part['holes']),
            countersink_top_diameter_mm=2*head,countersink_depth_mm=depth,through_diameter_mm=2*shaft,passed=True))
    # Screw axes coincide with the existing cabinet corner-hole grid.
    inset=p['corner_hole_inset']
    assert p['joining_plate_unit_gap']==0
    assert p['joining_plates'][0]['holes']==[[x,y] for x in [-inset,inset] for y in [-inset,inset]]
    # A 20 mm joiner ends inside the 10.5 mm side borders; drawer openings stay clear.
    assert max(p['joining_plates'][0]['size'][:2])/2 < p['drawer_border_edge']
    result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1400,900','--projection=o',
        '--viewall','--autocenter','--camera=0,0,0,35,0,25,100','--colorscheme=Tomorrow',
        '-o',str(folder/'joining_plates.png'),str(folder/'joining_plates.scad')],capture_output=True,text=True,timeout=180)
    result.check_returncode()
    report.update(all_checks_passed=True,total_bodies=2,total_countersunk_holes=6,
                  assumption='Plastic unit face edges touch; 10 mm corner-hole pitch. Add source gap for spaced plywood boxes.',
                  limitations='PETG fit, screw-head seating and joint strength require physical testing.')
    (out/'report.json').write_text(json.dumps(report,indent=2))
    print('PASS: both joiners in one STL; six countersinks; joining plate and earlier release CAD unchanged',flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--skip-generation',action='store_true')
    main(parser.parse_args().skip_generation)
