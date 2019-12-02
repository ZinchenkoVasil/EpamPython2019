import inspect
from Task1 import letters_range
from Task2 import atom
from Task3 import make_it_count
from Task3 import inc


def modified_func(func, *fixated_args, **fixated_kwargs):
    """
    A func implementation of <sorted>
    with pre-applied arguments being: list [1,2,3];
    >
    source_code:
    new_func = modified_func(sorted,[1,2,3])
    lst_result = new_func(reverse=True)

    A func implementation of <letters_range> (Task1)
    with pre-applied arguments being: start, stop;
    >
    source_code:
    new_func = modified_func(letters_range,'g', 'p')
    lst_result = new_func(3)

    A func implementation of <min>
    with pre-applied arguments being: numbers;
    >
    source_code:
    new_func = modified_func(min,4,-5,6)
    a = new_func(1,2,key=abs)

    A func implementation of <max>
    with pre-applied arguments being: numbers;
    >
    source_code:
    new_func = modified_func(max,4,-5,-6)
    a = new_func(-7,2,key=abs)

    A func implementation of <any>
    with pre-applied arguments being: booleans (True or False);
    >
    source_code:
    new_func = modified_func(any)
    a = new_func([True,False])
    print(a)

    A func implementation of <atom> (Task 2)
    with pre-applied arguments being: not;
    >
    source_code:
    new_func = modified_func(atom)
    func = new_func("t-34")
    print(func["get_value"]())

    A func implementation of <make_it_count>
    with pre-applied arguments being: function 'inc';
    >
    source_code:
    counter_inc = [0]
    new_func = modified_func(make_it_count,inc)
    new_inc = new_func(counter_inc)

    """

    modified_func.__name__ = 'func_' + func.__name__
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
lst_result = new_func(reverse=True)
print(lst_result)

new_func = modified_func(letters_range,'g', 'p')
lst_result = new_func(3)
print(list(lst_result))

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

print(modified_func.__name__)














