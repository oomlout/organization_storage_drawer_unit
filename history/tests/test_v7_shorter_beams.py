import copy
import unittest
import working_oomp_populate as population
import working_scad as drawing


class ShorterBeamTests(unittest.TestCase):
    def test_all_current_units_and_configurable_full_depth(self):
        for source in population.get_current_options():
            before=copy.deepcopy(source)
            p=drawing.get_ai_version_7_frame_parameters(**source)
            full=drawing.get_ai_version_7_frame_parameters(**dict(source,beam_depth_reduction_per_end=0))
            self.assertEqual(source,before)
            self.assertAlmostEqual(p['rail_length'],197)
            self.assertAlmostEqual(p['frame']['assembled_depth'],209)
            self.assertAlmostEqual(full['rail_length']-p['rail_length'],15)
            self.assertEqual(p['frame_mounts'],full['frame_mounts'])
            self.assertEqual(p['screw'],full['screw'])
            for amount in [0,2.5,7.5,10]:
                custom=drawing.get_ai_version_7_frame_parameters(**dict(source,beam_depth_reduction_per_end=amount))
                self.assertAlmostEqual(custom['rail_length'],212-2*amount)
                self.assertAlmostEqual(custom['frame']['middle_stop_z'],custom['rail_length']/2)

    def test_invalid_or_excessive_shortening_rejected(self):
        source=population.get_current_options()[-1]
        for amount in [-1,float('nan'),float('inf'),'7.5',True,100]:
            with self.subTest(amount=amount),self.assertRaises(ValueError):
                drawing.get_ai_version_7_frame_parameters(**dict(source,beam_depth_reduction_per_end=amount))

    def test_historical_unit_retains_full_depth(self):
        p=drawing.get_ai_version_7_frame_parameters(**population.get_ai_version_7_options()[-1])
        self.assertEqual(p['rail_length'],212)
        self.assertEqual(p['beam_depth_reduction_per_end'],0)
