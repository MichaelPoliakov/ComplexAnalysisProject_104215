# Math and plotting libraries:

import sympy
from sympy.physics.vector import *
from sympy import Curve, line_integrate, E, ln, diff
import numpy as np
import matplotlib.pyplot as plt

# Establish coordinates for calculus
R = ReferenceFrame('R')
x, y = R[0], R[1]

# Establish coordinates for plots
X, Y = np.meshgrid(np.arange(-10, 11), np.arange(-10, 11))


# ~~~~~~~~~~~~~~~~~~~~~
# LOTS OF BORING STUFF:
# ~~~~~~~~~~~~~~~~~~~~~

# Turn a 2-D vector to a tuple
def vector_components(vectorField):
    return vectorField.dot(R.x), vectorField.dot(R.y)


# Apply a field to a discrete set of points X, Y
def discretize_field(field):
    computeVector = sympy.lambdify((x, y), field)
    return computeVector(X, Y)


def plot_streamlines(vectorField):
    data = discretize_field(vector_components(vectorField))
    plt.figure()
    plt.streamplot(X, Y, data[0], data[1], density=2, linewidth=1, arrowsize=2, arrowstyle='->')


# Return a scalar potential function of a vector field
def integrateGradient(gradientField):
    return sympy.integrate(gradientField.dot(R.x), x) + sympy.integrate(gradientField.dot(R.y), y).subs(x, 0)


# ~~~~~~~~~~~~~~~~~~~~~
# THE FUN STARTS HERE!
# ~~~~~~~~~~~~~~~~~~~~~

# The given vector field. (Read R.x and R.y like the unit vectors i-hat and j-hat.)
u, v = (-2 * y * (1 - x ** 2)), (2 * x * (1 - y ** 2))
velocity = u * R.x + v * R.y

# Plot the vector field:
plot_streamlines(velocity)

# Find the stagnation points.
# The solve(v) function gives solutions for v = 0
stagPoints = sympy.solve(vector_components(velocity), [x, y])
for (x_point, y_point) in stagPoints:
    plt.scatter(x_point, y_point, color='#CD2305', s=80, marker='o')

# Does the field satisfy conservation of mass for an incompressible flow?
print(f"The divergence of the field is {divergence(velocity, R)}.")

# Is it a potential flow?
print(f"The vorticity of the field is {curl(velocity, R)}.")

# Find the stream function
u, v = velocity.dot(R.x), velocity.dot(R.y)
streamField = u * R.y - v * R.x
print(f"Stream function {integrateGradient(streamField)}")

plt.show()

# Establish coordinates for calculus
R = ReferenceFrame('R')
x, y = R[0], R[1]

# Establish coordinates for plots
X, Y = np.meshgrid(np.arange(-10, 11), np.arange(-10, 11))


# ~~~~~~~~~~~~~~~~~~~~~
# LOTS OF BORING STUFF:
# ~~~~~~~~~~~~~~~~~~~~~

# Turn a 2-D vector to a tuple
def vector_components(vectorField):
    return (vectorField.dot(R.x), vectorField.dot(R.y))


# Return a scalar potential function of a vector field
def integrateGradient(gradientField):
    return sympy.integrate(gradientField.dot(R.x), x) + sympy.integrate(gradientField.dot(R.y), y).subs(x, 0)


# Apply a field to a discrete set of points X, Y
def discretize_field(field):
    computeVector = sympy.lambdify((x, y), field)
    return computeVector(X, Y)


def plot_vector_field(vectorField):
    data = discretize_field(vector_components(vectorField))
    plt.figure()
    plt.quiver(X, Y, data[0], data[1])


def plot_contour(scalarField):
    data = discretize_field(scalarField)
    plt.figure()
    plt.contour(X, Y, data, 6, colors='k')


# ~~~~~~~~~~~~~~~~~~~~~
# THE FUN STARTS HERE!
# ~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~
# Example 2:
# ~~~~~~~~~~~~~~~~~~~~~

psi = -(y ** 3) / 3  # Stream function
u, v = diff(psi, y), -diff(psi, x)
velocity = u * R.x + v * R.y

# Plot
plot_vector_field(velocity)
print("Divergence:", divergence(velocity, R), "Curl:", curl(velocity, R), ".")

# Find the circulation around a box
from sympy.abc import t

circulationfun = curl(velocity, R).dot(R.z)
l1, l2, l3, l4 = Curve([1, t], (t, 0, 1)), Curve([-t, 1], (t, 0, 1)), Curve([0, -t], (t, 0, 1)), Curve([t, 0],
                                                                                                       (t, 0, 1));
circulation = line_integrate(circulationfun, l1, [x, y]) + line_integrate(circulationfun, l2, [x, y]) + line_integrate(
    circulationfun, l3, [x, y]) + line_integrate(circulationfun, l4, [x, y])
print(f"The total circulation around the curve is {circulation}")

# ~~~~~~~~~~~~~~~~~~~~~
# Example 3:
# ~~~~~~~~~~~~~~~~~~~~~

phi = -(x ** 3) / 3  # Velocity potential
velocity = gradient(phi, R)

# Plot
plot_vector_field(velocity)
print("Divergence:", divergence(velocity, R), "Curl:", curl(velocity, R), ".")

# Derive the pressure field
rho = 1.225  # density of air
u, v = velocity.dot(R.x), velocity.dot(R.y)
pressure = integrateGradient(-rho * (u * diff(u, x) * R.x + v * diff(v, y) * R.y))

# Plot the relative pressure
plot_contour(pressure)

plt.show()