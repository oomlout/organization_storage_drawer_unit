"""Protect the user-selected 27 key and 28 snap against accidental fit drift."""
import unittest

import working_oomp_populate as population
import working_scad as drawing


class SelectedConnectorTests(unittest.TestCase):
    def test_selected_profiles_match_numbered_references(self):
        options = population.get_ai_version_5_options()
        key = next(o for o in options if o["variant"] == "tight_key_27")
        snap = next(o for o in options if o["variant"] == "snap_recessed_twin")
        trial = next(t for t in population.get_ai_version_5_heavy_latch_trials()
                     if t["sample_number"] == 28)
        snap = {**snap, **trial}
        for style, reference in [("key", key), ("snap", snap)]:
            selected = population.get_ai_version_5_selected_connector(style)
            for name, value in selected.items():
                self.assertEqual(value, reference[name], (style, name))
            actual = drawing.get_ai_version_5_parameters(**selected)
            expected = drawing.get_ai_version_5_parameters(**reference)
            for name, value in actual.items():
                self.assertEqual(value, expected[name], (style, name))

    def test_approved_fit_values_are_locked(self):
        snap = drawing.get_ai_version_5_parameters(
            **population.get_ai_version_5_selected_connector())
        for name, value in {
            "sample_number": 28, "arm_thickness": 1.8,
            "connector_clearance": 0.25, "catch_end_clearance": 0.2,
            "snap_arm_outer": 3.4, "snap_arm_height": 10.0,
            "root_distance": 0.5, "hook_projection": 1.2,
            "hook_ramp_length": 1.5, "recessed_shoulder_depth": 6.0,
        }.items():
            self.assertEqual(snap[name], value, name)
        key = drawing.get_ai_version_5_parameters(
            **population.get_ai_version_5_selected_connector("key"))
        for name, value in {
            "sample_number": 27, "key_arm_thickness": 1.4,
            "key_half_width": 2.45, "key_height": 7.0,
            "key_tongue_half_width": 4.375, "key_latch_clearance": 0.1,
            "connector_clearance": 0.4, "through_clearance": 0.25,
            "through_height_clearance": 0.25, "key_head_length": 5.5,
            "key_shoulder_x": 4.475,
        }.items():
            self.assertAlmostEqual(key[name], value, msg=name)

    def test_main_units_use_28_with_printable_bevel(self):
        for option in population.get_ai_version_5_tiled_options():
            self.assertEqual(option["main_connector_sample"], 28)
            self.assertEqual(option["separate_key_sample"], 27)
            self.assertEqual(option["snap_profile"],
                             population.get_ai_version_5_selected_connector())
            self.assertEqual(option["snap_clearance"], 0.25)
            self.assertEqual(option["snap_tip_floor"], 6.0)
            self.assertEqual(option["snap_ledge_land"], 0.5)
