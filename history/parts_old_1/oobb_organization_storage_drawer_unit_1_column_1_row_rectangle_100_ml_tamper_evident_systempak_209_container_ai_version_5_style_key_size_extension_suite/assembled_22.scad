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
						translate(v = [-4.625, -0.25, -0.1]) {
							cube(size = [9.25, 10.5, 7.7]);
						}
						translate(v = [-6.1, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 1.8, text = "22", valign = "center");
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
						translate(v = [-4.375, 0, -15.737499999999997]) {
							cube(size = [8.75, 10.0, 15.837499999999997]);
						}
					}
					union() {
						translate(v = [-4.475, 1.1, -14.137499999999998]) {
							cube(size = [8.95, 7.8, 5.7]);
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "22", valign = "center");
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
		translate(v = [0, 1.5, -3.787499999999998]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-9.975, 0, -3.5875000000000004]) {
							cube(size = [18.9, 7.0, 7.175000000000001]);
						}
					}
					union() {
						translate(v = [0, 7.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 7.2) {
									polygon(points = [[-6.475, -2.45], [4.725, -2.45], [4.725, -3.5875], [5.25, -3.5875], [9.025, -2.059524], [9.025, -3.6875], [-6.475, -3.6875]]);
								}
							}
						}
						translate(v = [0, 7.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 7.2) {
									polygon(points = [[-6.475, 2.45], [4.725, 2.45], [4.725, 3.5875], [5.25, 3.5875], [9.025, 2.059524], [9.025, 3.6875], [-6.475, 3.6875]]);
								}
							}
						}
						translate(v = [0, 7.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 7.2) {
									polygon(points = [[-6.475, 0.35], [-6.464365, 0.471554], [-6.432785, 0.589414], [-6.381218, 0.7], [-6.311231, 0.799951], [-6.224951, 0.886231], [-6.125, 0.956218], [-6.014414, 1.007785], [-5.896554, 1.039365], [-5.775, 1.05], [9.025, 1.05], [9.025, -1.05], [-5.775, -1.05], [-5.896554, -1.039365], [-6.014414, -1.007785], [-6.125, -0.956218], [-6.224951, -0.886231], [-6.311231, -0.799951], [-6.381218, -0.7], [-6.432785, -0.589414], [-6.464365, -0.471554], [-6.475, -0.35]]);
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
