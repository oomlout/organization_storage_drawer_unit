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
						translate(v = [-4.625, -0.25, -0.1]) {
							cube(size = [9.25, 10.5, 7.7]);
						}
						translate(v = [-6.1, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 1.8, text = "27", valign = "center");
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
		translate(v = [12, 8.131250000000001, 0]) {
			rotate(a = [90, 0, 0]) {
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
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "27", valign = "center");
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
						translate(v = [-9.975, 0, -3.5875000000000004]) {
							cube(size = [18.65, 7.0, 7.175000000000001]);
						}
					}
					union() {
						translate(v = [0, 7.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 7.2) {
									polygon(points = [[-4.475, -2.45], [4.475, -2.45], [4.475, -3.5875], [5.0, -3.5875], [8.775, -2.059524], [8.775, -3.6875], [-4.475, -3.6875]]);
								}
							}
						}
						translate(v = [0, 7.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 7.2) {
									polygon(points = [[-4.475, 2.45], [4.475, 2.45], [4.475, 3.5875], [5.0, 3.5875], [8.775, 2.059524], [8.775, 3.6875], [-4.475, 3.6875]]);
								}
							}
						}
						translate(v = [0, 7.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 7.2) {
									polygon(points = [[-4.475, 0.35], [-4.464365, 0.471554], [-4.432785, 0.589414], [-4.381218, 0.7], [-4.311231, 0.799951], [-4.224951, 0.886231], [-4.125, 0.956218], [-4.014414, 1.007785], [-3.896554, 1.039365], [-3.775, 1.05], [8.775, 1.05], [8.775, -1.05], [-3.775, -1.05], [-3.896554, -1.039365], [-4.014414, -1.007785], [-4.125, -0.956218], [-4.224951, -0.886231], [-4.311231, -0.799951], [-4.381218, -0.7], [-4.432785, -0.589414], [-4.464365, -0.471554], [-4.475, -0.35]]);
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
