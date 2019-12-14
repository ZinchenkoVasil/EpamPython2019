#ответ сервера на запрос установления соединения
from Server.decorators import *

user_list = []

@log
def get_response(account_name, data):
    if account_name:
        user_list.append(account_name)
        return f"{account_name} joined to the chart.  User list: {str(user_list)}"
    else:
        return f"Anonymous joined to the chart."

@log
def get_message(account_name, data):
    if account_name:
        return account_name + ": " + data
    else:
        return data

@log
def log_out(account_name, data):
    if account_name:
        user_list.remove(account_name)
        return f"{account_name} left the chart.  User list: {str(user_list)}"
    else:
        return f"Anonymous left the chart."


