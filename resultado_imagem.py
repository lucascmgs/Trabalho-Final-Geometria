import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import flood


gridsize = 1000
flood_obj = flood.Flood(gridsize)
flood_obj.set_seeds(6)



control = gridsize//2

while control > 1:
    flood_obj.jump_flood_iteration()
    control = control //2

control = gridsize//2
while control > 1:
    flood_obj.jump_flood_iteration()
    control = control //2




gridsize = 100
data = flood_obj.data

plt.imshow(data)
plt.show()