$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										hull() {
											translate(v = [-51.85, 31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.85, 31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [-51.85, -31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.85, -31.85, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
										}
									}
									union() {
										translate(v = [0.0, -8.25, -0.1]) {
											hull() {
												translate(v = [-42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [0.0, 0.0, -0.1]) {
											hull() {
												translate(v = [-37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [-49.25, -29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-49.25, 29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.25, -29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.25, 29.25, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-47.25, 3.15, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, 3.15, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [-47.25, -23.85, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, -23.85, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
									}
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-28.0, -16.05, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [-28.1, -16.05, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[1.6999999999999997, -0.1], [7.8999999999999995, -0.1], [7.8999999999999995, 6.1]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [13.0, -16.05, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [12.9, -16.05, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[1.6999999999999997, -0.1], [7.8999999999999995, -0.1], [7.8999999999999995, 6.1]]);
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
			}
		}
	}
	union();
}
