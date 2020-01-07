"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
import collections.abc

class GraphIterator(collections.abc.Iterator):
    def __init__(self, dict_, key, cursor, item):
        self._dict = dict_
        self._cur_key = key
        self._cursor = cursor
        self._item = item
        self.lst = []


    def __next__(self):
        if self._cursor + 1 >= len(self._dict[self._cur_key]):
            while True:
                self._cur_key = next(self._item)
                if len(self._dict[self._cur_key]) > 0:
                    break
            self._cursor = -1

        self._cursor += 1
        #вставить проверку на отсутствие повторений
        next_ = self._dict[self._cur_key][self._cursor]
        if next_ in self.lst:
            return self.__next__()
        else:
            self.lst.append(next_)
            print(f'{self._cursor} дочерний узел от узла {self._cur_key}:')
            return next_

class Graph:
    def __init__(self, E):
        self.E = E
        key = iter(dict(E))
    def __iter__(self):
        item = iter(dict(E))
        first_key = next(item)
        return GraphIterator(self.E,first_key,-1,item)

E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertice in graph:
    print(vertice)
