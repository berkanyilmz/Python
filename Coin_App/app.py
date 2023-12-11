from PyQt6 import QtWidgets
import sys
from coin_app import Ui_MainWindow
from file_helper import FileHelper
from api import Api

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.coin_api = Api()
        self.coin_lists = self.coin_api.get_response()

        self.file_helper = FileHelper('coins.txt')
        self.row_index = 0
        self.row_count = 0

        self.load_table()
        self.ui.coin_add.clicked.connect(self.add_coin)
        self.ui.fresh_table.clicked.connect(self.refresh)

    def load_table(self):
        coins_info = self.file_helper.get_coins_info()

        for i in range(0, len(coins_info), 3):
            self.ui.coins_table.setItem(self.row_index, 0, QtWidgets.QTableWidgetItem(coins_info[i]))
            self.ui.coins_table.setItem(self.row_index, 1, QtWidgets.QTableWidgetItem(coins_info[i+1]))
            self.ui.coins_table.setItem(self.row_index, 2, QtWidgets.QTableWidgetItem(coins_info[i+2]))
            self.row_index += 1
            self.row_count += 1

    def add_coin(self):
        coin_symbol = self.ui.lineEdit.text()
        flag = self.coin_is_exists(coin_symbol)

        if (flag == False):
            self.ui.find_info.setText("Coin Not Founded !")
            self.ui.find_info.setStyleSheet("color : red;")
        else:
            self.ui.lineEdit.setText("")
            coin_name, coin_price = self.coin_infos(coin_symbol)
            self.ui.coins_table.setItem(self.row_index, 0, QtWidgets.QTableWidgetItem(coin_name))
            self.ui.coins_table.setItem(self.row_index, 1, QtWidgets.QTableWidgetItem(coin_symbol))
            self.ui.coins_table.setItem(self.row_index, 2, QtWidgets.QTableWidgetItem(str(coin_price)))
            self.row_index += 1
            self.ui.find_info.setText("Coin Added")
            self.file_helper.write(coin_name, coin_symbol, coin_price)

    def coin_is_exists(self, coin_symbol):
        coin_symbol = coin_symbol.upper()
        for i in range(500):
            if (self.coin_lists['data'][i]['symbol'] == coin_symbol):
                return True
        return False

    def coin_infos(self, coin_symbol):
        for i in range(500):
            if (self.coin_lists['data'][i]['symbol'] == coin_symbol):
                coin_name = self.coin_lists['data'][i]['name']
                coin_price = self.coin_lists['data'][i]['quote']['USD']['price']
                return (coin_name, coin_price)

    def refresh(self):
        self.coin_lists = self.coin_api.get_response()
        for row in range(self.row_count):
            coin_symbol = self.ui.coins_table.item(row, 1).text()
            _, coin_price = self.coin_infos(coin_symbol)
            self.ui.coins_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(coin_price)))




application = QtWidgets.QApplication(sys.argv)
win = App()
win.show()
sys.exit(application.exec())

