from classes.buyer import Buyer
from classes.ordinary_client import OrdinaryClient
from interfaces.i_buyer_behaviour import IBuyerBehaviour
from mixins.buyer_mixins import BuyerMixin


class TaxService(BuyerMixin, Buyer, IBuyerBehaviour):
    """
    Класс, представляющий службу.

    Attributes:
        name (str): Имя службы.

    Methods:
        get_buyer() -> Buyer:
            Возвращает экземпляр, представляющий службу для обычного клиента.
    """

    def __init__(self):
        """
        Инициализирует объект TaxService.
        """

        super().__init__(name="Tax audit")
        self.is_take_order: bool = False
        self.is_make_order: bool = False

    def get_buyer(self):
        """ Возвращает самого клиента. """
        return OrdinaryClient(self.name)
