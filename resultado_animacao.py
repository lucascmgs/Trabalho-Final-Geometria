import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import animation
import numpy as np
import random
import flood

plt.rcParams['animation.ffmpeg_path'] = 'D:/ffmpeg/bin/ffmpeg.exe'

gridsize = 1000
cmap = colors.ListedColormap(['#FFFFFF','#ffc5d0', '#ffff00', '#22cae0', '#f52ec0', '#603f8b', '#b4fee7', '#a16ae8', '#fd49a0', '#821d30'])
bounds = [0,1,2,3,4,5,6, 7, 8]
norm = colors.BoundaryNorm(bounds, cmap.N)
fig, ax = plt.subplots(figsize = (10, 10))
data = np.zeros((gridsize, gridsize))

updated_image = ax.imshow(data, cmap = cmap, norm = norm)


ax.set_xticks(np.arange(-.5, gridsize, 1))
ax.set_yticks(np.arange(-.5, gridsize, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])

flood_obj = flood.Flood(gridsize)
flood_obj.set_seeds(8)

data_history = [[[]]]
data_history.append(flood_obj.data.copy())

control = gridsize//2
while control > 1:
    flood_obj.jump_flood_iteration()
    data_history.append(flood_obj.data.copy())
    control = control //2

flood_obj.step = control = 32


while control > 1:
    flood_obj.jump_flood_iteration()
    data_history.append(flood_obj.data.copy())
    control = control //2

def draw_frame(frame_number):
    
    updated_image.set_array(data_history[frame_number])
    return [updated_image]


anim = animation.FuncAnimation(fig, draw_frame, frames=(len(data_history)), interval=2000, blit=True)
FFwriter = animation.FFMpegWriter()
anim.save("resultd.mp4", writer=FFwriter)
