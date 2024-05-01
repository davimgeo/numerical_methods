def base_natural(num, base_num, base):
    result = []
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz+/="

    if base_num != 10 and base == 10:
        dum = 0
        for i in range(len(str(num))):
            digit = num % 10
            dum += digit * (base_num ** i)
            num //= 10
        result.append(dum)
    else:
        while num >= 1:
            if 11 <= base <= 64:
                result += alphabet[num % base]
            else:
                result.append(num % base)
            num //= base

        result.reverse()

    result = "".join(map(str, result))
    return result

number = 265          #O número que deseja converter
number_base = 10    #A base do seu número
base2convert = 2    #A base que deseja converter seu número

result_list = base_natural(number, number_base, base2convert)

print(result_list)
