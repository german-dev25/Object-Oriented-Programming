from abc import ABC, abstractmethod
from classes.buyer import Buyer


class IQueueBehaviour(ABC):
    """
    Интерфейс, представляющий поведение очереди магазина.

    Methods:
        take_in_queue(buyer: Buyer) -> None:
            Помещает покупателя в очередь.

        release_from_queue() -> None:
            Удаляет покупателя из очереди.

        take_order() -> None:
            Обрабатывает получение заказа покупателем.

        give_order() -> None:
            Обрабатывает выдачу заказа покупателю.
    """

    @abstractmethod
    def take_in_queue(self, buyer: Buyer) -> None:
        """
        Помещает покупателя в очередь.

        :arg :
            buyer (Buyer): Покупатель.

        :return :
            None
        """

    @abstractmethod
    def release_from_queue(self) -> None:
        """
        Удаляет покупателя из очереди.

        :return :
            None
        """

    @abstractmethod
    def take_order(self) -> None:
        """
        Обрабатывает получение заказа покупателем.

        :return :
            None
        """

    @abstractmethod
    def give_order(self) -> None:
        """
        Обрабатывает выдачу заказа покупателю.

        :return :
            None
        """
