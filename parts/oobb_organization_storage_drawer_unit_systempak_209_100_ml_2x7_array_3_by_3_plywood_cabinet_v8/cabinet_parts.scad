include <cabinet_geometry.scad>
include <beam_joint_geometry.scad>
module part_cap() { cap_panel();
}
module part_side() { side_panel();
}
module part_plywood_joint() { beam_joint([[0, 0]],[],[15.6, 0]);
}
module part_floor_strip() { cube([15,2,209.0]);
}
module part_dowel() { dowel();
}
module part_wood_30() { wood_screw(30);
}
module part_wood_16() { wood_screw(16);
}
module part_edge_upright() { beam_joint([[0, 0], [0, 34.5]],[[6.5, 0], [6.5, 34.5]],[]);
}
module part_edge_across() { beam_joint([[0, 0], [19.2, 0]],[],[]);
}
module part_tee4() { beam_joint([[0, 0], [0, 34.5], [19.2, 0], [19.2, 34.5]],[[9.6, 0], [9.6, 34.5]],[]);
}
module part_array_unit() { include <array_unit.scad>
}
module part_beam_nut() { include <beam_nut.scad>
}
module part_beam_screw() { include <beam_screw.scad>
}
