$fn = 50;

union() {
	difference() {
		union() {
			hull() {
				translate(v = [-177.7, 174.9, 0]) {
					cylinder(h = 110.5, r = 2.4);
				}
				translate(v = [177.7, 174.9, 0]) {
					cylinder(h = 110.5, r = 2.4);
				}
				translate(v = [-177.7, -174.9, 0]) {
					cylinder(h = 110.5, r = 2.4);
				}
				translate(v = [177.7, -174.9, 0]) {
					cylinder(h = 110.5, r = 2.4);
				}
			}
		}
		union() {
			translate(v = [-133.95, -168.9, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, -161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, -174.8, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -168.9, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -174.8, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -168.9, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, -161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, -174.8, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, -168.9, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, -161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, -174.8, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, -166.9, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, -156.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, -139.6, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, -131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, -116.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -139.6, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -116.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -139.6, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, -131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -116.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, -139.6, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, -131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, -145.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, -116.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, -137.6, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, -126.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, -110.30000000000001, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, -102.55000000000001, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, -116.20000000000002, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -110.30000000000001, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -102.55000000000001, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -116.20000000000002, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -110.30000000000001, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, -102.55000000000001, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, -116.20000000000002, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, -110.30000000000001, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, -102.55000000000001, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, -116.20000000000002, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, -108.30000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, -97.55000000000001, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, -81.0, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, -73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -81.0, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -81.0, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, -73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, -81.0, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, -73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, -86.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, -79.0, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, -68.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, -51.7, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, -43.95, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -51.7, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -43.95, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -51.7, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, -43.95, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, -51.7, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, -43.95, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, -57.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, -49.7, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, -38.95, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, -22.400000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, -14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, 0.9999999999999947, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, -22.400000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 0.9999999999999947, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, -22.400000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, -14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 0.9999999999999947, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, -22.400000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, -14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, -28.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, 0.9999999999999947, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, -20.400000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, -9.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, 6.900000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, 14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, 1.0000000000000053, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, 30.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 6.900000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 1.0000000000000053, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 30.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 6.900000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, 14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, 1.0000000000000053, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 30.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, 6.900000000000006, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, 14.650000000000006, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, 1.0000000000000053, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, 30.300000000000004, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, 8.900000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, 19.650000000000006, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, 36.19999999999999, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, 43.94999999999999, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, 30.29999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, 59.59999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 36.19999999999999, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 43.94999999999999, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 30.29999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 59.59999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 36.19999999999999, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, 43.94999999999999, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, 30.29999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 59.59999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, 36.19999999999999, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, 43.94999999999999, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, 30.29999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, 59.59999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, 38.19999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, 48.94999999999999, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, 65.5, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, 73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, 59.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, 88.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 65.5, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 59.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 88.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 65.5, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, 73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, 59.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 88.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, 65.5, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, 73.25, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, 59.6, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, 88.9, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, 67.5, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, 78.25, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, 94.79999999999998, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, 102.54999999999998, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, 88.89999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 94.79999999999998, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 102.54999999999998, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 88.89999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 94.79999999999998, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, 102.54999999999998, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, 88.89999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, 94.79999999999998, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, 102.54999999999998, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, 88.89999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, 96.79999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, 107.54999999999998, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, 124.1, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, 131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 124.1, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 124.1, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, 131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, 124.1, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, 131.85, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, 118.19999999999999, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, 126.1, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, 136.85, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-133.95, 153.4, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-133.95, 161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-133.95, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-133.95, 177.39999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-180.2, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-180.2, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-95.79999999999998, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 153.4, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [-44.64999999999999, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-44.64999999999999, 177.39999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-90.29999999999998, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-6.499999999999993, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 153.4, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [44.650000000000006, 161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [44.650000000000006, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [44.650000000000006, 177.39999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [-0.9999999999999929, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [88.30000000000001, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [82.80000000000001, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [133.95, 153.4, -0.1]) {
				hull() {
					translate(v = [-42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, 5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [-42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
					translate(v = [42.75, -5.0, 0]) {
						cylinder(h = 110.7, r = 1.0);
					}
				}
			}
			translate(v = [133.95, 161.15, -0.1]) {
				hull() {
					translate(v = [-34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, 9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [-34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
					translate(v = [34.25, -9.75, 0]) {
						cylinder(h = 110.7, r = 4.0);
					}
				}
			}
			translate(v = [133.95, 147.5, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [133.95, 177.39999999999998, 0]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-33.75, 7.5], [33.75, 7.5], [33.75, 70.75], [0, 104.5], [-33.75, 70.75]]);
					}
				}
			}
			translate(v = [88.29999999999998, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.0) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [88.29999999999998, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 7.5) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
			translate(v = [177.59999999999997, 155.4, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 2.6) {
						polygon(points = [[-3.0, 7.5], [3.0, 7.5], [3.0, 101.5], [0, 104.5], [-3.0, 101.5]]);
					}
				}
			}
			translate(v = [172.09999999999997, 166.15, 0]) {
				rotate(a = [90, 0, 90]) {
					linear_extrude(height = 8.1) {
						polygon(points = [[-3.75, 7.5], [3.75, 7.5], [3.75, 100.75], [0, 104.5], [-3.75, 100.75]]);
					}
				}
			}
		}
	}
	union() {
		#translate(v = [-161.95, -174.9, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, -174.9, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, -174.9, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, -174.9, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, -145.6, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, -145.6, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, -145.6, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, -145.6, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, -116.30000000000001, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, -116.30000000000001, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, -116.30000000000001, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, -116.30000000000001, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, -87.0, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, -87.0, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, -87.0, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, -87.0, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, -57.7, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, -57.7, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, -57.7, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, -57.7, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, -28.400000000000006, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, -28.400000000000006, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, -28.400000000000006, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, -28.400000000000006, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, 0.9000000000000057, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, 0.9000000000000057, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, 0.9000000000000057, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, 0.9000000000000057, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, 30.19999999999999, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, 30.19999999999999, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, 30.19999999999999, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, 30.19999999999999, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, 59.5, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, 59.5, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, 59.5, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, 59.5, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, 88.79999999999998, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, 88.79999999999998, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, 88.79999999999998, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, 88.79999999999998, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, 118.1, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, 118.1, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, 118.1, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, 118.1, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-161.95, 147.4, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [-72.64999999999999, 147.4, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [16.650000000000006, 147.4, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		#translate(v = [105.94999999999999, 147.4, 0]) {
			rotate(a = [90, 0, 90]) {
				linear_extrude(height = 56.0) {
					polygon(points = [[-1.8, 0], [0, 0], [6.0, 6.0], [6.0, 7.5], [-1.8, 7.5]]);
				}
			}
		}
		translate(v = [-170.1, -187.8, 0]) {
			linear_extrude(height = 0.6) {
				polygon(points = [[10.0, 0.0], [9.95184726672197, 0.980171403295606], [9.807852804032304, 1.9509032201612824], [9.569403357322088, 2.902846772544623], [9.238795325112868, 3.826834323650898], [8.819212643483551, 4.7139673682599765], [8.314696123025453, 5.555702330196022], [7.73010453362737, 6.343932841636455], [7.0710678118654755, 7.0710678118654755], [6.343932841636455, 7.730104533627369], [5.555702330196023, 8.314696123025453], [4.713967368259978, 8.81921264348355], [3.8268343236508984, 9.238795325112868], [2.902846772544623, 9.56940335732209], [1.9509032201612833, 9.807852804032304], [0.9801714032956077, 9.951847266721968], [6.123233995736766e-16, 10.0], [-0.9801714032956065, 9.95184726672197], [-1.950903220161282, 9.807852804032304], [-2.9028467725446214, 9.56940335732209], [-3.826834323650897, 9.238795325112868], [-4.713967368259977, 8.819212643483551], [-5.55570233019602, 8.314696123025453], [-6.3439328416364535, 7.730104533627371], [-7.071067811865475, 7.0710678118654755], [-7.73010453362737, 6.343932841636455], [-8.314696123025453, 5.555702330196022], [-8.81921264348355, 4.713967368259978], [-9.238795325112868, 3.826834323650899], [-9.569403357322088, 2.902846772544624], [-9.807852804032304, 1.9509032201612861], [-9.951847266721968, 0.9801714032956083], [-10.0, 1.2246467991473533e-15], [-9.95184726672197, -0.9801714032956059], [-9.807852804032304, -1.9509032201612837], [-9.56940335732209, -2.902846772544621], [-9.238795325112868, -3.8268343236508966], [-8.819212643483551, -4.7139673682599765], [-8.314696123025454, -5.55570233019602], [-7.730104533627371, -6.343932841636453], [-7.071067811865477, -7.071067811865475], [-6.343932841636459, -7.730104533627367], [-5.555702330196022, -8.314696123025453], [-4.713967368259978, -8.81921264348355], [-3.8268343236509033, -9.238795325112864], [-2.9028467725446245, -9.569403357322088], [-1.9509032201612866, -9.807852804032303], [-0.9801714032956045, -9.95184726672197], [-1.8369701987210296e-15, -10.0], [0.9801714032956009, -9.95184726672197], [1.950903220161283, -9.807852804032304], [2.9028467725446205, -9.56940335732209], [3.8268343236509, -9.238795325112866], [4.713967368259976, -8.819212643483551], [5.555702330196018, -8.314696123025454], [6.343932841636456, -7.730104533627369], [7.071067811865474, -7.071067811865477], [7.730104533627365, -6.343932841636459], [8.314696123025453, -5.555702330196022], [8.819212643483548, -4.713967368259979], [9.238795325112864, -3.826834323650904], [9.569403357322088, -2.902846772544625], [9.807852804032303, -1.9509032201612873], [9.95184726672197, -0.980171403295605]]);
			}
		}
		translate(v = [-172.6, -178.60000000000002, 0]) {
			cube(size = [5.0, 1.700000000000017, 0.3]);
		}
		translate(v = [-170.1, 187.8, 0]) {
			linear_extrude(height = 0.6) {
				polygon(points = [[10.0, 0.0], [9.95184726672197, 0.980171403295606], [9.807852804032304, 1.9509032201612824], [9.569403357322088, 2.902846772544623], [9.238795325112868, 3.826834323650898], [8.819212643483551, 4.7139673682599765], [8.314696123025453, 5.555702330196022], [7.73010453362737, 6.343932841636455], [7.0710678118654755, 7.0710678118654755], [6.343932841636455, 7.730104533627369], [5.555702330196023, 8.314696123025453], [4.713967368259978, 8.81921264348355], [3.8268343236508984, 9.238795325112868], [2.902846772544623, 9.56940335732209], [1.9509032201612833, 9.807852804032304], [0.9801714032956077, 9.951847266721968], [6.123233995736766e-16, 10.0], [-0.9801714032956065, 9.95184726672197], [-1.950903220161282, 9.807852804032304], [-2.9028467725446214, 9.56940335732209], [-3.826834323650897, 9.238795325112868], [-4.713967368259977, 8.819212643483551], [-5.55570233019602, 8.314696123025453], [-6.3439328416364535, 7.730104533627371], [-7.071067811865475, 7.0710678118654755], [-7.73010453362737, 6.343932841636455], [-8.314696123025453, 5.555702330196022], [-8.81921264348355, 4.713967368259978], [-9.238795325112868, 3.826834323650899], [-9.569403357322088, 2.902846772544624], [-9.807852804032304, 1.9509032201612861], [-9.951847266721968, 0.9801714032956083], [-10.0, 1.2246467991473533e-15], [-9.95184726672197, -0.9801714032956059], [-9.807852804032304, -1.9509032201612837], [-9.56940335732209, -2.902846772544621], [-9.238795325112868, -3.8268343236508966], [-8.819212643483551, -4.7139673682599765], [-8.314696123025454, -5.55570233019602], [-7.730104533627371, -6.343932841636453], [-7.071067811865477, -7.071067811865475], [-6.343932841636459, -7.730104533627367], [-5.555702330196022, -8.314696123025453], [-4.713967368259978, -8.81921264348355], [-3.8268343236509033, -9.238795325112864], [-2.9028467725446245, -9.569403357322088], [-1.9509032201612866, -9.807852804032303], [-0.9801714032956045, -9.95184726672197], [-1.8369701987210296e-15, -10.0], [0.9801714032956009, -9.95184726672197], [1.950903220161283, -9.807852804032304], [2.9028467725446205, -9.56940335732209], [3.8268343236509, -9.238795325112866], [4.713967368259976, -8.819212643483551], [5.555702330196018, -8.314696123025454], [6.343932841636456, -7.730104533627369], [7.071067811865474, -7.071067811865477], [7.730104533627365, -6.343932841636459], [8.314696123025453, -5.555702330196022], [8.819212643483548, -4.713967368259979], [9.238795325112864, -3.826834323650904], [9.569403357322088, -2.902846772544625], [9.807852804032303, -1.9509032201612873], [9.95184726672197, -0.980171403295605]]);
			}
		}
		translate(v = [-172.6, 176.9, 0]) {
			cube(size = [5.0, 1.700000000000017, 0.3]);
		}
		translate(v = [170.1, -187.8, 0]) {
			linear_extrude(height = 0.6) {
				polygon(points = [[10.0, 0.0], [9.95184726672197, 0.980171403295606], [9.807852804032304, 1.9509032201612824], [9.569403357322088, 2.902846772544623], [9.238795325112868, 3.826834323650898], [8.819212643483551, 4.7139673682599765], [8.314696123025453, 5.555702330196022], [7.73010453362737, 6.343932841636455], [7.0710678118654755, 7.0710678118654755], [6.343932841636455, 7.730104533627369], [5.555702330196023, 8.314696123025453], [4.713967368259978, 8.81921264348355], [3.8268343236508984, 9.238795325112868], [2.902846772544623, 9.56940335732209], [1.9509032201612833, 9.807852804032304], [0.9801714032956077, 9.951847266721968], [6.123233995736766e-16, 10.0], [-0.9801714032956065, 9.95184726672197], [-1.950903220161282, 9.807852804032304], [-2.9028467725446214, 9.56940335732209], [-3.826834323650897, 9.238795325112868], [-4.713967368259977, 8.819212643483551], [-5.55570233019602, 8.314696123025453], [-6.3439328416364535, 7.730104533627371], [-7.071067811865475, 7.0710678118654755], [-7.73010453362737, 6.343932841636455], [-8.314696123025453, 5.555702330196022], [-8.81921264348355, 4.713967368259978], [-9.238795325112868, 3.826834323650899], [-9.569403357322088, 2.902846772544624], [-9.807852804032304, 1.9509032201612861], [-9.951847266721968, 0.9801714032956083], [-10.0, 1.2246467991473533e-15], [-9.95184726672197, -0.9801714032956059], [-9.807852804032304, -1.9509032201612837], [-9.56940335732209, -2.902846772544621], [-9.238795325112868, -3.8268343236508966], [-8.819212643483551, -4.7139673682599765], [-8.314696123025454, -5.55570233019602], [-7.730104533627371, -6.343932841636453], [-7.071067811865477, -7.071067811865475], [-6.343932841636459, -7.730104533627367], [-5.555702330196022, -8.314696123025453], [-4.713967368259978, -8.81921264348355], [-3.8268343236509033, -9.238795325112864], [-2.9028467725446245, -9.569403357322088], [-1.9509032201612866, -9.807852804032303], [-0.9801714032956045, -9.95184726672197], [-1.8369701987210296e-15, -10.0], [0.9801714032956009, -9.95184726672197], [1.950903220161283, -9.807852804032304], [2.9028467725446205, -9.56940335732209], [3.8268343236509, -9.238795325112866], [4.713967368259976, -8.819212643483551], [5.555702330196018, -8.314696123025454], [6.343932841636456, -7.730104533627369], [7.071067811865474, -7.071067811865477], [7.730104533627365, -6.343932841636459], [8.314696123025453, -5.555702330196022], [8.819212643483548, -4.713967368259979], [9.238795325112864, -3.826834323650904], [9.569403357322088, -2.902846772544625], [9.807852804032303, -1.9509032201612873], [9.95184726672197, -0.980171403295605]]);
			}
		}
		translate(v = [167.6, -178.60000000000002, 0]) {
			cube(size = [5.0, 1.700000000000017, 0.3]);
		}
		translate(v = [170.1, 187.8, 0]) {
			linear_extrude(height = 0.6) {
				polygon(points = [[10.0, 0.0], [9.95184726672197, 0.980171403295606], [9.807852804032304, 1.9509032201612824], [9.569403357322088, 2.902846772544623], [9.238795325112868, 3.826834323650898], [8.819212643483551, 4.7139673682599765], [8.314696123025453, 5.555702330196022], [7.73010453362737, 6.343932841636455], [7.0710678118654755, 7.0710678118654755], [6.343932841636455, 7.730104533627369], [5.555702330196023, 8.314696123025453], [4.713967368259978, 8.81921264348355], [3.8268343236508984, 9.238795325112868], [2.902846772544623, 9.56940335732209], [1.9509032201612833, 9.807852804032304], [0.9801714032956077, 9.951847266721968], [6.123233995736766e-16, 10.0], [-0.9801714032956065, 9.95184726672197], [-1.950903220161282, 9.807852804032304], [-2.9028467725446214, 9.56940335732209], [-3.826834323650897, 9.238795325112868], [-4.713967368259977, 8.819212643483551], [-5.55570233019602, 8.314696123025453], [-6.3439328416364535, 7.730104533627371], [-7.071067811865475, 7.0710678118654755], [-7.73010453362737, 6.343932841636455], [-8.314696123025453, 5.555702330196022], [-8.81921264348355, 4.713967368259978], [-9.238795325112868, 3.826834323650899], [-9.569403357322088, 2.902846772544624], [-9.807852804032304, 1.9509032201612861], [-9.951847266721968, 0.9801714032956083], [-10.0, 1.2246467991473533e-15], [-9.95184726672197, -0.9801714032956059], [-9.807852804032304, -1.9509032201612837], [-9.56940335732209, -2.902846772544621], [-9.238795325112868, -3.8268343236508966], [-8.819212643483551, -4.7139673682599765], [-8.314696123025454, -5.55570233019602], [-7.730104533627371, -6.343932841636453], [-7.071067811865477, -7.071067811865475], [-6.343932841636459, -7.730104533627367], [-5.555702330196022, -8.314696123025453], [-4.713967368259978, -8.81921264348355], [-3.8268343236509033, -9.238795325112864], [-2.9028467725446245, -9.569403357322088], [-1.9509032201612866, -9.807852804032303], [-0.9801714032956045, -9.95184726672197], [-1.8369701987210296e-15, -10.0], [0.9801714032956009, -9.95184726672197], [1.950903220161283, -9.807852804032304], [2.9028467725446205, -9.56940335732209], [3.8268343236509, -9.238795325112866], [4.713967368259976, -8.819212643483551], [5.555702330196018, -8.314696123025454], [6.343932841636456, -7.730104533627369], [7.071067811865474, -7.071067811865477], [7.730104533627365, -6.343932841636459], [8.314696123025453, -5.555702330196022], [8.819212643483548, -4.713967368259979], [9.238795325112864, -3.826834323650904], [9.569403357322088, -2.902846772544625], [9.807852804032303, -1.9509032201612873], [9.95184726672197, -0.980171403295605]]);
			}
		}
		translate(v = [167.6, 176.9, 0]) {
			cube(size = [5.0, 1.700000000000017, 0.3]);
		}
	}
}
