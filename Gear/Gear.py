from solid import *
from solid.utils import *

model_name = "Gear"

body_radius = 50
hole_radius = 20
tooth_height = 10
tooth_count = 20

gear_thickness = 10

def tooth_cross_section(i):
    angle = i * 2 * pi / tooth_count
    return rotate([0, 0, angle])(
        translate([body_radius, 0, 0])(
            polygon(points=[
                [0, 0],
                [tooth_height, 0],
                [tooth_height, tooth_height/2],
                [tooth_height/2, tooth_height],
                [0, tooth_height/2]
            ])
        )
    )

def gear_cross_section():
    body = circle(body_radius) - circle(hole_radius)
    for i in range(tooth_count):
        body += tooth_cross_section(i)
    return body

def gear():
    return linear_extrude(height=gear_thickness)(
        gear_cross_section()
    )

def assembly():
    return gear()