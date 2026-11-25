"""Check the new key's capture span without changing sample 22's receiver."""
import unittest
import working_oomp_populate as population
import working_scad as drawing


class TightKeyTests(unittest.TestCase):
    def test_compatible_slot_and_adjustable_capture(self):
        option=next(o for o in population.get_ai_version_5_options() if o["variant"]=="tight_key_27")
        old=drawing.get_ai_version_5_parameters(**{
            **option,**population.get_ai_version_5_key_extension_trials()[-1],
            "tight_key_trial":False,
        })
        for gap in [.05,.1,.2]:
            p=drawing.get_ai_version_5_parameters(**dict(option,key_latch_clearance=gap))
            for name in ["key_z","key_tongue_depth","key_tongue_half_width",
                         "key_height","key_half_width","connector_clearance",
                         "through_clearance","through_height_clearance"]:
                self.assertEqual(p[name],old[name],name)
            self.assertAlmostEqual(p["key_shoulder_x"]-p["key_tongue_half_width"],gap)
            self.assertAlmostEqual(-p["key_tongue_half_width"]-(p["key_head_x"]+p["key_head_length"]),gap)
        for invalid in [0,-.1,.3,float("nan")]:
            with self.assertRaises(ValueError):
                drawing.get_ai_version_5_parameters(**dict(option,key_latch_clearance=invalid))
        with self.assertRaises(ValueError):
            drawing.get_ai_version_5_parameters(**dict(option,tight_key_trial=False))
