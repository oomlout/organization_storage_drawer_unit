"""Version 4 modular interfaces, bed limits and output quantities."""
import unittest
from unittest.mock import patch
import working_oomp_populate as population
import working_scad as drawing
import working_scad_container_cutout as cutout

class ModularTests(unittest.TestCase):
    def setUp(self):
        self.option=population.get_ai_version_4_options()[0]
    def parameters(self,**changes):
        return drawing.get_ai_version_4_parameters(**dict(self.option,**changes))
    def test_repeatable_top_corner_and_shelf_rails(self):
        p=self.parameters(column=2,row=7)
        self.assertEqual(p['bom']['rail'],24)
        self.assertEqual(p['bom']['bottom_rail'],3)
        self.assertEqual(p['bom']['front'],1)
        self.assertEqual(p['bom']['back'],1)
        self.assertTrue(p['front_lip'])
        self.assertFalse(p['rear_lip'])
        self.assertEqual(p['bom']['M3_nut'],54)
        self.assertEqual(p['rail_length'],95.5)
        self.assertEqual({r['kind'] for r in p['rail_positions']},{'rail','bottom_rail'})
        self.assertEqual(p['nut_far']+p['plate_thickness'],16)
    def test_printer_faces_and_rail_batches_fit(self):
        options=population.get_ai_version_4_options()
        self.assertEqual(len(options),11)
        for option in options:
            p=drawing.get_ai_version_4_parameters(**option)
            self.assertLessEqual(p['plate_width']+2*p['bed_margin'],p['bed_width'])
            self.assertLessEqual(p['plate_footprint_height']+2*p['bed_margin'],p['bed_height'])
            self.assertGreater(p['rails_per_plate'],0)
        mini=next(o for o in options if o.get('variant')=='a1_mini_max')
        self.assertEqual(drawing.get_ai_version_4_parameters(**mini)['rail_plate_count'],2)
    def test_side_loading_uses_real_oobb_clearance_api(self):
        for side in ['left','right']:
            p=self.parameters(nut_side_clearance=side)
            with patch.object(cutout.oobb,'append_full') as append:
                cutout.get_container_cutout_ai_version_4([0,0,0],{},**dict(p,modular_component='rail'))
            nuts=[c.kwargs for c in append.call_args_list if c.kwargs.get('shape')=='oobb_nut']
            self.assertEqual(len(nuts),2)
            self.assertTrue(all(n['overhang'] and n['clearance']==side for n in nuts))
            with patch.object(cutout.oobb,'append_full') as append:
                cutout.get_container_cutout_ai_version_4([0,0,0],{},**dict(p,modular_component='plate_mounts'))
            screws=[c.kwargs for c in append.call_args_list if c.kwargs.get('shape')=='oobb_screw_countersunk']
            self.assertEqual(len(screws),len(p['rail_positions']))
            self.assertTrue(all(s['depth']==16 and s['overhang'] for s in screws))
    def test_invalid_mounts_are_rejected(self):
        for changes in [dict(rail_width=8),dict(rail_width=12),dict(plate_thickness=10),
                        dict(rail_end_band=6),dict(joint_test_depth=30),dict(nut_side_clearance='top'),
                        dict(drawer_border_edge=5.5),dict(inner_guide_depth=3),dict(rail_running_height=2),
                        dict(modular_key_clearance=0.6),dict(plate_thickness=6)]:
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                self.parameters(**changes)
    def test_samples_and_released_version_stay_independent(self):
        original=population.get_ai_version_3_options()
        options=population.get_ai_version_4_options()
        options[0]['drawer_border_edge']=99
        self.assertEqual(original,population.get_ai_version_3_options())
        faces=[o for o in options if o['part_role']=='face_fit']
        self.assertEqual(len(faces),2)
        self.assertEqual(self.parameters(part_role='face_fit')['bom']['front'],1)
        self.assertEqual(self.parameters(part_role='face_fit')['bom']['back'],0)

if __name__=='__main__': unittest.main()
