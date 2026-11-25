"""Check actual beam shortening while retaining both complete end mechanisms."""
from pathlib import Path
import numpy as np
import trimesh
from action_validate_v7_side_runner import to_service
from action_validate_v7_permanent_snap import region_clip

ROOT=Path(__file__).resolve().parent


def validate(folder,p,meshes):
    previous=ROOT/'validation_v7_shorter_beams/previous_current/parts'/Path(folder).name
    reduction=2*p['beam_depth_reduction_per_end'];length=p['rail_length']
    report=dict(reduction_per_end_mm=reduction/2,total_reduction_mm=reduction,
                rail_between_faces_mm=length,frame_depth_mm=p['frame']['assembled_depth'],beams=[])
    for name in ['front','back','front_laser','front_plug','screw_adapter','sample_71','receiver_6_0',
                 'front_3mm_test','front_3mm_test_layout',*p['reinforcement_types'],'clip_reinforcements']:
        assert (previous/f'{name}.stl').read_bytes()==(Path(folder)/f'{name}.stl').read_bytes(),(name,'unchanged part')
    for name in ['snap_beam','screw_beam']:
        old=to_service(trimesh.load_mesh(previous/f'{name}.stl'),p)
        new=to_service(meshes[name],p)
        assert abs(old.extents[1]-new.extents[1]-reduction)<.0002,(name,'actual shortening')
        # Compare full end mechanisms in the same local coordinates at BOTH ends.
        differences=[]
        for rear in [False,True]:
            prior=old.copy();current=new.copy()
            if rear:
                prior.apply_translation([0,length+reduction,0]);current.apply_translation([0,length,0])
            bounds=([-30,-12,-20],[30,20,40]) if not rear else ([-30,-20,-20],[30,12,40])
            if p.get('optional_joiners'):
                axis=p['tongue_height']/2 if name=='snap_beam' else p['screw']['axis_height']
                # New corner screw paths affect only the roof above all end
                # mechanisms. Include the complete clip or 12 mm screw boss.
                bounds=(bounds[0],[30,bounds[1][1],axis+6.1])
            a=region_clip(prior,*bounds);b=region_clip(current,*bounds)
            difference=a.difference(b,engine='manifold').volume+b.difference(a,engine='manifold').volume
            assert abs(difference)<.002,(name,rear,'end mechanism changed',difference)
            differences.append(float(difference))
        assert np.allclose(old.extents[[0,2]],new.extents[[0,2]],atol=.0002)
        report['beams'].append(dict(beam=name,old_length_mm=float(old.extents[1]),
            new_length_mm=float(new.extents[1]),end_difference_mm3=differences))
    report['all_checks_passed']=True
    return report
