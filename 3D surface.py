import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-1, 4, np.exp(-4)) # 25e-4 works, 25e-5 my computer fail to calculate (exit 137)
Y = np.arange(-1, 4, np.exp(-4)) # or np.linspace()
X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
Z = X**2 - Y**2

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=''
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-5.01, 5.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()