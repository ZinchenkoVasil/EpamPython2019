#json
#mongoDB
#postgress
#mysql
import pprint
import os
import json
from pymongo import MongoClient
import copy
import psycopg2
#Базовый класс и есть методо Out_to_db()
class Connection:
    def __init__(self, db_name):
        self.db_name = db_name

    def select_db(self, collection_name):
        raise Exception('This method without realisation!')

    def out_to_db(self, out_list, collection_name):
        raise Exception('This method without realisation!')

class Connection_json(Connection):
    def out_to_db(self, out_list, collection_name):
        try:
            print(self.db_name)
            with open(self.db_name, 'w', encoding='utf-8') as f:
                json.dump(out_list, f, ensure_ascii=False)
                print(f"файл {self.db_name} создался успешно!")
                return True
        except:
             print("Ошибка при записи выходного файла JSON")
             return False

    def select_db(self, collection_name):
        if os.path.exists(self.db_name):
            # Читаем JSON из файла и преобразуем к типу Python
            with open(self.db_name, 'r', encoding='UTF-8') as f:
                read_data = json.load(f)
                pprint.pprint(read_data)
        else:
            print(f"{self.db_name} File not found!")
            return None

class Connection_mongoDB(Connection):
    def __init__(self, db_name, conn_string):
        super().__init__(db_name)
        client = MongoClient(conn_string)#'mongodb://127.0.0.1:27017')
        self.db = client[self.db_name]

    def out_to_db(self, out_list, collection_name):
        db_table = self.db[collection_name]
        db_table.insert_many(out_list)

    def select_db(self, collection_name):
        db_table = self.db[collection_name]
        cur = db_table.find()
        for obj in cur:
            print(obj)

class Connection_postgreSQL(Connection):
    def __init__(self, db_name, user, password, host, port):
        super().__init__(db_name)
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.conn = psycopg2.connect(
            database = self.db_name,
            user = self.user,#"postgres",
            password = self.password, # "111111",
            host = self.host, # "127.0.0.1",
            port = self.port #"5432"
        )

    def create_table(self, table_name, out_dict): #conn
# Схема определяет таблицы в базе данных
        try:
            with self.conn:
                sql_command = f"create table {table_name}("
                for key in out_dict:
                    new_field = key + " VARCHAR(255),"
                    sql_command += new_field
                sql_command = sql_command[:-1] + ")"
                cur = self.conn.cursor()
                cur.execute(sql_command)
                self.conn.commit()
                return True
        except:
            return False

    def out_to_db(self, out_list, collection_name):
        # Insert
        with self.conn:
            for out_dict in out_list:
                str1 = ''
                str2 = ''
                for key,value in out_dict.items():
                    str1 = str1 + str(key) + ','
                    str2 = str2 + "'"+ str(value) + "'" + ','
                str1 = str1[:-1]
                str2 = str2[:-1]
                sql_command =  f"insert into {collection_name}({str1}) VALUES({str2})"
                print(sql_command)
                cur = self.conn.cursor()
                cur.execute(sql_command)
                self.conn.commit()

    def select_db(self, collection_name):
        with self.conn:
    # Select
            cur = self.conn.cursor()
            cur.execute(f"select * from {collection_name}")
            list_ = []
            for row in cur.fetchall():
                print(row)


out_lst = [{'first_name':'Vasil','last_name':'Zinchenko','position':'junior'}, {'first_name':'Rasul','last_name':'Osmanov','position':'CEO'}]
out_lst_copy1 = copy.deepcopy(out_lst)
out_lst_copy2 = copy.deepcopy(out_lst)

print("JSON")
conn = Connection_json('employees.json')
conn.out_to_db(out_lst,'')
conn.select_db('employees')

print("MongoDB")
conn = Connection_mongoDB('headhunter','mongodb://127.0.0.1:27017')
conn.out_to_db(out_lst_copy1,'employees')
conn.select_db('employees')

print("postgreSQL")
conn = Connection_postgreSQL('postgres', 'postgres', '111111', "127.0.0.1", "5432")
conn.create_table('employees', out_lst_copy2[0])
conn.out_to_db(out_lst_copy2, 'employees')
conn.select_db('employees')
