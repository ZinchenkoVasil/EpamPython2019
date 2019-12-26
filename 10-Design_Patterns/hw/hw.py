from queue import Queue

DUR_FROM_FACTORY_TO_PORT = 1
DUR_FROM_FACTORY_TO_STORAGE_B = 5
DUR_FROM_PORT_TO_STORAGE_A = 4

class Factory:
    def __init__(self, line_products):
        self.products_queue = Queue()  # Очередь продуктов фабрики
        self.products = {'A': 0, 'B': 0}
        for litera in line_products:
            self.products_queue.put(litera)
            if  litera in self.products:
                self.products[litera] += 1
            else:
                self.products[litera] = 1

class Port:
    def __init__(self):
        self.products_queue = Queue()  # Очередь в порт


storages = {'A': 0, 'B': 0}

class Transport:
    def __init__(self):
        self.duration = 0
        self.curr_product = ''

    def _step_timer(self):
        if self.duration > 0:
            self.duration -= 1

class Truck(Transport):
    def move_product(self, factory, port):
        self._step_timer()
        if self.duration == 0:
            if not factory.products_queue.empty():
                self.curr_product = factory.products_queue.get()
                if self.curr_product == 'A':
                    self._from_factory_to_port()
                elif self.curr_product == 'B':
                    self._from_factory_to_storage()

        if (self.duration == DUR_FROM_FACTORY_TO_PORT) and (self.curr_product == 'A'):
            port.products_queue.put(self.curr_product)

        if (self.duration == DUR_FROM_FACTORY_TO_STORAGE_B) and (self.curr_product == 'B'):
            storages[self.curr_product] += 1

    def _from_factory_to_port(self):
        self.duration = DUR_FROM_FACTORY_TO_PORT * 2

    def _from_factory_to_storage(self):
        self.duration = DUR_FROM_FACTORY_TO_STORAGE_B * 2

class Ship(Transport):
    def move_from_port_to_storage(self, port):
        self._step_timer()
        if self.duration == 0:
            if not port.products_queue.empty():
                self.curr_product = port.products_queue.get()
                if self.curr_product == 'A':
                    self.duration = 2 * DUR_FROM_PORT_TO_STORAGE_A

        if (self.duration == DUR_FROM_PORT_TO_STORAGE_A) and (self.curr_product == 'A'):
            storages[self.curr_product] += 1

def main():
    line_products = input("Input list of contaners (for example 'AAB'): ")
    line_products = line_products.upper()
    factory1 = Factory(line_products)
    port1 = Port()
    truck1 = Truck()
    truck2 = Truck()
    ship1 = Ship()

    print("Count of product A: ",factory1.products['A'])
    print("Count of product B: ",factory1.products['B'])
    timer = 0
    while (storages['A'] < factory1.products['A']) or (storages['B'] < factory1.products['B']):
        #print(storageA.product)
        #print(storageB.product)
        truck1.move_product(factory1, port1)
        truck2.move_product(factory1, port1)
        ship1.move_from_port_to_storage(port1)
        timer += 1

    print("delivery time: ", timer - 1)


main()

