$fn=64;
tie_t=3.0;
module native_adapter(){
include <native_adapter.scad>
}

module joint_bores(holes,wood,access) {
  for(slot=access) hull()
    for(y=[slot[1],slot[2]]) translate([slot[0],y,-.05]) cylinder(r=slot[3],h=tie_t+.1);
  // Leave the OOBB countersink and pilot cheeks of each native adapter intact.
  for(p=holes) translate([p[0],p[1],-.05]) cylinder(d=7,h=tie_t+.1);
  if(len(wood)) translate(wood) {
    translate([0,0,-.05]) cylinder(d=4,h=tie_t+.1);
    translate([0,0,-.01]) cylinder(d1=7.02,d2=4,h=1.51);
  }
}

module plate_outline(bounds) {
  r=2;
  offset(r=r) translate([bounds[0]+r,bounds[1]+r])
    square([bounds[2]-bounds[0]-2*r,bounds[3]-bounds[1]-2*r]);
}
module beam_joint(holes,bounds,wood=[],access=[]) {
  union(){
    for(p=holes) translate(p) intersection(){
      native_adapter();
      cylinder(r=4,h=12);
    }
    difference(){
      linear_extrude(tie_t) union(){
        plate_outline(bounds);
        for(p=holes) hull(){
          translate(p) circle(r=4.1);
          translate([p[0]+(p[0]==0 ? 3 : -3),p[1]]) circle(r=4.1);
        }
      }
      joint_bores(holes,wood,access);
    }
  }
}
