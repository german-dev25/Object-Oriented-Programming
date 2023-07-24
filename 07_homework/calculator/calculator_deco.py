from calculator.i_calculator import ICalculator, N
from logger.decorator import log_method
from logger.i_logger import ILogger


class CalculatorDeco(ICalculator):
    """
    Класс CalculatorDeco представляет собой декоратор для калькулятора
    Calculator.

    :param :
        old_calc (ICalculator): Экземпляр исходного калькулятора.
        logger (ILogger): Экземпляр логгера для записи сообщений.

    :methods :
        addition(arg: N) -> Calculator:
            Метод для выполнения операции сложения с записью лога.

        multiplication(arg: N) -> Calculator:
            Метод для выполнения операции умножения с записью лога.

        division(arg: N) -> Calculator:
            Метод для выполнения операции деления с записью лога.

        subtraction(arg: N) -> Calculator:
            Метод для выполнения операции вычитания с записью лога.

        get_result() -> N:
            Метод для получения текущего результата с записью лога.

        clear() -> None:
            Метод для очистки "памяти" калькулятора с записью лога.
    """
    def __init__(self,
                 old_calc: ICalculator,
                 logger: ILogger):
        self.old_calc = old_calc
        self.logger = logger

    @log_method
    def addition(self, arg: N):
        self.old_calc.addition(arg)
        return self

    @log_method
    def multiplication(self, arg: N):
        self.old_calc.multiplication(arg)
        return self

    @log_method
    def division(self, arg: N):
        try:
            self.old_calc.division(arg)
        except ZeroDivisionError:
            self.logger.log_error("Error: division by zero")
        return self

    @log_method
    def subtraction(self, arg: N):
        self.old_calc.subtraction(arg)
        return self

    @log_method
    def get_result(self) -> N:
        return self.old_calc.get_result()

    @log_method
    def clear(self) -> None:
        self.old_calc.clear()

