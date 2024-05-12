import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad


# Define the function for f(x) = sin(x) + 1
def functionSinPlusOne(x):
    return np.sin(x) + 1


# Define the function for f(x) = 3x + 2x^2
def function3xPlus2xSquared(x):
    return 3 * x + 2 * x ** 2


# Define the function for f(x) = ln(x)
def functionLog(x):
    return np.log(x)


# Define the function for f(x) = x^2 - x^3
def functionXsquaredMinusXcubed(x):
    return x ** 2 - x ** 3


# Function to compute Riemann sum given a function, interval, and number of subintervals
def computeRiemannSum(function, a, b, n, method='midpoint'):
    deltaX = (b - a) / n
    if method == 'left':
        endpoints = np.linspace(a, b - deltaX, n)
    elif method == 'right':
        endpoints = np.linspace(a + deltaX, b, n)
    elif method == 'midpoint':
        endpoints = np.linspace(a + deltaX / 2, b - deltaX / 2, n)
    else:
        raise ValueError("Method should be 'left', 'right', or 'midpoint'.")

    riemannSum = np.sum(function(endpoints) * deltaX)
    return riemannSum


# Numerically evaluate the integral of f(x) = sin(x) + 1 over the interval [-pi, pi]
numericalIntegralSinPlusOne = quad(functionSinPlusOne, -np.pi, np.pi)[0]

# Plot the function f(x) = sin(x) + 1 and its Riemann rectangles
x = np.linspace(-np.pi, np.pi, 1000)
y = functionSinPlusOne(x)
plt.figure(figsize=(14, 7))

# Partition the interval and add rectangles for each Riemann sum type
for method, subplot in zip(['left', 'right', 'midpoint'], [1, 2, 3]):
    plt.subplot(1, 3, subplot)
    plt.plot(x, y, label=f'f(x) = sin(x) + 1')

    for i in range(4):
        if method == 'left':
            x_rect = np.linspace(-np.pi, np.pi - np.pi / 2, 4)[i]
            width = np.pi / 2
            height = functionSinPlusOne(x_rect)
        elif method == 'right':
            x_rect = np.linspace(-np.pi + np.pi / 2, np.pi, 4)[i]
            width = np.pi / 2
            height = functionSinPlusOne(x_rect)
        elif method == 'midpoint':
            x_rect = np.linspace(-np.pi + np.pi / 4, np.pi - np.pi / 4, 4)[i]
            width = np.pi / 2
            height = functionSinPlusOne(x_rect)
        plt.bar(x_rect, height, width=width, align='edge', edgecolor='black', alpha=0.2)

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Riemann Sum: {method.capitalize()} Endpoint')
    plt.legend()
plt.tight_layout()
plt.show()

# Compute the Riemann sum for f(x) = ln(x) over [1, e]
riemannSumLog = computeRiemannSum(functionLog, 1, np.e, 1000000, method='midpoint')

# Output the results
output = numericalIntegralSinPlusOne, riemannSumLog

# Display the results
print(f"Numerical integral of f(x) = sin(x) + 1 over [-π, π]: {numericalIntegralSinPlusOne}")
print(f"Riemann sum of f(x) = ln(x) over [1, e] (midpoint method): {riemannSumLog}")

np.random.seed(42)  # For reproducibility
timeIntervals = np.arange(0, 31)  # 0 to 30 minutes
downloadRates = np.abs(np.random.normal(50, 10, size=31))  # Mean rate: 50 Mbps, std: 10


def fitFunction(t, a, b, c, d):
    return a * t ** 3 + b * t ** 2 + c * t + d


params, _ = curve_fit(fitFunction, timeIntervals, downloadRates)


# Define the continuous download rate function R(t)
def continuousDownloadRate(t):
    a, b, c, d = params
    return fitFunction(t, a, b, c, d)


totalDataDownloaded = quad(continuousDownloadRate, 0, 30)[0]

# Output the results
print(f"Total data downloaded over 30 minutes: {totalDataDownloaded} MB")

# Plotting the simulated data and the fitted function
plt.figure(figsize=(10, 5))
plt.scatter(timeIntervals, downloadRates, color='red', label='Simulated Data Rates (Mbps)')
tModel = np.linspace(0, 30, 100)
plt.plot(tModel, continuousDownloadRate(tModel), label='Fitted Rate Function R(t)', color='blue')
plt.xlabel('Time (minutes)')
plt.ylabel('Download Rate (Mbps)')
plt.title('Download Rate over Time')
plt.legend()
plt.grid(True)
plt.show()
