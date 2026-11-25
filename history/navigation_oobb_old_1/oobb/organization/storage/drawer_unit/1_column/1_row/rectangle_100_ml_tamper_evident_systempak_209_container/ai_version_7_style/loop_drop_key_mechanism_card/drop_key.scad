$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-3.5, -7.0, 0]) {
							cube(size = [7.0, 8.6, 2.0]);
						}
					}
					union() {
						translate(v = [-3.6, -7.1, -0.1]) {
							cube(size = [2.6, 7.1, 2.2]);
						}
						translate(v = [1.0, -7.1, -0.1]) {
							cube(size = [2.6, 7.1, 2.2]);
						}
					}
				}
			}
		}
	}
	union();
}
