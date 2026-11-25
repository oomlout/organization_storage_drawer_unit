"""Current beam regression checks; historical V7 records stay frozen."""
import unittest
from unittest.mock import patch
import numpy as np
import oobb
import working_oomp_populate as population
import working_scad as drawing
import working_scad_container_cutout as cuts


class SideRunnerTests(unittest.TestCase):
    def test_revision_applies_to_all_current_units_only(self):
        historical=population.get_ai_version_7_options()[-1]
        self.assertEqual(historical['spring_root_y'],-7)
        self.assertNotIn('side_runner',historical)
        for source in population.get_current_options():
            p=drawing.get_ai_version_7_frame_parameters(**source)
            self.assertEqual(p['spring_root_y'],-5)
            self.assertEqual(p['side_runner']['thickness'],3)
            self.assertEqual(p['beam_windows'],[])
            self.assertLess(p['trials'][0]['spring_length'],10)

    def test_bad_offset_or_unretained_nut_wall_is_rejected(self):
        for change in [dict(offset_x=2),dict(end_length=9),dict(thickness=0),dict(clip_rotation_y=180)]:
            source=population.get_current_options()[-1]
            source['side_runner'].update(change)
            with self.subTest(change=change),self.assertRaises(ValueError):
                drawing.get_ai_version_7_frame_parameters(**source)

    def test_nut_primitive_does_not_inherit_part_transform_or_anchor(self):
        p=drawing.get_ai_version_7_frame_parameters(**population.get_current_options()[-1])
        p.update(zz='top',rot_x=47,rot_y=19,rot_z=33,hole=True)
        with patch.object(oobb,'append_full') as append:
            cuts.get_container_cutout_ai_version_7([0,0,0],{},**dict(p,v7_component='screw_beam'))
        nut=next(call.kwargs for call in append.call_args_list if call.kwargs['shape']=='oobb_nut')
        self.assertEqual(nut['zz'],'bottom')
        self.assertEqual(nut['rot'],[90,0,0])
        self.assertEqual(nut['pos'],[0,-7,6.5])
        self.assertEqual(nut['clearance'],'right')
        self.assertFalse(nut['overhang'])
        for key in ['rot_x','rot_y','rot_z']:self.assertNotIn(key,nut)

    def test_print_transform_preserves_both_receiver_axes_and_roofs(self):
        p=drawing.get_ai_version_7_frame_parameters(**population.get_current_options()[-1])
        for mount in p['frame_mounts']:
            for kind,axis in [('snap_beam',2.5),('screw_beam',6.5)]:
                t=np.array(drawing.v7_beam_to_frame(p,mount,kind))
                for y,z in [(0,6),(-p['rail_length'],218)]:
                    point=t@[-axis,y,-p['side_runner']['bed_x'],1]
                    np.testing.assert_allclose(point,[mount['x'],mount['hole_y'],z,1],atol=1e-12)
                roof=t@[-axis-8,-80,-p['side_runner']['bed_x'],1]
                self.assertAlmostEqual(roof[1],mount['hole_y']-8)

    def test_shared_divider_runner_centre_matches_both_beam_types(self):
        for source in population.get_current_options():
            p=drawing.get_ai_version_7_frame_parameters(**source)
            for mount in p['frame_mounts']:
                for kind,axis in [('snap_beam',2.5),('screw_beam',6.5)]:
                    t=np.array(drawing.v7_beam_to_frame(p,mount,kind))
                    r=p['side_runner']
                    roof=t@[-axis-8,-80,r['offset_x']-r['bed_x'],1]
                    if mount['shared_runner']:
                        self.assertAlmostEqual(roof[0],mount['divider_x'])
                        self.assertAlmostEqual(mount['x']-mount['divider_x'],1.5)
                    else:self.assertAlmostEqual(mount['x'],mount['divider_x'])

    def test_offset_holes_keep_reinforcement_on_the_divider(self):
        for source in population.get_current_options():
            p=drawing.get_ai_version_7_frame_parameters(**source)
            for pad in p['reinforcement_pads']:
                self.assertAlmostEqual(pad['pad_x'],pad['divider_x'])
                self.assertAlmostEqual(pad['pad_x']+pad['hole_offset_x'],pad['x'])
                self.assertEqual(pad['hole_offset_x'],1.5 if pad['shared_runner'] else 0)
                self.assertGreaterEqual(6-abs(pad['hole_offset_x'])-2.6,1.5)


if __name__=='__main__':unittest.main()
