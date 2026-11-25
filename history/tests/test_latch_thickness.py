import unittest
import oobb
import working_oomp_populate as population
import working_scad as drawing


class LatchThicknessTests(unittest.TestCase):
    def option(self):
        return next(o for o in population.get_ai_version_5_options()
                    if o["connector_design"]=="recessed_twin_fit_suite")

    def test_numbered_progression_changes_only_arm_thickness(self):
        o=self.option()
        self.assertEqual([t["sample_number"] for t in o["latch_trials"]],[23,24,25,26])
        self.assertEqual([t["twin_arm_thickness"] for t in o["latch_trials"]],[1,1.2,1.4,1.6])
        reference=drawing.get_ai_version_5_parameters(**dict(o,connector_design="snap_recessed_twin"))
        for t in o["latch_trials"]:
            p=drawing.get_ai_version_5_parameters(**{**o,**t,"connector_design":"snap_recessed_twin"})
            for key in ["hook_tip_z","hook_shoulder_z","receiver_shoulder_z",
                        "receiver_pocket_half_width","connector_clearance","effective_arm_length"]:
                self.assertEqual(p[key],reference[key])
            self.assertGreater(p["open_center_half_width"],p["insertion_deflection"]+0.3)

    def test_old_19_guard_stays_strict_and_new_trials_are_bounded(self):
        o=self.option()
        for change in [dict(connector_design="snap_recessed_twin",twin_arm_thickness=1.6),
                       dict(connector_design="snap_recessed_twin",sample_number=26,latch_thickness_trial=True,twin_arm_thickness=1.8)]:
            with self.assertRaises(ValueError):
                drawing.get_ai_version_5_parameters(**{**o,**change})

    def test_complete_kit_and_individual_views(self):
        o=self.option()
        thing=oobb.get_default_thing(type="test")
        drawing.get_ai_version_5(thing,**o)
        self.assertEqual(thing["ai_design"]["expected_bodies"],8)
        self.assertEqual(len(drawing.get_ai_version_5_views(o)),17)
        for view,count in [("trial_26",2),("rail_26",1),("plate_26",1)]:
            thing=oobb.get_default_thing(type="test")
            drawing.get_ai_version_5(thing,**dict(o,connector_view=view))
            self.assertEqual(thing["ai_design"]["expected_bodies"],count)

    def test_heavy_suite_retains_controls_and_flex_space(self):
        o=next(o for o in population.get_ai_version_5_options()
               if o["variant"]=="recessed_twin_heavy_suite")
        self.assertEqual([t["sample_number"] for t in o["latch_trials"]],[25,26,28,29])
        self.assertEqual(o["latch_trials"][:2],population.get_ai_version_5_latch_trials()[2:])
        self.assertEqual([t["twin_arm_thickness"] for t in o["latch_trials"]],[1.4,1.6,1.8,2.0])
        drawing.get_ai_version_5_parameters(**o)
        for trial in o["latch_trials"][2:]:
            p=drawing.get_ai_version_5_parameters(**{**o,**trial,"connector_design":"snap_recessed_twin"})
            self.assertGreater(p["open_center_half_width"],p["insertion_deflection"]+.3)
            for change in [{"heavy_latch_trial":False},{"twin_arm_thickness":2.1}]:
                with self.assertRaises(ValueError):
                    drawing.get_ai_version_5_parameters(**{**p,**change})
