import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtWidgets, uic

class InterfaceWrapper(QtWidgets.QMainWindow):
    """Provides a wrapper for the UI"""
    def __init__(self):
        super(InterfaceWrapper, self).__init__()
        uic.loadUi('C:\\Users\\HPS19\\Desktop\\comp530-ui.ui', self)
        self.show()


def show_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = InterfaceWrapper()
    app.exec_()