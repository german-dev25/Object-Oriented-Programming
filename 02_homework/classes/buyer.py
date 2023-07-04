from abc import ABC, abstractmethod
from interfaces.i_buyer_behaviour import IBuyerBehaviour
from interfaces.i_return_order import IReturnOrder


class Buyer(IReturnOrder, IBuyerBehaviour, ABC):
    """ Абстрактный класс, представляющий покупателя.

    :attr :
        name (str): Имя покупателя.
        is_take_order (bool): Флаг - получил ли покупатель заказ.
        is_make_order (bool): Флаг - сделал ли покупатель заказ.
        is_make_return (bool): Флаг - возвращает ли покупатель товар.
        is_have_returned (bool): Флаг - вернул ли покупатель товар.

    Methods:
        get_name() -> str:
            Возвращает имя покупателя.
    """

    def __init__(self, name: str):
        """ Инициализирует объект Buyer.

        :param :
            name (str): Имя покупателя.
        """
        self.name = name
        self.is_take_order: bool = False
        self.is_make_order: bool = False
        self.is_make_return: bool = False
        self.is_have_returned: bool = False

    @abstractmethod
    def get_name(self) -> str:
        """ Возвращает имя покупателя.

        :return :
            (str): Имя покупателя.
        """
