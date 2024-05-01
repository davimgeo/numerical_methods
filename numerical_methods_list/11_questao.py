import numpy as np

def f(x):
    return np.cos(x) + 1 - x

def bissection_method(iterations, root_interval):
    roots_bissection = []
    for i in range(len(root_interval)):
        x0, x1 = root_interval[0], root_interval[1]
        for _ in range(iterations):
            xn = (x0 + x1) / 2
            if f(xn) * f(x0) < 0:
                x1 = xn
            else:
                x0 = xn
        roots_bissection.append(round(xn, 5))

    return roots_bissection

def regula_fasi_method(iteration, root_interval, tolerance= 1e-12):
    roots_regula_fasi = []
    for i in range(len(root_interval)):
        x0, x1 = root_interval[0], root_interval[1]
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

interval = [0.8, 1.6]   #O numpy calcula por padrão em radiano
iteration = 100

root_bissection = bissection_method(iteration, interval)
root_regula_fasi = regula_fasi_method(iteration, interval)

#Os 2 métodos apresentam o mesmo resultado
print(f"Bissection method: {set(root_bissection)}")
print(f"Regula Fasi method: {set(root_regula_fasi)}")
