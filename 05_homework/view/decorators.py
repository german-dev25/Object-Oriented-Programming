from functools import wraps


class PrintHeaderDecorator:
    """
    Декоратор для печати заголовка с использованием разделителя.

    :param header: Заголовок.
    :param width: Ширина заголовка.
    :param delimiter: Разделитель.
    """

    def __init__(self, header, width, delimiter):
        self.delimiter = delimiter
        self.header = header
        self.width = width

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Обертка функции с печатью заголовка.

            :param args: Позиционные аргументы функции.
            :param kwargs: Именованные аргументы функции.
            :return: Результат выполнения функции.
            """
            print('{}{}{}'.format(
                self.delimiter * 9,
                self.center_text(self.header, width=self.width),
                self.delimiter * 9)
            )
            result = func(*args, **kwargs)
            print(f'{self.delimiter}' * 2 * self.width)
            return result

        return wrapper

    @staticmethod
    def center_text(text: str, width: int) -> str:
        """
        Центрирует текст в заданной ширине.

        :param text: Текст для центрирования.
        :param width: Ширина.
        :return: Центрированный текст.
        """
        padding = (width - len(text)) // 2
        return ' ' * padding + text + ' ' * padding
