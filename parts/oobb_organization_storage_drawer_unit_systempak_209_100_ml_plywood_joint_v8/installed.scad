rotate([-90,0,0]) {
color("teal") import("detail_face.stl");
color("darkslategray") import("detail_rail.stl");
color("silver") import("detail_hardware.stl");
color("orange") import("detail_bracket.stl");
color("burlywood") difference() {translate([9.6,-14,0]) cube([12,28,27]); translate([15.6,0.0,-.05]) cylinder(d=2.5,h=16.05,$fn=48);}
color("silver") translate([15.6,0.0,-3.0]) wood_screw(16);
}

module cap_panel() {
  difference() {
    translate([-cap_w/2,0,0]) cube([cap_w,t,depth]);
    cap_bores();
  }
}
module side_panel() {
  difference() {
    cube([t,inside_h,depth]);
    side_bores();
  }
}
module wood_screw(length) {
  // Flush 90-degree head, nominal shank and tapered point. Thread envelope.
  difference(){
    union(){
      cylinder(h=1.75,d1=7,d2=3.5);
      translate([0,0,1.74]) cylinder(h=length-4.74,d=3.5);
      translate([0,0,length-3.01]) cylinder(h=3.01,d1=3.5,d2=0);
    }
    for(a=[0,90]) rotate([0,0,a]) translate([-2,-.4,-.01]) cube([4,.8,.81]);
  }
}
module dowel() {
  cylinder(h=.5,d1=5,d2=6);
  translate([0,0,.5]) cylinder(d=6,h=23);
  translate([0,0,23.5]) cylinder(h=.5,d1=6,d2=5);
}
