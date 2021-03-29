"""Contains code for abstractions used to simplify interaction with the model"""
class ModelWrapper:
    '''Provide a wrapper to the prediction model'''
    __model = None

    def __init__(self, model = None):
        super().__init__()
        if model is None:
            self.__model = "" #set the model to default
        else:
            self.__model = model


    def set_model(self, new_model):
        '''Allows the class to wrap a new model'''
        self.__model = new_model


    def detect(self, image):
        """Detects the biofuel type in a given image
            Parameters: image
            Returns: prediction and confidence
        """
        model = self.__model # reference model to remove linting errors
        print("Using model: " + model)
        class_label = "Not Set" + image
        confidence = 0.0
        return (class_label, confidence)
