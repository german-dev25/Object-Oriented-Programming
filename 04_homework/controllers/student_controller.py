from controllers.i_person_controller import IPersonController
from services.student_service import StudentService


class StudentController(IPersonController):
    """
    Класс StudentController реализует интерфейс IPersonController и
    управляет созданием студентов.

    :attr:
        data_service (StudentService): Сервис для работы со студентами.

    :methods:
        create(first_name: str, age: int) -> None:
            Создает нового студента с указанным именем и возрастом.
            Если в списке студентов больше одного элемента,
            выполняет сортировку по ФИО.
    """

    data_service: StudentService = StudentService()

    def create(self, first_name: str, age: int) -> None:
        """
        Создает нового студента с указанным именем и возрастом.
        Если в списке студентов больше одного студента, выполняет сортировку
        по ФИО.

        :param first_name: (str): Имя студента.
        :param age: (age): Возраст студента.
        :return: None
        """
        self.data_service.create(first_name=first_name, age=age)
        if len(self.data_service.get_all()) > 1:
            self.data_service.sort_by_fio()
