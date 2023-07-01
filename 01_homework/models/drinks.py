from models.product import Product


# Дочерний класс Напитки класса Продукт
class Drinks(Product):
    category: str = 'Напитки'

    # Конструктор класса
    def __init__(self,
                 name: str,
                 price: int,
                 quantity: int,
                 maker: str,
                 volume: float = 0.5
                 ):
        super().__init__(Drinks.category,
                         name=name,
                         price=price,
                         quantity=quantity)
        self.maker = maker
        self.volume = volume

    # Переопределение __str__
    def __str__(self):
        return super().__str__() + \
               f'Название: {self.name}\n' \
               f'Количество: {self.quantity}\n' \
               f'Объем: {self.volume}\n' \
               f'Цена: {self.price}\n' \
               f'Производитель: {self.maker}\n'
