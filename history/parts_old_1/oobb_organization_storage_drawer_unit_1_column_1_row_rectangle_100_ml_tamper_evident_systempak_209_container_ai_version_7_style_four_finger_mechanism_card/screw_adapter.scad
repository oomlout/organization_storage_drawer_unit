$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-4.75, 4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
							translate(v = [4.75, 4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
							translate(v = [-4.75, -4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
							translate(v = [4.75, -4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
						}
						translate(v = [-2.85, -2.05, 2.35]) {
							cube(size = [5.7, 4.1, 5.55]);
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -2.55, 2.4]) {
							cube(size = [3.8, 5.1, 5.6]);
						}
						translate(v = [0, 2.15, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.3) {
									polygon(points = [[-3.0500000000000003, 7.300000000000001], [-2.25, 8.1], [-3.0500000000000003, 8.1]]);
								}
							}
						}
						translate(v = [0, 2.15, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.3) {
									polygon(points = [[3.0500000000000003, 7.300000000000001], [2.25, 8.1], [3.0500000000000003, 8.1]]);
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
