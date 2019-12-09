"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
import functools

def instances_counter(cls):
    """Some code"""
    cls.count = 0
    @functools.wraps(cls)
    def inner(*args, **kwargs):
        cls.count += 1
        instance = cls(*args, **kwargs)
        return instance
    return inner

def instances_counter2(cls):
    class Counter(cls):
        @classmethod
        def get_created_instances(cls):
            return cls.count
        @classmethod
        def reset_instances_counter(cls):
            buf = cls.count
            cls.count = 0
            return buf
    return Counter


@instances_counter
class User:
    pass


if __name__ == '__main__':

#    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.count)
#    print(user.get_created_instances())  # 3
#    print(user.reset_instances_counter())  # 3
