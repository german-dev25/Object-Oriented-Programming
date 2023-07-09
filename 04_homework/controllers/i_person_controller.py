from abc import ABC, abstractmethod
from domen.person import N


class IPersonController(ABC):
    """
    Интерфейс контроллера для создания персон.

    :methods:
        create(first_name: str, age: int) -> None:
            Абстрактный метод для создания персоны.

    """

    @abstractmethod
    def create(self, first_name: str, age: N) -> None:
        """
        Абстрактный метод для создания персоны.

        :param first_name: (str): Имя персоны.
        :param age: (N): Возраст персоны.
        :return: None
        """