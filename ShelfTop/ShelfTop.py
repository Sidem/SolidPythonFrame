from solid import *
from solid.utils import *

model_name = "ShelfTop"

shelf_width = 230
shelf_depth = 160
shelf_thick = 16

shelf_peg_w = 20
shelf_peg_d = 20
shelf_peg_t = 8

peg_offset = (shelf_thick-shelf_peg_t)/2

def getPeg():
    peg = polygon([[0,0], [shelf_peg_d, 0], [shelf_peg_d/2, shelf_peg_t]])
    peg = linear_extrude(height=shelf_peg_w)(peg)
    peg = rotate([0, 90, 0])(peg)
    peg = rotate([90, 0, 0])(peg)
    return peg

def shelfTop():
    peg = getPeg()
    shelf = cube([shelf_width, shelf_depth, shelf_thick])
    peg1 = translate([0, shelf_peg_d, peg_offset])(peg)
    peg2 = translate([0, shelf_depth-(shelf_peg_d*2), peg_offset])(peg)
    peg3 = translate([shelf_width-shelf_peg_w, shelf_peg_d, peg_offset])(peg)
    peg4 = translate([shelf_width-shelf_peg_w, shelf_depth-(shelf_peg_d*2), peg_offset])(peg)
    return shelf - peg1 - peg2 - peg3 - peg4

def assembly():
    return shelfTop()