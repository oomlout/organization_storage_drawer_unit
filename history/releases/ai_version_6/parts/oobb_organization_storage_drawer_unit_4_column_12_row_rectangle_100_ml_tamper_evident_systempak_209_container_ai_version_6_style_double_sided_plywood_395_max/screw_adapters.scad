$fn = 50;

difference() {
	union() {
		translate(v = [-22.5, -15.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
		translate(v = [-7.5, -15.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
		translate(v = [7.5, -15.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
		translate(v = [22.5, -15.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
		translate(v = [-22.5, -0.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
		translate(v = [-7.5, -0.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
		translate(v = [7.5, -0.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
		translate(v = [22.5, -0.5, 2.4]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-3.4, 0, -0.05]) {
											cube(size = [6.8, 10.0, 5.55]);
										}
									}
									union() {
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[-0.1, -0.1], [6.0, -0.1], [6.0, 5.0], [6.6, 5.6], [-0.1, 5.6]]);
												}
											}
										}
										translate(v = [-3.5, 0, 0]) {
											rotate(a = [90, 0, 90]) {
												linear_extrude(height = 7.0) {
													polygon(points = [[10.0, -0.1], [11.0, -0.1], [11.0, 5.6], [9.4, 5.6], [10.0, 5.0]]);
												}
											}
										}
									}
								}
							}
						}
						translate(v = [0, 8.0, -2.4]) {
							hull() {
								translate(v = [-4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, 4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [-4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
								translate(v = [4.75, -4.25, 0]) {
									cylinder(h = 2.4, r = 0.75);
								}
							}
						}
					}
					union() {
						translate(v = [0, 8.0, -2.4]) {
							rotate(a = [0, 180, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.8);
										}
										translate(v = [0, 0, -20.0]) {
											cylinder(h = 20.0, r = 1.5);
										}
									}
									union();
								}
							}
						}
						translate(v = [-1.9, -1, 0]) {
							cube(size = [3.8, 12.0, 5.6]);
						}
					}
				}
			}
		}
	}
	union();
}
