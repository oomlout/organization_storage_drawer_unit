"""Dimensions, independent part routing and hardware guardrails for the split."""
import unittest
from unittest.mock import patch

import oobb
import working_oomp_populate as population
import working_scad as drawing
import working_scad_container_cutout as cutout


class SplitFrameVersionThreeTests(unittest.TestCase):
    def setUp(self):
        self.option = population.get_ai_version_3_options()[0]

    def parameters(self, **changes):
        return drawing.get_ai_version_3_parameters(**dict(self.option, **changes))

    def test_halves_equal_except_for_three_mm_interlock(self):
        front = self.parameters(assembly_half="front")
        back = self.parameters(assembly_half="back")
        self.assertEqual(front["body_depth"], back["body_depth"])
        self.assertEqual(front["depth_total"] - back["depth_total"], 3)
        self.assertEqual(front["body_depth"] + back["body_depth"], 110.5)
        self.assertEqual(back["catch_tab_height"], 0)
        self.assertEqual(front["catch_tab_height"], 6)
        self.assertEqual(front["screw_head_seat_offset"] + front["nut_seat_offset"] + oobb.gv("nut_depth_m3", "3dpr"), 16)

    def test_taper_preserves_joint_and_has_supportable_growth(self):
        for half in ["front", "back"]:
            p = self.parameters(assembly_half=half)
            self.assertEqual(p["running_shelf_thickness"], 4)
            self.assertEqual(p["lip_shelf_thickness"], 10)
            self.assertEqual(p["hardware_boss_band"], 12)
            self.assertAlmostEqual(p["boss_taper_end"] - p["boss_taper_start"], 7.2)
            self.assertGreater(p["boss_taper_start"], p["relief_start_depth"])
            self.assertEqual(p["relief_start_depth"], 7.5 if half == "front" else 6)
        for changes in [dict(hardware_boss_slope=0.5), dict(hardware_boss_band=8),
                        dict(running_shelf_thickness=2), dict(joint_test_depth=24)]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.parameters(**changes)

    def test_every_frame_has_views_in_one_record(self):
        options = population.get_ai_version_3_options()
        self.assertEqual(len(options), 12)
        for part in options:
            self.assertEqual(part["assembly_half"], "print_layout")
            if part["part_role"] != "frame":
                continue
            for half in ["front", "back"]:
                p = drawing.get_ai_version_3_parameters(**dict(part, assembly_half=half))
                self.assertLessEqual(p["print_height_total"] + 2 * p["bed_margin"], p["bed_height"])
                self.assertLessEqual(p["width_total"] + 2 * p["bed_margin"], p["bed_width"])

    def test_print_layout_separates_halves_and_reports_bed_limit(self):
        p = self.parameters()
        summary = drawing.get_ai_version_3_summary(p)
        self.assertEqual(summary["expected_bodies"], 2)
        self.assertTrue(summary["print_layout_fits_single_bed"])
        maximum = next(o for o in population.get_ai_version_3_options() if o.get("variant") == "p1p_max")
        p = drawing.get_ai_version_3_parameters(**maximum)
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
                    cutout.get_container_cutout_ai_version_3([0, 0, 0], {}, **dict(p, column_index=column, row_index=0))
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
                        cutout.get_container_cutout_ai_version_3(
                            [column * p["pitch_x"], row * p["pitch_y"], 0], {},
                            **dict(p, column_index=column, row_index=row))
            joints = [c.kwargs for c in append.call_args_list if c.kwargs.get("joint_feature") == "corner_interlock"]
            self.assertEqual(len(joints), 6)
            self.assertEqual(len({tuple(j["pos"][:2]) for j in joints}), 6)
            for joint in joints:
                self.assertEqual(joint["type"], "positive" if half == "front" else "negative")
                self.assertAlmostEqual(joint["points"][0][0], 1.4 if half == "front" else 1.65)

    def test_lower_rails_removed_without_changing_screw_count(self):
        for rows, expected in [(2, 4), (7, 9)]:
            p = self.parameters(row=rows, column=2, assembly_half="front")
            summary = drawing.get_ai_version_3_summary(p)
            self.assertEqual(summary["connections_per_vertical_boundary"], expected)
            self.assertEqual(summary["screw_count"], 3 * rows)
            self.assertEqual(summary["corner_interlock_count"], 6)
        restored = self.parameters(row=7, remove_internal_lower_supports=False)
        self.assertEqual(drawing.get_ai_version_3_summary(restored)["connections_per_vertical_boundary"], 15)
        self.assertFalse(self.parameters()["internal_lower_supports_removed"])


if __name__ == "__main__":
    unittest.main()
