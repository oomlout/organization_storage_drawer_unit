include <cabinet_geometry.scad>
include <beam_joint_geometry.scad>
module part_cap() { cap_panel();
}
module part_side() { side_panel();
}
module part_floor_strip() { cube([15,2,209.0]);
}
module part_dowel() { dowel();
}
module part_wood_30() { wood_screw(30);
}
module part_wood_16() { wood_screw(16);
}
module part_plywood_joint() { beam_joint([[0, 0]],[-0.9, -7.2, 21.6, 7.2],[15.6, 0.0],[[4.6, -8.0, -5.5, 2.05], [4.6, 5.5, 8.0, 2.05]]);
}
module part_plywood_double() { beam_joint([[0, 0], [0, 34.5]],[-0.9, -3.9, 21.6, 38.4],[15.6, 17.25],[[4.6, 5.5, 5.5, 2.05], [4.6, 17.0, 17.5, 2.05], [4.6, 29.0, 29.0, 2.05]]);
}
module part_edge_across() { beam_joint([[0, 0], [19.2, 0]],[-0.9, -7.2, 20.099999999999998, 7.2],[],[[4.6, -8.0, -5.5, 2.05], [4.6, 5.5, 8.0, 2.05], [14.6, -8.0, -5.5, 2.05], [14.6, 5.5, 8.0, 2.05]]);
}
module part_tee4() { beam_joint([[0, 0], [0, 34.5], [19.2, 0], [19.2, 34.5]],[-0.9, -3.9, 20.099999999999998, 38.4],[],[[4.6, 5.5, 5.5, 2.05], [4.6, 17.0, 17.5, 2.05], [4.6, 29.0, 29.0, 2.05], [14.6, 5.5, 5.5, 2.05], [14.6, 17.0, 17.5, 2.05], [14.6, 29.0, 29.0, 2.05]]);
}
module part_array_unit() { include <array_unit.scad>
}
module part_beam_nut() { include <beam_nut.scad>
}
module part_beam_screw() { include <beam_screw.scad>
}
