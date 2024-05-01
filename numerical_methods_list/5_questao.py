def base2base8(num, base_num):
    result = result_final = ''
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz+/="
    
    if type(num) != str:
        num = str(num)

    num = num[::-1]
    foo = bar = 0
    if base_num == 2:
    #Converter Base 2 para Base 8
        i = 0
        while i < len(num):
            result += num[i]
            if (i+1) % 3 == 0:
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
        return result_final[::-1]
    else:
    #Converter Base 8 para a base 2 utilizando hashmap
        hashmap = {'0':'000', '1': "001", '2':'010', '3':'011', '4':'100',
                   '5':'101', '6':'110','7':'111'}
        for element in num:
            result_final += hashmap[element]
        return result_final
        
            

number = '252'                 #O número que deseja converter
number_base = 8                #Escolha 8 para converter para base 2 e vice-versa

result_list = base2base8(number, number_base)

print(result_list)