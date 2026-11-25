"""Independent actual-mesh checks for OOBB hardware and complete joined groups."""
import itertools
import numpy as np
import trimesh
from action_validate_ai_version_5 import overlap,section
from action_validate_v7_finishing import run_envelopes,external_part
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
    alternate=trimesh.load_mesh(folder/'joiners_clasp_clearance.stl')
    pieces=sorted(alternate.split(),key=lambda mesh:mesh.centroid[0])
    assert alternate.is_volume and len(pieces)==2
    relieved=[moved(body,-np.array(part['print_center'])) for body,part in zip(pieces,p['joiners'])]
    backing_mesh=trimesh.load_mesh(folder/'joiner_backers.stl')
    assert backing_mesh.is_watertight and backing_mesh.is_winding_consistent
    backing_bodies=sorted(backing_mesh.split(),key=lambda body:body.centroid[0])
    assert len(backing_bodies)==2
    assert abs(backing_mesh.extents[2]-j['backer_depth'])<.001
    backers=[moved(body,-np.array(part['print_center'])) for body,part in zip(backing_bodies,p['joiners'])]
    layout=drawing.v7_joiner_layout(p)
    units=[moved(unit,xy) for xy in layout['units']]
    pipes=[moved(tube,xy) for xy in layout['units'] for tube in run_envelopes(p)]
    # Exercise the interchangeable snap assembly in the top screw receivers.
    # The normal assembled mesh only contains screw beams at those positions.
    snap=trimesh.load_mesh(folder/'snap_beam.stl')
    cap=trimesh.load_mesh(folder/'front_plug_square.stl')
    from action_validate_v7_permanent_snap import region_clip
    beam_screw=region_clip(screw,[-4,-4,-.1],[4,4,p['screw']['length']])
    alternates=[]
    mount_hardware=[]
    for mount in p['frame_mounts']:
        if mount['kind']!='screw_beam':continue
        beam=snap.copy();beam.apply_transform(drawing.v7_beam_to_frame(p,mount,'snap_beam'))
        fixtures=[beam]+[external_part(cap,p,mount,'snap_beam',rear) for rear in [False,True]]
        for rear in [False,True]:
            for mesh,z in [(beam_screw,-p['screw']['flange_size'][2]+.55),
                           (nut,p['panel_thickness']+p['screw']['nut_near'])]:
                z=q['assembled_depth']-z if rear else z
                mount_hardware.extend(moved(mesh,[xy[0]+mount['x'],xy[1]+mount['hole_y'],z],
                                            rear=rear,flip_axis='y') for xy in layout['units'])
        alternates.extend(moved(mesh,xy) for xy in layout['units'] for mesh in fixtures)
    for a,b in itertools.combinations(units,2):
        assert overlap(a,b)<.02,'Neighbouring complete units interfere'
    report=dict(hardware=[],joiners=[],group_units=4,unit_intersections_clear=True,
        reference_screw_length_mm=float(screw.extents[2]),reference_nut_thickness_mm=float(nut.extents[2]),
        adapter_gap_mm=j['beam_clearance'])
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
            # Assemble from the open frame interior. Offset above the rail,
            # approach the inside face, then lower into its transverse nut relief.
            roi=trimesh.creation.box(extents=[40,60,65])
            roi.apply_translation([x,y,q['assembled_depth']-20 if rear else 20])
            nearby=[other.intersection(roi,engine='manifold') for other in units]
            nearby=[mesh for mesh in nearby if not mesh.is_empty]
            motion=[(0,-8,d*(-1 if rear else 1)) for d in np.arange(20,-.1,-1)]
            motion += [(0,dy,0) for dy in np.arange(-7.5,.1,.5)]
            for candidate in mount_hardware:
                if np.any(candidate.bounds[1]<roi.bounds[0]) or np.any(candidate.bounds[0]>roi.bounds[1]):continue
                assert overlap(joiner,candidate)<.02,'Bracket blocks the installed beam fastener'
                nearby.append(candidate)
            for candidate in alternates:
                if np.any(candidate.bounds[1]<roi.bounds[0]) or np.any(candidate.bounds[0]>roi.bounds[1]):continue
                fixture=candidate.intersection(roi,engine='manifold')
                if not fixture.is_empty:nearby.append(fixture)
            clasp_plate=moved(relieved[index],[x,y,z],angle,rear,flip_axis='y')
            assert max(overlap(clasp_plate,mesh) for mesh in nearby)<.02,('Swap-in clasp obstructs joiner',rear,placement)
            def check_approach(mesh):
                peak=0.
                for step in motion:
                    trial=moved(mesh,step)
                    for other in nearby:
                        if np.any(np.minimum(trial.bounds[1],other.bounds[1])-np.maximum(trial.bounds[0],other.bounds[0])<.0001):continue
                        peak=max(peak,overlap(trial,other))
                assert peak<.02,('Backer installation path',rear,placement,peak)
                return peak
            report['joiners'][-1]['approach_peak_mm3']=check_approach(backer)
            a=np.radians(angle)
            for hx,hy in part['holes']:
                px=x+hx*np.cos(a)-hy*np.sin(a);py=y+hx*np.sin(a)+hy*np.cos(a)
                assert np.min(np.linalg.norm(corner_axes-[px,py],axis=1))<1e-6,'Screw axis misses face corner hole'
                head_front=-thickness+j['screw_reference_recess'];nut_front=end-j['nut_recess']
                def hardware(mesh,front_z,roll=0):
                    return moved(mesh,[px,py,q['assembled_depth']-front_z if rear else front_z],
                                 angle,rear,roll=roll,flip_axis='y')
                fastener=hardware(screw,head_front)
                assert overlap(fastener,clasp_plate)<.02 and overlap(hardware(screw,head_front+.8),clasp_plate)>.01,'Alternate front head seat'
                backing=hardware(nut,nut_front)
                screw_collision=max(overlap(fastener,other) for other in [joiner,backer,*units,*pipes])
                nut_collision=max(overlap(backing,other) for other in [joiner,backer,*units,*pipes,fastener])
                assert screw_collision<.02,('Screw/head obstruction',rear,px,py,screw_collision)
                assert nut_collision<.02,('Nut obstruction',rear,px,py,nut_collision)
                assert max(overlap(fastener,mesh) for mesh in nearby)<.02,'Shank clashes with alternate clasp'
                check_approach(backing)
                for step in np.arange(0,5,.25):
                    loose=hardware(nut,nut_front+step)
                    assert overlap(loose,backer)<.02,('Nut entry blocked',rear,placement)
                pressed=hardware(nut,nut_front-.25)
                seat_bearing=overlap(pressed,backer)/.25
                assert seat_bearing>2,('Nut seat lacks bearing',rear,placement)
                turned=hardware(nut,nut_front,30)
                assert overlap(turned,backer)>.01,'Nut pocket does not resist rotation'
                axis=np.array([0,0,-1 if rear else 1])
                for travel in [4,16]:
                    insertion=moved(fastener,-travel*axis)
                    assert max(overlap(insertion,other) for other in [joiner,backer,*units])<.02,'Blocked outside screw insertion'
                # These positive controls ensure the collision tests actually
                # catch a wrong axis and an over-driven countersunk head.
                displaced=moved(fastener,[1.2,0,0])
                assert overlap(displaced,joiner)>.1,'Wrong-axis control did not collide'
                deeper=moved(fastener,.8*axis)
                assert overlap(deeper,joiner)>.01,'Over-insertion control did not collide'
                protrusion=j['screw_length']-(nut_front-head_front)-nut.extents[2]
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
                    nut_seat_bearing_mm2=seat_bearing,alternate_clasp_clear=True,preloaded_approach_clear=True,
                    nominal_tip_beyond_nut_mm=float(protrusion),pad_contact_total_mm2=float(face_area),
                    insertion_clear=True,wrong_axis_rejected=True,over_insertion_rejected=True,nut_rotation_rejected=True))
    report['all_checks_passed']=True
    return report
