import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import flood


gridsize = 100
flood_obj = flood.Flood(gridsize)
flood_obj.set_seeds(10)
start_data = flood_obj.data.copy()
seeds_x = []
seeds_y = []

for value in flood_obj.colors_dict.values():
    seeds_x.append(value[1])
    seeds_y.append(value[0])

control = gridsize//2

while control > 1:
    flood_obj.jump_flood_iteration()
    control = control //2

flood_obj.step = 8
control = 8

while control > 1:
    flood_obj.jump_flood_iteration()
    control = control //2




data = flood_obj.data
figure, axes = plt.subplots(1, 2)
axes[0].imshow(data)
axes[0].scatter(seeds_x, seeds_y, color="red")



flood_obj.data = start_data
for i in range(gridsize):
    flood_obj.common_flood_iteration()

data2 = flood_obj.data
axes[1].imshow(data2)
axes[1].scatter(seeds_x, seeds_y, color="red")


plt.show()