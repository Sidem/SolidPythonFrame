from solid import *
from solid.utils import *
from math import sin, cos

model_name = "AirNozzle"

length = 220
radius = 8
wall_thickness = 1
hole_radius = 0.5



def nozzle():
    nozzle = cylinder(r=radius, h=length)
    nozzle = nozzle - translate([0,0,1])(cylinder(r=radius-wall_thickness, h=length))
    for j in range (0, int(length/8), 4):
        for i in range(0, 180, 20):
            nozzle = nozzle - rotate([0,0,i])(translate([0,radius*2,(length/8)-j])(rotate([90,0,0])(cylinder(r=0.5, h=radius*4))))
    return nozzle


def assembly():
    return nozzle()