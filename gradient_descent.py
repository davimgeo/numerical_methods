import numpy as np
import matplotlib.pyplot as plt

def polynomial_function(x, parameters):
        """
        make a polynomial 
        """
        function = 0.0
        for n, p in enumerate(parameters):
            function += p*x**n 

        return function

def apply_noise(y):
    """
    apply gausian noise to y 
    """
    std = 0.3*np.abs(y)
    noise = std*np.random.rand(len(y))
    #noise = np.random.poisson(lam= 0.4, size= len(y))

    return y + noise

def gradient_descent(x, y_noise, learning_rate, iterations):
    """
    finds minimum of cost function
    """
    n = len(y_noise)

    a0 = a1 = 0.0
    for _ in range(iterations):
        dP_da0 = (-2/n)*np.sum(y_noise - (a0 + a1*x))
        dP_da1 = (-2/n)*np.sum(x*(y_noise - (a0 + a1*x)))

        a0 -= learning_rate*dP_da0
        a1 -= learning_rate*dP_da1

    return a0, a1

def plot_graph(x):
    """
    plots a graph of noise data and a linear regression model
    """
    fig, ax = plt.subplots(nrows= 1, ncols= 1, figsize= (10,5))

    ax.plot(x, real_coef[0] + real_coef[1]*x)
    ax.scatter(x, y_noise, s= 10)

    fig.tight_layout()
    plt.grid(True)
    plt.show()

    return fig, ax

parameters = np.array([3, 5])
x = np.linspace(-5, 5, 101)
y = polynomial_function(x, parameters)

y_noise = apply_noise(y)
real_coef = gradient_descent(x, y_noise, learning_rate= 0.001, iterations= 10_000)

plot_graph(x)

print(f"{real_coef}") 