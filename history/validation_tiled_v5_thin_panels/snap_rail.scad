$fn = 50;

difference() {
	union() {
		translate(v = [0, 52.25, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -3.0]) {
							cube(size = [11.0, 10.0, 110.5]);
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
													polygon(points = [[-3.1, -3.1], [-3.1, -3.0], [-4.6, -1.8], [-4.6, -1.5], [-3.4, -1.5], [-3.4, 0], [-5.6, 0], [-5.6, -3.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -3.1], [3.1, -3.0], [4.6, -1.8], [4.6, -1.5], [3.4, -1.5], [3.4, 0], [5.6, 0], [5.6, -3.1]]);
												}
											}
										}
										translate(v = [-1.5999999999999999, -0.1, -3.1]) {
											cube(size = [3.1999999999999997, 10.2, 8.1]);
										}
										translate(v = [0, 10.1, 5.0]) {
											rotate(a = [90, 0, 0]) {
												cylinder(h = 10.2, r = 1.5999999999999999);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, 104.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -3.1], [-3.1, -3.0], [-4.6, -1.8], [-4.6, -1.5], [-3.4, -1.5], [-3.4, 0], [-5.6, 0], [-5.6, -3.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -3.1], [3.1, -3.0], [4.6, -1.8], [4.6, -1.5], [3.4, -1.5], [3.4, 0], [5.6, 0], [5.6, -3.1]]);
												}
											}
										}
										translate(v = [-1.5999999999999999, -0.1, -3.1]) {
											cube(size = [3.1999999999999997, 10.2, 8.1]);
										}
										translate(v = [0, 10.1, 5.0]) {
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
									polygon(points = [[-0.1, -3.1], [6.1, -3.1], [0, 3.0], [-0.1, 3.0]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, -0.1], [-4.0, -0.1], [-4.0, 5.05], [-3.4, 5.05]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 5.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, -0.1], [4.0, -0.1], [4.0, 5.05], [3.4, 5.05]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 5.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[-0.1, 107.6], [6.1, 107.6], [0, 101.5], [-0.1, 101.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 104.6], [-4.0, 104.6], [-4.0, 99.45], [-3.4, 99.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 99.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 104.6], [4.0, 104.6], [4.0, 99.45], [3.4, 99.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 99.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 90.0], [4.0, 82.8], [4.0, 21.7]]);
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
