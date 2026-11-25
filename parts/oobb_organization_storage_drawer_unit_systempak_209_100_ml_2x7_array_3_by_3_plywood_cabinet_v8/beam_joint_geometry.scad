$fn=64;
tie_t=2.4;
module native_adapter(){
include <native_adapter.scad>
}

module joint_bores(holes,wood) {
  // Leave the OOBB countersink and pilot cheeks of each native adapter intact.
  for(p=holes) translate([p[0],p[1],-.05]) cylinder(d=7,h=tie_t+.1);
  if(len(wood)) translate(wood) {
    translate([0,0,-.05]) cylinder(d=4,h=tie_t+.1);
    translate([0,0,-.01]) cylinder(d1=7.02,d2=4,h=1.51);
  }
}

module foot(p,r) { translate(p) circle(r=r); }
module strap(a,b,ra,rb) { hull(){ foot(a,ra); foot(b,rb); } }
module beam_joint(holes,spine=[],wood=[]) {
  union(){
    for(p=holes) translate(p) intersection(){
      native_adapter();
      cylinder(r=4,h=12);
    }
    difference(){
      linear_extrude(tie_t) union(){
        if(len(wood)) strap(holes[0],wood,4,4.6);
        else if(len(spine)==0) strap(holes[0],holes[1],4,4);
        else {
          strap(spine[0],spine[1],2.65,2.65);
          for(p=holes) strap(p,[spine[0][0],p[1]],4,2.65);
        }
      }
      joint_bores(holes,wood);
    }
  }
}
