$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-73.0, 14.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [73.0, 14.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [-73.0, -14.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
							translate(v = [73.0, -14.0, 0]) {
								cylinder(h = 6.0, r = 2);
							}
						}
					}
					union() {
						translate(v = [-63.0, -2.3, -0.1]) {
							cube(size = [6.0, 4.6, 6.2]);
						}
						translate(v = [-60.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "50", valign = "center");
							}
						}
						translate(v = [-39.0, -2.3, -0.1]) {
							cube(size = [6.0, 4.6, 6.2]);
						}
						translate(v = [-36.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "51", valign = "center");
							}
						}
						translate(v = [-15.0, -2.3, -0.1]) {
							cube(size = [6.0, 4.6, 6.2]);
						}
						translate(v = [-12.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "52", valign = "center");
							}
						}
						translate(v = [9.0, -2.3, -0.1]) {
							cube(size = [6.0, 4.6, 6.2]);
						}
						translate(v = [12.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "53", valign = "center");
							}
						}
						translate(v = [33.0, -2.3, -0.1]) {
							cube(size = [6.0, 4.6, 6.2]);
						}
						translate(v = [36.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "54", valign = "center");
							}
						}
						translate(v = [57.0, -2.3, -0.1]) {
							cube(size = [6.0, 4.6, 6.2]);
						}
						translate(v = [60.0, 10, 5.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "M3", valign = "center");
							}
						}
					}
				}
			}
		}
	}
	union();
}
