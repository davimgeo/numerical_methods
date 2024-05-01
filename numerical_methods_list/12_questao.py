import numpy as np

def f(x, parameters):
    function = 0.0
    for n, p in enumerate(parameters):
        function += p*x**n
    return function
    
def derivative(x0, parameters, h=1e-7):
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

def newton_raphson(root_interval, parameters, iterations):
    roots = []
    for i in range(len(root_interval)):
        xn = (root_interval[i][0] + root_interval[i][1]) / 2
        for _ in range(iterations):
            xn -= f(xn, parameters) / derivative(xn, parameters)
        roots.append(round(xn, 5))
    return roots

N = 10  # Número N da raiz
x = np.linspace(-10, 10, 1001)

functions = {3: [-N, 0, 0, 1],      # Polinômio x^3 - N cuja raiz aproxima o valor de sqrt(N)
             4: [-N, 0, 0, 0, 1]}   # Polinômio x^4 - N cuja raiz aproxima o valor de sqrt(N)

for element in functions:
    #y = f(x, functions[element])
    root_interval = bolzano(y)
    root_newton = newton_raphson(root_interval, functions[element], iterations=100)
    positive_roots = [i for i in root_newton if i > 0]
    print(f"Newton-Raphson method for N^1/{element}: {positive_roots}")
