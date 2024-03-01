import numpy as np
import matplotlib.pyplot as plt

def f(x, parameters):
    function = 0.0
    for n, p in enumerate(parameters):
        function += p*x**n
        
    return function
    
def derivative(x0, h= 1e-7):
   dydx = (f(x0 + h, parameters) - f(x0, parameters)) / h
   return dydx

def bolzano(y):
    """
    if f(x0)*f(x1) < 0 means that are at least one root bounded in [a, b]
    if f(x0)*f(x1) = 0 means that or x0, or x1 are a root
    if f(x0)*f(x1) > 0 means that there's no root in interval [x0, x1]
    """
    if len(y) == 0:
        raise ValueError("Input sequence must not be empty.")

    roots_interval = []
    for n in range(1, len(y)):
       product = y[n]*y[n-1]
       if product < 0:
        roots_interval.append([round(x[n], 4), round(x[n-1], 4)])
       elif product == 0:
           roots_interval.append([round(x[n], 4), round(x[n-1], 4)])  
           
    return roots_interval

def newton_raphson(iterations):
   roots = []
   for i in range(len(root_interval)):
        xn = root_interval[i][0]
        for _ in range(iterations):
            xn -= f(xn, parameters) / derivative(xn)

        roots.append(round(xn, 5))
   return roots

def bissection_method(iterations):
    roots_bissection = []
    for i in range(len(root_interval)):
        x0, x1 = root_interval[i][0], root_interval[i][1]
        for _ in range(iterations):
            xn = (x0 + x1) / 2
            if f(xn, parameters) * f(x0, parameters) < 0:
                x1 = xn
            else:
                x0 = xn
        roots_bissection.append(round(xn, 5))

    return roots_bissection

def regula_fasi_method(f, root_interval, iteration, tolerance= 1e-5):
    roots_regula_fasi = []
    for i in range(len(root_interval)):
        x0, x1 = root_interval[i][0], root_interval[i][1]
        for _ in range(iteration):
            slope = (f(x1) - f(x0)) / (x1 - x0)

            xn = x0 - f(x0) / slope
            if abs(xn - x0) < tolerance:
                break
            elif f(x0) * f(xn) < 0:
                x1 = xn
            else:
                x0 = xn

        roots_regula_fasi.append(round(xn, 5))

    return roots_regula_fasi


parameters = np.array([-1, 3, 2])
x = np.linspace(-10, 10, 1001)
y = f(x, parameters)

root_interval = bolzano(y)
root_newton = newton_raphson(100)
root_bissection = bissection_method(100)
root_regula_fasi = regula_fasi_method(100)

#print(f"These are the intervals of possible roots: {root_interval}")
print(f"Newton-Raphson method: {root_newton}")
print(f"Bissection method: {root_bissection}")
print(f"Regula Fasi method: {root_regula_fasi}")
