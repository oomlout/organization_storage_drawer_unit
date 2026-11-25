import copy
import unittest
import working_oomp_populate as population
import working_scad as drawing


class V6ScrewAdapterTests(unittest.TestCase):
    def parameters(self,**changes):
        option=population.get_ai_version_6_options()[0]
        option['screw_rail_settings'].update(changes)
        return drawing.get_ai_version_6_parameters(**option)

    def test_four_extreme_rail_positions_replace_snaps_in_both_sizes(self):
        for option in population.get_ai_version_6_options():
            p=drawing.get_ai_version_6_parameters(**option)
            expected={(x,y) for x in [min(p['x_mounts']),max(p['x_mounts'])]
                            for y in [min(r['y'] for r in p['rail_positions']),max(r['y'] for r in p['rail_positions'])]}
            self.assertEqual({(r['x'],r['y']) for r in p['screw_rail_positions']},expected)
            self.assertEqual(p['rail_kinds'].count('screw_rail'),4)
            self.assertEqual(p['rail_kinds'].count('snap_rail'),(p['column']+1)*p['row']-4)
            self.assertEqual(p['bom']['screw_adapter'],8)
            self.assertTrue(all(r['connection']=='screw_adapter' for r in p['screw_rail_positions']))

    def test_screw_stack_and_guide_clearance(self):
        p=self.parameters();s=p['screw_rail']
        self.assertEqual(s['screw_penetration'],11.6)
        self.assertAlmostEqual(s['screw_penetration']-s['nut_far'],1.6)
        self.assertEqual([s['nut_near'],s['nut_far']],[7,10])
        self.assertEqual(s['guide_depth'],5.5)
        self.assertEqual(s['guide_floor_outside'],6)
        self.assertEqual(s['guide_floor_inside'],6.5)
        self.assertEqual((s['guide_width']-s['guide_open_slot_width'])/2,1.5)
        self.assertAlmostEqual(p['assembled_depth']+2*s['flange_size'][2],228.8)

    def test_historical_kit_unchanged_and_new_views_have_expected_bodies(self):
        kit=population.get_ai_version_6_clearance_options()[0]
        self.assertNotIn('screw_rail_settings',kit['reference_frame'])
        p=self.parameters()
        for view,count in [('screw_rail',1),('screw_adapter',1),('screw_adapters',8),('screw_upgrade',12),('print_layout',31)]:
            thing=__import__('oobb').get_default_thing(type='test')
            drawing.get_ai_version_6(thing,**dict(population.get_ai_version_6_options()[0],connector_view=view))
            self.assertEqual(thing['ai_design']['expected_bodies'],count)
        self.assertIn('screw_upgrade',drawing.get_ai_version_6_views(p))

    def test_invalid_hardware_and_weak_walls_rejected(self):
        for change in [dict(replacement_count=5),dict(screw_length=16),dict(axis_height=5),
                       dict(end_height=11),dict(nut_near=10),dict(guide_width=7.3),
                       dict(guide_depth=6),dict(guide_open_slot_width=6),
                       dict(flange_size=[11,10,2]),dict(nut_side_clearance='')]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                self.parameters(**change)


if __name__=='__main__':
    unittest.main()
