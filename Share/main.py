import sys
from App import App
from PyQt6 import QtWidgets


application = QtWidgets.QApplication(sys.argv)
win = App()
win.show()
application.exec()
sys.exit(win.close_app())