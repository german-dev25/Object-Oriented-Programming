from controller.i_get_student_model import IGetStudentModel
from controller.i_get_student_view import IGetStudentView
from view.languages import LANG_DICT
from view.view import StudentView


class StudentController:
    """
    Класс контроллера студентов.

    :param model: Модель, реализующая интерфейс IGetStudentModel.
    :param language: Язык выбранный пользователем (rus/eng).
    """

    def __init__(self, model: IGetStudentModel, language: str):
        """
        Инициализация объекта класса StudentController.

        :param model: Модель, реализующая интерфейс IGetStudentModel.
        :param language: Язык выбранный пользователем (rus/eng).
        """
        self.model = model
        self.language = language
        self.view: IGetStudentView = StudentView(language=language)

    def print(self) -> None:
        """
        Выводит на экран всех студентов.
        """
        self.view.print_all_students(self.model.get_all_students())

    def search_student(self, student_id: int) -> None:
        """
        Ищет студента по указанному идентификатору и выводит результат на экран.

        :param student_id: Идентификатор студента.
        """
        result = self.model.search_student(student_id=student_id)
        if result != [None]:
            self.view.print_all_students(result)
        else:
            print(LANG_DICT[self.language]['msg'][3])

    def delete_student(self, student_id: int) -> None:
        """
        Удаляет студента с указанным идентификатором и выводит результат на экран.

        :param student_id: Идентификатор студента.
        """
        if self.model.delete_student(student_id=student_id):
            print(LANG_DICT[self.language]['msg'][5])
            self.view.print_all_students(self.model.get_all_students())
        else:
            print(LANG_DICT[self.language]['msg'][3])
