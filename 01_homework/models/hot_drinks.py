from models.product import Product


# Дочерний класс ГорячиеНапитки класса Продукт
class HotDrinks(Product):
    category: str = 'Горячие напитки'

    # Конструктор класса
    def __init__(self,
                 name: str,
                 price: int,
                 volume: float,
                 temperature: int
                 ) -> None:
        super().__init__(category=self.category,
                         name=name,
                         price=price)
        self.temperature = temperature
        self.volume = volume

    # Переопределение __str__
    def __str__(self):
        return super().__str__() + \
               f'Название: {self.name}\n' \
               f'Количество: {self.quantity}\n' \
               f'Цена: {self.price}\n' \
               f'Объем: {self.volume}\n' \
               f'Температура: {self.temperature}\n'
