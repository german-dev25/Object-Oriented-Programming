from models.chips import Chips
from models.chocolate import Chocolate
from models.cockie import Cookie
from models.drinks import Drinks
from models.places import Places
from models.product import Product
from services.menu import Menu
from services.payments import Payments


# класс Автомат
# Инициализация с созданием всех частей объекта
# ячеек, меню, монетоприемника
class VendingMachine:
    def __init__(self):
        self.places = Places()
        self.payments = Payments()
        self.menu = Menu(self.places, self.payments)
        self.products = Product
        self.cookie = Cookie
        self.drinks = Drinks
        self.chocolate = Chocolate
        self.chips = Chips

    def get_categories(self):
        return [self.chips.category,
                self.drinks.category,
                self.chocolate.category,
                self.chips.category]