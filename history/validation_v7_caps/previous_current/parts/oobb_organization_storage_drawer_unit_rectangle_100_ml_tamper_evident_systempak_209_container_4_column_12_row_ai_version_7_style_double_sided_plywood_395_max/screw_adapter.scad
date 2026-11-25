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
										translate(v = [-0.35, 0, 0]) {
											hull() {
												translate(v = [-4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, 4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [-4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
												translate(v = [4.4, -4.25, 0]) {
													cylinder(h = 2.4, r = 0.75);
												}
											}
										}
										translate(v = [-2.5, -2.5, 2.35]) {
											cube(size = [5.0, 5.0, 3.0]);
										}
									}
									union() {
										translate(v = [0, 0, 0]) {
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
										translate(v = [-1.5, -3.0, 2.4]) {
											cube(size = [3.0, 6.0, 3.0500000000000003]);
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[-2.7, 4.75], [-1.9, 5.55], [-2.7, 5.55]]);
												}
											}
										}
										translate(v = [0, 2.6, 0]) {
											rotate(a = [90, 0, 0]) {
												linear_extrude(height = 5.2) {
													polygon(points = [[2.7, 4.75], [1.9, 5.55], [2.7, 5.55]]);
												}
											}
										}
										translate(v = [-4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [-4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, -5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
										}
										translate(v = [4.6, 5.5, -0.1]) {
											cylinder(h = 2.6, r = 3.15);
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
