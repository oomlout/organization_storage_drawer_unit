$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, -30.0, 0]) {
							cube(size = [11.0, 39.75, 4.0]);
						}
					}
					union() {
						translate(v = [-5.6, 0, -0.1]) {
							cube(size = [2.85, 9.95, 4.2]);
						}
						translate(v = [2.75, 0, -0.1]) {
							cube(size = [2.85, 9.95, 4.2]);
						}
						translate(v = [0, 7.15, -0.1]) {
							hull() {
								translate(v = [-0.8999999999999999, 0.8, 0]) {
									cylinder(h = 4.2, r = 0.3);
								}
								translate(v = [0.8999999999999999, 0.8, 0]) {
									cylinder(h = 4.2, r = 0.3);
								}
								translate(v = [-0.8999999999999999, -0.8, 0]) {
									cylinder(h = 4.2, r = 0.3);
								}
								translate(v = [0.8999999999999999, -0.8, 0]) {
									cylinder(h = 4.2, r = 0.3);
								}
							}
						}
						translate(v = [0, -22, 3.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "54", valign = "center");
							}
						}
					}
				}
			}
		}
		translate(v = [15, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-3.5, -7.0, 0]) {
							cube(size = [7.0, 8.6, 2.0]);
						}
					}
					union() {
						translate(v = [-3.6, -7.1, -0.1]) {
							cube(size = [2.6, 7.1, 2.2]);
						}
						translate(v = [1.0, -7.1, -0.1]) {
							cube(size = [2.6, 7.1, 2.2]);
						}
					}
				}
			}
		}
	}
	union();
}
