"""Entry point for the console application"""
import argparse
import os

from gui import gui
from model import detect, train

def main():
    setup_file_system()
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
        detect.detect(args.detect)
    elif args.train is not None:
        print("Training model based on dataset: " + args.train)
        if os.path.exists(args.train):
            train.pipeline_inception_v3(args.train)
        else:
            print("The path: " + args.train + " does not exist")
    elif args.gui is True:
        gui.show_gui()


def setup_file_system():
    """Ensure the models and .playground folders exist to prevent crash on startup"""
    if not os.path.exists(os.path.join(os.getcwd(), "models")):
        os.makedirs(os.path.join(os.getcwd(), "models"))

    if not os.path.exists(os.path.join(os.getcwd(), ".playground")):
        os.makedirs(os.path.join(os.getcwd(), ".playground"))


if __name__ == "__main__":
    main()
