def define_error(exact_value, calculated_value, type_error):
    """
    Digite 1 para calcular o erro absoluto
    Digite 2 para calcular o erro relativo
    Digite 3 para calcular o erro relativo percentual
    """
    errors = {1: lambda x, y: abs(x - y),
              2: lambda x, y: abs(x - y) / x,
              3: lambda x, y: 100*abs(x - y) / x}
    return errors[type_error](exact_value, calculated_value)

a = [define_error(exact_value=1.0, calculated_value=0.999, type_error=i) for i in range(1, 4)]
print(f"Letra A - Erro absoluto: {a[0]:.3f}, Erro relativo: {a[1]:.3f} e Erro relativo percentual: {a[2]:.1f}% ")

b = [define_error(exact_value=0.34678, calculated_value=0.3458, type_error=i) for i in range(1, 4)]
print(f"Letra B - Erro absoluto: {b[0]:.5f}, Erro relativo: {b[1]:.7f} e Erro relativo percentual: {b[2]:.5f}% ")

c = [define_error(exact_value=0.000005, calculated_value=0.00000495, type_error=i) for i in range(1, 4)]
print(f"Letra C - Erro absoluto: {c[0]:.8f}, Erro relativo: {c[1]:.2f} e Erro relativo percentual: {c[2]:.1f}% ")

d = [define_error(exact_value=15000.85, calculated_value=14999.0, type_error=i) for i in range(1, 4)]
print(f"Letra D - Erro absoluto: {d[0]:.3f}, Erro relativo: {d[1]:.7f} e Erro relativo percentual: {d[2]:.5f}% ")