$fn = 50;

difference() {
	union() {
		translate(v = [-25.5, 5.75, 0]) {
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
		translate(v = [-8.5, 5.75, 0]) {
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
		translate(v = [8.5, 5.75, 0]) {
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
		translate(v = [25.5, 5.75, 0]) {
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
