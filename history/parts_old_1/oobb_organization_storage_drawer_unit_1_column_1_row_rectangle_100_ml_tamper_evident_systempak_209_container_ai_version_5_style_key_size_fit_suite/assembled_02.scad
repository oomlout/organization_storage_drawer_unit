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
						translate(v = [-2.75, -0.25, -0.1]) {
							cube(size = [5.5, 10.5, 7.7]);
						}
						translate(v = [-5.5, 8.5, 6.9]) {
							linear_extrude(height = 0.7) {
								text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "2", valign = "center");
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
						translate(v = [-2.5, 0, -13.05]) {
							cube(size = [5.0, 10.0, 13.15]);
						}
					}
					union() {
						translate(v = [-2.6, 2.7, -11.450000000000001]) {
							cube(size = [5.2, 4.6, 3.4]);
						}
						translate(v = [0, 9.4, 24.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "2", valign = "center");
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
		translate(v = [0, 3.0, -2.25]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.7, 0, -2.05]) {
							cube(size = [10.8, 4.0, 4.1]);
						}
					}
					union() {
						translate(v = [0, 4.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.2) {
									polygon(points = [[-3.7, -1.4], [2.7, -1.4], [2.7, -2.05], [3.0, -2.05], [5.1, -1.2], [5.2, -1.2], [5.2, -2.15], [-3.7, -2.15]]);
								}
							}
						}
						translate(v = [0, 4.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.2) {
									polygon(points = [[-3.7, 1.4], [2.7, 1.4], [2.7, 2.05], [3.0, 2.05], [5.1, 1.2], [5.2, 1.2], [5.2, 2.15], [-3.7, 2.15]]);
								}
							}
						}
						translate(v = [0, 4.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.2) {
									polygon(points = [[-3.7, 0.2], [-3.693923, 0.269459], [-3.675877, 0.336808], [-3.64641, 0.4], [-3.606418, 0.457115], [-3.557115, 0.506418], [-3.5, 0.54641], [-3.436808, 0.575877], [-3.369459, 0.593923], [-3.3, 0.6], [5.2, 0.6], [5.2, -0.6], [-3.3, -0.6], [-3.369459, -0.593923], [-3.436808, -0.575877], [-3.5, -0.54641], [-3.557115, -0.506418], [-3.606418, -0.457115], [-3.64641, -0.4], [-3.675877, -0.336808], [-3.693923, -0.269459], [-3.7, -0.2]]);
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
