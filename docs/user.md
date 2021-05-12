# User Documentation

## Command Line Interface

### Training a Model

Models can be trained via the CLI to enable use cases where training takes place on a remote system ie) a HPC compute cluster.

1. Navigate to the repository root folder in a terminal
2. Run `python src/main.py --train <path to dataset directory> <train ratio>`

The train ratio parameter determines the percentage of the dataset that is used for training, with the remaining amount being left for testing the model. `0.8` is a good starting value and will use 80% of the dataset as training material

### Using a Model

Models can detect biofuel in a single image file or in multiple image files held in a directory. In the `<path to image>` parameter, provide the specific file or directory as appropriate.

1. Navigate to the repository root folder in a terminal
2. Run `python src/main.py --detect <path to model h5 file> <path to image>`

Example: `python src/main.py --detect src/models/demo-model.h5 datasets/beetroot/beetroot-1.jpg` Will detect biofuel in the `beetroot-1.jpg` image

Example: `python src/main.py --detect src/models/demo-model.h5 datasets/beetroot/` Will detect biofuel in all images in the `beetroot` folder.

## Desktop Application

!['Desktop application startup state'](images/gui-1.png)

### Training a Model

The top of the left hand side of the application allows the user to select a training dataset and set the train:test ratio. Once both fields are set the model can be trained.

!['Desktop application output after training'](images/gui-trained.png)

Once the model has been trained, the user will see the training and validation accuracy and loss metrics. It is possible to view the metrics of previous models by selecting the model from the drop down.

!['Desktop application previous model statics'](images/gui-data-view.png)

### Using a Model

The bottom half of the left hand side of the application allows the user to select a folder containing data they wish to identify biofuel in. Once a folder has been selected, a pre-trained model should be selected. Once both are selected, the model can be used to predict the presence of biofuel in the images. The predictions are then displayed to the user.

!['Using the desktop application to predict biofuel presence'](images/gui-prediction.png)
