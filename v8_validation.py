"""Mesh-based manufacturing checks for the current double-sided frames and joiners."""
import itertools

import ezdxf
import numpy as np
import trimesh
import oobb
from shapely.affinity import translate
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import linemerge, unary_union
import working_scad as drawing

def section(mesh, z):
    result = mesh.section(plane_origin=[0,0,z], plane_normal=[0,0,1])
    shape = Polygon()
    if result is not None:
        for loop in result.discrete:
            shape = shape.symmetric_difference(Polygon(loop[:,:2]))
    return shape

def overlap(a,b):
    mesh = trimesh.boolean.intersection([a,b],engine='manifold')
    if mesh.is_empty or np.any(mesh.extents < 1e-8):
        return 0.0
    with np.errstate(divide='ignore', invalid='ignore'):
        return abs(float(mesh.volume))

def region_clip(mesh,lo,hi):
    lo,hi=np.asarray(lo),np.asarray(hi)
    cutter=trimesh.creation.box(extents=hi-lo);cutter.apply_translation((lo+hi)/2)
    return trimesh.boolean.intersection([mesh,cutter],engine='manifold')

def external_part(mesh,p,mount,kind,rear):
    part=mesh.copy()
    part.apply_transform(trimesh.transformations.euler_matrix(
        *np.radians(drawing.v8_external_part_rotation(p,kind,rear))))
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

def check_dxf(path,profile):
    doc=ezdxf.readfile(path)
    assert doc.units==4, 'DXF must declare millimetres'
    audit=doc.audit()
    assert not audit.has_errors and not audit.fixes, 'DXF requires structural repair'
    lines=[]
    for entity in doc.modelspace():
        assert entity.dxf.layer=='CUT'
        if entity.dxftype()=='LINE':
            start,end=entity.dxf.start,entity.dxf.end
            assert abs(start.z)<1e-8 and abs(end.z)<1e-8
            lines.append(LineString([(start.x,start.y),(end.x,end.y)]))
        elif entity.dxftype()=='LWPOLYLINE':
            assert entity.closed and abs(entity.dxf.elevation)<1e-8
            points=list(entity.get_points())
            assert all(abs(point[4])<1e-8 for point in points), 'Unexpected curved DXF segment'
            for a,b in zip(points,points[1:]+points[:1]):
                lines.append(LineString([(a[0],a[1]),(b[0],b[1])]))
        else:
            raise AssertionError((path.name,'unexpected entity',entity.dxftype()))
    assert len(set(line.wkb for line in lines))==len(lines), 'Duplicate DXF lines'
    merged=linemerge(unary_union(lines))
    rings=list(merged.geoms) if hasattr(merged,'geoms') else [merged]
    region=Polygon()
    for ring in rings:
        assert ring.is_ring, (path.name,'open DXF contour')
        region=region.symmetric_difference(Polygon(ring.coords))
    # OpenSCAD's DXF writer rounds coordinates to six significant digits.
    # Compare boundaries within 1.1 microns, rather than accumulating an
    # absolute area error across the many metres of cabinet cut contour.
    contour_error=region.boundary.hausdorff_distance(profile.boundary)
    assert contour_error<.0011,(path.name,'DXF / flat mesh mismatch',contour_error)
    assert region.symmetric_difference(profile).area<profile.length*.0011
    return dict(file=path.name,closed_contours=len(rings),units='mm',layer='CUT',
                area_mm2=region.area,profile_difference_mm2=region.symmetric_difference(profile).area,
                maximum_contour_difference_mm=contour_error)

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

def installed_cap_outlines(cap, p, layout, rear):
    """Use the largest production clip cap at every interchangeable receiver."""
    outlines = []
    for mount in p['frame_mounts']:
        mesh = external_part(cap, p, mount, 'snap_beam', rear)
        # Z grows inward at the front and outward at the rear.
        surface = mesh.bounds[1 if rear else 0, 2]
        face = p['frame']['assembled_depth'] if rear else 0
        profile = section(mesh, surface + (-.1 if rear else .1))
        for x, y, _ in layout['units']:
            outlines.append((translate(profile, x, y), abs(surface - face)))
    return outlines


def check_cap_pocket(plate, outlines, face, rear, side_gap, axial_gap):
    """Measure the first solid over the cap and sweep the outside insertion path."""
    direction = 1 if rear else -1
    levels = np.unique(np.round((plate.vertices[:, 2] - face) * direction, 5))
    roof = section(plate, face + direction * (levels[-1] - .1))
    nearby = [(shape, height) for shape, height in outlines if shape.intersection(roof).area > .01]
    if not nearby:
        return []
    # The recesses have vertical walls. Include their actual horizontal
    # transitions and the requested clearance limit as independent probes.
    samples = []
    for shape, height in nearby:
        top = height + axial_gap
        extent = shape.buffer(side_gap - .015)
        boundaries = sorted({0., top, *(float(z) for z in levels if 0 < z < top)})
        for lower, upper in zip(boundaries, boundaries[1:]):
            if upper - lower < .001:
                continue
            solid = section(plate, face + direction * ((lower + upper) / 2))
            assert solid.intersection(extent).area < .004, 'Clip cannot enter the pocket with the specified clearance'
        # Find the first real roof over the cap, excluding the screw bores.
        for lower, upper in zip(levels, levels[1:]):
            if upper - lower < .001:
                continue
            solid = section(plate, face + direction * ((lower + upper) / 2))
            if solid.intersection(shape).area > .01:
                gap = float(lower - height)
                assert gap >= axial_gap - .015, ('Roof fouls installed cap', gap, axial_gap)
                samples.append(gap)
                break
        else:
            raise AssertionError('Clip pocket is open through the visible face')
    return samples


def validate_hardware_and_group(folder,frame_folder,p):
    bodies=sorted(trimesh.load_mesh(folder/"joiners.stl").split(),key=lambda body:body.centroid[0])
    screw=trimesh.load_mesh(folder/'joiner_screw_reference.stl')
    nut=trimesh.load_mesh(folder/'joiner_nut_reference.stl')
    unit=trimesh.load_mesh(frame_folder/'assembled.stl')
    for name,mesh in [('screw',screw),('nut',nut)]:
        assert mesh.is_watertight and mesh.is_winding_consistent and len(mesh.split())==1,(name,'closed hardware')
    q=p['frame'];j=p['corner_fixing'];thickness=j['joining_plate_thickness']
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
    layout=drawing.v8_joiner_layout(p)
    units=[moved(unit,xy) for xy in layout['units']]
    pipes=[moved(tube,xy) for xy in layout['units'] for tube in run_envelopes(p)]
    # Exercise the interchangeable snap assembly in the top screw receivers.
    # The normal assembled mesh only contains screw beams at those positions.
    snap=trimesh.load_mesh(frame_folder/'snap_beam.stl')
    cap=trimesh.load_mesh(frame_folder/'front_plug_square.stl')
    beam_screw=region_clip(screw,[-4,-4,-.1],[4,4,p['screw']['length']])
    alternates=[]
    mount_hardware=[]
    for mount in p['frame_mounts']:
        if mount['kind']!='screw_beam':continue
        beam=snap.copy();beam.apply_transform(drawing.v8_beam_to_frame(p,mount,'snap_beam'))
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
        face = q['assembled_depth'] if rear else 0
        outlines = installed_cap_outlines(cap, p, layout, rear)
        all_gaps = [[], []]
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
            for index_style, (plate, extra) in enumerate([(joiner, 0), (clasp_plate, j['loose_cap_extra_clearance'])]):
                assert max(overlap(plate,mesh) for mesh in nearby)<.02,('Swap-in clasp obstructs joiner',rear,placement)
                gaps = check_cap_pocket(plate, outlines, face, rear, j['cap_side_clearance'] + extra,
                                        j['cap_axial_clearance'] + extra)
                all_gaps[index_style].extend(gaps)
                key = 'loose_cap_gaps_mm' if index_style else 'cap_gaps_mm'
                report['joiners'][-1][key] = gaps
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
        assert all(all_gaps), 'Both front styles must cover real caps on each face'
    report['all_checks_passed']=True
    return report

def validate_samples(folder,frame_folder,p):
    """Compare each loose trial part with its crop from the actual production mesh."""
    q=p['frame']
    sample=trimesh.load_mesh(folder/'joiner_fit_samples.stl')
    pieces=list(sample.split(only_watertight=False))
    assert len(pieces)==7 and all(body.is_volume and abs(body.bounds[0,2])<.001 for body in pieces)
    comparisons=[]
    def compare(mesh,shift):
        mesh.apply_translation(shift)
        nearest=min(range(len(pieces)),key=lambda i:np.linalg.norm(pieces[i].centroid-mesh.centroid))
        actual=pieces.pop(nearest)
        diff=actual.difference(mesh,engine='manifold').volume+mesh.difference(actual,engine='manifold').volume
        assert abs(diff)<.015,('Fit coupon differs from production part',shift,diff)
        comparisons.append(float(diff))
    face=trimesh.load_mesh(frame_folder/'front.stl')
    for hand in [-1,1]:
        x=hand*(q['width_total']/2-12);y=-q['height_total']/2+12
        compare(region_clip(face,[x-12,y-12,-1],[x+12,y+12,30]),[-hand*15-x,-y,0])
    for name,x in [('snap_beam',-18),('screw_beam',12)]:
        beam=trimesh.load_mesh(frame_folder/(name+'.stl'))
        compare(region_clip(beam,[-30,-26,-1],[30,12,30]),[x,45,0])
    compare(trimesh.load_mesh(frame_folder/'front_plug_square.stl'),[-38,0,0])
    compare(trimesh.load_mesh(frame_folder/'screw_adapter.stl'),[-38,15,0])
    x,y,_=next(f['pos'] for f in q['floor_support_features'] if f['kind']=='floor')
    compare(region_clip(face,[x-2,y-2,-1],[x+17,y+12,30]),[32-x,-y,0])
    return comparisons

def validate_stops(meshes,p):
    """Line probes on every catch of both printed faces and both laser thicknesses."""
    from shapely.geometry import LineString
    q=p['frame'];results=[]
    for name,web in [('front',6),('back',6),('front_laser',6),('front_3mm_test',3)]:
        mesh=meshes[name]
        sections=[section(mesh,z) for z in [.1,web/2,web-.1]]
        inside=section(mesh,web+.1) if name in ('front','back') else None
        for f in q['floor_support_features']:
            x,y,_=f['pos'];width,root,depth=f['envelope']
            x+=width/2
            probe=LineString([(x,y+.01),(x,y+root+.1)])
            lengths=[profile.intersection(probe).length for profile in sections]
            if inside is None:
                assert max(lengths)-min(lengths)<.001 and abs(lengths[0]-root+.01)<.01
            else:
                assert lengths[0]+.5<lengths[1]<lengths[2]-.5,('Ramp direction',name,f,lengths)
                assert abs(lengths[2]-root)<.25 and inside.intersection(probe).length<=q['floor_support_thickness']+.01
            results.append(dict(face=name,kind=f['kind'],column=f['column'],row=f['supported_row'],profile_mm=lengths))
    return results

def validate_joiner_profile(folder,frame_folder,p):
    mesh=trimesh.load_mesh(folder/'joiners.stl')
    assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0
    bodies=sorted(mesh.split(),key=lambda body:body.centroid[0])
    j=p['corner_fixing'];cap=p['front_plug']
    assert len(bodies)==2 and j['screw_length']==25
    report=dict(variant=p['variant'],pieces=[])
    # Check the visible outline against the actual latch and the OOBB cutter
    # at the mouth, along the cone and below the seat.
    from shapely.geometry import Polygon,box
    from shapely.affinity import translate
    latch=trimesh.load_mesh(frame_folder/'front_plug_square.stl')
    outline=section(latch,.1)
    cap_corner=box(*outline.bounds).difference(Polygon(outline.exterior))
    cap_corner=sorted(cap_corner.geoms,key=lambda g:g.bounds[:2])[0]
    r=oobb.gv('hole_radius_m3','3dpr');head=oobb.gv('screw_countersunk_radius_m3','3dpr')
    cone=oobb.gv('screw_countersunk_depth_m3','3dpr')
    for body,part in zip(bodies,p['joiners']):
        assert np.allclose(body.extents,part['size'],atol=.01)
        assert abs(body.bounds[0,2])<.001 and abs(body.extents[2]-(cap['outer_y']-p['panel_thickness']+j['cap_axial_clearance']+j['front_roof_thickness']))<.001
        front=section(body,.1)
        # The corner opposite the clasp cutouts retains the actual latch
        # arc. Compare the outline locally, excluding those deliberate cutouts.
        arc=translate(cap_corner,front.bounds[0]-outline.bounds[0],front.bounds[1]-outline.bounds[1])
        zone=box(front.bounds[0],front.bounds[1],front.bounds[0]+.75,front.bounds[1]+.75)
        assert zone.difference(front).symmetric_difference(arc).area<.004
        assert abs(box(*front.bounds).difference(Polygon(front.exterior)).area-4*cap_corner.area)<.015
        for z in [.1,j['countersink_setback']+cone/2,j['countersink_setback']+cone+.2]:
            cross=section(body,z)
            radius=max(r,head-(head-r)*max(0,z-j['countersink_setback'])/cone)
            for x,y in part['holes']:
                pt=Point(x+part['print_center'][0],y)
                assert not cross.contains(pt) and abs(cross.distance(pt)-radius)<.08,(part['name'],z)
        report['pieces'].append(dict(name=part['name'],size_mm=part['size'],corner_radius_mm=cap['cover_radius']))
    return report['pieces']

def validate_frame(folder,p,views,projections):
    meshes={};q=p['frame']
    for name in views:
        mesh=trimesh.load_mesh(folder/(name+'.stl'))
        assert mesh.is_volume,(name,'open or inverted mesh')
        if name!='assembled':
            count=len(mesh.split(only_watertight=False))
            assert count==views[name],(name,count,views[name])
            assert abs(mesh.bounds[0,2])<.001,(name,'bed contact')
        meshes[name]=mesh
    batches=p['print_batches']
    for name,b in batches.items():
        assert abs(meshes[name].volume-b['count']*meshes[b['component']].volume)<.5,(name,'quantity')
        assert all(meshes[name].extents[i]<q[key] for i,key in enumerate(['bed_width','bed_height']))
    kit=meshes['front'].volume+meshes['back'].volume+sum(meshes[n].volume for n in batches)
    assert abs(kit-meshes['3dpr'].volume)<1 and abs(kit-meshes['assembled'].volume)<3,'Kit/assembly volume mismatch'
    back=meshes['back'].copy()
    back.apply_transform([[-1,0,0,0],[0,1,0,0],[0,0,-1,q['assembled_depth']],[0,0,0,1]])
    for mount in p['frame_mounts']:
        for name in ['snap_beam','screw_beam']:
            beam=meshes[name].copy();beam.apply_transform(drawing.v8_beam_to_frame(p,mount,name))
            assert max(overlap(face,beam) for face in [meshes['front'],back])<.015,(mount,name)
    dxfs=[check_dxf(folder/(name+'.dxf'),section(meshes[source],.1)) for name,source in projections]
    return dict(mesh_views=len(meshes),beam_mount_combinations=2*len(p['frame_mounts']),
                both_faces_checked=True,drawer_count=q['drawer_count'],laser_cuts=dxfs,
                stop_profiles=validate_stops(meshes,p) if p.get('face_stop_profile')=='inside_flat' else [])
