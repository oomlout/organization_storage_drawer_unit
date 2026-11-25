$fn = 50;

difference() {
	union() {
		translate(v = [0, 8.39, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 32.0]);
						}
						translate(v = [-4.0, 0, -15.22]) {
							cube(size = [8.0, 10.0, 15.32]);
						}
					}
					union() {
						translate(v = [-4.1, 1.4, -13.620000000000001]) {
							cube(size = [8.2, 7.2, 5.28]);
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "21", valign = "center");
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
