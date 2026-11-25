$fn = 50;

difference() {
	union() {
		translate(v = [0, -5, 7.5]) {
			rotate(a = [0, 180, 0]) {
				difference() {
					union() {
						translate(v = [-7.5, -2.0, 0]) {
							cube(size = [15.0, 14.0, 7.5]);
						}
					}
					union() {
						translate(v = [-3.65, -0.25, -0.1]) {
							cube(size = [7.3, 10.5, 7.7]);
						}
						translate(v = [-4.85, -0.25, -0.1]) {
							cube(size = [9.7, 10.5, 1.8]);
						}
						translate(v = [6, 8.5, 0.6]) {
							rotate(a = [0, 180, 0]) {
								linear_extrude(height = 0.7) {
									text(font = "Arial:style=Bold", halign = "center", size = 1.8, text = "19", valign = "center");
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
