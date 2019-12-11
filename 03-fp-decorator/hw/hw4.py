def applydecorator(fn):
    def wrapper(*args, **kwargs):
        func = args[0]
        def wrapper2(*args, **kwargs):
            args_new = []
            args_new.append(func)
            for arg in args:
                args_new.append(arg)
            args_new = tuple(args_new)
            result = fn(*args_new, **kwargs)
            return result
        return wrapper2
    return wrapper


@applydecorator
def saymyname(f, *args, **kwargs):
  print('Name is', f.__name__)
  return f(*args, **kwargs)

# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever

print(*(foo(40, 2)))
#>>>foo
#>>>40 2
#То есть избавляет нас от необходимости писать wrapper самим каждый раз.

