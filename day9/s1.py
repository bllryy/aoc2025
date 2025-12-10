# change the input possibly to somthing smaller
# i watched a yt video ngl 
import sys


tiles = [[int(n) for n in line.split(',')] for line in open(0)]
print(max([(abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1) for tile1 in tiles for tile2 in tiles]))
# abs to keep the range inclusive
