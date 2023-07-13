from typing import List

from controller.i_get_student_view import IGetStudentView
from view.languages import LANG_DICT
from model.student import Student
from view.decorators import PrintHeaderDecorator


class StudentView(IGetStudentView):
    """ Класс представления Студента """
    def __init__(self, language: str):
        self.language = language

    def print_all_students(self, students_list: List[Student]) -> None:
        """
        Выводит список студентов.

        :param students_list: Список студентов.
        :type students_list: List[Student]
        """
        @PrintHeaderDecorator(**LANG_DICT[self.language]['decor_stud_list'])
        def print_students(students: List[Student]) -> None:
            list(map(print, students))

        print_students(students_list)
