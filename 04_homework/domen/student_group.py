from typing import List
from domen.student import Student


class StudentGroup:
    """
    Класс StudentGroup представляет группу студентов.

    :attr :
        group (List[Student]): Список студентов в группе.
        group_id (int): Идентификатор группы.

    :method :
        get_group() -> List[Student]:
            Возвращает список студентов в группе.

        set_group(group: List[Student]) -> None:
            Устанавливает список студентов в группе.

        get_group_id() -> int:
            Возвращает идентификатор группы.

        set_group_id(group_id: int) -> None:
            Устанавливает идентификатор группы.

        __lt__(g: StudentGroup) -> bool:
            Определяет порядок сортировки групп студентов на основе количества
            студентов и идентификатора группы. Возвращает True, если текущая
            группа меньше, иначе False.

        __iter__() -> StudentGroup:
            Инициализирует итерацию по группе студентов.

        __next__() -> Student:
            Возвращает следующего студента в группе при итерации.
            Вызывает исключение StopIteration, если достигнут конец группы.

        __str__() -> str:
            Возвращает строковое представление группы студентов в формате:
            "StudentGroup group_id = <идентификатор группы>
            number of students = <количество студентов>
            group = {<список студентов в формате "name=Имя, age=Возраст, student_id=Идентификатор">}"

    :property :
        get_group_len:
            Возвращает количество студентов в поток.
    """

    def __init__(self, group: List[Student], group_id: int):
        self.group = group
        self.group_id = group_id

    def get_group(self) -> List[Student]:
        """
        Возвращает список студентов в группе.

        :return :
            List[Student]: Список студентов.
        """
        return self.group

    def set_group(self, group: List[Student]) -> None:
        """
        Устанавливает список студентов в группе.

        :arg :
            group (List[Student]): Список студентов.
        """
        self.group = group

    def get_group_id(self) -> int:
        """
        Возвращает идентификатор группы.

        :return :
            int: Идентификатор группы.
        """
        return self.group_id

    def set_group_id(self, group_id: int) -> None:
        """
        Устанавливает идентификатор группы.

        :arg :
            group_id (int): Идентификатор группы.
        """
        self.group_id = group_id

    @property
    def get_group_len(self):
        """
        Возвращает количество студентов в группе.

        :return :
            int: Количество студентов в группе.
        """
        return len(self.group)

    def __lt__(self, g: 'StudentGroup') -> bool:
        """
        Аналог compareTo встроенными возможностями языка. Используется по
        определению в sorted (сравнение вида (объект_1) < (объект_2))
        - позволяет определять порядок сортировки групп студентов на основе
        количества студентов и идентификатора группы. Возвращает True,
        если значение меньше, иначе False.

        :arg :
            g (StudentGroup): Группа студентов для сравнения.

        :return :
            bool: True, если значения меньше, иначе False.
        """
        if self.get_group_len == g.get_group_len:
            return self.group_id < g.group_id
        return self.get_group_len < g.get_group_len

    def __str__(self) -> str:
        """
        Возвращает строковое представление группы студентов.

        :return :
            str: Строковое представление группы студентов.
        """
        group_str = ",\n".join(str(student) for student in self.group)
        return f'Номер группы №{self.get_group_id()} \n' \
               f'студентов {self.get_group_len} \n' \
               f'группа = {{{group_str}}}'

    def __iter__(self):
        """
        Инициализирует итерацию по группе студентов.

        :return :
            StudentGroup: Итератор группы студентов.
        """
        self.index = 0
        return self

    def __next__(self) -> Student:
        """
        Возвращает следующего студента в группе при итерации.
        Вызывает исключение StopIteration, если достигнут конец группы.

        :return :
            Student: Следующий студент.

        :raise :
            StopIteration: Если достигнут конец группы.
        """
        if self.index >= self.get_group_len:
            raise StopIteration
        student = self.group[self.index]
        self.index += 1
        return student
