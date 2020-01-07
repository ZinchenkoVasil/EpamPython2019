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
cProfile.run("main()"

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

#Результаты утилиты strace
#strace -c python3 Task2_Code_profile2.py

#% time     seconds  usecs/call     calls    errors syscall
#------ ----------- ----------- --------- --------- ----------------
# 87.42    9.607383        4689      2049           read
#  7.95    0.873192        2781       314           getdents
#  3.34    0.366716         146      2508        59 stat
#  1.18    0.130099         109      1198         2 openat
#  0.03    0.003785           3      1199           close
#  0.02    0.002724           1      2227           fstat
#  0.02    0.002145           1      2009         6 lseek
#  0.01    0.001336          20        68           munmap
#  0.01    0.001232           1       987       976 ioctl
#  0.00    0.000482           5       103           mmap
#  0.00    0.000209           6        33           write
#  0.00    0.000144           8        18           mprotect
#  0.00    0.000107           5        21           brk
#  0.00    0.000045           5         9         9 access
#  0.00    0.000033           4         9           lstat
#  0.00    0.000013           3         4         2 readlink
#  0.00    0.000005           2         3           dup
#  0.00    0.000004           0        68           rt_sigaction
#  0.00    0.000004           4         1           execve
#  0.00    0.000004           1         3           fcntl
#  0.00    0.000004           4         1           sysinfo
#  0.00    0.000003           3         1           getrandom
#  0.00    0.000002           2         1           getcwd
#  0.00    0.000002           2         1           arch_prctl
#  0.00    0.000001           1         1           rt_sigprocmask
#  0.00    0.000001           1         1           getuid
#  0.00    0.000001           1         1           geteuid
#  0.00    0.000001           1         1           getegid
#  0.00    0.000001           0         3           sigaltstack
#  0.00    0.000001           1         2           futex
#  0.00    0.000001           1         1           set_tid_address
#  0.00    0.000001           1         1           set_robust_list
#  0.00    0.000001           1         1           prlimit64
#  0.00    0.000000           0         1           getpid
#  0.00    0.000000           0         1           getgid
#------ ----------- ----------- --------- --------- ----------------
#100.00   10.989682                 12849      1054 total

