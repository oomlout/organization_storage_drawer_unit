"""Independent actual-mesh checks for OOBB hardware and complete joined groups."""
import itertools
import numpy as np
import trimesh
from action_validate_ai_version_5 import overlap,section
from action_validate_v7_finishing import run_envelopes
import working_scad as drawing


def moved(mesh,shift,angle=0,rear=False,tilt=0,roll=0,flip_axis='x'):
    result=mesh.copy()
    rotation=(trimesh.transformations.euler_matrix(0,0,np.radians(angle))@
        trimesh.transformations.euler_matrix(np.pi if rear and flip_axis=='x' else 0,
            np.pi if rear and flip_axis=='y' else 0,0)@
        trimesh.transformations.euler_matrix(np.radians(tilt),0,0)@
        trimesh.transformations.euler_matrix(0,0,np.radians(roll)))
    result.apply_transform(rotation)
    result.apply_translation(shift)
    return result


def validate_hardware_and_group(folder,p,bodies):
    screw=trimesh.load_mesh(folder/'joiner_screw_reference.stl')
    nut=trimesh.load_mesh(folder/'joiner_nut_reference.stl')
    unit=trimesh.load_mesh(folder/'assembled.stl')
    for name,mesh in [('screw',screw),('nut',nut)]:
        assert mesh.is_watertight and mesh.is_winding_consistent and len(mesh.split())==1,(name,'closed hardware')
    q=p['frame'];j=p['optional_joiners'];thickness=j['joining_plate_thickness']
    assert abs(screw.extents[2]-j['screw_length'])<.001
    assert abs(nut.extents[2]-2.5)<.001
    local=[]
    for body,part in zip(bodies,p['joiners']):
        local.append(moved(body,-np.array(part['print_center'])))
    backing_mesh=trimesh.load_mesh(folder/'joiner_backers.stl')
    assert backing_mesh.is_watertight and backing_mesh.is_winding_consistent
    backing_bodies=sorted(backing_mesh.split(),key=lambda body:body.centroid[0])
    assert len(backing_bodies)==2
    assert abs(backing_mesh.extents[2]-j['backer_depth'])<.001
    backers=[moved(body,-np.array(part['print_center'])) for body,part in zip(backing_bodies,p['joiners'])]
    layout=drawing.v7_joiner_layout(p)
    units=[moved(unit,xy) for xy in layout['units']]
    pipes=[moved(tube,xy) for xy in layout['units'] for tube in run_envelopes(p)]
    for a,b in itertools.combinations(units,2):
        assert overlap(a,b)<.02,'Neighbouring complete units interfere'
    report=dict(hardware=[],joiners=[],group_units=4,unit_intersections_clear=True,
        reference_screw_length_mm=float(screw.extents[2]),reference_nut_thickness_mm=float(nut.extents[2]),
        adapter_gap_mm=j['adapter_clearance_depth']-p['screw']['flange_size'][2])
    # Axis locations are derived independently from the actual unit envelopes
    # and corner-hole grid, rather than accepting a joiner placement as proof.
    corner_axes=np.array([[xy[0]+c['x'],xy[1]+c['y']] for xy in layout['units'] for c in q['corner_holes']])
    for rear in [False,True]:
        for placement in layout['joiners']:
            index=placement['part'];part=p['joiners'][index];x,y,_=placement['centre'];angle=placement['angle']
            z=q['assembled_depth']+thickness if rear else -thickness
            joiner=moved(local[index],[x,y,z],angle,rear,flip_axis='y')
            end=p['panel_thickness']+j['backer_depth']
            backer=moved(backers[index],[x,y,q['assembled_depth']-end if rear else end],angle+180 if rear else angle,not rear)
            collision=max(overlap(joiner,other) for other in [*units,*pipes])
            assert collision<.02,('Joiner/group interference',p['variant'],rear,placement,collision)
            backing_collision=max(overlap(backer,other) for other in [joiner,*units,*pipes])
            assert backing_collision<.02,('Backer/group interference',p['variant'],rear,placement,backing_collision)
            foot_plane=q['assembled_depth']-p['panel_thickness']-.01 if rear else p['panel_thickness']+.01
            face_plane=q['assembled_depth']-p['panel_thickness']+.01 if rear else p['panel_thickness']-.01
            feet=section(backer,foot_plane)
            bearing=sum(feet.intersection(section(other,face_plane)).area for other in units)
            assert bearing>5*len(part['holes']),('Backing feet lack face support',rear,placement,bearing)
            report['joiners'].append(dict(piece=part['name'],rear=rear,centre_mm=[x,y],
                rotation_degrees=angle,intersection_mm3=collision,backer_intersection_mm3=backing_collision,
                backing_foot_contact_mm2=float(bearing)))
            a=np.radians(angle)
            for hx,hy in part['holes']:
                px=x+hx*np.cos(a)-hy*np.sin(a);py=y+hx*np.sin(a)+hy*np.cos(a)
                assert np.min(np.linalg.norm(corner_axes-[px,py],axis=1))<1e-6,'Screw axis misses face corner hole'
                tilt=j['screw_angle']
                tangent=np.tan(np.radians(j['screw_angle']))
                head_front=-thickness+j['screw_reference_recess'];nut_front=end-j['nut_recess']
                def hardware(mesh,front_z,roll=0):
                    yy=hy-tangent*(front_z-p['panel_thickness']/2)
                    xx,yy=x+hx*np.cos(a)-yy*np.sin(a),y+hx*np.sin(a)+yy*np.cos(a)
                    return moved(mesh,[xx,yy,q['assembled_depth']-front_z if rear else front_z],angle,rear,tilt,roll,flip_axis='y')
                fastener=hardware(screw,head_front)
                backing=hardware(nut,nut_front)
                screw_collision=max(overlap(fastener,other) for other in [joiner,backer,*units,*pipes])
                nut_collision=max(overlap(backing,other) for other in [joiner,backer,*units,*pipes,fastener])
                assert screw_collision<.02,('Screw/head obstruction',rear,px,py,screw_collision)
                assert nut_collision<.02,('Nut obstruction',rear,px,py,nut_collision)
                turned=hardware(nut,nut_front,30)
                assert overlap(turned,backer)>.01,'Nut pocket does not resist rotation'
                axis=(trimesh.transformations.euler_matrix(0,0,a)@
                    trimesh.transformations.euler_matrix(0,np.pi if rear else 0,0)@
                    trimesh.transformations.euler_matrix(np.radians(tilt),0,0))[:3,2]
                for travel in [4,16]:
                    insertion=moved(fastener,-travel*axis)
                    assert max(overlap(insertion,other) for other in [joiner,backer,*units])<.02,'Blocked outside screw insertion'
                # These positive controls ensure the collision tests actually
                # catch a wrong axis and an over-driven countersunk head.
                displaced=moved(fastener,[1.2,0,0])
                assert overlap(displaced,joiner)>.1,'Wrong-axis control did not collide'
                deeper=moved(fastener,.8*axis)
                assert overlap(deeper,joiner)>.01,'Over-insertion control did not collide'
                protrusion=j['screw_length']-(nut_front-head_front)/np.cos(np.radians(j['screw_angle']))-nut.extents[2]
                assert protrusion>=1,'Insufficient nut engagement'
                # At the mating plane each pad has a real annular bearing area
                # on one of the ACTUAL production faceplates.
                plane=q['assembled_depth']+.01 if rear else -.01
                land=section(joiner,plane)
                panel_plane=q['assembled_depth']-.01 if rear else .01
                face_area=sum(land.intersection(section(other,panel_plane)).area for other in units)
                assert face_area>15*len(part['holes']),('Insufficient pad contact',face_area)
                report['hardware'].append(dict(rear=rear,axis_mm=[float(px),float(py)],
                    screw_intersection_mm3=screw_collision,nut_intersection_mm3=nut_collision,
                    nominal_tip_beyond_nut_mm=float(protrusion),pad_contact_total_mm2=float(face_area),
                    insertion_clear=True,wrong_axis_rejected=True,over_insertion_rejected=True,nut_rotation_rejected=True))
    report['all_checks_passed']=True
    return report
