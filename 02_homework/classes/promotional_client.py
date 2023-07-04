from classes.buyer import Buyer
from interfaces.i_buyer_behaviour import IBuyerBehaviour


class PromoClient(Buyer, IBuyerBehaviour):
    """
       Класс PromoClient представляет клиента-участника акции.

       Attributes:
           promo_participants (dict): Словарь, содержащий количество
           участников для каждой акции.
           promo_name (str): Название акции.
           promo_cl_id (int): Идентификатор клиента-участника.

       Methods:
           get_name(self) -> str:
               Возвращает имя клиента.
           get_promo_participants(self) -> dict:
               Возвращает словарь с количеством участников для каждой акции.
           get_promo_num(self) -> int:
               Возвращает количество участников для текущей акции.
           is_take_order(self) -> bool:
               Возвращает флаг, указывающий, получил ли клиент заказ.
           is_make_order(self) -> bool:
               Возвращает флаг, указывающий, сделал ли клиент заказ.
           set_take_order(self, take_order: bool) -> None:
               Устанавливает флаг получения заказа.
           set_make_order(self, make_order: bool) -> None:
               Устанавливает флаг совершения заказа.
           get_buyer(self) -> Buyer:
               Возвращает объект Buyer, представляющий клиента.
            is_make_return() -> bool:
                Проверяет, возвращает ли клиент товар.
            set_make_return(is_make_return: bool) -> None:
                Устанавливает значение флага возврата товара.
            is_have_returned() -> bool:
                Проверяет, вернул ли клиент товар.
            set_have_returned(is_have_returned: bool) -> None:
                Устанавливает значение флага возвращения товара.
       """
    promo_participants: dict = {
        'Лето 2023': 0,
        'Жаркая распродажа': 0,
    }

    def __init__(self, name: str, promo_name: str, promo_cl_id: int):
        """
        Инициализирует объект PromoClient.

        Args:
            name (str): Имя клиента.
            promo_name (str): Название акции.
            promo_cl_id (int): Идентификатор клиента-участника.
        """
        self.promo_name = promo_name
        self.promo_cl_id = promo_cl_id
        PromoClient.promo_participants[promo_name] += 1
        self.promo_participants = {
            self.promo_name: PromoClient.promo_participants[promo_name]
        }
        super().__init__(
            f'{name} - участник {promo_name} #{self.promo_participants[promo_name]}')

    def get_promo_participants(self) -> dict:
        """
        Возвращает словарь с количеством участников для каждой акции.

        :return :
            dict: Словарь акции и количества участников.
        """
        return self.promo_participants

    def get_promo_num(self) -> int:
        """
        Возвращает количество участников для текущей акции.

        :return :
            int: Количество участников.
        """
        return self.promo_participants[self.promo_name]

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
