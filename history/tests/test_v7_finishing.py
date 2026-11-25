"""Guard the finishing revision's mating depths, offset rim and rear pose."""
import unittest
import numpy as np
import trimesh
import working_oomp_populate as population
import working_scad as drawing


class FinishingTests(unittest.TestCase):
    def test_split_receiver_rejects_unbalanced_or_tight_guides(self):
        for change in [dict(beam_receiver_depth=2.5),dict(guide_depth=3.5),
                       dict(mating_clearance=0),dict(beam_guide_width=5.2),dict(beam_guide_height=-1)]:
            p=population.get_current_options()[-1];p['screw'].update(change)
            with self.subTest(change=change),self.assertRaises(ValueError):
                drawing.get_ai_version_7_frame_parameters(**p)

    def test_offset_cover_cannot_reuse_short_rim_height(self):
        p=population.get_current_options()[-1];p['front_plug']['cover_height']=8
        with self.assertRaises(ValueError):drawing.get_ai_version_7_frame_parameters(**p)

    def test_rear_adapter_keeps_its_trimmed_edge_on_same_side(self):
        p=drawing.get_ai_version_7_frame_parameters(**population.get_current_options()[-1])
        for rear in [False,True]:
            matrix=trimesh.transformations.euler_matrix(*np.radians(drawing.v7_external_part_rotation(p,'screw_beam',rear)))
            point=matrix@[p['screw']['flange_offset_x'],0,0,1]
            self.assertAlmostEqual(point[0],p['screw']['flange_offset_x'])
            self.assertAlmostEqual(matrix[2,2],-1 if rear else 1)

    def test_stop_height_must_remain_positive(self):
        p=population.get_current_options()[-1];p['side_runner']['stop_height']=0
        with self.assertRaises(ValueError):drawing.get_ai_version_7_frame_parameters(**p)


if __name__=='__main__':unittest.main()
