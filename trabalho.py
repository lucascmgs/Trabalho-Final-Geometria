import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import animation
import numpy as np
import random
import flood

plt.rcParams['animation.ffmpeg_path'] = 'D:/ffmpeg/bin/ffmpeg.exe'

gridsize = 400
cmap = colors.ListedColormap(['white','#ffc5d0', '#ffff00', '#22cae0', '#f52ec0', '#603f8b', '#b4fee7', '#a16ae8', '#fd49a0', '#821d30'])
bounds = [0,1,2,3,4,5,6, 7, 8]
norm = colors.BoundaryNorm(bounds, cmap.N)
fig, ax = plt.subplots(figsize = (8, 8))
data = np.zeros((gridsize, gridsize))

updated_image = ax.imshow(data, cmap=cmap, norm=norm)


#ax.grid(which='major', animated = True, axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, gridsize, 1))
ax.set_yticks(np.arange(-.5, gridsize, 1))
ax.set_yticklabels([])
ax.set_xticklabels([])

flood_obj = flood.Flood(gridsize)

def draw_frame(frame_number, *fargs):
    flood_obj = fargs[0]
    if not flood_obj.initialized:
        flood_obj.set_seeds(7)
    else:
        flood_obj.common_flood_with_distance_iteration()

    updated_image = fargs[1]
    updated_image.set_array(flood_obj.data)
    return [updated_image]

anim = animation.FuncAnimation(fig, draw_frame, frames=(data.shape[0]//2), fargs = (flood_obj, updated_image), interval=300, blit=True)
FFwriter = animation.FFMpegWriter()
anim.save("resultd.mp4", writer=FFwriter)