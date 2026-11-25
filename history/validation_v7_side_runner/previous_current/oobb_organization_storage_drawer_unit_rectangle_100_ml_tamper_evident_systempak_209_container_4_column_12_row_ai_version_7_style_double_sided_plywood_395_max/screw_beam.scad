$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, -212.0, 0]) {
							cube(size = [11.0, 212.0, 14.5]);
						}
						translate(v = [-9.5, -107.5, 0]) {
							cube(size = [19.0, 3.0, 14.5]);
						}
					}
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, -7.0, 6.5]) {
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
										translate(v = [0, 0.1, 6.5]) {
											rotate(a = [90, 0, 0]) {
												cylinder(h = 16, r = 1.8);
											}
										}
									}
									union();
								}
							}
						}
						translate(v = [0, -212.0, 0]) {
							rotate(a = [0, 0, 180]) {
								difference() {
									union() {
										translate(v = [0, -7.0, 6.5]) {
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
										translate(v = [0, 0.1, 6.5]) {
											rotate(a = [90, 0, 0]) {
												cylinder(h = 16, r = 1.8);
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
									polygon(points = [[0.1, 13.0], [-30.0, 13.0], [-31.5, 14.5], [-31.5, 14.7], [0.1, 14.7]]);
								}
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[-212.1, 13.0], [-182.0, 13.0], [-180.5, 14.5], [-180.5, 14.7], [-212.1, 14.7]]);
								}
							}
						}
						translate(v = [0, -66.5, -0.1]) {
							hull() {
								translate(v = [-0.5, 29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
								}
								translate(v = [0.5, 29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
								}
								translate(v = [-0.5, -29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
								}
								translate(v = [0.5, -29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
								}
							}
						}
						translate(v = [0, -145.5, -0.1]) {
							hull() {
								translate(v = [-0.5, 29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
								}
								translate(v = [0.5, 29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
								}
								translate(v = [-0.5, -29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
								}
								translate(v = [0.5, -29.5, 0]) {
									cylinder(h = 14.7, r = 2.0);
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
