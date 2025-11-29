import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# --- EASING FUNCTIONS ---
def ease_out_cubic(t):
    return 1 - (1 - t)**3

# --- SETUP FIGURE ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# --- INITIAL POSITIONS ---
earth_pos = np.array([0, 0])
n = 12

angles = np.linspace(0, 2*np.pi, n, endpoint=False)
radius = 1.2

galaxy_start = np.stack([radius*np.cos(angles), radius*np.sin(angles)], axis=1)

galaxy_final_x = 1.3
galaxy_final_y = np.linspace(-1, 1, n)

galaxy_target = np.stack([np.full(n, galaxy_final_x), galaxy_final_y], axis=1)

# --- PLOTS ---
earth_plot, = ax.plot([], [], 'wo', markersize=12)
galaxy_plots = [ax.plot([], [], 'ro')[0] for _ in range(n)]

# --- ANIMATION UPDATE ---
def update(frame):
    t = frame / 100
    smooth = ease_out_cubic(t)

    # Earth slides left
    earth_x = 0 - smooth * 1.5
    earth_plot.set_data([earth_x], [0])

    # Galaxies interpolate from circle → vertical line
    interp_positions = galaxy_start * (1 - smooth) + galaxy_target * smooth

    for i, point in enumerate(galaxy_plots):
        point.set_data([interp_positions[i, 0]], [interp_positions[i, 1]])

    return []

# --- RUN ANIMATION ---
anim = FuncAnimation(fig, update, frames=101, interval=16)
plt.show()