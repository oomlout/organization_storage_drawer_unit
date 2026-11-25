import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from presentation import drawer_labels


class DrawerLabelsTest(unittest.TestCase):
    def test_changing_contents_preserves_location_artwork_on_both_faces(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / "label_assignments"
            config.mkdir()
            sources = root / "presentation"
            sources.mkdir()
            (sources / "example_contents.json").write_bytes(
                (drawer_labels.HERE / "example_contents.json").read_bytes()
            )
            frame = {"row": 1, "column": 1, "variant": "1x1"}

            def generate(name):
                folder = root / name
                folder.mkdir()
                with patch.object(drawer_labels, "HERE", sources):
                    return drawer_labels.generate(folder, folder, frame)

            old, first = generate("first")
            replacement = dict(id="hardware_nut_m3", title="M3 nut", detail="Hex", code="M3")
            (config / "1x1.json").write_text(json.dumps({"contents": {"F-X1-Y1": replacement}}))
            new, second = generate("second")
            self.assertTrue((root/"second"/"labels"/new[0]["location_png"]).is_file())
            self.assertEqual(list(root.rglob("*.zip")), [])
            self.assertEqual([row["location_qr"] for row in new], ["1X1-F-X1-Y1", "1X1-R-X1-Y1"])
            for row in old:
                self.assertEqual(
                    (first / row["location_png"]).read_bytes(), (second / row["location_png"]).read_bytes()
                )
            self.assertEqual(new[0]["content_qr"], "hardware_nut_m3")
            self.assertNotEqual(old[0]["content_png"], new[0]["content_png"])
            self.assertEqual(old[1], new[1])
