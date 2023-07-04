from classes.buyer import Buyer
from interfaces.i_buyer_behaviour import IBuyerBehaviour
from mixins.buyer_mixins import BuyerMixin


class PromoClient(BuyerMixin, Buyer, IBuyerBehaviour):
    """
       Класс PromoClient представляет клиента-участника акции.

       Attributes:
           promo_participants (dict): Словарь, содержащий количество
           участников для каждой акции.
           promo_name (str): Название акции.
           promo_cl_id (int): Идентификатор клиента-участника.

       Methods:
           get_promo_participants(self) -> dict:
               Возвращает словарь с количеством участников для каждой акции.
           get_promo_num(self) -> int:
               Возвращает количество участников для текущей акции.
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
