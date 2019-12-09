#--9


SUM = 1000
def func(a,b):
    c = SUM - a - b
    if a*a + b*b == c*c:
        print(f"a={a}, b={b}, c={c}")

print('----Task9-----')
l1 = int(SUM / 2 + 1)
l2 = int(SUM / 3 + 1)
[func(a,b) for a in range(1,l2) for b in range(a+1,l1)]

#--6
#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
N = 100
square = lambda n: n ** 2
dif = sum(list(range(1,N + 1)))**2 - sum(map(square, range(1,N + 1)))
print('----Task6-----')
print(f'The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum: {dif}')

#--48
#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

N = 1000
sum_ = sum(map(lambda n: n ** n, range(1, N + 1)))
result = str(sum_)[-10:]
print('----Task48-----')
print(f'The last ten digits of the series: {result}')
#print(len(result))


#--40
#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

from functools import reduce

def Task_40():
    N = 1000000
    def func(value, element):
        nonlocal N
        if len(value) < N:
            return value + str(element)
        else:
            N = 0
            return value

    string = reduce(func, range(2,N), '1')
    return string

str_numbers = Task_40()
d1 = int(str_numbers[0])
d10 = int(str_numbers[9])
d100 = int(str_numbers[99])
d1000 = int(str_numbers[999])
d10000 = int(str_numbers[9999])
d100000 = int(str_numbers[99999])
d1000000 = int(str_numbers[999999])
result = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
print('----Task40-----')
print(f'd1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 = {result}')


