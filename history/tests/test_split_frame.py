"""Dimensions, independent part routing and hardware guardrails for the split."""
import unittest
from unittest.mock import patch

import oobb
import working_oomp_populate as population
import working_scad as drawing
import working_scad_container_cutout as cutout


class SplitFrameTests(unittest.TestCase):
    def setUp(self):
        self.option = population.get_ai_version_2_options()[0]

    def parameters(self, **changes):
        return drawing.get_ai_version_2_parameters(**dict(self.option, **changes))

    def test_halves_equal_except_for_three_mm_interlock(self):
        front = self.parameters(assembly_half="front")
        back = self.parameters(assembly_half="back")
        self.assertEqual(front["body_depth"], back["body_depth"])
        self.assertEqual(front["depth_total"] - back["depth_total"], 3)
        self.assertEqual(front["body_depth"] + back["body_depth"], 110.5)
        self.assertEqual(back["catch_tab_height"], 0)
        self.assertEqual(front["catch_tab_height"], 6)
        self.assertEqual(front["screw_head_seat_offset"] + front["nut_seat_offset"] + oobb.gv("nut_depth_m3", "3dpr"), 16)

    def test_every_frame_has_views_in_one_record(self):
        options = population.get_ai_version_2_options()
        self.assertEqual(len(options), 12)
        for part in options:
            self.assertEqual(part["assembly_half"], "print_layout")
            if part["part_role"] != "frame":
                continue
            for half in ["front", "back"]:
                p = drawing.get_ai_version_2_parameters(**dict(part, assembly_half=half))
                self.assertLessEqual(p["print_height_total"] + 2 * p["bed_margin"], p["bed_height"])
                self.assertLessEqual(p["width_total"] + 2 * p["bed_margin"], p["bed_width"])

    def test_print_layout_separates_halves_and_reports_bed_limit(self):
        p = self.parameters()
        summary = drawing.get_ai_version_2_summary(p)
        self.assertEqual(summary["expected_bodies"], 2)
        self.assertTrue(summary["print_layout_fits_single_bed"])
        maximum = next(o for o in population.get_ai_version_2_options() if o.get("variant") == "p1p_max")
        p = drawing.get_ai_version_2_parameters(**maximum)
        self.assertFalse(p["print_layout_fits_single_bed"])
        axis = p["print_layout_axis"]
        individual_size = [p["width_total"], p["print_height_total"]][axis]
        self.assertAlmostEqual(p["print_layout_pitch"] - individual_size, 8)

    def test_reject_thin_hardware_walls_and_bad_lengths(self):
        for changes in [dict(drawer_border_edge=2.4), dict(lip_shelf_thickness=3),
                        dict(screw_length=10), dict(interlock_width=4),
                        dict(interlock_clearance=2), dict(joint_test_depth=12),
                        dict(corner_interlock_diameter=6),
                        dict(assembly_half="left")]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.parameters(**changes)

    def test_oobb_hardware_clearance_and_shared_divider_count(self):
        for half in ["front", "back"]:
            p = self.parameters(assembly_half=half, column=2, row=1)
            with patch.object(cutout.oobb, "append_full") as append:
                for column in range(2):
                    cutout.get_container_cutout_ai_version_2([0, 0, 0], {}, **dict(p, column_index=column, row_index=0))
            screws = [c.kwargs for c in append.call_args_list if c.kwargs.get("shape") == "oobb_screw_socket_cap"]
            self.assertEqual(len(screws), 3)
            for screw in screws:
                self.assertEqual(screw["depth"], 16)
                self.assertEqual(screw["radius_name"], "m3")
                self.assertTrue(screw["top_clearance"])
                self.assertTrue(screw["bottom_clearance"])
                self.assertTrue(screw["include_nut"])
                self.assertEqual(screw["clearance"], ["top", "bottom"])

    def test_corner_interlocks_cover_unique_grid_junctions(self):
        for half in ["front", "back"]:
            p = self.parameters(assembly_half=half, column=2, row=2)
            with patch.object(cutout.oobb, "append_full") as append:
                for row in range(2):
                    for column in range(2):
                        cutout.get_container_cutout_ai_version_2(
                            [column * p["pitch_x"], row * p["pitch_y"], 0], {},
                            **dict(p, column_index=column, row_index=row))
            joints = [c.kwargs for c in append.call_args_list if c.kwargs.get("joint_feature") == "corner_interlock"]
            self.assertEqual(len(joints), 9)
            self.assertEqual(len({tuple(j["pos"][:2]) for j in joints}), 9)
            for joint in joints:
                self.assertEqual(joint["type"], "positive" if half == "front" else "negative")
                self.assertAlmostEqual(joint["points"][0][0], 1.4 if half == "front" else 1.65)


if __name__ == "__main__":
    unittest.main()
