$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 4.5]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, -30.0, -4.5]) {
							cube(size = [11.0, 30.0, 13.0]);
						}
					}
					union() {
						translate(v = [0, -7.0, 2.0]) {
							rotate(a = [90, 0, 0]) {
								difference() {
									union() {
										translate(v = [-1.75, -3.25, -0.3]) {
											cube(size = [3.5, 6.5, 0.3]);
										}
										translate(v = [-1.75, -1.75, -0.6]) {
											cube(size = [3.5, 3.5, 0.3]);
										}
										translate(v = [-1.75, -3.25, 3]) {
											cube(size = [3.5, 6.5, 0.3]);
										}
										translate(v = [-1.75, -1.75, 3.3]) {
											cube(size = [3.5, 3.5, 0.3]);
										}
										translate(v = [0.0, -3.4619999999999997, 0]) {
											cube(size = [20, 6.9239999999999995, 3]);
										}
										linear_extrude(height = 3) {
											polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
										}
										translate(v = [-1.75, -3.25, -0.3]) {
											cube(size = [3.5, 6.5, 0.3]);
										}
										translate(v = [-1.75, -1.75, -0.6]) {
											cube(size = [3.5, 3.5, 0.3]);
										}
										translate(v = [-1.75, -3.25, 3]) {
											cube(size = [3.5, 6.5, 0.3]);
										}
										translate(v = [-1.75, -1.75, 3.3]) {
											cube(size = [3.5, 3.5, 0.3]);
										}
										translate(v = [-1.75, -3.25, -0.3]) {
											cube(size = [3.5, 6.5, 0.3]);
										}
										translate(v = [-1.75, -1.75, -0.6]) {
											cube(size = [3.5, 3.5, 0.3]);
										}
										translate(v = [-1.75, -3.25, 3]) {
											cube(size = [3.5, 6.5, 0.3]);
										}
										translate(v = [-1.75, -1.75, 3.3]) {
											cube(size = [3.5, 3.5, 0.3]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0.1, 2.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 16, r = 1.8);
							}
						}
					}
				}
			}
		}
		translate(v = [20, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-4.75, 4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
							translate(v = [4.75, 4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
							translate(v = [-4.75, -4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
							translate(v = [4.75, -4.25, 0]) {
								cylinder(h = 2.4, r = 0.75);
							}
						}
						translate(v = [-2.85, -2.05, 2.35]) {
							cube(size = [5.7, 4.1, 5.55]);
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -2.55, 2.4]) {
							cube(size = [3.8, 5.1, 5.6]);
						}
						translate(v = [0, 2.15, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.3) {
									polygon(points = [[-3.0500000000000003, 7.300000000000001], [-2.25, 8.1], [-3.0500000000000003, 8.1]]);
								}
							}
						}
						translate(v = [0, 2.15, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 4.3) {
									polygon(points = [[3.0500000000000003, 7.300000000000001], [2.25, 8.1], [3.0500000000000003, 8.1]]);
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
