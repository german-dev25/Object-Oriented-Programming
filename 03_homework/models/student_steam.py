from typing import List
from models.student_group import StudentGroup


class StudentSteam:
    """
    Класс StudentSteam представляет поток студентов.

    :attr :
        steam (List[StudentGroup]):
            Список групп студентов в потоке.
        steam_id (int):
            Идентификатор потока студентов.

    :method :
        get_steam(): 
            Возвращает список групп студентов в потоке.
            
        set_steam(steam: List[StudentGroup]): 
            Устанавливает список групп студентов в потоке.
            
        get_steam_id(): 
            Возвращает идентификатор потока студентов.
            
        set_steam_id(steam_id: int): 
            Устанавливает идентификатор потока студентов.
            
        __str__(): 
            Возвращает строковое представление объекта StudentSteam.
            
        __iter__(): 
            Итератор, который позволяет итерироваться по группам студентов 
            в потоке.
            
        __next__(): 
            Возвращает следующую группу студентов в потоке при каждой итерации.

    :property :
        get_steam_len:
            Возвращает количество групп студентов в потоке.
    """

    def __init__(self, steam: List[StudentGroup], steam_id: int):
        """
        Инициализирует объект класса StudentSteam.

        :arg :
            steam (List[StudentGroup]): 
                Список групп студентов в потоке.
            
            steam_id (int): 
                Идентификатор потока студентов.
        """
        self.steam = steam
        self.steam_id = steam_id

    def get_steam(self) -> List[StudentGroup]:
        """
        Возвращает список групп студентов в потоке.

        :return :
            List[StudentGroup]: Список групп студентов в потоке.
        """
        return self.steam

    def set_steam(self, steam: List[StudentGroup]) -> None:
        """
        Устанавливает список групп студентов в потоке.

        :arg :
            steam (List[StudentGroup]): Список групп студентов в потоке.
        """
        self.steam = steam

    def get_steam_id(self) -> int:
        """
        Возвращает идентификатор потока студентов.

        :return :
            int: Идентификатор потока студентов.
        """
        return self.steam_id

    def set_steam_id(self, steam_id: int) -> None:
        """
        Устанавливает идентификатор потока студентов.

        :arg :
            steam_id (int): Идентификатор потока студентов.
        """
        self.steam_id = steam_id

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта StudentSteam.

        :return :
            str: Строковое представление объекта StudentSteam.
        """
        group_info = "\n".join(
            f"Группа №{group.get_group_id()}: "
            f"студентов {group.get_group_len} \n"
            f"{', '.join(str(student) for student in group.get_group())}"
            for group in self.steam
        )
        return f'Поток №{self.steam_id} \n' \
               f'Число групп = {self.get_steam_len} \n' \
               f'{group_info}'

    @property
    def get_steam_len(self):
        """
        Возвращает количество групп студентов в потоке.

        :return :
            int: Количество групп студентов в потоке.
        """
        return len(self.steam)

    def __iter__(self):
        """
        Возвращает итератор для класса StudentSteam.

        :return :
            StudentSteam: Итератор для класса StudentSteam.
        """
        self.index = 0
        return self

    def __next__(self) -> StudentGroup:
        """
        Возвращает следующую группу студентов в потоке при каждой итерации.

        :return :
            StudentGroup: Следующая группа студентов в потоке.

        :raise :
            StopIteration: Если достигнут конец итерируемого объекта.
        """
        if self.index >= self.get_steam_len:
            raise StopIteration
        group = self.steam[self.index]
        self.index += 1
        return group
