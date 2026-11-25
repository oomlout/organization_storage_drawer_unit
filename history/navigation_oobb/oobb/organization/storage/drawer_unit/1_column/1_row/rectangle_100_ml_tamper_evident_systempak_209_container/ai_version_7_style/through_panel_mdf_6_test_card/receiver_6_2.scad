$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-61.0, 14.0, 0]) {
								cylinder(h = 6.2, r = 2);
							}
							translate(v = [61.0, 14.0, 0]) {
								cylinder(h = 6.2, r = 2);
							}
							translate(v = [-61.0, -14.0, 0]) {
								cylinder(h = 6.2, r = 2);
							}
							translate(v = [61.0, -14.0, 0]) {
								cylinder(h = 6.2, r = 2);
							}
						}
					}
					union() {
						translate(v = [-51.6, -2.3, -0.1]) {
							cube(size = [7.2, 4.6, 6.4]);
						}
						translate(v = [-48, 10, 5.8]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "7.2", valign = "center");
							}
						}
						translate(v = [-27.7, -2.3, -0.1]) {
							cube(size = [7.4, 4.6, 6.4]);
						}
						translate(v = [-24, 10, 5.8]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "7.4", valign = "center");
							}
						}
						translate(v = [-3.8, -2.3, -0.1]) {
							cube(size = [7.6, 4.6, 6.4]);
						}
						translate(v = [0, 10, 5.8]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "7.6", valign = "center");
							}
						}
						translate(v = [20.1, -2.3, -0.1]) {
							cube(size = [7.8, 4.6, 6.4]);
						}
						translate(v = [24, 10, 5.8]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "7.8", valign = "center");
							}
						}
						translate(v = [44.0, -2.3, -0.1]) {
							cube(size = [8.0, 4.6, 6.4]);
						}
						translate(v = [48, 10, 5.8]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 3, text = "8.0", valign = "center");
							}
						}
					}
				}
			}
		}
	}
	union();
}
