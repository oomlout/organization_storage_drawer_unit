$fn = 50;

difference() {
	union() {
		translate(v = [-28, 30, 0]) {
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
										translate(v = [-1.65, -0.25, 4.25]) {
											cube(size = [3.3, 10.5, 3.35]);
										}
										translate(v = [0, 4.25, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.5) {
													polygon(points = [[-1.5, -0.1], [-4.05, -0.1], [-4.05, 6.85], [-4.8, 7.6], [-0.75, 7.6], [-1.5, 6.85]]);
												}
											}
										}
										translate(v = [-7.5, 3, -0.1]) {
											cylinder(h = 7.7, r = 0.6);
										}
									}
								}
							}
						}
						translate(v = [12, 10.95, 0]) {
							rotate(a = [90, 0, 0]) {
								union() {
									difference() {
										union() {
											translate(v = [-5.5, 0, 0]) {
												cube(size = [11.0, 10.0, 32.0]);
											}
											translate(v = [-1.4, 0, -3.0]) {
												cube(size = [2.8, 10.0, 3.1]);
											}
										}
										union() {
											translate(v = [-5.6, -0.1, -0.1]) {
												cube(size = [4.199999999999999, 10.2, 8.1]);
											}
											translate(v = [1.4, -0.1, -0.1]) {
												cube(size = [4.199999999999999, 10.2, 8.1]);
											}
											translate(v = [5.5, 10.1, 30.0]) {
												rotate(a = [90, 0, 0]) {
													cylinder(h = 10.2, r = 0.6);
												}
											}
										}
									}
									union() {
										translate(v = [0, 4.0, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.0) {
													polygon(points = [[-2.2, -10.1], [-3.55, -10.1], [-4.45, -8.0], [-4.45, -7.7], [-3.8, -7.7], [-3.8, 8.5], [-1.1, 8.5], [-1.1, 8.0], [-1.291013, 7.983289], [-1.476222, 7.933662], [-1.65, 7.852628], [-1.807066, 7.742649], [-1.942649, 7.607066], [-2.052628, 7.45], [-2.133662, 7.276222], [-2.183289, 7.091013], [-2.2, 6.9]]);
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
		translate(v = [28, 30, 0]) {
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
										translate(v = [-1.65, -0.25, 4.25]) {
											cube(size = [3.3, 10.5, 3.35]);
										}
										translate(v = [0, 4.25, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.5) {
													polygon(points = [[-1.5, -0.1], [-4.05, -0.1], [-4.05, 6.85], [-4.8, 7.6], [-0.75, 7.6], [-1.5, 6.85]]);
												}
											}
										}
										translate(v = [0, 4.25, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.5) {
													polygon(points = [[1.5, -0.1], [4.05, -0.1], [4.05, 6.85], [4.8, 7.6], [0.75, 7.6], [1.5, 6.85]]);
												}
											}
										}
										translate(v = [-7.5, 3, -0.1]) {
											cylinder(h = 7.7, r = 0.6);
										}
										translate(v = [-7.5, 5, -0.1]) {
											cylinder(h = 7.7, r = 0.6);
										}
									}
								}
							}
						}
						translate(v = [12, 10.95, 0]) {
							rotate(a = [90, 0, 0]) {
								union() {
									difference() {
										union() {
											translate(v = [-5.5, 0, 0]) {
												cube(size = [11.0, 10.0, 32.0]);
											}
											translate(v = [-1.4, 0, -3.0]) {
												cube(size = [2.8, 10.0, 3.1]);
											}
										}
										union() {
											translate(v = [-5.6, -0.1, -0.1]) {
												cube(size = [4.199999999999999, 10.2, 12.1]);
											}
											translate(v = [1.4, -0.1, -0.1]) {
												cube(size = [4.199999999999999, 10.2, 12.1]);
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
										}
									}
									union() {
										translate(v = [0, 4.0, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.0) {
													polygon(points = [[-2.4, -10.1], [-3.55, -10.1], [-4.45, -8.0], [-4.45, -7.7], [-3.8, -7.7], [-3.8, 12.5], [-1.3, 12.5], [-1.3, 12.0], [-1.491013, 11.983289], [-1.676222, 11.933662], [-1.85, 11.852628], [-2.007066, 11.742649], [-2.142649, 11.607066], [-2.252628, 11.45], [-2.333662, 11.276222], [-2.383289, 11.091013], [-2.4, 10.9]]);
												}
											}
										}
										translate(v = [0, 4.0, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 4.0) {
													polygon(points = [[2.4, -10.1], [3.55, -10.1], [4.45, -8.0], [4.45, -7.7], [3.8, -7.7], [3.8, 12.5], [1.3, 12.5], [1.3, 12.0], [1.491013, 11.983289], [1.676222, 11.933662], [1.85, 11.852628], [2.007066, 11.742649], [2.142649, 11.607066], [2.252628, 11.45], [2.333662, 11.276222], [2.383289, 11.091013], [2.4, 10.9]]);
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
		translate(v = [-28, -30, 0]) {
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
										translate(v = [-2.75, -0.25, -0.1]) {
											cube(size = [5.5, 10.5, 7.7]);
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
						translate(v = [12, 9.5, 0]) {
							rotate(a = [90, 0, 0]) {
								difference() {
									union() {
										translate(v = [-5.5, 0, 0]) {
											cube(size = [11.0, 10.0, 32.0]);
										}
										translate(v = [-2.5, 0, -13.0]) {
											cube(size = [5.0, 10.0, 13.1]);
										}
									}
									union() {
										translate(v = [-2.6, 2.75, -11.4]) {
											cube(size = [5.2, 4.5, 3.3]);
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
		translate(v = [28, -30, 0]) {
			rotate(a = [0, 0, 0]) {
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
			}
		}
	}
	union();
}
