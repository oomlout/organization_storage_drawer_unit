"""Current catalogue boundaries and generation entry points."""
from contextlib import chdir
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import yaml
import working
import working_oomp
import working_oomp_populate as population
import working_scad as cad


class V8CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.parts = {p["variant"]: p for p in population.get_current_options()}

    def test_distinct_current_records(self):
        self.assertTrue({"1x1", "2x2", "2x7", "joiners"} <= self.parts.keys())
        self.assertEqual(len({population.record_id(p) for p in self.parts.values()}), len(self.parts))
        self.assertTrue(all(p["version"] == 8 for p in self.parts.values()))
        with self.assertRaises(ValueError):
            population.selected_options("unit_1_wide_2_tall")

    def test_frame_grids_and_quantities(self):
        for size, counts in {"1x1": (2,2,2), "2x2": (8,6,3), "2x7": (28,17,4)}.items():
            with self.subTest(size=size):
                p = cad.frame_parameters(**self.parts[size])
                self.assertEqual((p["frame"]["drawer_count"], p["bom"]["snap_beam"], p["bom"]["screw_beam"]), counts)
                self.assertNotIn("joiners", p)
                self.assertNotIn("countersink_setback", p.get("corner_fixing", {}))
                self.assertAlmostEqual(p["frame"]["assembled_depth"], 209)
                self.assertEqual(sum(p["cap_quantities"].values()), 2 * counts[1])
                self.assertTrue(all(batch["count"] > 0 for batch in p["print_batches"].values()))

    def test_one_opening_has_four_nested_pads(self):
        p = cad.frame_parameters(**self.parts["1x1"])
        slots = p["reinforcement_layout"]
        self.assertEqual(len(slots), 4)
        self.assertEqual(len({pad["layout_x"] for pad in slots}), 4)
        self.assertEqual({pad["layout_y"] for pad in slots}, {slots[0]["layout_y"]})
        self.assertEqual(p["cap_quantities"], {"front_plug": 4, "front_plug_square": 0})

    def test_new_tray_family_reaches_the_catalogue_and_manual(self):
        from presentation.catalogue import write_index, tray_name
        tray = dict(population.TRAYS["systempak_209_100_ml"], name="Test pot", capacity_ml=150,
                    dimensions_mm={"across": 95, "height": 31, "depth": 110},
                    layouts={"test-1x3": {"grid": (1, 3), "mounts": "top_braces"}})
        with patch.dict(population.TRAYS, {"test_150_ml": tray}):
            record, = population.selected_options("test-1x3")
            self.assertEqual(record["drawer_count"], 6)
            self.assertEqual(record["taxonomy_5"], "test_150_ml")
            self.assertNotIn("corner_fixing", record)
            self.assertIn("150 ml", tray_name(record))
            with TemporaryDirectory() as tmp:
                write_index(Path(tmp), [record])
                index = (Path(tmp) / "README.md").read_text(encoding="utf-8")
                self.assertIn(population.record_id(record) + "/presentation.jpg", index)
                self.assertIn("Test pot", index)

    def test_joiner_is_an_independent_accessory(self):
        accessory = self.parts["joiners"]
        self.assertEqual(accessory["part_role"], "accessory")
        self.assertTrue({"1x1", "2x2"} <= set(accessory["compatible_frames"]))
        self.assertEqual([p["variant"] for p in population.selected_options("joiners")], [*accessory["compatible_frames"], "joiners"])
        self.assertEqual([p["variant"] for p in population.selected_options("2x7")], ["2x7"])
        self.assertNotIn("corner_fixing", self.parts["2x7"])
        host = self.parts[accessory["reference_frame"]]
        p = cad.frame_parameters(**dict(host, draw_joiners=True, corner_fixing=accessory["corner_fixing"]))
        self.assertEqual(sorted(len(piece["holes"]) for piece in p["joiners"]), [2,4])
        self.assertEqual(p["corner_fixing"]["screw_length"], 25)

    def test_raising_the_joiner_keeps_the_screw_and_nut_seats(self):
        accessory = self.parts["joiners"]
        host = self.parts["2x2"]
        interface = cad.frame_parameters(**host)["corner_fixing"]
        settings = dict(accessory["corner_fixing"], front_roof_thickness=3.5)
        p = cad.frame_parameters(**dict(host, draw_joiners=True, corner_fixing=settings))
        j = p["corner_fixing"]
        height = p["joiners"][0]["size"][2]
        self.assertAlmostEqual(height, j["cap_projection"] + j["cap_axial_clearance"] + 3.5)
        self.assertAlmostEqual(j["screw_reference_recess"] - height,
                               interface["screw_reference_recess"] - interface["joining_plate_thickness"])
        self.assertEqual(j["backer_depth"], interface["backer_depth"])
        with self.assertRaisesRegex(ValueError, "roof"):
            cad.frame_parameters(**dict(host, draw_joiners=True,
                corner_fixing=dict(settings, front_roof_thickness=2)))

    def test_make_all_order_and_stale_files(self):
        with TemporaryDirectory() as tmp, chdir(tmp):
            stale = Path("parts_source/retired_v7/working.yaml")
            stale.parent.mkdir(parents=True)
            stale.write_text("version: 7")
            retired = Path("parts/retired_v7/working.yaml")
            retired.parent.mkdir(parents=True)
            retired.write_text("version: 7")
            with patch("v8_manufacturing.frame_outputs") as draw:
                working.run(part="1x1", output_dir=tmp, generate_stl=False)
            self.assertEqual(draw.call_count, 1)
            self.assertEqual(draw.call_args.args[1]["variant"], "1x1")
            self.assertEqual(stale.read_text(), retired.read_text())
            self.assertEqual(list(retired.parent.iterdir()), [retired])
            canonical = population.record_id(self.parts["1x1"])
            self.assertEqual(sorted(p.name for p in Path("parts").iterdir()), sorted([canonical, "retired_v7"]))
            path = Path("parts_source") / canonical / "working.yaml"
            source = yaml.safe_load(path.read_text())
            source["oobb_details"]["version"] = 7
            path.write_text(yaml.safe_dump(source))
            with self.assertRaisesRegex(ValueError, "Stale part definition"):
                working_oomp.main(part="1x1")

    def test_default_output_follows_the_project_when_launched_elsewhere(self):
        with TemporaryDirectory() as tmp, chdir(tmp), patch.object(population, "main") as populate:
            populate.side_effect = lambda **kwargs: self.assertEqual(Path.cwd(), Path(working.__file__).resolve().parent)
            working.run(part="1x1", run_oomp=False, run_scad=False)
            populate.assert_called_once_with(part="1x1")
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_archive_is_protected(self):
        with self.assertRaisesRegex(ValueError, "archive"):
            working.run(output_dir=Path(working.__file__).parent / "history" / "parts")


if __name__ == "__main__":
    unittest.main()
