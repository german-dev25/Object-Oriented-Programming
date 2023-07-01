from PyQt5 import QtCore, QtGui, QtWidgets

from models.chips import Chips
from models.chocolate import Chocolate
from models.cockie import Cookie
from models.config import BG_IMG, TITLE, BG_COL
from services.vending_machine import VendingMachine


# отрисовка интерфейса с помощью QT Designer
# функционал вручную настраивал
class Ui_MainWindow(object):
    def __init__(self):
        self.vm = VendingMachine()
        self.places_labels = {}
        self.categories = self.vm.get_categories()

    def setupUi(self, MainWindow):
        # Настройки окна и фона
        MainWindow.setFixedSize(1000, 900)
        MainWindow.setStyleSheet(BG_IMG)

        # Создаем центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # заголовок вверху
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 900, 50))
        self.title.setText(TITLE)

        # создаем label для каждого place
        for row in range(self.vm.places.rows):
            for col in range(self.vm.places.cols):
                key = f'{row}{col}'
                label = QtWidgets.QLabel(self.centralwidget)
                label.setGeometry(
                    QtCore.QRect(275 + col * 80, 120 + row * 105, 60, 60))
                label.setText(
                    f'<html><head/><body><p align=\'center\'>'
                    f'<span style=\' font-size:12pt; font-weight:600;\'>'
                    f'{key}'
                    f'</span><br/></p></body></html>')
                self.places_labels[key] = label

        # Виджет покупки товара
        self.product_choice = QtWidgets.QWidget(self.centralwidget)
        self.product_choice.setGeometry(QtCore.QRect(40, 210, 121, 131))
        self.product_choice.setStyleSheet(BG_COL)

        # Заголовок виджета
        self.product_title = QtWidgets.QLabel(self.centralwidget)
        self.product_title.setGeometry(QtCore.QRect(40, 190, 121, 16))
        self.product_title.setText(
            '<html><head/><body><p align=\'center\'>'
            'Ввод номера'
            '</p></body></html>'
        )

        # Поле выбора номера продукта
        self.product_place_choice = QtWidgets.QComboBox(self.product_choice)
        self.product_place_choice.setGeometry(QtCore.QRect(20, 10, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.product_place_choice.setFont(font)
        self.product_place_choice.setEditable(True)

        for row in range(self.vm.places.rows):
            for col in range(self.vm.places.cols):
                place_num = f"{row}{col}"
                self.product_place_choice.addItem(place_num)

        self.product_place_choice.setCurrentText('00')
        self.product_place_choice.setStyleSheet(BG_COL)

        # Покупаем
        self.buy_product = QtWidgets.QPushButton(self.product_choice)
        self.buy_product.setGeometry(QtCore.QRect(20, 80, 81, 32))
        self.buy_product.setText('Купить')
        self.buy_product.setStyleSheet(BG_COL)

        # Виджет зоны добавления продуктов
        self.add_product = QtWidgets.QWidget(self.centralwidget)
        self.add_product.setGeometry(QtCore.QRect(790, 80, 151, 321))

        # Текст сверху
        self.plus_product = QtWidgets.QLabel(self.centralwidget)
        self.plus_product.setGeometry(QtCore.QRect(800, 60, 131, 21))
        self.plus_product.setText(
            '<html><head/><body><p align=\'center\'>'
            'Добавить продукты'
            '</p></body></html>')

        # Список категорий
        self.product_list = QtWidgets.QListWidget(self.add_product)
        self.product_list.setGeometry(QtCore.QRect(10, 10, 131, 81))
        self.product_list.setStyleSheet(BG_COL)

        # заполняем Список категорий
        for category in self.categories:
            item = QtWidgets.QListWidgetItem()
            self.product_list.addItem(item)
            item.setText(category)

        # Устанавливаем на 0й элемент курсор
        self.product_list.setCurrentRow(0)

        # Цена лейбл
        self.product_price_label = QtWidgets.QLabel(self.add_product)
        self.product_price_label.setGeometry(QtCore.QRect(10, 100, 60, 16))
        self.product_price_label.setText('Цена')

        # Цена переключатель
        self.product_price_num = QtWidgets.QSpinBox(self.add_product)
        self.product_price_num.setGeometry(QtCore.QRect(80, 100, 61, 20))

        # Кол-во лейбл
        self.product_quantity_label = QtWidgets.QLabel(self.add_product)
        self.product_quantity_label.setGeometry(QtCore.QRect(10, 130, 60, 16))
        self.product_quantity_label.setText('Кол-во')

        # Кол-во переключатель
        self.product_quantity_num = QtWidgets.QSpinBox(self.add_product)
        self.product_quantity_num.setGeometry(QtCore.QRect(80, 130, 61, 20))

        # Название добавляемого продукта
        self.product_name = QtWidgets.QLineEdit(self.add_product)
        self.product_name.setGeometry(QtCore.QRect(10, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.product_name.setFont(font)
        self.product_name.setStyleSheet(BG_COL)
        self.product_name.setAlignment(QtCore.Qt.AlignCenter)
        self.product_name.setText('Название')

        # Производитель добавляемого продукта
        self.product_maker = QtWidgets.QLineEdit(self.add_product)
        self.product_maker.setGeometry(QtCore.QRect(10, 190, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.product_maker.setFont(font)
        self.product_maker.setStyleSheet(BG_COL)
        self.product_maker.setAlignment(QtCore.Qt.AlignCenter)
        self.product_maker.setText('Производитель')

        # Поле ввода номера ячейки для добавления продукта
        self.product_set_place = QtWidgets.QComboBox(self.add_product)
        self.product_set_place.setGeometry(QtCore.QRect(30, 220, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.product_set_place.setFont(font)
        self.product_set_place.setStyleSheet(BG_COL)
        self.product_set_place.setEditable(True)

        for row in range(self.vm.places.rows):
            for col in range(self.vm.places.cols):
                place_num = f"{row}{col}"
                self.product_set_place.addItem(place_num)

        self.product_set_place.setCurrentText('Место №')

        # Кнопка Добавить продукт в ячейку
        self.product_add_buttom = QtWidgets.QPushButton(self.add_product)
        self.product_add_buttom.setGeometry(QtCore.QRect(30, 250, 91, 32))
        self.product_add_buttom.setStyleSheet(BG_COL)
        self.product_add_buttom.setText('Добавить')

        # Вывод результата
        # self.product_add_result = QtWidgets.QLabel(self.add_product)
        # self.product_add_result.setGeometry(QtCore.QRect(10, 290, 131, 21))

        # Блок приема монет
        self.payments = QtWidgets.QWidget(self.centralwidget)
        self.payments.setGeometry(QtCore.QRect(600, 510, 111, 131))
        self.payments.setStyleSheet(BG_COL)

        # блок приема монет (+5 монет)
        self.add_coins_5 = QtWidgets.QPushButton(self.payments)
        self.add_coins_5.setGeometry(QtCore.QRect(20, 70, 70, 20))
        self.add_coins_5.setText('+5 монет')

        # блок приема монет (+10 монет)
        self.add_coins_10 = QtWidgets.QPushButton(self.payments)
        self.add_coins_10.setGeometry(QtCore.QRect(20, 40, 70, 20))
        self.add_coins_10.setText('+10 монет')

        # блок приема монет (сумма монет)
        self.amount_paid = QtWidgets.QLabel(self.payments)
        self.amount_paid.setGeometry(QtCore.QRect(0, 10, 110, 20))
        self.amount_paid.setText(
            f'<html><head/><body><p align=\'center\'>'
            f'{self.vm.payments}'
            f'</p></body></html>')

        # блок приема монет (сброс монет)
        self.add_coins_reset = QtWidgets.QPushButton(self.payments)
        self.add_coins_reset.setGeometry(QtCore.QRect(20, 100, 70, 20))
        self.add_coins_reset.setText('Сброс')

        # что-то =)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # Подключаем функции кнопок
        self.btn_func()

    # функции для монетоприемника
    def insert_coin(self, amount):
        self.vm.payments.insert_money(amount)
        self.update_amount_paid_label()

    def reset_coins(self):
        self.vm.payments.amount_reset()
        self.update_amount_paid_label()

    def update_amount_paid_label(self):
        self.amount_paid.setText(
            f'<html><head/><body><p align=\'center\'>Монет: {self.vm.payments.amount_paid}</p></body></html>')

    # функции для добавления продуктов
    def add_product_func(self):
        category_item = self.product_list.currentItem()
        category = category_item.text()
        name = self.product_name.text()
        quantity = self.product_quantity_num.value()
        price = self.product_price_num.value()
        maker = self.product_maker.text()
        place_num = self.product_set_place.currentText()

        if category == 'Печенье':
            self.vm.products = self.vm.cookie(name, price, quantity, maker)
        elif category == 'Чипсы':
            self.vm.products = self.vm.chips(name, price, quantity, maker)
        elif category == 'Шоколад':
            self.vm.products = self.vm.chocolate(name, price, quantity, maker)
        elif category == 'Напитки':
            self.vm.products = self.vm.drinks(name, price, quantity, maker)

        place = self.vm.places.get_place(int(place_num[0]), int(place_num[1]))
        place.add_product(self.vm.products)
        self.update_label_text(place)

    # функция для обновления данных ячеек
    def update_label_text(self, place):
        place_key = f'{place.row}{place.col}'
        label = self.places_labels.get(place_key)

        if label is not None:
            text_parts = str(place).split('\n')
            label.setText(
                f'<html><head/><body><p align=\'center\'>'
                f'<span style=\' font-size:10pt; font-weight:600;\'>'
                f'{text_parts[0]}<br/>'
                f'{text_parts[1]}<br/>'
                f'{text_parts[2]}<br/>'
                f'{text_parts[3]}</span>'
                f'</p></body></html>')

    # покупка
    def buy_product_func(self):
        place_num = self.product_place_choice.currentText()
        self.vm.menu.buy_product(place_num)
        place = self.vm.places.get_place(int(place_num[0]), int(place_num[1]))
        self.update_label_text(place)
        self.update_amount_paid_label()

    # связываем клик кнопки с функциями
    def btn_func(self):
        self.buy_product.clicked.connect(
            lambda: self.buy_product_func()
        )
        self.product_add_buttom.clicked.connect(
            lambda: self.add_product_func()
        )
        self.add_coins_5.clicked.connect(lambda: self.insert_coin(5))
        self.add_coins_10.clicked.connect(lambda: self.insert_coin(10))
        self.add_coins_reset.clicked.connect(self.reset_coins)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
