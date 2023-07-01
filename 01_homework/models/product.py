# Главный класса Продукт


class Product:
    current_product_id = 0

    # Инициализация
    def __init__(self,
                 category: str = 'Не указана',
                 price: int = 0,
                 quantity: int = 0,
                 name: str = '-----'
                 ) -> None:
        self.category = category
        self.name = name
        self.price = price
        self.quantity = quantity

    # Переопределение __str__
    def __str__(self) -> str:
        return f'Категория: {self.category}\n'

    # Получаем кол-во
    @property
    def get_quantity(self) -> int:
        return self.quantity

    # Получаем цену
    @property
    def get_price(self) -> int:
        return self.price
