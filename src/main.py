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
        action="store",
        nargs=2,
        metavar=("model_location", "detect_src")
    )
    parser.add_argument("-t", "--train",
        help="Takes a training dataset and trains a model",
        nargs=2,
        metavar=("dataset_location", "train_ratio")
    )
    parser.add_argument("-g", "--gui",
        help="Run a graphical user interface",
        action="store_true"
    )

    args = parser.parse_args()

    if args.detect is not None:
        print("Detecting biofuels in " + args.detect[1] + " using model " + args.detect[0])
        detect.detect(args.detect[1], args.detect[0])
    elif args.train is not None:
        print("Training model based on dataset: " + args.train[0])
        if os.path.exists(args.train[0]) and float(args.train[1]) < 1:
            train.pipeline_inception_v3(args.train[0], float(args.train[1]))
        else:
            print("Ensure the path: " + args.train + " exists and that train ratio < 1")
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
