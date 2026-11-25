$fn = 50;

difference() {
	union() {
		translate(v = [120.575, 174.425, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 6.0]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														hull() {
															translate(v = [-381.1, 151.6, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
															translate(v = [381.1, 151.6, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
															translate(v = [-381.1, -151.6, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
															translate(v = [381.1, -151.6, 0]) {
																cylinder(h = 6.0, r = 2.4);
															}
														}
													}
													union() {
														translate(v = [-44.65, 146.75, 4.5]) {
															rotate(a = [0, 0, 0]) {
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
														translate(v = [-133.95, 146.75, 4.5]) {
															rotate(a = [0, 0, 0]) {
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
														translate(v = [2.275957200481571e-14, 65.35000000000002, 0]) {
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
																		translate(v = [2.275957200481571e-14, 101.9, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-4.949999999999976, 91.65, 0]) {
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
																		translate(v = [2.275957200481571e-14, 133.20000000000002, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-4.949999999999976, 122.95000000000002, 0]) {
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
														translate(v = [2.275957200481571e-14, 144.7, 0]) {
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
														translate(v = [-89.29999999999998, 65.35000000000002, 0]) {
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
																		translate(v = [-89.29999999999998, 101.9, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.24999999999997, 91.65, 0]) {
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
																		translate(v = [-89.29999999999998, 133.20000000000002, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.24999999999997, 122.95000000000002, 0]) {
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
																		translate(v = [-89.29999999999998, 149.95, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-94.24999999999997, 139.7, 0]) {
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
														translate(v = [-178.59999999999994, 65.35000000000002, 0]) {
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
																		translate(v = [-178.59999999999994, 101.9, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-183.54999999999993, 91.65, 0]) {
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
																		translate(v = [-178.59999999999994, 133.20000000000002, 0]) {
																			rotate(a = [90, 0, 0]) {
																				linear_extrude(height = 10.5) {
																					polygon(points = [[-4.85, -0.1], [4.85, -0.1], [4.85, 1.7], [4.35, 1.7], [3.62, 2.4299999999999997], [-3.62, 2.4299999999999997], [-4.35, 1.7], [-4.85, 1.7]]);
																				}
																			}
																		}
																	}
																	union() {
																		translate(v = [-183.54999999999993, 122.95000000000002, 0]) {
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
														translate(v = [-178.59999999999994, 144.7, 0]) {
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
														translate(v = [-223.25, 54.35000000000002, -0.1]) {
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
														translate(v = [-223.25, 62.60000000000002, -0.1]) {
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
														translate(v = [-223.25, 76.35000000000002, -0.1]) {
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
														translate(v = [-267.0, 75.85000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-133.95000000000002, 54.35000000000002, -0.1]) {
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
														translate(v = [-133.95000000000002, 62.60000000000002, -0.1]) {
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
														translate(v = [-133.95000000000002, 76.35000000000002, -0.1]) {
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
														translate(v = [-177.70000000000002, 75.85000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-44.650000000000034, 54.35000000000002, -0.1]) {
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
														translate(v = [-44.650000000000034, 62.60000000000002, -0.1]) {
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
														translate(v = [-44.650000000000034, 76.35000000000002, -0.1]) {
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
														translate(v = [-88.40000000000003, 75.85000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.64999999999998, 54.35000000000002, -0.1]) {
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
														translate(v = [44.64999999999998, 62.60000000000002, -0.1]) {
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
														translate(v = [44.64999999999998, 76.35000000000002, -0.1]) {
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
														translate(v = [0.8999999999999773, 75.85000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-223.25, 85.65, -0.1]) {
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
														translate(v = [-223.25, 93.9, -0.1]) {
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
														translate(v = [-223.25, 107.65, -0.1]) {
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
														translate(v = [-267.0, 107.15, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-133.95000000000002, 85.65, -0.1]) {
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
														translate(v = [-133.95000000000002, 93.9, -0.1]) {
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
														translate(v = [-133.95000000000002, 107.65, -0.1]) {
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
														translate(v = [-177.70000000000002, 107.15, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-44.650000000000034, 85.65, -0.1]) {
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
														translate(v = [-44.650000000000034, 93.9, -0.1]) {
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
														translate(v = [-44.650000000000034, 107.65, -0.1]) {
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
														translate(v = [-88.40000000000003, 107.15, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.64999999999998, 85.65, -0.1]) {
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
														translate(v = [44.64999999999998, 93.9, -0.1]) {
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
														translate(v = [44.64999999999998, 107.65, -0.1]) {
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
														translate(v = [0.8999999999999773, 107.15, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-223.25, 116.95000000000002, -0.1]) {
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
														translate(v = [-223.25, 125.20000000000002, -0.1]) {
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
														translate(v = [-223.25, 138.95000000000002, -0.1]) {
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
														translate(v = [-267.0, 138.45000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-133.95000000000002, 116.95000000000002, -0.1]) {
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
														translate(v = [-133.95000000000002, 125.20000000000002, -0.1]) {
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
														translate(v = [-133.95000000000002, 138.95000000000002, -0.1]) {
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
														translate(v = [-177.70000000000002, 138.45000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-44.650000000000034, 116.95000000000002, -0.1]) {
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
														translate(v = [-44.650000000000034, 125.20000000000002, -0.1]) {
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
														translate(v = [-44.650000000000034, 138.95000000000002, -0.1]) {
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
														translate(v = [-88.40000000000003, 138.45000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [44.64999999999998, 116.95000000000002, -0.1]) {
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
														translate(v = [44.64999999999998, 125.20000000000002, -0.1]) {
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
														translate(v = [44.64999999999998, 138.95000000000002, -0.1]) {
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
														translate(v = [0.8999999999999773, 138.45000000000002, -0.1]) {
															cube(size = [87.5, 0.5, 6.2]);
														}
														translate(v = [-369.0, -139.7, -0.1]) {
															cube(size = [4.800000000000011, 12.25, 6.2]);
														}
														translate(v = [364.2, -139.7, -0.1]) {
															cube(size = [4.800000000000011, 12.25, 6.2]);
														}
														translate(v = [-369.0, -117.44999999999999, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [364.2, -117.44999999999999, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [-369.0, -86.14999999999999, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [364.2, -86.14999999999999, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [-369.0, -54.849999999999994, -0.1]) {
															cube(size = [4.800000000000011, 21.30000000000001, 6.2]);
														}
														translate(v = [364.2, -54.849999999999994, -0.1]) {
															cube(size = [4.800000000000011, 21.30000000000001, 6.2]);
														}
														translate(v = [-369.0, -23.549999999999983, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [364.2, -23.549999999999983, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [-369.0, 7.750000000000014, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [364.2, 7.750000000000014, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999997, 6.2]);
														}
														translate(v = [-369.0, 39.05000000000001, -0.1]) {
															cube(size = [4.800000000000011, 21.30000000000001, 6.2]);
														}
														translate(v = [364.2, 39.05000000000001, -0.1]) {
															cube(size = [4.800000000000011, 21.30000000000001, 6.2]);
														}
														translate(v = [-369.0, 70.35000000000002, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999983, 6.2]);
														}
														translate(v = [364.2, 70.35000000000002, -0.1]) {
															cube(size = [4.800000000000011, 21.299999999999983, 6.2]);
														}
														translate(v = [-369.0, 101.65, -0.1]) {
															cube(size = [4.800000000000011, 21.30000000000001, 6.2]);
														}
														translate(v = [364.2, 101.65, -0.1]) {
															cube(size = [4.800000000000011, 21.30000000000001, 6.2]);
														}
														translate(v = [-369.0, 132.95000000000002, -0.1]) {
															cube(size = [4.800000000000011, 6.749999999999972, 6.2]);
														}
														translate(v = [364.2, 132.95000000000002, -0.1]) {
															cube(size = [4.800000000000011, 6.749999999999972, 6.2]);
														}
														translate(v = [-44.65, 146.75, -0.1]) {
															cylinder(h = 6.2, r = 3.25);
														}
														translate(v = [-133.95, 146.75, -0.1]) {
															cylinder(h = 6.2, r = 3.25);
														}
														translate(v = [-3.6499999999999773, 91.65, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-3.6499999999999773, 122.95000000000002, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.94999999999999, 91.65, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.94999999999999, 122.95000000000002, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-92.94999999999999, 139.7, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-182.24999999999994, 91.65, 0]) {
															rotate(a = [90, 0, 90]) {
																linear_extrude(height = 7.3) {
																	polygon(points = [[5.85, -0.1], [10.25, -0.1], [10.25, 6.1], [-0.25, 6.1], [-0.25, 6.0]]);
																}
															}
														}
														translate(v = [-182.24999999999994, 122.95000000000002, 0]) {
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
										translate(v = [-867.0, -867.0, -1]) {
											cube(size = [693.975, 1734.0, 4.0]);
										}
										translate(v = [-5.574999999999977, -867.0, -1]) {
											cube(size = [872.5749999999999, 1734.0, 4.0]);
										}
										translate(v = [-867.0, -867.0, -1]) {
											cube(size = [1734.0, 936.9250000000001, 4.0]);
										}
										translate(v = [-867.0, 154.0, -1]) {
											cube(size = [1734.0, 713.0, 4.0]);
										}
										translate(v = [-867.0, -867.0, 3.0]) {
											cube(size = [682.975, 1734.0, 4.0]);
										}
										translate(v = [5.425000000000023, -867.0, 3.0]) {
											cube(size = [861.5749999999999, 1734.0, 4.0]);
										}
										translate(v = [-867.0, -867.0, 3.0]) {
											cube(size = [1734.0, 927.9250000000001, 4.0]);
										}
										translate(v = [-867.0, 154.0, 3.0]) {
											cube(size = [1734.0, 713.0, 4.0]);
										}
										translate(v = [-5.499999999999977, 60.85000000000002, 3.0]) {
											cube(size = [11.0, 9.0, 4.0]);
										}
										translate(v = [-184.09999999999994, 60.85000000000002, 3.0]) {
											cube(size = [11.0, 9.0, 4.0]);
										}
										translate(v = [-867.0, -867.0, 6.0]) {
											cube(size = [1734.0, 1734.0, 7.0]);
										}
									}
								}
							}
						}
						translate(v = [-172.79999999999995, -160.5, 0]) {
							cylinder(h = 0.3, r = 6.0);
						}
						translate(v = [-173.79999999999995, -160.5, 0]) {
							cube(size = [2.0, 6.599999999999994, 0.2]);
						}
						translate(v = [-172.79999999999995, -54.425000000000026, 0]) {
							cylinder(h = 0.3, r = 6.0);
						}
						translate(v = [-173.79999999999995, -61.02500000000003, 0]) {
							cube(size = [2.0, 6.600000000000001, 0.2]);
						}
						translate(v = [-5.799999999999977, -160.5, 0]) {
							cylinder(h = 0.3, r = 6.0);
						}
						translate(v = [-6.799999999999977, -160.5, 0]) {
							cube(size = [2.0, 6.599999999999994, 0.2]);
						}
						translate(v = [-5.799999999999977, -54.425000000000026, 0]) {
							cylinder(h = 0.3, r = 6.0);
						}
						translate(v = [-6.799999999999977, -61.02500000000003, 0]) {
							cube(size = [2.0, 6.600000000000001, 0.2]);
						}
					}
					union();
				}
			}
		}
	}
	union();
}
