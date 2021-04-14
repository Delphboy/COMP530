"""A module to handle command line operations to represent the console application"""

import os

from model.detection_model_wrapper import ModelWrapper

SUPPORTED_FILES = ['png', 'jpg', 'jpeg']

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


def get_prediction(image_location, model_path = "models/inceptionV3-1.h5"):
    extension = os.path.splitext(image_location)[1]
    extension = extension.replace('.', '')
    if not extension in SUPPORTED_FILES:
        return extension + " is not a supported file type"

    model = ModelWrapper(model_path)
    return model.detect(image_location)
