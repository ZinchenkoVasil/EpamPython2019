"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго, проверку делаю автотестами и просмотром кода.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
import time
from collections import defaultdict

class DeadlineError(Exception):
    pass

class HomeworkResult:
    def __init__(self, homework,solution,author): # good_student, "fff", "Solution"):
        if not isinstance(homework, Homework):
            raise ValueError('You gave a not Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        if self.created + self.deadline < datetime.datetime.now():
            return False
        else:
            return True

class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

class Student(Person):
    def do_homework(self,homework,solution):
        if homework.is_active():
            homework_result = HomeworkResult(homework,solution,self)
            return homework_result
        else:
            raise DeadlineError('You are late') #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Teacher(Person):
    homework_done = {}
    @staticmethod
    def create_homework(text, deadline):
        homework = Homework(text, deadline)
        return homework

    @classmethod
    def remove_dubl(cls,lst):
        return list(set(lst))

    @classmethod
    def check_homework(cls,homework_result):
        if len(homework_result.solution) > 5:
            homework = homework_result.homework
            #нужно добавить результаты ДЗ студента
            if homework in cls.homework_done:
                cls.homework_done[homework].append(homework_result)
                lst = cls.homework_done[homework]
                cls.homework_done[homework] = cls.remove_dubl(lst)
            else:
                cls.homework_done[homework] = []
                cls.homework_done[homework].append(homework_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework:
            cls.homework_done[homework] = None
        else:
            cls.homework_done = {}
        return


if __name__ == '__main__':
    oop_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = oop_teacher.create_homework('Learn OOP', 1)
    docs_hw = oop_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    oop_teacher.check_homework(result_1)
    temp_1 = oop_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    oop_teacher.check_homework(result_2)
    oop_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
#    Teacher.reset_results()

    for homework in Teacher.homework_done:
        print('homework',homework.text)
        for homework_result in Teacher.homework_done[homework]:
            print("homework_result",homework_result.solution)

    Teacher.reset_results(result_1)

    Teacher.reset_results()

    student = Student('Roman', 'Petrov')
    expired_homework = oop_teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = oop_teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    print(student.do_homework(oop_homework,'123456'))
    time.sleep(1)
    print(student.do_homework(expired_homework,'123456'))  # You are late

