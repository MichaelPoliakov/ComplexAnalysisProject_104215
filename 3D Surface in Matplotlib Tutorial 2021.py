import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d
from matplotlib import cm
import numpy as np
from mpl_toolkits import mplot3d
from mpmath import plot

fig_9 = plt.figure(figsize=(8, 5), dpi=100)
axes_9 = fig_9.add_axes([0.1, 0.1, 0.9, 0.9], projection='3d')

z_3 = 15 * np.random.random(100)
x_3 = np.sin(z_3) * np.random.randn(100)
y_3 = np.cos(z_3) * np.random.randn(100)
# axes_9.scatter3D(x_3, y_3, z_3, c=z_3, cmap='Blues')
# plt.show()

def get_z(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

x_4 = np.linspace(-6, 6, 30)
y_4 = np.linspace(-6, 6, 30)

x_4, y_4 = np.meshgrid(x_4, y_4)
z_4 = get_z(x_4, y_4)

axes_9.view_init(35, 55)
# axes_9.scatter3D(x_4, y_4, z_4, cmap=cm.coolwarm)
#axes_9.plot_surface(x_4, y_4, z_4, cmap=cm.coolwarm)
#axes_9.contour3D(x_4, y_4, z_4, 250, cmap='PRGn_r')

axes_9.set_xlabel('x')
axes_9.set_ylabel('y')
axes_9.set_zlabel('z = f(x,y)')

#axes_9.plot_wireframe(x_4, y_4, z_4, color='yellow')
axes_9.plot_surface(x_4, y_4, z_4, rstride=1 ,cstride=1, cmap='BrBG', edgecolor= 'none')
plt.show()