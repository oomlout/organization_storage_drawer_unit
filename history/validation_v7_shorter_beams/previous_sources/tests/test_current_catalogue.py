"""Current manufacturing scope, counts and bed-sized V7 batches."""
import copy
import unittest
from unittest.mock import patch
import working_oomp_populate as population
import working_scad as drawing


class CurrentCatalogueTests(unittest.TestCase):
    def test_default_population_emits_current_v7_frames(self):
        with patch.object(population,'write_extras') as writer:population.main()
        parts=writer.call_args.args[0]
        self.assertEqual([(p['column'],p['row']) for p in parts],[(2,7),(4,12),(1,2),(2,2)])
        self.assertTrue(all(p['style']=='ai_version_7' and p['part_role']=='frame' for p in parts))
        self.assertEqual(len({population.build_oomp_id(p) for p in parts}),4)
        for part in parts:
            self.assertEqual(part['taxonomy_5'],part['container_short']+'_container')
            self.assertEqual(part['taxonomy_6'],f"{part['column']}_column")
            self.assertEqual(part['taxonomy_7'],f"{part['row']}_row")
            for field in ['taxonomy_5','taxonomy_6','taxonomy_7']:
                self.assertEqual(part['oobb_details'][field],part[field])

    def test_plywood_envelopes_and_outer_screw_positions_are_preserved(self):
        for source in population.get_current_options()[:2]:
            p=drawing.get_ai_version_7_frame_parameters(**source);q=p['frame']
            old=next(o for o in population.get_ai_version_6_options() if o['variant']==p['variant'])
            before=drawing.get_ai_version_6_parameters(**old)
            for key in ['width_total','height_total','assembled_depth','drawer_count']:
                self.assertAlmostEqual(q[key],before[key])
            self.assertEqual(p['bom']['screw_beam'],4)
            screws=[r for r in p['frame_mounts'] if r['kind']=='screw_beam']
            self.assertEqual({(r['x'],r['hole_y']-8) for r in screws},
                             {(r['x'],r['y']) for r in before['screw_rail_positions']})
            self.assertEqual(len(p['frame_mounts']),len(before['rail_positions']))

    def test_batches_conserve_quantities_and_fit_declared_bed(self):
        for source in population.get_current_options():
            p=drawing.get_ai_version_7_frame_parameters(**source);q=p['frame']
            totals={key:0 for key in ['snap_beam','screw_beam','front_plug','screw_adapter']}
            for batch in p['print_batches'].values():
                totals[batch['component']]+=batch['count']
                self.assertLessEqual(batch['count']*batch['pitch'],
                                     q['bed_width']-q['bed_exclusion'][0]-2*q['bed_margin'])
            for key,total in totals.items():self.assertEqual(total,p['bom'][key])
            self.assertEqual(p['bom']['front_plug'],2*p['bom']['snap_beam'])
            self.assertEqual(p['bom']['screw_adapter'],2*p['bom']['screw_beam'])

    def test_current_options_do_not_mutate_historical_options(self):
        before=copy.deepcopy(population.get_historical_options())
        current=population.get_current_options();current[0]['front_plug']['stem_width']=99
        self.assertEqual(population.get_historical_options(),before)

    def test_laser_test_reinforces_every_clip_and_screw(self):
        for source,quantity,relieved in zip(population.get_current_options(),[21,60,6,9],[2,2,0,0]):
            p=drawing.get_ai_version_7_frame_parameters(**source)
            self.assertEqual(len(p['reinforcement_pads']),quantity)
            self.assertEqual(sum(bool(pad['reliefs']) for pad in p['reinforcement_pads']),relieved)
            self.assertEqual({(pad['x'],pad['hole_y']) for pad in p['reinforcement_pads']},
                             {(r['x'],r['hole_y']) for r in p['frame_mounts']})
            self.assertEqual(p['laser_face_test']['face_thickness']+p['laser_face_test']['reinforcement_thickness'],6)
            self.assertEqual(p['laser_face_test']['reinforcement_side'],12)

    def test_laser_test_rejects_wrong_stack_or_wide_square(self):
        for changes in [dict(face_thickness=2),dict(reinforcement_side=13),dict(nesting_gap=-1)]:
            source=population.get_current_options()[0]
            source['laser_face_test'].update(changes)
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                drawing.get_ai_version_7_frame_parameters(**source)


if __name__=='__main__':unittest.main()
