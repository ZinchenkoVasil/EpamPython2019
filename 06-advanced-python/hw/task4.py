"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""
import os

class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        if os.path.exists(self.name):
            final_str = self.name + '\n'
            return self._tree(self.name, -1, final_str)
        else:
            print('File not found!')

    def _tree(self, dir_name, level, final_str):
        level += 1
        for file_name in os.listdir(dir_name):
            final_str += level * ' ' + '|->' + file_name + '\n'
            full_file_name = os.path.join(dir_name, file_name)

            if os.path.isdir(full_file_name):
                final_str += self._tree(full_file_name, level, final_str)
        return final_str

    def __contains__(self, item):
        return self._search(self.name, item.name)

    def _search(self, dir_name, searched_name):
        full_file_name = os.path.join(dir_name, searched_name)
        if os.path.exists(full_file_name):
            return True
        else:
            for file_name in os.listdir(dir_name):
                full_file_name = os.path.join(dir_name, file_name)
                if os.path.isdir(full_file_name):
                    if self._search(full_file_name, searched_name):
                        return True
        return False



class PrintableFile:
    def __init__(self, name):
        self.name = name


printableFolder = PrintableFolder(r'D:\EpamPython2019\06-advanced-python','111')
print(printableFolder)

printableFile = PrintableFile('task2.py')
print(printableFile in printableFolder)



