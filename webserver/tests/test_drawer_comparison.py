import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from history import working_oomp_populate_comparison as costs
from webserver.services.drawer_comparison import comparison_row, select_rows
from webserver.app import create_app
import yaml


class DrawerComparisonTests(unittest.TestCase):
    def record(self, name, price, count=20, sample=False, weight=None):
        return {
            "id": name,
            "part_dir": ".",
            "data": {
                "record_type": "purchased_drawer_unit",
                "product_name": name,
                "number_of_drawers": count,
                "drawer_capacity_ml": 225,
                "price_gbp": price,
                "weight_kg": weight,
                "comparison_sample": sample,
            },
        }

    def test_numeric_sort_and_unknown_values_last_in_both_directions(self):
        records = [self.record("ten", 10), self.record("two", 2), self.record("missing", None)]
        rows, _, _, _ = select_rows(records, {"sort": "price"})
        self.assertEqual([r["name"] for r in rows], ["two", "ten", "missing"])
        rows, _, _, _ = select_rows(records, {"sort": "price", "direction": "desc"})
        self.assertEqual([r["name"] for r in rows], ["ten", "two", "missing"])

    def test_capacity_normalization_and_sample_filter(self):
        records = [self.record("cabinet", 20), self.record("sample", 1, sample=True)]
        rows, total, _, _ = select_rows(records, {"capacity": "small"})
        self.assertEqual(total, 2)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["total_litres"], 4.5)
        self.assertAlmostEqual(rows[0]["per_litre"], 20 / 4.5)
        self.assertEqual(len(select_rows(records, {"samples": "1"})[0]), 2)
        self.assertEqual(len(select_rows(records, {"capacity": "550"})[0]), 0)

    def test_printed_material_cost_includes_pots_vat_and_lidless_mass(self):
        part = {
            "container": "systempak_209",
            "column": 2,
            "row": 2,
            "style": "basic",
            "taxonomy_1": "oobb",
            "oobb_details": {"column": 2, "row": 2},
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "drawer_comparison").mkdir()
            (root / "drawer_comparison/cad_measurements.json").write_text(json.dumps({"test": {
                "fingerprint": "fresh", "volume_mm3": 100000, "finished_envelope_mm": [180, 60, 111],
            }}))
            with patch.object(costs, "ROOT", root), patch.object(costs, "build_oomp_id", return_value="test"), patch.object(costs, "geometry_fingerprint", return_value="fresh"):
                costs.enrich([part])
            self.assertEqual(part["filament_mass_g"], 124)
            self.assertAlmostEqual(part["filament_cost_gbp"], 1.24)
            self.assertAlmostEqual(part["price_gbp"], round(1.24 + 4 * 60.95 * 1.2 / 500, 4))
            self.assertAlmostEqual(part["weight_kg"], 0.156)
            self.assertEqual(part["drawer_count"], 4)

    def test_stale_measurements_do_not_publish_a_price(self):
        part = {"container": "systempak_209", "column": 1, "row": 1, "style": "basic", "oobb_details": {"row": 1}}
        with tempfile.TemporaryDirectory() as tmp, patch.object(costs, "ROOT", Path(tmp)), patch.object(costs, "geometry_fingerprint", return_value="stale"):
            costs.enrich([part])
        self.assertNotIn("price_gbp", part)
        self.assertIn("refresh", part["comparison_measurement_status"])

    def test_separate_half_has_no_pots_or_complete_unit_cost_ratios(self):
        part = {"container": "systempak_209", "column": 1, "row": 1,
                "style": "ai_version_2", "assembly_half": "front", "oobb_details": {}}
        part["oobb_details"] = {"column": 1, "row": 1}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "drawer_comparison").mkdir()
            (root / "drawer_comparison/cad_measurements.json").write_text(json.dumps({"test": {
                "fingerprint": "fresh", "volume_mm3": 100000, "finished_envelope_mm": [98.5, 38.5, 58.25]}}))
            with patch.object(costs, "ROOT", root), patch.object(costs, "build_oomp_id", return_value="test"), patch.object(costs, "geometry_fingerprint", return_value="fresh"):
                costs.enrich([part])
        self.assertTrue(part["comparison_sample"])
        self.assertEqual(part["pot_quantity"], 0)
        self.assertEqual(part["pots_cost_gbp"], 0)
        self.assertEqual(part["price_gbp"], 1.24)
        self.assertEqual(part["weight_kg"], 0.124)
        row = comparison_row({"id": "test", "part_dir": ".", "data": part})
        self.assertIsNone(row["per_drawer"])
        self.assertIsNone(row["per_litre"])

    def test_connector_trial_is_hidden_petg_sample_without_pots(self):
        part = {"container":"systempak_209", "column":1, "row":1,
                "style":"ai_version_5", "part_role":"connector_test",
                "variant":"snap_twin", "connector_design":"snap_twin",
                "oobb_details":{"connector_design":"snap_twin"}}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"drawer_comparison").mkdir()
            (root/"drawer_comparison/cad_measurements.json").write_text(json.dumps({"test":{
                "fingerprint":"fresh", "volume_mm3":10000, "finished_envelope_mm":[40,44,10]}}),encoding="utf-8")
            with patch.object(costs,"ROOT",root), patch.object(costs,"build_oomp_id",return_value="test"), patch.object(costs,"geometry_fingerprint",return_value="fresh"):
                costs.enrich([part])
        self.assertTrue(part["comparison_sample"])
        self.assertEqual(part["pot_quantity"],0)
        self.assertEqual(part["pots_cost_gbp"],0)
        self.assertEqual(part["filament_mass_g"],12.7)
        self.assertEqual(part["weight_kg"],0.0127)
        self.assertIn("PETG",part["filament_mass_basis"])
        row=comparison_row({"id":"test","part_dir":".","data":part})
        self.assertIsNone(row["per_drawer"])
        self.assertIsNone(row["total_litres"])

    def test_tiled_frame_is_visible_petg_unit_with_pots(self):
        part = {"container":"systempak_209","column":3,"row":9,
                "style":"ai_version_5","part_role":"frame","variant":"tiled_362_by_300",
                "connector_design":"tiled_hybrid","oobb_details":{"connector_design":"tiled_hybrid"}}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"drawer_comparison").mkdir()
            (root/"drawer_comparison/cad_measurements.json").write_text(json.dumps({"test":{
                "fingerprint":"fresh","volume_mm3":100000,"finished_envelope_mm":[362,300,110.5]}}))
            with patch.object(costs,"ROOT",root), patch.object(costs,"build_oomp_id",return_value="test"), patch.object(costs,"geometry_fingerprint",return_value="fresh"):
                costs.enrich([part])
        self.assertFalse(part["comparison_sample"])
        self.assertEqual(part["pot_quantity"],27)
        self.assertEqual(part["drawer_count"],27)
        self.assertEqual(part["filament_mass_g"],127)
        self.assertAlmostEqual(part["weight_kg"],0.343)
        self.assertGreater(part["pots_cost_gbp"],0)
        self.assertIsNotNone(part["cost_per_drawer_gbp"])
        self.assertIn("excluded",part["hardware_cost_basis"])

    def test_double_sided_frame_counts_both_banks(self):
        part = {"container":"systempak_209","column":2,"row":7,"drawer_sides":2,
                "style":"ai_version_6","part_role":"frame","variant":"double_sided_plywood_250_max",
                "connector_design":"double_sided_snap","oobb_details":{"connector_design":"double_sided_snap"}}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"drawer_comparison").mkdir()
            (root/"drawer_comparison/cad_measurements.json").write_text(json.dumps({"test":{
                "fingerprint":"fresh","volume_mm3":100000,"finished_envelope_mm":[197.8,220.3,224]}}))
            with patch.object(costs,"ROOT",root), patch.object(costs,"build_oomp_id",return_value="test"), patch.object(costs,"geometry_fingerprint",return_value="fresh"):
                costs.enrich([part])
        self.assertFalse(part["comparison_sample"])
        self.assertEqual(part["drawer_count"],28)
        self.assertEqual(part["pot_quantity"],28)
        self.assertAlmostEqual(part["weight_kg"],.351)
        self.assertEqual(part["filament_mass_g"],127)
        self.assertEqual(part["hardware_cost_basis"],"No assembly hardware")

    def test_current_frame_card_without_price_research(self):
        with tempfile.TemporaryDirectory() as tmp:
            parts = Path(tmp)
            frame = parts / "frame"
            frame.mkdir()
            (frame / "working.yaml").write_text(yaml.safe_dump({
                "record_type": "printed_drawer_unit", "product_name": "V8 test frame",
                "drawer_capacity_ml": 100, "drawer_count": 2,
            }))
            client = create_app({"TESTING": True, "PARTS_DIR": parts}).test_client()
            response = client.get("/drawers")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"V8 test frame", response.data)
            self.assertIn(b"Cost estimates are unavailable", response.data)

    def test_cards_table_filters_and_sort_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, price in [("Cabinet two", 2), ("Cabinet ten", 10)]:
                folder = root / name
                folder.mkdir()
                data = self.record(name, price)["data"]
                data.update({"for_sale_url": "https://example.com/item", "seller": "Example", "width_mm": 100, "height_mm": 200, "depth_mm": 150})
                (folder / "working.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
            client = create_app({"TESTING": True, "PARTS_DIR": root}).test_client()
            response = client.get("/drawers")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"2 of 2 units", response.data)
            response = client.get("/compare?kind=Purchased&sort=price&direction=desc")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'aria-sort="descending"', response.data)
            self.assertIn(b"kind=Purchased&amp;sort=price&amp;direction=asc", response.data)
            self.assertLess(response.data.find(b"Cabinet ten"), response.data.find(b"Cabinet two"))
            response = client.get("/compare?kind=Printed")
            self.assertIn(b"No units match", response.data)
            self.assertEqual(client.get("/").location, "/drawers")
