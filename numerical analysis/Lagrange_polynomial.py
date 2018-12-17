# Lagrange polynomial
import matplotlib.pyplot as plt
import numpy as np

x = [0, 4, 6, 8]
y = [0, 1.3863, 1.7918, 2.1638]

def f(g_x):
    global x, y
    n = len(x)
    sum = 0
    for i in range(n):
        part = 1.0
        for j in range(n):
            if i != j:
                part = part*((g_x - x[j]) / (x[i] - x[j]))
        # print(y[i])
        sum = y[i]*part + sum
    return sum

plt.figure(figsize=(8, 6))
plt.title("1607094243许建明's Lagrange polynomial")
plt.xlabel("x")
plt.ylabel("f(x)")
g_x = np.arange( x[0], x[len(x)-1], 0.01)
plt.plot(g_x, f(g_x))
plt.scatter(x, y)
plt.plot(g_x, f(g_x))
plt.show()