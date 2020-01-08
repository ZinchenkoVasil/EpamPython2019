from queue import Queue

DUR_FROM_FACTORY_TO_PORT = 1
DUR_FROM_FACTORY_TO_STORAGE_B = 5
DUR_FROM_PORT_TO_STORAGE_A = 4

class Hub:
    def __init__(self):
        self.products_queue = Queue()  # Очередь продуктов

    def get_product_from_queue(self):
        if not self.products_queue.empty():
            return self.products_queue.get()
        return None

    def put_product_to_queue(self, product):
        self.products_queue.put(product)

class Factory(Hub):
    def __init__(self, line_products):
        self.products_queue = Queue()  # Очередь продуктов
        self.products = {'A': 0, 'B': 0}
        for litera in line_products:
            self.put_product_to_queue(litera)
            if  litera in self.products:
                self.products[litera] += 1
            else:
                self.products[litera] = 1

class Port(Hub):
    pass

class Storage:
    def __init__(self):
        self.products = {'A': 0, 'B': 0}

class Transport:
    def __init__(self):
        self.duration = 0
        self.curr_product = ''

    def _step_timer(self):
        if self.duration > 0:
            self.duration -= 1

class Truck(Transport):
    def move_product(self, factory, port, storage, lst_product_names):
        self._step_timer()
        if self.duration == 0:
            self.curr_product = factory.get_product_from_queue()
            if (len(lst_product_names) > 0) and (self.curr_product == lst_product_names[0]):
                self._from_factory_to_port()
            elif (len(lst_product_names) > 1) and (self.curr_product == lst_product_names[1]):
                self._from_factory_to_storage()

        if (self.duration == DUR_FROM_FACTORY_TO_PORT) and (len(lst_product_names) > 0) and (self.curr_product == lst_product_names[0]):
            port.put_product_to_queue(self.curr_product)

        if (self.duration == DUR_FROM_FACTORY_TO_STORAGE_B) and (len(lst_product_names) > 1) and (self.curr_product == lst_product_names[1]):
            storage.products[self.curr_product] += 1

    def _from_factory_to_port(self):
        self.duration = DUR_FROM_FACTORY_TO_PORT * 2

    def _from_factory_to_storage(self):
        self.duration = DUR_FROM_FACTORY_TO_STORAGE_B * 2

class Ship(Transport):
    def move_from_port_to_storage(self, port, storage, lst_product_names):
        self._step_timer()
        if self.duration == 0:
            self.curr_product = port.get_product_from_queue()
            if self.curr_product == lst_product_names[0]:
                self.duration = 2 * DUR_FROM_PORT_TO_STORAGE_A

        if (self.duration == DUR_FROM_PORT_TO_STORAGE_A) and (len(lst_product_names) > 0) and (self.curr_product == lst_product_names[0]):
            storage.products[self.curr_product] += 1

def main():
    line_products = input("Input list of contaners (for example 'AAB'): ")
    line_products = line_products.upper()
    factory1 = Factory(line_products)
    port1 = Port()
    truck1 = Truck()
    truck2 = Truck()
    ship1 = Ship()
    storageA = Storage()
    storageB = Storage()

    print("Count of product A: ",factory1.products['A'])
    print("Count of product B: ",factory1.products['B'])
    timer = 0
    while (storageA.products['A'] < factory1.products['A']) or (storageB.products['B'] < factory1.products['B']):
#        print(storageA.products['A'])
#        print(storageB.products['B'])
        truck1.move_product(factory1, port1, storageB, ['A','B'])
        truck2.move_product(factory1, port1, storageB, ['A','B'])
        ship1.move_from_port_to_storage(port1, storageA, ['A'])
        timer += 1

    print("delivery time: ", timer - 1)


main()

