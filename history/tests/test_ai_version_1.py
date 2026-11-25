"""Design guardrails and pipeline dispatch checks; mesh checks are in the validator."""
import copy
import unittest
from unittest.mock import patch

import oobb
import working_oomp_populate
import working_scad
import working_scad_container_cutout


CONTAINER = "packaging_takeaway_container_rectangle_100_ml_capacity_109_mm_width_86_mm_height_29_mm_depth_tamper_evident_systempak_209"
CONTAINER_550 = "packaging_takeaway_container_rectangle_550_ml_capacity_108_mm_width_86_mm_height_95_mm_depth_tamper_evident_systempak_214"


class AiVersionOneTests(unittest.TestCase):
    def parameters(self, **changes):
        return working_scad.get_ai_version_1_parameters(container=CONTAINER, **changes)

    def test_large_module_fits_bed_with_margin(self):
        values = self.parameters(column=4, row=12)
        self.assertAlmostEqual(values["width_total"], 360.2)
        self.assertAlmostEqual(values["height_total"], 354.6)
        self.assertAlmostEqual(values["print_height_total"], 395.6)
        with self.assertRaises(ValueError):
            self.parameters(column=5, row=12)

    def test_ear_footprint_and_removal_controls(self):
        bare = self.parameters(column=4, row=12, adhesion_ears=False, bed_margin=10)
        self.assertAlmostEqual(bare["print_height_total"], 354.6)
        for changes in [dict(column=4, row=12, bed_margin=10),
                        dict(ear_link_height=1), dict(ear_link_width=15),
                        dict(ear_diameter=60)]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.parameters(**changes)

    def test_catch_projection_and_supportable_ramp(self):
        values = self.parameters()
        self.assertEqual(values["catch_tab_height"], 6)
        self.assertEqual(values["catch_tab_ramp_depth"], 6)
        self.assertEqual(values["front_band"], 7.5)
        self.assertEqual(values["catch_tab_ramp_depth"] + values["catch_tab_depth"], 7.5)
        with self.assertRaises(ValueError):
            self.parameters(catch_tab_ramp_depth=3)
        with self.assertRaises(ValueError):
            self.parameters(catch_tab_ramp_depth=7.5)

    def test_clearance_is_total_and_can_be_changed(self):
        values = self.parameters(container_clearance=0.75)
        self.assertEqual(values["opening_width"], 86.75)
        self.assertEqual(values["opening_height"], 26.75)

    def test_lip_profile_preserves_shelf_and_allows_no_centre_rib(self):
        values = self.parameters()
        self.assertEqual(values["depth_lip"], 12)
        self.assertEqual(values["inset_lip"], 5.5)
        self.assertEqual(values["lip_body_width"], 76.5)
        self.assertEqual(values["lip_step_y"], -1.75)
        self.assertEqual(values["middle_rib_width"], 0)
        self.assertEqual(values["shelf_window_width"], 67.5)
        for changes in [dict(lip_shelf_thickness=1), dict(depth_lip=30),
                        dict(inset_lip=50), dict(lip_shelf_thickness=12),
                        dict(middle_rib_width=-1), dict(runner_width=6)]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.parameters(**changes)

    def test_invalid_geometry_is_rejected(self):
        for changes in [dict(row=0), dict(column=1.5), dict(roof_slope=0.8),
                        dict(runner_width=1), dict(middle_rib_width=100),
                        dict(front_band=100), dict(container_clearance=-1),
                        dict(catch_tab_depth=20), dict(thickness_wall=float("nan")),
                        dict(part_role="unknown"), dict(part_role="fit", test_depth=0)]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.parameters(**changes)

    def test_population_carries_trials_and_drawing_inputs(self):
        with patch.object(working_oomp_populate, "write_extras") as writer:
            working_oomp_populate.main(catalogue="historical")
        parts = writer.call_args.args[0]
        ai_parts = [p for p in parts if p.get("style") == "ai_version_1"]
        self.assertEqual(len(ai_parts), 11)
        ids = [working_oomp_populate.build_oomp_id(p) for p in parts]
        self.assertEqual(len(set(ids)), len(ids))
        generated = [p for p in parts if "oobb_details" in p]
        purchased = [p for p in parts if p.get("record_type") == "purchased_drawer_unit"]
        self.assertEqual(len(generated), 73)
        self.assertEqual(len(purchased), 15)
        for part in generated:
            self.assertEqual(part["taxonomy_1"], "oobb")
            self.assertEqual(part["taxonomy_2"], "organization")
            self.assertEqual(part["oobb_details"]["taxonomy_1"], "oobb")
        for part in purchased:
            self.assertEqual(part["taxonomy_1"], "organization")
            self.assertNotIn("oobb_details", part)
        for part in ai_parts:
            self.assertEqual(part["oobb_details"]["oobb_name"], "ai_version_1")
            self.assertEqual(part["container_clearance"], part["oobb_details"]["container_clearance"])
            self.assertTrue(callable(getattr(working_scad, "get_" + part["oobb_details"]["oobb_name"])))

    def test_printer_variants_are_maximum_grids_with_current_ears(self):
        with patch.object(working_oomp_populate, "write_extras") as writer:
            working_oomp_populate.main(catalogue="historical")
        parts = writer.call_args.args[0]
        expected = {"a1_mini_max": (1, 4, 92.3, 161.2),
                    "p1p_max": (2, 7, 181.6, 249.1)}
        for variant, (columns, rows, width, height) in expected.items():
            part = next(p for p in parts if p.get("variant") == variant and p["container"] == CONTAINER)
            with self.subTest(variant=variant):
                values = working_scad.get_ai_version_1_parameters(**part["oobb_details"])
                self.assertEqual((values["column"], values["row"]), (columns, rows))
                self.assertAlmostEqual(values["width_total"], width)
                self.assertAlmostEqual(values["print_height_total"], height)
                self.assertLessEqual(values["depth_total"], values["build_height"])
                for key in ["column", "row"]:
                    larger = copy.deepcopy(part["oobb_details"])
                    larger[key] += 1
                    with self.assertRaises(ValueError):
                        working_scad.get_ai_version_1_parameters(**larger)
                too_short = dict(part["oobb_details"], build_height=100)
                with self.assertRaises(ValueError):
                    working_scad.get_ai_version_1_parameters(**too_short)

    def test_550_lidless_dimensions_and_shared_lip_profile(self):
        values = working_scad.get_ai_version_1_parameters(container=CONTAINER_550)
        self.assertEqual([values[key] for key in
                          ["container_width", "container_height", "container_depth"]],
                         [86, 92, 108])
        self.assertEqual(values["opening_height"], 93.5)
        self.assertEqual(values["depth_total"], 109.5)
        original = self.parameters()
        for key in ["depth_lip", "inset_lip", "lip_cutout_radius", "lip_body_width",
                    "lip_shelf_thickness", "runner_width", "catch_tab_height",
                    "catch_tab_ramp_depth", "adhesion_ears"]:
            self.assertEqual(values[key], original[key])

    def test_550_population_and_printer_maximum_grids(self):
        with patch.object(working_oomp_populate, "write_extras") as writer:
            working_oomp_populate.main(catalogue="historical")
        parts = [p for p in writer.call_args.args[0] if p.get("container") == CONTAINER_550 and p.get("style") == "ai_version_1"]
        self.assertEqual(len(parts), 3)
        expected = {"frame": (1, 1, 92.3, 140.8),
                    "a1_mini_max": (1, 1, 92.3, 140.8),
                    "p1p_max": (2, 2, 181.6, 237.6)}
        for part in parts:
            variant = part.get("variant", "frame")
            with self.subTest(variant=variant):
                columns, rows, width, height = expected[variant]
                self.assertEqual(part["container"], part["oobb_details"]["container"])
                values = working_scad.get_ai_version_1_parameters(**part["oobb_details"])
                self.assertEqual((values["column"], values["row"]), (columns, rows))
                self.assertAlmostEqual(values["width_total"], width)
                self.assertAlmostEqual(values["print_height_total"], height)
                self.assertAlmostEqual(values["depth_total"], 109.5)
                if variant != "frame":
                    self.assertEqual(part["taxonomy_9"], variant)
                    self.assertLessEqual(values["depth_total"], values["build_height"])
                    for key in ["column", "row"]:
                        larger = dict(part["oobb_details"])
                        larger[key] += 1
                        with self.assertRaises(ValueError):
                            working_scad.get_ai_version_1_parameters(**larger)

    def test_taller_body_keeps_100_ml_support_height(self):
        for clearance in [0.75, 1.5, 2.25]:
            original = self.parameters(container_clearance=clearance)
            taller = working_scad.get_ai_version_1_parameters(
                container=CONTAINER_550, container_clearance=clearance)
            self.assertEqual(original["body_extension_height"], 0)
            self.assertEqual(taller["body_extension_height"], 66)
            self.assertEqual(taller["lip_support_channel_height"], original["opening_height"])
            self.assertEqual(taller["lip_support_end_y"] - taller["lip_step_y"],
                             original["opening_height"] - original["depth_lip"])
        with self.assertRaises(ValueError):
            self.parameters(lip_support_reference_height=10)

    def test_cutout_style_dispatch(self):
        with patch.object(working_scad_container_cutout, "get_container_cutout_ai_version_1") as ai, \
             patch.object(working_scad_container_cutout, "get_container_cutout_version_1") as basic:
            working_scad_container_cutout.get_base([0, 0, 0], {}, style="ai_version_1")
            ai.assert_called_once()
            basic.assert_not_called()
            working_scad_container_cutout.get_base([0, 0, 0], {}, style="basic")
            basic.assert_called_once()

    def test_offset_models_do_not_mutate_inputs(self):
        kwargs = dict(container=CONTAINER, column=2, row=2, pos=[15, 25, 0])
        original = copy.deepcopy(kwargs)
        thing = oobb.get_default_thing(type="test")
        working_scad.get_ai_version_1(thing, **kwargs)
        self.assertEqual(kwargs, original)
        self.assertGreater(len(thing["components"]), 0)
        # Catch positional forwarding regressions in the paired layout as well.
        thing = oobb.get_default_thing(type="test")
        working_scad.get_ai_version_1(thing, part_role="bank_layout", **kwargs)
        self.assertEqual(thing["ai_design"]["expected_bodies"], 2)


if __name__ == "__main__":
    unittest.main()

