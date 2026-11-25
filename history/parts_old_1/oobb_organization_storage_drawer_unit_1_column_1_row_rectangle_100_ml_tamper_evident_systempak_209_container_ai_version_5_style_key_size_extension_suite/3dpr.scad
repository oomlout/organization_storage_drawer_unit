$fn = 50;

difference() {
	union() {
		translate(v = [-48, 0, 0]) {
			rotate(a = [0, 0, 0]) {
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
										translate(v = [-3.875, -0.25, -0.1]) {
											cube(size = [7.75, 10.5, 7.7]);
										}
										translate(v = [-6.1, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 1.8, text = "20", valign = "center");
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
						translate(v = [12, 8.64875, 0]) {
							rotate(a = [90, 0, 0]) {
								difference() {
									union() {
										translate(v = [-5.5, 0, 0]) {
											cube(size = [11.0, 10.0, 32.0]);
										}
										translate(v = [-3.625, 0, -14.702499999999999]) {
											cube(size = [7.25, 10.0, 14.802499999999998]);
										}
									}
									union() {
										translate(v = [-3.725, 1.7000000000000002, -13.1025]) {
											cube(size = [7.45, 6.6, 4.859999999999999]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "20", valign = "center");
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
										translate(v = [-8.265, 0, -2.9724999999999997]) {
											cube(size = [15.66, 5.8, 5.944999999999999]);
										}
									}
									union() {
										translate(v = [0, 5.8999999999999995, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 6.0) {
													polygon(points = [[-5.365, -2.03], [3.915, -2.03], [3.915, -2.9725], [4.35, -2.9725], [7.495, -1.699524], [7.495, -3.0725], [-5.365, -3.0725]]);
												}
											}
										}
										translate(v = [0, 5.8999999999999995, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 6.0) {
													polygon(points = [[-5.365, 2.03], [3.915, 2.03], [3.915, 2.9725], [4.35, 2.9725], [7.495, 1.699524], [7.495, 3.0725], [-5.365, 3.0725]]);
												}
											}
										}
										translate(v = [0, 5.8999999999999995, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 6.0) {
													polygon(points = [[-5.365, 0.29], [-5.356188, 0.390716], [-5.330022, 0.488372], [-5.287295, 0.58], [-5.229306, 0.662817], [-5.157817, 0.734306], [-5.075, 0.792295], [-4.983372, 0.835022], [-4.885716, 0.861188], [-4.785, 0.87], [7.495, 0.87], [7.495, -0.87], [-4.785, -0.87], [-4.885716, -0.861188], [-4.983372, -0.835022], [-5.075, -0.792295], [-5.157817, -0.734306], [-5.229306, -0.662817], [-5.287295, -0.58], [-5.330022, -0.488372], [-5.356188, -0.390716], [-5.365, -0.29]]);
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
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
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
										translate(v = [-4.25, -0.25, -0.1]) {
											cube(size = [8.5, 10.5, 7.7]);
										}
										translate(v = [-6.1, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 1.8, text = "21", valign = "center");
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
						translate(v = [12, 8.39, 0]) {
							rotate(a = [90, 0, 0]) {
								difference() {
									union() {
										translate(v = [-5.5, 0, 0]) {
											cube(size = [11.0, 10.0, 32.0]);
										}
										translate(v = [-4.0, 0, -15.22]) {
											cube(size = [8.0, 10.0, 15.32]);
										}
									}
									union() {
										translate(v = [-4.1, 1.4, -13.620000000000001]) {
											cube(size = [8.2, 7.2, 5.28]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 4.0, text = "21", valign = "center");
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
										translate(v = [-9.12, 0, -3.2800000000000002]) {
											cube(size = [17.28, 6.4, 6.5600000000000005]);
										}
									}
									union() {
										translate(v = [0, 6.5, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 6.6000000000000005) {
													polygon(points = [[-5.92, -2.24], [4.32, -2.24], [4.32, -3.28], [4.8, -3.28], [8.26, -1.879524], [8.26, -3.38], [-5.92, -3.38]]);
												}
											}
										}
										translate(v = [0, 6.5, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 6.6000000000000005) {
													polygon(points = [[-5.92, 2.24], [4.32, 2.24], [4.32, 3.28], [4.8, 3.28], [8.26, 1.879524], [8.26, 3.38], [-5.92, 3.38]]);
												}
											}
										}
										translate(v = [0, 6.5, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 6.6000000000000005) {
													polygon(points = [[-5.92, 0.32], [-5.910277, 0.431135], [-5.881403, 0.538893], [-5.834256, 0.64], [-5.770268, 0.731384], [-5.691384, 0.810268], [-5.6, 0.874256], [-5.498893, 0.921403], [-5.391135, 0.950277], [-5.28, 0.96], [8.26, 0.96], [8.26, -0.96], [-5.28, -0.96], [-5.391135, -0.950277], [-5.498893, -0.921403], [-5.6, -0.874256], [-5.691384, -0.810268], [-5.770268, -0.731384], [-5.834256, -0.64], [-5.881403, -0.538893], [-5.910277, -0.431135], [-5.92, -0.32]]);
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
		translate(v = [48, 0, 0]) {
			rotate(a = [0, 0, 0]) {
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
						translate(v = [-12, -18, 0]) {
							rotate(a = [90, 0, 0]) {
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
			}
		}
	}
	union();
}
