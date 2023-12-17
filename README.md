# dvr-breakup-cleaner

## About

Using machine learning, this program is able to detect and remove frames containing breakup from your DVR. Don't worry about your DVR's framerate as the removed frames will be replaced with a smooth transition between the previous and next frame. As this is still a work-in-progress, my thought progress for how the project will pan out is detailed below.

## Process

### Creating the model

**script 1 :** take random frames from a couple of given DVR files and put them in a folder. Also create two empty folders, called "breakup" and "clean". From there I can manually move the frames into the appropriate folders to "label" the dataset.

**script 2 :** go through each folder and train a model based on patterns in frames.

Create model using [**liner.ai**](https://liner.ai/) : I might come back to this step and make my own models "manually", thought process is that I could either make the model based on pixel values or features of the frames (contrast, textures, edges, etc.). However, I was able to find an application called liner.ai that can create machine learning models in a couple of different formats given data in exactly the format we have it in here. I have added the created model in a variety of formats here (Standard Keras, Tensorflow, Tensorflow Lite). *Note : model_std.keras - standard Keras model, model.keras - Tensorflow model, and model.tflite - Tensorflow Lite model.*

### Using the model

**script 3 :** use model to detect frames with breakup in given dvr video file and replace those frames with weighted averages of "clean" frames that came before and after it.

If you want to try out the code yourself, make sure to download opencv-python by using the following command : `pip install opencv-python`.

If you want to try making your own model using this code, make sure to download tensorflow using : `pip install tensorflow`. (Note tensorflow requires python version 3.9-3.11)


### Currently working on script 3 (final .exe version)

Currently working on improving speed of video frame classification and an alternative approach for frame interpolation to hopefully produce a better result.
