rotate([-90,0,0]) intersection() {
translate([-186.6,-177.4,-3]) cube([16,18,29]);
union() {
color("teal") { include <front.scad>; }
color("gold") translate([-178.6,-166.4,-2.4]) import("screw_adapter.stl");
color("steelblue") translate([-178.6,-174.4,6]) multmatrix([[1,0,0,0],[0,0,1,0],[0,-1,0,106.0],[0,0,0,1]]) import("screw_rail.stl");
}
}
