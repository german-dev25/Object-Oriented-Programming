from typing import Optional, List

from models.config import MAX_PLACE_CAPACITY, VENDING_ROW, VENDING_COL
from models.product import Product
import numpy as np


# класс Места(ячейки) в автомате
class Places:
    # инициализация класс + создание набора Ячеек
    def __init__(self,
                 rows: int = VENDING_ROW,
                 cols: int = VENDING_COL):
        self.rows: int = rows
        self.cols: int = cols
        self.places = self.create_places(rows, cols)

    # метод, создающий весь набор ячеек
    @staticmethod
    def create_places(rows: int, cols: int):
        places = np.empty((rows, cols), dtype=object)
        for row in range(rows):
            for col in range(cols):
                place = Place(row, col)
                places[row, col] = place
        return places

    # получаем набор ячеек
    def get_all_places(self):
        return self.places

    # получить одну ячейку
    def get_place(self, row: int, col: int):
        return self.places[row][col]

    # переопределение вывода набора ячеек
    def __str__(self) -> str:
        return '\n'.join(str(place)
                         for row in self.places
                         for place in row)


# класс одной ячейки (не наследник)
# ряд/ячейка, изначально без продукта
# вместительность MAX_PLACE_CAPACITY (15)
class Place:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col
        self.products_in_place: int = 0
        self.capacity: int = MAX_PLACE_CAPACITY
        self.product: Optional[Product] = None

    # свойство для получения номер формата '00' итд
    @property
    def place_num(self) -> str:
        return f'{self.row}{self.col}'

    # пустая ли ячейка
    @property
    def is_empty(self) -> bool:
        return self.products_in_place == 0

    # добавляем в ячейку продукт, пока есть место
    def add_product(self, product: Product) -> str:
        if self.product and not isinstance(product, type(self.product)):
            return f'Невозможно положить в ячейку продукт другой категории'
        self.product = product
        self.products_in_place += product.get_quantity
        self.products_in_place = min(self.products_in_place, self.capacity)
        return self.fullness()

    # заполненность ячейки
    def fullness(self) -> str:
        return f'{self.products_in_place}/{self.capacity}'

    def __str__(self):
        if self.is_empty:
            return f'Тут\n' \
                   f'{self.place_num}\n' \
                   f'пусто\n'
        else:
            return f'{self.place_num}\n' \
                   f'{self.fullness()}\n' \
                   f'{self.product.name}\n' \
                   f'{self.product.get_price} мон.'
