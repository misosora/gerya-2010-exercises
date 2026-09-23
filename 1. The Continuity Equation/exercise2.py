# Exercise 1.2
# Computing and visualizing a 2D velocity field and its divergence

import numpy as np
import matplotlib.pyplot as plt

# Defining the domain
W = 1_000_000.0 # m
H = 1_500_000.0 # m

x = np.linspace(0, W, 100) # horizontal
y = np.linspace(0, H, 100) # vertical

X, Y = np.meshgrid(x, y)

X_km = X / 1000 # converting the horizontal axis to km
Y_km = Y / 1000 # converting the vertical axis to km

# Defining the velocity field scaling values
vx0 = 1.0E-9 # m/s
vy0 = 1.0E-9 # m/s

# Defining the velocity field
VX = -vx0 * np.sin(2 * np.pi * X / W) * np.cos(np.pi * Y / H)
VY = +vy0 * np.cos(2 * np.pi * X / W) * np.sin(np.pi * Y / H)

Vmag = np.sqrt(VX**2 + VY**2) # magnitude

# Computing the divergence of the velocity field
dVXdx = -vx0 * (2 * np.pi / W) * np.cos(2 * np.pi * X / W) * np.cos(np.pi * Y / H)
dVYdy = +vy0 * (np.pi / H)     * np.cos(2 * np.pi * X / W) * np.cos(np.pi * Y / H)
div = dVXdx + dVYdy

# Plotting
fig, axs = plt.subplots(2, 3, figsize=(18, 9))

# 1) Magnitude of the velocity field and vector plot
skip = 5 # spacing for the vector plot
im = axs[0, 0].pcolormesh(X_km, Y_km, Vmag, cmap="inferno")
fig.colorbar(im, ax=axs[0, 0], label="Velocity magnitude (m/s)")
axs[0, 0].quiver(X_km[::skip, ::skip], Y_km[::skip, ::skip],
                 VX[::skip, ::skip], VY[::skip, ::skip],
                 angles="xy", color="white")
axs[0, 0].set_title("Velocity magnitude and vector field")

# 2) Horizontal velocity component
vmax = np.abs(VX).max()
im = axs[0, 1].pcolormesh(X_km, Y_km, VX, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
fig.colorbar(im, ax=axs[0, 1], label="$v_x$ (m/s)")
axs[0, 1].set_title("$v_x$")

# 3) Vertical velocity component
vmax = np.abs(VY).max()
im = axs[0, 2].pcolormesh(X_km, Y_km, VY, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
fig.colorbar(im, ax=axs[0, 2], label="$v_y$ (m/s)")
axs[0, 2].set_title("$v_y$")

# 4) Horizontal derivative of the horizontal velocity component
vmax = np.abs(dVXdx).max()
im = axs[1, 0].pcolormesh(X_km, Y_km, dVXdx, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
fig.colorbar(im, ax=axs[1, 0], label="1/s")
axs[1, 0].set_title(r"$\partial v_x/\partial x$")

# 5) Vertical derivative of the vertical velocity component
vmax = np.abs(dVYdy).max()
im = axs[1, 1].pcolormesh(X_km, Y_km, dVYdy, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
fig.colorbar(im, ax=axs[1, 1], label="1/s")
axs[1, 1].set_title(r"$\partial v_y/\partial y$")

# 6) Divergence of the velocity field
vmax = np.abs(div).max()
im = axs[1, 2].pcolormesh(X_km, Y_km, div, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
fig.colorbar(im, ax=axs[1, 2], label="1/s")
axs[1, 2].set_title(r"Divergence $\nabla\cdot\vec{v}$")

for ax in axs.flat:
    ax.set_xlabel("Length (km)")
    ax.set_ylabel("Depth (km)")
    ax.set_ylim(Y_km.max(), Y_km.min())

fig.suptitle("2D Velocity Field of a Central Upwelling and its Components", fontsize=16)
fig.tight_layout()
plt.show()