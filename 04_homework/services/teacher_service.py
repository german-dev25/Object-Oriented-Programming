from functools import cmp_to_key
from typing import List

from domen.person_average_age import AverageAge
from domen.person_comparator import PersonComparator
from domen.teacher import Teacher
from services.i_person_service import IPersonService


class TeacherService(IPersonService):
    """
    Класс TeacherService предоставляет сервисные функции для работы с учителями.

    :attr :
        teachers (List[Teacher]): Список учителей.

    :methods :
        get_all() -> List[Teacher]:
            Возвращает список всех учителей.

        create(first_name: str, age: float) -> None:
            Создает нового учителя и добавляет его в список.

        sort_by_fio() -> None:
            Сортирует список учителей по возрасту и ФИО.

        print_list() -> None:
            Выводит список учителей на консоль.

        print_average() -> None:
            Выводит средний возраст учителей на консоль.
    """
    teachers: List[Teacher] = []

    def get_all(self) -> List[Teacher]:
        """
        Возвращает список всех учителей.

        :return :
            List[Teacher]: Список учителей.
        """
        return self.teachers

    def create(self, first_name: str, age: float) -> None:
        """
        Создает нового учителя и добавляет его в список.

        :param first_name: (str): Имя учителя.
        :param age: (float): Возраст учителя.
        """
        self.teachers.append(Teacher(first_name=first_name,
                                     age=age))

    def sort_by_fio(self) -> None:
        """
        Сортирует список учителей по возрасту и ФИО.
        """
        self.teachers = sorted(self.teachers,
                               key=cmp_to_key(PersonComparator.compare))

    def print_list(self) -> None:
        """
        Выводит список учителей на консоль.
        """
        for teacher in self.teachers:
            print(teacher)

    def print_average(self) -> None:
        """
        Выводит средний возраст учителей на консоль.
        """
        AverageAge.average_ages(self.teachers)
