from solid import *
from solid.utils import *
from math import sin, cos

model_name = "DoubleHook"

thickness = 8

hook_radius_top = 16
hook_radius_bottom = 32
connection_length = 40


def hook():
    return union()(
        translate([0, 0, 0])(
            cube([40, 8, 8])
        ),
        translate([56, 8, 0])(
            rotate([90, 110, 0])(
                rotate_extrude(angle=290)(
                    translate([16, 0, 0])(
                        square(8)
                    )
                )
            )
        ),
        translate([-32, 0, 0])(
            rotate([90, 180, 180])(
                rotate_extrude(angle=270)(
                    translate([32, 0, 0])(
                        square(8)
                    )
                )
            )
        )
    )


def assembly():
    return hook()