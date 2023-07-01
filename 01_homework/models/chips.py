from models.product import Product


# Дочерний класс Чипсы класса Продукт
class Chips(Product):
    category: str = 'Чипсы'

    # Конструктор класса
    def __init__(self, name: str,
                 price: int,
                 quantity: int,
                 maker: str) -> None:
        super().__init__(category=self.category,
                         name=name,
                         price=price,
                         quantity=quantity)
        self.maker = maker

    # Переопределение __str__
    def __str__(self):
        return super().__str__() + \
               f'Название: {self.name}\n' \
               f'Количество: {self.quantity}\n' \
               f'Цена: {self.price}\n' \
               f'Производитель: {self.maker}\n'
