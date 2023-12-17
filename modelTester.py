# TFLite for image classification model

import tensorflow as tf
import numpy as np
import cv2
import os


#model setup:

model = tf.lite.Interpreter(model_path="modelv2.tflite")
classes = [  "breakup" ,  "clean" ,  ]

# Learn about its input and output details
input_details = model.get_input_details()
output_details = model.get_output_details()

model.resize_tensor_input(input_details[0]['index'], (1, 224, 224, 3))
model.allocate_tensors()


#videoPath = input("Input video filename : ")
videoPath="testdvr.avi"
video = cv2.VideoCapture(videoPath)
fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

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
counter = 0

video_writer = cv2.VideoWriter("output_video.avi",cv2.VideoWriter_fourcc(*'XVID'), fps,(width,height))

classification_results = []
# 1 is clean and 0 is breakup

for frame in images:
    
    frame_np = np.array( frame )[None].astype('float32')
    model.set_tensor(input_details[0]['index'], frame_np)
    model.invoke()

    class_scores = model.get_tensor(output_details[0]['index'])
    
    if classes[class_scores.argmax()] == "clean":
        classification_results.append(1)
    else:
        classification_results.append(0)

if not os.path.exists("breakup"):
    os.mkdir("breakup")
    
if not os.path.exists("clean"):
    os.mkdir("clean")

for index, result in enumerate(classification_results):
    if result:
        cv2.imwrite(os.path.join("clean",f"output_frame_{index}.jpg"),cv2.cvtColor(images[index],cv2.COLOR_RGB2BGR))
    else:
         cv2.imwrite(os.path.join("breakup",f"output_frame_{index}.jpg"),cv2.cvtColor(images[index],cv2.COLOR_RGB2BGR))
