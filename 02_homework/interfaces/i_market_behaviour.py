from abc import ABC, abstractmethod
from typing import List
from classes.buyer import Buyer


class IMarketBehaviour(ABC):
    """
    Интерфейс для определения поведения магазина.

    Methods:
        accept_to_market(buyer: Buyer) -> None:
            Принимает покупателя в магазин.

        release_from_market(buyers: List[Buyer]) -> None:
            Освобождает покупателей из магазина.

        update() -> None:
            Обновляет состояние магазина.
    """

    @abstractmethod
    def accept_to_market(self, buyer: Buyer) -> None:
        """
        Принимает покупателя в магазин.

        :arg:
            buyer (Buyer): Покупатель.

        :return :
            None
        """

    @abstractmethod
    def release_from_market(self, buyers: List[Buyer]) -> None:
        """
        Освобождает покупателей из магазина.

        :arg:
            buyers (List[Buyer]): Список покупателей.

        :return :
            None
        """

    @abstractmethod
    def update(self) -> None:
        """
        Обновляет состояние магазина.

        :return :
            None
        """
