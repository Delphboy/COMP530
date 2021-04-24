"""Module to hold the GUI functionality"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5 import QtWidgets, uic

class InterfaceWrapper(QtWidgets.QMainWindow):
    """Provides a wrapper for the UI"""
    def __init__(self):
        super(InterfaceWrapper, self).__init__()
        uic.loadUi('src/gui/ui.ui', self)

        # Plumb UI events
        self.btnTrainModel.clicked.connect(self.train_model)
        self.btnSelectDataset.clicked.connect(self.select_dataset)
        self.btnRunModel.clicked.connect(self.run_model)
        self.btnSelectData.clicked.connect(self.select_data)

    def show_ui(self):
        """Show the UI"""
        self.show()

    def run_model(self):
        """Run a model on the selected data"""
        print("I am going to run a model")

    def select_data(self):
        """Selected data to be evaluated by a trained model"""
        print("I am going to open a popup box file dialogue")

    def train_model(self):
        """Use selected dataset to train a model"""
        print("I am going to train a model")

    def select_dataset(self):
        """Selected dataset to be train a model"""
        print("I am going to open a popup box file dialogue")


def show_gui():
    app = QtWidgets.QApplication(sys.argv)
    user_interface = InterfaceWrapper()
    user_interface.show()
    app.exec_()
