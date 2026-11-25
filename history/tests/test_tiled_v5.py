import unittest
from working_oomp_populate import get_ai_version_5_tiled_options
from working_scad import get_ai_version_5_parameters
from working_scad_tiling import bed_pose


class TiledTests(unittest.TestCase):
    def parameters(self):
        return [get_ai_version_5_parameters(**o) for o in get_ai_version_5_tiled_options()]

    def test_outside_dimensions_preserve_tray_openings(self):
        for p, width, height, columns, rows in zip(
                self.parameters(),[767,362,205.8],[308,308,268.6],[8,3,2],[9,9,8]):
            self.assertEqual([p["width_total"],p["height_total"]],[width,height])
            self.assertEqual([p["column"],p["row"]],[columns,rows])
            self.assertEqual([p["opening_width"],p["opening_height"]],[87.5,28.5])
            self.assertTrue(p["front_lip"])
            self.assertFalse(p["rear_lip"])

    def test_extra_spacing_moves_openings_and_rails_together(self):
        for option,p in zip(get_ai_version_5_tiled_options(),self.parameters()):
            old=get_ai_version_5_parameters(**dict(option,row_spacing_extra=0))
            self.assertAlmostEqual(p["pitch_y"],31.3)
            self.assertAlmostEqual(p["pitch_y"]-p["opening_height"],2.8)
            self.assertAlmostEqual(p["pitch_y"]-old["pitch_y"],1)
            self.assertAlmostEqual(p["natural_height"]-old["natural_height"],p["row"]-1)
            top=-p["natural_height"]/2+p["drawer_border_edge"]+(p["row"]-1)*p["pitch_y"]+p["opening_height"]
            self.assertAlmostEqual(p["natural_height"]/2-top,p["drawer_border_edge"])
            for x in p["x_mounts"]:
                rails=[r for r in p["rail_positions"] if r["x"]==x][:p["row"]]
                for row,rail in enumerate(rails):
                    bottom=-p["natural_height"]/2+p["drawer_border_edge"]+row*p["pitch_y"]
                    self.assertAlmostEqual(rail["y"]-bottom,p["depth_lip"])
                for a,b in zip(rails,rails[1:]):
                    self.assertAlmostEqual(b["y"]-a["y"],p["pitch_y"])

    def test_seam_ends_and_long_edge_middle_use_screws(self):
        for p, count, old_screws in zip(self.parameters(),[8,4],[39,14]):
            self.assertEqual(len(p["tiles"]),count)
            self.assertLess(p["bom"]["M3_nut"],2*old_screws)
            for r in p["rail_positions"]:
                self.assertEqual(r["connection"],"screw" if r["seam_anchor"] else "snap")
                if r["seam_anchor"]:
                    self.assertTrue(r["seam"])
            self.assertTrue(any(r["seam"] and r["connection"]=="snap" for r in p["rail_positions"]))
            self.assertEqual(sum(p["bom"][k] for k in p["bom"] if k.endswith("rail")),
                             (p["column"]+1)*(p["row"]+2))
        o=get_ai_version_5_tiled_options()[0]
        p=get_ai_version_5_parameters(**dict(o,additional_screw_every=1))
        self.assertTrue(all(r["connection"]=="screw" for r in p["rail_positions"]))

    def test_whole_footprint_clears_cutter_and_ears(self):
        for p in self.parameters():
            for t in p["tiles"]:
                x,y=t["bed_center"]
                w,h=t["footprint"]
                self.assertGreaterEqual(x-w/2,-p["bed_width"]/2+p["bed_margin"]-1e-7)
                self.assertLessEqual(x+w/2,p["bed_width"]/2-p["bed_margin"]+1e-7)
                self.assertGreaterEqual(y-h/2,-p["bed_height"]/2+p["bed_margin"]-1e-7)
                self.assertLessEqual(y+h/2,p["bed_height"]/2-p["bed_margin"]+1e-7)
                self.assertTrue(x-w/2 >= -p["bed_width"]/2+p["bed_exclusion"][0]+p["bed_margin"]-1e-7 or
                                y-h/2 >= -p["bed_height"]/2+p["bed_exclusion"][1]+p["bed_margin"]-1e-7)
        self.assertIsNone(bed_pose(252,252,self.parameters()[0]))

    def test_laps_are_half_thickness_without_overlapping_tiles(self):
        from shapely.geometry import box
        for p in self.parameters():
            self.assertEqual(p["plate_thickness"]/2,3)
            for layer in [0,1]:
                shapes=[]
                for t in p["tiles"]:
                    shape=box(*t["layers"][layer])
                    for notch in t["notches"][layer]:
                        shape=shape.difference(box(*notch))
                    shapes.append(shape)
                for i,a in enumerate(shapes):
                    for b in shapes[i+1:]:
                        self.assertLess(a.intersection(b).area,1e-7)
            for t in p["tiles"]:
                self.assertGreater(box(*t["layers"][0]).intersection(box(*t["layers"][1])).area,100)
                shapes=[]
                for layer in [0,1]:
                    shape=box(*t["layers"][layer])
                    for notch in t["notches"][layer]:
                        shape=shape.difference(box(*notch))
                    shapes.append(shape)
                self.assertLess(shapes[1-t["bed_layer"]].difference(shapes[t["bed_layer"]]).area,1e-7)
                self.assertEqual(t["bed_layer"],(t["column"]+t["row"])%2)

    def test_oversize_or_invalid_inputs_rejected(self):
        o=get_ai_version_5_tiled_options()[0]
        for change in [dict(target_width=300),dict(tile_seam_clearance=1),
                       dict(additional_screw_every=-1),dict(tile_lap_x=3),dict(snap_tip_floor=3),
                       dict(row_spacing_extra=-1),dict(row_spacing_extra=float('nan'))]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                get_ai_version_5_parameters(**{**o,**change})

    def test_position_is_applied_once_without_mutating_caller(self):
        import oobb
        from working_scad import get_ai_version_5
        o=get_ai_version_5_tiled_options()[0]
        origin=[2,3,4]
        thing=oobb.get_default_thing(type="test")
        get_ai_version_5(thing,**dict(o,connector_view="snap_rail",pos=origin))
        self.assertEqual(origin,[2,3,4])
        self.assertEqual(thing["components"][0]["pos"],[2,52.25,4])

    def test_six_mm_panels_keep_recessed_hooks_and_flex_length(self):
        for p in self.parameters():
            self.assertEqual(p["plate_thickness"],6)
            self.assertEqual(p["catch_tab_height"],6)
            self.assertEqual(p["stop_thickness"],6)
            self.assertEqual(p["snap_tip_length"],6)
            self.assertEqual(p["snap_shoulder_depth"],4.5)
            self.assertEqual(p["snap_root_distance"],2)
            self.assertEqual(p["rail_length"],98.5)
            self.assertEqual(p["snap_root_relief_width"],.6)
            self.assertEqual(p["snap_root_distance"]+p["snap_shoulder_depth"],6.5)
            self.assertEqual(p["nut_far"]+p["plate_thickness"],16)
            self.assertGreaterEqual(p["rail_end_band"]-p["nut_far"],1.5)

    def test_a1_mini_has_four_tiles_per_face(self):
        p=self.parameters()[2]
        self.assertEqual([p["bed_width"],p["bed_height"]],[180,180])
        self.assertEqual([len(p["tile_x_edges"])-1,len(p["tile_y_edges"])-1],[2,2])
        self.assertEqual(len(p["tiles"]),4)
        self.assertEqual([p["column"],p["row"]],[2,8])
        self.assertEqual(p["tile_ear_diameter"],11)
        # The next full row needs a third row of tiles with the ears retained.
        o=get_ai_version_5_tiled_options()[2]
        with self.assertRaises(ValueError):
            get_ai_version_5_parameters(**dict(o,row=9,target_height=291.9))
        with self.assertRaises(ValueError):
            get_ai_version_5_parameters(**dict(o,column=3,target_width=295.1))

    def test_rear_m6_seats_are_mirrored_and_clear_of_joints(self):
        for p in self.parameters():
            points={(a["x"],a["y"]) for a in p["rear_attachments"]}
            self.assertGreaterEqual(len(points),6)
            self.assertEqual(points,{(-x,y) for x,y in points})
            self.assertEqual(p["attachment_nut_depth"],1.5)
            for x,y in points:
                for seam in p["tile_x_edges"][1:-1]:
                    self.assertGreater(abs(x-seam),11)
                for seam in p["tile_y_edges"][1:-1]:
                    self.assertGreater(abs(y-seam),10)
                for rail in p["rail_positions"]:
                    self.assertTrue(abs(x-rail["x"])>12 or abs(y-rail["axis_y"])>12)
