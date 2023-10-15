# dvr-breakup-cleaner

## About

Using machine learning, this program is able to detect and remove frames containing breakup from your DVR. Don't worry about your DVR's framerate as the removed frames will be replaced with a smooth transition between the previous and next frame. As this is still a work-in-progress, my thought progress for how the project will pan out is detailed below.

## Process

### Creating the model

**script 1 :** take random frames from a couple of given DVR files and put them in a folder. Also create two empty folders, called "breakup" and "clean". From there I can manually move the frames into the appropriate folders to "label" the dataset.

**script 2 :** go through each folder and train a model based on patterns in frames.

### Using the model

**script 3 :** use model to detect frames with breakup in given dvr video file and replace those frames with "averages" of frames that came before and after it
