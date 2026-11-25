$fn = 50;

difference() {
	union() {
		translate(v = [-48, 54, 0]) {
			rotate(a = [0, 0, 0]) {
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
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "1", valign = "center");
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
										translate(v = [-2.5, 0, -12.95]) {
											cube(size = [5.0, 10.0, 13.049999999999999]);
										}
									}
									union() {
										translate(v = [-2.6, 2.8, -11.35]) {
											cube(size = [5.2, 4.4, 3.1999999999999997]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "1", valign = "center");
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
			}
		}
		translate(v = [0, 54, 0]) {
			rotate(a = [0, 0, 0]) {
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
			}
		}
		translate(v = [48, 54, 0]) {
			rotate(a = [0, 0, 0]) {
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
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "3", valign = "center");
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
										translate(v = [-2.5, 0, -13.15]) {
											cube(size = [5.0, 10.0, 13.25]);
										}
									}
									union() {
										translate(v = [-2.6, 2.6, -11.55]) {
											cube(size = [5.2, 4.8, 3.5999999999999996]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "3", valign = "center");
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
			}
		}
		translate(v = [-48, 0, 0]) {
			rotate(a = [0, 0, 0]) {
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
										translate(v = [-3.125, -0.25, -0.1]) {
											cube(size = [6.25, 10.5, 7.7]);
										}
										translate(v = [-5.5, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "4", valign = "center");
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
										translate(v = [-2.875, 0, -13.467499999999998]) {
											cube(size = [5.75, 10.0, 13.567499999999997]);
										}
									}
									union() {
										translate(v = [-2.975, 2.5, -11.867499999999998]) {
											cube(size = [5.95, 5.0, 3.62]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "4", valign = "center");
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
						translate(v = [0, 2.7, -2.557499999999999]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-6.555, 0, -2.3575]) {
											cube(size = [12.42, 4.6, 4.715]);
										}
									}
									union() {
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, -1.61], [3.105, -1.61], [3.105, -2.3575], [3.45, -2.3575], [5.865, -1.38], [5.965, -1.38], [5.965, -2.4575], [-4.255, -2.4575]]);
												}
											}
										}
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, 1.61], [3.105, 1.61], [3.105, 2.3575], [3.45, 2.3575], [5.865, 1.38], [5.965, 1.38], [5.965, 2.4575], [-4.255, 2.4575]]);
												}
											}
										}
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, 0.23], [-4.248012, 0.309878], [-4.227259, 0.387329], [-4.193372, 0.46], [-4.14738, 0.525682], [-4.090682, 0.58238], [-4.025, 0.628372], [-3.952329, 0.662259], [-3.874878, 0.683012], [-3.795, 0.69], [5.965, 0.69], [5.965, -0.69], [-3.795, -0.69], [-3.874878, -0.683012], [-3.952329, -0.662259], [-4.025, -0.628372], [-4.090682, -0.58238], [-4.14738, -0.525682], [-4.193372, -0.46], [-4.227259, -0.387329], [-4.248012, -0.309878], [-4.255, -0.23]]);
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
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-7.5, -2.0, 0]) {
											cube(size = [15.0, 14.0, 7.5]);
										}
									}
									union() {
										translate(v = [-3.125, -0.25, -0.1]) {
											cube(size = [6.25, 10.5, 7.7]);
										}
										translate(v = [-5.5, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "5", valign = "center");
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
										translate(v = [-2.875, 0, -13.567499999999999]) {
											cube(size = [5.75, 10.0, 13.667499999999999]);
										}
									}
									union() {
										translate(v = [-2.975, 2.4000000000000004, -11.9675]) {
											cube(size = [5.95, 5.199999999999999, 3.8200000000000003]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "5", valign = "center");
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
						translate(v = [0, 2.7, -2.557499999999999]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-6.555, 0, -2.3575]) {
											cube(size = [12.42, 4.6, 4.715]);
										}
									}
									union() {
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, -1.61], [3.105, -1.61], [3.105, -2.3575], [3.45, -2.3575], [5.865, -1.38], [5.965, -1.38], [5.965, -2.4575], [-4.255, -2.4575]]);
												}
											}
										}
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, 1.61], [3.105, 1.61], [3.105, 2.3575], [3.45, 2.3575], [5.865, 1.38], [5.965, 1.38], [5.965, 2.4575], [-4.255, 2.4575]]);
												}
											}
										}
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, 0.23], [-4.248012, 0.309878], [-4.227259, 0.387329], [-4.193372, 0.46], [-4.14738, 0.525682], [-4.090682, 0.58238], [-4.025, 0.628372], [-3.952329, 0.662259], [-3.874878, 0.683012], [-3.795, 0.69], [5.965, 0.69], [5.965, -0.69], [-3.795, -0.69], [-3.874878, -0.683012], [-3.952329, -0.662259], [-4.025, -0.628372], [-4.090682, -0.58238], [-4.14738, -0.525682], [-4.193372, -0.46], [-4.227259, -0.387329], [-4.248012, -0.309878], [-4.255, -0.23]]);
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
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-7.5, -2.0, 0]) {
											cube(size = [15.0, 14.0, 7.5]);
										}
									}
									union() {
										translate(v = [-3.125, -0.25, -0.1]) {
											cube(size = [6.25, 10.5, 7.7]);
										}
										translate(v = [-5.5, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "6", valign = "center");
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
										translate(v = [-2.875, 0, -13.667499999999999]) {
											cube(size = [5.75, 10.0, 13.767499999999998]);
										}
									}
									union() {
										translate(v = [-2.975, 2.3000000000000003, -12.067499999999999]) {
											cube(size = [5.95, 5.3999999999999995, 4.0200000000000005]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "6", valign = "center");
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
						translate(v = [0, 2.7, -2.557499999999999]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-6.555, 0, -2.3575]) {
											cube(size = [12.42, 4.6, 4.715]);
										}
									}
									union() {
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, -1.61], [3.105, -1.61], [3.105, -2.3575], [3.45, -2.3575], [5.865, -1.38], [5.965, -1.38], [5.965, -2.4575], [-4.255, -2.4575]]);
												}
											}
										}
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, 1.61], [3.105, 1.61], [3.105, 2.3575], [3.45, 2.3575], [5.865, 1.38], [5.965, 1.38], [5.965, 2.4575], [-4.255, 2.4575]]);
												}
											}
										}
										translate(v = [0, 4.699999999999999, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.8) {
													polygon(points = [[-4.255, 0.23], [-4.248012, 0.309878], [-4.227259, 0.387329], [-4.193372, 0.46], [-4.14738, 0.525682], [-4.090682, 0.58238], [-4.025, 0.628372], [-3.952329, 0.662259], [-3.874878, 0.683012], [-3.795, 0.69], [5.965, 0.69], [5.965, -0.69], [-3.795, -0.69], [-3.874878, -0.683012], [-3.952329, -0.662259], [-4.025, -0.628372], [-4.090682, -0.58238], [-4.14738, -0.525682], [-4.193372, -0.46], [-4.227259, -0.387329], [-4.248012, -0.309878], [-4.255, -0.23]]);
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
		translate(v = [-48, -54, 0]) {
			rotate(a = [0, 0, 0]) {
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
										translate(v = [-3.5, -0.25, -0.1]) {
											cube(size = [7.0, 10.5, 7.7]);
										}
										translate(v = [-5.5, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "7", valign = "center");
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
										translate(v = [-3.25, 0, -13.985]) {
											cube(size = [6.5, 10.0, 14.084999999999999]);
										}
									}
									union() {
										translate(v = [-3.35, 2.1999999999999997, -12.385]) {
											cube(size = [6.7, 5.6000000000000005, 4.04]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "7", valign = "center");
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
						translate(v = [0, 2.4, -2.865]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-7.41, 0, -2.665]) {
											cube(size = [14.04, 5.2, 5.33]);
										}
									}
									union() {
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, -1.82], [3.51, -1.82], [3.51, -2.665], [3.9, -2.665], [6.63, -1.56], [6.73, -1.56], [6.73, -2.765], [-4.81, -2.765]]);
												}
											}
										}
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, 1.82], [3.51, 1.82], [3.51, 2.665], [3.9, 2.665], [6.63, 1.56], [6.73, 1.56], [6.73, 2.765], [-4.81, 2.765]]);
												}
											}
										}
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, 0.26], [-4.8021, 0.350297], [-4.77864, 0.43785], [-4.740333, 0.52], [-4.688343, 0.59425], [-4.62425, 0.658343], [-4.55, 0.710333], [-4.46785, 0.74864], [-4.380297, 0.7721], [-4.29, 0.78], [6.73, 0.78], [6.73, -0.78], [-4.29, -0.78], [-4.380297, -0.7721], [-4.46785, -0.74864], [-4.55, -0.710333], [-4.62425, -0.658343], [-4.688343, -0.59425], [-4.740333, -0.52], [-4.77864, -0.43785], [-4.8021, -0.350297], [-4.81, -0.26]]);
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
		translate(v = [0, -54, 0]) {
			rotate(a = [0, 0, 0]) {
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
										translate(v = [-3.5, -0.25, -0.1]) {
											cube(size = [7.0, 10.5, 7.7]);
										}
										translate(v = [-5.5, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "8", valign = "center");
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
										translate(v = [-3.25, 0, -14.085]) {
											cube(size = [6.5, 10.0, 14.185]);
										}
									}
									union() {
										translate(v = [-3.35, 2.1, -12.485000000000001]) {
											cube(size = [6.7, 5.8, 4.24]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "8", valign = "center");
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
						translate(v = [0, 2.4, -2.865]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-7.41, 0, -2.665]) {
											cube(size = [14.04, 5.2, 5.33]);
										}
									}
									union() {
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, -1.82], [3.51, -1.82], [3.51, -2.665], [3.9, -2.665], [6.63, -1.56], [6.73, -1.56], [6.73, -2.765], [-4.81, -2.765]]);
												}
											}
										}
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, 1.82], [3.51, 1.82], [3.51, 2.665], [3.9, 2.665], [6.63, 1.56], [6.73, 1.56], [6.73, 2.765], [-4.81, 2.765]]);
												}
											}
										}
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, 0.26], [-4.8021, 0.350297], [-4.77864, 0.43785], [-4.740333, 0.52], [-4.688343, 0.59425], [-4.62425, 0.658343], [-4.55, 0.710333], [-4.46785, 0.74864], [-4.380297, 0.7721], [-4.29, 0.78], [6.73, 0.78], [6.73, -0.78], [-4.29, -0.78], [-4.380297, -0.7721], [-4.46785, -0.74864], [-4.55, -0.710333], [-4.62425, -0.658343], [-4.688343, -0.59425], [-4.740333, -0.52], [-4.77864, -0.43785], [-4.8021, -0.350297], [-4.81, -0.26]]);
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
		translate(v = [48, -54, 0]) {
			rotate(a = [0, 0, 0]) {
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
										translate(v = [-3.5, -0.25, -0.1]) {
											cube(size = [7.0, 10.5, 7.7]);
										}
										translate(v = [-5.5, 8.5, 6.9]) {
											linear_extrude(height = 0.7) {
												text(font = "Arial:style=Bold", halign = "center", size = 2.5, text = "9", valign = "center");
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
										translate(v = [-3.25, 0, -14.185]) {
											cube(size = [6.5, 10.0, 14.285]);
										}
									}
									union() {
										translate(v = [-3.35, 2.0, -12.585]) {
											cube(size = [6.7, 6.0, 4.44]);
										}
										translate(v = [0, 9.4, 24.0]) {
											rotate(a = [-90, 0, 0]) {
												linear_extrude(height = 0.7) {
													text(font = "Arial:style=Bold", halign = "center", size = 5.0, text = "9", valign = "center");
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
						translate(v = [0, 2.4, -2.865]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-7.41, 0, -2.665]) {
											cube(size = [14.04, 5.2, 5.33]);
										}
									}
									union() {
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, -1.82], [3.51, -1.82], [3.51, -2.665], [3.9, -2.665], [6.63, -1.56], [6.73, -1.56], [6.73, -2.765], [-4.81, -2.765]]);
												}
											}
										}
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, 1.82], [3.51, 1.82], [3.51, 2.665], [3.9, 2.665], [6.63, 1.56], [6.73, 1.56], [6.73, 2.765], [-4.81, 2.765]]);
												}
											}
										}
										translate(v = [0, 5.3, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.4) {
													polygon(points = [[-4.81, 0.26], [-4.8021, 0.350297], [-4.77864, 0.43785], [-4.740333, 0.52], [-4.688343, 0.59425], [-4.62425, 0.658343], [-4.55, 0.710333], [-4.46785, 0.74864], [-4.380297, 0.7721], [-4.29, 0.78], [6.73, 0.78], [6.73, -0.78], [-4.29, -0.78], [-4.380297, -0.7721], [-4.46785, -0.74864], [-4.55, -0.710333], [-4.62425, -0.658343], [-4.688343, -0.59425], [-4.740333, -0.52], [-4.77864, -0.43785], [-4.8021, -0.350297], [-4.81, -0.26]]);
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
