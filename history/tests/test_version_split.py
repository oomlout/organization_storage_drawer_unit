"""Original version 1/2 routing and parameter independence."""
import unittest
from unittest.mock import patch

import working_oomp_populate as population
import working_scad as drawing
import working_scad_container_cutout as cutout


class VersionSplitTests(unittest.TestCase):
    def test_independent_population_and_parameters(self):
        original = population.get_ai_version_1_options()
        changed = population.get_ai_version_2_options()
        changed[0]["row"] = 99
        self.assertEqual(original, population.get_ai_version_1_options())
        defaults = population.get_ai_version_2_defaults()
        defaults["container_clearance"] = 2
        with patch.object(population, "get_ai_version_2_defaults", return_value=defaults):
            container = original[0]["container"]
            self.assertEqual(drawing.get_ai_version_1_parameters(container=container)["container_clearance"], 1.5)
            self.assertEqual(drawing.get_ai_version_2_parameters(container=container)["container_clearance"], 2)

    def test_independent_cutout_dispatch(self):
        with patch.object(cutout, "get_container_cutout_ai_version_1") as one, \
             patch.object(cutout, "get_container_cutout_ai_version_2") as two:
            cutout.get_base([0, 0, 0], {}, style="ai_version_1")
            one.assert_called_once()
            two.assert_not_called()
            cutout.get_base([0, 0, 0], {}, style="ai_version_2")
            two.assert_called_once()
            one.assert_called_once()

    def test_released_550_extra_height_per_row(self):
        for option in population.get_ai_version_1_options():
            if "550_ml" not in option["container"]:
                continue
            self.assertEqual(option["opening_height_extra"], 1.5)
            values = drawing.get_ai_version_1_parameters(**option)
            self.assertEqual(values["opening_height"], 95)
            self.assertEqual(values["body_extension_height"], 67.5)
            old = drawing.get_ai_version_1_parameters(**dict(option, opening_height_extra=0))
            self.assertAlmostEqual(values["height_total"] - old["height_total"], 1.5 * option["row"])


if __name__ == "__main__":
    unittest.main()
