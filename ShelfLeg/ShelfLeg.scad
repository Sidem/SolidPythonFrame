$fn = 48;


difference() {
	cube(size = [160, 160, 5]);
	translate(v = [5, 0, 0]) {
		cube(size = [150, 155, 5]);
	}
	translate(v = [155, 159, 0]) {
		cube(size = [5, 5, 5]);
	}
	translate(v = [0, 159, 0]) {
		cube(size = [5, 5, 5]);
	}
	translate(v = [20, 146, 0]) {
		linear_extrude(height = 20) {
			polygon(points = [[0, 0], [20, 0], [10.0000000000, 8]]);
		}
	}
	translate(v = [120, 146, 0]) {
		linear_extrude(height = 20) {
			polygon(points = [[0, 0], [20, 0], [10.0000000000, 8]]);
		}
	}
}