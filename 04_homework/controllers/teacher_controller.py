from typing import Optional

from controllers.i_person_controller import IPersonController
from domen.teacher import Teacher
from services.teacher_service import TeacherService


class TeacherController(IPersonController):
    """
    Класс TeacherController реализует интерфейс IPersonController и
    управляет созданием учителей и выплатой зарплаты.

    :attr :
        teach_service (TeacherService): Сервис для работы с учителями.

    :methods :
        create(first_name: str, age: float, acad_degree: Optional[str] = None) -> None:
            Создает нового учителя и добавляет его в сервис teach_service.
            При необходимости сортирует список учителей по ФИО.

        pay_salary(person: Teacher) -> None:
            Выплачивает зарплату учителю.
    """
    teach_service: TeacherService = TeacherService()

    def create(self, first_name: str, age: float,
               acad_degree: Optional[str] = None) -> None:
        """
        Создает новый объект Teacher и добавляет его в сервис teach_service.
        При необходимости сортирует список учителей по ФИО.

        :param first_name: (srt): Имя учителя.
        :param age: (float): Возраст учителя.
        :param acad_degree: (str or None): Ученая степень учителя
            (необязательный параметр).
        :return: None
        """
        self.teach_service.create(first_name=first_name, age=age)
        if len(self.teach_service.get_all()) > 1:
            self.teach_service.sort_by_fio()

    @staticmethod
    def pay_salary(person: Teacher) -> None:
        """
        Выплачивает зарплату учителю.

        :param person: (Teacher): Учитель, которому нужно выплатить зарплату.
        :return: None
        """
        if isinstance(person, Teacher):
            print(person.get_name() + ' учитель - выплачена зарплата')

