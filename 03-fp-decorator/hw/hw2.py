### Задача

#Написать функцию определения числа Армстронга


### Пример сигнатуры и вызовов функции

def is_armstrong(number):
    str_number = str(number)
    len_number = len(str_number)
    sum_ = sum(list(map(lambda x: int(x)**len_number, str_number))) # [8.5, 9.5, 8.7])
    return (number == sum_)

print(is_armstrong(153))
print(is_armstrong(10))

assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'