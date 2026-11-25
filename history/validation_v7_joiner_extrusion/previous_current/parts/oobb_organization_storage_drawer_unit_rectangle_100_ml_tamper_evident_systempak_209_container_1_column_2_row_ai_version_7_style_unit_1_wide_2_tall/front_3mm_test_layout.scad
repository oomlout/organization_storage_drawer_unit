$fn = 50;

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
											translate(v = [-51.8500000005, 47.5000000005, 0]) {
												cylinder(h = 3.0, r = 2.4);
											}
											translate(v = [51.8500000005, 47.5000000005, 0]) {
												cylinder(h = 3.0, r = 2.4);
											}
											translate(v = [-51.8500000005, -47.5000000005, 0]) {
												cylinder(h = 3.0, r = 2.4);
											}
											translate(v = [51.8500000005, -47.5000000005, 0]) {
												cylinder(h = 3.0, r = 2.4);
											}
										}
									}
									union() {
										translate(v = [0.0, -23.900000000000006, -0.1]) {
											hull() {
												translate(v = [-42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [0.0, -15.650000000000006, -0.1]) {
											hull() {
												translate(v = [-37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [0.0, 7.399999999999995, -0.1]) {
											hull() {
												translate(v = [-42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, 5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [42.75, -5.0, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [0.0, 15.649999999999995, -0.1]) {
											hull() {
												translate(v = [-37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, 13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [-37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
												translate(v = [37.25, -13.25, 0]) {
													cylinder(h = 18.2, r = 1.0);
												}
											}
										}
										translate(v = [-49.2500000005, -44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-49.2500000005, 44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.2500000005, -44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [49.2500000005, 44.9000000005, -0.1]) {
											cylinder(h = 6.2, r = 1.8);
										}
										translate(v = [-47.25, -12.500000000000005, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [-47.25, 18.799999999999994, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, -12.500000000000005, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, 18.799999999999994, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [-47.25, -39.5, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
										translate(v = [42.05, -39.5, -0.1]) {
											cube(size = [5.2, 5.2, 6.2]);
										}
									}
								}
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										translate(v = [-28.0, -31.7, 0]) {
											cube(size = [15.0, 7.8, 3.0]);
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
										translate(v = [-28.0, -1.3999999999999986, 0]) {
											cube(size = [15.0, 8.8, 3.0]);
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
										translate(v = [13.0, -31.7, 0]) {
											cube(size = [15.0, 7.8, 3.0]);
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
										translate(v = [13.0, -1.3999999999999986, 0]) {
											cube(size = [15.0, 8.8, 3.0]);
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
		translate(v = [-17.000000000500002, -9.899999999999999, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-6.0, -6.0, 0]) {
							cube(size = [12.0, 12.0, 3.0]);
						}
					}
					union() {
						translate(v = [-2.6, -2.6, -0.1]) {
							cube(size = [5.2, 5.2, 3.2]);
						}
					}
				}
			}
		}
		translate(v = [-5.000018177270249e-10, -9.899999999999999, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-6.0, -6.0, 0]) {
							cube(size = [12.0, 12.0, 3.0]);
						}
					}
					union() {
						translate(v = [-2.6, -2.6, -0.1]) {
							cube(size = [5.2, 5.2, 3.2]);
						}
					}
				}
			}
		}
		translate(v = [16.999999999499998, -9.899999999999999, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-6.0, -6.0, 0]) {
							cube(size = [12.0, 12.0, 3.0]);
						}
					}
					union() {
						translate(v = [-2.6, -2.6, -0.1]) {
							cube(size = [5.2, 5.2, 3.2]);
						}
					}
				}
			}
		}
		translate(v = [-17.000000000500002, 21.400000000000002, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-6.0, -6.0, 0]) {
							cube(size = [12.0, 12.0, 3.0]);
						}
					}
					union() {
						translate(v = [-2.6, -2.6, -0.1]) {
							cube(size = [5.2, 5.2, 3.2]);
						}
					}
				}
			}
		}
		translate(v = [-5.000018177270249e-10, 21.400000000000002, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-6.0, -6.0, 0]) {
							cube(size = [12.0, 12.0, 3.0]);
						}
					}
					union() {
						translate(v = [-2.6, -2.6, -0.1]) {
							cube(size = [5.2, 5.2, 3.2]);
						}
					}
				}
			}
		}
		translate(v = [16.999999999499998, 21.400000000000002, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-6.0, -6.0, 0]) {
							cube(size = [12.0, 12.0, 3.0]);
						}
					}
					union() {
						translate(v = [-2.6, -2.6, -0.1]) {
							cube(size = [5.2, 5.2, 3.2]);
						}
					}
				}
			}
		}
	}
	union();
}
