from calculator.i_calculator import ICalculator, N
from logger.i_logger import ILogger


class ControllerCalculator:
    """
    Класс ControllerCalculator представляет собой контроллер для работы
    с калькулятором.

    :param :
        calc (ICalculator): Экземпляр калькулятора.
        logger_file (ILogger, optional): Экземпляр логгера для записи
        сообщений в файл.
        logger_console (ILogger, optional): Экземпляр логгера для записи
        сообщений в консоль.

    :methods :
        __call__() -> None:
            Метод для взаимодействия с пользователем и выполнения операций
            над калькулятором.

        get_arg(text: str) -> N:
            Метод для получения аргумента от пользователя.

        ask_user() -> bool:
            Метод для запроса продолжения работы и очистки калькулятора.
    """

    def __init__(self, calculator: ICalculator,
                 logger_file: ILogger = None,
                 logger_console: ILogger = None):
        self.calc: ICalculator = calculator
        self.logger_file = logger_file
        self.logger_console = logger_console

    def __call__(self):
        print(self.hello_text())
        primary_arg = self.get_arg('Введите 1-й аргумент: ')
        self.calc.addition(primary_arg)

        while True:
            cmd: str = input('Введите команду: ').strip()
            # # конструкция match - case
            # match cmd:
            #     case '+':
            #         self.calc.addition(self.get_arg('Введите 2-й аргумент: '))
            #     case '-':
            #         self.calc.subtraction(
            #             self.get_arg('Введите 2-й аргумент: '))
            #     case '*':
            #         self.calc.multiplication(
            #             self.get_arg('Введите 2-й аргумент: '))
            #     case '/':
            #         self.calc.division(self.get_arg('Введите 2-й аргумент: '))
            #     case '=':
            #         print(self.calc.get_result())
            #         self.ask_user()
            #     case _:
            #         print('Неизвестная команда')
            # конструкция if-elif-else
            if cmd == '+':
                self.calc.addition(self.get_arg('Введите 2-й аргумент: '))
            elif cmd == '-':
                self.calc.subtraction(
                    self.get_arg('Введите 2-й аргумент: '))
            elif cmd == '*':
                self.calc.multiplication(
                    self.get_arg('Введите 2-й аргумент: '))
            elif cmd == '/':
                self.calc.division(self.get_arg('Введите 2-й аргумент: '))
            elif cmd == '=':
                print(self.calc.get_result())
                self.ask_user()
            else:
                print('Неизвестная команда')

    @staticmethod
    def get_arg(text: str) -> N:
        arg = input(f'{text}').strip()
        if 'j' in arg:
            return complex(arg)
        else:
            try:
                return int(arg)
            except ValueError:
                return float(arg)

    def ask_user(self):
        if 'n' in input('Продолжить (Y/N)? ').lower():
            print('Good bye')
            exit()
        if 'y' in input('Очистить память (Y/N)? ').lower():
            self.calc.clear()
            primary_arg = self.get_arg('Введите 1-й аргумент: ')
            self.calc.addition(primary_arg)
            return True

    @staticmethod
    def hello_text() -> str:
        return f'Добро пожаловать в калькулятор\n' \
               'Доступные команды: +, -, /, *\n' \
               'Считаются числа целые, дробные\n' \
               'и комплексные в формате a + bj'
