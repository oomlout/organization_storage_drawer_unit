$fn = 50;

difference() {
	union() {
		translate(v = [-87.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 98.5]);
						}
					}
					union() {
						translate(v = [0, 5.0, 7.0]) {
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
						translate(v = [0, 5.0, 88.5]) {
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
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
						translate(v = [0, 5.0, -0.1]) {
							cylinder(h = 11.1, r = 1.8);
						}
						translate(v = [0, 5.0, 87.5]) {
							cylinder(h = 11.1, r = 1.8);
						}
					}
				}
			}
		}
		translate(v = [-71.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [-55.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [-39.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 98.5]);
						}
					}
					union() {
						translate(v = [0, 5.0, 7.0]) {
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
						translate(v = [0, 5.0, 88.5]) {
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
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
						translate(v = [0, 5.0, -0.1]) {
							cylinder(h = 11.1, r = 1.8);
						}
						translate(v = [0, 5.0, 87.5]) {
							cylinder(h = 11.1, r = 1.8);
						}
					}
				}
			}
		}
		translate(v = [-23.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 98.5]);
						}
					}
					union() {
						translate(v = [0, 5.0, 7.0]) {
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
						translate(v = [0, 5.0, 88.5]) {
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
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [6.0, 76.8], [6.0, 21.7]]);
								}
							}
						}
						translate(v = [0, 5.0, -0.1]) {
							cylinder(h = 11.1, r = 1.8);
						}
						translate(v = [0, 5.0, 87.5]) {
							cylinder(h = 11.1, r = 1.8);
						}
					}
				}
			}
		}
		translate(v = [-7.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [8.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [24.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [40.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [56.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [72.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [88.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 98.5]);
						}
					}
					union() {
						translate(v = [0, 5.0, 7.0]) {
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
						translate(v = [0, 5.0, 88.5]) {
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
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
						translate(v = [0, 5.0, -0.1]) {
							cylinder(h = 11.1, r = 1.8);
						}
						translate(v = [0, 5.0, 87.5]) {
							cylinder(h = 11.1, r = 1.8);
						}
					}
				}
			}
		}
		translate(v = [104.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [120.5, 4.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [-87.5, 120.0, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [4.0, 76.8], [4.0, 21.7]]);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [-71.5, 120.0, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, -6.0]) {
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
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
						translate(v = [0, 0, 98.5]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[-3.1, -6.1], [-3.1, -6.0], [-4.6, -4.8], [-4.6, -4.5], [-3.4, -4.5], [-3.4, 0], [-5.6, 0], [-5.6, -6.1]]);
												}
											}
										}
										translate(v = [0, 10.1, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 10.2) {
													polygon(points = [[3.1, -6.1], [3.1, -6.0], [4.6, -4.8], [4.6, -4.5], [3.4, -4.5], [3.4, 0], [5.6, 0], [5.6, -6.1]]);
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
									polygon(points = [[-0.1, -6.1], [6.1, -6.1], [0, 0.0], [-0.1, 0.0]]);
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
									polygon(points = [[-0.1, 104.6], [6.1, 104.6], [0, 98.5], [-0.1, 98.5]]);
								}
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[-3.4, 98.6], [-4.0, 98.6], [-4.0, 96.45], [-3.4, 96.45]]);
								}
							}
						}
						translate(v = [-3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [0, 10.1, 0]) {
							rotate(a = [90, 0, 0]) {
								linear_extrude(height = 10.2) {
									polygon(points = [[3.4, 98.6], [4.0, 98.6], [4.0, 96.45], [3.4, 96.45]]);
								}
							}
						}
						translate(v = [3.6999999999999997, 10.1, 96.5]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.3);
							}
						}
						translate(v = [-5.6, 0, 0]) {
							rotate(a = [90, 0, 90]) {
								linear_extrude(height = 11.2) {
									polygon(points = [[10.1, 14.5], [10.1, 84.0], [6.0, 76.8], [6.0, 21.7]]);
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
