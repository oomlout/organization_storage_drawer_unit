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
	}
	union();
}
