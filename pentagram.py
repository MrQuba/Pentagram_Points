# Program that generates points for pentagram/pentagon
from litemapy import Schematic, Region, BlockState
import math 
import string

def calculate_endpoint(x1, y1, length, angle,):
    angle_rad = math.radians(angle)
    x2 = x1 + int(length * math.cos(angle_rad))
    y2 = y1 + int(length * math.sin(angle_rad))
    return x2, y2

pentagon_perimeter= 271 # Perimeter of pentagon
reg = Region(0,0,0, 175,1, 171) # Area, modify this if size increases
pentagon_angle = 72
pentagon_side_length = round((2 * pentagon_perimeter) / 5)
block = BlockState("minecraft:gold_block") # block points are made of 
schem = reg.as_schematic(name="Pentagram", author="MrQuba", description="Made with litemapy")

pent_x,pent_y = 141,2 # increase/decrease pent_x as size changes, otherwise some points will be at negative positions
for i in range(5):
     reg[pent_x, 0, pent_y] = block # set block at position
     pent_x,pent_y = calculate_endpoint(pent_x, pent_y, pentagon_side_length, pentagon_angle) # calculate next position
     pentagon_angle = pentagon_angle + 72 # increase angle
     print("(%s, %s)" % (pent_x, pent_y)) # display coordinates

schem.save("pentagram_points.litematic") # saves schem
