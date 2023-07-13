from abc import ABC, abstractmethod
from typing import List

from model.student import Student


class IGetStudentView(ABC):
    """
    Интерфейс для представления студентов.

    Абстрактный базовый класс, определяющий методы для
    вывода информации о студентах.

    :methods:
        print_all_students(students: List[Student]) -> None:
            Выводит информацию о всех студентах.

    """

    @staticmethod
    @abstractmethod
    def print_all_students(students: List[Student]) -> None:
        """
        Выводит информацию о всех студентах.

        :param students: Список студентов.
        :type students: List[Student]
        :return: None
        """