from classes.buyer import Buyer


class BuyerMixin(Buyer):
    """Класс миксинов для классов Покупателей
    """
    def get_name(self) -> str:
        """
        Возвращает имя клиента.

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
        """ Возвращает самого клиента.
        """
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
