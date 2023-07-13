from controller.command import ConsoleCommand
from controller.student_controller import StudentController
from model.db import students_list, students_dict
from model.student_dict import StudentDict
from model.student_list import StudentList
from view.languages import LANG_DICT


def run():
    """
    Функция запуска программы для работы со списком и словарем студентов.

    Процесс работы:
    1. Пользователь выбирает язык.
    2. Создаются модели списка и словаря студентов на основе предварительно
    заданных данных.
    3. Выполняется бесконечный цикл, пока пользователь не выберет команду
    "Выход". В каждой итерации цикла пользователю предлагается ввести команду.
    4. В зависимости от выбранной команды выполняются соответствующие действия:
       - Вывод списка студентов из моделей списка и словаря.
       - Поиск студента по идентификатору в моделях списка и словаря.
       - Удаление студента по идентификатору из моделей списка и словаря.
    5. Если пользователь выбирает команду "Выход", программа завершается.

    """
    # инициализация моделей словаря и списка
    model_list = StudentList(students_list)
    model_dict = StudentDict(students_dict)

    while True:
        language = input(LANG_DICT['rus']['msg'][0])
        if language.lower() in LANG_DICT:
            # инициализируем команды на выбранном языкe
            commands = ConsoleCommand(language=language)
            break
        else:
            print('Invalid language. Please choose available language.')

    # инициализируем контроллеры с соответствующими представлениями
    # (view) на выбранном языке
    control_list = StudentController(model=model_list,
                                     language=language)
    control_dict = StudentController(model=model_dict,
                                     language=language)
    while True:
        # выводим список команд и ждем от пользователя ввод
        print(LANG_DICT[language]['commands'][1:])
        user_input = input(LANG_DICT[language]['msg'][1])

        # команда вывода всех моделей
        if user_input.lower() == commands.ALL_READ.lower():
            control_list.print()
            control_dict.print()

        # команда вывода модели списка
        elif user_input.lower() == commands.LIST_READ.lower():
            control_list.print()

        # команда вывода модели словаря
        elif user_input.lower() == commands.DICT_READ.lower():
            control_dict.print()

        # команда поиска по ID
        elif user_input.lower() == commands.SEARCH.lower():
            search_id = int(input(LANG_DICT[language]['msg'][2]))
            control_list.search_student(search_id)
            control_dict.search_student(search_id)

        # команда удаления по ID
        elif user_input.lower() == commands.DELETE.lower():
            delete_id = int(input(LANG_DICT[language]['msg'][2]))
            control_list.delete_student(delete_id)
            control_dict.delete_student(delete_id)

        # команда выхода
        elif user_input.lower() == commands.EXIT.lower():
            print(LANG_DICT[language]['msg'][6])
            break
        else:
            print(LANG_DICT[language]['msg'][3])


run()
