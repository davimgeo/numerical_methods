import numpy as np

def f(x):
    return x * np.cos(x / (x - 2))

def function_derivative(x, h=1e-7):
    dydx = ((x + h) * np.cos((x + h) / (x + h - 2)) - x * np.cos(x / (x - 2))) / h
    return dydx

def newton_raphson(root_interval, iterations):
    roots = []
    for i in range(len(root_interval)):
        xn = (root_interval[0] + root_interval[1]) / 2
        for _ in range(iterations):
            xn -= f(xn) / function_derivative(xn)
        roots.append(round(xn, 5))
    return roots

root_interval = [0.8, 1.6]
root_newton = newton_raphson(root_interval, iterations=100)

print(f"Newton-Raphson method: {set(root_newton)}")
