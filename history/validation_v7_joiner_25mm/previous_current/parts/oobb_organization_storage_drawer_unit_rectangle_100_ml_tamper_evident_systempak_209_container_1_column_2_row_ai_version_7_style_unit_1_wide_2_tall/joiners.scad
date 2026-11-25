$fn = 50;

difference() {
	union() {
		translate(v = [-12.5, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-9.0, 9.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
							translate(v = [9.0, 9.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
							translate(v = [-9.0, -9.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
							translate(v = [9.0, -9.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
						}
						translate(v = [-5.0, -5.0, 3.35]) {
							cylinder(h = 2.65, r = 3.0);
						}
						translate(v = [-5.0, 5.0, 3.35]) {
							cylinder(h = 2.65, r = 3.0);
						}
						translate(v = [5.0, -5.0, 3.35]) {
							cylinder(h = 2.65, r = 3.0);
						}
						translate(v = [5.0, 5.0, 3.35]) {
							cylinder(h = 2.65, r = 3.0);
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
		translate(v = [12.5, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-9.0, 4.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
							translate(v = [9.0, 4.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
							translate(v = [-9.0, -4.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
							translate(v = [9.0, -4.0, 0]) {
								cylinder(h = 3.4, r = 1.0);
							}
						}
						translate(v = [-5.0, 0, 3.35]) {
							cylinder(h = 2.65, r = 3.0);
						}
						translate(v = [5.0, 0, 3.35]) {
							cylinder(h = 2.65, r = 3.0);
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
	}
	union();
}
