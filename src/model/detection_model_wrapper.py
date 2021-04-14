"""Contains code for abstractions used to simplify interaction with the model"""

import os
import tensorflow as tf
import numpy as np

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

        #print("Using model: " + self.__model)
        image = tf.keras.preprocessing.image.load_img(image_location)

        image = tf.keras.preprocessing.image.load_img(image_location)
        image = image.resize((224,224))
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image / 255.0

        image_array = image.reshape(-1, 224, 224,3)
        
        class_label = self.__model.predict(image_array, batch_size=15, steps=None)
        class_label = np.argmax(class_label, axis = 1)
        
        return class_label
