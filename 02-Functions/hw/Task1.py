#Некоторые встроенные функции в Python имеют нестандартное поведение, когда
#дело касается аргументов и их значений по умолчанию.
#Например, range, принимает от 1 до 3 аргументов, которые обычно называются
#start, stop и step и при использовании всех трех, должны указываться
#именно в таком порядке. При этом только у аргументов start и step есть значения
#по умолчанию (ноль и единица), а у stop его нет, но ведь аргументы без значения
#по умолчанию, то есть позиционные аргументы, должны указываться до именнованных,
#а stop указывается после start. Более того, при передаче функции только одного
#аргумента он интерпретируется как stop, а не start.
#Подумайте, каким образом, можно было бы добиться такого же поведения для
#какой-нибудь нашей пользовательской функции.
#Напишите функцию letters_range, которая ведет себя похожим на range образом,
#однако в качестве start и stop принимает не числа, а буквы латинского алфавита
#(в качестве step принимает целое число) и возвращает не перечисление чисел, а
#список букв, начиная с указанной в качестве start (либо начиная с 'a',
#если start не указан), до указанной в качестве stop с шагом step (по умолчанию
#равным 1). Добавить возможность принимать словарь с заменами букв для подобия траслитерации.
#Т.е. замена символов из оригинального алфавита другими, возможно несколькими символами.

#Пример:
#>>>letters_range('b', 'w', 2)
#['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']

#>>>letters_range('g')
#['a', 'b', 'c', 'd', 'e', 'f']

#>>>letters_range('g', 'p')
#['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

#>>>letters_range('g', 'p', **{'l': 7, 'o': 0})
#['g', 'h', 'i', 'j', 'k', '7', 'm', 'n', '0']

#>>>letters_range('p', 'g', -2)
#['p', 'n', 'l', 'j', 'h']

#>>>letters_range('a')


def letters_range(*args, **kwargs): #start='a',stop=None,step=1):
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 1:
        start = 'a'
        stop = args[0]
        step = 1
    else:
        raise Exception("The count of arguments must be 1-3.")

    num = ord(start)
    while ((step > 0) and (num < ord(stop))) or ((step < 0) and (num > ord(stop))):
        litera = chr(num)
        if litera in kwargs:
            litera = kwargs[litera]
        yield litera
        num += step





#print(list(letters_range('g')))

#print(list(letters_range('b', 'w', 2)))
#['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']

#>>>letters_range('g')
#['a', 'b', 'c', 'd', 'e', 'f']

print(list(letters_range('g', 'p')))
#['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

print(list(letters_range('g', 'p', **{'l': 7, 'o': 0})))
#['g', 'h', 'i', 'j', 'k', '7', 'm', 'n', '0']

print(list(letters_range('p', 'g', -2)))
#['p', 'n', 'l', 'j', 'h']
