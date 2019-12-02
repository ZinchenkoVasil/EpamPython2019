# Гипотеза Коллатца

#- берём любое натуральное число n, если оно чётное, то делим его на 2
#- если нечётное, то умножаем на 3 и прибавляем 1 (получаем 3n + 1)
#- над полученным числом выполняем те же самые действия, и так далее

### Задача

#Вычислить число шагов для числа n, согласно гипотезе Коллатца необходимых для достижения этим числом единицы, используя функциональный стиль. По возможности не забыть проверить пограничные условия и входные данные.
from functools import reduce

def collatz_steps(n):
    lst = [0]
    def func(value, element):
        nonlocal lst
        if value != 1:
            lst.append(value)
        if value % 2 == 0:
            return value / 2
        else:
            return 3 * value + 1
    reduce(func, lst, n)
    return len(lst[1:])

print(collatz_steps(16))
print(collatz_steps(12))
print(collatz_steps(1000000))


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

