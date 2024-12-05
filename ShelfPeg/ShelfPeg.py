from solid import *
from solid.utils import *

model_name = "ShelfPeg"

shelf_peg_w = 25
shelf_peg_d = 20
shelf_peg_t = 8

def getPeg():
    peg = polygon([[0,0], [shelf_peg_d, 0], [shelf_peg_d/2, shelf_peg_t]])
    peg = linear_extrude(height=shelf_peg_w)(peg)
    return peg

def assembly():
    return getPeg()