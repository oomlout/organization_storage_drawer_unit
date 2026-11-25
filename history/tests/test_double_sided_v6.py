import unittest
import working_oomp_populate as population
import working_scad as drawing

class DoubleSidedTests(unittest.TestCase):
    def parameters(self, **changes):
        return drawing.get_ai_version_6_parameters(**dict(population.get_ai_version_6_options()[0],**changes))

    def test_capacity_and_compact_limits(self):
        p=self.parameters()
        self.assertEqual([p['width_total'],p['height_total'],p['drawer_count']],[197.8,220.3,28])
        self.assertAlmostEqual(p['width_total'],p['natural_width'])
        self.assertAlmostEqual(p['height_total'],p['opening_grid_height']+2*p['face_edge_y'])
        self.assertGreater(p['density_limits']['next_column_width_mm'],250)
        self.assertGreater(p['density_limits']['next_row_height_mm'],250)
        # Eight rows cannot fit even with minimum 1.8 mm top/bottom walls.
        self.assertGreater(8*p['opening_height']+7*(p['thickness_wall']+p['row_spacing_extra'])+2*p['thickness_wall'],250)
        self.assertEqual([p['opening_width'],p['opening_height'],p['pitch_y']],[87.5,28.5,31.3])

    def test_opposing_drawers_have_independent_stop_faces(self):
        p=self.parameters()
        self.assertEqual(p['assembled_depth'],224)
        stop=p['plate_thickness']+p['middle_stop_z']
        self.assertEqual(stop-p['middle_stop_thickness']/2,p['bank_depth'])
        self.assertEqual(p['assembled_depth']-stop-p['middle_stop_thickness']/2,p['bank_depth'])
        self.assertGreaterEqual(p['bank_depth']-p['container_depth'],1.5)
        self.assertGreater(p['middle_stop_width']/2,p['inset_lip']+3)

    def test_four_screw_replacements_and_no_redundant_border_holes(self):
        p=self.parameters()
        self.assertEqual(p['bom'],dict(front=1,back=1,snap_rail=17,screw_rail=4,screw_adapter=8,M3_countersunk_screw_20_mm=8,M3_nut=8))
        for x in p['x_mounts']:
            rows=[r for r in p['rail_positions'] if r['x']==x]
            self.assertEqual(len(rows),7)
            self.assertTrue(all(r['connection'] in ['snap','screw_adapter'] for r in rows))
            self.assertGreater(p['height_total']/2-max(r['y']+p['rail_height'] for r in rows),8)
        self.assertFalse(p['rear_attachments'])

    def test_four_corner_m3_holes_clear_trays_and_rail_mounts(self):
        import oobb
        p=self.parameters()
        self.assertEqual(len(p['corner_holes']),4)
        self.assertEqual(p['corner_hole_size'],'m3')
        radius=oobb.gv('hole_radius_m3','3dpr')
        for h in p['corner_holes']:
            self.assertAlmostEqual(p['width_total']/2-abs(h['x']),5)
            self.assertAlmostEqual(p['height_total']/2-abs(h['y']),5)
            self.assertGreater(5-radius,1.8)
            for rail in p['rail_positions']:
                self.assertTrue(abs(h['x']-rail['x'])>p['rail_width']/2+radius or
                                h['y']+radius<rail['y'] or h['y']-radius>rail['y']+p['rail_height'])

    def test_selected_recessed_springs_and_both_outer_catches(self):
        p=self.parameters()
        self.assertEqual(p['snap_profile']['twin_arm_thickness'],1.8)
        self.assertEqual([p['snap_tip_length'],p['snap_shoulder_depth'],p['snap_root_distance']],[6,4.5,2])
        self.assertTrue(p['front_lip'] and p['rear_lip'])
        self.assertEqual(p['plate_print_depth'],18)

    def test_both_sizes_adopt_37_without_altering_receiver_or_kit(self):
        trial=drawing.get_ai_version_6_clearance_parameters(**population.get_ai_version_6_clearance_options()[0])['trials'][7]
        for option in population.get_ai_version_6_options():
            p=drawing.get_ai_version_6_parameters(**option)
            self.assertEqual(p['selected_latch_sample'],37)
            self.assertEqual(p['selected_rail_fit'],trial)
            self.assertEqual([trial['hook_projection'],trial['shoulder_depth'],trial['insertion_deflection']],[1.4,4.4,1.15])
            old=dict(option);old.pop('selected_latch_sample')
            reference=drawing.get_ai_version_6_parameters(**old)
            self.assertEqual({k:v for k,v in p.items() if k not in ['selected_latch_sample','selected_rail_fit']},reference)
        with self.assertRaises(ValueError):
            self.parameters(selected_latch_sample=99)
        self.assertNotIn('selected_latch_sample',population.get_ai_version_6_clearance_options()[0]['reference_frame'])

    def test_joiners_align_with_four_existing_unit_corners(self):
        p=self.parameters()
        four,two=p['joining_plates']
        self.assertEqual(four['size'],[20,20,6])
        self.assertEqual(two['size'],[20,10,6])
        corners=[]
        for sx in [-1,1]:
            for sy in [-1,1]:
                cx=sx*p['width_total']/2
                cy=sy*p['height_total']/2
                nearest=min(p['corner_holes'],key=lambda h:(cx+h['x'])**2+(cy+h['y'])**2)
                corners.append([round(cx+nearest['x'],6),round(cy+nearest['y'],6)])
        self.assertEqual(sorted(corners),sorted(four['holes']))
        self.assertEqual(two['holes'],[[-5,0],[5,0]])
        self.assertEqual(two['holes'][1][0]-two['holes'][0][0],2*p['corner_hole_inset'])
        self.assertEqual(p['bom']['snap_rail'],17)
        self.assertEqual(p['bom']['screw_rail'],4)

    def test_joiner_countersinks_retain_edges_and_reject_invalid_dimensions(self):
        import oobb
        p=self.parameters()
        self.assertGreaterEqual(p['joining_plate_edge_distance']-oobb.gv('screw_countersunk_radius_m3','3dpr'),1.2)
        for change in [dict(joining_plate_thickness=3),dict(joining_plate_edge_distance=4),
                       dict(joining_plate_unit_gap=-1),dict(joining_plate_radius=2)]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                self.parameters(**change)

    def test_395_max_uses_largest_compact_grid_without_square_padding(self):
        option=population.get_ai_version_6_options()[1]
        p=drawing.get_ai_version_6_parameters(**option)
        self.assertEqual([p['column'],p['row'],p['drawer_count']],[4,12,96])
        self.assertEqual([p['width_total'],p['height_total'],p['assembled_depth']],[376.4,376.8,224])
        self.assertAlmostEqual(p['width_total'],4*87.5+3*1.8+2*10.5)
        self.assertAlmostEqual(p['height_total'],12*28.5+11*2.8+2*2)
        self.assertGreater(p['density_limits']['next_column_width_mm'],395)
        self.assertGreater(p['density_limits']['next_row_height_mm'],395)
        self.assertEqual(p['bom'],dict(front=1,back=1,snap_rail=56,screw_rail=4,screw_adapter=8,M3_countersunk_screw_20_mm=8,M3_nut=8))
        self.assertEqual([p['rails_per_plate'],p['rail_plate_count']],[16,4])
        with self.assertRaises(ValueError):
            drawing.get_ai_version_6_parameters(**dict(option,target_width=395,target_height=395))

    def test_395_rails_and_joiners_match_250_interfaces(self):
        small=self.parameters()
        large=drawing.get_ai_version_6_parameters(**population.get_ai_version_6_options()[1])
        for key in ['rail_length','snap_tip_length','snap_shoulder_depth','snap_root_distance',
                    'snap_profile','middle_stop_width','middle_stop_thickness','joining_plates']:
            self.assertEqual(large[key],small[key],key)
        for h in large['corner_holes']:
            self.assertAlmostEqual(large['width_total']/2-abs(h['x']),5)
            self.assertAlmostEqual(large['height_total']/2-abs(h['y']),5)
        self.assertEqual(large['bed_exclusion'],[0,0])
        self.assertGreaterEqual(large['bed_width']-2*large['bed_margin'],large['width_total'])
        self.assertGreaterEqual(large['bed_height']-2*large['bed_margin'],large['height_total'])

    def test_split_floor_supports_leave_bottom_for_plywood(self):
        for option in population.get_ai_version_6_options():
            p=drawing.get_ai_version_6_parameters(**option)
            supports=[f for f in p['floor_support_features'] if f['kind']=='floor']
            self.assertEqual(len(supports),2*p['column']*(p['row']-1))
            self.assertEqual(p['plate_print_depth'],18)
            self.assertEqual(p['catch_tab_width']-2*p['floor_support_tab_width'],26)
            self.assertTrue(all(f['supported_row']<p['row']-1 for f in supports))
            for f in supports:
                self.assertEqual(f['envelope'],[15,8.8,18])
                floor=p['opening_origin_y']+f['supported_row']*p['pitch_y']+p['opening_height']
                self.assertAlmostEqual(f['bearing_y'],floor)
                self.assertAlmostEqual(f['ramp_end_z'],6.8)

    def test_receiver_web_has_matching_rail_clearance(self):
        for option in population.get_ai_version_6_options():
            p=drawing.get_ai_version_6_parameters(**option)
            self.assertEqual(p['snap_inner_web_height'],1)
            self.assertEqual(p['snap_tip_root_floor'],1.25)
            # At both panel faces the tab floor remains .25 mm above its receiver.
            for z in [0,3,6]:
                rail=p['snap_tip_floor']-p['snap_bevel_slope']*z
                receiver=p['snap_tip_floor']-p['snap_clearance']-p['snap_bevel_slope']*z
                self.assertAlmostEqual(rail-receiver,.25)
                self.assertGreaterEqual(receiver,1)

    def test_lower_web_is_solid_and_cutout_radii_match(self):
        for option in population.get_ai_version_6_options():
            p=drawing.get_ai_version_6_parameters(**option)
            self.assertEqual(p['body_extension_height'],0)
            self.assertEqual(p['opening_radius'],1)
            self.assertEqual(p['opening_radius'],p['lip_cutout_radius'])
        for change in [dict(body_extension_height=1),dict(body_cutout_radius=4)]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                self.parameters(**change)

    def test_invalid_envelopes_and_stops_rejected(self):
        for change in [dict(target_width=251),dict(target_height=251),dict(target_width=200),
                       dict(column=3),dict(row=8),dict(face_edge_y=1),dict(corner_hole_inset=1),dict(middle_stop_width=11),
                       dict(middle_stop_width=40),dict(middle_stop_thickness=0)]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                self.parameters(**change)

if __name__=='__main__':
    unittest.main()
