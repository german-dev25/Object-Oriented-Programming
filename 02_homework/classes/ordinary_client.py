from classes.buyer import Buyer
from interfaces.i_buyer_behaviour import IBuyerBehaviour
from mixins.buyer_mixins import BuyerMixin


class OrdinaryClient(BuyerMixin, Buyer, IBuyerBehaviour):
    """ Класс, представляющий обычного клиента.

    Attributes:
        name (str): Имя клиента.
    """

    def __init__(self, name: str):
        """ Инициализирует объект OrdinaryClient.

        :arg :
            name (str): Имя клиента.
        """
        super().__init__(name)
