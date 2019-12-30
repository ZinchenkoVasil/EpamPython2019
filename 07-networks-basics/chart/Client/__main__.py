# Программа клиента для отправки приветствия серверу и получения ответа
import argparse
from socket import *
import json
import sys
import time
from threading import Thread
#from Log.client_log_config import *

# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
#logger = logging.getLogger('client.main')


message_from_client = {
        "action": "presence",
        "message": "",
        "user": {
                "account_name":  None,
                "avatar": None},
        "to": None
}

def read_thread(sock):
    while True:
        # необходимо сделать поток на чтение!
        try:
            data = sock.recv(1024)
#            logger.debug("Приняли сообщение от сервера")
            response = json.loads(data.decode('utf-8'))
            if int(response["response"]) == 200:
                print('\t\t\t\t'+response["alert"])
        except:
            pass



def write_thread(sock):
    while True:
        # необходимо сделать поток на запись!
        key = input('Public message - key [1], private message - key [2], exit - key [3]: ')
        if key == '3':
            message_from_client['action'] = "logout"
            sock.send(json.dumps(message_from_client).encode())
            break
        if key == '1':
            msg = input('Input your public message for all: ')
        elif key == '2':
            message_from_client['to'] = input('Input the receiver of your message: ')
            msg = input(f'Input your message for {message_from_client["to"]}: ')
        else:
            continue
        message_from_client['action'] = "message"
        message_from_client['message'] = msg
        sock.send(json.dumps(message_from_client).encode())
 #       print("Сообщение только что отправлено!")


def echo_client(addr, port):

    # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
    # При выходе из оператора with сокет будет автоматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock: # Создать сокет TCP
        sock.connect((addr, port))   # Соединиться с сервером
#        logger.debug("Соединиться с сервером")
        user = input('Your nickname: ')
        message_from_client["user"]["account_name"] = user
        message_from_client['action'] = "presence"
        sock.send(json.dumps(message_from_client).encode())
#        logger.debug("Послали сообщение серверу")
        data = sock.recv(1024)
#        logger.debug("Приняли приветствие от сервера")
        response = json.loads(data.decode('utf-8'))
        if int(response["response"]) == 200:
            print(f"Hello, I am the server {addr}")
        print(response["alert"])

        #необходимо сделать 2 потока: на чтение и запись!
        t1 = Thread(target=read_thread, args=(sock, ))
        t1.daemon = True
        t1.start()
        write_thread(sock)
        time.sleep(10)

if __name__ == '__main__':
#    logger.info('Запуск клиента-------------------------------------------------------------')
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='localhost')
    parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
    args = parser.parse_args(sys.argv[1:])

    print("адрес сервера: ", args.addr)
    echo_client(args.addr, args.port)


