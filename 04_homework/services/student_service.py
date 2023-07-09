from functools import cmp_to_key
from typing import List

from domen.person_average_age import AverageAge
from domen.student import Student
from domen.person_comparator import PersonComparator
from services.i_person_service import IPersonService


class StudentService(IPersonService):
    """
    Класс StudentService предоставляет сервисные функции для работы
    со списком студентов.

    :attr:
        count (int): Счетчик студентов.
        students (List[Student]): Список студентов.

    :methods:
        get_all() -> List[Student]:
            Возвращает список всех студентов.

        create(first_name: str, age: int) -> None:
            Создает нового студента и добавляет его в список.

        sort_by_fio() -> None:
            Сортирует список студентов по ФИО с использованием
            компаратора PersonComparator.

        print_list() -> None:
            Выводит список студентов на консоль.

        print_average() -> None:
            Вычисляет и выводит средний возраст студентов на консоль.

    """
    count: int = 0
    students: List[Student] = []

    def get_all(self) -> List[Student]:
        """
        Возвращает список всех студентов.

        :return:
            List[Student]: Список всех студентов.
        """
        return self.students

    def create(self, first_name: str, age: int) -> None:
        """
        Создает нового студента и добавляет его в список.

        :param first_name: Имя студента.
        :param age: Возраст студента.
        """
        self.students.append(Student(name=first_name,
                                     age=age,
                                     student_id=self.count))
        self.count += 1

    def sort_by_fio(self) -> None:
        """
        Сортирует список студентов по ФИО с использованием
        компаратора PersonComparator.
        """
        self.students = sorted(self.students,
                               key=cmp_to_key(PersonComparator.compare)
                               )

    def print_list(self) -> None:
        """
        Выводит список всех студентов.
        """
        for student in self.students:
            print(student)

    def print_average(self) -> None:
        """
        Выводит средний возраст студентов.
        """
        AverageAge.average_ages(self.students)
