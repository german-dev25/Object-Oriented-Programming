import logging
from typing import List
from classes.buyer import Buyer
from classes.promotional_client import PromoClient
from interfaces.i_market_behaviour import IMarketBehaviour
from interfaces.i_queue_behaviour import IQueueBehaviour


class Market(IMarketBehaviour, IQueueBehaviour):
    """ Класс, представляющий магазин.

    :attr :
        queue (List[Buyer]): Очередь покупателей.

    Methods:
        accept_to_market(buyer: Buyer) -> None:
            Принимает покупателя в магазин.
        take_in_queue(buyer: Buyer) -> None:
            Принимает покупателя в очередь.
        release_from_market(buyers: List[Buyer]) -> None:
            Освобождает покупателей из магазина.
        give_order() -> None:
            Выполняет выдачу заказов покупателям.
        release_from_queue() -> None:
            Освобождает покупателей из очереди.
        take_order() -> None:
            Обрабатывает заказы покупателей.
        update() -> None:
            Обновляет состояние магазина.
        handle_promo(promo_buyer: Buyer) -> None:
            Обрабатывает заказы для клиентов в акции.
    """

    def __init__(self):
        """ Инициализирует объект Market.
        """
        self.queue: List[Buyer] = []
        self.log = []  # Лог работы магазина

        # Настройка логирования
        self.logger = logging.getLogger('market_logger')
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('market.log')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def accept_to_market(self, buyer: Buyer) -> None:
        """ Принимает покупателя на магазин.

        :arg :
            buyer (Buyer): Покупатель.

        :return :
            None
        """
        self.logger.info(
            f'{buyer.get_buyer().get_name()} клиент пришел в магазин')
        self.take_in_queue(buyer=buyer)

    def take_in_queue(self, buyer: Buyer) -> None:
        """
        Принимает покупателя в очередь.

        :arg :
            buyer (Buyer): Покупатель.

        :return :
            None
        """
        self.queue.append(buyer)
        self.logger.info(
            f'{buyer.get_buyer().get_name()} клиент добавлен в очередь')

    def release_from_market(self, buyers: List[Buyer]) -> None:
        """
        Освобождает покупателей из магазина.

        :arg :
            buyers (List[Buyer]): Список покупателей.

        :return :
            None
        """
        for buyer in buyers:
            self.logger.info(
                f'{buyer.get_buyer().get_name()} клиент ушел из магазина')
            self.queue.remove(buyer)

    def give_order(self) -> None:
        """
        Выполняет выдачу заказов/возврат покупателям.

        :return :
            None
        """
        for buyer in self.queue:
            if buyer.is_make_order:
                buyer.set_take_order(take_order=True)
                self.logger.info(
                    f'{buyer.get_buyer().get_name()} клиент получил свой заказ')
            elif buyer.is_make_return:
                buyer.get_buyer().set_have_returned(is_have_returned=True)
                self.logger.info(
                    f'{buyer.get_buyer().get_name()} клиент получил возврат')

    def release_from_queue(self) -> None:
        """ Освобождает покупателей из очереди.

        :return :
            None
        """
        release_buyers = []
        for buyer in self.queue:
            if buyer.get_buyer().is_take_order or buyer.get_buyer().is_have_returned:
                release_buyers.append(buyer.get_buyer())
                self.logger.info(
                    f'{buyer.get_buyer().get_name()} клиент ушел из очереди')
        self.release_from_market(release_buyers)

    def take_order(self) -> None:
        """ Обрабатывает заказы покупателей (в том числе возврат).

        :return :
            None
        """
        for buyer in self.queue:
            if isinstance(buyer, PromoClient):
                self.handle_promo(buyer)
            elif buyer.get_buyer().is_make_return:
                self.logger.info(
                    f'{buyer.get_buyer().get_name()} клиент оформил возврат')
            else:
                buyer.set_make_order(True)
                self.logger.info(
                    f'{buyer.get_buyer().get_name()} клиент сделал заказ')

    def update(self) -> None:
        """ Обновляет состояние магазина.

        :return :
            None
        """
        self.take_order()
        self.give_order()
        self.release_from_queue()

    def handle_promo(self, promo_buyer: Buyer) -> None:
        """ Обрабатывает заказы для клиентов в акции.

        :arg :
            promo_buyer (Buyer): Покупатель в акции.

        :return :
            None
        """
        if promo_buyer.get_buyer().get_promo_num() <= 2:
            promo_buyer.set_make_order(True)
            self.logger.info(f'{promo_buyer.get_buyer().get_name()} '
                             f'клиент сделал заказ в рамках акции')
        else:
            promo_buyer.set_take_order(True)
            self.logger.info(f'{promo_buyer.get_buyer().get_name()} '
                             f'не может сделать заказ в рамках акции')
