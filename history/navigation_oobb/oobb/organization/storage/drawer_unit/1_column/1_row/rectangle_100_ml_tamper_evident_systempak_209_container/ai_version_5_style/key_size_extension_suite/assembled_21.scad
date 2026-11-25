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
						translate(v = [-4.25, -0.25, -0.1]) {
							cube(size = [8.5, 10.5, 7.7]);
						}
						translate(v = [-6.1, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 1.8, text = "21", valign = "center");
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
		translate(v = [0, 1.7999999999999998, -3.4800000000000004]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-9.12, 0, -3.2800000000000002]) {
							cube(size = [17.28, 6.4, 6.5600000000000005]);
						}
					}
					union() {
						translate(v = [0, 6.5, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 6.6000000000000005) {
									polygon(points = [[-5.92, -2.24], [4.32, -2.24], [4.32, -3.28], [4.8, -3.28], [8.26, -1.879524], [8.26, -3.38], [-5.92, -3.38]]);
								}
							}
						}
						translate(v = [0, 6.5, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 6.6000000000000005) {
									polygon(points = [[-5.92, 2.24], [4.32, 2.24], [4.32, 3.28], [4.8, 3.28], [8.26, 1.879524], [8.26, 3.38], [-5.92, 3.38]]);
								}
							}
						}
						translate(v = [0, 6.5, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 6.6000000000000005) {
									polygon(points = [[-5.92, 0.32], [-5.910277, 0.431135], [-5.881403, 0.538893], [-5.834256, 0.64], [-5.770268, 0.731384], [-5.691384, 0.810268], [-5.6, 0.874256], [-5.498893, 0.921403], [-5.391135, 0.950277], [-5.28, 0.96], [8.26, 0.96], [8.26, -0.96], [-5.28, -0.96], [-5.391135, -0.950277], [-5.498893, -0.921403], [-5.6, -0.874256], [-5.691384, -0.810268], [-5.770268, -0.731384], [-5.834256, -0.64], [-5.881403, -0.538893], [-5.910277, -0.431135], [-5.92, -0.32]]);
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
