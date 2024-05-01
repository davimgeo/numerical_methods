def base2base16(num, base_num):
    result = result_final = ''
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz+/="
    
    num = num[::-1]
    foo = bar = 0
    if base_num == 2:
        i = 0
        while i < len(num):
            result += num[i]
            if (i+1) % 4 == 0:
                for j in range(len(result)):
                    foo += int(result[j]) * (2 ** j)
                result_final += alphabet[foo]
                result = ''
            foo = 0
            i += 1
        if result != '':
            for k in range(len(result)):
                bar += int(result[k]) * (2 ** k)
            result_final += alphabet[bar]
    else:
       for element in num:
        index = alphabet.index(element)
        while index >= 1:
                result_final += str(index % 2)
                index //= 2
                
        result += str(index)
            
    return result_final[::-1]

number = '2DA'            #O número que deseja converter
number_base = 16         #DIgite 16 para conversar para a base 2 e vice-versa

result_list = base2base16(number, number_base)

print(result_list)