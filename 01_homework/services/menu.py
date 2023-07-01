from models.places import Places
from services.payments import Payments

# класс Меню для получения/создания меню и покупки товара
class Menu:
    def __init__(self,
                 places: Places,
                 payments: Payments) -> None:
        # создаем словарь {кнопка: место (+ купить)}
        self.buttons: dict = self.create_menu(places)
        self.payments: Payments = payments
        self.order_quantity: int = 1
        self.menu = self.create_menu

    # создаем словарь меню для каждой ячейки + покупка
    def create_menu(self, places: Places) -> dict:
        menu = {}
        all_places = places.get_all_places()
        for row in all_places:
            for place in row:
                button_label = f'{place.row}{place.col}'
                menu[button_label] = place
        menu['buy_product'] = self.buy_product
        return menu

    # вывод меню
    def get_menu(self) -> dict:
        return self.buttons

    # покупка продукта, с проверкой введен ли номер и есть ли продукт
    def buy_product(self, button: str = None) -> str:
        if button is not None:
            selected_place = self.buttons[button]
            if selected_place.is_empty:
                return 'Невозможно купить продукт: выбранное место пусто'
            if selected_place.product.get_price <= self.payments.amount_paid:
                selected_place.products_in_place -= 1
                self.payments.amount_reduce(selected_place.product.get_price)
        else:
            return 'Команда не выполнена'

    # переопределение __str__
    def __str__(self):
        return str(self.buttons)
