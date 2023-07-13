from abc import ABC, abstractmethod
from typing import List

from model.student import Student


class IGetStudentModel(ABC):
    """
    Абстрактный класс, представляющий интерфейс модели получения информации о студентах.

    :methods:
        get_all_students() -> List[Student]:
            Абстрактный метод для получения списка всех студентов.

        search_student(self, student_id: int) -> List[Student]:
            Абстрактный метод для поиска студента по его идентификатору.

        delete_student(student_id: int) -> bool:
            Абстрактный метод для удаления студента по его идентификатору.
    """

    @abstractmethod
    def get_all_students(self) -> List[Student]:
        """
        Получает список всех студентов.

        :return:
            List[Student]: Список всех студентов.
        """

    @abstractmethod
    def search_student(self, student_id: int) -> List[Student]:
        """
        Ищет студента по его идентификатору.

        :param student_id:
            int: Идентификатор студента.
        :return:
            Student: Список студентов, соответствующих
            заданному идентификатору.
        """

    @abstractmethod
    def delete_student(self, student_id: int) -> bool:
        """
        Удаляет студента по его идентификатору.

        :param student_id:
            int: Идентификатор студента.
        :return:
            bool: True, если удаление прошло успешно, иначе False.
        """