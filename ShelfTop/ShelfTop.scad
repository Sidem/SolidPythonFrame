$fn = 48;


difference() {
	cube(size = [230, 160, 16]);
	translate(v = [0, 20, 4.0000000000]) {
		rotate(a = [90, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				linear_extrude(height = 20) {
					polygon(points = [[0, 0], [20, 0], [10.0000000000, 8]]);
				}
			}
		}
	}
	translate(v = [0, 120, 4.0000000000]) {
		rotate(a = [90, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				linear_extrude(height = 20) {
					polygon(points = [[0, 0], [20, 0], [10.0000000000, 8]]);
				}
			}
		}
	}
	translate(v = [210, 20, 4.0000000000]) {
		rotate(a = [90, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				linear_extrude(height = 20) {
					polygon(points = [[0, 0], [20, 0], [10.0000000000, 8]]);
				}
			}
		}
	}
	translate(v = [210, 120, 4.0000000000]) {
		rotate(a = [90, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				linear_extrude(height = 20) {
					polygon(points = [[0, 0], [20, 0], [10.0000000000, 8]]);
				}
			}
		}
	}
}