$fn = 50;

difference() {
	union() {
		translate(v = [-12.4, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-9.15, 9.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
							translate(v = [9.15, 9.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
							translate(v = [-9.15, -9.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
							translate(v = [9.15, -9.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
						}
					}
					union() {
						translate(v = [-5.0, -5.0, 4.75]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -8.599999999999998]) {
											cylinder(h = 8.599999999999998, r = 1.8);
										}
									}
									union();
								}
							}
						}
						translate(v = [-5.0, 5.0, 4.75]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -8.599999999999998]) {
											cylinder(h = 8.599999999999998, r = 1.8);
										}
									}
									union();
								}
							}
						}
						translate(v = [5.0, -5.0, 4.75]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -8.599999999999998]) {
											cylinder(h = 8.599999999999998, r = 1.8);
										}
									}
									union();
								}
							}
						}
						translate(v = [5.0, 5.0, 4.75]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -8.599999999999998]) {
											cylinder(h = 8.599999999999998, r = 1.8);
										}
									}
									union();
								}
							}
						}
						translate(v = [-11.1, 13.0, 2.69]) {
							hull() {
								translate(v = [-4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [-8.1, 13.0, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [-10.0, 7.65, 5.64]) {
							cube(size = [5.55, 2.3499999999999996, 2.8600000000000003]);
						}
						translate(v = [-10.0, 7.65, 5.64]) {
							cube(size = [6.25, 2.3499999999999996, 2.8600000000000003]);
						}
						translate(v = [8.1, 13.0, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [3.75, 7.65, 5.64]) {
							cube(size = [6.25, 2.3499999999999996, 2.8600000000000003]);
						}
						translate(v = [4.45, 7.65, 5.64]) {
							cube(size = [5.55, 2.3499999999999996, 2.8600000000000003]);
						}
						translate(v = [11.1, 13.0, 2.69]) {
							hull() {
								translate(v = [-4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [12.4, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-9.15, 4.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
							translate(v = [9.15, 4.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
							translate(v = [-9.15, -4.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
							translate(v = [9.15, -4.15, 0]) {
								cylinder(h = 8.399999999999999, r = 0.75);
							}
						}
					}
					union() {
						translate(v = [-5.0, 0, 4.75]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -8.599999999999998]) {
											cylinder(h = 8.599999999999998, r = 1.8);
										}
									}
									union();
								}
							}
						}
						translate(v = [5.0, 0, 4.75]) {
							rotate(a = [180, 0, 0]) {
								difference() {
									union() {
										translate(v = [0, 0, -1.9]) {
											cylinder(h = 1.9, r1 = 1.8, r2 = 3.6);
										}
										cylinder(h = 250, r = 3.6);
										translate(v = [0, 0, -8.599999999999998]) {
											cylinder(h = 8.599999999999998, r = 1.8);
										}
									}
									union();
								}
							}
						}
						translate(v = [-13.0, 3.1, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [-13.0, 6.1000000000000005, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [-11.1, 8.0, 2.69]) {
							hull() {
								translate(v = [-4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [-8.1, 8.0, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [-10.0, -1.25, 5.64]) {
							cube(size = [2.3499999999999996, 6.25, 2.8600000000000003]);
						}
						translate(v = [-10.0, -0.55, 5.64]) {
							cube(size = [2.3499999999999996, 5.55, 2.8600000000000003]);
						}
						translate(v = [-10.0, 2.65, 5.64]) {
							cube(size = [5.55, 2.35, 2.8600000000000003]);
						}
						translate(v = [-10.0, 2.65, 5.64]) {
							cube(size = [6.25, 2.35, 2.8600000000000003]);
						}
						translate(v = [8.1, 8.0, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [3.75, 2.65, 5.64]) {
							cube(size = [6.25, 2.35, 2.8600000000000003]);
						}
						translate(v = [4.45, 2.65, 5.64]) {
							cube(size = [5.55, 2.35, 2.8600000000000003]);
						}
						translate(v = [11.1, 8.0, 2.69]) {
							hull() {
								translate(v = [-4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.149999999999999, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [13.0, 3.1, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [13.0, 6.1000000000000005, 2.69]) {
							hull() {
								translate(v = [-4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, 4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [-4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
								translate(v = [4.15, -4.15, 0]) {
									cylinder(h = 5.8100000000000005, r = 1.65);
								}
							}
						}
						translate(v = [7.65, -1.25, 5.64]) {
							cube(size = [2.3499999999999996, 6.25, 2.8600000000000003]);
						}
						translate(v = [7.65, -0.55, 5.64]) {
							cube(size = [2.3499999999999996, 5.55, 2.8600000000000003]);
						}
					}
				}
			}
		}
	}
	union();
}
