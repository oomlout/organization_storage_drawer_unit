"""Upward stops, half-depth screw joints and centred offset front locks."""
from pathlib import Path
import numpy as np
import trimesh
import oobb
import working_scad as drawing
from action_validate_v7_side_runner import to_service
from action_validate_v7_permanent_snap import region_clip
from action_validate_ai_version_5 import overlap,moved


def external_part(mesh,p,mount,kind,rear):
    part=mesh.copy()
    part.apply_transform(trimesh.transformations.euler_matrix(
        *np.radians(drawing.v7_external_part_rotation(p,kind,rear))))
    extension=(p['front_plug']['outer_y']-p['panel_thickness'] if kind=='snap_beam'
               else p['screw']['flange_size'][2])
    part.apply_translation([mount['x'],mount['hole_y'],
        p['frame']['assembled_depth']+extension if rear else -extension])
    return part


def run_envelopes(p):
    """Conservative configured lip/body passage, swept through both ends."""
    q=p['frame'];result=[];depth=q['assembled_depth']+40
    for row in range(p['row']):
        y=q['opening_origin_y']+row*q['pitch_y']
        for col in range(p['column']):
            x=-q['width_total']/2+q['drawer_border_edge']+q['opening_width']/2+col*q['pitch_x']
            for width,height in [(q['opening_width'],q['depth_lip']),
                                 (q['opening_width']-2*q['inset_lip'],q['opening_height'])]:
                tube=trimesh.creation.box(extents=[width,height,depth])
                tube.apply_translation([x,y+height/2,q['assembled_depth']/2]);result.append(tube)
    return result


def validate(folder,p,meshes):
    r=p['side_runner'];s=p['screw'];q=p['frame'];length=p['rail_length']
    report=dict(stops=[],screw_joint=[],locks=[],drawer_paths=[],corner_heads_clear=True)
    for kind,axis in [('snap_beam',p['tongue_height']/2),('screw_beam',s['axis_height'])]:
        native=to_service(meshes[kind],p);roof=axis+8;centre=-length/2
        upper=region_clip(native,[r['stop_min_x']-.1,centre-1.4,roof+.01],
                          [r['stop_max_x']+.1,centre+1.4,roof+r['stop_height']+.1])
        assert not upper.is_empty and abs(upper.bounds[1,2]-roof-6)<.0002,(kind,'stop must rise 6 mm')
        assert abs(upper.extents[0]-(r['stop_max_x']-r['stop_min_x']))<.0002
        below=region_clip(native,[r['stop_min_x']-.1,centre-1.4,roof-10],
                          [r['stop_max_x']+.1,centre+1.4,roof-r['thickness']-.01])
        assert below.is_empty or abs(below.volume)<.001,(kind,'old downward stop remains')
        report['stops'].append(dict(beam=kind,height_above_runner_mm=float(upper.bounds[1,2]-roof),
            below_runner_extension=False))
    native=to_service(meshes['screw_beam'],p)
    adapter_depth=float(meshes['screw_adapter'].bounds[1,2]-s['flange_size'][2])
    assert abs(adapter_depth-s['adapter_engagement'])<.0002
    for rear in [False,True]:
        local=native.copy()
        if rear:local.apply_transform([[1,0,0,0],[0,-1,0,-length],[0,0,-1,2*s['axis_height']],[0,0,0,1]])
        tongue=region_clip(local,[-s['beam_guide_width']/2-.1,.001,s['axis_height']-s['beam_guide_height']/2-.1],
            [s['beam_guide_width']/2+.1,s['beam_engagement']+.1,s['axis_height']+s['beam_guide_height']/2+.1])
        depth=float(tongue.bounds[1,1]);gap=p['panel_thickness']-depth-adapter_depth
        assert abs(depth-s['beam_engagement'])<.0002 and abs(gap-s['mating_clearance'])<.0002
        assert abs(tongue.extents[0]-s['beam_guide_width'])<.0002
        assert abs(tongue.extents[2]-s['beam_guide_height'])<.0002
        report['screw_joint'].append(dict(rear=rear,nominal_beam_mm=s['beam_receiver_depth'],
            nominal_adapter_mm=s['guide_depth'],actual_beam_mm=depth,actual_adapter_mm=adapter_depth,
            mating_gap_mm=gap))
    shank=trimesh.creation.cylinder(radius=s['bore_radius']-.04,height=s['length'],sections=48)
    shank.apply_translation([0,0,s['length']/2])
    assert overlap(meshes['screw_adapter'],shank)<.02,'Adapter shank path is blocked'
    hr=oobb.gv('screw_countersunk_radius_m3','3dpr')-.04
    hd=oobb.gv('screw_countersunk_depth_m3','3dpr')
    head=trimesh.creation.revolve([[0,.02],[hr,.02],[s['bore_radius']-.04,hd-.02],[0,hd-.02]],sections=48)
    assert overlap(meshes['screw_adapter'],head)<.02,'Countersink head path is blocked'
    assert overlap(meshes['screw_adapter'],moved(head,[0,0,.3]))>.02,'No screw head seating stop'
    cover=meshes['front_plug']
    assert abs(cover.bounds[:,1].mean()-p['front_plug']['cover_offset_y'])<.0002
    # fn=50 misses the Y extrema of each R0.75 corner by ~0.0015 mm.
    assert abs(cover.extents[1]-p['front_plug']['cover_height'])<.004
    pipes=run_envelopes(p)
    for mount in p['frame_mounts']:
        for kind,name in [('snap_beam','front_plug'),('screw_beam','screw_adapter')]:
            for rear in [False,True]:
                part=external_part(meshes[name],p,mount,kind,rear)
                maximum=0.0
                for tube in pipes:
                    if np.any(np.minimum(part.bounds[1],tube.bounds[1])-np.maximum(part.bounds[0],tube.bounds[0])<1e-5):continue
                    maximum=max(maximum,overlap(part,tube))
                assert maximum<.015,(mount,kind,rear,'Outside fitting obstructs drawer run',maximum)
                report['drawer_paths'].append(dict(**mount,beam=kind,rear=rear,intrusion_mm3=maximum))
                if kind=='snap_beam':
                    centre=float(part.bounds[:,0].mean());runner=mount['x']-r['offset_x']
                    assert abs(centre-runner)<.0002,(mount,rear,'Cover not centred on runner')
                    report['locks'].append(dict(**mount,rear=rear,cover_centre_x=centre,runner_centre_x=runner))
                for corner in q['corner_holes']:
                    head=trimesh.creation.cylinder(radius=3,height=3,sections=32)
                    head.apply_translation([corner['x'],corner['y'],q['assembled_depth']+1.5 if rear else -1.5])
                    assert overlap(part,head)<.015,(mount,kind,rear,'Corner head blocked')
    report.update(all_checks_passed=True,offset_cover_mm=p['front_plug']['cover_offset_y'],
        minimum_rim_wall_mm=p['front_plug']['minimum_rim_wall'],adapter_head_path_clear=True,
        limitations='CAD clearance only: measured sheet/bondline, print fit, force, loading and creep need physical tests.')
    return report
