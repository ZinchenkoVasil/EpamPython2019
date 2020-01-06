#в этой задаче еще до профилирования можно сказать, что самый "горячий" участок кода (узкое место) будет работа с жестким диском, чтение файла с диска.
#работа с диском на порядок медленее, чем работа процессора и ОП.
import cProfile
import timeit
import os

FILE = r'girl.jpg'

def read_file(full_file_name):
    # чтение файла в body
    fin = open(full_file_name, 'rb')
    file_body = fin.read()
    fin.close()
    return file_body

def _search(dir_name, searched_hash):
    for file_name in os.listdir(dir_name):
        full_file_name = os.path.join(dir_name, file_name)
        if os.path.isfile(full_file_name):
            #чтение файла в body
            file_body = read_file(full_file_name)
            if hash(file_body) == searched_hash:
                print("совпадение по хэшу найдено: ", full_file_name)
        if os.path.isdir(full_file_name):
            _search(full_file_name, searched_hash)

def main():
    dir_name = r"." #input("directory name: ")
    fin = open(FILE, 'rb')
    file_body = fin.read()
    fin.close()
    print("hash: ",hash(file_body))
    searched_hash = hash(file_body)
    _search(dir_name, searched_hash)

#main()
cProfile.run("main()")

#Результаты профилирования в Windows 8:
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 Task2_Code_profile.py:16(_search)
#        1    0.000    0.000    0.003    0.003 Task2_Code_profile.py:27(main)
#        2    0.000    0.000    0.001    0.000 Task2_Code_profile.py:9(read_file)

#        4    0.001    0.000    0.001    0.000 {built-in method builtins.hash}
#        7    0.001    0.000    0.001    0.000 {method 'read' of '_io.BufferedReader' objects}

#Результаты профилирования в эмуляторе Linux:
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.090    0.090 <string>:1(<module>)
#    145/1    0.006    0.000    0.090    0.090 Task2_Code_profile2.py:16(_search)
#        1    0.000    0.000    0.090    0.090 Task2_Code_profile2.py:27(main)
#      972    0.002    0.000    0.039    0.000 Task2_Code_profile2.py:9(read_file)

#      974    0.028    0.000    0.028    0.000 {built-in method builtins.hash}
#      973    0.029    0.000    0.029    0.000 {method 'read' of '_io.BufferedReader' objects}

#Выводы:
#в этой задаче в результате профилирования можно сказать, что самые "горячие" участки кода (узкие места):
# вычисление hash-функции файла и чтение файла из файловой с-мы.


