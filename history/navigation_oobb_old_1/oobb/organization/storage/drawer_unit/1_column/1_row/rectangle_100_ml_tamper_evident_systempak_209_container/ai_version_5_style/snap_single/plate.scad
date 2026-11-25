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
						translate(v = [-1.65, -0.25, 4.25]) {
							cube(size = [3.3, 10.5, 3.35]);
						}
						translate(v = [0, 4.25, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.5) {
									polygon(points = [[-1.5, -0.1], [-4.05, -0.1], [-4.05, 6.85], [-4.8, 7.6], [-0.75, 7.6], [-1.5, 6.85]]);
								}
							}
						}
						translate(v = [-7.5, 3, -0.1]) {
							cylinder(h = 7.7, r = 0.6);
						}
					}
				}
			}
		}
	}
	union();
}
