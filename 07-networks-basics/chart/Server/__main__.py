# Программа сервера для получения приветствия от клиента и отправки ответа
import json
import sys
import argparse
from Server import routes
from Log.server_log_config import *
import select
from socket import socket, AF_INET, SOCK_STREAM
from queue import Queue
from threading import Thread

user_dict = {}  # словарик где в качестве ключей nickname и в качестве значений конекты-сокеты (con)

def parsing(data):
    print("вошли в parsing")
    logger.debug("сервер принял сообщение от клиента")
    request = json.loads(data)
    print("сервер принял сообщение от клиента")
    print("парсинг сообщения от клиента")
    client_action = request.get('action')
    resolved_routes = list(
        filter(
            lambda itm: itm.get('action') == client_action, routes))
    route = resolved_routes[0] if resolved_routes else None
    response_dict = {}
    if route:
        controller = route.get('controller')
        if "user" in request:
            user = request.get('user')
            account_name = user['account_name']
        else:
            account_name = ''
        if "message" in request:
            message = request.get('message')
        else:
            message = ''
        print("парсинг поля to")
        if "to" in request:
            to = request.get('to')
        else:
            to = None
        response_string = controller(account_name, message)
        response_dict['response'] = 200
        response_dict['alert'] = response_string
        response_dict['from'] = account_name
        print("парсинг поля to")
        response_dict['to'] = to
    else:
        response_dict['response'] = 401
        response_dict['alert'] = "Action don't support"
        logger.error("Action don't support")
        logger.error("клиент работает по неизвестному протоколу!")
    return response_dict

def read_request(responses,sock,all_clients):
    try:
        print("вошли в read_request")
        data = sock.recv(1024).decode('utf-8')
        response = parsing(data)
        print("парсинг сообщения от клиента и формирование ответа")
        print(response["from"])
        user_dict[response["from"]] = sock #формируем словарь соответствий прозвища и коннекта (сокета)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        responses.put(response)
        print("сообщение от клиента получено")
    except:
        print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
        sock.close()
        all_clients.remove(sock)


def read_requests(r_clients, all_clients):
#    print("вошли в read_requests")
    response_queue = Queue()  # Очередь ответов сервера вида
    for sock in r_clients:
        read_request(response_queue,sock,all_clients)
    return response_queue #надо в цикле заполнить очередь


def write_response(response,sock,all_clients):
    try:
        # Подготовить и отправить ответ сервера
        print("Подготовить и отправить ответ сервера")
        print("Пакет на выход - ",response)
        resp = json.dumps(response).encode('utf-8')
        # Эхо-ответ
        sock.send(resp)
        print(f"Эхо-ответ {resp} выслали всем слушающим клиентам")
    except:  # Сокет недоступен, клиент отключился
        print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
        sock.close()
        all_clients.remove(sock)


def write_responses(response, w_clients, all_clients):
    print("write_responses")
    if response['to']:
        if response['to'] in user_dict:
            sock = user_dict[response['to']] #определяем куда пересылать
            if sock in w_clients:
                t = Thread(target=write_response, args=(response, sock, all_clients))
                t.start()
            else:
                print('невозможно доставить сообщение пользователю, который вышел из чата!')
        else:
            print('невозможно доставить сообщение, пользователь с таким ником не заходил с момента последнего запуска сервера!')
        return
    else:
        for sock in w_clients:
            t = Thread(target=write_response, args=(response, sock, all_clients))
            t.start()

def mainloop():
   """ Основной цикл обработки запросов клиентов
   """
   clients = []
#   user_dict = {} #словарик где в качестве ключей nickname и в качестве значений конекты-сокеты (con)

   s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
   print("Создает сокет TCP")
   s.bind((args.addr, args.port))  # Присваивает порт
   print("Присваивает порт")
   s.listen(5)  # Переходит в режим ожидания запросов;
   print("Переходит в режим ожидания запросов")
   s.settimeout(0.2)  # Таймаут для операций с сокетом
   while True:
       try:
           conn, addr = s.accept()  # Проверка подключений
       except OSError as e:
           pass  # timeout вышел
       else:
           print("Получен запрос на соединение от %s" % str(addr))
           clients.append(conn)
       finally:
           # Проверить наличие событий ввода-вывода
           wait = 10
           r = []
           w = []
           try:
               r, w, e = select.select(clients, clients, [], wait)
           except:
               pass  # Ничего не делать, если какой-то клиент отключился
  #         print("вход в read_requests")
           response_queue = read_requests(r, clients)  # Сохраним запросы клиентов
#           print("выход из read_requests")
           if not response_queue.empty():
               print("вход в бесконечный цикл")
               while True:
                   if response_queue.empty():
                       break
                   item = response_queue.get()
                   write_responses(item, w, clients)  # Выполним отправку ответов клиентам
                   response_queue.task_done()
               # Конец. Сообщить, что сигнальная метка была принята, и выйти

# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
logger.info('Запуск сервера-------------------------------------------------------------')

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='localhost')
parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
args = parser.parse_args(sys.argv[1:])
mainloop()
