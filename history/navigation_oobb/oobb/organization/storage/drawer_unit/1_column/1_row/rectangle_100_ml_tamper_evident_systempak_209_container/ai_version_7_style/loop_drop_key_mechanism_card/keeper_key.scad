$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [-2.25, -4.0, 0]) {
							cube(size = [4.5, 13.2, 4.0]);
						}
					}
					union() {
						translate(v = [-2.35, -4.1, -0.1]) {
							cube(size = [1.1500000000000001, 12.1, 4.2]);
						}
						translate(v = [1.2, -4.1, -0.1]) {
							cube(size = [1.1500000000000001, 12.1, 4.2]);
						}
					}
				}
			}
		}
	}
	union();
}
