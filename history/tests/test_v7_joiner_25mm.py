import unittest
from unittest.mock import patch

import working_oomp_populate as population
import working_scad as drawing
import working_scad_container_cutout as cutouts


class JoinerTests(unittest.TestCase):
    def test_stack_rejects_long_screw_and_incomplete_engagement(self):
        for length in [20, 30, 35]:
            source = population.get_current_options()[-1]
            source['optional_joiners']['screw_length'] = length
            with self.subTest(length=length), self.assertRaises(ValueError):
                drawing.get_ai_version_7_frame_parameters(**source)

    def test_cutters_load_from_the_accessible_ends(self):
        source = population.get_current_options()[-1]
        p = drawing.get_ai_version_7_frame_parameters(**source)
        for component, shape in [('joining_plate', 'oobb_screw_countersunk'), ('joiner_backer', 'oobb_nut')]:
            with self.subTest(component=component), patch.object(cutouts.oobb, 'append_full') as append:
                cutouts.get_container_cutout_ai_version_7([0, 0, 0], {}, **dict(
                    p, v7_component=component, joining_plate=p['joiners'][0], reliefs=[]))
                calls = [call.kwargs for call in append.call_args_list if call.kwargs['shape'] == shape]
                self.assertEqual(len(calls), 4)
                for cutter in calls:
                    self.assertEqual(cutter['mode'], '3dpr')
                    self.assertEqual(cutter['radius_name'], 'm3')
                    self.assertTrue(cutter['overhang'])
                    self.assertIn('top', cutter['clearance'])
                    self.assertEqual(cutter['rot'], [180, 0, 0])
