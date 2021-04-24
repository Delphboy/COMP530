"""A collection of functions for training models"""
import os
import random
import datetime
import json

from shutil import copy2, rmtree
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.applications.inception_v3 import InceptionV3

IMAGE_SIZE = [224,224]

def pipeline_inception_v3(dataset_location, train_ratio=0.8):
    """Generates a InceptionV3 Model and returns the model and performance metrics"""
    train_test_data_randomiser(dataset_location, train_ratio)
    training_data_loc = ".playground/train"
    testing_data_loc = ".playground/test"
    data_generators = build_data_generators(training_data_loc, testing_data_loc)
    model = build_inception_v3_model()
    return train_inception_v3(data_generators[0], data_generators[1], model)


def build_inception_v3_model():
    class_label_count = 10

    inception = InceptionV3(input_shape=IMAGE_SIZE + [3],
                    weights= "imagenet",
                    include_top = False)

    for layer in inception.layers:
        layer.trainable = False

    flattened = Flatten()(inception.output)
    output_layer = Dense(class_label_count, activation='softmax')(flattened)
    model = Model(inputs = inception.input, outputs = output_layer)
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model


def train_inception_v3(train, test, model):
    training_history = model.fit(
        train,
        validation_data=test,
        epochs=9,
        steps_per_epoch=len(train),
        validation_steps=len(test)
    )
    now = str(datetime.datetime.now()).split(".")[0].replace(" ", "-").replace(":","-")
    model.save("models/inceptionV3-" + now + ".h5")
    json.dump(training_history.history, open("models/inceptionV3-" + now + "-history.json", 'w'))
    return (model, training_history.history)


def train_test_data_randomiser(dataset_location, train_ratio=0.8):
    rmtree(".playground")
    os.mkdir(".playground")
    os.mkdir(".playground/test")
    os.mkdir(".playground/train")
    os.mkdir(".playground/train/beetroot")
    os.mkdir(".playground/train/coconut")
    os.mkdir(".playground/train/corn")
    os.mkdir(".playground/train/palm")
    os.mkdir(".playground/train/potato")
    os.mkdir(".playground/train/rice")
    os.mkdir(".playground/train/soybean")
    os.mkdir(".playground/train/sugarcane")
    os.mkdir(".playground/train/sunflower")
    os.mkdir(".playground/train/wood-chip")
    os.mkdir(".playground/test/beetroot")
    os.mkdir(".playground/test/coconut")
    os.mkdir(".playground/test/corn")
    os.mkdir(".playground/test/palm")
    os.mkdir(".playground/test/potato")
    os.mkdir(".playground/test/rice")
    os.mkdir(".playground/test/soybean")
    os.mkdir(".playground/test/sugarcane")
    os.mkdir(".playground/test/sunflower")
    os.mkdir(".playground/test/wood-chip")

    for class_label in os.listdir(dataset_location):
        if os.path.isdir(os.path.join(dataset_location, class_label)):
            files = os.listdir(os.path.join(dataset_location, class_label))
            training_files = []
            random.shuffle(files)

            train_amount = (int)(len(files) * train_ratio)

            for count in range(train_amount):
                copy2(os.path.join(dataset_location, class_label, files[count]),
                        os.path.join(".playground/train/", class_label, files[count]))
                training_files.append(files[count])

            test_files = [f for f in files if f not in training_files]
            for file in test_files:
                copy2(os.path.join(dataset_location, class_label, file),
                        os.path.join(".playground/test/", class_label, file))


def build_data_generators(training_data, testing_data):
    training_data_generator = ImageDataGenerator(rescale = 1./255,
                                                shear_range = 0.2,
                                                zoom_range = 0.2,
                                                horizontal_flip = True)

    generated_training_data = training_data_generator.flow_from_directory(training_data,
                                                target_size= IMAGE_SIZE,
                                                batch_size = 15,
                                                class_mode= 'categorical')

    test_data_generator = ImageDataGenerator(rescale = 1./255)
    generated_test_data = test_data_generator.flow_from_directory(testing_data,
                                                target_size= IMAGE_SIZE,
                                                batch_size = 15,
                                                class_mode= 'categorical')

    return (generated_training_data, generated_test_data)
