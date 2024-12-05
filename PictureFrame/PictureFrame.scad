$fn = 48;


union() {
	difference() {
		cube(size = [206, 206, 9]);
		translate(v = [3, 3, 2]) {
			cube(size = [203, 200, 5]);
		}
		translate(v = [4, 4, 0]) {
			cube(size = [198, 198, 15]);
		}
		translate(v = [4, 4, 2]) {
			cube(size = [203, 198, 15]);
		}
	}
	difference() {
		translate(v = [4, 75, 8]) {
			cube(size = [10, 50, 1]);
		}
		translate(v = [8.5000000000, 79.5000000000, 8]) {
			cube(size = [2, 2, 1]);
		}
		translate(v = [8.5000000000, 118.5000000000, 8]) {
			cube(size = [2, 2, 1]);
		}
	}
}