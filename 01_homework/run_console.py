from models.chips import Chips
from models.chocolate import Chocolate
from models.cockie import Cookie
from models.drinks import Drinks
from models.hot_drinks import HotDrinks
from services.vending_machine import VendingMachine

'''
Консольный вариант
Создаем объект Автомата и получаем массив Ячеек
Создаем список товаров
Укладываем их в различные ячейки
Вносим деньги
Покупаем товар
Выводим результат заполнения
'''
vm = VendingMachine()
all_places = vm.places.get_all_places()

products = [
    Cookie(name='Утреннее', quantity=10, price=1, maker='Любятово'),
    Chips(name='Сметана и лук', quantity=9, price=2, maker='Lays'),
    Chocolate(name='Milky way', quantity=8, price=3, maker='Mars'),
    Drinks(name='Кола', quantity=7, price=4, maker='Pepsi', volume=1.0),
    HotDrinks(name='Латте', price=5, volume=0.3, temperature=50),
    Cookie(name='Вечернее', quantity=10, price=1, maker='Добрыня'),
    Chips(name='Барбекю', quantity=9, price=2, maker='Pringles'),
    Chocolate(name='Сникерс', quantity=8, price=3, maker='Snickers'),
    Drinks(name='Фанта', quantity=7, price=4, maker='Coca Cola', volume=0.5),
    HotDrinks(name='Капучино', price=5, volume=0.5, temperature=55),
    Cookie(name='Дневное', quantity=10, price=1, maker='Большевик'),
    Chips(name='Краб', quantity=9, price=2, maker='Pringles'),
    Chocolate(name='Аленка', quantity=8, price=3, maker='Октябрь'),
    Drinks(name='Вода', quantity=7, price=4, maker='Аква', volume=0.7),
    HotDrinks(name='Раф', price=5, volume=0.6, temperature=45),
]

# заполняем ячейки подряд имеющимися продуктами из списка
product_index = 0
for row in all_places:
    for place in row:
        if product_index >= len(products):
            break

        place.add_product(products[product_index])
        product_index += 1

# получаем, что лежит в ячейке 00
print(vm.places.get_place(0, 0))
print('-----')

# вносим деньги
vm.payments.insert_money(20)
print(f'Монет: {vm.payments.get_amount}')

# покупаем 1 продукт из ячейки
vm.menu.buy_product('00')

# получаем, что теперь лежит в ячейке
print(vm.places.get_place(0, 0))
print(f'Монет: {vm.payments.get_amount}')