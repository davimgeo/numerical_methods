import numpy as np

def factorial(num):
    if num == 0: return 1
    return num * factorial(num - 1)

def cosine_mclaurin_series(point, iterations, tolerance=1e-7):
    result = 0
    for m in range(iterations):
        result += (-1)**(m) * point**(2*m) / factorial(2*m)
        if abs(result - np.cos(point)) < tolerance:
            print(f"A partir de m = {m} a série de McLaurin se "
                  f"aproxima da função f(x) a um erro menor que {tolerance}")
            return
    print(f"É necessário mais iterações para diminuir o erro")
          
cosine_mclaurin_series(point=np.pi, iterations=12)