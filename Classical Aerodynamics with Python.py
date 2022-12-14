import math                             # provides the mathenathical functions defined by the C standard.
import numpy as np                      # scientific library to create and manage multi-dimensional arrays and matrices.
from matplotlib import pyplot as plt    # 2D plotting library for visualizing results.


def cartesian_grid_of_points(N=50, x_start=-2.0 , x_end=2.0, y_start=-1.0, y_end=1.0):
    # N = 50                                # number of points in each direction
    # x_start, x_end = -2.0, 2.0            # boundaries in the x-direction
    # y_start, y_end = -1.0, 1.0            # boundaries in the y-direction
    x = np.linspace(x_start, x_end, N)    # creates a 1D-array with the x-coordinates
    y = np.linspace(y_start, y_end, N)    # creates a 1D-array with the y-coordinates

    # print('x = ', x)
    # print('y = ', y)

    X, Y = np.meshgrid(x, y)              # generates a mesh grid
    return X, Y


def plotting_grid_of_points(X, Y, x_start=-2.0 , x_end=2.0, y_start=-1.0, y_end=1.0):
    # plot the grid of points
    width = 10.0
    height = (y_end - y_start) / (x_end - x_start) * width
    plt.figure(figsize=(width, height))
    plt.xlabel('x-axis   ||    Real(z)', fontsize=13)
    plt.ylabel('y = f(x) ||    Im(z)', fontsize=13)
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)
    plt.scatter(X, Y, s=5, color='#CD2305', marker='o')
    plt.show()


X, Y = cartesian_grid_of_points()
plotting_grid_of_points(X, Y)