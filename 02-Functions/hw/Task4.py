import inspect
from Task1 import letters_range
from Task2 import atom
from Task3 import make_it_count
from Task3 import inc


def modified_func(func, *fixated_args, **fixated_kwargs):
    """
    A func implementation of <имя функции func>
    with pre-applied arguments being:
    <перечисление имен и значений переданных fixated_args и fixated_kwargs;
    если ключевые аргументы переданны как позиционные - соотнести их с именами
    из function definition
    >
    source_code:
       ...
    """

 #   args, varargs, varkw, defaults)
    def new_func(*args, **kwargs):
        nonlocal fixated_args
        nonlocal fixated_kwargs
#        ArgSpec = inspect.getfullargspec(func)
        if args:
            fixated_args = fixated_args + args
        if kwargs:
            for key, value in kwargs.items():
                fixated_kwargs[key] = value
        # ключевые аргументы переданы как позиционные
        #для случая у функции есть только ключевые аргументы и они все передаются как позиционные
#        elif not ArgSpec.varargs and ArgSpec.varkw and fixated_args:  # ключевые аргументы переданы как позиционные
#            j = 0
#            for fixated_arg in fixated_args:
#                for key in ArgSpec.varkw:
#                    kwargs[key] = fixated_arg
#                j += 1

        if fixated_args and fixated_kwargs:
           return func(*fixated_args,**fixated_kwargs)
        elif fixated_args:
           return func(*fixated_args)
        elif fixated_kwargs:
           return func(**fixated_kwargs)

    return new_func


new_func = modified_func(sorted,[1,2,3])
a = new_func(reverse=True)
print(a)
new_func = modified_func(letters_range,'g', 'p')
a = new_func(3)
print(list(a))
new_func = modified_func(min,4,-5,6)
a = new_func(1,2,key=abs)
print(a)
new_func = modified_func(max,4,-5,-6)
a = new_func(-7,2,key=abs)
print(a)
new_func = modified_func(any)
a = new_func([True,False])
print(a)

#Task2
new_func = modified_func(atom)
func = new_func("t-34")
print(func["get_value"]())

#Task3
counter_inc = [0]
new_func = modified_func(make_it_count,inc)
new_inc = new_func(counter_inc)
new_inc(0)
new_inc(1)
new_inc(2)
print("Count of calls:", counter_inc[0])














