$fn = 50;

difference() {
	union() {
		translate(v = [0, 12.25, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -7.5]) {
							cube(size = [11.0, 10.0, 39.5]);
						}
					}
					union() {
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.1, -7.6], [-3.1, -7.5], [-4.6, -6.3], [-4.6, -6.0], [-3.4, -6.0], [-3.4, 0], [-5.6, 0], [-5.6, -7.6]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.1, -7.6], [3.1, -7.5], [4.6, -6.3], [4.6, -6.0], [3.4, -6.0], [3.4, 0], [5.6, 0], [5.6, -7.6]]);
								}
							}
						}
						translate(v = [-1.7999999999999998, -0.1, -7.6]) {
							cube(size = [3.5999999999999996, 10.2, 8.1]);
						}
						translate(v = [0, 10.1, 0.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 1.7999999999999998);
							}
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "26", valign = "center");
								}
							}
						}
					}
				}
			}
		}
	}
	union();
}
