rotate([-90,0,0]) intersection() {
translate([-97.3,-99.14999999999999,-3]) cube([16,18,29]);
union() {
color("teal") { include <front.scad>; }
color("gold") translate([-89.3,-88.14999999999999,-2.4]) import("screw_adapter.stl");
color("steelblue") translate([-89.3,-96.14999999999999,6]) multmatrix([[1,0,0,0],[0,0,1,0],[0,-1,0,106.0],[0,0,0,1]]) import("screw_rail.stl");
}
}
