from calculator.i_calculator import ICalculator, N


class Calculator(ICalculator):
    """
    Класс Calculator представляет собой простой калькулятор.

    :param :
        primary_arg (N): Начальное значение калькулятора.

    :methods :
        addition(arg: N) -> Calculator:
            Метод для выполнения операции сложения.

        multiplication(arg: N) -> Calculator:
            Метод для выполнения операции умножения.

        division(arg: N) -> Calculator:
            Метод для выполнения операции деления.

        subtraction(arg: N) -> Calculator:
            Метод для выполнения операции вычитания.

        get_result() -> N:
            Метод для получения текущего результата.

        clear() -> None:
            Метод для очистки памяти калькулятора.
    """

    def __init__(self, primary_arg: N = 0):
        self.primary_arg = primary_arg

    def addition(self, arg: N):
        self.primary_arg += arg
        return self

    def multiplication(self, arg: N):
        self.primary_arg *= arg
        return self

    def division(self, arg: N):
        try:
            self.primary_arg /= arg
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")

        return self

    def subtraction(self, arg: N):
        self.primary_arg -= arg
        return self

    def get_result(self):
        return self.primary_arg

    def clear(self):
        self.primary_arg = 0
