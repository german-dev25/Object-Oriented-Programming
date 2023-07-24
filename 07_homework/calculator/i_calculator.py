from abc import ABC, abstractmethod
from typing import TypeVar

N = TypeVar('N', int, float, complex)


class ICalculator(ABC):
    """
    Абстрактный класс ICalculator представляет интерфейс для калькулятора.

    Methods:
        addition(arg: N)  -> N:
            Абстрактный метод для выполнения операции сложения.

        multiplication(arg: N)  -> N:
            Абстрактный метод для выполнения операции умножения.

        division(arg: N)  -> N:
            Абстрактный метод для выполнения операции деления.

        subtraction(arg: N)  -> N:
            Абстрактный метод для выполнения операции вычитания.
            
        get_result() -> N:
            Абстрактный метод для получения текущего результата.

        clear() -> None:
            Абстрактный метод для очистки "памяти" калькулятора.
    """

    @abstractmethod
    def addition(self, arg: N) -> N: pass

    @abstractmethod
    def multiplication(self, arg: N) -> N: pass

    @abstractmethod
    def division(self, arg: N) -> N: pass

    @abstractmethod
    def subtraction(self, arg: N) -> N: pass

    @abstractmethod
    def get_result(self) -> N: pass

    @abstractmethod
    def clear(self) -> None: pass
