import math                             # provides the mathenathical functions defined by the C standard.
import numpy as np                      # scientific library to create and manage multi-dimensional arrays and matrices.
from matplotlib import pyplot as plt    # 2D plotting library for visualizing results.


N = 30                                # number of points in each direction
x_start, x_end = -50.0, 50.0          # boundaries in the x-direction
y_start, y_end = -50.0, 50.0          # boundaries in the y-direction
x = np.linspace(x_start, x_end, N)    # creates a 1D-array with the x-coordinates
y = np.linspace(y_start, y_end, N)    # creates a 1D-array with the y-coordinates
X, Y = np.meshgrid(x, y)              # generates a mesh grid

# plot the streamlines
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(1, figsize=(width, height))
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)

# define R2 vector field
u = 2 + (Y**2 - X**2) / (X**2 + Y**2)
v = 2 + (-2 * X * Y) / (X ** 2 + Y ** 2)

plt.quiver(X, Y, u, v)
plt.title('3.7 Field')

plt.show()