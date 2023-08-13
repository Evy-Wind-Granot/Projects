import numpy as np
from math import sin
import matplotlib.pyplot as plt

# Define the original function
def f(x):
    return sin(x)

# Define the range of x values
dx = 1
x_values = np.arange(0, 20, dx)

# Calculate the y values for the original function
sin_x = [x for x in np.arange(0,20,dx)]
sin_y = [f(x) for x in x_values]

# Calculate the derivative using np.gradient()
sin_deriv = np.gradient(sin_y, dx)

plt.plot(sin_x, sin_y)
plt.plot(sin_x, sin_deriv)
plt.show()