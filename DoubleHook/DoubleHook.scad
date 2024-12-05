$fn = 48;


union() {
	translate(v = [0, 0, 0]) {
		cube(size = [40, 8, 8]);
	}
	translate(v = [56, 8, 0]) {
		rotate(a = [90, 110, 0]) {
			rotate_extrude(angle = 290) {
				translate(v = [16, 0, 0]) {
					square(size = 8);
				}
			}
		}
	}
	translate(v = [-32, 0, 0]) {
		rotate(a = [90, 180, 180]) {
			rotate_extrude(angle = 270) {
				translate(v = [32, 0, 0]) {
					square(size = 8);
				}
			}
		}
	}
}