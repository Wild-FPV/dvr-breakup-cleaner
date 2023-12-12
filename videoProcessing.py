# TFLite for image classification model

import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

#model setup:

model = tf.lite.Interpreter(model_path="model.tflite")
classes = [  "breakup" ,  "clean" ,  ]

# Learn about its input and output details
input_details = model.get_input_details()
output_details = model.get_output_details()

model.resize_tensor_input(input_details[0]['index'], (1, 224, 224, 3))
model.allocate_tensors()

######################################################################

videoPath = input("Input video filename : ")
video = cv2.VideoCapture(videoPath)

images = []

while True:
    
    #capture frame
    running,frame = video.read()
    
    if not running:
        break
    
    #convert from BGR to RGB
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    rgb_frame = cv2.resize(rgb_frame, (224,224))
    
    images.append(rgb_frame)
    
video.release()

frame_count = len(images)

print("Frames :")
print(frame_count)

counter = 1

for frame in images:
    
    frame_np = np.array( frame )[None].astype('float32')

    model.set_tensor(input_details[0]['index'], frame_np)
    model.invoke()

    class_scores = model.get_tensor(output_details[0]['index'])

    print("")
    #print("class_scores", class_scores)
    print("Class : ", classes[class_scores.argmax()])
    print("Progress : " + str(counter/frame_count)*100)
    
    counter += 1
