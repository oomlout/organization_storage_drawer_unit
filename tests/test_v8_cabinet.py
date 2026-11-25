from collections import Counter
from copy import deepcopy
import unittest

from v8_cabinet import plan
from working_oomp_populate import CABINET, selected_options


class CabinetTest(unittest.TestCase):
    def test_corner_hardware_and_sheet_dimensions(self):
        host, cabinet = selected_options(CABINET)
        self.assertEqual(host["variant"], "2x7")
        _, params, _, _, pieces, units = plan(cabinet, host)
        self.assertEqual(len(set(units)), 9)
        self.assertAlmostEqual(params["cap_w"] - params["inside_w"], 24)
        self.assertAlmostEqual(params["cap_w"], 617.4)
        self.assertEqual(cabinet["cabinet"]["side_gap_mm"], 0)
        self.assertAlmostEqual(params["inside_h"], 665.5)
        for right in (False, True):
            for bottom in (False, True):
                joint = [
                    p
                    for p in pieces
                    if p.name in ("dowel", "wood_30")
                    and (p.matrix[0, 3] > 0) == right
                    and (p.matrix[1, 3] > 0) == bottom
                ]
                self.assertEqual(Counter(p.name for p in joint), {"dowel": 3, "wood_30": 2})
                self.assertEqual(sorted(p.matrix[2, 3] for p in joint), params["stations"])
        counts = Counter(piece.name for piece in pieces)
        self.assertEqual({k: counts[k] for k in ("beam_screw","beam_nut","plywood_joint","wood_16")},
                         {"beam_screw":72, "beam_nut":72, "plywood_joint":8, "wood_16":16})
        self.assertEqual([counts[k] for k in ("edge_across","plywood_double","tee4")], [8,8,8])
        for screw in (piece for piece in pieces if piece.name == "wood_16"):
            self.assertAlmostEqual(abs(screw.matrix[0,3])-params["inside_w"]/2, 6)
        self.assertEqual(params["tie_t"],3)
        self.assertEqual(len(params["retainer_y"]),4)
        # Each side gets a single contact at each end and a shared two-beam contact at each tier seam.
        outside = params["inside_w"]/2 + params["t"]
        for plate in (piece for piece in pieces if piece.name in ("plywood_joint","plywood_double")):
            edge = plate.matrix[0,3] + plate.matrix[0,0]*(9.6+params["t"])
            self.assertAlmostEqual(abs(edge),outside)
        proud = deepcopy(cabinet)
        proud["cabinet"]["cap_overhang_mm"] = 12
        self.assertAlmostEqual(plan(proud, host)[1]["cap_w"], params["cap_w"] + 24)
