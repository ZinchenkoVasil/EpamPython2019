import cProfile
import timeit
import os
import hashlib

FILE = r'girl.jpg'

def read_file(full_file_name):
    # чтение файла в bodyfile_body
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
            hashvalue = hashlib.sha256(file_body)
#            print(hashvalue)
            if hashvalue.hexdigest() == searched_hash.hexdigest():
                print("совпадение по хэшу найдено: ", full_file_name)
        if os.path.isdir(full_file_name):
            _search(full_file_name, searched_hash)

def main():
    dir_name = '.' #input("directory name: ")
    fin = open(FILE, 'rb')
    file_body = fin.read()
    fin.close()
    hashvalue = hashlib.sha256(file_body)
#    print(hashvalue)
    _search(dir_name, hashvalue)

main()
cProfile.run("main()")


