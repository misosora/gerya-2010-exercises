# Exercise Introduction.2
# Visualizing sine and cosine functions in 2D and 3D

import numpy as np
import matplotlib.pyplot as plt

angles = np.linspace(-2 * np.pi, 2 * np.pi, 1000) # from -2π to 2π with 1000 points

# 2D plotting
y_sin = np.sin(angles)
y_cos = np.cos(angles)

plt.figure(figsize=(10, 5))

plt.plot(angles, y_sin, label='sin(x)', color='pink', linewidth=2)
plt.plot(angles, y_cos, label='cos(x)', color='purple', linewidth=2)

plt.title('Sine and Cosine Functions in 2D')
plt.xlabel('x (rad)')
plt.ylabel('Amplitude')

plt.grid()
plt.legend()
plt.show()

# 3D plotting
x_cos = np.cos(angles)
y_sin = np.sin(angles)
z_angles = angles

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_cos, y_sin, z_angles, color='green', linewidth=2)

ax.set_title('Sine and Cosine Functions in 3D')
ax.set_xlabel('sin(x)')
ax.set_ylabel('cos(x)')
ax.set_zlabel('x (rad)')

plt.show()