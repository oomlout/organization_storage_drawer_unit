import copy
import unittest
from unittest.mock import patch
import working_oomp_populate as population
import working_scad as drawing


class V6ClearanceTests(unittest.TestCase):
    def parameters(self,**changes):
        return drawing.get_ai_version_6_clearance_parameters(**dict(population.get_ai_version_6_clearance_options()[0],**changes))

    def test_nine_unique_trials_include_current_fit(self):
        p=self.parameters()
        self.assertEqual([t['sample_number'] for t in p['trials']],list(range(30,39)))
        self.assertEqual({(t['hook_side_clearance'],t['axial_clearance']) for t in p['trials']},
                         {(s,a) for s in [.25,.15,.05] for a in [.2,.1,.05]})
        control=p['trials'][0];base=p['reference']
        self.assertEqual(control['hook_projection'],base['snap_hook_projection'])
        self.assertEqual(control['shoulder_depth'],base['snap_shoulder_depth'])
        self.assertEqual(p['drawer_count'],0)
        self.assertEqual([p['width_total'],p['height_total'],p['assembled_depth']],[43,70,10])

    def test_only_hooks_and_axial_shoulders_change(self):
        p=self.parameters();base=p['reference']
        inputs=population.get_ai_version_6_options()[0]
        inputs.pop('selected_latch_sample',None)
        inputs.pop('screw_rail_settings',None)
        expected=drawing.get_ai_version_6_parameters(**inputs)
        self.assertEqual(base,expected)
        self.assertEqual(base['snap_profile']['twin_arm_thickness'],1.8)
        pocket=base['snap_profile']['snap_arm_outer']+base['snap_hook_projection']+base['snap_clearance']
        for t in p['trials']:
            self.assertAlmostEqual(pocket-base['snap_profile']['snap_arm_outer']-t['hook_projection'],t['hook_side_clearance'])
            self.assertAlmostEqual(base['snap_receiver_shoulder']-(base['plate_thickness']-t['shoulder_depth']),t['axial_clearance'])
            self.assertLessEqual(t['insertion_deflection'],1.15)

    def test_invalid_or_colliding_specimens_rejected(self):
        original=population.get_ai_version_6_clearance_trials()
        for changes in [dict(coupon_grip_length=25),dict(suite_pitch_x=10),dict(suite_pitch_y=20),
                        dict(number_rail_z=3),dict(number_depth=2)]:
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                self.parameters(**changes)
        for change in [dict(hook_side_clearance=0),dict(axial_clearance=-.1),dict(sample_number=29)]:
            trials=copy.deepcopy(original);trials[0].update(change)
            with self.subTest(change=change),self.assertRaises(ValueError):
                self.parameters(trials=trials)

    def test_population_hides_kit_and_counts_no_pots(self):
        with patch.object(population,'write_extras') as writer:
            population.main(catalogue="historical")
        kit=next(p for p in writer.call_args.args[0] if p.get('variant')=='latch_clearance_suite')
        self.assertTrue(kit['comparison_sample'])
        self.assertEqual(kit['drawer_count'],0)
        self.assertEqual(kit['pot_quantity'],0)
        self.assertEqual(kit['filament_density_g_per_cm3'],1.27)
        self.assertIn('connector',kit['print_instruction'])


if __name__=='__main__':
    unittest.main()
