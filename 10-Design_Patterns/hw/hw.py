DUR_FROM_FACTORY_TO_PORT = 1
DUR_FROM_FACTORY_TO_STORAGE_B = 5
DUR_FROM_PORT_TO_STORAGE_A = 4

class Factory:
     products = {'A': 0, 'B': 0}
     curr_products = {'A': 0, 'B': 0} #current count of product A
#     b = products['B'] #current count of product B

     @classmethod
     def create_product(cls, line_products):
         cls.products = {'A': 0, 'B': 0}
         cls.curr_products = {'A': 0, 'B': 0}

         for litera in line_products:
             if litera in cls.products:
                 cls.products[litera] += 1
                 cls.curr_products[litera] += 1
             else:
                 cls.products[litera] = 1
                 cls.curr_products[litera] = 1

class Port:
    curr_products = {'A': 0}  #current count of product A

storage = {'A': 0, 'B': 0}

class Transport:
    def __init__(self):
        self.duration = 0

    def step_timer(self):
        if self.duration > 0:
            self.duration -= 1

class Truck(Transport):
    def move_from_factory_to_port(self, product):
        if (Factory.curr_products[product] > 0) and (self.duration == 0):
            Factory.curr_products[product] -= 1
            self.duration = DUR_FROM_FACTORY_TO_PORT * 2

        if (self.duration == DUR_FROM_FACTORY_TO_PORT):
            Port.curr_products[product] += 1

    def move_from_factory_to_storage(self, product):
        if (Factory.curr_products[product] > 0) and (self.duration == 0):
            Factory.curr_products[product] -= 1
            self.duration = 2 * DUR_FROM_FACTORY_TO_STORAGE_B

        if self.duration == DUR_FROM_FACTORY_TO_STORAGE_B:
            storage[product] += 1

class Ship(Transport):
    def move_from_port_to_storage(self, product):
        if (Port.curr_products[product] > 0) and (self.duration == 0):
            Port.curr_products[product] -= 1
            self.duration = 2 * DUR_FROM_PORT_TO_STORAGE_A

        if self.duration == DUR_FROM_PORT_TO_STORAGE_A:
            storage[product] += 1

def main():
    line_products = input("Input list of contaners (for example 'AAB'): ")
    line_products = line_products.upper()
    Factory.create_product(line_products)
    truck1 = Truck()
    truck2 = Truck()
    ship1 = Ship()
    timer = 0

    print("Count of product A: ",Factory.curr_products['A'])
    print("Count of product B: ",Factory.curr_products['B'])

    while (storage['A'] < Factory.products['A']) or (storage['B'] < Factory.products['B']):
        truck1.step_timer()
        truck2.step_timer()
        ship1.step_timer()
        truck1.move_from_factory_to_port('A')
        truck1.move_from_factory_to_storage('B')
        truck2.move_from_factory_to_storage('B')
        truck2.move_from_factory_to_port('A')
        ship1.move_from_port_to_storage('A')
        timer += 1

    print("delivery time: ", timer - 1)


main()

