$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [-90, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -4.6]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											hull() {
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.15, 9.15, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 4.6, r = 0.75);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.15, 9.15, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 4.6, r = 0.75);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.15, -9.15, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 4.6, r = 0.75);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.15, -9.15, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 4.6, r = 0.75);
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-5.0, -5.0, 0.95]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -4.8]) {
															cylinder(h = 4.8, r = 1.8);
														}
													}
													union();
												}
											}
										}
										translate(v = [-5.0, 5.0, 0.95]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -4.8]) {
															cylinder(h = 4.8, r = 1.8);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, -5.0, 0.95]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -4.8]) {
															cylinder(h = 4.8, r = 1.8);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, 5.0, 0.95]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -4.8]) {
															cylinder(h = 4.8, r = 1.8);
														}
													}
													union();
												}
											}
										}
										translate(v = [-10.0, 7.65, 1.84]) {
											cube(size = [5.55, 2.3499999999999996, 2.8600000000000003]);
										}
										translate(v = [-10.0, 7.65, 1.84]) {
											cube(size = [6.25, 2.3499999999999996, 2.8600000000000003]);
										}
										translate(v = [3.75, 7.65, 1.84]) {
											cube(size = [6.25, 2.3499999999999996, 2.8600000000000003]);
										}
										translate(v = [4.45, 7.65, 1.84]) {
											cube(size = [5.55, 2.3499999999999996, 2.8600000000000003]);
										}
									}
								}
							}
						}
						translate(v = [0, 0, 21.35]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
											hull() {
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.15, 9.15, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 15.35, r = 0.75);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.15, 9.15, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 15.35, r = 0.75);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.15, -9.15, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 15.35, r = 0.75);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.15, -9.15, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 15.35, r = 0.75);
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-5.0, 5.0, 3.0]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														linear_extrude(height = 53.0) {
															polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
														}
														translate(v = [-1.75, -3.25, -0.3]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, -0.6]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
														translate(v = [-1.75, -3.25, 53.0]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, 53.3]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
													}
													union();
												}
											}
										}
										translate(v = [-5.0, -5.0, 3.0]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														linear_extrude(height = 53.0) {
															polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
														}
														translate(v = [-1.75, -3.25, -0.3]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, -0.6]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
														translate(v = [-1.75, -3.25, 53.0]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, 53.3]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, 5.0, 3.0]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														linear_extrude(height = 53.0) {
															polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
														}
														translate(v = [-1.75, -3.25, -0.3]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, -0.6]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
														translate(v = [-1.75, -3.25, 53.0]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, 53.3]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, -5.0, 3.0]) {
											rotate(a = [180, 0, 0]) {
												difference() {
													union() {
														linear_extrude(height = 53.0) {
															polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
														}
														translate(v = [-1.75, -3.25, -0.3]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, -0.6]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
														translate(v = [-1.75, -3.25, 53.0]) {
															cube(size = [3.5, 6.5, 0.3]);
														}
														translate(v = [-1.75, -1.75, 53.3]) {
															cube(size = [3.5, 3.5, 0.3]);
														}
													}
													union();
												}
											}
										}
										translate(v = [-10.0, -10.0, -0.01]) {
											cube(size = [3.25, 5.35, 15.459999999999999]);
										}
										translate(v = [-10.0, -10.0, -0.01]) {
											cube(size = [6.25, 5.35, 15.459999999999999]);
										}
										translate(v = [-10.0, -10.0, 2.99]) {
											cube(size = [3.25, 3.3499999999999996, 12.459999999999999]);
										}
										translate(v = [-10.0, -10.0, 2.99]) {
											cube(size = [6.25, 3.3499999999999996, 12.459999999999999]);
										}
										translate(v = [3.75, -10.0, -0.01]) {
											cube(size = [6.25, 5.35, 15.459999999999999]);
										}
										translate(v = [3.75, -10.0, 2.99]) {
											cube(size = [6.25, 3.3499999999999996, 12.459999999999999]);
										}
										translate(v = [6.75, -10.0, -0.01]) {
											cube(size = [3.25, 5.35, 15.459999999999999]);
										}
										translate(v = [6.75, -10.0, 2.99]) {
											cube(size = [3.25, 3.3499999999999996, 12.459999999999999]);
										}
										translate(v = [-5.0, 5.0, -0.2]) {
											cylinder(h = 15.75, r = 1.8);
										}
										translate(v = [-5.0, -5.0, -0.2]) {
											cylinder(h = 15.75, r = 1.8);
										}
										translate(v = [5.0, 5.0, -0.2]) {
											cylinder(h = 15.75, r = 1.8);
										}
										translate(v = [5.0, -5.0, -0.2]) {
											cylinder(h = 15.75, r = 1.8);
										}
									}
								}
							}
						}
						translate(v = [-5.0, -5.0, -3.0999999999999996]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_screw_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						translate(v = [-5.0, -5.0, 18.35]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_nut_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						translate(v = [-5.0, 5.0, -3.0999999999999996]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_screw_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						translate(v = [-5.0, 5.0, 18.35]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_nut_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						translate(v = [5.0, -5.0, -3.0999999999999996]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_screw_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						translate(v = [5.0, -5.0, 18.35]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_nut_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						translate(v = [5.0, 5.0, -3.0999999999999996]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_screw_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						translate(v = [5.0, 5.0, 18.35]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.72, 0.75, 0.78]) {
											import(file = "joiner_nut_reference.stl", origin = [0, 0]);
										}
									}
									union();
								}
							}
						}
						color(alpha = 1.0, c = [0.24, 0.48, 0.54]) {
							translate(v = [-98.9000000005, -49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
							}
						}
						color(alpha = 1.0, c = [0.24, 0.48, 0.54]) {
							translate(v = [-98.9000000005, 49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
							}
						}
						color(alpha = 1.0, c = [0.24, 0.48, 0.54]) {
							translate(v = [98.9000000005, -49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
							}
						}
						color(alpha = 1.0, c = [0.24, 0.48, 0.54]) {
							translate(v = [98.9000000005, 49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
							}
						}
					}
					union() {
						translate(v = [-500, -500, 55]) {
							cube(size = [1000, 1000, 500]);
						}
						translate(v = [24, -500, -500]) {
							cube(size = [500, 1000, 1000]);
						}
						translate(v = [-524, -500, -500]) {
							cube(size = [500, 1000, 1000]);
						}
						translate(v = [-500, 24, -500]) {
							cube(size = [1000, 500, 1000]);
						}
						translate(v = [-500, -524, -500]) {
							cube(size = [1000, 500, 1000]);
						}
					}
				}
			}
		}
	}
	union();
}
