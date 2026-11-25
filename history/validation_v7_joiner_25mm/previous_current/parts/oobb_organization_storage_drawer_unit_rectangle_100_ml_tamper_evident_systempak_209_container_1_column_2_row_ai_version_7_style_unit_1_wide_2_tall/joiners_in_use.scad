$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [-90, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -6.0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											hull() {
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, 9.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, 9.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, -9.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, -9.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [-5.0, -5.0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [-5.0, 5.0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [5.0, -5.0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [5.0, 5.0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
									}
									union() {
										translate(v = [-5.0, -5.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [-5.0, 5.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, -5.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, 5.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
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
						translate(v = [0, 0, 24.0]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
											hull() {
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, 9.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, 9.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, -9.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, -9.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-5.0, 5.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [-5.0, -5.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [5.0, 5.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [5.0, -5.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [-5.0, 5.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [-5.0, -5.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [5.0, 5.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [5.0, -5.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [-103.9000000005, -104.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [3.900000000500003, -104.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-50, -50, 18.0]) {
											cube(size = [100, 100, 2]);
										}
									}
								}
							}
						}
						translate(v = [-5.0, -5.0, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [-5.0, -5.0, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [-5.0, 5.0, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [-5.0, 5.0, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, -5.0, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, -5.0, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, 5.0, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, 5.0, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [0, -94.800000001, -6.0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											hull() {
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [-5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
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
						translate(v = [0, -94.800000001, 24.0]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
											hull() {
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [-5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [-103.9000000005, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-104.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [3.900000000500003, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [4.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-50, -50, 18.0]) {
											cube(size = [100, 100, 2]);
										}
									}
								}
							}
						}
						translate(v = [-5.0, -94.800000001, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [-5.0, -94.800000001, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, -94.800000001, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, -94.800000001, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [0, 94.800000001, -6.0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											hull() {
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [-5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
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
						translate(v = [0, 94.800000001, 24.0]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
											hull() {
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [-5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [-103.9000000005, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-104.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [3.900000000500003, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [4.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-50, -50, 18.0]) {
											cube(size = [100, 100, 2]);
										}
									}
								}
							}
						}
						translate(v = [-5.0, 94.800000001, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [-5.0, 94.800000001, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, 94.800000001, -5.45]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [5.0, 94.800000001, 22.0]) {
							rotate(a = [0.0, 0, 0]) {
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
						translate(v = [-103.500000001, 0, -6.0]) {
							rotate(a = [0, 0, -90]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											hull() {
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [-5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
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
						translate(v = [-103.500000001, 0, 24.0]) {
							rotate(a = [180, 0, -90]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
											hull() {
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [-5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [-103.9000000005, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-104.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [3.900000000500003, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [4.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-50, -50, 18.0]) {
											cube(size = [100, 100, 2]);
										}
									}
								}
							}
						}
						translate(v = [-103.500000001, 5.0, -5.45]) {
							rotate(a = [0.0, 0, -90]) {
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
						translate(v = [-103.500000001, 5.0, 22.0]) {
							rotate(a = [0.0, 0, -90]) {
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
						translate(v = [-103.500000001, -5.0, -5.45]) {
							rotate(a = [0.0, 0, -90]) {
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
						translate(v = [-103.500000001, -5.0, 22.0]) {
							rotate(a = [0.0, 0, -90]) {
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
						translate(v = [103.500000001, 0, -6.0]) {
							rotate(a = [0, 0, 90]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											hull() {
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [1, 0.49, 0.12]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [1, 0.49, 0.12]) {
															cylinder(h = 3.4, r = 1.0);
														}
													}
												}
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [-5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
										color(alpha = 1.0, c = [1, 0.49, 0.12]) {
											translate(v = [5.0, 0, 3.35]) {
												cylinder(h = 2.65, r = 3.0);
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
													}
													union();
												}
											}
										}
										translate(v = [5.0, 0.0, 0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
														}
														translate(v = [0, 0, -1.9]) {
															cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
														}
														cylinder(h = 250, r = 3.6);
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.8);
														}
														translate(v = [0, 0, -6.2]) {
															cylinder(h = 6.2, r = 1.5);
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
						translate(v = [103.500000001, 0, 24.0]) {
							rotate(a = [180, 0, 90]) {
								difference() {
									union() {
										color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
											hull() {
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, 4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [-9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
												color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
													translate(v = [9.0, -4.0, 0]) {
														color(alpha = 1.0, c = [0.79, 0.62, 0.32]) {
															cylinder(h = 18.0, r = 1.0);
														}
													}
												}
											}
										}
									}
									union() {
										translate(v = [-5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [5.0, 0.0, 2.0]) {
											rotate(a = [180.0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																difference() {
																	union() {
																		linear_extrude(height = 4.0) {
																			polygon(points = [[3.4619999999999997, 0.0], [1.7310000000000003, 2.9981799479017264], [-1.7309999999999992, 2.9981799479017264], [-3.4619999999999997, 4.2397272186481365e-16], [-1.7310000000000014, -2.998179947901726], [1.7309999999999977, -2.9981799479017277]]);
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
										translate(v = [-5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [5.0, 0.0, -0.5]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [-103.9000000005, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-104.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [3.900000000500003, -99.8, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [4.8, -98.9000000005, -0.1]) {
											cube(size = [100, 100, 19.0]);
										}
										translate(v = [-50, -50, 18.0]) {
											cube(size = [100, 100, 2]);
										}
									}
								}
							}
						}
						translate(v = [103.500000001, -5.0, -5.45]) {
							rotate(a = [0.0, 0, 90]) {
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
						translate(v = [103.500000001, -5.0, 22.0]) {
							rotate(a = [0.0, 0, 90]) {
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
						translate(v = [103.500000001, 5.0, -5.45]) {
							rotate(a = [0.0, 0, 90]) {
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
						translate(v = [103.500000001, 5.0, 22.0]) {
							rotate(a = [0.0, 0, 90]) {
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
							translate(v = [-54.2500000005, -49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
							}
						}
						color(alpha = 1.0, c = [0.24, 0.48, 0.54]) {
							translate(v = [-54.2500000005, 49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
							}
						}
						color(alpha = 1.0, c = [0.24, 0.48, 0.54]) {
							translate(v = [54.2500000005, -49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
							}
						}
						color(alpha = 1.0, c = [0.24, 0.48, 0.54]) {
							translate(v = [54.2500000005, 49.9000000005, 0]) {
								import(file = "assembled.stl", origin = [0, 0]);
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
