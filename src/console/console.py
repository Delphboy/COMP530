"""A module to handle command line operations to represent the console application"""

import os
from model.detect import get_prediction


def detect(path):
    if not os.path.exists(path):
        raise Exception("Please enter a valid file or directory path. Given:" + path)

    if os.path.isfile(path):
        prediction = get_prediction(path)
        print(prediction)
    else:
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            prediction = get_prediction(full_path)
            print(prediction)
