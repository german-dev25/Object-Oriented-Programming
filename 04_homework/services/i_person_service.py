from abc import abstractmethod, ABC
from typing import List
from domen.person_comparator import P


class IPersonService(ABC):
    """
    Абстрактный класс IPersonService, представляющий интерфейс сервиса
    для работы с Person.

    :methods:
        get_all() -> List[P]:
            Абстрактный метод для получения списка всех Person.

            :return:
                List[P]: Список персон.

        create(first_name: str, age: int) -> None:
            Абстрактный метод для создания новой Person.

            :param:
                first_name (str): Имя Person.
                age (int): Возраст Person.

            :return:
                None
    """

    @abstractmethod
    def get_all(self) -> List[P]:
        """
        Абстрактный метод для получения списка всех Person.

        :return:
            List[P]: Список Person.
        """
    @abstractmethod
    def create(self, first_name: str, age: int) -> None:
        """
        Абстрактный метод для создания новой Person.

        :param:
            first_name (str): Имя Person.
            age (int): Возраст Person.

        :return:
            None
        """