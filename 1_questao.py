def binary2decimal(integer_part, decimal_part=None):
    dum = 0

    for i in range(len(str(integer_part))):
        digit = integer_part % 10
        dum += digit * (2 ** i)
        integer_part //= 10

    if decimal_part is not None:
        result_str = str(decimal_part)
        for i in range(1, len(result_str) + 1):
            dum += int(result_str[i - 1]) * (2 ** -i)

    return dum
"""
Insira como argumento a parte inteira e a parte decimal. Ex.: 11.11110101 teria como integer_part = 11
e decimal_part = 11110101
"""
decimal = binary2decimal(integer_part=10110101, decimal_part=1010101)
decimal_2 = binary2decimal(integer_part=11, decimal_part=11110101)
print(f"Seu número na base 10 é: {decimal:.3f}")
print(f"Seu número na base 10 é: {decimal_2:.3f}")

