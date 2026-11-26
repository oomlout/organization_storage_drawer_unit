face_t=6.0;
tie_t=3.0;
$fn=64;

module cap_bores() {
  for (side=[-1,1], i=[0:4])
    translate([side*(inside_w/2+t/2),0,stations[i]]) rotate([-90,0,0])
      if (i%2==0) translate([0,0,-.01]) cylinder(d=6.1,h=8.01);
      else {
        translate([0,0,-.01]) cylinder(d=4,h=t+.02);
        translate([0,0,t-1.5]) cylinder(d1=4,d2=7.02,h=1.51);
      }
}
module side_bores() {
  for (bottom=[0,1], i=[0:4])
    translate([t/2,bottom*inside_h,stations[i]]) rotate([bottom?90:-90,0,0])
      translate([0,0,-.01]) cylinder(d=i%2?2.5:6.1,h=i%2?21.01:17.01);
  for (back=[0,1], y=retainer_y)
    translate([t/2,y,back*depth]) rotate([0,back?180:0,0])
      translate([0,0,-.01]) cylinder(d=2.5,h=16.01);
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
