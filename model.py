from solid import *
from solid.utils import *

model_name = "ShelfLeg"

leg_height = 160
leg_depth = 160
leg_thick = 5

shelf_peg_w = 20
shelf_peg_d = 20
shelf_peg_t = 8

def getPeg():
    peg = polygon([[0,0], [shelf_peg_d, 0], [shelf_peg_d/2, shelf_peg_t]])
    peg = linear_extrude(height=shelf_peg_w)(peg)
    return peg

def shelfLeg():
    leg = cube([leg_height, leg_depth, leg_thick])
    peg1 = translate([shelf_peg_w, leg_height-(shelf_peg_t+6), 0])(getPeg())
    peg2 = translate([leg_depth-(shelf_peg_w*2), leg_height-(shelf_peg_t+6), 0])(getPeg())
    leg = leg - translate([leg_thick,0,0])(cube([leg_height-(leg_thick*2), leg_depth-leg_thick, leg_thick]))
    leg = leg - translate([leg_depth-leg_thick,leg_height-1,0])(cube([leg_thick, leg_thick, leg_thick]))
    leg = leg - translate([0,leg_height-1,0])(cube([leg_thick, leg_thick, leg_thick]))
    
    return leg - peg1 - peg2

def assembly():
    return shelfLeg()