from typing import List

from controller.i_get_student_model import IGetStudentModel
from model.student import Student


class StudentList(IGetStudentModel):
    """
    Класс, представляющий студентов в виде списка.

    Наследуется от интерфейса IGetStudentModel.

    :param students: Список объектов Student.
    """
    def __init__(self, students: List[Student]):
        """
        Конструктор класса StudentList.

        :param students: Список объектов Student.
        """
        self.students = students

    def get_all_students(self) -> List[Student]:
        """
        Возвращает все объекты студентов в списке.

        :return: Список объектов Student.
        """
        return self.students

    def search_student(self, student_id: int) -> List[Student]:
        """
        Поиск студента по указанному идентификатору.

        :param student_id: Идентификатор студента.
        :return: Список найденных объектов Student или список [None], если студент не найден.
        """
        return [next((student for student in self.students if
                     student.get_student_id() == student_id), None)]

    def delete_student(self, student_id: int) -> bool:
        """
        Удаляет студента с указанным идентификатором из списка.

        :param student_id: Идентификатор студента.
        :return: True, если студент успешно удален,
        False, если студент не найден.
        """
        for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                return True
        return False
