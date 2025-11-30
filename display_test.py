import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# --- EASING FUNCTIONS ---
def ease_out_cubic(t):
    return 1 - (1 - t)**3

def ease_in_out_cubic(t):
    if t < 0.5:
        return 4 * t**3
    return 1 - pow(-2 * t + 2, 3) / 2

# --- SETUP FIGURE ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# --- INITIAL POSITIONS ---
earth_pos = np.array([0, 0])
n = 50

angles = np.linspace(0, 2*np.pi, n, endpoint=False)
radius = np.linspace(0.8, 1.6, n, endpoint=False)

galaxy_start = np.stack([radius*np.cos(angles), radius*np.sin(angles)], axis=1)

galaxy_final_x = np.linspace(-1, 1, n)
galaxy_final_y = np.zeros(n)       # ✔ FIX: make this an array, not a scalar

galaxy_target = np.stack([galaxy_final_x, galaxy_final_y], axis=1)

# --- PLOTS ---
earth_plot, = ax.plot([0], [0], 'wo', markersize=12)  # ✔ FIX: start visible
galaxy_plots = [ax.plot([0], [0], 'ro')[0] for _ in range(n)]  # ✔ FIX: start visible

# --- ANIMATION UPDATE ---
def update(frame):
    t = frame / 100
    smooth = ease_in_out_cubic(t)

    # Earth slides left
    earth_x = 0 - smooth * 1.5
    earth_plot.set_data([earth_x], [0])

    # Galaxies interpolate from circle to line
    interp_positions = galaxy_start * (1 - smooth) + galaxy_target * smooth

    for i, point in enumerate(galaxy_plots):
        point.set_data([interp_positions[i, 0]], [interp_positions[i, 1]])

    return [earth_plot] + galaxy_plots

# --- RUN ANIMATION ---
anim = FuncAnimation(fig, update, frames=101, interval=16, blit=True)
plt.show()
