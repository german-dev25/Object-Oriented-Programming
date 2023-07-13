"""
Словарь rus/eng,
хранящий аргументы для декоратора,
список команд и
список сообщений от системы.
"""

LANG_DICT = {
    'rus': {
        'decor_stud_list': {
            'header': 'Список студентов',
            'delimiter': '=',
            'width': 20},
        'commands':
            [' ',
             'Все модели',
             'Список',
             'Словарь',
             'Поиск',
             'Удалить',
             'Выход'],
        'msg': ['Выберите язык (rus/eng): ',
                'Введите команду: ',
                'Введите ID студента: ',
                'Не найден',
                'Команда не найдена',
                'Студент удален',
                'До свидания']
    },
    'eng': {
        'decor_stud_list': {
            'header': 'Students list',
            'delimiter': '*',
            'width': 20},
        'commands':
            [' ',
             'All models',
             'List',
             'Dict',
             'Search',
             'Delete',
             'Exit'],
        'msg': ['Select a language (rus/eng): ',
                'Insert command: ',
                'Insert student ID: ',
                'Not found',
                'Invalid command. Please try again.',
                'Student is delete',
                'Good bye']
    }
}
