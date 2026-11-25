import copy
import oobb

# Current side-printed V8 beams: allow the bin to project through each face.
# Override with beam_depth_reduction_per_end in the SCAD-stage inputs (0 restores
# full depth). This reduces the span, never the retaining pins or screw guides.
V8_BEAM_DEPTH_REDUCTION_PER_END = 7.5


def component_parameters(**kwargs):
    """Resolve and check the common V8 beam, receiver and latch dimensions."""
    import math
    p = copy.deepcopy(kwargs)
    for key in ['panel_thickness','receiver_hole_width','receiver_hole_height',
                'neck_width','tongue_height','grip_width','grip_length',
                'hook_projection','hook_land','lead_angle']:
        if not isinstance(p[key], (int,float)) or not math.isfinite(p[key]) or p[key] <= 0:
            raise ValueError('Invalid V8 dimension: '+key)
    if not 20 <= p['lead_angle'] <= 45:
        raise ValueError('V8 lead angle must be 20–45 degrees')
    if p['receiver_hole_height'] <= p['tongue_height'] or p['receiver_hole_width'] <= p['neck_width']:
        raise ValueError('V8 rigid tongue needs positive clearance')
    p['outer'] = p['neck_width']/2
    p['hook_ramp'] = p['hook_projection']/math.tan(math.radians(p['lead_angle']))
    p['side_clearance'] = (p['receiver_hole_width']-p['neck_width'])/2
    p['deflection'] = p['hook_projection']-p['side_clearance']+.1
    p['retention_overlap'] = p['hook_projection']-p['side_clearance']
    if p.get('permanent_snap_test'):
        # Here the middle arms TOUCH at the hook as it passes the receiver.
        # Never use the older extra 0.1 mm flex: it would interpenetrate them.
        p['deflection']=p['hook_projection']-p['side_clearance']
        p['required_arm_contact']=True
    if p.get('drop_loop'):
        d=p['drop_loop']
        d['eye_far']=d['eye_near']+d['eye_depth']
        d['tip_y']=d['eye_far']+d['nose_thickness']
        d['axial_play']=d['eye_far']-d['key_depth']-p['panel_thickness']
        d['wall_thickness']=(p['neck_width']-d['eye_width'])/2
        if (min(d['wall_thickness'],d['nose_thickness'])<1.4 or
            d['eye_width']<=d['key_width'] or d['eye_depth']<=d['key_depth'] or
            d['eye_near']<p['panel_thickness'] or d['key_near']<=d['eye_near'] or
            d['key_near']+d['key_depth']>=d['eye_far'] or
            d['key_length']<=p['receiver_hole_height'] or d['key_head_width']<=d['eye_width']):
            raise ValueError('Loop/key requires retained walls, insertion clearance and positive stops')
    for t in p['trials']:
        if t.get('technique')=='drop_loop':
            t['tip_y']=p['drop_loop']['tip_y']
            t['axial_clearance']=p['drop_loop']['axial_play']
            continue
        t['shoulder_y'] = p['panel_thickness']+t['axial_clearance']
        t['tip_y'] = t['shoulder_y']+p['hook_land']+p['hook_ramp']+p['tip_land']
        if p.get('finger_count',5)==4:
            t['root_radius']=p['outer']-t.get('root_thickness',t['arm_thickness'])
        else:
            t['root_radius'] = (p['outer']-t['arm_thickness']-p['pilot_half_width'])/2
        t['effective_root_y'] = p['spring_root_y']+2*max(.5,t['root_radius'])
        t['spring_length'] = t['shoulder_y']-t['effective_root_y']
        strength_thickness=t.get('root_thickness',t['arm_thickness']) if p.get('permanent_snap_test') else t['arm_thickness']
        t['strain_proxy'] = 1.5*strength_thickness*p['deflection']/t['spring_length']**2
        t['stiffness_proxy'] = t['arm_thickness']**3/t['spring_length']**3
        if t['root_radius'] < .59 or t['axial_clearance'] < .05:
            raise ValueError('V8 needs open spring slots and positive end clearance')
        if p.get('permanent_snap_test'):
            t['closed_arm_gap']=2*(p['outer']-t['tip_thickness']-p['deflection'])
            t['closed_hook_width']=2*(t['tip_thickness']+p['hook_projection'])
            if abs(t['closed_arm_gap'])>1e-6 or abs(t['closed_hook_width']-p['receiver_hole_width'])>1e-6:
                raise ValueError('Permanent hooks must require full arm contact and still pass the hole')
        elif p['outer']-t['arm_thickness']-p['deflection'] <= p['pilot_half_width']+.1:
            raise ValueError('V8 compressed arm would hit the rigid pilot')
    if p.get('finger_count',5)==4:
        p['outer_strip_width']=p['grip_width']/2-p['outer']-p['outer_release_width']
        if p['outer_strip_width']<1.5:
            raise ValueError('Four-finger outer seating strips must stay substantial')
        p['keeper']['stem_height']=p['tongue_height']
        p['keeper']['tip_y']=p['keeper']['head_start_y']+p['keeper']['head_length']
    if p.get('front_plug_test'):
        s=p['front_plug'];trial=p['trials'][0]
        s['outer_y']=s['cap_inner_y']+s['cover_thickness']
        s['cup_depth']=s['outer_y']-s['panel_stop_y']
        s['cover_radius']=.75
        s['stem_depth']=s['outer_y']-s['nose_y']
        s['free_slot_width']=2*(p['outer']-trial['tip_thickness'])
        s['seated_spread']=(s['stem_width']-s['free_slot_width'])/2
        s['insertion_spread']=(s.get('detent_width',s['stem_width'])-s['free_slot_width'])/2
        s['expanded_neck_width']=p['neck_width']+2*s['seated_spread']
        s['insertion_neck_width']=p['neck_width']+2*s['insertion_spread']
        if not (0<s['seated_spread']<=s['insertion_spread'] and
                s['insertion_neck_width']<=p['receiver_hole_width']+1e-6 and
                s['panel_stop_y']>=p['panel_thickness'] and s['cap_inner_y']>trial['tip_y'] and
                s['cavity_width']>2*(p['outer']+p['hook_projection']+s['insertion_spread']) and
                s['cavity_height']>p['tongue_height'] and
                p['upper_support_height']>p['receiver_hole_height']):
            raise ValueError('Front cap needs room to spread, clear the hooks and support above the hole')
        if 'cover_offset_y' in s:
            s['minimum_rim_wall']=min((s['cover_width']-s['cavity_width'])/2,
                s['cover_height']/2-abs(s['cover_offset_y'])-s['cavity_height']/2)
            if s['minimum_rim_wall']<.5:
                raise ValueError('Offset cover needs at least 0.5 mm of rim around the unchanged hook cavity')
    s = p['screw']
    s['nut_depth'] = oobb.gv('nut_depth_m3','3dpr')
    s['nut_radius'] = oobb.gv('nut_radius_m3','3dpr')
    s['bore_radius'] = oobb.gv('hole_radius_m3','3dpr')
    s['projection_after_nut'] = s['length']-s['flange_size'][2]-p['panel_thickness']-s['nut_near']-s['nut_depth']
    if s['projection_after_nut'] < 1 or s['guide_depth'] >= p['panel_thickness']:
        raise ValueError('V8 screw must pass the nut and the adapter must seat on its flange')
    if 'beam_receiver_depth' in s:
        if (not all(isinstance(s[k],(int,float)) and math.isfinite(s[k]) and s[k]>0
                    for k in ['beam_receiver_depth','guide_depth','mating_clearance','beam_guide_width','beam_guide_height']) or
            abs(s['beam_receiver_depth']-p['panel_thickness']/2)>1e-6 or
            abs(s['guide_depth']-p['panel_thickness']/2)>1e-6 or
            not 0<s['mating_clearance']<.5 or
            s['beam_guide_width']>=p['receiver_hole_width'] or
            s['beam_guide_height']>=p['receiver_hole_height']):
            raise ValueError('Screw receiver needs equal half-depth ends, positive clearance and guides inside the hole')
        s['beam_engagement']=s['beam_receiver_depth']-s['mating_clearance']/2
        s['adapter_engagement']=s['guide_depth']-s['mating_clearance']/2
    return p


def draw_component(thing, **kwargs):
    """Solid envelopes here; every removal lives in the V8 container cutout."""
    import working_scad_container_cutout as cuts
    p = component_parameters(**kwargs)
    view = p.get('connector_view','clips')
    origin = p.get('pos',[0,0,0])

    def place(sub, shift=(0,0,0), rot=(0,0,0)):
        thing['components'].append(dict(type='rotation',typetype='positive',rot=list(rot),
            pos=[origin[i]+shift[i] for i in range(3)],objects=sub['components']))

    def clip(t, shift=(0,0,0)):
        sub = oobb.get_default_thing(type='v8_short_clip')
        oobb.append_full(sub, **dict(p,type='positive',shape='cube',m='',
            size=[p['grip_width'],p['grip_length']+t['tip_y'],p['tongue_height']],
            pos=[-p['grip_width']/2,-p['grip_length'],0]))
        cuts.cut([0,0,0],sub,**dict(p,
            v8_component=('drop_loop' if t.get('technique')=='drop_loop' else 'clip'),trial=t))
        if p.get('front_plug_test'):
            body=oobb.get_default_thing(type='v8_upper_supported_clip')
            body['components'].append(dict(type='rotation',typetype='positive',rot=[0,0,0],pos=[0,0,0],objects=sub['components']))
            for side in [-1,1]:
                x=p['outer']+p['outer_release_width']+.05 if side==1 else -p['grip_width']/2
                oobb.append_full(body,**dict(p,type='positive',shape='cube',m='',
                    size=[p['outer_strip_width']-.05,p['grip_length'],p['upper_support_height']-p['tongue_height']+.05],
                    pos=[x,-p['grip_length'],p['tongue_height']-.05]))
            grip=oobb.get_default_thing(type='v8_tall_rear_grip')
            oobb.append_full(grip,**dict(p,type='positive',shape='cube',m='',
                size=[p['grip_width'],p['grip_length']+p['spring_root_y']-.5,p['upper_support_height']-p['tongue_height']+.05],
                pos=[-p['grip_width']/2,-p['grip_length'],p['tongue_height']-.05]))
            cuts.cut([0,0,0],grip,**dict(p,v8_component='front_upper_support',trial=t))
            body['components'].append(dict(type='rotation',typetype='positive',rot=[0,0,0],pos=[0,0,0],objects=grip['components']))
            sub=body
        place(sub,shift)

    def front_cap(shift=(0,0,0)):
        s=p['front_plug'];body=oobb.get_default_thing(type='v8_front_cover_cup')
        oobb.append_full(body,**dict(p,type='positive',shape='rounded_rectangle',m='',
            size=[s['cover_width'],s['cover_height'],s['cup_depth']],radius=s['cover_radius'],
            pos=[0,s.get('cover_offset_y',0),0]))
        cuts.cut([0,0,0],body,**dict(p,v8_component='front_cap_cup'))
        stem=oobb.get_default_thing(type='v8_spreader_stem')
        oobb.append_full(stem,**dict(p,type='positive',shape='cube',m='',
            size=[s.get('detent_width',s['stem_width'])+.2,s['stem_height'],s['stem_depth']-s['cover_thickness']+.05],
            pos=[-(s.get('detent_width',s['stem_width'])+.2)/2,-s['stem_height']/2,s['cover_thickness']-.05]))
        cuts.cut([0,0,0],stem,**dict(p,v8_component='front_cap_stem'))
        combined=oobb.get_default_thing(type='v8_front_cover_and_stem')
        for part in [body,stem]:
            combined['components'].append(dict(type='rotation',typetype='positive',rot=[0,0,0],pos=[0,0,0],objects=part['components']))
        place(combined,shift)

    if view in ['front_plug','front_plug_square']:
        if view=='front_plug_square':p['front_plug']['corner_reliefs']=[]
        front_cap();count=1
    elif view.startswith('sample_'):
        clip(next(t for t in p['trials'] if t['sample_number']==int(view.split('_')[-1])))
        count = 1
    elif view.startswith('receiver'):
        thick = p.get('receiver_print_thickness',p['panel_thickness'])
        sub = oobb.get_default_thing(type='v8_receiver_card')
        oobb.append_full(sub,**dict(p,type='positive',shape='rounded_rectangle',m='',
            size=[*p['receiver_size'],thick],radius=2,pos=[0,0,0]))
        cuts.cut([0,0,0],sub,**dict(p,
            v8_component='receiver',receiver_print_thickness=thick))
        place(sub)
        count = 1
    elif view in ['screw_beam','screw_adapter','screw_test']:
        s=p['screw']
        if view != 'screw_adapter':
            sub=oobb.get_default_thing(type='v8_screw_beam_end')
            oobb.append_full(sub,**dict(p,type='positive',shape='cube',m='',
                size=[p['grip_width'],p['grip_length'],s['end_height']],
                pos=[-p['grip_width']/2,-p['grip_length'],s['axis_height']-s['end_height']/2]))
            cuts.cut([0,0,0],sub,**dict(p,v8_component='screw_beam'))
            # Beam long side on the bed; axial bore and side-loading nut match V6.
            place(sub,[0,0,s['end_height']/2-s['axis_height']])
        if view != 'screw_beam':
            sub=oobb.get_default_thing(type='v8_external_adapter')
            depth=s.get('adapter_engagement',s['guide_depth'])
            oobb.append_full(sub,**dict(p,type='positive',shape='rounded_rectangle',m='',
                size=s['flange_size'],radius=.75,pos=[s.get('flange_offset_x',0),0,0]))
            oobb.append_full(sub,**dict(p,type='positive',shape='cube',m='',
                size=[s['guide_width'],s['guide_height'],depth+.05],
                pos=[-s['guide_width']/2,-s['guide_height']/2,s['flange_size'][2]-.05]))
            cuts.cut([0,0,0],sub,**dict(p,v8_component='screw_adapter'))
            place(sub,[20,0,0] if view=='screw_test' else [0,0,0])
        count = 2 if view=='screw_test' else 1
    else:
        raise ValueError('Unknown V8 view '+view)
    thing['ai_design']=dict(style='ai_version_8',part_role='connector_test',view=view,
        expected_bodies=count,experimental=True,material='PETG / 6 mm MDF',
        physical_fit='Awaiting numbered sample feedback')

def plan_face(p):
    """Opening pitch and receiver coordinates in front-face CAD axes."""
    q=dict(p['frame_definition'])
    cols,rows=p['column'],p['row']
    pot=p['container_dimensions_mm']
    width=pot['across']+q['container_clearance']
    height=pot['height']+q['container_clearance']+q['opening_height_extra']
    pitch_x=width+q['thickness_wall']
    pitch_y=height+q['thickness_wall']+q['row_spacing_extra']
    grid_height=height+(rows-1)*pitch_y
    frame_width=width+(cols-1)*pitch_x+2*q['drawer_border_edge']
    frame_height=grid_height+2*q['face_edge_y']
    inset=q['corner_hole_inset']
    q.update(column=cols,row=rows,natural_width=frame_width, width_total=frame_width,
             height_total=frame_height,opening_width=width,opening_height=height,
             opening_origin_y=-grid_height/2,pitch_x=pitch_x,pitch_y=pitch_y,
             plate_thickness=p['panel_thickness'],drawer_count=2*cols*rows,
             bank_depth=pot['depth']+q['depth_clearance'],
             corner_holes=[dict(x=sx*(frame_width/2-inset),y=sy*(frame_height/2-inset))
                           for sx in (-1,1) for sy in (-1,1)])
    xs=[(col-cols/2)*pitch_x for col in range(cols+1)]
    xs[0] += q['thickness_wall']/2 - q['outer_mount_offset']
    xs[-1] -= q['thickness_wall']/2 - q['outer_mount_offset']
    # Shared receivers get the separate 1.5 mm offset in the mount planner.
    q['rail_positions']=[dict(x=x,y=-grid_height/2+row*pitch_y+q['depth_lip'])
                         for x in xs for row in range(rows)]
    q['floor_support_features']=floor_supports(q)
    return q


def frame_parameters(**kwargs):
    p=component_parameters(**kwargs)
    q=plan_face(p)
    import math
    reduction=p.get('beam_depth_reduction_per_end',
        V8_BEAM_DEPTH_REDUCTION_PER_END if p.get('beam_revision')=='side_printed_runner' else 0)
    if (isinstance(reduction,bool) or not isinstance(reduction,(int,float)) or
        not math.isfinite(reduction) or reduction<0):
        raise ValueError('beam_depth_reduction_per_end must be finite and nonnegative')
    p['beam_depth_reduction_per_end']=reduction
    q['bank_depth']-=reduction
    q['assembled_depth']=2*q['bank_depth']+q['middle_stop_thickness']
    q['rail_length']=q['assembled_depth']-2*q['plate_thickness']
    q['middle_stop_z']=q['rail_length']/2
    # Preserve a solid centre and both complete end mechanisms.
    minimum_span=2*max(p['grip_length'],p.get('side_runner',{}).get('end_length',0),
                       p['beam_end_length']+p['beam_transition_length'])+q['middle_stop_thickness']
    if q['rail_length']<=minimum_span:
        raise ValueError('Beam depth reduction leaves insufficient span for ends and centre stop')
    p['frame']=q
    p['rail_length']=q['rail_length']
    p['frame_mounts']=[dict(x=r['x'],hole_y=r['y']+8,kind='snap_beam') for r in q['rail_positions']]
    if p.get('frame_mount_layout') == 'four_corner_replacements':
        xs=[min(r['x'] for r in p['frame_mounts']),max(r['x'] for r in p['frame_mounts'])]
        ys=[min(r['hole_y'] for r in p['frame_mounts']),max(r['hole_y'] for r in p['frame_mounts'])]
        for r in p['frame_mounts']:
            if r['x'] in xs and r['hole_y'] in ys:r['kind']='screw_beam'
    else:
        for x in sorted({r['x'] for r in q['rail_positions']}):
            p['frame_mounts'].append(dict(x=x,hole_y=q['opening_origin_y']-p['screw_brace_above_opening'],kind='screw_beam'))
    outer_x = {min(r['x'] for r in p['frame_mounts']), max(r['x'] for r in p['frame_mounts'])}
    outer_y = {min(r['hole_y'] for r in p['frame_mounts']), max(r['hole_y'] for r in p['frame_mounts'])}
    for mount in p['frame_mounts']:
        mount['corner_beam'] = mount['x'] in outer_x and mount['hole_y'] in outer_y
        if mount['corner_beam']:
            mount['kind'] = 'screw_beam'
    if p.get('runner_alignment'):
        shift=p['runner_alignment']['shared_receiver_offset_x']
        if not isinstance(shift,(int,float)) or abs(shift-p['side_runner']['offset_x'])>1e-6:
            raise ValueError('Shared receiver offset must centre the running strip on its divider')
        xs=[r['x'] for r in p['frame_mounts']];left=min(xs);right=max(xs)
        for mount in p['frame_mounts']:
            mount['divider_x']=mount['x']
            mount['shared_runner']=left+1e-6<mount['x']<right-1e-6
            if mount['shared_runner']:mount['x']+=shift
    if (sum(r['kind']=='snap_beam' for r in p['frame_mounts'])!=p['snap_beam_count'] or
        sum(r['kind']=='screw_beam' for r in p['frame_mounts'])!=p['screw_beam_count']):
        raise ValueError('Beam quantities must match the selected frame mounts')
    if p['screw']['guide_width']>=p['receiver_hole_width'] or p['screw']['guide_height']>=p['receiver_hole_height']:
        raise ValueError('Screw guides must pass through the common receiver')
    p['screw']['running_height']=p['beam_running_height']+p['screw']['axis_height']-p['tongue_height']/2
    if not p.get('screw_beam_drop_in'):
        raise ValueError('Screw beams must replace snap beams at the same receiver')
    w=p['beam_lightening'];half=p['rail_length']/2
    slot_length=half-w['centre_land']/2-w['end_land']
    if (not all(isinstance(v,(int,float)) and v>0 for v in w.values()) or
        p['grip_width']-w['width']<6 or w['width']<2*w['radius'] or
        slot_length<2*w['radius'] or w['end_land']<p['beam_end_length']+p['beam_transition_length'] or
        w['centre_land']<q['middle_stop_thickness']+8):
        raise ValueError('Beam windows need solid ends, 3 mm side rails and a supported centre stop')
    p['beam_windows']=[dict(width=w['width'],length=slot_length,radius=w['radius'],
        y=-d) for d in [(w['end_land']+half-w['centre_land']/2)/2,
                        (half+w['centre_land']/2+p['rail_length']-w['end_land'])/2]]
    if p.get('beam_revision')=='side_printed_runner':
        r=p['side_runner']
        import math
        if (not all(isinstance(v,(int,float)) and math.isfinite(v) for v in r.values()) or
            r['thickness']<=0 or r['thickness']>=p['beam_running_height']-p['tongue_height']/2 or
            abs(r['offset_x']-r['width']/2-r['bed_x'])>1e-6 or
            abs(r['bed_x']+p['tongue_height']/2)>1e-6 or r['clip_rotation_y']!=90 or
            r['width']<=0 or r['bed_x']+r['width']>p['grip_width']/2 or
            r['runner_end_clearance']<=0 or r['runner_end_clearance']>=1 or
            r['stop_min_x']<r['bed_x'] or r['stop_max_x']<=r['stop_min_x'] or
            r['stop_max_x']>q['middle_stop_width']/2 or
            r.get('stop_height',1)<=0 or
            r['end_length']<p['screw']['nut_near']+p['screw']['nut_depth']+1.5 or
            p['grip_length']<abs(p['spring_root_y'])+4):
            raise ValueError('Side runner needs a common bed plane, joined ends and retained nut walls')
        p['beam_windows']=[]
    if p.get('corner_fixing'):
        configure_v8_joiners(p)
    p['bom']=dict(front=1,back=1,snap_beam=p['snap_beam_count'],screw_beam=p['screw_beam_count'],
                  front_plug=2*p['snap_beam_count'],screw_adapter=2*p['screw_beam_count'],
                  M3_countersunk_screw_20_mm=2*p['screw_beam_count'],M3_nut=2*p['screw_beam_count'])
    p['cap_quantities'] = {'front_plug': 0, 'front_plug_square': p['bom']['front_plug']}
    for mount in p['frame_mounts']:
        if mount['kind'] == 'snap_beam':
            mount['cap_component'] = 'front_plug_square'
    # Single-bed batches; do not stretch the complete quantity across one bed.
    usable_width=q['bed_width']-q['bed_exclusion'][0]-2*q['bed_margin']
    p['print_batches']={}
    batch_types=[('snap_beams','snap_beam',24),('screw_beams','screw_beam',24),
                 ('front_plugs','front_plug',15),('screw_adapters','screw_adapter',15)]
    if p.get('cap_quantities'):
        batch_types=[('snap_beams','snap_beam',24),('screw_beams','screw_beam',24),
                     ('front_plugs_corner_clearance','front_plug',15),
                     ('front_plugs_square','front_plug_square',15),('screw_adapters','screw_adapter',15)]
    for plural,single,pitch in batch_types:
        capacity=int(usable_width//pitch)
        quantity=p.get('cap_quantities',{}).get(single,p['bom'].get(single,0))
        remaining=quantity;index=1
        while remaining:
            count=min(capacity,remaining)
            name=plural if quantity<=capacity else f'{plural}_{index:02d}'
            p['print_batches'][name]=dict(component=single,count=count,pitch=pitch)
            remaining-=count;index+=1
    if p.get('laser_face_test'):
        t=p['laser_face_test'];side=t['reinforcement_side'];half=side/2
        if (min(t.values())<=0 or abs(t['face_thickness']+t['reinforcement_thickness']-p['panel_thickness'])>1e-6 or
            side>q['thickness_wall']+2*q['inset_lip'] or
            side-max(p['receiver_hole_width'],p['receiver_hole_height'])<4):
            raise ValueError('Laser reinforcement needs a 6 mm stack, retained hole walls and an upright-sized square')
        radius=oobb.gv('hole_radius_'+q['corner_hole_size'],'3dpr')+t['corner_relief_clearance']
        p['reinforcement_pads']=[];p['reinforcement_types']={'clip_reinforcement':[]}
        p['reinforcement_hole_offsets']={'clip_reinforcement':0.0}
        for mount in p['frame_mounts']:
            pad_x=mount.get('divider_x',mount['x'])
            hole_offset=mount['x']-pad_x
            if side/2-abs(hole_offset)-p['receiver_hole_width']/2<1.5:
                raise ValueError('Offset reinforcement hole needs at least 1.5 mm of edge material')
            reliefs=[]
            for corner in q['corner_holes']:
                dx=corner['x']-pad_x;dy=corner['y']-mount['hole_y']
                if max(abs(dx)-half,0)**2+max(abs(dy)-half,0)**2<radius**2:
                    reliefs.append(dict(x=round(dx,6),y=round(dy,6),radius=radius))
            name=('clip_reinforcement_corner_left' if reliefs[0]['x']<0 else
                  'clip_reinforcement_corner_right') if reliefs else (
                  'clip_reinforcement_offset' if abs(hole_offset)>1e-6 else 'clip_reinforcement')
            p['reinforcement_types'][name]=reliefs
            p['reinforcement_hole_offsets'][name]=hole_offset
            p['reinforcement_pads'].append(dict(**mount,view=name,reliefs=reliefs,
                                                pad_x=pad_x,hole_offset_x=hole_offset))
        # Nest the complete set of receiver pads in unused drawer openings.
        slots=[];pitch=side+t['nesting_gap']
        across=4 if p['row']==1 and p['column']==1 else 3
        if across*side+(across-1)*t['nesting_gap']>q['opening_width']-2*q['inset_lip']:
            raise ValueError('Reinforcement squares do not fit in the bin-opening waste')
        for row in range(p['row']):
            for col in range(p['column']):
                cx=-q['width_total']/2+q['drawer_border_edge']+q['opening_width']/2+col*q['pitch_x']
                cy=q['opening_origin_y']+row*q['pitch_y']+q['depth_lip']+8
                slots.extend([(cx+(j-(across-1)/2)*pitch,cy) for j in range(across)])
        if len(slots)<len(p['reinforcement_pads']):raise ValueError('Insufficient waste area for all reinforcement squares')
        p['reinforcement_layout']=[dict(pad,layout_x=xy[0],layout_y=xy[1])
                                   for pad,xy in zip(p['reinforcement_pads'],slots)]
    return p


def v8_beam_to_frame(p, mount, kind):
    """Place a manufacturing beam at an existing face receiver."""
    axis=p['tongue_height']/2 if kind=='snap_beam' else p['screw']['axis_height']
    if p.get('beam_revision')=='side_printed_runner':
        return [[0,0,-1,mount['x']-p['side_runner']['bed_x']],
                [1,0,0,mount['hole_y']+axis],
                [0,-1,0,p['panel_thickness']],[0,0,0,1]]
    return [[-1,0,0,mount['x']],[0,0,-1,mount['hole_y']+axis],
            [0,-1,0,p['panel_thickness']],[0,0,0,1]]


def v8_external_part_rotation(p,kind,rear=False):
    if kind=='snap_beam':
        turn=90 if p.get('beam_revision')=='side_printed_runner' else 0
        return [0,180,turn] if rear else [0,0,turn]
    if rear:
        return [180,0,0] if p.get('finishing_revision') else [0,180,0]
    return [0,0,0]


def draw_frame(thing,**kwargs):
    """Selected V8 unit; compose unchanged short clips onto full-length beams."""
    import working_scad_container_cutout as cuts
    p=frame_parameters(**kwargs);q=p['frame'];length=p['rail_length']
    view=p.get('connector_view','print_layout');origin=p.pop('pos',[0,0,0])
    def place(part,shift=(0,0,0),rot=(0,0,0),target=thing):
        target['components'].append(dict(type='rotation',typetype='positive',rot=list(rot),
            pos=[origin[i]+shift[i] if target is thing else shift[i] for i in range(3)],objects=part['components']))
    def single(name,seated=False):
        sub=oobb.get_default_thing(type='v8_selected_component')
        draw_component(sub,**dict(p,connector_design='v8_through_panel',part_role='connector_test',
            connector_view=name,suppress_markings=True,seated_clip=seated,
            seated_visual_clearance=.001 if seated else 0))
        return sub
    def face(laser=False,web=None,back=False):
        web=p['panel_thickness'] if web is None else web
        sub=oobb.get_default_thing(type='v8_selected_face')
        oobb.append_full(sub,**dict(p,type='positive',shape='rounded_rectangle',m='',
            size=[q['width_total'],q['height_total'],web],radius=q['outer_radius'],pos=[0,0,0]))
        mounts=p['frame_mounts']
        if back and any(m.get('shared_runner') for m in mounts):
            mounts=[dict(m,x=-m['x']) for m in mounts]
        cuts.cut([0,0,0],sub,**dict(p,v8_component='frame_face',frame_mounts=mounts))
        body=oobb.get_default_thing(type='v8_selected_face_with_stops');place(sub,target=body)
        for f in q['floor_support_features']:
            rib=oobb.get_default_thing(type='v8_selected_stop');size=copy.deepcopy(f['envelope'])
            if laser:size[2]=web
            oobb.append_full(rib,**dict(p,type='positive',shape='cube',m='',size=size,pos=f['pos']))
            if not laser:
                cuts.floor_stop(rib,**dict(q,floor_support_feature=f,
                    face_stop_profile=p.get('face_stop_profile')))
            place(rib,target=body)
        return body
    def reinforcement(reliefs,hole_offset=0):
        sub=oobb.get_default_thing(type='v8_laser_clip_reinforcement');t=p['laser_face_test']
        side=t['reinforcement_side']
        oobb.append_full(sub,**dict(p,type='positive',shape='cube',m='',
            size=[side,side,t['reinforcement_thickness']],pos=[-side/2,-side/2,0]))
        cuts.cut([0,0,0],sub,**dict(p,
            v8_component='clip_reinforcement',reinforcement_reliefs=reliefs,
            reinforcement_hole_offset_x=hole_offset))
        return sub
    def snap(seated=False):
        return side_beam(True,seated)
    def screw():
        return side_beam(False)
    def side_beam(is_snap,seated=False):
        # Native service coordinates: X across drawers, -Y along the beam,
        # Z up. The print transform below puts X=bed_x on the plate.
        r=p['side_runner'];s=p['screw']
        axis=p['tongue_height']/2 if is_snap else s['axis_height']
        roof=axis+p['beam_running_height']-p['tongue_height']/2
        body=oobb.get_default_thing(type='v8_thin_runner')
        oobb.append_full(body,type='positive',shape='cube',m='',
            size=[r['width'],length-2*r['runner_end_clearance'],r['thickness']],
            pos=[r['offset_x']-r['width']/2,-length+r['runner_end_clearance'],roof-r['thickness']])
        if is_snap:
            end=single('sample_71',seated)
            turned=oobb.get_default_thing(type='v8_turned_snap')
            place(end,[-axis,0,axis],[0,r['clip_rotation_y'],0],target=turned)
            place(turned,target=body)
            place(end,[-axis,-length,axis],[180,-90,0],target=body)
        else:
            for rear in [False,True]:
                end=oobb.get_default_thing(type='v8_explicit_nut_boss')
                oobb.append_full(end,type='positive',shape='cube',m='',
                    size=[r['width'],r['end_length'],s['end_height']],
                    pos=[r['bed_x'],-r['end_length'],axis-s['end_height']/2])
                if 'beam_engagement' in s:
                    oobb.append_full(end,type='positive',shape='cube',m='',
                        size=[s['beam_guide_width'],s['beam_engagement']+.05,s['beam_guide_height']],
                        pos=[-s['beam_guide_width']/2,-.05,axis-s['beam_guide_height']/2])
                cuts.cut([0,0,0],end,**dict(p,v8_component='screw_beam'))
                if rear:
                    place(end,[0,-length,2*axis],[180,0,0],target=body)
                else:place(end,target=body)
        if 'stop_height' in r:
            stop_bottom=roof-.05;stop_height=r['stop_height']+.05
        else:
            stop_bottom=axis-r['stop_below_axis'];stop_height=roof-stop_bottom
        oobb.append_full(body,type='positive',shape='cube',m='',
            size=[r['stop_max_x']-r['stop_min_x'],q['middle_stop_thickness'],stop_height],
            pos=[r['stop_min_x'],-length/2-q['middle_stop_thickness']/2,stop_bottom])
        if p.get('corner_fixing'):
            cuts.cut([0,0,0],body,
                **dict(p,v8_component='joiner_corner_paths',joiner_beam_axis=axis))
        printed=oobb.get_default_thing(type='v8_side_printed_beam')
        place(body,[0,0,-r['bed_x']],[0,-90,0],target=printed)
        return printed
    count=0
    if view in ['joiners','joiners_clasp_clearance','joiner_backers'] and p.get('joiners'):
        for part in p['joiners']:
            sub=oobb.get_default_thing(type='v8_optional_joiner')
            if view=='joiner_backers':draw_backer(sub,p,part)
            else:draw_joiner(sub,p,part,clasp_clearance=view=='joiners_clasp_clearance')
            place(sub,part['print_center'])
        count=len(p['joiners'])
    elif view=='joiner_fit_samples':
        # Two independent top corners across a real vertical seam, both types of
        # interchangeable ends, their matching locks and a complete drawer catch.
        for hand in [-1,1]:
            cut=face()
            x=hand*(q['width_total']/2-12)
            y=-q['height_total']/2+12
            crop=oobb.get_default_thing(type='corner_fit_sample')
            place(cut,[-x,-y,0],target=crop)
            cuts.cut([0,0,0],crop,**dict(p,
                v8_component='sample_window',sample_bounds=[-12,-12,12,12]))
            place(crop,[-hand*15,0,0])
        for is_snap in [True,False]:
            beam=snap() if is_snap else screw()
            cuts.cut([0,0,0],beam,**dict(p,
                v8_component='sample_window',sample_bounds=[-30,-26,30,12]))
            place(beam,[-18 if is_snap else 12,45,0])
        place(single('front_plug_square'),[-38,0,0])
        place(single('screw_adapter'),[-38,15,0])
        feature=next(f for f in q['floor_support_features'] if f['kind']=='floor')
        crop=oobb.get_default_thing(type='face_stop_sample')
        x,y,_=feature['pos']
        place(face(),[-x,-y,0],target=crop)
        cuts.cut([0,0,0],crop,**dict(p,
            v8_component='sample_window',sample_bounds=[-2,-2,17,12]))
        place(crop,[32,0,0]);count=7
    elif view in ['front','back','front_laser']:
        place(face(view=='front_laser',back=view=='back'));count=1
    elif view in p.get('reinforcement_types',{}):
        place(reinforcement(p['reinforcement_types'][view],p['reinforcement_hole_offsets'][view]));count=1
    elif view in ['front_3mm_test','front_3mm_test_layout','clip_reinforcements']:
        if view!='clip_reinforcements':
            place(face(laser=True,web=p['laser_face_test']['face_thickness']));count=1
        for pad in p['reinforcement_layout']:
            assembled=view=='front_3mm_test'
            shift=[pad['pad_x'],pad['hole_y'],p['laser_face_test']['face_thickness']] if assembled else [pad['layout_x'],pad['layout_y'],0]
            place(reinforcement(pad['reliefs'],pad['hole_offset_x']),shift);count+=1
        if view=='front_3mm_test':count=1  # Bonded reference is one unioned solid.
    elif view in ['snap_beam','screw_beam','front_plug','front_plug_square','screw_adapter','sample_71','receiver_6_0']:
        part=snap() if view=='snap_beam' else screw() if view=='screw_beam' else single(view)
        place(part);count=1
    elif view in p['print_batches']:
        batch=p['print_batches'][view];name=batch['component'];n=batch['count']
        part=snap() if name=='snap_beam' else screw() if name=='screw_beam' else single(name)
        pitch=batch['pitch']
        for i in range(n):place(part,[(i-(n-1)/2)*pitch,0,0])
        count=n
    elif view=='assembled':
        place(face());place(face(back=True),[0,0,q['assembled_depth']],[0,180,0]);count=2
        for r in p['frame_mounts']:
            is_snap=r['kind']=='snap_beam';part=snap(seated=True) if is_snap else screw()
            offset=p['tongue_height']/2 if is_snap else p['screw']['axis_height']
            if p.get('beam_revision')=='side_printed_runner':
                native=oobb.get_default_thing(type='v8_beam_service_orientation')
                place(part,[p['side_runner']['bed_x'],0,0],[0,90,0],target=native)
                part=native
            place(part,[r['x'],r['hole_y']+offset,p['panel_thickness']],[90,180,0]);count+=1
            if r["corner_beam"] and p.get("omit_corner_adapters"):
                continue
            for rear in [False,True]:
                sub=single(r.get('cap_component','front_plug') if is_snap else 'screw_adapter')
                if is_snap:
                    # Native cover prints face down; stem follows +Z into panel.
                    shift=[r['x'],r['hole_y'],q['assembled_depth']+p['front_plug']['outer_y']-p['panel_thickness']] if rear else [r['x'],r['hole_y'],p['panel_thickness']-p['front_plug']['outer_y']]
                    place(sub,shift,v8_external_part_rotation(p,r['kind'],rear))
                else:
                    shift=[r['x'],r['hole_y'],q['assembled_depth']+p['screw']['flange_size'][2]] if rear else [r['x'],r['hole_y'],-p['screw']['flange_size'][2]]
                    place(sub,shift,v8_external_part_rotation(p,r['kind'],rear))
                count+=1
    elif view=='print_layout':
        place(face(),[-(q['width_total']+10)/2,0,0])
        place(face(back=True),[(q['width_total']+10)/2,0,0]);count=2
        y=q['height_total']/2+length+30
        for batch_name,batch in p['print_batches'].items():
            sub=oobb.get_default_thing(type='batch_overview')
            draw_frame(sub,**dict(kwargs,connector_view=batch_name))
            place(sub,[0,y,0]);count+=batch['count'];y+=length+30
    else:raise ValueError('Unknown V8 unit view '+view)
    thing['ai_design']=dict(style='ai_version_8',part_role='frame',view=view,expected_bodies=count,
        bom=p['bom'],grid_per_face=[p['column'],p['row']],drawer_count=q['drawer_count'],selected_clip_sample=71,
        printable=view not in ['assembled','print_layout'],physical_fit='User selected sample 71; complete assembly requires testing')


def configure_v8_joiners(p):
    q=p['frame'];cap=p['front_plug'];j=p['corner_fixing']
    depth=cap['outer_y']-p['panel_thickness']
    edge=cap['cover_width']/2
    station=max(p['grip_length'],p['side_runner']['end_length'])+j['nut_seat_clearance']
    j.update(joining_plate_thickness=depth, joining_plate_edge_distance=edge,
             joining_plate_radius=cap['cover_radius'], backer_depth=station+j['nut_recess'],
             joiner_bore_radius=oobb.gv('hole_radius_m3','3dpr'))
    reach=j['screw_length']+j['screw_reference_recess']-depth-p['panel_thickness']
    if j['screw_length']>25 or reach-station-oobb.gv('nut_depth_m3','true')<1:
        raise ValueError('Use a countersunk screw of at most 25 mm with full nut engagement')
    if not p.get('draw_joiners'):
        return
    # Raise the outside face over a seated clip. Deepen the head recess by
    # the same amount so the screw, nut and existing beam relief stay aligned.
    rise = j['cap_axial_clearance'] + j['front_roof_thickness']
    if min(j['cap_axial_clearance'], j['cap_side_clearance']) <= 0 or not 0 <= j['loose_cap_extra_clearance'] <= j['front_roof_thickness'] - 2:
        raise ValueError('The clip pocket needs positive clearance and a roof at least 2 mm thick')
    j['cap_projection'] = depth
    depth += rise
    j['joining_plate_thickness'] = depth
    j['screw_reference_recess'] += rise
    j['countersink_setback'] += rise
    if depth-j['countersink_setback']-oobb.gv('screw_countersunk_depth_m3','3dpr')<1.2:
        raise ValueError('Insufficient material beneath the countersink')
    pitch=2*q['corner_hole_inset']+j['joining_plate_unit_gap']
    width=pitch+2*edge
    center=(width+j['joining_plate_layout_gap'])/2
    p['joiners']=[]
    for four in [True,False]:
        ys=[-pitch/2,pitch/2] if four else [0]
        p['joiners'].append(dict(name='four_unit_joiner' if four else 'two_unit_joiner',
            size=[width,width if four else 2*edge,depth],hole_pitch_mm=pitch,
            holes=[[x,y] for x in [-pitch/2,pitch/2] for y in ys],
            print_center=[-center if four else center,0,0]))


def v8_joiner_reliefs(p,part,inside,clasp_clearance=False):
    """Map each nearby mount into this universal part's own print coordinates."""
    j=p['corner_fixing'];r=p['side_runner'];s=p['screw'];cap=p['front_plug']
    depth=j['backer_depth'] if inside else part['size'][2]
    half_x,half_y=[v/2 for v in part['size'][:2]]
    layout=v8_joiner_layout(p);cuts=set();gap=j['beam_clearance']
    for placement in layout['joiners']:
        if p['joiners'][placement['part']]['name']!=part['name']:continue
        cx,cy,_=placement['centre']
        for ux,uy,_ in layout['units']:
            for mount in p['frame_mounts']:
                x=ux+mount['x']-cx;y=uy+mount['hole_y']-cy
                # Coordinates in the front assembly. The runner sits above the mount.
                if inside:
                    lo=-r['bed_x']-r['width'];hi=-r['bed_x']
                    roof=p['beam_running_height']-p['tongue_height']/2
                    profiles=[(lo,hi,-roof,-roof+r['thickness'],0,depth),
                              (lo,hi,-s['end_height']/2,s['end_height']/2,
                               depth-max(r['end_length'],p['grip_length'])-gap,depth)]
                else:
                    # Every receiver can carry a clip. Leave a closed roof over its cap.
                    dx=-cap['cover_offset_y'];w=cap['cover_height'];h=cap['cover_width']
                    extra = j['loose_cap_extra_clearance'] if clasp_clearance else 0
                    cap_ceiling = depth - j['cap_projection'] - j['cap_axial_clearance'] - extra
                    profiles=[(dx-w/2,dx+w/2,-h/2,h/2,cap_ceiling,depth)]
                    w,h,t=s['flange_size'];dx=s['flange_offset_x']
                    profiles.append((dx-w/2,dx+w/2,-h/2,h/2,depth-t-gap,depth))
                a=placement['angle']
                for profile_index, (left,right,bottom,top,z0,z1) in enumerate(profiles):
                    cap_pocket = not inside and profile_index == 0
                    clearance = j['cap_side_clearance'] + extra if cap_pocket else gap
                    points=[(x+i,y+k) for i in [left-clearance,right+clearance] for k in [bottom-clearance,top+clearance]]
                    local=[(v,-u) if a==90 else (-v,u) if a==-90 else (u,v) for u,v in points]
                    # Outside rear flips X; front backing flips Y and rear turns 180 about Z.
                    for rear in [False,True]:
                        xy=[((-u if rear else u),(-v if inside else v)) for u,v in local]
                        x0=max(-half_x-.1,min(u for u,v in xy));x1=min(half_x+.1,max(u for u,v in xy))
                        y0=max(-half_y-.1,min(v for u,v in xy));y1=min(half_y+.1,max(v for u,v in xy))
                        if x1>x0 and y1>y0:
                            if inside:
                                # Open the relief toward the beam, through the
                                # short outside edge. Avoid trapped ledges during
                                # lateral assembly and isolated slivers on the bed.
                                if a==0:y0=-half_y-.1
                                elif (a==90) != rear:x1=half_x+.1
                                else:x0=-half_x-.1
                            radius=0
                            if cap_pocket:
                                x0=min(u for u,v in xy);x1=max(u for u,v in xy)
                                y0=min(v for u,v in xy);y1=max(v for u,v in xy)
                                radius=cap['cover_radius']+clearance
                            cuts.add(tuple(round(v,5) for v in (x0,y0,z0-.01,x1,y1,z1+.1,radius)))
    return sorted(cuts)


def draw_joiner(thing,p,part,color='',clasp_clearance=False):
    import working_scad_container_cutout as cuts
    oobb.append_full(thing,type='positive',shape='rounded_rectangle',m='',color=color,
        size=part['size'],radius=p['front_plug']['cover_radius'],pos=[0,0,0])
    cuts.cut([0,0,0],thing,
        **dict(p,v8_component='joining_plate',joining_plate=part,reliefs=v8_joiner_reliefs(p,part,False,clasp_clearance)))


def draw_hardware(thing,p,kind):
    """Purchased hardware reference in OOBB true dimensions; never print it."""
    if kind=='screw':
        oobb.append_full(thing,type='positive',shape='oobb_screw_countersunk',m='',
            mode='true',radius_name='m3',depth=p['corner_fixing']['screw_length'],
            hole=True,nut_include=False,include_nut=False,clearance=[],overhang=False,
            zz='none',rot=[180,0,0],pos=[0,0,0])
    elif kind=='nut':
        import working_scad_container_cutout as cuts
        oobb.append_full(thing,type='positive',shape='oobb_nut',m='',mode='true',
            radius_name='m3',zz='bottom',clearance='',overhang=False,
            rot=[0,0,0],pos=[0,0,0])
        cuts.cut([0,0,0],thing,
            **dict(p,v8_component='joiner_nut_reference'))
    else:raise ValueError('Unknown joiner hardware '+kind)


def draw_backer(thing,p,part,color=''):
    """Continuous extrusion of the relieved outline, nut pockets on the bed."""
    import working_scad_container_cutout as cuts
    j=p['corner_fixing']
    oobb.append_full(thing,type='positive',shape='rounded_rectangle',m='',color=color,
        size=[*part['size'][:2],j['backer_depth']],radius=j['joining_plate_radius'],pos=[0,0,0])
    cuts.cut([0,0,0],thing,
        **dict(p,v8_component='joiner_backer',joining_plate=part,reliefs=v8_joiner_reliefs(p,part,True)))


def v8_joiner_layout(p):
    q=p['frame'];gap=p['corner_fixing']['joining_plate_unit_gap']
    w=q['width_total']+gap;h=q['height_total']+gap;inset=q['corner_hole_inset']+gap/2
    return dict(units=[[sx*w/2,sy*h/2,0] for sx in [-1,1] for sy in [-1,1]],
        joiners=[dict(part=0,centre=[0,0,0],angle=0)]+
            [dict(part=1,centre=[0,sy*(h-inset),0],angle=0) for sy in [-1,1]]+
            [dict(part=1,centre=[sx*(w-inset),0,0],angle=90*sx) for sx in [-1,1]])


def draw_joiners_scene(thing,p,detail=False,section=False):
    """Four actual current units; orange joiners and silver purchased hardware."""
    scene=oobb.get_default_thing(type='v8_joiners_in_use');layout=v8_joiner_layout(p)
    for xy in layout['units']:
        oobb.append_full(scene,type='positive',shape='import_stl',m='',
            file=p.get('assembly_reference_file','assembled.stl'),pos=xy,color=[.24,.48,.54])
    for placement in layout['joiners'][:1] if detail else layout['joiners']:
        part=p['joiners'][placement['part']];x,y,_=placement['centre'];angle=placement['angle']
        sub=oobb.get_default_thing(type='v8_joiner_in_use')
        draw_joiner(sub,p,part,color=[1,.49,.12])
        scene['components'].append(dict(type='rotation',typetype='positive',
            rot=[0,0,angle],pos=[x,y,-part['size'][2]],objects=sub['components']))
        backing=oobb.get_default_thing(type='v8_backer_in_use')
        draw_backer(backing,p,part,color=[.79,.62,.32])
        end=p['panel_thickness']+p['corner_fixing']['backer_depth']
        scene['components'].append(dict(type='rotation',typetype='positive',
            rot=[180,0,angle],pos=[x,y,end],objects=backing['components']))
        import math
        for hx,hy in part['holes']:
            a=math.radians(angle);j=p['corner_fixing']
            for kind,z in [('screw',-part['size'][2]+j['screw_reference_recess']),('nut',end-j['nut_recess'])]:
                yy=hy
                px=x+hx*math.cos(a)-yy*math.sin(a);py=y+hx*math.sin(a)+yy*math.cos(a)
                metal=oobb.get_default_thing(type='v8_joiner_hardware_pose')
                oobb.append_full(metal,type='positive',shape='import_stl',m='',
                    file=f'joiner_{kind}_reference.stl',color=[.72,.75,.78])
                scene['components'].append(dict(type='rotation',typetype='positive',
                    rot=[0,0,angle],pos=[px,py,z],objects=metal['components']))
    if detail:
        # Cut only the reference scene, to expose pads, adapter clearance and nuts.
        for size,pos in [([1000,1000,500],[-500,-500,55]),
                         ([500,1000,1000],[24,-500,-500]),([500,1000,1000],[-524,-500,-500]),
                         ([1000,500,1000],[-500,24,-500]),([1000,500,1000],[-500,-524,-500])]:
            oobb.append_full(scene,type='negative',shape='cube',m='',size=size,pos=pos)
    if section:
        oobb.append_full(scene,type='negative',shape='cube',m='',size=[100,105,120],pos=[-50,-100,-10])
    thing['components'].append(dict(type='rotation',typetype='positive',
        rot=[-90,0,0],pos=[0,0,0],objects=scene['components']))




def floor_supports(p):
    """CAD +Y points down in service. Every inter-row stop bears on the floor above."""
    import math
    for key in ['floor_support_tab_width','floor_support_projection','floor_support_thickness','floor_support_tip_chamfer']:
        value=p[key]
        if not isinstance(value,(int,float)) or not math.isfinite(value) or value <= 0:
            raise ValueError('Invalid floor support parameter: '+key)
    width=p['floor_support_tab_width']
    span=p['catch_tab_width']
    tip=p['floor_support_tip_chamfer']
    thick=p['floor_support_thickness']
    gap=p['pitch_y']-p['opening_height']
    if width != 15 or 2*width >= span:
        raise ValueError('Use two 15 mm tabs with an open centre in the original stop span')
    if p['floor_support_projection'] != 12:
        raise ValueError('Floor extensions project 12 mm past the 6 mm web')
    if not p['thickness_wall'] <= thick < gap or not 0 < tip < thick:
        raise ValueError('Supports must fit between the drawer floors and next top openings')
    depth=p['plate_thickness']+p['floor_support_projection']
    root=gap+p['catch_tab_height']
    ramp=root-thick
    if ramp >= depth-tip:
        raise ValueError('Leave a flat underside after the 45 degree root ramp')
    features=[]
    for col in range(p['column']):
        cx=-p['natural_width']/2+p['drawer_border_edge']+p['opening_width']/2+col*p['pitch_x']
        for tab in [0,1]:
            x=cx-span/2+(span-width)*tab
            # At the cabinet top there is no preceding drawer floor. Retain two
            # small tapered catches only, with no inward floor extension.
            top=p['opening_origin_y']
            features.append(dict(kind='top_catch',column=col,supported_row=None,
                pos=[x,top-p['thickness_wall'],0],
                envelope=[width,p['thickness_wall']+p['catch_tab_height'],p['plate_thickness']]))
            # Row N-1 is the physical bottom drawer: its floor gets plywood,
            # so do not create a support at that floor.
            for row in range(p['row']-1):
                floor=p['opening_origin_y']+row*p['pitch_y']+p['opening_height']
                features.append(dict(kind='floor',column=col,supported_row=row,
                    pos=[x,floor,0],envelope=[width,root,depth],
                    bearing_y=floor,ramp_end_z=ramp))
    return features


def main(**kwargs):
    from v8_manufacturing import generate
    generate(**kwargs)

CABINET_SOLIDS = """
module cap_panel() {
  difference() {
    translate([-cap_w/2,0,0]) cube([cap_w,t,depth]);
    cap_bores();
  }
}
module side_panel() {
  difference() {
    cube([t,inside_h,depth]);
    side_bores();
  }
}
module wood_screw(length) {
  // Flush 90-degree head, nominal shank and tapered point. Thread envelope.
  difference(){
    union(){
      cylinder(h=1.75,d1=7,d2=3.5);
      translate([0,0,1.74]) cylinder(h=length-4.74,d=3.5);
      translate([0,0,length-3.01]) cylinder(h=3.01,d1=3.5,d2=0);
    }
    for(a=[0,90]) rotate([0,0,a]) translate([-2,-.4,-.01]) cube([4,.8,.81]);
  }
}
module dowel() {
  cylinder(h=.5,d1=5,d2=6);
  translate([0,0,.5]) cylinder(d=6,h=23);
  translate([0,0,23.5]) cylinder(h=.5,d1=6,d2=5);
}
"""


def cabinet_fastener(kind,p):
    thing=oobb.get_default_thing(type="cabinet_hardware")
    if kind=="nut":
        draw_hardware(thing,p,"nut")
    else:
        oobb.append_full(thing,type="positive",shape="oobb_screw_socket_cap",mode="true",
            radius_name="m3",depth=12,hole=True,nut_include=False,include_nut=False,
            clearance=[],overhang=False,zz="none",rot=[180,0,0],pos=[0,0,0])
    return thing

# Shared by the independent joint records and the cabinet. Z=0 is the outside print face.
BEAM_JOINT_SOLIDS = """
module plate_outline(bounds) {
  r=2;
  offset(r=r) translate([bounds[0]+r,bounds[1]+r])
    square([bounds[2]-bounds[0]-2*r,bounds[3]-bounds[1]-2*r]);
}
module beam_joint(holes,bounds,wood=[],access=[]) {
  union(){
    for(p=holes) translate(p) intersection(){
      native_adapter();
      cylinder(r=4,h=12);
    }
    difference(){
      linear_extrude(tie_t) union(){
        plate_outline(bounds);
        for(p=holes) hull(){
          translate(p) circle(r=4.1);
          translate([p[0]+(p[0]==0 ? 3 : -3),p[1]]) circle(r=4.1);
        }
      }
      joint_bores(holes,wood,access);
    }
  }
}
"""
