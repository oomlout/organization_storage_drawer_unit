$fn = 50;

difference() {
	union() {
		translate(v = [-12, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										hull() {
											translate(v = [-5.1, 4.6, 0]) {
												cylinder(h = 7.5, r = 2.4);
											}
											translate(v = [5.1, 4.6, 0]) {
												cylinder(h = 7.5, r = 2.4);
											}
											translate(v = [-5.1, -4.6, 0]) {
												cylinder(h = 7.5, r = 2.4);
											}
											translate(v = [5.1, -4.6, 0]) {
												cylinder(h = 7.5, r = 2.4);
											}
										}
										translate(v = [0, -5, 7.4]) {
											linear_extrude(height = 3.1) {
												polygon(points = [[-3.5, 1.5], [3.5, 1.5], [3.5, 5], [0, 8.5], [-3.5, 5]]);
											}
										}
									}
									union() {
										translate(v = [0, 0.0, 0]) {
											rotate(a = [0, 180, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -16.0]) {
															cylinder(h = 16.0, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -16.0]) {
															cylinder(h = 16.0, r = 1.8);
														}
														translate(v = [0, 0, -16.0]) {
															cylinder(h = 16.0, r = 1.5);
														}
													}
													union();
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
		translate(v = [12, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 16.0, 0]) {
							rotate(a = [90, 0, 0]) {
								difference() {
									union() {
										translate(v = [-5.5, 0, 0]) {
											cube(size = [11.0, 10.0, 32.0]);
										}
									}
									union() {
										translate(v = [0, 5.0, 5.5]) {
											rotate(a = [0, 0, 0]) {
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
										translate(v = [0, 5.0, 23.5]) {
											rotate(a = [0, 0, 0]) {
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
										translate(v = [0, 0, -0.1]) {
											linear_extrude(height = 3.3000000000000003) {
												polygon(points = [[-3.75, 1.25], [3.75, 1.25], [3.75, 5.25], [0, 9.0], [-3.75, 5.25]]);
											}
										}
										translate(v = [0, 5.0, -0.1]) {
											cylinder(h = 9.6, r = 1.8);
										}
										translate(v = [0, 0, 28.8]) {
											linear_extrude(height = 3.3000000000000003) {
												polygon(points = [[-3.75, 1.25], [3.75, 1.25], [3.75, 5.25], [0, 9.0], [-3.75, 5.25]]);
											}
										}
										translate(v = [0, 5.0, 22.5]) {
											cylinder(h = 9.6, r = 1.8);
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
