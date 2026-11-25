$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-13.0, 13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [13.0, 13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [-13.0, -13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [13.0, -13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
						}
					}
					union() {
						translate(v = [-2.6, -2.6, -0.1]) {
							cube(size = [5.2, 5.2, 6.2]);
						}
						translate(v = [0.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "70", valign = "center");
							}
						}
					}
				}
			}
		}
	}
	union();
}
