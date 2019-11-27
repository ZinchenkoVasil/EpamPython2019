#Напишите реализацию функции atom, которая инкапсулирует некую переменную,
#предоставляя интерфейс для получения и изменения ее значения,
#таким образом, что это значение нельзя было бы получить или изменить
#иными способами.
#Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
#(значение по умолчанию, в случае вызова atom без аргумента - None),
#а возвращает 3 функции - get_value, set_value, process_value, delete_value,такие, что:

#get_value - позволяет получить значение хранимой переменной;
#set_value - позволяет установить новое значение хранимой переменной,
#	возвращает его;
#process_value - принимает в качестве аргументов сколько угодно функций
#	и последовательно (в порядке перечисления аргументов) применяет эти функции
	#к хранимой переменной, обновляя ее значение (перезаписывая получившийся
	#результат) и возвращая получишееся итоговое значение.
#delete_value - удаляет значение

def atom(*args):
    attribute = None
    if len(args) == 1:
        attribute = args[0]
    elif len(args) > 1:
        raise ValueError("The count of arguments must be 0 or 1.")
    def get_value():
        return attribute
    def set_value(attr):
        nonlocal attribute
        attribute = attr
        return attribute
    def process_value(*args):
        return_result = attribute
        for arg in args:
            return_result = arg(return_result)
        return return_result
    def delete_value():
        nonlocal attribute
        attribute = None
    functions = {}
    functions["get_value"] = get_value
    functions["set_value"] = set_value
    functions["process_value"] = process_value
    functions["delete_value"] = delete_value
    return functions

if __name__ == "__main__":
    func = atom("t-26")
    print(func["get_value"]())
    print(func["set_value"]("t-34"))
    print(func["get_value"]())
    func["delete_value"]()
    print(func["get_value"]())

    func["set_value"]("t-34")
    func = atom()
    print(func["get_value"]())





