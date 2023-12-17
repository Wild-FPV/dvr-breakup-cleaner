# TFLite for image classification model

import tensorflow as tf
import numpy as np
import cv2

#model setup:

model = tf.lite.Interpreter(model_path="modelv2.tflite")
classes = [  "breakup" ,  "clean" ,  ]

# Learn about its input and output details
input_details = model.get_input_details()
output_details = model.get_output_details()

model.resize_tensor_input(input_details[0]['index'], (1, 224, 224, 3))
model.allocate_tensors()

######################################################################

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

    #print("")
    #print("class_scores", class_scores)
    #print("Class : ", classes[class_scores.argmax()])
    #print("Progress : " + str((counter/frame_count)*100))
    
    if classes[class_scores.argmax()] == "clean":
        classification_results.append(1)
    else:
        classification_results.append(0)
    
print(classification_results)

counter = 0
for frame in images:
    if counter != len(images)-1:
        if classification_results[counter]:
            last_clean_frame = frame
            print("Counter is " + str(counter) + " and frame is clean")
        else:
            temp_counter = counter
            if classification_results[counter+1]:
                next_clean_frame = images[counter+1]
            else:
                while not classification_results[temp_counter]:
                    temp_counter += 1
                next_clean_frame = images[temp_counter]
            images[counter] = cv2.addWeighted(last_clean_frame,0.5,next_clean_frame,0.5,0)
        counter += 1
for frame in images:
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame,(width,height))
    video_writer.write(frame)

video_writer.release()
print("Done")