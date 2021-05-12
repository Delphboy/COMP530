# Technical Documentation

## Architecture

![Architectural diagram](images/architecture.png)

## Adding Supported Image File Types

1. Add the image file type to the `.gitattributes` file with `git lfs track "*.<file type>"`. So `git lfs track "*.jpg"` will track jpeg files
2. Add the file type to the `SUPPORTED_FILES` list at the top of `detect.py`

Currently supported image files are:
- jpg
- jpeg
- png

## Adding CLI Operations

CLI argument parsing is handled by the [argparse](https://docs.python.org/3/library/argparse.html) library. Additional arguments can be added to the `main.py` by adding an appropriate argument to the parser object and providing a corresponding path in the if/else tree.
