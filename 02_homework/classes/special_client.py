from classes.buyer import Buyer
from interfaces.i_buyer_behaviour import IBuyerBehaviour


class SpecialClient(Buyer, IBuyerBehaviour):
    """
    Класс, представляющий особого клиента.

    Attributes:
        name (str): Имя клиента.
        vip_id (int): Идентификатор VIP-клиента.
        is_take_order (bool): Флаг, указывающий получил ли клиент заказ.
        is_make_order (bool): Флаг, указывающий сделал ли клиент заказ.
        is_make_return (bool): Флаг, указывающий возвращает ли клиент товар.
        is_have_returned (bool): Флаг, указывающий вернул ли клиент товар.

    Methods:
        get_name() -> str:
            Возвращает имя клиента.
        is_take_order() -> bool:
            Проверяет, получил ли клиент заказ.
        is_make_order() -> bool:
            Проверяет, сделал ли клиент заказ.
        set_take_order(take_order: bool) -> None:
            Устанавливает значение флага получения заказа.
        set_make_order(make_order: bool) -> None:
            Устанавливает значение флага совершения заказа.
        get_buyer():
            Возвращает самого клиента.
        is_make_return() -> bool:
            Проверяет, возвращает ли клиент товар.
        set_make_return(is_make_return: bool) -> None:
            Устанавливает значение флага возврата товара.
        is_have_returned() -> bool:
            Проверяет, вернул ли клиент товар.
        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает значение флага возвращения товара.
    """

    def __init__(self, name: str, vip_id: int):
        """
        Инициализирует объект SpecialClient.

        :arg :
            name (str): Имя клиента.
            vip_id (int): Идентификатор VIP-клиента.
        """
        super().__init__(name + ' - VIP')
        self.vip_id = vip_id

    def get_name(self) -> str:
        """ Возвращает имя клиента.

        :return :
            str: Имя клиента.
        """
        return self.name

    def is_take_order(self) -> bool:
        """ Проверяет, получил ли клиент заказ.

        :return :
            bool: Флаг получения заказа.
        """
        return self.is_take_order

    def is_make_order(self) -> bool:
        """ Проверяет, сделал ли клиент заказ.

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
        return self

    def is_make_return(self) -> bool:
        """ Проверяет, возвращает ли клиент товар.

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
        """ Проверяет, вернул ли клиент товар.

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
