"""The development version can change without mutating either release."""
import unittest
from unittest.mock import patch

import working_oomp_populate as population
import working_scad as drawing
import working_scad_container_cutout as cutout


class VersionThreeSplitTests(unittest.TestCase):
    def test_population_and_parameters_are_independent(self):
        released = population.get_ai_version_2_options()
        development = population.get_ai_version_3_options()
        development[0]["row"] = 99
        self.assertEqual(released, population.get_ai_version_2_options())
        defaults = population.get_ai_version_3_defaults()
        defaults["container_clearance"] = 2
        container = released[0]["container"]
        with patch.object(population, "get_ai_version_3_defaults", return_value=defaults):
            self.assertEqual(drawing.get_ai_version_1_parameters(container=container)["container_clearance"], 1.5)
            self.assertEqual(drawing.get_ai_version_2_parameters(container=container)["container_clearance"], 1.5)
            self.assertEqual(drawing.get_ai_version_3_parameters(container=container)["container_clearance"], 2)

    def test_each_version_routes_to_its_own_cutout(self):
        with patch.object(cutout, "get_container_cutout_ai_version_1") as one, \
             patch.object(cutout, "get_container_cutout_ai_version_2") as two, \
             patch.object(cutout, "get_container_cutout_ai_version_3") as three:
            cutout.get_base([0, 0, 0], {}, style="ai_version_3")
            three.assert_called_once()
            two.assert_not_called()
            one.assert_not_called()

    def test_only_default_clearance_is_populated_without_taxonomy_variant(self):
        for version in [1, 2, 3, 4]:
            options = getattr(population, f"get_ai_version_{version}_options")()
            for option in options:
                if option["style"] == "basic":
                    continue
                self.assertEqual(option["container_clearance"], 1.5)
                self.assertNotIn("clearance", option.get("variant", ""))
                self.assertNotEqual(option["part_role"], "fit")
            container = options[0]["container"]
            p = getattr(drawing, f"get_ai_version_{version}_parameters")(
                container=container, container_clearance=2)
            self.assertEqual(p["container_clearance"], 2)


if __name__ == "__main__":
    unittest.main()
