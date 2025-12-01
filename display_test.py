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
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor("black")
ax.set_facecolor("white")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# --- INITIAL POSITIONS ---
earth_pos = np.array([0, 0])
n = 20
galaxies = heap_choose(galaxies, n)

distances = np.array([g.distance for g in galaxies])
max_dist = distances.max()

scaled_r = 0.2 + 2.2 * (distances / max_dist)

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
galaxy_plots = [ax.plot([0], [0], 'wo', markersize=4)[0] for _ in range(n)]

# --- ANIMATION UPDATE ---
def update(frame):
    t = frame / 100
    smooth = ease_in_out_cubic(t)

    # Earth slides left
    earth_x = 0 - smooth * 2
    earth_plot.set_data([earth_x], [0])

    # Galaxies interpolate from circle to line
    interp_positions = galaxy_start * (1 - smooth) + galaxy_target * smooth

    for i, point in enumerate(galaxy_plots):
        point.set_data([interp_positions[i, 0]], [interp_positions[i, 1]])

    return [earth_plot] + galaxy_plots

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

# Extract galaxy names for tooltips
galaxy_names = [g.name for g in galaxies]

# --- RUN ANIMATION ---
anim = FuncAnimation(fig, update, frames=101, interval=16, blit=True, repeat=False)
plt.show()
