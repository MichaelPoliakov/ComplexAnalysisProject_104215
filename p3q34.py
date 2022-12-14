import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


delta = 0.5
x = np.arange(-10, 10.0, delta)
y = np.arange(-10, 10.0, delta)
X, Y = np.meshgrid(x, y)
Phi = X**2 - Y**2
Psi = 2*X*Y

fig, ax = plt.subplots()

phi_x, phi_y = 2*X, -2*Y

plt.quiver(X, Y, phi_x, phi_y)
CS = ax.contour(X, Y, Phi, colors= 'r')
ax.contour(X, Y, Psi, colors= 'b')
# ax.set_title('Simplest default with labels')
plt.title('3.2')
plt.show()