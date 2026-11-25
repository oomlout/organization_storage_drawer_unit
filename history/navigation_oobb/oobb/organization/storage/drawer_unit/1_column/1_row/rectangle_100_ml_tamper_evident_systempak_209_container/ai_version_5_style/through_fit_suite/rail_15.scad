$fn = 50;

difference() {
	union() {
		translate(v = [0, 9.21625, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 32.0]);
						}
						translate(v = [0, 10.0, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.0) {
									polygon(points = [[-2.875, -13.5675], [2.875, -13.5675], [2.875, -6.0], [3.125, 0], [3.125, 0.1], [-3.125, 0.1], [-3.125, 0], [-2.875, -6.0]]);
								}
							}
						}
					}
					union() {
						translate(v = [-2.975, 2.4000000000000004, -11.9675]) {
							cube(size = [5.95, 5.199999999999999, 3.8200000000000003]);
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "15", valign = "center");
								}
							}
						}
						translate(v = [5.5, 10.1, 30.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.6);
							}
						}
						translate(v = [5.5, 10.1, 28.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.6);
							}
						}
						translate(v = [5.5, 10.1, 26.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.6);
							}
						}
					}
				}
			}
		}
	}
	union();
}
