import threading
from PyQt6 import QtWidgets
from Share import Share
from PyQt6.QtGui import QColor
from DBHelper import DBHelper
from shareapp import Ui_MainWindow
from Scraping import Scraping
from threading import Thread
import time

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.shares_list = []

        self.dbhelper = DBHelper('username', 'password', 'share')
        self.connection = self.dbhelper.getConnection()
        self.dbhelper.create(self.connection)

        self.request = Scraping()
        html = self.request.request()
        self.shares = self.request.getShares(html)
        self.row_index = 0

        self.load_table()

        self.is_thread_running = True
        self.stop_event = threading.Event()
        self.stop_event.set()
        self.thread = Thread(target=self.fresh_table, args=(self.stop_event,))
        self.thread.start()

        #asyncio.run(self.fresh_table())

        self.ui.addButton.clicked.connect(self.add_share)



    def get_share_infos(self, share_name):
        for item in self.shares:
            if share_name == item.find('b').text:
                share_cost = item.find('td', {'id' : 'h_td_fiyat_id_{}'.format(share_name)}).text
                share_percent = item.find('td', {'id' : 'h_td_yuzde_id_{}'.format(share_name)}).text
                return (share_cost, share_percent)


    def load_table(self):
        results = self.dbhelper.query(self.connection)
        for result in results:
            self.shares_list.append(Share(result[0], result[1], result[2]))
            (share_cost, share_percent) = self.get_share_infos(result[0])

            self.ui.tableWidget.setItem(self.row_index, 0, QtWidgets.QTableWidgetItem(result[0]))
            self.ui.tableWidget.setItem(self.row_index, 1, QtWidgets.QTableWidgetItem(str(share_cost)))
            self.ui.tableWidget.setItem(self.row_index, 2, QtWidgets.QTableWidgetItem(str(share_percent)))
            self.ui.tableWidget.setItem(self.row_index, 3, QtWidgets.QTableWidgetItem(str(self.shares_list[self.row_index].share_quantity)))
            self.ui.tableWidget.setItem(self.row_index, 4, QtWidgets.QTableWidgetItem(str(self.shares_list[self.row_index].average)))
            self.row_index += 1

    def fresh_table(self, event):
        while self.stop_event.is_set():
            #print("fresh table")
            html = self.request.request()
            #self.shares = self.request.getShares(html)
            for row in range(self.row_index):
                #share_name = self.ui.tableWidget.item(row, 0).text()
                share_name = self.shares_list[row].share_code
                share_cost, share_percent = self.get_share_infos(share_name)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(share_name))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(share_cost)))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(share_percent)))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.shares_list[row].share_quantity)))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.shares_list[row].average)))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(self.pl(share_name, share_cost))))
            time.sleep(1)
            self.color_table()


    def color_table(self):
        for row in range(self.row_index):
            self.ui.tableWidget.item(row,2).setBackground(QColor(255,0,0)) if float(self.ui.tableWidget.item(row, 2).text().replace(',', '.')) < 0 else self.ui.tableWidget.item(row,2).setBackground(QColor(0,255,0))
            self.ui.tableWidget.item(row,5).setBackground(QColor(255,0,0)) if float(self.ui.tableWidget.item(row, 5).text()) < 0 else self.ui.tableWidget.item(row,5).setBackground(QColor(0,255,0))
    def find_share(self, share_code):
        for item in self.shares:
            if share_code == item.find('b').text:
                return True
        return False

    def pl(self, share_code, share_cost):
        avg, quantity = next(((s.average, s.share_quantity) for s in self.shares_list if share_code == s.share_code), (0, 0))
        share_cost = share_cost.replace(',', '.')
        p_l = (float(share_cost) * float(quantity)) - (float(avg) * float(quantity))
        return p_l

    def add_share(self):
        #self.is_thread_running = False
        self.stop_event.clear()
        self.thread.join()
        share_code = self.ui.share_name_text.text()
        if share_code == '':
            self.ui.share_name_info.setText('This field must be filled.')
            self.ui.share_name_info.setStyleSheet("color : red;")

        elif self.find_share(share_code) is False:
            self.ui.share_name_info.setText('This share is not found.')
            self.ui.share_name_info.setStyleSheet("color : red;")

        elif self.ui.quantity_text.text() == '':
            self.ui.quantity_info.setText('This field must be filled.')
            self.ui.quantity_info.setStyleSheet("color : red;")

        elif float(self.ui.cost_text.text()) < 0:
            self.ui.cost_info.setText('This field must be filled.')
            self.ui.cost_info.setStyleSheet("color : red;")

        else:
            self.average(share_code)
            self.ui.share_name_text.setText('')
            self.ui.quantity_text.setText('')
            self.ui.cost_text.setText('')

        self.stop_event.set()
        self.thread = Thread(target=self.fresh_table, args=(self.stop_event,))
        self.thread.start()

    def is_exist(self, share_code):
        return any(share_code == code.share_code for code in self.shares_list)

    def average(self, share_code):
        #self.is_thread_running = False
        #self.thread.join()
        if self.is_exist(share_code):
            avg, quantity = next(((s.average, s.share_quantity) for s in self.shares_list if share_code == s.share_code), (0, 0))
            old_cost = avg * quantity
            new_cost = float(self.ui.cost_text.text()) * float(self.ui.quantity_text.text())
            new_quantity = quantity + int(self.ui.quantity_text.text())
            new_avg = (old_cost + new_cost) / new_quantity
            #next((s.update(new_avg, new_quantity) for s in self.shares_list if share_code == s.share_code), None)
            for s in self.shares_list:
                if share_code == s.share_code:
                    s.share_quantity = new_quantity
                    s.average = new_avg
                    break
            self.dbhelper.update(self.connection, share_code, new_quantity, new_avg)

        else:
            self.shares_list.append(Share(share_code, self.ui.quantity_text.text(), self.ui.cost_text.text()))
            self.dbhelper.insert(self.connection, share_code, self.ui.quantity_text.text(), self.ui.cost_text.text())
            self.row_index += 1


    def close_app(self):
        self.stop_event.clear()
        time.sleep(1)
        self.connection.close()
