
class Factory:
     products = {'A': 0, 'B': 0}
     a = products['A'] #current count of product A
     b = products['B'] #current count of product B

     @classmethod
     def create_product(cls, line_products):
         cls.products = {'A': 0, 'B': 0}
         for litera in line_products:
             if litera in cls.products:
                 cls.products[litera] += 1
             else:
                 cls.products[litera] = 0
         cls.a = cls.products['A']
         cls.b = cls.products['B']

class Port:
    a = 0  #current count of product A

class StorageA:
    a = 0  #current count of product A

class StorageB:
    b = 0  #current count of product B

class Transport:
    def __init__(self):
        self.duration = 0

    def step_timer(self):
        if self.duration > 0:
            self.duration -= 1


class Truck(Transport):
    def moveA_from_factory_to_port(self):
        if (Factory.a > 0) and (self.duration == 0):
            Factory.a -= 1
            self.duration = 2 * 1

        if (self.duration == 1):
            Port.a += 1

    def moveB_from_factory_to_storageB(self):
        if (Factory.b > 0) and (self.duration == 0):
            Factory.b -= 1
            self.duration = 2 * 5

        if self.duration == 5:
            StorageB.b += 1

class Ship(Transport):
    def moveA_from_port_to_storageA(self):
        if (Port.a > 0) and (self.duration == 0):
            Port.a -= 1
            self.duration = 2 * 4

        if self.duration == 4:
            StorageA.a += 1

def main():
    line_products = input("Input list of contaners (for example 'AAB'): ")
    line_products = line_products.upper()
    Factory.create_product(line_products)
    truck1 = Truck()
    truck2 = Truck()
    ship1 = Ship()
    timer = 0

    print("Count of product A: ",Factory.a)
    print("Count of product B: ",Factory.b)

    while (StorageA.a < Factory.products['A']) or (StorageB.b < Factory.products['B']):
        truck1.step_timer()
        truck2.step_timer()
        ship1.step_timer()
        truck1.moveA_from_factory_to_port()
        truck1.moveB_from_factory_to_storageB()
        truck2.moveB_from_factory_to_storageB()
        truck2.moveA_from_factory_to_port()
        ship1.moveA_from_port_to_storageA()
        timer += 1

    print("delivery time: ", timer - 1)


main()

