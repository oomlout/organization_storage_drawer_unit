import copy
import unittest
import working_oomp_populate as population
import working_scad as drawing


class ThroughPanelTests(unittest.TestCase):
    def setUp(self):
        self.inputs=population.get_ai_version_7_options()[0]
        self.p=drawing.get_ai_version_7_parameters(**self.inputs)

    def test_trial_variables_are_independent(self):
        self.assertEqual([t['sample_number'] for t in self.p['trials']],list(range(40,49)))
        self.assertEqual(len({(t['arm_thickness'],t['axial_clearance']) for t in self.p['trials']}),9)
        self.assertEqual(self.p['panel_material'],'MDF')
        self.assertAlmostEqual(self.p['retention_overlap'],.55)
        for t in self.p['trials']:
            self.assertLess(t['tip_y']-6,2)
            self.assertGreater(t['spring_length'],16)
            self.assertLess(t['strain_proxy'],.01)

    def test_drawing_does_not_mutate_population(self):
        before=copy.deepcopy(self.inputs)
        drawing.get_ai_version_7_parameters(**self.inputs)
        self.assertEqual(before,self.inputs)

    def test_rigid_interference_is_rejected(self):
        self.inputs['receiver_hole_width']=7.0
        with self.assertRaises(ValueError): drawing.get_ai_version_7_parameters(**self.inputs)

    def test_short_screw_is_rejected(self):
        self.inputs['screw']['length']=16
        with self.assertRaises(ValueError): drawing.get_ai_version_7_parameters(**self.inputs)

    def test_historical_receiver_is_not_replaced(self):
        self.assertEqual([p['selected_latch_sample'] for p in population.get_ai_version_6_options()],[37,37])
        self.assertEqual(self.p['part_role'],'connector_test')
        self.assertAlmostEqual(self.p['screw']['projection_after_nut'],1.6)


class FourFingerMechanismTests(unittest.TestCase):
    def setUp(self):
        self.inputs=population.get_ai_version_7_options()[1]
        self.p=drawing.get_ai_version_7_parameters(**self.inputs)

    def test_different_methods_share_one_interface(self):
        self.assertEqual({t['technique'] for t in self.p['trials']},{'straight','tapered','curved','keeper'})
        self.assertEqual({t['axial_clearance'] for t in self.p['trials']},{.25})
        self.assertEqual(set(self.p['receiver_hole_widths']),{6.0})
        self.assertEqual({t['shoulder_y'] for t in self.p['trials']},{6.25})
        self.assertEqual(len({t['tip_y'] for t in self.p['trials']}),1)

    def test_centre_is_removed_and_seating_strips_gain_material(self):
        self.assertEqual(self.p['finger_count'],4)
        self.assertEqual(self.p['pilot_half_width'],0)
        self.assertAlmostEqual(self.p['outer_strip_width'],1.75)
        old=drawing.get_ai_version_7_parameters(**population.get_ai_version_7_options()[0])
        self.assertLess(self.p['receiver_hole_width'],old['receiver_hole_width'])
        self.assertGreater(self.p['outer_strip_width'],old['grip_width']/2-old['outer']-1)

    def test_key_and_screw_use_the_common_hole(self):
        self.assertLess(self.p['screw']['guide_width'],self.p['receiver_hole_width'])
        self.assertLess(self.p['keeper']['stem_width'],2*(self.p['outer']-1.5))
        self.assertGreater(self.p['keeper']['head_start_y'],max(t['tip_y'] for t in self.p['trials']))


class LoopDropKeyTests(unittest.TestCase):
    def setUp(self):
        self.inputs=population.get_ai_version_7_options()[2]
        self.p=drawing.get_ai_version_7_parameters(**self.inputs)

    def test_loop_is_an_additional_rigid_technique(self):
        trial=next(t for t in self.p['trials'] if t['sample_number']==54)
        self.assertEqual(trial['technique'],'drop_loop')
        self.assertNotIn('spring_length',trial)
        self.assertEqual([t['sample_number'] for t in self.p['trials']],[50,51,52,53,54])
        self.assertEqual(set(self.p['receiver_hole_widths']),{6.0})
        self.assertEqual(self.p['neck_width'],5.5)

    def test_key_clearance_and_stops(self):
        d=self.p['drop_loop']
        self.assertGreater(d['eye_width'],d['key_width'])
        self.assertGreater(d['eye_depth'],d['key_depth'])
        self.assertGreater(d['key_length'],self.p['receiver_hole_height'])
        self.assertGreater(d['key_head_width'],d['eye_width'])
        self.assertAlmostEqual(d['axial_play'],.25)
        self.assertAlmostEqual(d['tip_y']-self.p['panel_thickness'],3.75)

    def test_invalid_key_and_thin_loop_are_rejected(self):
        for change in [dict(key_width=2.5),dict(nose_thickness=1),dict(key_head_width=2)]:
            inputs=copy.deepcopy(self.inputs);inputs['drop_loop'].update(change)
            with self.subTest(change=change),self.assertRaises(ValueError):
                drawing.get_ai_version_7_parameters(**inputs)


class PermanentSnapTests(unittest.TestCase):
    def setUp(self):
        self.inputs=population.get_ai_version_7_options()[3]
        self.p=drawing.get_ai_version_7_parameters(**self.inputs)

    def test_actual_contact_is_required(self):
        self.assertTrue(self.p['required_arm_contact'])
        self.assertAlmostEqual(self.p['deflection'],1.2)
        for t in self.p['trials']:
            self.assertAlmostEqual(t['closed_arm_gap'],0)
            self.assertAlmostEqual(t['closed_hook_width'],self.p['receiver_hole_width'])

    def test_holes_shrink_and_retaining_hooks_grow(self):
        old=population.get_ai_version_7_options()[1]
        self.assertLess(self.p['receiver_hole_width'],old['receiver_hole_width'])
        self.assertLess(self.p['receiver_hole_height'],old['receiver_hole_height'])
        self.assertGreater(self.p['hook_projection'],old['hook_projection'])
        self.assertGreater(self.p['retention_overlap'],1)
        self.assertGreater(self.p['retaining_rake'],0)
        self.assertEqual([t['sample_number'] for t in self.p['trials']],[60,61,62])

    def test_impossible_or_partial_contact_fit_is_rejected(self):
        for projection in [1.3,1.5]:
            inputs=copy.deepcopy(self.inputs);inputs['hook_projection']=projection
            with self.subTest(projection=projection),self.assertRaises(ValueError):
                drawing.get_ai_version_7_parameters(**inputs)


class FrontSpreaderPlugTests(unittest.TestCase):
    def setUp(self):
        self.inputs=population.get_ai_version_7_options()[4]
        self.p=drawing.get_ai_version_7_parameters(**self.inputs)

    def test_upper_support_and_taller_hole(self):
        self.assertAlmostEqual(self.p['receiver_hole_height'],5.2)
        self.assertAlmostEqual(self.p['tongue_height'],5.0)
        self.assertGreater(self.p['upper_support_height'],self.p['receiver_hole_height'])
        self.assertEqual(self.p['trials'][0]['sample_number'],70)

    def test_plug_actively_spreads_the_arms(self):
        s=self.p['front_plug']
        self.assertGreater(s['stem_width'],s['free_slot_width'])
        self.assertAlmostEqual(s['seated_spread'],.1)
        self.assertAlmostEqual(s['insertion_spread'],.1)
        self.assertAlmostEqual(s['expanded_neck_width'],5.0)
        self.assertAlmostEqual(s['insertion_neck_width'],5.0)
        self.assertEqual(s['retention'],'friction')
        self.assertNotIn('detent_y',s)
        self.assertNotIn('notch_y',s)

    def test_overwide_plug_and_small_cover_are_rejected(self):
        for change in [dict(stem_width=3),dict(cavity_width=7.7),dict(cap_inner_y=8.3)]:
            inputs=copy.deepcopy(self.inputs);inputs['front_plug'].update(change)
            with self.subTest(change=change),self.assertRaises(ValueError):
                drawing.get_ai_version_7_parameters(**inputs)

    def test_half_depth_spring_preserves_the_friction_interface(self):
        short=population.get_ai_version_7_options()[5]
        p=drawing.get_ai_version_7_parameters(**short)
        self.assertEqual(short['spring_root_y'],self.inputs['spring_root_y']/2)
        self.assertEqual(p['trials'][0]['sample_number'],71)
        self.assertEqual(short['front_plug'],self.inputs['front_plug'])
        self.assertEqual(p['receiver_hole_width'],self.p['receiver_hole_width'])
        self.assertEqual(p['receiver_hole_height'],self.p['receiver_hole_height'])
        self.assertAlmostEqual(p['trials'][0]['closed_arm_gap'],0)


if __name__=='__main__': unittest.main()
