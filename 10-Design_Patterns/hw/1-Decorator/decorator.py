"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseCoffe(Component):
    def get_cost(self):
        return 90

class Whip:
    def __init__(self, coffe):
        self.coffe = coffe
        self.cost = 10

    def get_cost(self):
        return self.coffe.get_cost() + self.cost

class Marshmallow:
    def __init__(self, coffe):
        self.coffe = coffe
        self.cost = 20

    def get_cost(self):
        return self.coffe.get_cost() + self.cost

class Syrup:
    def __init__(self, coffe):
        self.coffe = coffe
        self.cost = 10

    def get_cost(self):
        return self.coffe.get_cost() + self.cost


if __name__ == "__main__":
    coffe = BaseCoffe()
    coffe = Whip(coffe)
    coffe = Marshmallow(coffe)
    coffe = Syrup(coffe)
    print("Итоговая стоимость за кофе: {}".format(str(coffe.get_cost())))
