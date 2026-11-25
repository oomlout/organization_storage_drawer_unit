$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, -30.0, 0]) {
							cube(size = [11.0, 37.99251840539369, 4.0]);
						}
					}
					union() {
						translate(v = [0, 0, -0.1]) {
							linear_extrude(height = 4.2) {
								polygon(points = [[-3.55, 0], [-3.55, 6.4], [-4.35, 6.4], [-4.35, 6.75], [-3.55, 7.892518405393692], [-3.55, 8.992518405393692], [-5.7, 8.992518405393692], [-5.7, 0]]);
							}
						}
						translate(v = [-4.0249999999999995, -5.5, -0.1]) {
							hull() {
								translate(v = [-0.0, 5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
								translate(v = [0.0, 5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
								translate(v = [-0.0, -5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
								translate(v = [0.0, -5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
							}
						}
						translate(v = [-1.15, -1.5037407973031538, -0.1]) {
							hull() {
								translate(v = [-0.0, 9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
								translate(v = [0.0, 9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
								translate(v = [-0.0, -9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
								translate(v = [0.0, -9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
							}
						}
						translate(v = [0, 0, -0.1]) {
							linear_extrude(height = 4.2) {
								polygon(points = [[3.55, 0], [3.55, 6.4], [4.35, 6.4], [4.35, 6.75], [3.55, 7.892518405393692], [3.55, 8.992518405393692], [5.7, 8.992518405393692], [5.7, 0]]);
							}
						}
						translate(v = [4.0249999999999995, -5.5, -0.1]) {
							hull() {
								translate(v = [-0.0, 5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
								translate(v = [0.0, 5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
								translate(v = [-0.0, -5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
								translate(v = [0.0, -5.975, 0]) {
									cylinder(h = 4.2, r = 0.525);
								}
							}
						}
						translate(v = [1.15, -1.5037407973031538, -0.1]) {
							hull() {
								translate(v = [-0.0, 9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
								translate(v = [0.0, 9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
								translate(v = [-0.0, -9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
								translate(v = [0.0, -9.896259202696847, 0]) {
									cylinder(h = 4.2, r = 0.5999999999999999);
								}
							}
						}
						translate(v = [-0.6000000000000001, 5.5, -0.1]) {
							cube(size = [1.2000000000000002, 3.4925184053936915, 4.2]);
						}
						translate(v = [0, -22, 3.6]) {
							linear_extrude(height = 0.5) {
								text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "48", valign = "center");
							}
						}
					}
				}
			}
		}
	}
	union();
}
