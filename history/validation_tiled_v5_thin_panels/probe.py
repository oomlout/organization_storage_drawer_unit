from pathlib import Path
import subprocess,shutil
import oobb
import working_oomp_populate as pop
import working_scad as draw
out=Path('validation_tiled_v5_thin_panels')
o=pop.get_ai_version_5_tiled_options()[1]
p=draw.get_ai_version_5_parameters(**o)
print({k:p[k] for k in ['plate_thickness','opening_height','rail_length','nut_near','nut_far','snap_root_distance','snap_shoulder_depth']})
for view in ['snap_rail','front','back','front_tile_02']:
 t=oobb.get_default_thing(type='thin_probe')
 draw.get_ai_version_5(t,**dict(o,connector_view=view))
 path=out/view
 oobb.opsc_make_object(str(path)+'.scad',t['components'],mode='3dpr',save_type='none',overwrite=True)
 r=subprocess.run([shutil.which('openscad.com'),'--backend=Manifold','--hardwarnings','--export-format=binstl','-o',str(path)+'.stl',str(path)+'.scad'],capture_output=True,text=True)
 print(view,r.returncode,r.stderr[-600:])
 r.check_returncode()
