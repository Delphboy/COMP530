# COMP530 - MSc Group Project

## Using Deep Convolutional Neural Network to Detection Bio-energy Image Segments

The aim of this project is to develop a desktop application that is capable of detecting bio-energy sources within images. It is developed in Python with PyQt and TensorFlow.

Keep track of the project progress with the [Kanban Board](https://github.com/Delphboy/COMP530/projects/1)

Technical documentation can be found at [docs/technical.md](/docs/technical.md) and user documentation can be found at [docs/user.md](/docs/user.md).

## Setup Guide

Ensure you have [Git LFS](https://git-lfs.github.com/) and [TensorFlow](https://www.tensorflow.org/install) installed. The project is written in Python 3.7.

Clone the project: `git clone https://github.com/Delphboy/COMP530.git`

Navigate to the project root: `cd COMP530`

Install dependencies: `pip install -r requirements.txt`

## Running The Project

The project can be operated from a UI or via the command line via a CLI.

- **Recommended:** Running the UI: `python src/main.py --gui`
- Running an existing model on the dataset via the CLI: `python src/main.py --detect <location of the model .h5 file> <directory of training set>`
- Training a model via the CLI `python src/main.py --train <directory of dataset> <train ratio>` Where the train ratio is: 0 < train ratio < 1.

## Contribution

- Any PRs to the `master` branch require a code review from one other team member
- Any PRs will undergo automated linting checks via GitHub Actions. These checks *must* pass before the PR can be merged.

## Team Members

- [Bharathkumar Ayyadurai](https://github.com/BharathKumar)
- [Sai Saranya Donthukurthi](https://github.com/Sai-SaranyaD)
- [Guo Li](https://github.com/ronan1028)
- [Zhiying Li](https://github.com/ZhiyingLi-123)
- [Susanthi Mandalapu](https://github.com/SusanthiMandalapu)
- [Henry Senior](https://github.com/Delphboy)