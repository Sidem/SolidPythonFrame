from solid import *
from solid.utils import *

model_name = "PictureFrame"

canvas_width = 200
canvas_height = 200
canvas_thickness = 4.5

def pictureFrame():
    cube1 = cube([206,206,9])
    cube2 = translate([3,3,2])(cube([203,200,5]))
    cube3 = translate([4,4,0])(cube([198,198,15]))
    cube4 = translate([4,4,2])(cube([203,198,15]))
    nailmount = translate([4,75,8])(cube([10,50,1]))
    nailhole1 = translate([4+4.5,75+4.5,8])(cube([2,2,1]))
    nailhole2 = translate([4+4.5,125-6.5,8])(cube([2,2,1]))
    cube1 = cube1 - cube2
    cube1 = cube1 - cube3
    cube1 = cube1 - cube4
    return cube1 + ((nailmount - nailhole1) - nailhole2)

def assembly():
    return pictureFrame()