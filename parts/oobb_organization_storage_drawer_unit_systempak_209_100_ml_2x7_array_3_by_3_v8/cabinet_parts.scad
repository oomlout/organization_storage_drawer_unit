include <cabinet_geometry.scad>
include <beam_joint_geometry.scad>
module part_floor_strip() { cube([15,2,209.0]);
}
module part_screw_adapter() { include <array_adapter_source.scad>
}
module part_edge_upright() { beam_joint([[0, 0], [0, 34.5]],[-0.9, -3.9, 9.6, 38.4],[],[[4.6, 5.5, 5.5, 2.05], [4.6, 17.0, 17.5, 2.05], [4.6, 29.0, 29.0, 2.05]]);
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
