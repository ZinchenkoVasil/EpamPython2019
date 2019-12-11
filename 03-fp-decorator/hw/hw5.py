import datetime
import cProfile
import timeit
from functools import reduce


def calc_timeit(fn):
    def wrapper(*args, **kwargs):
        print('time of execution: ',timeit.timeit(fn, number=3))
        result = fn(*args, **kwargs)
        return result
    return wrapper


def cash(fn):
    def wrapper(*args, **kwargs):
        spam1 = args
        spam2 = ""
        if spam1 in wrapper.cash:
            result = wrapper.cash[spam1]
        else:
            result = fn(*args, **kwargs)
        wrapper.cash[spam1] = result
        return result
    wrapper.cash = {}
    return wrapper

def fibonachi(n):
    if n <= 1:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)

@cash
def cash_fibonachi(n):
    if n <= 1:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


@calc_timeit
def fib_with_recursion(n=10):
    return fibonachi(n)

@calc_timeit
def fib_with_cash_recursion(n=10):
    return cash_fibonachi(n)


@calc_timeit
def fib1(n=10):
    return [(lambda: (l[-1], l.append(l[-1] + l[-2]))[0])() for l in [[1, 1]] for x in range(n)]

@calc_timeit
def fib2(n=10):
    return [(l[-1], l.append(l[-1] + l[-2]))[0] for l in [[1, 1]] for x in range(n)]

@calc_timeit
def fib3(n=10):
    return [l.append(l[-1] + l[-2]) or l for l in [[1, 1]] for x in range(n-1)][0][1:]

@calc_timeit
def fib4(n=10):
    return reduce(lambda a, b: a + [a[-1] + a[-2]], range(n-1), [1, 1])[1:]

@calc_timeit
def fib5(n=10):
    return reduce(lambda a, b: a.append(a[-1] + a[-2]) or a, range(n-1), [1, 1])[1:]

print('fib with recursion')
print('fibonachi number 10: ',fib_with_recursion())
print('-------------------------------------------')

print('fib with recursion but cash calls')
print('fibonachi number 10: ',fib_with_cash_recursion())
print('-------------------------------------------')

print('fib1')
lst = fib1()
print('fibonachi number 10: ',lst[-1])
print('-------------------------------------------')

print('fib2')
lst = fib2()
print('fibonachi number 10: ',lst[-1])
print('-------------------------------------------')

print('fib3')
lst = fib3()
print('fibonachi number 10: ',lst[-1])
print('-------------------------------------------')

print('fib4 (reduce)')
lst = fib4()
print('fibonachi number 10: ',lst[-1])
print('-------------------------------------------')

print('fib5 (reduce)')
lst = fib5()
print('fibonachi number 10: ',lst[-1])
print('-------------------------------------------')

#Вывод: порядок везде одинаковый. Лучше всего работают fib3 и fib5. Рекурсия в 8 раз медленнее.
