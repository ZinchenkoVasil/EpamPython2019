#Напишите реализацию функции make_it_count, которая принимает в качестве
#аргументов некую функцию (обозначим ее func) и имя глобальной переменной
#(обозначим её counter_name), возвращая новую функцию, которая ведет себя
#в точности как функция func, за тем исключением, что всякий раз при вызове
#инкрементирует значение глобальной переменной с именем counter_name.

#написать обертку!

def make_it_count(func, counter_name):
    def new_func(*args,**kwargs):
        counter_name[0] += 1
        func(*args,**kwargs)
    return new_func

def inc(i):
    i += 1
    return i

counter_inc = [0]
new_inc = make_it_count(inc, counter_inc)

new_inc(0)
new_inc(1)
new_inc(2)
print("Count of calls:", counter_inc[0])
