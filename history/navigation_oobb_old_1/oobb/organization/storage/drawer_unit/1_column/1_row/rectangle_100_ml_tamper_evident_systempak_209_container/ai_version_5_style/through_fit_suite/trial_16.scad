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
						translate(v = [-3.175, -0.25, -0.1]) {
							cube(size = [6.35, 10.5, 7.7]);
						}
						translate(v = [-5.5, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "16", valign = "center");
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
		translate(v = [12, 9.21625, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 32.0]);
						}
						translate(v = [0, 10.0, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.0) {
									polygon(points = [[-2.875, -13.5675], [2.875, -13.5675], [2.875, -6.0], [3.15, 0], [3.15, 0.1], [-3.15, 0.1], [-3.15, 0], [-2.875, -6.0]]);
								}
							}
						}
					}
					union() {
						translate(v = [-2.975, 2.4000000000000004, -11.9675]) {
							cube(size = [5.95, 5.199999999999999, 3.8200000000000003]);
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "16", valign = "center");
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
						translate(v = [-6.555, 0, -2.3575]) {
							cube(size = [12.42, 4.6, 4.715]);
						}
					}
					union() {
						translate(v = [0, 4.699999999999999, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.8) {
									polygon(points = [[-4.255, -1.61], [3.105, -1.61], [3.105, -2.3575], [3.45, -2.3575], [5.865, -1.38], [5.965, -1.38], [5.965, -2.4575], [-4.255, -2.4575]]);
								}
							}
						}
						translate(v = [0, 4.699999999999999, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.8) {
									polygon(points = [[-4.255, 1.61], [3.105, 1.61], [3.105, 2.3575], [3.45, 2.3575], [5.865, 1.38], [5.965, 1.38], [5.965, 2.4575], [-4.255, 2.4575]]);
								}
							}
						}
						translate(v = [0, 4.699999999999999, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.8) {
									polygon(points = [[-4.255, 0.23], [-4.248012, 0.309878], [-4.227259, 0.387329], [-4.193372, 0.46], [-4.14738, 0.525682], [-4.090682, 0.58238], [-4.025, 0.628372], [-3.952329, 0.662259], [-3.874878, 0.683012], [-3.795, 0.69], [5.965, 0.69], [5.965, -0.69], [-3.795, -0.69], [-3.874878, -0.683012], [-3.952329, -0.662259], [-4.025, -0.628372], [-4.090682, -0.58238], [-4.14738, -0.525682], [-4.193372, -0.46], [-4.227259, -0.387329], [-4.248012, -0.309878], [-4.255, -0.23]]);
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
