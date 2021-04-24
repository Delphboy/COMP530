"""Module to hold the GUI functionality"""
import sys
import os
import json

from tkinter import Tk
from tkinter.filedialog import askdirectory
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from model import detect, train

class InterfaceWrapper(QtWidgets.QMainWindow):
    """Provides a wrapper for the PyQt UI"""

    def __init__(self):
        super().__init__()
        self.train_ratio = 50
        self.train_dataset_location = ""
        self.run_data_location = ""
        self.models = load_model_names()

        # Load UI File
        uic.loadUi('src/gui/ui.ui', self)

        # Populate Models
        self.cBoxSelectModel.addItems(self.models)

        # Plumb UI events
        self.btnTrainModel.clicked.connect(self.train_model)
        self.btnSelectDataset.clicked.connect(self.select_dataset)
        self.btnRunModel.clicked.connect(self.run_model)
        self.btnSelectData.clicked.connect(self.select_data)
        self.sliderTrainTestSplit.valueChanged.connect(self.slider_moved)
        self.cBoxSelectModel.currentTextChanged.connect(self.load_table_widget_data)


    def show_ui(self):
        """Show the UI"""
        self.show()


    def select_dataset(self):
        """Selected dataset to be train a model"""
        self.train_dataset_location = self.get_directory()
        self.lblDatasetLocation.setText(self.train_dataset_location)


    def slider_moved(self):
        """Update the train/test split based on slider"""
        self.train_ratio = self.sliderTrainTestSplit.value()
        self.lblTrainTestSplit.setText(
            "Train/Test Split - " + str(self.train_ratio) + ":" + str(100 - self.train_ratio))


    def train_model(self):
        """Use selected dataset to train a model"""
        self.btnRunModel.setEnabled(False)
        is_safe_to_train = True
        if self.train_dataset_location == "" or self.train_dataset_location is None:
            print("select a dataset")
            is_safe_to_train = False

        if is_safe_to_train:
            ratio = self.train_ratio / 100
            _, history = train.pipeline_inception_v3(self.train_dataset_location, ratio)
            # Refresh the model list
            self.models = self.load_model_names()
            self.populate_table_widget(history)
        self.btnRunModel.setEnabled(True)


    def select_data(self):
        """Selected data to be evaluated by a trained model"""
        self.run_data_location = self.get_directory()
        self.lblDataLocation.setText(self.run_data_location)


    def run_model(self):
        """Run a model on the selected data"""
        # Check: model file selected, data directory selected
        # Make call
        model_name = self.cBoxSelectModel.currentText()
        is_safe_to_run = True
        if len(self.models) < 1:
            print("no models loaded")
            is_safe_to_run = False

        if model_name == "" or model_name is None:
            print("Select a model")
            is_safe_to_run = False

        if self.run_data_location == "" or self.run_data_location is None:
            print("Select some data!")
            is_safe_to_run = False

        if is_safe_to_run:
            model_loc = os.path.join(os.getcwd(), "models", model_name)
            results = detect.detect(self.run_data_location, model_loc)
            self.display_detection_results(results)

    #Helper functions
    def load_table_widget_data(self):
        """Loads the training history of a model into the table view"""
        file_name = self.cBoxSelectModel.currentText().replace(".h5", "-history.json")
        if os.path.exists(os.path.join(os.getcwd(), "models", file_name)):
            data = json.load(open(os.path.join(os.getcwd(), "models", file_name), 'r'))
            self.populate_table_widget(data)


    def populate_table_widget(self, data):
        """Populates the table view with training history"""
        headers = []
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(4)
        for row, key in enumerate(sorted(data.keys())):
            headers.append(key)
            for column, item in enumerate(data[key]):
                self.tableWidget.setItem(column, row, QTableWidgetItem(str(item)))
        self.tableWidget.setHorizontalHeaderLabels(headers)


    def display_detection_results(self, results):
        """Displays the detection results in the table view"""
        files = [i[0] for i in results]
        predictions = [i[1] for i in results]
        self.tableWidget.setRowCount(len(predictions))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["File", "Prediction"])
        count = 0
        for item in files:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(item))
            count += 1
        count = 0
        for item in predictions:
            self.tableWidget.setItem(count, 1, QTableWidgetItem(item))
            count += 1


def show_gui():
    """Creates an instance of the UI and displays it"""
    app = QtWidgets.QApplication(sys.argv)
    user_interface = InterfaceWrapper()
    user_interface.show()
    app.exec_()


def load_model_names():
    """Load a list of models found in the models directory
        RETURNS: A list of .h5 files in the /models directory
    """
    location = os.path.join(os.getcwd(), "models")
    models = [file for file in os.listdir(location) if file.endswith(".h5")]
    return models


def get_directory():
    """Use the OS directory selection to get a directory
        RETURNS: directory selected by the user
    """
    root = Tk()
    root.withdraw()
    directory = askdirectory(initialdir=os.getcwd(), parent=root)
    root.destroy()
    return directory
