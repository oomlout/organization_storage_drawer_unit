import unittest
import working_oomp_populate as population
import working_scad as drawing
from working_scad_v7 import views


class PushInCapTests(unittest.TestCase):
    def test_four_relief_caps_per_complete_unit_and_remaining_square(self):
        for source in population.get_current_options():
            p=drawing.get_ai_version_7_frame_parameters(**source)
            self.assertEqual(p['cap_quantities']['front_plug'],4)
            self.assertEqual(p['cap_quantities']['front_plug_square'],2*p['snap_beam_count']-4)
            self.assertIn('front_plug_square',views(p))
            total={name:0 for name in p['cap_quantities']}
            for batch in p['print_batches'].values():
                if batch['component'] in total:total[batch['component']]+=batch['count']
            self.assertEqual(total,p['cap_quantities'])
            snaps=[m for m in p['frame_mounts'] if m['kind']=='snap_beam']
            self.assertEqual(sum(m['cap_component']=='front_plug' for m in snaps),2)
            self.assertEqual(sum(m['cap_component']=='front_plug_square' for m in snaps),p['snap_beam_count']-2)

    def test_historical_unit_keeps_original_cap_batches(self):
        p=drawing.get_ai_version_7_frame_parameters(**population.get_ai_version_7_options()[-1])
        self.assertNotIn('cap_quantities',p)
        self.assertIn('front_plugs',p['print_batches'])
        self.assertNotIn('front_plug_square',views(p))
