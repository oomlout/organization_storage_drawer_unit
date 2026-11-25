$fn = 50;

difference() {
	union() {
		translate(v = [82.57500000000002, -57.80000000000002, 0]) {
			rotate(a = [0, 0, 0]) {
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
															translate(v = [-100.5, 131.9, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
															translate(v = [100.5, 131.9, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
															translate(v = [-100.5, -131.9, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
															translate(v = [100.5, -131.9, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
														}
													}
													union() {
														translate(v = [-95.65, 0, 4.5]) {
															rotate(a = [0, 0, 30]) {
																difference() {
																	union() {
																		translate(v = [-2.875, -5.0, -0.3]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, -0.6]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, 1.5]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, 1.8]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		linear_extrude(height = 1.5) {
																			polygon(points = [[5.914249999999999, 0.0], [2.957125, 5.1218907443321156], [-2.9571249999999982, 5.1218907443321156], [-5.914249999999999, 7.242867331857232e-16], [-2.9571250000000022, -5.121890744332115], [2.9571249999999956, -5.121890744332118]]);
																		}
																		translate(v = [-2.875, -5.0, -0.3]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, -0.6]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, 1.5]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, 1.8]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, -0.3]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, -0.6]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, 1.5]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, 1.8]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																	}
																	union();
																}
															}
														}
														translate(v = [-95.65, 94.01, 4.5]) {
															rotate(a = [0, 0, 30]) {
																difference() {
																	union() {
																		translate(v = [-2.875, -5.0, -0.3]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, -0.6]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, 1.5]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, 1.8]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		linear_extrude(height = 1.5) {
																			polygon(points = [[5.914249999999999, 0.0], [2.957125, 5.1218907443321156], [-2.9571249999999982, 5.1218907443321156], [-5.914249999999999, 7.242867331857232e-16], [-2.9571250000000022, -5.121890744332115], [2.9571249999999956, -5.121890744332118]]);
																		}
																		translate(v = [-2.875, -5.0, -0.3]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, -0.6]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, 1.5]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, 1.8]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, -0.3]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, -0.6]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																		translate(v = [-2.875, -5.0, 1.5]) {
																			cube(size = [5.75, 10, 0.3]);
																		}
																		translate(v = [-2.875, -2.875, 1.8]) {
																			cube(size = [5.75, 5.75, 0.3]);
																		}
																	}
																	union();
																}
															}
														}
														translate(v = [-5.662137425588298e-15, -12.900000000000006, 0]) {
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
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-5.662137425588298e-15, 23.64999999999999, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-4.950000000000005, 13.399999999999991, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
																				}
																			}
																		}
																	}
																}
															}
														}
														translate(v = [-5.662137425588298e-15, 49.69999999999999, 0]) {
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
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-5.662137425588298e-15, 86.25, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-4.950000000000005, 76.0, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
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
																		translate(v = [-5.662137425588298e-15, 117.54999999999998, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-4.950000000000005, 107.29999999999998, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
																				}
																			}
																		}
																	}
																}
															}
														}
														translate(v = [-5.662137425588298e-15, 129.05, 0]) {
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
														translate(v = [-89.30000000000001, -12.900000000000006, 0]) {
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
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		translate(v = [-89.30000000000001, 23.64999999999999, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.25, 13.399999999999991, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
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
																		translate(v = [-89.30000000000001, 54.94999999999999, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.25, 44.69999999999999, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
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
																		translate(v = [-89.30000000000001, 86.25, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.25, 76.0, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
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
																		translate(v = [-89.30000000000001, 117.54999999999998, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.25, 107.29999999999998, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
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
																		translate(v = [-89.30000000000001, 134.3, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.25, 124.05000000000001, 0]) {
																			rotate(a = [90, 0, 90]) {
																				linear_extrude(height = 9.899999999999999) {
																					polygon(points = [[-1, -1], [6.76, -1], [-0.24, 6.0], [-1, 6.0]]);
																				}
																			}
																		}
																	}
																}
															}
														}
														translate(v = [-44.64999999999999, -23.900000000000006, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [-44.64999999999999, -15.650000000000006, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [-44.64999999999999, -1.9000000000000057, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [-88.39999999999999, -2.4000000000000057, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.650000000000006, -23.900000000000006, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [44.650000000000006, -15.650000000000006, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [44.650000000000006, -1.9000000000000057, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [0.9000000000000057, -2.4000000000000057, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-44.64999999999999, 7.3999999999999915, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 15.649999999999991, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 29.39999999999999, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [-88.39999999999999, 28.89999999999999, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.650000000000006, 7.3999999999999915, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [44.650000000000006, 15.649999999999991, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [44.650000000000006, 29.39999999999999, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [0.9000000000000057, 28.89999999999999, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-44.64999999999999, 38.69999999999999, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 46.94999999999999, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 60.69999999999999, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [-88.39999999999999, 60.19999999999999, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.650000000000006, 38.69999999999999, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [44.650000000000006, 46.94999999999999, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [44.650000000000006, 60.69999999999999, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [0.9000000000000057, 60.19999999999999, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-44.64999999999999, 70.0, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 78.25, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 92.0, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [-88.39999999999999, 91.5, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.650000000000006, 70.0, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [44.650000000000006, 78.25, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [44.650000000000006, 92.0, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [0.9000000000000057, 91.5, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-44.64999999999999, 101.29999999999998, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 109.54999999999998, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [-44.64999999999999, 123.29999999999998, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [-88.39999999999999, 122.79999999999998, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.650000000000006, 101.29999999999998, -0.1]) {
															hull() {
																translate(v = [-42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, 5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [-42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
																translate(v = [42.75, -5.0, 0]) {
																	cylinder(h = 6.2, r = 1.0);
																}
															}
														}
														translate(v = [44.650000000000006, 109.54999999999998, -0.1]) {
															hull() {
																translate(v = [-34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, 10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [-34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
																translate(v = [34.25, -10.25, 0]) {
																	cylinder(h = 6.2, r = 4.0);
																}
															}
														}
														translate(v = [44.650000000000006, 123.29999999999998, -0.1]) {
															hull() {
																translate(v = [-43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, 0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [-43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
																translate(v = [43.25, -0.0, 0]) {
																	cylinder(h = 6.2, r = 0.5);
																}
															}
														}
														translate(v = [0.9000000000000057, 122.79999999999998, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-95.65, 0, -0.1]) {
															cylinder(h = 6.2, r = 3.25);
														}
														translate(v = [-95.65, 94.01, -0.1]) {
															cylinder(h = 6.2, r = 3.25);
														}
														translate(v = [-3.6500000000000057, 13.399999999999991, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-3.6500000000000057, 76.0, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-3.6500000000000057, 107.29999999999998, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.95000000000002, 13.399999999999991, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.95000000000002, 44.69999999999999, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.95000000000002, 76.0, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.95000000000002, 107.29999999999998, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.95000000000002, 124.05000000000001, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-368.6, -368.6, -1]) {
											cube(size = [265.70000000000005, 737.2, 4.0]);
										}
										translate(v = [5.4249999999999945, -368.6, -1]) {
											cube(size = [363.175, 737.2, 4.0]);
										}
										translate(v = [-368.6, -368.6, -1]) {
											cube(size = [737.2, 351.27500000000003, 4.0]);
										}
										translate(v = [-368.6, 134.3, -1]) {
											cube(size = [737.2, 234.3, 4.0]);
										}
										translate(v = [-5.500000000000005, -17.400000000000006, -1]) {
											cube(size = [11.0, 9.0, 4.0]);
										}
										translate(v = [-368.6, -368.6, 3.0]) {
											cube(size = [265.70000000000005, 737.2, 4.0]);
										}
										translate(v = [-5.5750000000000055, -368.6, 3.0]) {
											cube(size = [374.175, 737.2, 4.0]);
										}
										translate(v = [-368.6, -368.6, 3.0]) {
											cube(size = [737.2, 360.27500000000003, 4.0]);
										}
										translate(v = [-368.6, 134.3, 3.0]) {
											cube(size = [737.2, 234.3, 4.0]);
										}
										translate(v = [-368.6, -368.6, 6.0]) {
											cube(size = [737.2, 737.2, 7.0]);
										}
									}
								}
							}
						}
						translate(v = [-94.9, -23.325000000000006, 0]) {
							cylinder(h = 0.3, r = 5.5);
						}
						translate(v = [-95.9, -23.325000000000006, 0]) {
							cube(size = [2.0, 6.100000000000001, 0.2]);
						}
						translate(v = [-94.9, 140.3, 0]) {
							cylinder(h = 0.3, r = 5.5);
						}
						translate(v = [-95.9, 134.20000000000002, 0]) {
							cube(size = [2.0, 6.099999999999994, 0.2]);
						}
						translate(v = [-5.800000000000005, -23.325000000000006, 0]) {
							cylinder(h = 0.3, r = 5.5);
						}
						translate(v = [-6.800000000000005, -23.325000000000006, 0]) {
							cube(size = [2.0, 6.100000000000001, 0.2]);
						}
						translate(v = [-5.800000000000005, 140.3, 0]) {
							cylinder(h = 0.3, r = 5.5);
						}
						translate(v = [-6.800000000000005, 134.20000000000002, 0]) {
							cube(size = [2.0, 6.099999999999994, 0.2]);
						}
					}
					union();
				}
			}
		}
	}
	union();
}
