$fn = 50;

difference() {
	union() {
		translate(v = [-12, -5, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-7.5, -2.0, 0]) {
							cube(size = [15.0, 14.0, 7.5]);
						}
					}
					union() {
						translate(v = [-3.875, -0.25, -0.1]) {
							cube(size = [7.75, 10.5, 7.7]);
						}
						translate(v = [-6.1, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 1.8, text = "20", valign = "center");
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
		translate(v = [12, 8.64875, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 32.0]);
						}
						translate(v = [-3.625, 0, -14.702499999999999]) {
							cube(size = [7.25, 10.0, 14.802499999999998]);
						}
					}
					union() {
						translate(v = [-3.725, 1.7000000000000002, -13.1025]) {
							cube(size = [7.45, 6.6, 4.859999999999999]);
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "20", valign = "center");
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
		translate(v = [-12, -18, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-8.265, 0, -2.9724999999999997]) {
							cube(size = [15.66, 5.8, 5.944999999999999]);
						}
					}
					union() {
						translate(v = [0, 5.8999999999999995, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 6.0) {
									polygon(points = [[-5.365, -2.03], [3.915, -2.03], [3.915, -2.9725], [4.35, -2.9725], [7.495, -1.699524], [7.495, -3.0725], [-5.365, -3.0725]]);
								}
							}
						}
						translate(v = [0, 5.8999999999999995, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 6.0) {
									polygon(points = [[-5.365, 2.03], [3.915, 2.03], [3.915, 2.9725], [4.35, 2.9725], [7.495, 1.699524], [7.495, 3.0725], [-5.365, 3.0725]]);
								}
							}
						}
						translate(v = [0, 5.8999999999999995, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 6.0) {
									polygon(points = [[-5.365, 0.29], [-5.356188, 0.390716], [-5.330022, 0.488372], [-5.287295, 0.58], [-5.229306, 0.662817], [-5.157817, 0.734306], [-5.075, 0.792295], [-4.983372, 0.835022], [-4.885716, 0.861188], [-4.785, 0.87], [7.495, 0.87], [7.495, -0.87], [-4.785, -0.87], [-4.885716, -0.861188], [-4.983372, -0.835022], [-5.075, -0.792295], [-5.157817, -0.734306], [-5.229306, -0.662817], [-5.287295, -0.58], [-5.330022, -0.488372], [-5.356188, -0.390716], [-5.365, -0.29]]);
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
