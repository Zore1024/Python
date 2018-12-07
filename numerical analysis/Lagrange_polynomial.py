# Lagrange polynomial
import matplotlib.pyplot as plt
import numpy as np

x = [1, 4.0, 6]
y = [0, 1.3863, 1.7918]

def f(temp_x):
    global x, y
    n = len(x)
    return ((temp_x - x[1]) / (x[0] - x[1]))*((temp_x - x[2]) / (x[0] - x[2]))*y[0] \
+ ((temp_x - x[0]) / (x[1] - x[0]))*((temp_x - x[2]) / (x[1] - x[2]))*y[1] \
+ ((temp_x - x[0]) / (x[2] - x[0]))*((temp_x - x[1]) / (x[2] - x[1]))*y[2]

plt.figure(figsize=(8, 6))
plt.title("1607094243许建明's Lagrange polynomial")
plt.xlabel("x")
plt.ylabel("f(x)")
g_x = np.arange( x[0], x[len(x)-1], 0.01)
plt.scatter(x, y)
plt.plot(g_x, f(g_x))
plt.show()
