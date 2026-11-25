$fn = 50;

difference() {
	union() {
		translate(v = [0, -5, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-7.5, -2.0, 0]) {
							cube(size = [15.0, 14.0, 7.5]);
						}
					}
					union() {
						translate(v = [-3.175, -0.25, -0.1]) {
							cube(size = [6.35, 10.5, 7.7]);
						}
						translate(v = [-5.5, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "18", valign = "center");
							}
						}
						translate(v = [-7.5, 3, -0.1]) {
							cylinder(h = 7.7, r = 0.6);
						}
						translate(v = [-7.5, 5, -0.1]) {
							cylinder(h = 7.7, r = 0.6);
						}
						translate(v = [-7.5, 7, -0.1]) {
							cylinder(h = 7.7, r = 0.6);
						}
					}
				}
			}
		}
	}
	union();
}
