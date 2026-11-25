"""Reproducible detail views of the exported finishing components."""
from pathlib import Path
import json
import shutil
import subprocess
import yaml
import working_scad as drawing

ROOT=Path(__file__).resolve().parent


def main():
    out=ROOT/'validation_v7_finishing';out.mkdir(exist_ok=True)
    folder=next((ROOT/'parts').glob('*unit_2_wide_2_tall'))
    p=drawing.get_ai_version_7_frame_parameters(**yaml.safe_load((folder/'working.yaml').read_text(encoding='utf-8'))['oobb_details'])
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    include=lambda name:'{ include <'+(folder/(name+'.scad')).as_posix()+'>; }'
    roof=p['beam_running_height'];half=p['rail_length']/2;bed=p['side_runner']['bed_x']
    matrix=[[0,0,1,bed],[0,1,0,0],[-1,0,0,0],[0,0,0,1]]
    stop=out/'upward_stop_scene.scad'
    stop.write_text(f'translate([0,{half},{-roof}]) intersection() {{\n'
        'multmatrix('+json.dumps(matrix)+') '+include('snap_beam')+'\n'
        f'translate([-4,{-half-25},{roof-3.1}]) cube([15,50,9.3]);\n}}\n',encoding='utf-8')
    joint=out/'screw_joint_scene.scad'
    transform=drawing.v7_beam_to_frame(p,dict(x=0,hole_y=0),'screw_beam')
    joint.write_text('intersection() { union() {\n'
        'color([.78,.80,.82]) '+include('receiver_6_0')+
        '\ncolor([.13,.52,.55]) multmatrix('+json.dumps(transform)+') '+include('screw_beam')+'\n'
        f'color([.92,.63,.30]) translate([0,0,{-p["screw"]["flange_size"][2]}]) '+include('screw_adapter')+'\n'
        '} translate([-12,-9,-3]) cube([12,18,23]); }\n',encoding='utf-8')
    for name,source,camera in [
        ('offset_lock_preview',folder/'front_plug.scad','25,-35,32,0,0,0'),
        ('upward_stop_preview',stop,'45,-65,40,0,0,0'),
        ('screw_joint_preview',joint,'65,-55,38,0,0,0')]:
        # Keep these as presentation references; manufacturing sources remain
        # outputs of populate -> OOMP -> SCAD.
        result=subprocess.run([exe,'--backend=Manifold','--render','--imgsize=1200,900',
            '--projection=o','--viewall','--autocenter','--camera='+camera,
            '--colorscheme=Tomorrow','-o',str(out/(name+'.png')),str(source)],
            capture_output=True,text=True,timeout=240)
        (out/(name+'.log')).write_text(result.stdout+result.stderr,encoding='utf-8')
        result.check_returncode()
    print('Rendered offset lock, upward stop and screw-joint section')


if __name__=='__main__':main()
