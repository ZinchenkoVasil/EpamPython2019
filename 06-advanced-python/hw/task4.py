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

full_file_name = ''

class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        if os.path.exists(self.name):
            global final_str
            final_str = self.name + '\n'
            self._tree(self.name)
            return final_str
        else:
            return 'Directory not found!'

    def _tree(self, dir_name, level=-1):
        level += 1
        if len(os.listdir(dir_name)) == 0:
            return
        for file_name in os.listdir(dir_name):
            global final_str
            final_str += level * ' ' + '|->' + file_name + '\n'
            full_file_name = os.path.join(dir_name, file_name)
            if os.path.isdir(full_file_name):
                self._tree(full_file_name, level)

    def __contains__(self, item):
        if not os.path.exists(self.name):
            print('Directory not found!')
            return False
        else:
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


printableFolder = PrintableFolder(r'.','111')
print(printableFolder)

printableFile = PrintableFile('task4.py')
print(printableFile in printableFolder)



