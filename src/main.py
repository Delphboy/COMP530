"""Entry point for the console application"""
import argparse
import os
import sys

from model.detection_model_wrapper import ModelWrapper
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

SUPPORTED_FILES = ['png', 'jpg', 'jpeg']


def main():
    parser = argparse.ArgumentParser(
        description=
        """Train biofuel detection models, test biofuel detection models,
        and detect biofuel sources in images"""
    )
    parser.add_argument("-d", "--detect",
        help="Takes an image file and detects possible biofuel sources",
        action="store"
    )
    parser.add_argument("-t", "--train",
        help="Takes a training dataset and trains a model"
    )
    parser.add_argument("-T", "--test",
        help="Takes a test dataset and evaluates the model"
    )
    parser.add_argument("-g", "--gui",
        help="Run a graphical user interface",
        action="store_true"
    )

    args = parser.parse_args()

    if args.detect is not None:
        print("Detecting biofuels in " + args.detect)
        detect(args.detect)
    elif args.train is not None:
        print("Training model based on dataset: " + args.train)
    elif args.test is not None:
        print("Testing model based on dataset: " + args.test)
    elif args.gui is True:
        print("Start the GUI once it has been developed")
        app = QApplication(sys.argv)
        w = QWidget()
        b = QLabel(w)
        b.setText("Hello World!")
        w.setGeometry(100,100,200,50)
        b.move(50,20)
        w.setWindowTitle("PyQt5")
        w.show()
        sys.exit(app.exec_())


def detect(path):
    if not os.path.exists(path):
        raise Exception("Please enter a valid file or directory path")

    if os.path.isfile(path):
        prediction = get_prediction(path)
        print(prediction)
    else:
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            prediction = get_prediction(full_path)
            print(prediction)


def get_prediction(file_path):
    extension = os.path.splitext(file_path)[1]
    extension = extension.replace('.', '')
    if not extension in SUPPORTED_FILES:
        return extension + " is not a supported file type"

    model = ModelWrapper()
    return model.detect(file_path)


if __name__ == "__main__":
    main()
