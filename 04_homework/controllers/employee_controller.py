from typing import Optional

from controllers.i_person_controller import IPersonController
from domen.employee import Employee
from services.employee_service import EmployeeService


class EmployeeController(IPersonController):
    """
    Класс EmployeeController реализует интерфейс IPersonController и
    управляет созданием работников и выплатой зарплаты.

    :attr :
        emp_service (EmployeeService): Сервис для работы с сотрудниками.

    :methods :
        create(first_name: str, age: int, special: Optional[str] = None) -> None:
            Создает нового сотрудника с указанными параметрами и добавляет
            его в список сотрудников.
            Если в списке сотрудников больше одного,
            выполняет сортировку списка по ФИО.

        pay_salary(person: Employee) -> None:
            Выводит сообщение о выплате зарплаты указанному сотруднику.

    """

    emp_service: EmployeeService = EmployeeService()

    def create(self, first_name: str, age: int,
               special: Optional[str] = None) -> None:
        """
        Создает нового сотрудника с указанными параметрами и добавляет его
        в список сотрудников.
        Если в списке сотрудников больше одного, выполняет сортировку списка
        по ФИО.

        :param first_name: (str): Имя сотрудника.
        :param age: (int): Возраст сотрудника.
        :param special: (str or None): Должность сотрудника (необязательно).

        :return: None
        """
        self.emp_service.create(first_name=first_name, age=age)
        if len(self.emp_service.get_all()) > 1:
            self.emp_service.sort_by_fio()

    @staticmethod
    def pay_salary(person: Employee) -> None:
        """
        Выводит сообщение о выплате зарплаты для указанного сотрудника.

        :param person: (Employee): Сотрудник, которому выплачивается зарплата.

        :return: None
        """
        if isinstance(person, Employee):
            print(person.get_name() + ' выплачена зарплата')
