from classes.buyer import Buyer
from interfaces.i_buyer_behaviour import IBuyerBehaviour
from mixins.buyer_mixins import BuyerMixin


class PensionerClient(BuyerMixin, Buyer, IBuyerBehaviour):
    """
    Класс, представляющий клиента-пенсионера.

    Attributes:
        name (str): Имя клиента.
        pens_id (int): Идентификатор пенсионера.

    """

    def __init__(self, name: str, pens_id: int):
        """
        Инициализирует объект PensionerClient.

        :arg :
            name (str): Имя клиента.
            pens_id (int): Идентификатор пенсионера.
        """
        super().__init__(name + ' - пенсионер')
        self.pens_id = pens_id
