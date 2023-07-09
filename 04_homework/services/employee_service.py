from functools import cmp_to_key
from typing import List
from domen.employee import Employee
from domen.person_average_age import AverageAge
from domen.person_comparator import PersonComparator
from services.i_person_service import IPersonService


class EmployeeService(IPersonService):
    """
        Сервис для работы с сотрудниками.
        Реализует интерфейс IPersonService.

        :attr employees: Список сотрудников.

        :methods:
            get_all() -> List[Employee]:
                Возвращает список всех сотрудников.

            create(first_name: str, age: int) -> None:
                Создает нового сотрудника с указанным именем и возрастом.

            sort_by_fio() -> None:
                Сортирует список сотрудников по ФИО.

            print_list() -> None:
                Выводит список всех сотрудников.

            print_average() -> None:
                Выводит средний возраст сотрудников.
        """

    employees: List[Employee] = []

    def get_all(self) -> List[Employee]:
        """
        Возвращает список всех сотрудников.

        :return: Список сотрудников.
        """
        return self.employees

    def create(self, first_name: str, age: int) -> None:
        """
        Создает нового сотрудника с указанным именем и возрастом.

        :param first_name: (str): Имя сотрудника.
        :param age: (int): Возраст сотрудника.
        """
        self.employees.append(Employee(first_name=first_name,
                                       age=age))

    def sort_by_fio(self):
        """
        Сортирует список сотрудников по ФИО.
        """
        self.employees = sorted(self.employees,
                                key=cmp_to_key(PersonComparator.compare)
                                )

    def print_list(self) -> None:
        """
        Выводит список всех сотрудников.
        """
        for employee in self.employees:
            print(employee)

    def print_average(self) -> None:
        """
        Выводит средний возраст сотрудников.
        """
        AverageAge.average_ages(self.employees)
