import copy
import math
import oobb


def cut(pos, thing, **kwargs):
    """Complete V8 removals, independent of every frozen connector profile."""
    p=kwargs
    component=p['v8_component']
    if component=='sample_window':
        x0,y0,x1,y1=p['sample_bounds']
        for x,y,w,h in [(-500,-500,x0+500,1000),(x1,-500,500,1000),
                        (-500,-500,1000,y0+500),(-500,y1,1000,500)]:
            oobb.append_full(thing,type='negative',shape='cube',m='',
                size=[w,h,500],pos=[x,y,-100])
        return
    if component=='joiner_corner_paths':
        j=p['corner_fixing'];axis=p['joiner_beam_axis'];length=p['rail_length']
        offset=max(c['x'] for c in p['frame']['corner_holes'])-max(m['x'] for m in p['frame_mounts'])
        station=j['backer_depth']-j['nut_recess']
        reach=j['screw_length']-j['joining_plate_thickness']+j['screw_reference_recess']-p['panel_thickness']
        for rear in [False,True]:
            for x in [-offset,offset]:
                for radius,start,depth in [(oobb.gv('hole_radius_m3','3dpr'),-.1,reach+.3),
                    (oobb.gv('nut_radius_m3','true')+j['beam_clearance'],station-j['beam_clearance'],
                     oobb.gv('nut_depth_m3','true')+2*j['beam_clearance'])]:
                    oobb.append_full(thing,type='negative',shape='cylinder',m='',radius=radius,h=depth,
                        rot=[-90 if rear else 90,0,0],
                        pos=[x,-length+start if rear else -start,axis+8])
        return
    if component in ('joining_plate','joiner_backer'):
        j=p['corner_fixing'];part=p['joining_plate']
        for x0,y0,z0,x1,y1,z1,radius in p['reliefs']:
            size=[x1-x0,y1-y0,z1-z0]
            if radius:
                oobb.append_full(thing,type='negative',shape='rounded_rectangle',m='',
                    size=size,radius=radius,pos=[(x0+x1)/2,(y0+y1)/2,z0])
            else:
                oobb.append_full(thing,type='negative',shape='cube',m='',size=size,pos=[x0,y0,z0])
        for x,y in part['holes']:
            if component=='joining_plate':
                oobb.append_full(thing,type='negative',shape='oobb_screw_countersunk',m='',
                    mode='3dpr',radius_name='m3',depth=part['size'][2]+.2,hole=True,
                    nut_include=False,include_nut=False,clearance=['top'],overhang=True,
                    zz='none',rot=[180,0,0],pos=[x,y,j['countersink_setback']])
            else:
                oobb.append_full(thing,type='negative',shape='oobb_hole',m='',mode='3dpr',
                    radius_name='m3',depth=j['backer_depth']+.4,pos=[x,-y,-.2])
                # Local +Z points out of the open nut-loading face. The two OOBB
                # overhang layers transition from the hex seat into the shaft bore.
                oobb.append_full(thing,type='negative',shape='oobb_nut',m='',mode='3dpr',
                    radius_name='m3',depth=j['nut_recess'],zz='bottom',clearance='top',
                    overhang=True,rot=[180,0,0],pos=[x,-y,j['nut_recess']])
        return
    if component=='joiner_nut_reference':
        oobb.append_full(thing,type='negative',shape='oobb_hole',m='',
            mode='true',radius_name='m3',depth=oobb.gv('nut_depth_m3','true')+.2,
            pos=[0,0,-.1])
        return
    if component=='clip_reinforcement':
        depth=p['laser_face_test']['reinforcement_thickness']
        oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
            size=[p['receiver_hole_width'],p['receiver_hole_height'],depth+.2],
            pos=[p.get('reinforcement_hole_offset_x',0)-p['receiver_hole_width']/2,-p['receiver_hole_height']/2,-.1]))
        for relief in p['reinforcement_reliefs']:
            oobb.append_full(thing,**dict(p,type='negative',shape='cylinder',m='',
                radius=relief['radius'],h=depth+.2,
                pos=[relief['x'],relief['y'],-.1]))
        return
    if component=='frame_face':
        q=p['frame']
        d=q['plate_thickness']+q['floor_support_projection']+.2
        for row in range(q['row']):
            y=q['opening_origin_y']+row*q['pitch_y']
            for col in range(q['column']):
                x=(col-(q['column']-1)/2)*q['pitch_x']
                for width,height in [(q['opening_width'],q['depth_lip']),
                                    (q['opening_width']-2*q['inset_lip'],q['opening_height'])]:
                    oobb.append_full(thing,type='negative',shape='rounded_rectangle',m='',
                        size=[width,height,d],radius=q['lip_cutout_radius'],pos=[x,y+height/2,-.1])
        for hole in q['corner_holes']:
            oobb.append_full(thing,type='negative',shape='oobb_hole',m='',radius_name=q['corner_hole_size'],
                depth=q['plate_thickness']+.2,pos=[hole['x'],hole['y'],-.1])
        for r in p['frame_mounts']:
            oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                size=[p['receiver_hole_width'],p['receiver_hole_height'],p['panel_thickness']+.2],
                pos=[r['x']-p['receiver_hole_width']/2,r['hole_y']-p['receiver_hole_height']/2,-.1]))
        return
    if component=='front_upper_support':
        if p.get('suppress_markings'):return
        oobb.append_full(thing,**dict(p,type='negative',shape='text',m='',
            text=str(p['trial']['sample_number']),font='Arial:style=Bold',size=p['number_size'],
            height=p['number_depth']+.1,depth=p['number_depth']+.1,
            halign='center',valign='center',pos=[0,-22,p['upper_support_height']-p['number_depth']]))
        return
    if component=='front_cap_cup':
        s=p['front_plug']
        oobb.append_full(thing,**dict(p,type='negative',shape='rounded_rectangle',m='',
            size=[s['cavity_width'],s['cavity_height'],s['cup_depth']-s['cover_thickness']+.1],radius=.3,
            pos=[0,0,s['cover_thickness']]))
        for relief in s.get('corner_reliefs',[]):
            oobb.append_full(thing,type='negative',shape='cylinder',m='',
                r=relief['radius'],h=s['cup_depth']+.2,
                pos=[relief['x'],relief['y'],-.1])
        return
    if component=='front_cap_stem':
        s=p['front_plug'];outer_y=s['outer_y'];stem=s['stem_width']/2;detent=s.get('detent_width',s['stem_width'])/2
        if s.get('retention')=='friction':
            stations=[(s['cover_thickness']-.15,stem),(outer_y-s['full_width_y'],stem),
                      (s['stem_depth'],s['nose_width']/2),(s['stem_depth']+.2,s['nose_width']/2)]
        else:
            a,b,c,d=s['detent_y']
            stations=[(s['cover_thickness']-.15,stem),(outer_y-d,stem),
                      (outer_y-c,detent),(outer_y-b,detent),(outer_y-a,stem),
                      (outer_y-s['full_width_y'],stem),(s['stem_depth'],s['nose_width']/2),
                      (s['stem_depth']+.2,s['nose_width']/2)]
        for side in [-1,1]:
            points=[[side*x,z] for z,x in stations]+[
                [side*(detent+.3),s['stem_depth']+.2],[side*(detent+.3),s['cover_thickness']-.15]]
            oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
                points=points,height=s['stem_height']+.2,depth=s['stem_height']+.2,
                rot=[90,0,0],pos=[0,s['stem_height']/2+.1,0]))
        return
    if p.get('finger_count',5)==4 and component=='clip':
        t=p['trial'];outer=p['outer'];root=p['spring_root_y']
        seated=(p['front_plug']['seated_spread']+p.get('seated_visual_clearance',0)) if p.get('seated_clip') else 0.0
        # The two outer strips are rigid panel stops. Only the two inner
        # hooked arms enter the hole; there is no permanent centre tongue.
        def profile(y):
            u=max(0,min(1,(y-root)/(t['shoulder_y']-root)))
            thick=t.get('root_thickness',t['arm_thickness'])+(t.get('tip_thickness',t['arm_thickness'])-t.get('root_thickness',t['arm_thickness']))*u
            wave=0.0
            if t['technique']=='curved' and root<y<0:
                wave=t['curve_amplitude']*math.sin(2*math.pi*(y-root)/(-root))
            if seated:
                v=max(0,min(1,(y-t['effective_root_y'])/(-t['effective_root_y'])))
                wave+=seated*v*v*(3-2*v)
            return outer+wave,outer+wave-thick
        top=t['tip_y']+1;limit=p['grip_width']/2+.2
        edge=outer+seated
        outline=[[edge,0],[edge,t['shoulder_y']+p.get('retaining_rake',0)],
                 [edge+p['hook_projection'],t['shoulder_y']],
                 [edge+p['hook_projection'],t['shoulder_y']+p['hook_land']],
                 [edge,t['tip_y']-p['tip_land']],[edge,top],[limit,top],[limit,0]]
        for side in [-1,1]:
            oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
                points=[[side*x,y] for x,y in outline],height=p['tongue_height']+.2,
                depth=p['tongue_height']+.2,pos=[0,0,-.1]))
            ys=[root+.5+i*(-root-.5)/40 for i in range(41)]
            # Close around the outside of the arm; overlap the open end at Y=0.
            points=[[side*(profile(y)[0]-.05),y] for y in ys]+[
                [side*(edge-.05),.1],[side*(outer+p['outer_release_width']),.1],
                [side*(outer+p['outer_release_width']),root+.5]]
            oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
                points=points,height=p['tongue_height']+.2,depth=p['tongue_height']+.2,pos=[0,0,-.1]))
            oobb.append_full(thing,**dict(p,type='negative',shape='cylinder',m='',
                r=.55,h=p['tongue_height']+.2,pos=[side*(outer+.475),root+.525,-.1]))
        ys=[root+t['root_radius']-.05+i*(top-root-t['root_radius']+.05)/70 for i in range(71)]
        if p.get('permanent_snap_test'):
            ys=sorted(set(ys+[0,t['shoulder_y'],t['shoulder_y']+p['retaining_rake']]))
        points=[[-profile(y)[1],y] for y in ys]+[[profile(y)[1],y] for y in reversed(ys)]
        oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
            points=points,height=p['tongue_height']+.2,depth=p['tongue_height']+.2,pos=[0,0,-.1]))
        oobb.append_full(thing,**dict(p,type='negative',shape='cylinder',m='',
            r=t['root_radius']+.025,h=p['tongue_height']+.2,pos=[0,root+t['root_radius'],-.1]))
        if not p.get('suppress_markings'):
            oobb.append_full(thing,**dict(p,type='negative',shape='text',m='',
                text=str(t['sample_number']),font='Arial:style=Bold',size=p['number_size'],
                height=p['number_depth']+.1,depth=p['number_depth']+.1,
                halign='center',valign='center',pos=[0,-22,p.get('upper_support_height',p['tongue_height'])-p['number_depth']]))
        if p.get('front_plug_test') and p['front_plug'].get('retention')!='friction':
            s=p['front_plug'];inner=p['outer']-t['tip_thickness']
            for side in [-1,1]:
                x=inner-.05 if side==1 else -inner-s['notch_depth']
                oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                    size=[s['notch_depth']+.05,s['notch_y'][1]-s['notch_y'][0],p['tongue_height']-2*s['notch_z_clearance']],
                    pos=[x,s['notch_y'][0],s['notch_z_clearance']]))
        return
    if component=='receiver':
        for i,width in enumerate(p['receiver_hole_widths']):
            x=(i-(len(p['receiver_hole_widths'])-1)/2)*24 if p.get('drop_loop') or p.get('permanent_snap_test') else (i-2)*24
            oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                size=[width,p['receiver_hole_height'],p['receiver_print_thickness']+.2],
                pos=[x-width/2,-p['receiver_hole_height']/2,-.1]))
            oobb.append_full(thing,**dict(p,type='negative',shape='text',m='',
                text=p.get('receiver_labels',[f'{w:.1f}' for w in p['receiver_hole_widths']])[i],font='Arial:style=Bold',size=3,
                height=p['number_depth']+.1,depth=p['number_depth']+.1,
                halign='center',valign='center',
                pos=[x,10,p['receiver_print_thickness']-p['number_depth']]))
    elif component=='screw_beam':
        s=p['screw']
        if s.get('nut_primitive')=='oobb_v5_explicit':
            # Give the primitive its own local frame. Do not inherit part-level
            # anchors/rotations or overhang tooling from the cabinet kwargs.
            oobb.append_full(thing,type='negative',shape='cylinder',m='',
                r=s['bore_radius'],h=s['length']+s.get('beam_engagement',0),rot=[90,0,0],
                pos=[0,s.get('beam_engagement',0)+.1,s['axis_height']])
            oobb.append_full(thing,type='negative',shape='oobb_nut',m='',
                radius_name='m3',depth=s['nut_depth'],zz='bottom',
                overhang=s['nut_overhang'],clearance=s['nut_side_clearance'],
                hole=False,mode='3dpr',rot=[90,0,0],
                pos=[0,-s['nut_near'],s['axis_height']])
            return
        oobb.append_full(thing,**dict(p,type='negative',shape='cylinder',m='',
            r=s['bore_radius'],h=16,rot=[90,0,0],pos=[0,.1,s['axis_height']]))
        p3={
            **copy.deepcopy(p),'type':'negative','shape':'oobb_nut','m':'',
            'radius_name':'m3','depth':s['nut_depth'],'overhang':True,
            'clearance':s['nut_side_clearance'],'rot':[90,0,0],
            'pos':[0,-s['nut_near'],s['axis_height']],
        }
        oobb.append_full(thing,**p3)
    elif component=='screw_adapter':
        s=p['screw']; f=s['flange_size'][2]
        depth=s.get('adapter_engagement',s['guide_depth'])
        p3={
            **copy.deepcopy(p),'type':'negative','shape':'oobb_screw_countersunk','m':'',
            'radius_name':'m3','depth':s['length'],'hole':True,
            'nut_include':False,'include_nut':False,'clearance':['top'],
            'overhang':False,'zz':'none','rot':[0,180,0],'pos':[0,0,0],
        }
        oobb.append_full(thing,**p3)
        # Two open cheeks avoid the thin walls a circular guide would leave.
        oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
            size=[s['guide_slot_width'],s['guide_height']+1,depth+.1],
            pos=[-s['guide_slot_width']/2,-(s['guide_height']+1)/2,f]))
        # Simple 0.4 mm side chamfers let an imperfect guide find the opening.
        for side in [-1,1]:
            edge=side*s['guide_width']/2
            points=[[edge+side*.2,f+depth-.6],
                    [edge-side*.6,f+depth+.2],
                    [edge+side*.2,f+depth+.2]]
            oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
                points=points,height=s['guide_height']+.2,depth=s['guide_height']+.2,
                rot=[90,0,0],pos=[0,s['guide_height']/2+.1,0]))
        for relief in s.get('corner_reliefs',[]):
            oobb.append_full(thing,type='negative',shape='cylinder',m='',
                r=relief['radius'],h=f+.2,pos=[relief['x'],relief['y'],-.1])


def floor_stop(thing,**p):
    feature=p['floor_support_feature']
    width,root,depth=feature['envelope']
    if p.get('face_stop_profile')=='inside_flat':
        web=p['plate_thickness']
        # Grow the lead-in toward the inner web face. At that plane the
        # catch ends square; only the level bearing shelf continues inward.
        rise=min(p['catch_tab_height'],web)
        points=[[root-rise-.1,-.1],[root+.1,-.1],[root+.1,web+.1]]
        if feature['kind']=='floor':
            oobb.append_full(thing,type='negative',shape='cube',m='',
                size=[width+.2,root,depth-web+.1],
                pos=[feature['pos'][0]-.1,feature['pos'][1]+p['floor_support_thickness'],web])
    elif feature['kind']=='top_catch':
        # Sloped stop underside: each successive print layer is narrower.
        points=[[root+.1,-.1],[root+.1,depth+.1],[root-depth-.1,depth+.1]]
    else:
        thick=p['floor_support_thickness']
        chamfer=p['floor_support_tip_chamfer']
        # The bearing roof is horizontal in service. The bed-facing lower
        # surface rises at 45 degrees, then stays thin and bevels at the tip.
        points=[[root+.1,-.1],[root+.1,depth+.1],
                [thick-chamfer-.1,depth+.1],[thick,depth-chamfer],
                [thick,feature['ramp_end_z']]]
    p3={
        **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
        'points':points,'height':width+.2,'depth':width+.2,
        'rot':[90,0,90],
        'pos':[feature['pos'][0]-.1,feature['pos'][1],0],
    }
    oobb.append_full(thing,**p3)

# Cabinet shop axes match the face CAD: X across, Y down, Z front to rear.
CABINET_CUTS = """
module cap_bores() {
  for (side=[-1,1], i=[0:4])
    translate([side*(inside_w/2+t/2),0,stations[i]]) rotate([-90,0,0])
      if (i%2==0) translate([0,0,-.01]) cylinder(d=6.1,h=8.01);
      else {
        translate([0,0,-.01]) cylinder(d=4,h=t+.02);
        translate([0,0,t-1.5]) cylinder(d1=4,d2=7.02,h=1.51);
      }
}
module side_bores() {
  for (bottom=[0,1], i=[0:4])
    translate([t/2,bottom*inside_h,stations[i]]) rotate([bottom?90:-90,0,0])
      translate([0,0,-.01]) cylinder(d=i%2?2.5:6.1,h=i%2?21.01:17.01);
  for (back=[0,1], y=retainer_y)
    translate([t/2,y,back*depth]) rotate([0,back?180:0,0])
      translate([0,0,-.01]) cylinder(d=2.5,h=16.01);
}
"""

BEAM_JOINT_CUTS = """
module joint_bores(holes,wood,access) {
  for(slot=access) hull()
    for(y=[slot[1],slot[2]]) translate([slot[0],y,-.05]) cylinder(r=slot[3],h=tie_t+.1);
  // Leave the OOBB countersink and pilot cheeks of each native adapter intact.
  for(p=holes) translate([p[0],p[1],-.05]) cylinder(d=7,h=tie_t+.1);
  if(len(wood)) translate(wood) {
    translate([0,0,-.05]) cylinder(d=4,h=tie_t+.1);
    translate([0,0,-.01]) cylinder(d1=7.02,d2=4,h=1.51);
  }
}
"""
