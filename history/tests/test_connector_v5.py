"""Guard the connector-only scope and meaningful mechanical constraints."""
import unittest
import working_oomp_populate as population
import working_scad as drawing


class ConnectorTests(unittest.TestCase):
    def parameters(self, **changes):
        return drawing.get_ai_version_5_parameters(**dict(population.get_ai_version_5_options()[0],**changes))

    def test_only_test_records_and_default_clearance(self):
        options=[o for o in population.get_ai_version_5_options() if o["part_role"]=="connector_test"]
        self.assertEqual(len(options),12)
        self.assertEqual({o["part_role"] for o in options},{"connector_test"})
        self.assertTrue(all("clearance" not in o["variant"] for o in options))
        self.assertTrue(all(o["test_material"]=="PETG" for o in options))
        self.assertEqual(len({o["connector_design"] for o in options}),8)
        self.assertAlmostEqual(self.parameters(connector_clearance=0.3)["insertion_deflection"],0.35)

    def test_same_scale_as_current_rail_and_plate(self):
        existing=population.get_ai_version_4_defaults()
        p=self.parameters()
        for key in ["rail_width","rail_height","plate_thickness"]:
            self.assertEqual(p[key],existing[key])
        self.assertEqual(p["guide_depth"],existing["modular_key_depth"])

    def test_rejects_nonlocking_or_blocked_latches(self):
        for change in [dict(connector_clearance=0.7),dict(hook_projection=0.1),
                       dict(single_arm_thickness=2.5),dict(test_rail_length=8),
                       dict(part_role="frame"),dict(connector_design="cabinet"),
                       dict(key_arm_thickness=1.2),dict(rail_width=15)]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                self.parameters(**change)

    def test_three_piece_key_and_two_piece_direct_snaps(self):
        import oobb
        for name,count in [("snap_single",2),("snap_twin",2),("snap_key",3),("screw_reference",2),("connector_suite",9)]:
            p=self.parameters(connector_design=name)
            thing=oobb.get_default_thing(type="test")
            drawing.get_ai_version_5(thing,**p)
            self.assertEqual(thing["ai_design"]["expected_bodies"],count)
            self.assertEqual("key" in drawing.get_ai_version_5_views(p),name=="snap_key")

    def test_options_do_not_modify_v4(self):
        original=population.get_ai_version_4_options()
        options=population.get_ai_version_5_options()
        options[0]["plate_thickness"]=999
        self.assertEqual(population.get_ai_version_4_options(),original)

    def test_numbered_matrix_has_nine_distinct_pairs_at_original_rail_scale(self):
        suite=next(o for o in population.get_ai_version_5_options() if o["connector_design"]=="key_size_fit_suite")
        trials=suite["key_trials"]
        self.assertEqual([t["sample_number"] for t in trials],list(range(1,10)))
        self.assertEqual({t["key_scale"] for t in trials},{1.0,1.15,1.3})
        self.assertEqual({t["connector_clearance"] for t in trials},{0.2,0.3,0.4})
        self.assertEqual(len({(t["key_scale"],t["connector_clearance"]) for t in trials}),9)
        for t in trials:
            p=drawing.get_ai_version_5_parameters(**{**suite,**t,"connector_design":"snap_key"})
            self.assertEqual((p["rail_width"],p["rail_height"],p["plate_thickness"]),(11,10,7.5))
            self.assertAlmostEqual(p["key_height"],4*t["key_scale"])
        import oobb
        thing=oobb.get_default_thing(type="test")
        drawing.get_ai_version_5(thing,**suite)
        self.assertEqual(thing["ai_design"]["expected_bodies"],27)

    def test_numbers_are_recessed_on_print_top_away_from_joint(self):
        from unittest.mock import patch
        import working_scad_container_cutout as cuts
        suite=next(o for o in population.get_ai_version_5_options() if o["variant"]=="key_size_fit_suite")
        p=drawing.get_ai_version_5_parameters(**{**suite,**suite["key_trials"][-1],"connector_design":"snap_key"})
        with patch.object(cuts.oobb,"append_full") as append:
            cuts.get_container_cutout_ai_version_5([0,0,0],{},**dict(p,connector_component="rail"))
        label=next(c.kwargs for c in append.call_args_list if c.kwargs.get("shape")=="text")
        self.assertEqual(label["type"],"negative")
        self.assertEqual(label["text"],"9")
        self.assertEqual(label["rot"],[-90,0,0])
        self.assertEqual(label["pos"],[0,9.4,24])

    def test_through_taper_matrix_is_independent_and_modest(self):
        trials=population.get_ai_version_5_through_trials()
        self.assertEqual([t["sample_number"] for t in trials],list(range(10,19)))
        self.assertEqual({t["key_scale"] for t in trials},{1.15})
        self.assertEqual({t["connector_clearance"] for t in trials},{0.3})
        self.assertEqual(len({(t["through_clearance"],t["through_seat_interference"]) for t in trials}),9)
        for trial in trials:
            p=self.parameters(**trial,connector_design="snap_key")
            self.assertEqual(p["through_taper_length"],6)
            self.assertLessEqual(p["through_seat_interference"],0.05)
        with self.assertRaises(ValueError):
            self.parameters(**{**trials[0],"through_seat_interference":0.15})

    def test_recessed_tabs_have_room_to_flex_and_stay_inside_plate(self):
        option=next(o for o in population.get_ai_version_5_options() if o["connector_design"]=="snap_recessed_twin")
        p=drawing.get_ai_version_5_parameters(**option)
        self.assertEqual(p["connector_design"],"snap_recessed_twin")
        self.assertAlmostEqual(p["insertion_deflection"],0.95)
        self.assertGreater(p["open_center_half_width"],p["insertion_deflection"]+0.3)
        self.assertAlmostEqual(p["hook_tip_z"]+p["plate_thickness"],0)
        self.assertAlmostEqual(p["effective_arm_length"],6)
        self.assertLessEqual(p["root_distance"],1)
        self.assertGreater(p["receiver_shoulder_z"],0)
        self.assertLess(p["receiver_shoulder_z"],p["plate_thickness"])
        for change in [dict(hook_projection=2),dict(recessed_shoulder_depth=5),
                       dict(coupon_width=11),dict(twin_arm_thickness=2.3),
                       dict(twin_root_distance=12)]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                drawing.get_ai_version_5_parameters(**{**option,**change})

    def test_larger_keys_continue_size_axis_from_nine(self):
        suite=next(o for o in population.get_ai_version_5_options() if o["variant"]=="key_size_extension_suite")
        trials=suite["key_trials"]
        self.assertEqual([t["sample_number"] for t in trials],[20,21,22])
        self.assertEqual([t["key_scale"] for t in trials],[1.45,1.6,1.75])
        for t in trials:
            self.assertEqual(t["connector_clearance"],0.4)
            self.assertEqual(t["through_clearance"],0.25)
            p=drawing.get_ai_version_5_parameters(**{**suite,**t,"connector_design":"snap_key"})
            self.assertGreaterEqual((p["rail_height"]-p["key_height"]-2*p["connector_clearance"])/2,1)
            self.assertAlmostEqual(p["key_arm_thickness"],0.8*p["key_scale"])
        import oobb
        thing=oobb.get_default_thing(type="test")
        drawing.get_ai_version_5(thing,**suite)
        self.assertEqual(thing["ai_design"]["expected_bodies"],9)
        self.assertEqual(len(drawing.get_ai_version_5_views(suite)),16)


if __name__=="__main__":
    unittest.main()
