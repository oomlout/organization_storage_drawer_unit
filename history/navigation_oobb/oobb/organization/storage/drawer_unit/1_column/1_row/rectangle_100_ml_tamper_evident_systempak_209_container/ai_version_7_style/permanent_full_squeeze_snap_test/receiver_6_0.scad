$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-37.0, 13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [37.0, 13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [-37.0, -13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [37.0, -13.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
						}
					}
					union() {
						translate(v = [-26.6, -2.1, -0.1]) {
							cube(size = [5.2, 4.2, 6.2]);
						}
						translate(v = [-24.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "60", valign = "center");
							}
						}
						translate(v = [-2.6, -2.1, -0.1]) {
							cube(size = [5.2, 4.2, 6.2]);
						}
						translate(v = [0.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "61", valign = "center");
							}
						}
						translate(v = [21.4, -2.1, -0.1]) {
							cube(size = [5.2, 4.2, 6.2]);
						}
						translate(v = [24.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "62", valign = "center");
							}
						}
					}
				}
			}
		}
	}
	union();
}
