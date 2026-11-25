$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-7.5, -2.0, 0]) {
							cube(size = [15.0, 14.0, 7.5]);
						}
					}
					union() {
						translate(v = [-3.5, -0.25, -0.1]) {
							cube(size = [7.0, 10.5, 7.7]);
						}
						translate(v = [-5.5, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "7", valign = "center");
							}
						}
						translate(v = [-7.5, 3, -0.1]) {
							cylinder(h = 7.7, r = 0.6);
						}
						translate(v = [-7.5, 5, -0.1]) {
							cylinder(h = 7.7, r = 0.6);
						}
						translate(v = [-7.5, 7, -0.1]) {
							cylinder(h = 7.7, r = 0.6);
						}
					}
				}
			}
		}
		translate(v = [0, 0, 7.5]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 32.0]);
						}
						translate(v = [-3.25, 0, -13.985]) {
							cube(size = [6.5, 10.0, 14.084999999999999]);
						}
					}
					union() {
						translate(v = [-3.35, 2.1999999999999997, -12.385]) {
							cube(size = [6.7, 5.6000000000000005, 4.04]);
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "7", valign = "center");
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
		translate(v = [0, 2.4, -2.865]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-7.41, 0, -2.665]) {
							cube(size = [14.04, 5.2, 5.33]);
						}
					}
					union() {
						translate(v = [0, 5.3, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 5.4) {
									polygon(points = [[-4.81, -1.82], [3.51, -1.82], [3.51, -2.665], [3.9, -2.665], [6.63, -1.56], [6.73, -1.56], [6.73, -2.765], [-4.81, -2.765]]);
								}
							}
						}
						translate(v = [0, 5.3, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 5.4) {
									polygon(points = [[-4.81, 1.82], [3.51, 1.82], [3.51, 2.665], [3.9, 2.665], [6.63, 1.56], [6.73, 1.56], [6.73, 2.765], [-4.81, 2.765]]);
								}
							}
						}
						translate(v = [0, 5.3, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 5.4) {
									polygon(points = [[-4.81, 0.26], [-4.8021, 0.350297], [-4.77864, 0.43785], [-4.740333, 0.52], [-4.688343, 0.59425], [-4.62425, 0.658343], [-4.55, 0.710333], [-4.46785, 0.74864], [-4.380297, 0.7721], [-4.29, 0.78], [6.73, 0.78], [6.73, -0.78], [-4.29, -0.78], [-4.380297, -0.7721], [-4.46785, -0.74864], [-4.55, -0.710333], [-4.62425, -0.658343], [-4.688343, -0.59425], [-4.740333, -0.52], [-4.77864, -0.43785], [-4.8021, -0.350297], [-4.81, -0.26]]);
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
