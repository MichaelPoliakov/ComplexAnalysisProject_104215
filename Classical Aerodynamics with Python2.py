import math                             # provides the mathenathical functions defined by the C standard.
import numpy as np                      # scientific library to create and manage multi-dimensional arrays and matrices.
from matplotlib import pyplot as plt    # 2D plotting library for visualizing results.


N = 50                                # number of points in each direction
x_start, x_end = -2.0, 2.0            # boundaries in the x-direction
y_start, y_end = -1.0, 1.0            # boundaries in the y-direction
x = np.linspace(x_start, x_end, N)    # creates a 1D-array with the x-coordinates
y = np.linspace(y_start, y_end, N)    # creates a 1D-array with the y-coordinates

# print('x = ', x)
# print('y = ', y)

X, Y = np.meshgrid(x, y)              # generates a mesh grid

# plot the grid of points
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(0, figsize=(width, height))
plt.xlabel('x-axis   ||    Real(z)', fontsize=13)
plt.ylabel('y = f(x) ||    Im(z)', fontsize=13)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.scatter(X, Y, s=5, color='#CD2305', marker='o')
plt.show()

strength_source = 5.0                      # source strength
x_source, y_source = -1.0, 0.0             # location of the source

# compute the velocity field on the mesh grid
u_source = (strength_source / (2 * math.pi) *
            (X - x_source) / ((X - x_source)**2 + (Y - y_source)**2))
v_source = (strength_source / (2 * math.pi) *
            (Y - y_source) / ((X - x_source)**2 + (Y - y_source)**2))

# plot the streamlines
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(1, figsize=(width, height))
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
# plot the stream lines
plt.streamplot(X, Y, u_source, v_source,
                  density=2, linewidth=1, arrowsize=2, arrowstyle='->')
# put a red dot right on the source
plt.scatter(x_source, y_source,
               color='#CD2305', s=80, marker='o')

plt.show()