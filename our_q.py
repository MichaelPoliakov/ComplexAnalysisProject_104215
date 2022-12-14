import numpy as np  # scientific library to create and manage multi-dimensional arrays and matrices.
import matplotlib.pyplot  as plt
from matplotlib import mlab

# x_coordinates = np.linspace(-2.0, 5.0, 10 ** 2)
# y_coordinates = np.linspace(-2.0, 2.0, 10 ** 2)
# X, Y = np.meshgrid(x_coordinates, y_coordinates)

# fig1 = plt.figure(figsize=(5, 4), dpi=100)
# ax = fig1.gca()
#
# x, y = np.meshgrid(np.arange(-0.8, 10, 0.2),
#                       np.arange(-0.8, 3, 0.2))
#
# c = 2
#
# u = c * x
# v = 0 * y
#
# ax.quiver(x, y, u, v)
#
# plt.show()
#
#
# # x_F, y_F = c , 0
# # fi, xi = -c * Y, c * X
# # plt.streamplot(X, Y, 0*X, c*Y, density=2, linewidth=1, arrowsize=1, arrowstyle=' ->')
# plt.show()


# plt.rcParams['text.usetex'] = True


# t = np.linspace(0.0, 1.0, 100)
# s = np.cos(4 * np.pi * t) + 2
#
# fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
# ax.plot(t, s)
#
# ax.set_xlabel(r'\textbf{time (s)}')
# ax.set_ylabel('\\textit{Velocity (\N{DEGREE SIGN}/sec)}', fontsize=16)
# ax.set_title(r'\TeX\ is Number $\displaystyle\sum_{n=1}^\infty'
#              r'\frac{-e^{i\pi}}{2^n}$!', fontsize=16, color='r')

X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
# X = np.ones(len(Y), dtype=int)

# X, Y = np.mgrid[-10:10:100j, -10:10:100j]

U, V = np.meshgrid(0*X +.25, 0*Y)
Z = np.arange(-10, 10, 1)
fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True, dpi=150)
plt.grid(True)
flow_field = ax.quiver(X, Y, U, V)
field_contour = ax.contour(X,Y, Z)
ax.quiverkey(flow_field, X=0.45, Y=1.1, U=.25,
             label='Flow Field', labelpos='E')

# plt.xlabel(r'$\mathfrak{Re(𝜑)}$') #fontname='Snell Roundhand', fontsize=18)
# plt.ylabel(r'$\mathfrak{Im(𝜑)}$') #', fontname='Snell Roundhand', fontsize= 18)
# plt.title('-cy + i cx') # , fontname='Geneva', fontsize=18)

plt.xlabel(r'x-axis') #fontname='Snell Roundhand', fontsize=18)
plt.ylabel(r'y') #', fontname='Snell Roundhand', fontsize= 18)
plt.title(r'$\Psi$ (x,y)') # , fontname='Geneva', fontsize=18)


# U, V = np.meshgrid(0*X, -2*Y)
# plt.contour(U, 20)

plt.show()