"""Check two push-in cap styles, exact quantities and actual assembly placement."""
from pathlib import Path
import numpy as np
import trimesh
from action_validate_ai_version_5 import overlap
from action_validate_v7_finishing import external_part,run_envelopes
from action_validate_v7_permanent_snap import region_clip

ROOT=Path(__file__).resolve().parent


def validate(folder,p,meshes):
    previous=ROOT/'validation_v7_caps/previous_current/parts'/Path(folder).name
    for name in ['front','back','front_laser','snap_beam','screw_beam','front_plug','screw_adapter',
                 'sample_71','receiver_6_0','front_3mm_test','front_3mm_test_layout',
                 *p['reinforcement_types'],'clip_reinforcements']:
        if p.get('optional_joiners') and name in ['snap_beam','screw_beam']:
            continue  # Later joiner revision independently verifies end mechanisms.
        assert (previous/f'{name}.stl').read_bytes()==(Path(folder)/f'{name}.stl').read_bytes(),(name,'cap revision changed existing part')
    square=meshes['front_plug_square'];relieved=meshes['front_plug']
    assert square.volume>relieved.volume+1,'Square cap lacks restored corners'
    assert abs(relieved.difference(square,engine='manifold').volume)<.002,'Square cap loses existing material'
    stem_lo=[-10,-10,p['front_plug']['cup_depth']+.01];stem_hi=[10,10,p['front_plug']['stem_depth']+.1]
    a=region_clip(square,stem_lo,stem_hi);b=region_clip(relieved,stem_lo,stem_hi)
    assert abs(a.difference(b,engine='manifold').volume)+abs(b.difference(a,engine='manifold').volume)<.002,'Cap stem changed'
    quantities={name:sum(b['count'] for b in p['print_batches'].values() if b['component']==name)
                for name in p['cap_quantities']}
    assert quantities==p['cap_quantities'] and quantities['front_plug']==4
    assert sum(quantities.values())==2*p['bom']['snap_beam']
    report=dict(quantities=quantities,placement=[],same_stem=True,square_added_volume_mm3=float(square.volume-relieved.volume))
    pipes=run_envelopes(p);actual={name:0 for name in quantities}
    for mount in p['frame_mounts']:
        if mount['kind']!='snap_beam':continue
        for rear in [False,True]:
            name=mount['cap_component'];actual[name]+=1
            part=external_part(meshes[name],p,mount,'snap_beam',rear)
            path_max=0;head_max=0
            for tube in pipes:
                if np.any(np.minimum(part.bounds[1],tube.bounds[1])-np.maximum(part.bounds[0],tube.bounds[0])<1e-5):continue
                path_max=max(path_max,overlap(part,tube))
            for corner in p['frame']['corner_holes']:
                head=trimesh.creation.cylinder(radius=3,height=3,sections=32)
                head.apply_translation([corner['x'],corner['y'],p['frame']['assembled_depth']+1.5 if rear else -1.5])
                head_max=max(head_max,overlap(part,head))
            assert path_max<.015 and head_max<.015,(name,mount,rear,path_max,head_max)
            report['placement'].append(dict(x=mount['x'],hole_y=mount['hole_y'],rear=rear,cap=name,
                                          drawer_intrusion_mm3=path_max,head_intersection_mm3=head_max))
    assert actual==quantities,(actual,quantities,'Assembly cap count')
    report['all_checks_passed']=True
    return report
