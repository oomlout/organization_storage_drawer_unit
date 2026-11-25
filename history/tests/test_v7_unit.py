import copy
import unittest
import working_oomp_populate as population
import working_scad as drawing


class SelectedUnitTests(unittest.TestCase):
    def setUp(self):
        self.inputs=population.get_ai_version_7_options()[-1]
        self.p=drawing.get_ai_version_7_frame_parameters(**self.inputs)

    def test_selected_interface_is_preserved_except_plug_tip(self):
        old=drawing.get_ai_version_7_parameters(**population.get_ai_version_7_options()[5])
        for key in ['trials','spring_root_y','neck_width','tongue_height','receiver_hole_width',
                    'receiver_hole_height','hook_projection','hook_land','retaining_rake','upper_support_height']:
            self.assertEqual(self.p[key],old[key],key)
        for key in old['front_plug']:
            if key!='nose_width':self.assertEqual(self.p['front_plug'][key],old['front_plug'][key],key)
        self.assertLess(self.p['front_plug']['nose_width'],old['front_plug']['nose_width'])

    def test_grid_and_requested_quantities(self):
        p=self.p;q=p['frame']
        self.assertEqual((p['column'],p['row']),(1,2))
        self.assertEqual(p['bom']['snap_beam'],4)
        self.assertEqual(p['bom']['screw_beam'],2)
        self.assertEqual(p['bom']['front_plug'],8)
        self.assertEqual(p['bom']['M3_nut'],4)
        self.assertEqual(len(p['frame_mounts']),6)
        self.assertEqual(q['drawer_count'],4)
        self.assertAlmostEqual(q['rail_length'],212)

    def test_top_braces_clear_the_drawer_openings(self):
        p=self.p;q=p['frame'];half=p['screw']['end_height']/2
        for r in p['frame_mounts']:
            if r['kind']=='screw_beam':
                self.assertLess(r['hole_y']+half,q['opening_origin_y'])
                self.assertGreater(r['hole_y']-half,-q['height_total']/2)

    def test_parameters_are_pure_and_invalid_quantity_rejected(self):
        original=copy.deepcopy(self.inputs)
        drawing.get_ai_version_7_frame_parameters(**self.inputs)
        self.assertEqual(original,self.inputs)
        self.inputs['snap_beam_count']=5
        with self.assertRaises(ValueError):drawing.get_ai_version_7_frame_parameters(**self.inputs)

    def test_screw_and_snap_share_the_service_bearing_height(self):
        p=self.p
        self.assertAlmostEqual(p['screw']['running_height']-p['screw']['axis_height'],
                               p['beam_running_height']-p['tongue_height']/2)
        # The deeper screw/nut reinforcement must remain above the drawer floor.
        for r in p['frame']['rail_positions']:
            floor=r['y']-p['frame']['depth_lip']+p['frame']['opening_height']
            beam_bottom=r['y']+8+p['screw']['axis_height']
            self.assertGreaterEqual(floor-beam_bottom,2-1e-6)

    def test_windows_keep_ends_side_rails_and_stop_solid(self):
        p=self.p;w=p['beam_lightening']
        self.assertEqual(len(p['beam_windows']),2)
        self.assertGreaterEqual((p['grip_width']-w['width'])/2,3)
        self.assertGreaterEqual(w['end_land'],p['beam_end_length']+p['beam_transition_length'])
        self.assertGreaterEqual(w['centre_land'],p['frame']['middle_stop_thickness']+8)
        for key,value in [('width',6),('end_land',30),('centre_land',5)]:
            changed=copy.deepcopy(self.inputs);changed['beam_lightening'][key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):
                drawing.get_ai_version_7_frame_parameters(**changed)


if __name__=='__main__':unittest.main()
