from classes.buyer import Buyer
from classes.ordinary_client import OrdinaryClient
from interfaces.i_buyer_behaviour import IBuyerBehaviour


class TaxService(Buyer, IBuyerBehaviour):
    """
    Класс, представляющий службу.

    Attributes:
        name (str): Имя службы.
        is_take_order (bool): Флаг, указывающий получила ли служба заказ.
        is_make_order (bool): Флаг, указывающий сделала ли служба заказ.

    Methods:
        get_name() -> str:
            Возвращает имя службы.
        is_take_order() -> bool:
            Возвращает флаг, указывающий получила ли служба заказ.
        is_make_order() -> bool:
            Возвращает флаг, указывающий сделала ли служба заказ.
        set_take_order(take_order: bool) -> None:
            Устанавливает флаг, указывающий получила ли служба заказ.
        set_make_order(make_order: bool) -> None:
            Устанавливает флаг, указывающий сделала ли служба заказ.
        get_buyer() -> Buyer:
            Возвращает экземпляр, представляющий службу.
        is_make_return() -> bool:
            Проверяет, возвращает ли служба товар.
        set_make_return(is_make_return: bool) -> None:
            Устанавливает значение флага возврата товара.
        is_have_returned() -> bool:
            Проверяет, вернула ли служба товар.
        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает значение флага возвращения товара.
    """

    def __init__(self):
        """
        Инициализирует объект TaxService.
        """

        super().__init__(name="Tax audit")
        self.is_take_order: bool = False
        self.is_make_order: bool = False

    def get_name(self) -> str:
        """ Возвращает имя клиента.

        :return :
            str: Имя клиента.
        """
        return self.name

    def is_take_order(self) -> bool:
        """ Проверяет, получила ли служба заказ.

        :return :
            bool: Флаг получения заказа.
        """
        return self.is_take_order

    def is_make_order(self) -> bool:
        """ Проверяет, сделала ли служба заказ.

        :return :
            bool: Флаг совершения заказа.
        """
        return self.is_make_order

    def set_take_order(self, take_order: bool) -> None:
        """ Устанавливает значение флага получения заказа.

        :arg :
            take_order (bool): Значение флага получения заказа.
        """
        self.is_take_order = take_order

    def set_make_order(self, make_order: bool) -> None:
        """ Устанавливает значение флага совершения заказа.

        :arg :
            make_order (bool): Значение флага совершения заказа.
        """
        self.is_make_order = make_order

    def get_buyer(self):
        """ Возвращает самого клиента. """
        return OrdinaryClient(self.name)

    def is_make_return(self) -> bool:
        """ Проверяет, возвращает ли служба товар.

        :return :
            bool: Флаг возврата товара.
        """
        return self.is_make_return

    def set_make_return(self, is_make_return: bool) -> None:
        """ Устанавливает значение флага возврата товара.

        :arg :
            is_make_return (bool): Значение флага возврата товара.
        """
        self.is_make_return = True

    def is_have_returned(self) -> bool:
        """ Проверяет, вернула ли служба товар.

        :return :
            bool: Флаг возвращения товара.
        """
        return self.is_have_returned

    def set_have_returned(self, is_have_returned: bool) -> None:
        """ Устанавливает значение флага возвращения товара.

        :arg :
            is_have_returned (bool): Значение флага возвращения товара.
        """
        self.is_have_returned = True
