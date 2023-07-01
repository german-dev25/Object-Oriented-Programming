from PyQt5 import QtWidgets

from gui.gui import Ui_MainWindow

# инициализируем GUI интерфейс для VendingMachine
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
