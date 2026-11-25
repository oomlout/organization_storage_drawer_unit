import copy
import math
from turtle import position
import oobb
import yaml
import os
import scad_help


def get_container_cutout_ai_version_7(pos, thing, **kwargs):
    """Complete V7 removals, independent of every frozen connector profile."""
    p=kwargs
    component=p['v7_component']
    if component=='joining_plate':
        get_container_cutout_ai_version_6(pos,thing,**dict(p['frame'],
            v6_component='joining_plate',joining_plate=p['joining_plate']))
        # Remove a shallow underside layer except for circular seating lands.
        # Keep this complete removal in the cutout stage, never in body code.
        part=p['joining_plate'];j=p['optional_joiners']
        layer=oobb.get_default_thing(type='v7_joiner_adapter_clearance')
        oobb.append_full(layer,type='positive',shape='cube',m='',
            size=[part['size'][0]+.2,part['size'][1]+.2,j['adapter_clearance_depth']+.1],
            pos=[-part['size'][0]/2-.1,-part['size'][1]/2-.1,-.1])
        for x,y in part['holes']:
            oobb.append_full(layer,type='negative',shape='cylinder',m='',
                radius=j['seating_pad_radius'],h=j['adapter_clearance_depth']+.3,pos=[x,y,-.2])
        thing['components'].append(dict(type='rotation',typetype='negative',rot=[0,0,0],
            pos=[0,0,0],objects=layer['components']))
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
        get_container_cutout_ai_version_6(pos,thing,**dict(q,v6_component='plate',rail_positions=[]))
        for r in p['frame_mounts']:
            oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                size=[p['receiver_hole_width'],p['receiver_hole_height'],p['panel_thickness']+.2],
                pos=[r['x']-p['receiver_hole_width']/2,r['hole_y']-p['receiver_hole_height']/2,-.1]))
        return
    if component=='frame_snap_body':
        band=p['beam_end_length'];length=p['rail_length'];run=p['beam_transition_length']
        # Bed-rooted, 45 degree rise from the exact coupon grip to running roof.
        for rear in [False,True]:
            anchor=-length+band if rear else -band
            direction=1 if rear else -1
            points=[[anchor-direction*.2,p['upper_support_height']],
                    [anchor+direction*run,p['beam_running_height']],
                    [anchor+direction*run,p['beam_running_height']+.2],
                    [anchor-direction*.2,p['beam_running_height']+.2]]
            oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
                points=points,height=p['grip_width']+.2,depth=p['grip_width']+.2,
                rot=[90,0,90],pos=[-p['grip_width']/2-.1,0,0]))
        return
    if component=='frame_beam_windows':
        for w in p['beam_windows']:
            oobb.append_full(thing,**dict(p,type='negative',shape='rounded_rectangle',m='',
                size=[w['width'],w['length'],max(p['beam_running_height'],p['screw']['running_height'])+.2],
                radius=w['radius'],pos=[0,w['y'],-.1]))
        return
    if component=='frame_screw_body':
        # Match the snap beam's bearing elevation relative to the hole axis.
        # Nut bosses remain solid at each end, with a bed-supported roof rise.
        s=p['screw'];length=p['rail_length'];band=p['beam_end_length']
        rise=s['running_height']-s['end_height']
        for rear in [False,True]:
            start=-length if rear else 0;direction=1 if rear else -1
            points=[[start-direction*.1,s['end_height']],
                    [start+direction*band,s['end_height']],
                    [start+direction*(band+rise),s['running_height']],
                    [start+direction*(band+rise),s['running_height']+.2],
                    [start-direction*.1,s['running_height']+.2]]
            oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
                points=points,height=p['grip_width']+.2,depth=p['grip_width']+.2,
                rot=[90,0,90],pos=[-p['grip_width']/2-.1,0,0]))
        for rear in [False,True]:
            sub=oobb.get_default_thing(type='v7_screw_end_cuts')
            get_container_cutout_ai_version_7(pos,sub,**dict(p,v7_component='screw_beam'))
            objects=sub['components']
            while any(isinstance(obj,list) for obj in objects):
                objects=[item for obj in objects for item in (obj if isinstance(obj,list) else [obj])]
            # The enclosing transform is the subtraction. Its child tools
            # must be positive solids, including compound OOBB nut cutters.
            for obj in objects:
                if obj['type']=='rotation':obj['typetype']='positive'
                else:obj['type']='positive'
            thing['components'].append(dict(type='rotation',typetype='negative',
                rot=[0,0,180] if rear else [0,0,0],pos=[0,-p['rail_length'] if rear else 0,0],objects=objects))
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
    if component=='drop_loop':
        d=p['drop_loop']
        for side in [-1,1]:
            x=p['neck_width']/2 if side==1 else -p['grip_width']/2-.1
            oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                size=[(p['grip_width']-p['neck_width'])/2+.1,d['tip_y']+.2,p['tongue_height']+.2],
                pos=[x,0,-.1]))
        oobb.append_full(thing,**dict(p,type='negative',shape='rounded_rectangle',m='',
            size=[d['eye_width'],d['eye_depth'],p['tongue_height']+.2],radius=d['eye_radius'],
            pos=[0,(d['eye_near']+d['eye_far'])/2,-.1]))
        oobb.append_full(thing,**dict(p,type='negative',shape='text',m='',
            text='54',font='Arial:style=Bold',size=p['number_size'],
            height=p['number_depth']+.1,depth=p['number_depth']+.1,
            halign='center',valign='center',pos=[0,-22,p['tongue_height']-p['number_depth']]))
        return
    if component=='drop_key':
        d=p['drop_loop']
        for side in [-1,1]:
            x=d['key_width']/2 if side==1 else -d['key_head_width']/2-.1
            oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                size=[(d['key_head_width']-d['key_width'])/2+.1,d['key_length']+.1,d['key_depth']+.2],
                pos=[x,-d['key_length']-.1,-.1]))
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
    if component=='keeper':
        k=p['keeper']
        for side in [-1,1]:
            x=k['stem_width']/2 if side==1 else -k['head_width']/2-.1
            oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                size=[(k['head_width']-k['stem_width'])/2+.1,k['head_start_y']-k['stem_start_y']+.1,k['stem_height']+.2],
                pos=[x,k['stem_start_y']-.1,-.1]))
        return
    if component=='clip':
        t=p['trial']; outer=p['outer']; limit=p['grip_width']/2+.2
        # Outside silhouette: a hard seating shoulder, straight neck, square
        # retaining land and shallow insertion ramp, duplicated on both arms.
        outline=[[outer,0],[outer,t['shoulder_y']],
                 [outer+p['hook_projection'],t['shoulder_y']],
                 [outer+p['hook_projection'],t['shoulder_y']+p['hook_land']],
                 [outer,t['tip_y']-p['tip_land']],[outer,t['tip_y']+1],[limit,t['tip_y']+1],
                 [limit,0]]
        for side in [-1,1]:
            oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
                points=[[side*x,y] for x,y in outline],height=p['tongue_height']+.2,
                depth=p['tongue_height']+.2,pos=[0,0,-.1]))
            # Keep rigid outer bearing strips to the panel seating plane.
            # A 1 mm open slot releases the arm within the beam itself.
            oobb.append_full(thing,**dict(p,type='negative',shape='rounded_rectangle',m='',
                size=[1.05,-p['spring_root_y']+1,p['tongue_height']+.2],radius=.525,
                pos=[side*(outer+.475),(p['spring_root_y']+1)/2,-.1]))
            inner=outer-t['arm_thickness']
            width=inner-p['pilot_half_width']
            bottom=p['spring_root_y']
            top=t['tip_y']+1
            oobb.append_full(thing,**dict(p,type='negative',shape='rounded_rectangle',m='',
                size=[width,top-bottom,p['tongue_height']+.2],radius=width/2,
                pos=[side*(inner+p['pilot_half_width'])/2,(top+bottom)/2,-.1]))
        # The rigid centre pilot bears vertically; its tip stops within the hole.
        oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
            size=[2*p['pilot_half_width']+.1,t['tip_y']-p['pilot_depth']+1,p['tongue_height']+.2],
            pos=[-p['pilot_half_width']-.05,p['pilot_depth'],-.1]))
        oobb.append_full(thing,**dict(p,type='negative',shape='text',m='',
            text=str(t['sample_number']),font='Arial:style=Bold',size=p['number_size'],
            height=p['number_depth']+.1,depth=p['number_depth']+.1,
            halign='center',valign='center',
            pos=[0,-22,p['tongue_height']-p['number_depth']]))
    elif component=='receiver':
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
    elif component=='face':
        q=p['face']
        get_container_cutout_ai_version_6(pos,thing,**dict(q,v6_component='plate',rail_positions=[]))
        for rail in q['rail_positions']:
            oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
                size=[p['receiver_hole_width'],p['receiver_hole_height'],q['plate_thickness']+.2],
                pos=[rail['x']-p['receiver_hole_width']/2,
                     rail['y']+8-p['receiver_hole_height']/2,-.1]))
    else:
        raise ValueError('Unknown V7 removal '+component)


def get_base(pos, thing, **kwargs):
    if kwargs.get("style") == "ai_version_1":
        get_container_cutout_ai_version_1(pos, thing, **kwargs)
    elif kwargs.get("style") == "ai_version_2":
        get_container_cutout_ai_version_2(pos, thing, **kwargs)
    elif kwargs.get("style") == "ai_version_3":
        get_container_cutout_ai_version_3(pos, thing, **kwargs)
    elif kwargs.get("style") == "ai_version_4":
        get_container_cutout_ai_version_4(pos, thing, **kwargs)
    elif kwargs.get("style") == "ai_version_5":
        get_container_cutout_ai_version_5(pos, thing, **kwargs)
    else:
        get_container_cutout_version_1(pos, thing, **kwargs)

def get_container_cutout_ai_legacy_straight(pos, thing, **kwargs):
    # Through opening; epsilon avoids coincident faces at both ends.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "n",
        "shape": "rounded_rectangle",
        "m": "#",
        "size": [kwargs["opening_width"], kwargs["opening_height"], kwargs["depth_total"] + 0.2],
        "radius": kwargs["opening_radius"],
        "pos": [pos[0], pos[1], pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # All material-saving cuts for this cell live here, relative to its centre.
    # Adjacent cells deliberately repeat shared-wall cuts: subtracting the same
    # space twice is harmless and keeps each cutout complete on its own.
    if kwargs["lightening"] and kwargs["part_role"] == "frame":
        wall = kwargs["thickness_wall"]
        border = kwargs["drawer_border_edge"]
        row_index = kwargs.get("row_index", 0)
        column_index = kwargs.get("column_index", 0)
        bottom = kwargs["front_band"]
        top = kwargs["depth_total"] - kwargs["rear_band"]

        # Two windows through BOTH the floor and ceiling of this drawer.
        # The pointed end retains the existing supportable closing roof.
        half = kwargs["shelf_window_width"] / 2
        shoulder = top - half * kwargs["roof_slope"]
        offset = (kwargs["middle_rib_width"] + kwargs["shelf_window_width"]) / 2
        for side_y in [-1, 1]:
            outside = (side_y == -1 and row_index == 0) or (side_y == 1 and row_index == kwargs["row"] - 1)
            thickness = border if outside else wall
            y = pos[1] + side_y * (kwargs["opening_height"] / 2 + thickness / 2)
            for side_x in [-1, 1]:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "n",
                    "shape": "polygon",
                    "m": "",
                    "height": thickness + 0.2,
                    "depth": thickness + 0.2,
                    "points": [
                        [-half, bottom],
                        [half, bottom],
                        [half, shoulder],
                        [0, top],
                        [-half, shoulder],
                    ],
                    "rot": [90, 0, 0],
                    "pos": [pos[0] + side_x * offset, y + thickness / 2 + 0.1, pos[2]],
                }
                oobb.append_full(thing, **p3)

        # One window through EACH side wall, retaining the corner rails.
        half = kwargs["side_window_width"] / 2
        shoulder = top - half * kwargs["roof_slope"]
        for side_x in [-1, 1]:
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            thickness = border if outside else wall
            x = pos[0] + side_x * (kwargs["opening_width"] / 2 + thickness / 2)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "n",
                "shape": "polygon",
                "m": "",
                "height": thickness + 0.2,
                "depth": thickness + 0.2,
                "points": [
                    [-half, bottom],
                    [half, bottom],
                    [half, shoulder],
                    [0, top],
                    [-half, shoulder],
                ],
                "rot": [90, 0, 90],
                "pos": [x - thickness / 2 - 0.1, pos[1], pos[2]],
            }
            oobb.append_full(thing, **p3)

    # A supportable ramp grows into the opening from the shelf at Z=0.
    # Local polygon coordinates are (projection into opening, print Z).
    # Extrude along X; add after subtraction so the cavity cannot erase it.
    if kwargs.get("catch_tab_height", 0) > 0:
        projection = kwargs["catch_tab_height"]
        ramp = kwargs["catch_tab_ramp_depth"]
        tip_end = ramp + kwargs["catch_tab_depth"]
        wall = kwargs["thickness_wall"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "positive_positive",
            "shape": "polygon",
            "m": "#",
            "height": kwargs["catch_tab_width"],
            "depth": kwargs["catch_tab_width"],
            "points": [
                [-wall, 0],
                [0, 0],
                [projection, ramp],
                [projection, tip_end],
                [-wall, tip_end],
            ],
            "rot": [90, 0, 90],
            "pos": [pos[0] - kwargs["catch_tab_width"] / 2,
                    pos[1] - kwargs["opening_height"] / 2, pos[2]],
        }
        oobb.append_full(thing, **p3)

def get_container_cutout_ai_version_1(pos, thing, **kwargs):
    # Preserve the user's two-piece stepped opening. The lip-bearing ledge is
    # at lip_step_y; the reliefs below deliberately avoid that entire shelf.
    opening_width = kwargs["opening_width"]
    opening_height = kwargs["opening_height"]
    depth_total = kwargs["depth_total"]
    depth_lip = kwargs["depth_lip"]
    inset_lip = kwargs["inset_lip"]
    step = kwargs["lip_step_y"]

    # Full-width, 12 mm high channel: same profile and position as the user edit.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width, depth_lip, depth_total + 0.2],
        "radius": kwargs["lip_cutout_radius"],
        "pos": [pos[0], pos[1] - (opening_height - depth_lip) / 2, pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Narrower body opening forms the 5.5 mm shoulders beside the lip.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width - 2 * inset_lip, opening_height, depth_total + 0.2],
        "radius": kwargs["opening_radius"],
        "pos": [pos[0], pos[1], pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Taller containers do not need thick shoulders all the way down the body.
    # Keep only the 100 ml support height, then open to full width for the rest
    # of the cavity, along the ENTIRE insertion depth including the end bands.
    # The small square-bottom cut makes the shoulder end exact; the rounded
    # rectangle preserves the two far corners of the enlarged opening.
    extension = kwargs["body_extension_height"]
    if extension > 0:
        radius = min(kwargs["opening_radius"], extension / 2)
        end_y = pos[1] + kwargs["lip_support_end_y"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "rounded_rectangle",
            "m": "",
            "size": [opening_width, extension, depth_total + 0.2],
            "radius": radius,
            "pos": [pos[0], end_y + extension / 2, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "cube",
            "m": "",
            "size": [opening_width, radius, depth_total + 0.2],
            "pos": [pos[0] - opening_width / 2, end_y, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)

    if kwargs["lightening"] and kwargs["part_role"] == "frame":
        wall = kwargs["thickness_wall"]
        border = kwargs["drawer_border_edge"]
        row_index = kwargs.get("row_index", 0)
        column_index = kwargs.get("column_index", 0)
        bottom = kwargs["front_band"]
        top = depth_total - kwargs["rear_band"]

        # One broad floor/ceiling window: no longitudinal centre support.
        # A nonzero middle_rib_width optionally restores two windows for trials.
        half = kwargs["shelf_window_width"] / 2
        shoulder = top - half * kwargs["roof_slope"]
        offsets = [0]
        if kwargs["middle_rib_width"] > 0:
            offset = (kwargs["middle_rib_width"] + kwargs["shelf_window_width"]) / 2
            offsets = [-offset, offset]
        for side_y in [-1, 1]:
            outside = (side_y == -1 and row_index == 0) or (side_y == 1 and row_index == kwargs["row"] - 1)
            thickness = border if outside else wall
            y = pos[1] + side_y * (opening_height / 2 + thickness / 2)
            for offset in offsets:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": thickness + 0.2,
                    "depth": thickness + 0.2,
                    "points": [
                        [-half, bottom],
                        [half, bottom],
                        [half, shoulder],
                        [0, top],
                        [-half, shoulder],
                    ],
                    "rot": [90, 0, 0],
                    "pos": [pos[0] + offset, y + thickness / 2 + 0.1, pos[2]],
                }
                oobb.append_full(thing, **p3)

        # Separate reliefs BELOW and ABOVE the shelf. The upper cut reaches
        # through the thick shoulder as well as the wall, instead of leaving
        # a large solid block behind a cosmetic outer-wall hole.
        # The shelf's full root is retained from step-1 to step+3 by default.
        zones = [
            {
                "low": -opening_height / 2 + kwargs["side_rail_width"],
                "high": step - kwargs["lip_cutout_radius"],
                "inset": 0,
            },
            {
                "low": step + kwargs["lip_shelf_thickness"],
                "high": opening_height / 2 - kwargs["side_rail_width"],
                "inset": inset_lip,
            },
        ]
        for side_x in [-1, 1]:
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            thickness = border if outside else wall
            for zone in zones:
                half = (zone["high"] - zone["low"]) / 2
                shoulder = top - half * kwargs["roof_slope"]
                cut_depth = thickness + zone["inset"] + 0.2
                x = pos[0] + side_x * (opening_width / 2 + (thickness - zone["inset"]) / 2)
                y = pos[1] + (zone["low"] + zone["high"]) / 2
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": cut_depth,
                    "depth": cut_depth,
                    "points": [
                        [-half, bottom],
                        [half, bottom],
                        [half, shoulder],
                        [0, top],
                        [-half, shoulder],
                    ],
                    "rot": [90, 0, 90],
                    "pos": [x - cut_depth / 2, y, pos[2]],
                }
                oobb.append_full(thing, **p3)

    # Front catch and 45-degree ramp use the population dimensions.
    if kwargs.get("catch_tab_height", 0) > 0:
        projection = kwargs["catch_tab_height"]
        ramp = kwargs["catch_tab_ramp_depth"]
        tip_end = ramp + kwargs["catch_tab_depth"]
        wall = kwargs["thickness_wall"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "positive_positive",
            "shape": "polygon",
            "m": "#",
            "height": kwargs["catch_tab_width"],
            "depth": kwargs["catch_tab_width"],
            "points": [
                [-wall, 0],
                [0, 0],
                [projection, ramp],
                [projection, tip_end],
                [-wall, tip_end],
            ],
            "rot": [90, 0, 90],
            "pos": [pos[0] - kwargs["catch_tab_width"] / 2,
                    pos[1] - opening_height / 2, pos[2]],
        }
        oobb.append_full(thing, **p3)

def get_container_cutout_ai_version_2(pos, thing, **kwargs):
    # Preserve the user's two-piece stepped opening. The lip-bearing ledge is
    # at lip_step_y; the reliefs below deliberately avoid that entire shelf.
    opening_width = kwargs["opening_width"]
    opening_height = kwargs["opening_height"]
    depth_total = kwargs["depth_total"]
    depth_lip = kwargs["depth_lip"]
    inset_lip = kwargs["inset_lip"]
    step = kwargs["lip_step_y"]

    # Full-width, 12 mm high channel: same profile and position as the user edit.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width, depth_lip, depth_total + 0.2],
        "radius": kwargs["lip_cutout_radius"],
        "pos": [pos[0], pos[1] - (opening_height - depth_lip) / 2, pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Narrower body opening forms the 5.5 mm shoulders beside the lip.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width - 2 * inset_lip, opening_height, depth_total + 0.2],
        "radius": kwargs["opening_radius"],
        "pos": [pos[0], pos[1], pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Taller containers do not need thick shoulders all the way down the body.
    # Keep only the 100 ml support height, then open to full width for the rest
    # of the cavity, along the ENTIRE insertion depth including the end bands.
    # The small square-bottom cut makes the shoulder end exact; the rounded
    # rectangle preserves the two far corners of the enlarged opening.
    extension = kwargs["body_extension_height"]
    if extension > 0:
        radius = min(kwargs["opening_radius"], extension / 2)
        end_y = pos[1] + kwargs["lip_support_end_y"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "rounded_rectangle",
            "m": "",
            "size": [opening_width, extension, depth_total + 0.2],
            "radius": radius,
            "pos": [pos[0], end_y + extension / 2, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "cube",
            "m": "",
            "size": [opening_width, radius, depth_total + 0.2],
            "pos": [pos[0] - opening_width / 2, end_y, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)

    if kwargs["lightening"] and kwargs["part_role"] == "frame":
        wall = kwargs["thickness_wall"]
        border = kwargs["drawer_border_edge"]
        row_index = kwargs.get("row_index", 0)
        column_index = kwargs.get("column_index", 0)
        bottom = kwargs["front_band"]
        top = kwargs["body_depth"] + 0.1 if kwargs["split_frame"] else depth_total - kwargs["rear_band"]

        # One broad floor/ceiling window: no longitudinal centre support.
        # A nonzero middle_rib_width optionally restores two windows for trials.
        half = kwargs["shelf_window_width"] / 2
        shoulder = top if kwargs["split_frame"] else top - half * kwargs["roof_slope"]
        offsets = [0]
        if kwargs["middle_rib_width"] > 0:
            offset = (kwargs["middle_rib_width"] + kwargs["shelf_window_width"]) / 2
            offsets = [-offset, offset]
        for side_y in [-1, 1]:
            outside = (side_y == -1 and row_index == 0) or (side_y == 1 and row_index == kwargs["row"] - 1)
            thickness = border if outside else wall
            y = pos[1] + side_y * (opening_height / 2 + thickness / 2)
            for offset in offsets:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": thickness + 0.2,
                    "depth": thickness + 0.2,
                    "points": ([[-half, bottom], [half, bottom], [half, top], [-half, top]]
                               if kwargs["split_frame"] else
                               [[-half, bottom], [half, bottom], [half, shoulder], [0, top], [-half, shoulder]]),
                    "rot": [90, 0, 0],
                    "pos": [pos[0] + offset, y + thickness / 2 + 0.1, pos[2]],
                }
                oobb.append_full(thing, **p3)

        # Separate reliefs BELOW and ABOVE the shelf. The upper cut reaches
        # through the thick shoulder as well as the wall, instead of leaving
        # a large solid block behind a cosmetic outer-wall hole.
        # The shelf's full root is retained from step-1 to step+3 by default.
        zones = [
            {
                "low": -opening_height / 2 + kwargs["side_rail_width"],
                "high": step - kwargs["lip_cutout_radius"],
                "inset": 0,
            },
            {
                "low": step + kwargs["lip_shelf_thickness"],
                "high": opening_height / 2 - kwargs["side_rail_width"],
                "inset": inset_lip,
            },
        ]
        for side_x in [-1, 1]:
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            thickness = border if outside else wall
            for zone in zones:
                half = (zone["high"] - zone["low"]) / 2
                shoulder = top if kwargs["split_frame"] else top - half * kwargs["roof_slope"]
                cut_depth = thickness + zone["inset"] + 0.2
                x = pos[0] + side_x * (opening_width / 2 + (thickness - zone["inset"]) / 2)
                y = pos[1] + (zone["low"] + zone["high"]) / 2
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": cut_depth,
                    "depth": cut_depth,
                    "points": ([[-half, bottom], [half, bottom], [half, top], [-half, top]]
                               if kwargs["split_frame"] else
                               [[-half, bottom], [half, bottom], [half, shoulder], [0, top], [-half, shoulder]]),
                    "rot": [90, 0, 90],
                    "pos": [x - cut_depth / 2, y, pos[2]],
                }
                oobb.append_full(thing, **p3)

    # Extend the protected lip shelf into the joint. Each shared divider has
    # one fixing, not two overlapping screws. No hardware intrudes into the pot
    # cavity: the outside border has been widened to house its own fixing.
    if kwargs["split_frame"] and kwargs["assembly_half"] in ["front", "back"]:
        seam = kwargs["body_depth"]
        for side_x in [-1, 1]:
            column_index = kwargs.get("column_index", 0)
            if side_x == -1 and column_index > 0:
                continue
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            offset = ((kwargs["drawer_border_edge"] - inset_lip) / 2 if outside
                      else kwargs["thickness_wall"] / 2)
            x = pos[0] + side_x * (opening_width / 2 + offset)
            y = pos[1] + step + kwargs["hardware_axis_height"]
            if kwargs["assembly_half"] == "front":
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "positive",
                    "shape": "cube",
                    "m": "",
                    "size": [kwargs["interlock_width"], kwargs["interlock_height"], kwargs["interlock_depth"] + 0.1],
                    "pos": [x - kwargs["interlock_width"] / 2, y - kwargs["interlock_height"] / 2, pos[2] + seam - 0.1],
                }
                oobb.append_full(thing, **p3)
            else:
                width = kwargs["interlock_width"] + 2 * kwargs["interlock_clearance"]
                height = kwargs["interlock_height"] + 2 * kwargs["interlock_clearance"]
                pocket = kwargs["interlock_depth"] + kwargs["interlock_end_clearance"]
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "cube",
                    "m": "",
                    "size": [width, height, pocket + 0.1],
                    "pos": [x - width / 2, y - height / 2, pos[2] + seam - pocket],
                }
                oobb.append_full(thing, **p3)

            # OOBB's current API consumes clearance=["top", "bottom"]. Keep
            # the explicitly requested boolean flags too. A 16 mm under-head
            # length leaves 13 mm to the near nut face and a 3 mm nut pocket.
            # The front head seat lies 6 mm before the seam. The rear's same
            # screw origin is 6 mm beyond its seam in local print coordinates.
            front = kwargs["assembly_half"] == "front"
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative",
                "shape": "oobb_screw_socket_cap",
                "m": "",
                "radius_name": "m3",
                "depth": kwargs["screw_length"],
                "include_nut": True,
                "top_clearance": True,
                "bottom_clearance": True,
                "clearance": ["top", "bottom"],
                "overhang": True,
                "rot": [0, 180, 0] if front else [0, 0, 0],
                "pos": [x, y, pos[2] + seam + (-kwargs["screw_head_seat_offset"] if front else kwargs["screw_head_seat_offset"])],
            }
            oobb.append_full(thing, **p3)

        # The other mating islands are the corner rails at every grid junction.
        # Each cell owns its left/bottom junctions, plus the far outside edges;
        # this produces one peg/socket per junction without duplicate features.
        # Internal row joints are offset toward the rounded top of the lower
        # opening, where enough material remains around the socket. These pegs
        # stay inside existing rail material and do not reduce drawer clearance.
        column_index = kwargs.get("column_index", 0)
        row_index = kwargs.get("row_index", 0)
        for side_x in [-1, 1]:
            if side_x == 1 and column_index < kwargs["column"] - 1:
                continue
            outside_x = side_x == 1 or column_index == 0
            border_x = kwargs["drawer_border_edge"] if outside_x else kwargs["thickness_wall"]
            x = pos[0] + side_x * (opening_width / 2 + border_x / 2)
            for side_y in [-1, 1]:
                if side_y == 1 and row_index < kwargs["row"] - 1:
                    continue
                outside_y = side_y == 1 or row_index == 0
                border_y = kwargs["drawer_border_edge"] if outside_y else kwargs["thickness_wall"]
                y = pos[1] + side_y * (opening_height / 2 + border_y / 2)
                if not outside_y:
                    y -= kwargs["thickness_wall"] / 2
                front = kwargs["assembly_half"] == "front"
                radius = kwargs["corner_interlock_diameter"] / 2
                if not front:
                    radius += kwargs["interlock_clearance"]
                pocket = kwargs["interlock_depth"] + kwargs["interlock_end_clearance"]
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "positive" if front else "negative",
                    "shape": "polygon",
                    "m": "",
                    "joint_feature": "corner_interlock",
                    "points": [[radius * math.cos(i * math.tau / 64),
                                radius * math.sin(i * math.tau / 64)] for i in range(64)],
                    "height": (kwargs["interlock_depth"] if front else pocket) + 0.1,
                    "depth": (kwargs["interlock_depth"] if front else pocket) + 0.1,
                    "rot": [0, 0, 0],
                    "pos": [x, y, pos[2] + seam - (0.1 if front else pocket)],
                }
                oobb.append_full(thing, **p3)

    # Front catch and 45-degree ramp use the population dimensions.
    if kwargs.get("catch_tab_height", 0) > 0:
        projection = kwargs["catch_tab_height"]
        ramp = kwargs["catch_tab_ramp_depth"]
        tip_end = ramp + kwargs["catch_tab_depth"]
        wall = kwargs["thickness_wall"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "positive_positive",
            "shape": "polygon",
            "m": "#",
            "height": kwargs["catch_tab_width"],
            "depth": kwargs["catch_tab_width"],
            "points": [
                [-wall, 0],
                [0, 0],
                [projection, ramp],
                [projection, tip_end],
                [-wall, tip_end],
            ],
            "rot": [90, 0, 90],
            "pos": [pos[0] - kwargs["catch_tab_width"] / 2,
                    pos[1] - opening_height / 2, pos[2]],
        }
        oobb.append_full(thing, **p3)

def get_container_cutout_version_1(pos, thing, **kwargs):
    container_depth = kwargs.get("container_depth", 0)
    container_width = kwargs.get("container_width", 0)
    container_height = kwargs.get("container_height", 0)
    container_clearance = kwargs.get("container_clearance", 0)
    thickness_wall = kwargs.get("thickness_wall", 2)
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"rounded_rectangle"
    wid = container_width+container_clearance
    hei = container_height+container_clearance
    dep = container_depth+container_clearance+thickness_wall
    size = [wid, hei, dep]
    p3["size"] = size
    p3["radius"] = 5 - thickness_wall
    pos1 = copy.deepcopy(pos)         
    pos1[2] += 0
    p3["pos"] = pos1
    p3["m"] = "#"
    oobb.append_full(thing,**p3)
    #catch tab
    catch_tab_depth = 1.5
    kwargs["catch_tab_depth"] = catch_tab_depth
    catch_tab_height = 6
    kwargs["catch_tab_height"] = catch_tab_height
    catch_tab_minus = 30
    kwargs["catch_tab_minus"] = catch_tab_minus
    p3["type"] = "positive_positive"
    p3["shape"] = f"rounded_rectangle"
    wid = container_width-catch_tab_minus
    hei = catch_tab_height + thickness_wall
    dep = catch_tab_depth
    size = [wid, hei, dep]
    p3["size"] = size
    p3["radius"] = 2.5
    pos1 = copy.deepcopy(pos)         
    pos1[1] += -container_height/2 - container_clearance/2 + catch_tab_height/2 - thickness_wall
    p3["pos"] = pos1
    p3["m"] = "#"
    oobb.append_full(thing,**p3)
        


# Version 3: independent development copy of the locked version 2 release.

def get_container_cutout_ai_version_3(pos, thing, **kwargs):
    # Preserve the user's two-piece stepped opening. The lip-bearing ledge is
    # at lip_step_y; the reliefs below deliberately avoid that entire shelf.
    opening_width = kwargs["opening_width"]
    opening_height = kwargs["opening_height"]
    depth_total = kwargs["depth_total"]
    depth_lip = kwargs["depth_lip"]
    inset_lip = kwargs["inset_lip"]
    step = kwargs["lip_step_y"]

    # Full-width, 12 mm high channel: same profile and position as the user edit.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width, depth_lip, depth_total + 0.2],
        "radius": kwargs["lip_cutout_radius"],
        "pos": [pos[0], pos[1] - (opening_height - depth_lip) / 2, pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Narrower body opening forms the 5.5 mm shoulders beside the lip.
    p3 = {
        **copy.deepcopy(kwargs),
        "type": "negative",
        "shape": "rounded_rectangle",
        "m": "",
        "size": [opening_width - 2 * inset_lip, opening_height, depth_total + 0.2],
        "radius": kwargs["opening_radius"],
        "pos": [pos[0], pos[1], pos[2] - 0.1],
    }
    oobb.append_full(thing, **p3)

    # Taller containers do not need thick shoulders all the way down the body.
    # Keep only the 100 ml support height, then open to full width for the rest
    # of the cavity, along the ENTIRE insertion depth including the end bands.
    # The small square-bottom cut makes the shoulder end exact; the rounded
    # rectangle preserves the two far corners of the enlarged opening.
    extension = kwargs["body_extension_height"]
    if extension > 0:
        radius = min(kwargs["opening_radius"], extension / 2)
        end_y = pos[1] + kwargs["lip_support_end_y"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "rounded_rectangle",
            "m": "",
            "size": [opening_width, extension, depth_total + 0.2],
            "radius": radius,
            "pos": [pos[0], end_y + extension / 2, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "cube",
            "m": "",
            "size": [opening_width, radius, depth_total + 0.2],
            "pos": [pos[0] - opening_width / 2, end_y, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)

    if kwargs["lightening"] and kwargs["part_role"] == "frame":
        wall = kwargs["thickness_wall"]
        border = kwargs["drawer_border_edge"]
        row_index = kwargs.get("row_index", 0)
        column_index = kwargs.get("column_index", 0)
        bottom = kwargs["relief_start_depth"]
        top = kwargs["body_depth"] + 0.1 if kwargs["split_frame"] else depth_total - kwargs["rear_band"]

        # One broad floor/ceiling window: no longitudinal centre support.
        # A nonzero middle_rib_width optionally restores two windows for trials.
        half = kwargs["shelf_window_width"] / 2
        shoulder = top if kwargs["split_frame"] else top - half * kwargs["roof_slope"]
        offsets = [0]
        if kwargs["middle_rib_width"] > 0:
            offset = (kwargs["middle_rib_width"] + kwargs["shelf_window_width"]) / 2
            offsets = [-offset, offset]
        for side_y in [-1, 1]:
            outside = (side_y == -1 and row_index == 0) or (side_y == 1 and row_index == kwargs["row"] - 1)
            thickness = border if outside else wall
            y = pos[1] + side_y * (opening_height / 2 + thickness / 2)
            for offset in offsets:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": thickness + 0.2,
                    "depth": thickness + 0.2,
                    "points": ([[-half, bottom], [half, bottom], [half, top], [-half, top]]
                               if kwargs["split_frame"] else
                               [[-half, bottom], [half, bottom], [half, shoulder], [0, top], [-half, shoulder]]),
                    "rot": [90, 0, 0],
                    "pos": [pos[0] + offset, y + thickness / 2 + 0.1, pos[2]],
                }
                oobb.append_full(thing, **p3)

        # Separate reliefs BELOW and ABOVE the shelf. The upper cut reaches
        # through the thick shoulder as well as the wall, instead of leaving
        # a large solid block behind a cosmetic outer-wall hole.
        # The shelf's full root is retained from step-1 to step+3 by default.
        zones = [
            {
                "low": -opening_height / 2 + kwargs["side_rail_width"],
                "high": step - kwargs["lip_cutout_radius"],
                "inset": 0,
            },
            {
                "low": step + kwargs["lip_shelf_thickness"],
                "high": opening_height / 2 - kwargs["side_rail_width"],
                "inset": inset_lip,
            },
        ]
        for side_x in [-1, 1]:
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            thickness = border if outside else wall
            for zone in zones:
                half = (zone["high"] - zone["low"]) / 2
                shoulder = top if kwargs["split_frame"] else top - half * kwargs["roof_slope"]
                cut_depth = thickness + zone["inset"] + 0.2
                x = pos[0] + side_x * (opening_width / 2 + (thickness - zone["inset"]) / 2)
                y = pos[1] + (zone["low"] + zone["high"]) / 2
                # Open the upper side relief farther beside the running rail.
                # It closes gradually into the full hardware boss; screw/nut
                # seating faces and every mating feature stay unchanged.
                upper_taper = kwargs["shelf_relief_active"] and zone["inset"] == inset_lip
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "polygon",
                    "m": "",
                    "height": cut_depth,
                    "depth": cut_depth,
                    "points": ([[step + kwargs["running_shelf_thickness"] - (zone["low"] + zone["high"]) / 2, bottom],
                                [half, bottom], [half, top], [-half, top],
                                [-half, kwargs["boss_taper_end"]],
                                [step + kwargs["running_shelf_thickness"] - (zone["low"] + zone["high"]) / 2, kwargs["boss_taper_start"]]]
                               if upper_taper else
                               [[-half, bottom], [half, bottom], [half, top], [-half, top]]
                               if kwargs["split_frame"] else
                               [[-half, bottom], [half, bottom], [half, shoulder], [0, top], [-half, shoulder]]),
                    "rot": [90, 0, 90],
                    "pos": [x - cut_depth / 2, y, pos[2]],
                }
                oobb.append_full(thing, **p3)

    # Remove the depthwise rail at each internal row boundary, including its
    # rounded-corner remnants. The upper cell owns the cut. Full-width removal
    # joins the existing side/floor reliefs while keeping both outer face bands,
    # the front catches and the separate lip-bearing hardware shelves intact.
    if kwargs["internal_lower_supports_removed"] and kwargs.get("row_index", 0) > 0:
        # Overlap adjacent reliefs by 0.1 mm to avoid coplanar slivers.
        rail = kwargs["side_rail_width"]
        wall = kwargs["thickness_wall"]
        width = opening_width + 2 * kwargs["drawer_border_edge"] + 0.2
        bottom = kwargs["relief_start_depth"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "cube",
            "m": "",
            "joint_feature": "removed_internal_lower_support",
            "size": [width, wall + 2 * rail + 0.2, depth_total - bottom + 0.2],
            "pos": [pos[0] - width / 2, pos[1] - opening_height / 2 - wall - rail - 0.1, pos[2] + bottom],
        }
        oobb.append_full(thing, **p3)

    # Extend the protected lip shelf into the joint. Each shared divider has
    # one fixing, not two overlapping screws. No hardware intrudes into the pot
    # cavity: the outside border has been widened to house its own fixing.
    if kwargs["split_frame"] and kwargs["assembly_half"] in ["front", "back"]:
        seam = kwargs["body_depth"]
        for side_x in [-1, 1]:
            column_index = kwargs.get("column_index", 0)
            if side_x == -1 and column_index > 0:
                continue
            outside = (side_x == -1 and column_index == 0) or (side_x == 1 and column_index == kwargs["column"] - 1)
            offset = ((kwargs["drawer_border_edge"] - inset_lip) / 2 if outside
                      else kwargs["thickness_wall"] / 2)
            x = pos[0] + side_x * (opening_width / 2 + offset)
            y = pos[1] + step + kwargs["hardware_axis_height"]
            if kwargs["assembly_half"] == "front":
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "positive",
                    "shape": "cube",
                    "m": "",
                    "size": [kwargs["interlock_width"], kwargs["interlock_height"], kwargs["interlock_depth"] + 0.1],
                    "pos": [x - kwargs["interlock_width"] / 2, y - kwargs["interlock_height"] / 2, pos[2] + seam - 0.1],
                }
                oobb.append_full(thing, **p3)
            else:
                width = kwargs["interlock_width"] + 2 * kwargs["interlock_clearance"]
                height = kwargs["interlock_height"] + 2 * kwargs["interlock_clearance"]
                pocket = kwargs["interlock_depth"] + kwargs["interlock_end_clearance"]
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative",
                    "shape": "cube",
                    "m": "",
                    "size": [width, height, pocket + 0.1],
                    "pos": [x - width / 2, y - height / 2, pos[2] + seam - pocket],
                }
                oobb.append_full(thing, **p3)

            # OOBB's current API consumes clearance=["top", "bottom"]. Keep
            # the explicitly requested boolean flags too. A 16 mm under-head
            # length leaves 13 mm to the near nut face and a 3 mm nut pocket.
            # The front head seat lies 6 mm before the seam. The rear's same
            # screw origin is 6 mm beyond its seam in local print coordinates.
            front = kwargs["assembly_half"] == "front"
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative",
                "shape": "oobb_screw_socket_cap",
                "m": "",
                "radius_name": "m3",
                "depth": kwargs["screw_length"],
                "include_nut": True,
                "top_clearance": True,
                "bottom_clearance": True,
                "clearance": ["top", "bottom"],
                "overhang": True,
                "rot": [0, 180, 0] if front else [0, 0, 0],
                "pos": [x, y, pos[2] + seam + (-kwargs["screw_head_seat_offset"] if front else kwargs["screw_head_seat_offset"])],
            }
            oobb.append_full(thing, **p3)

        # The other mating islands are the retained top/bottom corner rails.
        # Each cell owns its left/bottom junctions, plus the far outside edges;
        # this produces one peg/socket per junction without duplicate features.
        # Internal row joints are offset toward the rounded top of the lower
        # opening, where enough material remains around the socket. These pegs
        # stay inside existing rail material and do not reduce drawer clearance.
        column_index = kwargs.get("column_index", 0)
        row_index = kwargs.get("row_index", 0)
        for side_x in [-1, 1]:
            if side_x == 1 and column_index < kwargs["column"] - 1:
                continue
            outside_x = side_x == 1 or column_index == 0
            border_x = kwargs["drawer_border_edge"] if outside_x else kwargs["thickness_wall"]
            x = pos[0] + side_x * (opening_width / 2 + border_x / 2)
            for side_y in [-1, 1]:
                if side_y == 1 and row_index < kwargs["row"] - 1:
                    continue
                junction_row = row_index + (1 if side_y == 1 else 0)
                if junction_row not in kwargs["corner_interlock_rows"]:
                    continue
                outside_y = side_y == 1 or row_index == 0
                border_y = kwargs["drawer_border_edge"] if outside_y else kwargs["thickness_wall"]
                y = pos[1] + side_y * (opening_height / 2 + border_y / 2)
                if not outside_y:
                    y -= kwargs["thickness_wall"] / 2
                front = kwargs["assembly_half"] == "front"
                radius = kwargs["corner_interlock_diameter"] / 2
                if not front:
                    radius += kwargs["interlock_clearance"]
                pocket = kwargs["interlock_depth"] + kwargs["interlock_end_clearance"]
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "positive" if front else "negative",
                    "shape": "polygon",
                    "m": "",
                    "joint_feature": "corner_interlock",
                    "points": [[radius * math.cos(i * math.tau / 64),
                                radius * math.sin(i * math.tau / 64)] for i in range(64)],
                    "height": (kwargs["interlock_depth"] if front else pocket) + 0.1,
                    "depth": (kwargs["interlock_depth"] if front else pocket) + 0.1,
                    "rot": [0, 0, 0],
                    "pos": [x, y, pos[2] + seam - (0.1 if front else pocket)],
                }
                oobb.append_full(thing, **p3)

    # Front catch and 45-degree ramp use the population dimensions.
    if kwargs.get("catch_tab_height", 0) > 0:
        projection = kwargs["catch_tab_height"]
        ramp = kwargs["catch_tab_ramp_depth"]
        tip_end = ramp + kwargs["catch_tab_depth"]
        wall = kwargs["thickness_wall"]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "positive_positive",
            "shape": "polygon",
            "m": "#",
            "height": kwargs["catch_tab_width"],
            "depth": kwargs["catch_tab_width"],
            "points": [
                [-wall, 0],
                [0, 0],
                [projection, ramp],
                [projection, tip_end],
                [-wall, tip_end],
            ],
            "rot": [90, 0, 90],
            "pos": [pos[0] - kwargs["catch_tab_width"] / 2,
                    pos[1] - opening_height / 2, pos[2]],
        }
        oobb.append_full(thing, **p3)



def get_container_cutout_ai_version_4(pos, thing, **kwargs):
    component = kwargs.get("modular_component", "face_plate")
    if component == "face_plate":
        # Preserve the user's two-piece stepped opening. The lip-bearing ledge is
        # at lip_step_y; the reliefs below deliberately avoid that entire shelf.
        opening_width = kwargs["opening_width"]
        opening_height = kwargs["opening_height"]
        depth_total = kwargs["plate_print_depth"]
        depth_lip = kwargs["depth_lip"]
        inset_lip = kwargs["inset_lip"]
        step = kwargs["lip_step_y"]

        # Full-width, 12 mm high channel: same profile and position as the user edit.
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "rounded_rectangle",
            "m": "",
            "size": [opening_width, depth_lip, depth_total + 0.2],
            "radius": kwargs["lip_cutout_radius"],
            "pos": [pos[0], pos[1] - (opening_height - depth_lip) / 2, pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)

        # Narrower body opening forms the 5.5 mm shoulders beside the lip.
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative",
            "shape": "rounded_rectangle",
            "m": "",
            "size": [opening_width - 2 * inset_lip, opening_height, depth_total + 0.2],
            "radius": kwargs["opening_radius"],
            "pos": [pos[0], pos[1], pos[2] - 0.1],
        }
        oobb.append_full(thing, **p3)

        # Taller containers do not need thick shoulders all the way down the body.
        # Keep only the 100 ml support height, then open to full width for the rest
        # of the cavity, along the ENTIRE insertion depth including the end bands.
        # The small square-bottom cut makes the shoulder end exact; the rounded
        # rectangle preserves the two far corners of the enlarged opening.
        extension = kwargs["body_extension_height"]
        if extension > 0:
            radius = min(kwargs["opening_radius"], extension / 2)
            end_y = pos[1] + kwargs["lip_support_end_y"]
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative",
                "shape": "rounded_rectangle",
                "m": "",
                "size": [opening_width, extension, depth_total + 0.2],
                "radius": radius,
                "pos": [pos[0], end_y + extension / 2, pos[2] - 0.1],
            }
            oobb.append_full(thing, **p3)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative",
                "shape": "cube",
                "m": "",
                "size": [opening_width, radius, depth_total + 0.2],
                "pos": [pos[0] - opening_width / 2, end_y, pos[2] - 0.1],
            }
            oobb.append_full(thing, **p3)


        # Only the front receives the catch and its reverse ramp. The rear
        # opening stays clear; mounting keys and countersinks are unchanged.
        if kwargs.get("include_forward_lip", True):
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "positive_positive", "shape": "polygon", "m": "",
                "height": kwargs["catch_tab_width"], "depth": kwargs["catch_tab_width"],
                "points": [[-kwargs["thickness_wall"], 0], [0, 0],
                           [kwargs["catch_tab_height"], kwargs["catch_tab_ramp_depth"]],
                           [kwargs["catch_tab_height"], kwargs["plate_thickness"]],
                           [0, kwargs["plate_thickness"] + kwargs["inner_guide_depth"]],
                           [-kwargs["thickness_wall"], kwargs["plate_thickness"]]],
                "rot": [90, 0, 90],
                "pos": [pos[0] - kwargs["catch_tab_width"]/2, pos[1] - opening_height/2, pos[2]],
            }
            oobb.append_full(thing, **p3)

    elif component == "plate_mounts":
        for rail in kwargs["rail_positions"]:
            # Key grows from the inside of the plate. Its pointed roof lets
            # the receiving rail socket print on its long bearing face.
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "positive", "shape": "polygon", "m": "",
                "points": kwargs["key_points"],
                "height": kwargs["modular_key_depth"] + 0.1,
                "depth": kwargs["modular_key_depth"] + 0.1,
                "pos": [rail["x"], rail["y"], kwargs["plate_thickness"] - 0.1],
                "rot": [0, 0, 0],
            }
            oobb.append_full(thing, **p3)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "oobb_screw_countersunk", "m": "",
                "radius_name": "m3", "depth": kwargs["modular_screw_length"],
                "include_nut": False, "clearance": ["top"], "overhang": True,
                "rot": [0, 180, 0],
                "pos": [rail["x"], rail["y"] + kwargs["nut_axis_height"], 0],
            }
            oobb.append_full(thing, **p3)

    elif component in ["rail", "bottom_rail"]:
        length = kwargs["rail_length"]
        axis = kwargs["nut_axis_height"]
        running = kwargs["bottom_rail_running_height"] if component == "bottom_rail" else kwargs["rail_running_height"]
        band = kwargs["rail_end_band"]
        taper = kwargs["rail_taper_run"]
        if length > 2 * (band + taper) + 1:
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "polygon", "m": "",
                "points": [[kwargs["rail_height"] + 0.1, band],
                           [kwargs["rail_height"] + 0.1, length - band],
                           [running, length - band - taper], [running, band + taper]],
                "height": kwargs["rail_width"] + 0.2, "depth": kwargs["rail_width"] + 0.2,
                "rot": [90, 0, 90], "pos": [-kwargs["rail_width"]/2 - 0.1, 0, 0],
            }
            oobb.append_full(thing, **p3)
        for rear in [False, True]:
            pocket = kwargs["modular_key_depth"] + kwargs["modular_key_end_clearance"]
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "polygon", "m": "",
                "points": kwargs["socket_points"],
                "height": pocket + 0.1, "depth": pocket + 0.1,
                "pos": [0, 0, length - pocket if rear else -0.1], "rot": [0, 0, 0],
            }
            oobb.append_full(thing, **p3)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cylinder", "m": "",
                "r": oobb.gv("hole_radius_m3", "3dpr"),
                "h": kwargs["nut_far"] + 1.1,
                "pos": [0, axis, length - kwargs["nut_far"] - 1 if rear else -0.1],
            }
            oobb.append_full(thing, **p3)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "oobb_nut", "m": "",
                "radius_name": "m3", "depth": kwargs["nut_depth"],
                "overhang": True, "clearance": kwargs["nut_side_clearance"],
                "pos": [0, axis, length - kwargs["nut_far"] if rear else kwargs["nut_near"]],
                "rot": [0, 0, 0],
            }
            oobb.append_full(thing, **p3)
    else:
        raise ValueError(f"Unknown modular component: {component}")


def get_container_cutout_ai_version_5(pos, thing, **kwargs):
    # All coupon openings, spring reliefs, hooks and locking-key details stay
    # together here. X/across, Y/rail height, Z/insertion; rails print on Y=0.
    p = kwargs
    component = p["connector_component"]
    design = p["connector_design"]
    clearance = p["connector_clearance"]
    sides = [-1] if design == "snap_single" else [-1, 1]
    if component == "plate":
        if design == "snap_recessed_twin":
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cube", "m": "",
                "size": [2*(p["snap_arm_outer"]+clearance),
                         p["rail_height"]+2*clearance,p["plate_thickness"]+0.2],
                "pos": [-p["snap_arm_outer"]-clearance,-clearance,-0.1],
            }
            oobb.append_full(thing, **p3)
            # Square ledges stay inside the plate; the outside opening gives
            # inspection access, but the hooks never emerge beyond that face.
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cube", "m": "",
                "size": [2*p["receiver_pocket_half_width"],
                         p["rail_height"]+2*clearance,p["receiver_shoulder_z"]+0.1],
                "pos": [-p["receiver_pocket_half_width"],-clearance,-0.1],
            }
            oobb.append_full(thing, **p3)
        elif design == "snap_key":
            through_clearance = p.get("through_clearance", clearance)
            height_clearance = p.get("through_height_clearance", clearance)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cube", "m": "",
                "size": [2*(p["key_tongue_half_width"]+through_clearance),
                         p["rail_height"]+2*height_clearance, p["plate_thickness"]+0.2],
                "pos": [-p["key_tongue_half_width"]-through_clearance,-height_clearance,-0.1],
            }
            oobb.append_full(thing, **p3)
        else:
            # Blind rigid guide supports lateral loads separately from latches.
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cube", "m": "",
                "size": [2*(p["guide_half_width"]+clearance),
                         p["rail_height"]+2*clearance, p["guide_depth"]+clearance+0.1],
                "pos": [-p["guide_half_width"]-clearance,-clearance,
                        p["plate_thickness"]-p["guide_depth"]-clearance],
            }
            oobb.append_full(thing, **p3)
            for side in sides:
                outer = p["snap_arm_outer"]+clearance
                inner = (p["snap_arm_outer"]-p["arm_thickness"]-clearance
                         -p["insertion_deflection"]-0.05)
                # Open into the blind guide pocket, avoiding a sub-line-width
                # web between adjacent cuts. The outer catch shoulder stays intact.
                inner = min(inner, p["guide_half_width"]+clearance-0.15)
                # Open-through window leaves a flat outside retaining shoulder.
                # Only the INNER entrance flares, at 45 degrees, for insertion.
                points = [[side*inner,-0.1],[side*outer,-0.1],
                          [side*outer,p["plate_thickness"]-0.65],
                          [side*(outer+0.75),p["plate_thickness"]+0.1],
                          [side*(inner-0.75),p["plate_thickness"]+0.1],
                          [side*inner,p["plate_thickness"]-0.65]]
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative", "shape": "polygon", "m": "",
                    "points": [[round(x,6),round(z,6)] for x,z in points],
                    "height": p["snap_arm_height"]+2*clearance,
                    "depth": p["snap_arm_height"]+2*clearance,
                    "rot": [90,0,0], "pos": [0,p["snap_arm_height"]+clearance,0],
                }
                oobb.append_full(thing, **p3)
    elif component == "rail":
        if design == "snap_recessed_twin":
            # Two independent tabs with no central guide or loose locking key.
            for side in [-1,1]:
                points = [
                    [p["snap_arm_outer"]-0.3,p["hook_tip_z"]-0.1],
                    [p["snap_arm_outer"]-0.3,p["hook_tip_z"]],
                    [p["snap_arm_outer"]+p["hook_projection"],p["hook_shoulder_z"]-0.3],
                    [p["snap_arm_outer"]+p["hook_projection"],p["hook_shoulder_z"]],
                    [p["snap_arm_outer"],p["hook_shoulder_z"]],
                    [p["snap_arm_outer"],0],
                    # Full-width beam seats directly against the entry face.
                    [p["rail_width"]/2+0.1,0],
                    [p["rail_width"]/2+0.1,p["hook_tip_z"]-0.1],
                ]
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative", "shape": "polygon", "m": "",
                    "points": [[round(side*x,6),round(z,6)] for x,z in points],
                    "height": p["rail_height"]+0.2, "depth": p["rail_height"]+0.2,
                    "rot": [90,0,0], "pos": [0,p["rail_height"]+0.1,0],
                }
                oobb.append_full(thing, **p3)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cube", "m": "",
                "size": [2*p["open_center_half_width"],p["rail_height"]+0.2,
                         p["root_distance"]-p["hook_tip_z"]+0.1],
                "pos": [-p["open_center_half_width"],-0.1,p["hook_tip_z"]-0.1],
            }
            oobb.append_full(thing, **p3)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cylinder", "m": "",
                "r": p["open_center_half_width"], "h": p["rail_height"]+0.2,
                "rot": [90,0,0],
                "pos": [0,p["rail_height"]+0.1,p["root_distance"]],
            }
            oobb.append_full(thing, **p3)
        elif design == "snap_key":
            if "through_taper_length" in p:
                # Full-height X/Z wedge prints on its long flat Y face.
                # Only the final 6 mm inside the plate widens; the key and
                # its shoulders outside the plate keep their original fit.
                half = p["key_tongue_half_width"]
                seat = half+p["through_clearance"]+p["through_seat_interference"]
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "positive", "shape": "polygon", "m": "",
                    "points": [
                        [-half,-p["key_tongue_depth"]],
                        [half,-p["key_tongue_depth"]],
                        [half,-p["through_taper_length"]],
                        [seat,0], [seat,0.1],
                        [-seat,0.1], [-seat,0],
                        [-half,-p["through_taper_length"]],
                    ],
                    "height": p["rail_height"], "depth": p["rail_height"],
                    "rot": [90,0,0], "pos": [0,p["rail_height"],0],
                }
                p3["points"] = [[round(x,6),round(z,6)] for x,z in p3["points"]]
            else:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "positive", "shape": "cube", "m": "",
                    "size": [2*p["key_tongue_half_width"],p["rail_height"],p["key_tongue_depth"]+0.1],
                    "pos": [-p["key_tongue_half_width"],0,-p["key_tongue_depth"]],
                }
            oobb.append_full(thing, **p3)
            # Transverse key slot: a short 2.9 mm bridge in the rail's print pose.
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cube", "m": "",
                "size": [2*p["key_tongue_half_width"]+0.2,p["key_height"]+2*clearance,
                         2*(p["key_half_width"]+clearance)],
                "pos": [-p["key_tongue_half_width"]-0.1,
                        (p["rail_height"]-p["key_height"])/2-clearance,
                        p["key_z"]-p["key_half_width"]-clearance],
            }
            oobb.append_full(thing, **p3)
        else:
            # Remove the full-height side bands so no roof welds a spring arm
            # back to the rail. A central full-height spine carries the guide.
            for side in [-1,1]:
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "negative", "shape": "cube", "m": "",
                    "size": [p["rail_width"]/2-p["guide_half_width"]+0.1,
                             p["rail_height"]+0.2,p["root_distance"]+0.1],
                    "pos": [p["guide_half_width"] if side == 1 else -p["rail_width"]/2-0.1,
                            -0.1,-0.1],
                }
                oobb.append_full(thing, **p3)
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "positive", "shape": "cube", "m": "",
                "size": [2*p["guide_half_width"],p["rail_height"],p["guide_depth"]+0.1],
                "pos": [-p["guide_half_width"],0,-p["guide_depth"]],
            }
            oobb.append_full(thing, **p3)
            for side in sides:
                outer = p["snap_arm_outer"]
                inner = outer-p["arm_thickness"]
                root = p["root_distance"]
                radius = p["root_radius"]
                points = [[inner,p["hook_tip_z"]],[outer-0.25,p["hook_tip_z"]],
                          [outer+p["hook_projection"],p["hook_shoulder_z"]-0.3],
                          [outer+p["hook_projection"],p["hook_shoulder_z"]],
                          [outer,p["hook_shoulder_z"]],[outer,root+0.5],
                          [inner-radius,root+0.5]]
                # Quarter-circle root fillet, sampled finely enough for this scale.
                for angle in range(90,-1,-10):
                    theta = math.radians(angle)
                    points.append([inner-radius+radius*math.cos(theta),
                                   root-radius+radius*math.sin(theta)])
                p3 = {
                    **copy.deepcopy(kwargs),
                    "type": "positive_positive", "shape": "polygon", "m": "",
                    "points": [[round(side*x,6),round(z,6)] for x,z in points],
                    "height": p["snap_arm_height"], "depth": p["snap_arm_height"],
                    "rot": [90,0,0], "pos": [0,p["snap_arm_height"],0],
                }
                oobb.append_full(thing, **p3)
    elif component == "key":
        # Independent planar fork: squeeze during side insertion, then two
        # square shoulders recover beyond the tongue to retain the locking key.
        outer = p["key_half_width"]
        inner = outer-p["key_arm_thickness"]
        root = p["key_head_x"]+p.get("key_head_length",2)
        shoulder = p["key_shoulder_x"]
        tip = shoulder+p["hook_ramp_length"]
        for side in [-1,1]:
            points = [[root,outer],[shoulder,outer],
                      [shoulder,outer+p["hook_projection"]],
                      [shoulder+p.get("key_hook_flat",0.3),outer+p["hook_projection"]],
                      [tip,outer-p.get("key_tip_chamfer",0.2)],
                      [tip+0.1,outer-p.get("key_tip_chamfer",0.2)],
                      [tip+0.1,outer+p["hook_projection"]+0.1],
                      [root,outer+p["hook_projection"]+0.1]]
            if p.get("sample_number") in [20,21,22] or p.get("tight_key_trial",False):
                # Continue the ramp beyond the envelope. A kink exactly at
                # its end plane creates sub-STL-resolution slivers at larger
                # scales when cube length + origin rounds differently.
                slope = (p["hook_projection"]+p["key_tip_chamfer"])/(p["hook_ramp_length"]-p["key_hook_flat"])
                points[4:6] = [[tip+0.1,outer-p["key_tip_chamfer"]-0.1*slope]]
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "polygon", "m": "",
                "points": [[round(x,6),round(side*z,6)] for x,z in points],
                "height": p["key_height"]+0.2, "depth": p["key_height"]+0.2,
                "rot": [90,0,0], "pos": [0,p["key_height"]+0.1,0],
            }
            oobb.append_full(thing, **p3)
        radius = p["key_root_radius"]
        arc = []
        for angle in range(180,89,-10):
            theta = math.radians(angle)
            arc.append([root+radius+radius*math.cos(theta),
                        inner-radius+radius*math.sin(theta)])
        points = arc + [[tip+0.1,inner],[tip+0.1,-inner]] + [[x,-z] for x,z in reversed(arc)]
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative", "shape": "polygon", "m": "",
            "points": [[round(x,6),round(z,6)] for x,z in points],
            "height": p["key_height"]+0.2, "depth": p["key_height"]+0.2,
            "rot": [90,0,0], "pos": [0,p["key_height"]+0.1,0],
        }
        oobb.append_full(thing, **p3)
    else:
        raise ValueError(f"Unknown connector component: {component}")
    if p.get("sample_number") and component in ["rail", "plate"]:
        # Rail's local +Y becomes print +Z. Rx(-90) makes this engraving
        # upright on the print bed after the rail's Rx(+90) print rotation.
        p3 = {
            **copy.deepcopy(kwargs),
            "type": "negative", "shape": "text", "m": "",
            "text": str(p["sample_number"]),
            "font": "Arial:style=Bold",
            "size": p["number_size"] if component == "rail" else p.get("plate_number_size",2.5),
            "height": p["number_depth"]+0.1, "depth": p["number_depth"]+0.1,
            "halign": "center", "valign": "center",
            "rot": [-90,0,0] if component == "rail" else [0,0,0],
            "pos": [0,p["rail_height"]-p["number_depth"],p["number_rail_z"]]
                   if component == "rail" else [p.get("plate_number_x",-5.5),8.5,p["plate_thickness"]-p["number_depth"]],
        }
        if design == "snap_recessed_twin" and component == "plate":
            # Plate is flipped in its print view; recess the number on +Z there.
            p3["pos"] = [6,8.5,p["number_depth"]]
            p3["rot"] = [0,180,0]
            p3["size"] = 1.8
        oobb.append_full(thing, **p3)
    # One/two/three edge notches identify A/B/C after removing them from the bed.
    # They are confined to the plate border or the rail's solid rear grip.
    if component in ["plate", "rail"]:
        for index in range({"snap_single":1,"snap_twin":2,"snap_key":3,"snap_recessed_twin":0}[design]):
            p3 = {
                **copy.deepcopy(kwargs),
                "type": "negative", "shape": "cylinder", "m": "",
                "r": 0.6,
                "h": p["plate_thickness"]+0.2 if component == "plate" else p["rail_height"]+0.2,
                "rot": [0,0,0] if component == "plate" else [90,0,0],
                "pos": [-p["coupon_width"]/2,3+2*index,-0.1] if component == "plate"
                       else [p["rail_width"]/2,p["rail_height"]+0.1,p["test_rail_length"]-2-2*index],
            }
            oobb.append_full(thing, **p3)

def get_container_cutout_ai_version_5_tiled(pos, thing, **kwargs):
    # Complete tiled plate / rail cuts live here. V4 supplies only the unchanged
    # tray profile and screw primitive dimensions; coupon 19 supplies its tabs.
    p = kwargs
    component = p['tiled_component']
    if component == 'plate':
        bounds = p['tile_bounds']
        for row in range(p['row']):
            for col in range(p['column']):
                cell = [-p['natural_width']/2+p['drawer_border_edge']+p['opening_width']/2+col*p['pitch_x'],
                        -p['natural_height']/2+p['drawer_border_edge']+p['opening_height']/2+row*p['pitch_y'],0]
                if (cell[0]+p['opening_width']/2 < bounds[0] or cell[0]-p['opening_width']/2 > bounds[2] or
                    cell[1]+p['opening_height']/2 < bounds[1] or cell[1]-p['opening_height']/2 > bounds[3]):
                    continue
                get_container_cutout_ai_version_4(cell,thing,**dict(
                    p,modular_component='face_plate',row_index=row,column_index=col,
                    include_forward_lip=False))
                if p['include_forward_lip']:
                    # Six mm of tray retention across the panel depth. Both print
                    # faces have a bed-supported edge; short 45-degree chamfers
                    # soften the top without a projecting reverse guide.
                    height = p['catch_tab_height']
                    depth = p['stop_thickness']
                    chamfer = p['stop_edge_chamfer']
                    p3 = {
                        **copy.deepcopy(p),'type':'positive_positive','shape':'polygon','m':'',
                        'points':[[-p['thickness_wall'],0],[height-chamfer,0],
                                  [height,chamfer],[height,depth-chamfer],
                                  [height-chamfer,depth],[-p['thickness_wall'],depth]],
                        'height':p['catch_tab_width'],'depth':p['catch_tab_width'],
                        'rot':[90,0,90],
                        'pos':[cell[0]-p['catch_tab_width']/2,cell[1]-p['opening_height']/2,0],
                    }
                    oobb.append_full(thing,**p3)
        # Open the extra side margins into short windows, retaining the outside
        # border, the rail walls and a full cross-tie at each mount height.
        left = -p['width_total']/2+max(p['drawer_border_edge'],p['attachment_border_band'])
        right = min(p['x_mounts'])-p['rail_width']/2-1.5
        if right-left >= 4:
            levels = sorted({r['y'] for r in p['rail_positions']})
            for lo,hi in zip(levels,levels[1:]):
                bottom,top = lo+p['rail_height'],hi
                if top-bottom <= 2:
                    continue
                for side in [-1,1]:
                    x0 = left if side == -1 else -right
                    p3 = {
                        **copy.deepcopy(p),'type':'negative','shape':'cube','m':'',
                        'size':[right-left,top-bottom,p['plate_print_depth']+0.2],
                        'pos':[x0,bottom,-0.1],
                    }
                    oobb.append_full(thing,**p3)
        if p.get('include_rear_attachments',False):
            for attachment in p['rear_attachments']:
                x,y = attachment['x'],attachment['y']
                if not bounds[0]-7 <= x <= bounds[2]+7 or not bounds[1]-7 <= y <= bounds[3]+7:
                    continue
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'oobb_hole','m':'',
                    'radius_name':'m6','depth':p['plate_thickness']+0.2,
                    'pos':[x,y,-0.1],
                }
                oobb.append_full(thing,**p3)
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'oobb_nut','m':'',
                    'radius_name':'m6','depth':p['attachment_nut_depth'],
                    'overhang':True,'clearance':'','rot':[0,0,attachment['rotation']],
                    'pos':[x,y,p['plate_thickness']-p['attachment_nut_depth']],
                }
                oobb.append_full(thing,**p3)
        for rail in p['rail_positions']:
            if not bounds[0]-6 <= rail['x'] <= bounds[2]+6 or not bounds[1]-10 <= rail['y'] <= bounds[3]+1:
                continue
            if rail['connection'] == 'screw':
                # Flat plate seat on either print face. The laps and adjacent
                # snap mounts align the grid; no projecting plate key.
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'oobb_screw_countersunk','m':'',
                    'radius_name':'m3','depth':p['modular_screw_length'],
                    'include_nut':False,'clearance':['top'],'overhang':True,
                    'rot':[0,180,0],'pos':[rail['x'],rail['axis_y'],0],
                }
                oobb.append_full(thing,**p3)
            else:
                # The old hole crossed the narrow vertical spine below the
                # shelf step. A 45-degree floor retains that spine in BOTH lap
                # layers, and matches a bed-supported bevel under the tabs.
                clearance = p['snap_clearance']
                entry = p['snap_profile']['snap_arm_outer']+clearance
                pocket = entry+p['snap_hook_projection']
                ledge = p['snap_receiver_shoulder']
                land = p['snap_ledge_land']
                ramp = p['snap_hook_projection']-land
                if p.get('snap_inner_web_height',0)>0:
                    outside=p['snap_tip_floor']-clearance
                    slope=(outside-p['snap_inner_web_height'])/p['plate_thickness']
                    floor_points=[[outside+slope*.1,-.1],
                                  [p['rail_height']+clearance,-.1],
                                  [p['rail_height']+clearance,p['plate_thickness']+.1],
                                  [p['snap_inner_web_height']-slope*.1,p['plate_thickness']+.1]]
                else:
                    floor_points=[[p['snap_tip_floor']+0.1-clearance,-0.1],
                                  [p['rail_height']+clearance,-0.1],
                                  [p['rail_height']+clearance,p['plate_thickness']+0.1],
                                  [-clearance,p['plate_thickness']+0.1],
                                  [-clearance,p['snap_tip_floor']]]
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
                    'points':floor_points,
                    'height':2*entry,'depth':2*entry,'rot':[90,0,90],
                    'pos':[rail['x']-entry,rail['y'],0],
                }
                oobb.append_full(thing,**p3)
                cavity = oobb.get_default_thing(type='bevelled_snap_pocket')
                p3 = {
                    **copy.deepcopy(p),'type':'positive','shape':'polygon','m':'',
                    'points':[[-pocket,-0.1],[pocket,-0.1],[pocket,ledge],
                              [pocket-land,ledge],[entry-0.03,ledge+ramp+0.03],
                              [-entry+0.03,ledge+ramp+0.03],[-pocket+land,ledge],[-pocket,ledge]],
                    'height':p['rail_height']+2*clearance,
                    'depth':p['rail_height']+2*clearance,
                    'rot':[90,0,0],
                    'pos':[rail['x'],rail['y']+p['rail_height']+clearance,0],
                }
                oobb.append_full(cavity,**p3)
                if p.get('snap_inner_web_height',0)>0:
                    floor_clip=[[-1,-1],[outside+slope+.01,-1],
                                [outside-slope*(p['plate_thickness']+1)+.01,p['plate_thickness']+1],
                                [-1,p['plate_thickness']+1]]
                else:
                    floor_clip=[[-1,-1],[p['snap_tip_floor']+1-clearance+0.01,-1],
                                [-clearance+0.01,p['snap_tip_floor']],[-1,p['snap_tip_floor']]]
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
                    # Overlap the compound pocket cut without opening the web.
                    'points':floor_clip,
                    'height':2*pocket+0.2,'depth':2*pocket+0.2,'rot':[90,0,90],
                    'pos':[rail['x']-pocket-0.1,rail['y'],0],
                }
                oobb.append_full(cavity,**p3)
                thing['components'].append({
                    'type':'rotation','typetype':'negative','rot':[0,0,0],
                    'pos':[0,0,0],'objects':cavity['components'],
                })
    elif component == 'tile_mask':
        extent = max(p['width_total'],p['height_total'])+100
        for layer,b in enumerate(p['tile_layers']):
            z0 = -1 if layer==0 else p['plate_thickness']/2-p['tile_layer_clearance']/2
            z1 = p['plate_thickness']/2+p['tile_layer_clearance']/2 if layer==0 else p['plate_print_depth']+1
            for low,size in [
                ([-extent,-extent],[b[0]+extent,2*extent]),
                ([b[2],-extent],[extent-b[2],2*extent]),
                ([-extent,-extent],[2*extent,b[1]+extent]),
                ([-extent,b[3]],[2*extent,extent-b[3]]),
            ]:
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'cube','m':'',
                    'size':[size[0],size[1],z1-z0], 'pos':[low[0],low[1],z0],
                }
                oobb.append_full(thing,**p3)
            for b in p['tile_notches'][layer]:
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'cube','m':'',
                    'size':[b[2]-b[0],b[3]-b[1],z1-z0],
                    'pos':[b[0],b[1],z0],
                }
                oobb.append_full(thing,**p3)
        # Keep the front catch ramp, but finish its inner face flush. A
        # protruding reverse guide would hold an inside-down tile off the bed.
        p3 = {
            **copy.deepcopy(p),'type':'negative','shape':'cube','m':'',
            'size':[2*extent,2*extent,p['plate_print_depth']+1],
            'pos':[-extent,-extent,p['plate_thickness']],
        }
        oobb.append_full(thing,**p3)
    elif component.startswith('screw_'):
        # Retain the proven screw/nut placement, with a solid flat end seat
        # instead of the old socket for the now-removed projecting plate key.
        length,axis = p['rail_length'],p['nut_axis_height']
        running = p['bottom_rail_running_height'] if component=='screw_bottom_rail' else p['rail_running_height']
        band,taper = p['rail_end_band'],p['rail_taper_run']
        p3 = {
            **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
            'points':[[p['rail_height']+0.1,band],[p['rail_height']+0.1,length-band],
                      [running,length-band-taper],[running,band+taper]],
            'height':p['rail_width']+0.2,'depth':p['rail_width']+0.2,
            'rot':[90,0,90],'pos':[-p['rail_width']/2-0.1,0,0],
        }
        oobb.append_full(thing,**p3)
        for rear in [False,True]:
            p3 = {
                **copy.deepcopy(p),'type':'negative','shape':'cylinder','m':'',
                'r':oobb.gv('hole_radius_m3','3dpr'),'h':p['nut_far']+1.1,
                'pos':[0,axis,length-p['nut_far']-1 if rear else -0.1],
            }
            oobb.append_full(thing,**p3)
            p3 = {
                **copy.deepcopy(p),'type':'negative','shape':'oobb_nut','m':'',
                'radius_name':'m3','depth':p['nut_depth'],'overhang':True,
                'clearance':p['nut_side_clearance'],'rot':[0,0,0],
                'pos':[0,axis,length-p['nut_far'] if rear else p['nut_near']],
            }
            oobb.append_full(thing,**p3)
    elif component.startswith('snap_'):
        import working_scad as drawing
        source = copy.deepcopy(p['snap_profile'])
        source.update(connector_clearance=p['snap_clearance'],hook_projection=p['snap_hook_projection'])
        snap = drawing.get_ai_version_5_parameters(**source)
        snap.update(sample_number=0,connector_component='rail',
                    root_distance=p['snap_root_distance'],
                    hook_shoulder_z=-p['snap_shoulder_depth'],
                    hook_tip_z=-p['snap_tip_length'])
        if p.get('v6_clearance_trial',False):
            # Coupon-only override AFTER reading the locked profile. The
            # receiver and production profile keep their selected dimensions.
            snap['hook_projection']=p['clearance_trial']['hook_projection']
        elif p.get('v6_selected_latch',False):
            snap['hook_projection']=p['selected_rail_fit']['hook_projection']
        for rear in [False,True]:
            negative = oobb.get_default_thing(type='tab_cuts')
            get_container_cutout_ai_version_5([0,0,0],negative,**snap)
            objects = negative['components']
            while any(isinstance(obj,list) for obj in objects):
                objects = [item for obj in objects for item in (obj if isinstance(obj,list) else [obj])]
            negative['components'] = objects
            for obj in objects:
                if obj['type'] not in ['negative','n']:
                    raise ValueError('Snap envelope must be carved only by negatives')
                obj['type']='positive'
            thing['components'].append({
                'type':'rotation','typetype':'negative','rot':[0,180,0] if rear else [0,0,0],
                'pos':[0,0,p['rail_length'] if rear else 0],'objects':negative['components'],
            })
            if p.get('snap_inner_web_height',0)>0:
                slope=p['snap_bevel_slope']
                points=[[-.1,-p['plate_thickness']-.1],
                        [p['snap_tip_floor']+slope*.1,-p['plate_thickness']-.1],
                        [p['snap_tip_root_floor'],0],[-.1,0]]
            else:
                points = [[-0.1,-p['plate_thickness']-0.1],
                          [p['snap_tip_floor']+0.1,-p['plate_thickness']-0.1],
                          [0,-p['plate_thickness']+p['snap_tip_floor']],
                          [-0.1,-p['plate_thickness']+p['snap_tip_floor']]]
            p3 = {
                **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
                'points':[[y,p['rail_length']-z if rear else z] for y,z in points],
                'height':p['rail_width']+0.2,'depth':p['rail_width']+0.2,
                'rot':[90,0,90],'pos':[-p['rail_width']/2-0.1,0,0],
            }
            oobb.append_full(thing,**p3)
            # Preserve the selected arm thickness inside the beam, not just
            # at the short exposed tips. Outer strips remain rigid bearing
            # edges; rounded-ended slots separate them from the spring arms.
            outer = p['snap_profile']['snap_arm_outer']
            slot = p['snap_root_relief_width']
            root = p['snap_root_distance']
            for side in [-1,1]:
                # Overlap the round end beyond its centre to avoid coincident
                # root planes with the central slot in the exported mesh.
                points = [[side*outer,-0.1],[side*(outer+slot),-0.1],
                          [side*(outer+slot),root+0.05],[side*outer,root+0.05]]
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
                    'points':[[x,p['rail_length']-z if rear else z] for x,z in points],
                    'height':p['rail_height']+0.2,'depth':p['rail_height']+0.2,
                    'rot':[90,0,0],'pos':[0,p['rail_height']+0.1,0],
                }
                oobb.append_full(thing,**p3)
                p3 = {
                    **copy.deepcopy(p),'type':'negative','shape':'cylinder','m':'',
                    'r':slot/2,'h':p['rail_height']+0.2,'rot':[90,0,0],
                    'pos':[side*(outer+slot/2),p['rail_height']+0.1,
                           p['rail_length']-root if rear else root],
                }
                oobb.append_full(thing,**p3)
        running = p['bottom_rail_running_height'] if component=='snap_bottom_rail' else p['rail_running_height']
        band,taper,length = p['rail_end_band'],p['rail_taper_run'],p['rail_length']
        p3 = {
            **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
            'points':[[p['rail_height']+0.1,band],[p['rail_height']+0.1,length-band],
                      [running,length-band-taper],[running,band+taper]],
            'height':p['rail_width']+0.2,'depth':p['rail_width']+0.2,
            'rot':[90,0,90],'pos':[-p['rail_width']/2-0.1,0,0],
        }
        oobb.append_full(thing,**p3)
    else:
        raise ValueError(f'Unknown tiled component: {component}')


def get_container_cutout_ai_version_6(pos, thing, **kwargs):
    # Keep complete removals in the cutout stage. Reuse the selected bevelled
    # receiver and twin snap cuts without modifying v5 or numbered samples.
    p = kwargs
    component = p['v6_component']
    if component == 'clearance_rail':
        trial=p['clearance_trial']
        get_container_cutout_ai_version_5_tiled(pos,thing,**dict(p,
            tiled_component='snap_rail',v6_clearance_trial=True,
            snap_shoulder_depth=trial['shoulder_depth']))
        if p['clearance_number']:
            p3={
                **copy.deepcopy(p),'type':'negative','shape':'text','m':'',
                'text':str(p['clearance_number']),'font':'Arial:style=Bold',
                'size':p['number_size'],'height':p['number_depth']+.1,'depth':p['number_depth']+.1,
                'halign':'center','valign':'center','rot':[-90,0,0],
                'pos':[0,p['rail_height']-p['number_depth'],p['number_rail_z']],
            }
            oobb.append_full(thing,**p3)
    elif component == 'screw_adapter_guide':
        s=p['screw_rail'];chamfer=s['guide_tip_chamfer'];floor=s['guide_floor_outside']
        points=[[-.1,-.1],[floor,-.1],[floor,s['guide_depth']-chamfer],
                [floor+chamfer+.1,s['guide_depth']+.1],
                [-.1,s['guide_depth']+.1]]
        p3={
            **copy.deepcopy(p),'type':'negative','shape':'polygon','m':'',
            'points':points,'height':s['guide_width']+.2,'depth':s['guide_width']+.2,
            'rot':[90,0,90],'pos':[-s['guide_width']/2-.1,0,0],
        }
        oobb.append_full(thing,**p3)
        top=s['guide_top']
        oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
            points=[[top,-.1],[p['rail_height']+1,-.1],
                    [p['rail_height']+1,s['guide_depth']+.1],
                    [top-chamfer-.1,s['guide_depth']+.1],[top,s['guide_depth']-chamfer]],
            height=s['guide_width']+.2,depth=s['guide_width']+.2,
            rot=[90,0,90],pos=[-s['guide_width']/2-.1,0,0]))
    elif component == 'screw_adapter':
        s=p['screw_rail']
        p3={
            **copy.deepcopy(p),'type':'negative','shape':'oobb_screw_countersunk','m':'',
            'radius_name':s['screw_size'],'depth':s['screw_length'],'hole':True,
            'nut_include':False,'include_nut':False,'clearance':['top'],'overhang':False,
            'zz':'none','rot':[0,180,0],'pos':[0,s['axis_height'],-s['flange_size'][2]],
        }
        oobb.append_full(thing,**p3)
        # The receiver's shallow outer floor leaves no sensible closed wall
        # above/below a circular bore. Two 1.5 mm cheeks avoid thin slivers;
        # the round flange bore locates the screw vertically.
        oobb.append_full(thing,**dict(p,type='negative',shape='cube',m='',
            size=[s['guide_open_slot_width'],p['rail_height']+2,s['guide_depth']+.1],
            pos=[-s['guide_open_slot_width']/2,-1,0]))
    elif component == 'screw_rail':
        s=p['screw_rail'];length=p['rail_length']
        band,taper=p['rail_end_band'],p['rail_taper_run']
        oobb.append_full(thing,**dict(p,type='negative',shape='polygon',m='',
            points=[[s['end_height']+.1,band],[s['end_height']+.1,length-band],
                    [p['rail_running_height'],length-band-taper],[p['rail_running_height'],band+taper]],
            height=p['rail_width']+.2,depth=p['rail_width']+.2,
            rot=[90,0,90],pos=[-p['rail_width']/2-.1,0,0]))
        for rear in [False,True]:
            bore=s['screw_penetration']+1
            oobb.append_full(thing,**dict(p,type='negative',shape='cylinder',m='',
                r=s['bore_radius'],h=bore+.1,
                pos=[0,s['axis_height'],length-bore if rear else -.1]))
            p3={
                **copy.deepcopy(p),'type':'negative','shape':'oobb_nut','m':'',
                'radius_name':s['screw_size'],'depth':s['nut_depth'],'overhang':True,
                'clearance':s['nut_side_clearance'],'rot':[0,0,0],
                'pos':[0,s['axis_height'],length-s['nut_far'] if rear else s['nut_near']],
            }
            oobb.append_full(thing,**p3)
    elif component == 'joining_plate':
        part=p['joining_plate']
        for x,y in part['holes']:
            p3={
                **copy.deepcopy(p),'type':'negative','shape':'oobb_screw_countersunk','m':'',
                'radius_name':'m3','depth':part['size'][2]+0.2,'hole':True,
                'nut_include':False,'include_nut':False,'clearance':['top'],
                'overhang':False,'zz':'none','rot':[0,0,0],
                'pos':[x,y,part['size'][2]],
            }
            oobb.append_full(thing,**p3)
    elif component == 'floor_support':
        feature=p['floor_support_feature']
        width,root,depth=feature['envelope']
        if feature['kind']=='top_catch':
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
    elif component == 'plate':
        get_container_cutout_ai_version_5_tiled(pos,thing,**dict(p,
            tiled_component='plate',include_forward_lip=False,include_rear_attachments=False,
            natural_height=p['profile_reference_height'],
            tile_bounds=[-p['width_total']/2,-p['height_total']/2,p['width_total']/2,p['height_total']/2]))
        for hole in p['corner_holes']:
            p3 = {
                **copy.deepcopy(p),'type':'negative','shape':'oobb_hole','m':'',
                'radius_name':p['corner_hole_size'],'depth':p['plate_thickness']+0.2,
                'pos':[hole['x'],hole['y'],-0.1],
            }
            oobb.append_full(thing,**p3)
    else:
        rail_kwargs=dict(p,tiled_component=component)
        if component.startswith('snap_') and 'selected_rail_fit' in p:
            rail_kwargs.update(v6_selected_latch=True,
                               snap_shoulder_depth=p['selected_rail_fit']['shoulder_depth'])
        get_container_cutout_ai_version_5_tiled(pos,thing,**rail_kwargs)
