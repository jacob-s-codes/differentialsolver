import numpy as np

step_size = 0.04

def eulers_method(x, y, func, y_val):
    y_not = y
    x_not = x
    steps = int((y_val - x_not) / step_size)
    for i in range(steps):
        y = y_not + step_size*(func(x_not, y_not))
        x_not += step_size
        y_not = y
    return y

# Any function of x and y should work
def func(x, y):
    return 3*x+y


ans = eulers_method(0, -1, func, 0.2)
print("{:.5f}".format(ans))