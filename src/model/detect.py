"""Contains code for abstractions used to simplify interaction with the model"""

import os
import tensorflow as tf
import numpy as np

SUPPORTED_FILES = ['png', 'jpg', 'jpeg']

class ModelWrapper:
    '''Provide a wrapper to the prediction model'''
    __model = None

    def __init__(self, model_location):
        super().__init__()
        loc = os.path.join(os.getcwd(), model_location)
        self.__model = tf.keras.models.load_model(loc, compile=True)

    def detect(self, image_location):
        """Detects the biofuel type in a given image
            Parameters: image
            Returns: prediction and confidence
        """
        image = tf.keras.preprocessing.image.load_img(image_location)

        image = tf.keras.preprocessing.image.load_img(image_location)
        image = image.resize((224,224))
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image / 255.0

        image_array = image.reshape(-1, 224, 224,3)

        class_label = self.__model.predict(image_array, batch_size=15, steps=None)
        class_label = np.argmax(class_label, axis = 1)

        return class_label


def detect(path, model_path = "models/inceptionV3-1.h5"):
    """Generate a prediction of the biofuel source in image contained in a directory

    Args:
        path: the directory of images or single image to be processed
        model_path: The absolute file path of the model weights file
    """
    if not os.path.exists(path):
        raise Exception("Please enter a valid file or directory path. Given:" + path)

    if os.path.isfile(path):
        prediction = get_prediction(path, model_path)
        print(prediction)
    else:
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            prediction = get_prediction(full_path, model_path)
            print(prediction)


def get_prediction(image_location, model_path):
    """Generate a prediction of the biofuel source in an image

    Args:
        image_location: The absolute file path of the image
        model_path: The absolute file path of the model weights file

    Returns:
        The class label of the biofuel detected
    """
    extension = os.path.splitext(image_location)[1]
    extension = extension.replace('.', '')
    if not extension in SUPPORTED_FILES:
        return extension + " is not a supported file type"

    model = ModelWrapper(model_path)
    return model.detect(image_location)
