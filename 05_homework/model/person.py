from abc import ABC
from typing import Generic, TypeVar

T = TypeVar('T')
N = TypeVar('N', int, float)


class Person(Generic[T, N], ABC):
    """
    Абстрактный класс Person, представляющий человека.

    :attr :
        name (T): Имя человека.
        age (N): Возраст человека.

    :methods :
        get_name() -> T:
            Возвращает имя человека.

        set_name(name: T) -> None:
            Устанавливает имя человека.

        get_age() -> N:
            Возвращает возраст человека.

        set_age(age: N) -> None:
            Устанавливает возраст человека.

        __str__() -> str:
            Возвращает строковое представление человека.
    """

    def __init__(self, name: T, age: N):
        """
        Инициализация объекта класса Person.

        :atr :
            name (T): Имя человека.
            age (N): Возраст человека.
        """
        self.name = name
        self.age = age

    def get_name(self) -> T:
        """
        Возвращает имя человека.

        :return :
            T: Имя человека.
        """
        return self.name

    def set_name(self, name: T) -> None:
        """
        Устанавливает имя человека.

        :atr :
            name (T): Имя человека.
        """
        self.name = name

    def get_age(self) -> N:
        """
        Возвращает возраст человека.

        :return :
            N: Возраст человека.
        """
        return self.age

    def set_age(self, age: N) -> None:
        """
        Устанавливает возраст человека.

        :atr :
            age (N): Возраст человека.
        """
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление человека.

        :return :
            str: Строковое представление человека.
        """
        return f'{type(self).__name__} [name={self.name}, age={self.age}]'
