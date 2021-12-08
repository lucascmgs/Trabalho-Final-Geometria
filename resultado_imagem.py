import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import flood


gridsize = 1000
flood_obj = flood.Flood(gridsize)
flood_obj.set_seeds(40)
start_data = flood_obj.data.copy()
seeds_x = []
seeds_y = []

for value in flood_obj.colors_dict.values():
    seeds_x.append(value[1])
    seeds_y.append(value[0])

control = gridsize//2

while control > 1:
    print(f"Step: {control}")
    flood_obj.jump_flood_iteration()
    control = control //2

flood_obj.step = 8
control = 8

while control > 1:
    print(f"Step: {control}")
    flood_obj.jump_flood_iteration()
    control = control //2


data = flood_obj.data

plt.imshow(data)
plt.scatter(seeds_x, seeds_y, color="red", marker='.')

plt.show()