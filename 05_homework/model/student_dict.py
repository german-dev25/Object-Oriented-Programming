from typing import List, Dict

from controller.i_get_student_model import IGetStudentModel
from model.student import Student


class StudentDict(IGetStudentModel):
    """
    Класс, представляющий студентов в виде словаря.

    Наследуется от интерфейса IGetStudentModel.

    :param students: Словарь объектов Student.
    """
    def __init__(self, students: Dict[int, Student]):
        """
        Конструктор класса StudentDict.

        :param students: Словарь объектов Student.
        """
        self.students = students

    def get_all_students(self) -> List[Student]:
        """
        Возвращает список всех студентов.

        :return: Список студентов.
        """
        return list(self.students.values())

    def search_student(self, student_id: int) -> List[Student]:
        """
        Ищет студента по идентификатору.

        :param student_id: Идентификатор студента.
        :return: Список найденных студентов. Если студент не найден,
        возвращается [None] список.
        """
        return [next((student for student in self.students.values() if
                     student.get_student_id() == student_id), None)]

    def delete_student(self, student_id: int) -> bool:
        """
        Удаляет студента по идентификатору.

        :param student_id: Идентификатор студента.
        :return: True, если студент успешно удален.
        False, если студент с заданным идентификатором не найден.
        """
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
