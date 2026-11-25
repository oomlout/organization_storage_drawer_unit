$fn = 50;

difference() {
	union() {
		translate(v = [0, 9.5, 0]) {
			rotate(a = [90, 0, 0]) {
				difference() {
					union() {
						translate(v = [-5.5, 0, 0]) {
							cube(size = [11.0, 10.0, 32.0]);
						}
						translate(v = [-2.5, 0, -13.0]) {
							cube(size = [5.0, 10.0, 13.1]);
						}
					}
					union() {
						translate(v = [-2.6, 2.75, -11.4]) {
							cube(size = [5.2, 4.5, 3.3]);
						}
						translate(v = [5.5, 10.1, 30.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.6);
							}
						}
						translate(v = [5.5, 10.1, 28.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.6);
							}
						}
						translate(v = [5.5, 10.1, 26.0]) {
							rotate(a = [90, 0, 0]) {
								cylinder(h = 10.2, r = 0.6);
							}
						}
					}
				}
			}
		}
	}
	union();
}
