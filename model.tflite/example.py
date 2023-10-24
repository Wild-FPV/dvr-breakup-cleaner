
# TFLite for image classification model

import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.lite.Interpreter(model_path="model.tflite")
classes = [  "breakup" ,  "clean" ,  ]


# Learn about its input and output details
input_details = model.get_input_details()
output_details = model.get_output_details()

model.resize_tensor_input(input_details[0]['index'], (1, 224, 224, 3))
model.allocate_tensors()

img = Image.open( "image.jpg"  ).convert('RGB')
img = img.resize((224, 224))
img_np = np.array( img )[None].astype('float32')

model.set_tensor(input_details[0]['index'], img_np)
model.invoke()

class_scores = model.get_tensor(output_details[0]['index'])

print("")
print("class_scores", class_scores)
print("Class : ", classes[class_scores.argmax()])