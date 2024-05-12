import numpy as np
import math
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D     # noqa: F401 unused import

# ----------------------------------------------
# Part 1 - A
# ----------------------------------------------

# Define the function and interval
f = lambda x: np.sin(x) + 1
a, b = -np.pi, np.pi
x = np.linspace(a, b, 400)
y = f(x)

# Create plot side by side
fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # Adjust subplot to horizontal layout

# Subinterval partitions
n = 4
dx = (b - a) / n
x_sub = np.linspace(a, b, n + 1)

# Left-hand endpoint Riemann Sum
x_left = x_sub[:-1]
y_left = f(x_left)
axs[0].bar(x_left, y_left, width=dx, alpha=0.3, align='edge', edgecolor='blue', color='cyan')
axs[0].plot(x, y, 'r-')
axs[0].set_title("Left-hand Endpoint Riemann Sum")

# Right-hand endpoint Riemann Sum
x_right = x_sub[1:]
y_right = f(x_right)
axs[1].bar(x_left, y_right, width=dx, alpha=0.3, align='edge', edgecolor='green', color='lightgreen')
axs[1].plot(x, y, 'r-')
axs[1].set_title("Right-hand Endpoint Riemann Sum")

# Midpoint Riemann Sum
x_mid = (x_left + x_right) / 2
y_mid = f(x_mid)
axs[2].bar(x_mid, y_mid, width=dx, alpha=0.3, color='yellow', align='center', edgecolor='purple')
axs[2].plot(x, y, 'r-')
axs[2].set_title("Midpoint Riemann Sum")

# Show plots
plt.tight_layout()
plt.show()

# ----------------------------------------------
# Part 1 - C.1 
# ----------------------------------------------

def riemann_sum(n):
    a = 1
    b = math.e
    delta_x = (b - a) / n
    sum_result = 0
    for i in range(1, n+1):
        x_mid = a + ((2*i - 1) * delta_x) / 2
        sum_result += math.log(x_mid) * delta_x
    return sum_result

# Number of subintervals
n = 1000000
result = riemann_sum(n)
print ("The Riemann sum approximation for the integral of ln(x) from 1 to e is:" ,result)

# ----------------------------------------------
# Part 1 - C.2 
# ----------------------------------------------

def f(x):
    return x**2 - x**3

def riemann_sum2(n):
    delta_x = 1 / n
    sum_result = 0
    for k in range(1, n+1):
        x_k = -1 + k / n
        sum_result += f(x_k) * delta_x
    return sum_result

# Number of subintervals
n = 1000000
result = riemann_sum2(n)
print("The Riemann sum approximation of the integral of x^2-x^3 from -1 to 0 is:",result)