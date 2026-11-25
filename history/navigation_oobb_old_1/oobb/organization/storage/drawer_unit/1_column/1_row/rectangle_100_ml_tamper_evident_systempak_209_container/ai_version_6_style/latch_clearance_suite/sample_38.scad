$fn = 50;

difference() {
	union() {
		translate(v = [0, 4.0, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
							cube(size = [11.0, 10.0, 20.0]);
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.8, -4.65], [-4.8, -4.35], [-3.4, -4.35], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.8, -4.65], [4.8, -4.35], [3.4, -4.35], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
												}
											}
										}
										translate(v = [-1.5999999999999999, -0.1, -6.1]) {
											cube(size = [3.1999999999999997, 10.2, 8.1]);
										}
										translate(v = [0, 10.1, 2.0]) {
											rotate(a = [90, 0, 0]) {
												cylinder(h = 10.2, r = 1.5999999999999999);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, 212.0]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.8, -4.65], [-4.8, -4.35], [-3.4, -4.35], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.8, -4.65], [4.8, -4.35], [3.4, -4.35], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
												}
											}
										}
										translate(v = [-1.5999999999999999, -0.1, -6.1]) {
											cube(size = [3.1999999999999997, 10.2, 8.1]);
										}
										translate(v = [0, 10.1, 2.0]) {
											rotate(a = [90, 0, 0]) {
												cylinder(h = 10.2, r = 1.5999999999999999);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[-0.1, -6.1], [6.079166666666667, -6.1], [1.25, 0], [-0.1, 0]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, -0.1], [-4.0, -0.1], [-4.0, 2.05], [-3.4, 2.05]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 2.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, -0.1], [4.0, -0.1], [4.0, 2.05], [3.4, 2.05]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 2.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[-0.1, 218.1], [6.079166666666667, 218.1], [1.25, 212.0], [-0.1, 212.0]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 212.1], [-4.0, 212.1], [-4.0, 209.95], [-3.4, 209.95]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 210.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 212.1], [4.0, 212.1], [4.0, 209.95], [3.4, 209.95]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 210.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 197.5], [4.0, 190.3], [4.0, 21.7]]);
								}
							}
						}
						translate(v = [0, 9.5, 9.0]) {
							rotate(a = [-90, 0, 0]) {
								linear_extrude(height = 0.6) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "38", valign = "center");
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
