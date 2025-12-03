import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from helpers import *

galaxies = parse_galaxies('NED30.5.1-D-17.1.2-20200415.csv')

# --- EASING FUNCTIONS ---
def ease_out_cubic(t):
    return 1 - (1 - t)**3

def ease_in_out_cubic(t):
    if t < 0.5:
        return 4 * t**3
    return 1 - pow(-2 * t + 2, 3) / 2

# --- SETUP FIGURE ---
FIG_W = 700
FIG_H = 700
DPI = 100

fig, ax = plt.subplots(figsize=(FIG_W / DPI, FIG_H / DPI), dpi=DPI)
fig.patch.set_facecolor("black")
ax.set_facecolor("white")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')
fig.subplots_adjust(0,0,1,1)
# --- INITIAL POSITIONS ---
earth_pos = np.array([0, 0])
n = 30
galaxies = heap_choose(galaxies, n)

distances = np.array([g.distance for g in galaxies])
max_dist = distances.max()

scaled_r = 0.2 + 1.8 * (distances / max_dist)

n = len(galaxies)
d_norm = (distances - distances.min()) / (distances.max() - distances.min())
angles = np.linspace(0, 10*np.pi, n)

galaxy_start = np.stack([
    scaled_r * np.cos(angles),
    scaled_r * np.sin(angles)
], axis=1)

norm = (distances - distances.min()) / (distances.max() - distances.min())

final_x = -1 + 2 * norm
final_y = np.zeros(n)

galaxy_target = np.stack([final_x, final_y], axis=1)

# --- PLOTS ---
earth_plot, = ax.plot([0], [0], 'co', markersize=12)
scatter = ax.scatter(galaxy_start[:,0], galaxy_start[:,1], s=6, c='white')

# --- ANIMATION UPDATE ---
def update(frame):
    t = frame / 100
    smooth = ease_in_out_cubic(t)

    earth_x = 0 - smooth * 1.8
    earth_plot.set_data([earth_x], [0])

    interp = galaxy_start * (1 - smooth) + galaxy_target * smooth
    scatter.set_offsets(interp)

    return [earth_plot, scatter]#[earth_plot, bloom, scatter]

annot = ax.annotate(
    "",
    xy=(0,0),
    xytext=(10,10),
    textcoords="offset points",
    bbox=dict(boxstyle="round", fc="black", ec="white"),
    color="white",
    fontsize=8
)
annot.set_visible(False)

# --- RUN ANIMATION ---
anim = FuncAnimation(fig, update, frames=101, interval=16, blit=True, repeat=False)
plt.show()
