from typing import TypeVar

from domen.employee import Employee
from domen.student import Student
from domen.teacher import Teacher

P = TypeVar('P', Student, Teacher, Employee)


class PersonComparator:
    """
        Класс PersonComparator используется для сравнения объектов типов
        Student, Teacher и Employee.

    :methods:
        compare(o1: P, o2: P) -> int:
            Сравнивает два объекта типа P по имени и возрасту.
            Возвращает:
                0, если объекты равны,
                -1, если o1 меньше o2,
                1, если o1 больше o2.
    """

    @staticmethod
    def compare(o1: P, o2: P) -> int:
        """
        Сравнивает два объекта типа P по имени и возрасту.

        :param o1: Первый объект для сравнения.
        :param o2: Второй объект для сравнения.
        :return: 0, если объекты равны,
                 -1, если o1 меньше o2,
                 1, если o1 больше o2.
        """
        if o1.get_name() == o2.get_name():
            if o1.get_age() == o2.get_age():
                return 0
            elif o1.get_age() < o2.get_age():
                return -1
            else:
                return 1
        elif o1.get_name() < o2.get_name():
            return -1
        else:
            return 1
