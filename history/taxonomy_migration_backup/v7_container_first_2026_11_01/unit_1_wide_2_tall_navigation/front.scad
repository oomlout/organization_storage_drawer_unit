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
											translate(v = [-51.8500000005, 47.5000000005, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.8500000005, 47.5000000005, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [-51.8500000005, -47.5000000005, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
											translate(v = [51.8500000005, -47.5000000005, 0]) {
												cylinder(h = 6.0, r = 2.4);
											}
										}
									}
									union() {
										translate(v = [0.0, -23.900000000000006, -0.1]) {
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
										translate(v = [0.0, -15.650000000000006, -0.1]) {
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
										translate(v = [0.0, 7.399999999999995, -0.1]) {
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
										translate(v = [0.0, 15.649999999999995, -0.1]) {
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
										translate(v = [-49.2500000005, -44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-49.2500000005, 44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.2500000005, -44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.2500000005, 44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-47.25, -12.500000000000005, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [-47.25, 18.799999999999994, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, -12.500000000000005, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, 18.799999999999994, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [-47.25, -39.5, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, -39.5, -0.1]) {
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
										translate(v = [-28.0, -31.7, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [-28.1, -31.7, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[7.8999999999999995, -0.1], [7.8999999999999995, 6.1], [1.6999999999999997, 6.1]]);
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
										translate(v = [-28.0, -1.3999999999999986, 0]) {
											cube(size = [15.0, 8.8, 18.0]);
										}
									}
									union() {
										translate(v = [-28.1, -1.3999999999999986, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[8.9, -0.1], [8.9, 18.1], [1.15, 18.1], [2.0, 17.25], [2.0, 6.800000000000001]]);
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
										translate(v = [13.0, -31.7, 0]) {
											cube(size = [15.0, 7.8, 6.0]);
										}
									}
									union() {
										translate(v = [12.9, -31.7, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[7.8999999999999995, -0.1], [7.8999999999999995, 6.1], [1.6999999999999997, 6.1]]);
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
										translate(v = [13.0, -1.3999999999999986, 0]) {
											cube(size = [15.0, 8.8, 18.0]);
										}
									}
									union() {
										translate(v = [12.9, -1.3999999999999986, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 15.2) {
													polygon(points = [[8.9, -0.1], [8.9, 18.1], [1.15, 18.1], [2.0, 17.25], [2.0, 6.800000000000001]]);
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
