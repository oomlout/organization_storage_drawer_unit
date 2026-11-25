"""V7 output metadata and flat DXF sources, called by the ordinary SCAD stage."""
import csv
import json
from pathlib import Path
import shutil
import subprocess
import ezdxf
import oobb
import working_scad as drawing


def views(p):
    result={f"sample_{t['sample_number']}":{} for t in p['trials']}
    result.update(receiver_6_0={},receiver_5_8={'receiver_print_thickness':5.8},
                  receiver_6_2={'receiver_print_thickness':6.2},
                  screw_test={},screw_beam={},screw_adapter={})
    result.update({f'front_{size}_{kind}':{} for size in ['small','large']
                   for kind in ['printed','laser']})
    return result


def export_dxfs(folder,sources):
    """Laser deliverables are emitted by the responsible SCAD stage itself."""
    exe=shutil.which('openscad.com') or shutil.which('openscad')
    if not exe:
        raise RuntimeError('OpenSCAD is required to generate the V7 laser DXFs')
    for name in sources:
        result=subprocess.run([exe,'--backend=Manifold','--hardwarnings',
            '-o',str(folder/f'{name}.dxf'),str(folder/f'{name}.scad')],
            capture_output=True,text=True,timeout=240)
        (folder/f'{name}_export.log').write_text(result.stdout+result.stderr,encoding='utf-8')
        result.check_returncode()
        doc=ezdxf.readfile(folder/f'{name}.dxf')
        # OpenSCAD omits units in its legacy DXF header. Use a standard version
        # that supports explicit mm units and its closed lightweight polylines.
        doc.dxfversion='AC1024';doc.units=4;doc.header['$MEASUREMENT']=1
        if 'CUT' not in doc.layers:doc.layers.new('CUT',dxfattribs={'color':1})
        for entity in doc.modelspace():entity.dxf.layer='CUT'
        doc.saveas(folder/f'{name}.dxf')


def write_outputs(folder,thing,kwargs,save_type,overwrite):
    folder=Path(folder)
    p=drawing.get_ai_version_7_parameters(**kwargs)
    thing['ai_files']={'3dpr':thing['ai_design']}
    for name,extra in views(p).items():
        sub=oobb.get_default_thing(type='v7_test_view')
        drawing.get_ai_version_7(sub,**dict(kwargs,connector_view=name,**extra))
        oobb.opsc_make_object(str(folder/f'{name}.scad'),sub['components'],mode='3dpr',
                             save_type=save_type,overwrite=overwrite)
        thing['ai_files'][name]=sub['ai_design']
    # Pure projected contours: no pockets, countersinks, text or duplicate lines.
    # MDF card uses the bottom section of its printed counterpart, below labels.
    sources={'receiver_laser':'receiver_6_0',
             'front_small_laser_2d':'front_small_laser',
             'front_large_laser_2d':'front_large_laser'}
    for name,source in sources.items():
        (folder/f'{name}.scad').write_text(
            ('projection(cut=true) translate([0,0,-0.1]) '
             if name=='receiver_laser' else 'projection(cut=false) ')
            + '{ include <'+source+'.scad>; }\n',encoding='utf-8')
    export_dxfs(folder,sources)
    (folder/'connector_test.json').write_text(json.dumps(dict(
        version=7,experimental=True,panel_material='6 mm nominal MDF',
        nominal_hole_mm=[p['receiver_hole_width'],p['receiver_hole_height']],
        nominal_side_clearance_mm=p['side_clearance'],retaining_overlap_mm=p['retention_overlap'],
        trials=p['trials'],screw=p['screw'],
        thickness_note='Measure actual sheet; 5.8 / 6.0 / 6.2 mm printed cards check sensitivity.',
        projection_note='DXF is nominal finished contour in mm; compensate measured kerf once in CAM.',
        adoption='Test coupons only; no full V7 rail selected. Prototype face files await physical testing.'
    ),indent=2),encoding='utf-8')
    fields=['sample_number','arm_thickness','axial_clearance','spring_length','root_radius',
            'tip_y','strain_proxy','stiffness_proxy']
    with (folder/'trial_index.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore')
        writer.writeheader(); writer.writerows(p['trials'])
    # Never erase the user's observations during a rebuild.
    if not (folder/'results.csv').exists():
        with (folder/'results.csv').open('w',newline='') as stream:
            writer=csv.writer(stream)
            writer.writerow(['sample_number','receiver_material','measured_thickness_mm','hole_width_mm',
                'insertion_effort','clicked','side_play','axial_play','release_effort','cycles','damage','preferred','notes'])
            writer.writerows([[t['sample_number']]+['']*12 for t in p['trials']])
    (folder/'printing.txt').write_text(
        'V7 EXPERIMENTAL THROUGH-PANEL CLIPS — 6 mm MDF — dimensions in mm\n\n'
        'PRINT FIRST: 3dpr.stl once (nine separate numbered clips 40–48), receiver_6_0.stl once,\n'
        'and screw_test.stl once (beam end + outside adapter). Do not connect parts with a raft.\n'
        'Optional receiver_5_8.stl and receiver_6_2.stl simulate sheet variation. sample_*.stl are spares.\n'
        'Keep all supplied orientations. Clips lie long-face-down; numbers UP; no designed supports.\n'
        'Use the production PETG, ideally 0.4 mm nozzle, 0.2 mm layers; record your actual settings.\n'
        'Start with sample 44 in the CENTRE 7.6 x 4.6 hole; then compare 41 and 47 (softer/stiffer).\n'
        '40–42: 1.2 mm arms; 43–45: 1.5 mm; 46–48: 1.8 mm. Within each row axial play is\n'
        '0.10 / 0.25 / 0.40 mm for a true 6.00 mm sheet. These are CAD values, not measured fit.\n'
        'Insert from the unlabelled back of the receiver; hooks emerge on the labelled outside.\n'
        'The broad beam shoulder seats on the inside; squeeze both exposed hooks to remove.\n'
        'Holes left-to-right: 7.2, 7.4, 7.6, 7.8, 8.0 mm; all 4.6 mm high. Printed labels show widths.\n'
        'Record insertion, play, removal, damage and repeat-cycle behaviour in results.csv.\n'
        'Test thickness variation separately: thin panels add play; thick panels can prevent clicking.\n\n'
        'LASER: receiver_laser.dxf is a 126 x 32 mm test card in nominal 6 mm MDF. No engraving\n'
        'is required: mark hole widths by hand using receiver_map.svg. DXF has CUT contours only,\n'
        'all at Z=0, mm units. Use measured kerf compensation ONCE in CAM and cut holes first.\n'
        'Measure actual sheet thickness and hole width on both faces before comparing to prints.\n\n'
        'SCREW: M3 x 20 countersunk screw + M3 nut, one each (not included). Side-load the nut\n'
        'into the beam; put the adapter from OUTSIDE through the SAME centre receiver hole;\n'
        'beam seats INSIDE. Adapter countersink face prints DOWN, cheeks UP. Screw is entered\n'
        'through the adapter into the nut. Flange adds 2.4 mm outside; tighten gently for this test.\n\n'
        'PROTOTYPE FACES: front_small/large_laser_2d.dxf are complete nominal flat MDF faces.\n'
        'Their stops are solid across the 6 mm sheet. front_small/large_printed.stl retain the V6\n'
        'angled slide-on stop and 12 mm inward floor supports, with the new rectangular holes.\n'
        'These demonstrate the two manufacturing paths; NO full-length V7 rail is selected yet.\n'
        'The flat MDF version has no inward floor extensions; plywood/enclosure support remains\n'
        'necessary. Do not mix these receiver holes with V6 rails. Test coupons before full faces.\n'
        'Analytical strain and stiffness are screening proxies; insertion force, fatigue, MDF edge\n'
        'durability, PETG creep and loaded cabinet performance require physical testing.\n',encoding='utf-8')
    labels=''.join(f'<rect x="{15+i*48-w}" y="30.8" width="{2*w}" height="9.2" fill="white" stroke="black"/>'
                   f'<text x="{15+i*48}" y="23" text-anchor="middle">{w:.1f}</text>'
                   for i,w in enumerate(p['receiver_hole_widths']))
    (folder/'receiver_map.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="756" height="240" viewBox="-20 0 270 85">'
        '<rect x="-15" y="3" width="252" height="64" rx="4" fill="#eee" stroke="black"/>'
        '<g font-family="Arial" font-size="7">'+labels+
        '<text x="110" y="58" text-anchor="middle">All holes 4.6 mm high; centre is nominal</text>'
        '<text x="110" y="80" text-anchor="middle">V7 receiver — printed or 6 mm MDF</text></g></svg>',encoding='utf-8')
