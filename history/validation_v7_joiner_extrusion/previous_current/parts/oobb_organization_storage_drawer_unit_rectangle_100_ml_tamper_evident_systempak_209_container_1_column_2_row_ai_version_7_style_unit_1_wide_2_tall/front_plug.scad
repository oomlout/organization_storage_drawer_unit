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
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [0, 1.5, 0]) {
															hull() {
																translate(v = [-4.15, 4.15, 0]) {
																	cylinder(h = 4.55, r = 0.75);
																}
																translate(v = [4.15, 4.15, 0]) {
																	cylinder(h = 4.55, r = 0.75);
																}
																translate(v = [-4.15, -4.15, 0]) {
																	cylinder(h = 4.55, r = 0.75);
																}
																translate(v = [4.15, -4.15, 0]) {
																	cylinder(h = 4.55, r = 0.75);
																}
															}
														}
													}
													union() {
														translate(v = [0, 0, 2.0]) {
															hull() {
																translate(v = [-3.9000000000000004, 2.5, 0]) {
																	cylinder(h = 2.65, r = 0.3);
																}
																translate(v = [3.9000000000000004, 2.5, 0]) {
																	cylinder(h = 2.65, r = 0.3);
																}
																translate(v = [-3.9000000000000004, -2.5, 0]) {
																	cylinder(h = 2.65, r = 0.3);
																}
																translate(v = [3.9000000000000004, -2.5, 0]) {
																	cylinder(h = 2.65, r = 0.3);
																}
															}
														}
														translate(v = [-5.5, -4.6, -0.1]) {
															cylinder(h = 4.75, r = 3.15);
														}
														translate(v = [-5.5, 4.6, -0.1]) {
															cylinder(h = 4.75, r = 3.15);
														}
														translate(v = [5.5, -4.6, -0.1]) {
															cylinder(h = 4.75, r = 3.15);
														}
														translate(v = [5.5, 4.6, -0.1]) {
															cylinder(h = 4.75, r = 3.15);
														}
													}
												}
											}
										}
										translate(v = [0, 0, 0]) {
											rotate(a = [0, 0, 0]) {
												difference() {
													union() {
														translate(v = [-1.4000000000000001, -1.9, 1.95]) {
															cube(size = [2.8000000000000003, 3.8, 12.65]);
														}
													}
													union() {
														translate(v = [0, 2.0, 0]) {
															rotate(a = [90, 0, 0]) {
																linear_extrude(height = 4.0) {
																	polygon(points = [[-1.3, 1.85], [-1.3, 10.6], [-0.4, 14.6], [-0.4, 14.799999999999999], [-1.6, 14.799999999999999], [-1.6, 1.85]]);
																}
															}
														}
														translate(v = [0, 2.0, 0]) {
															rotate(a = [90, 0, 0]) {
																linear_extrude(height = 4.0) {
																	polygon(points = [[1.3, 1.85], [1.3, 10.6], [0.4, 14.6], [0.4, 14.799999999999999], [1.6, 14.799999999999999], [1.6, 1.85]]);
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
					}
					union();
				}
			}
		}
	}
	union();
}
