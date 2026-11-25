$fn = 50;

union() {
	difference() {
		union() {
			translate(v = [0, 0, 3]) {
				rotate(a = [0, 0, 0]) {
					difference() {
						union() {
							#translate(v = [0, 0, -3.0]) {
								cylinder(h = 3, r = 1.5);
							}
							#translate(v = [0, 0, -1.9]) {
								cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
							}
							#translate(v = [0, 0, -3.0]) {
								cylinder(h = 3, r = 1.8);
							}
							#translate(v = [0, 0, -3.0]) {
								cylinder(h = 3, r = 1.5);
							}
						}
						union();
					}
				}
			}
			hull() {
				translate(v = [-39.75, 9.75, 0]) {
					cylinder(h = 111.5, r = 5);
				}
				translate(v = [39.75, 9.75, 0]) {
					cylinder(h = 111.5, r = 5);
				}
				translate(v = [-39.75, -9.75, 0]) {
					cylinder(h = 111.5, r = 5);
				}
				translate(v = [39.75, -9.75, 0]) {
					cylinder(h = 111.5, r = 5);
				}
			}
		}
		union() {
			##hull() {
				translate(v = [-39.75, 9.75, 0]) {
					cylinder(h = 111.5, r = 4);
				}
				translate(v = [39.75, 9.75, 0]) {
					cylinder(h = 111.5, r = 4);
				}
				translate(v = [-39.75, -9.75, 0]) {
					cylinder(h = 111.5, r = 4);
				}
				translate(v = [39.75, -9.75, 0]) {
					cylinder(h = 111.5, r = 4);
				}
			}
		}
	}
	union() {
		#translate(v = [0.0, -11.75, 0]) {
			#hull() {
				translate(v = [-25.5, 1.0, 0]) {
					cylinder(h = 1.5, r = 2.5);
				}
				translate(v = [25.5, 1.0, 0]) {
					cylinder(h = 1.5, r = 2.5);
				}
				translate(v = [-25.5, -1.0, 0]) {
					cylinder(h = 1.5, r = 2.5);
				}
				translate(v = [25.5, -1.0, 0]) {
					cylinder(h = 1.5, r = 2.5);
				}
			}
		}
	}
}
