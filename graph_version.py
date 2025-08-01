import numpy as np
import matplotlib.pyplot as plt

step_size = 0.04

def eulers_method(x, y, func, y_val):
    y_vals = [y]
    x_vals = [x]
    while x < y_val:
        y = y + step_size*(func(x, y))
        y_vals.append(y)
        x_vals.append(x)
        x += step_size
    return x_vals, y_vals

# Any function of x and y should work
def func(x, y):
    return 3*x+y


x_vals, y_vals = eulers_method(-4, 9.03, func, 4)

plt.plot(x_vals, y_vals, label="Euler's method", marker='o')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
# print("{:.5f}".format(ans))