"""Entry point for the console application"""
import argparse
import os
import sys

from gui import gui


from console import console




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
        console.detect(args.detect)
    elif args.train is not None:
        print("Training model based on dataset: " + args.train)
    elif args.test is not None:
        print("Testing model based on dataset: " + args.test)
    elif args.gui is True:
        # print("Start the GUI once it has been developed")
        # app = QApplication(sys.argv)
        # window = QWidget()
        # message_label = QLabel(window)
        # message_label.setText("Hello World!")
        # window.setGeometry(100,100,200,50)
        # message_label.move(50,20)
        # window.setWindowTitle("PyQt5")
        # window.show()
        # sys.exit(app.exec_())
        
        gui.show_gui()










if __name__ == "__main__":
    main()
