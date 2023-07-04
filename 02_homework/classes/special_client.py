from classes.buyer import Buyer
from interfaces.i_buyer_behaviour import IBuyerBehaviour
from mixins.buyer_mixins import BuyerMixin


class SpecialClient(BuyerMixin, Buyer, IBuyerBehaviour):
    """
    Класс, представляющий особого клиента.

    Attributes:
        name (str): Имя клиента.
        vip_id (int): Идентификатор VIP-клиента.
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
