from abc import abstractmethod, ABC


class IBuyerBehaviour(ABC):
    """
    Интерфейс для определения поведения покупателя.

    Methods:
        is_take_order() -> bool:
            Проверяет, получил ли покупатель заказ.

        is_make_order() -> bool:
            Проверяет, сделал ли покупатель заказ.

        set_take_order(take_order: bool) -> None:
            Устанавливает флаг получения заказа для покупателя.

        set_make_order(make_order: bool) -> None:
            Устанавливает флаг сделанного заказа для покупателя.

        get_buyer():
            Возвращает объект покупателя.
    """

    @abstractmethod
    def is_take_order(self) -> bool:
        """
        Проверяет, получил ли покупатель заказ.

        :return :
            bool: Флаг, указывающий получил ли покупатель заказ.
        """

    @abstractmethod
    def is_make_order(self) -> bool:
        """
        Проверяет, сделал ли покупатель заказ.

        :return :
            bool: Флаг, указывающий сделал ли покупатель заказ.
        """

    @abstractmethod
    def set_take_order(self, take_order: bool) -> None:
        """
        Устанавливает флаг получения заказа для покупателя.

        :arg :
            take_order (bool): Флаг, указывающий получил ли покупатель заказ.
        """

    @abstractmethod
    def set_make_order(self, make_order: bool) -> None:
        """
        Устанавливает флаг сделанного заказа для покупателя.

        :arg :
            make_order (bool): Флаг, указывающий сделал ли покупатель заказ.
        """

    @abstractmethod
    def get_buyer(self):
        """
        Возвращает объект покупателя.
        """
