
# Keras for image classification model

import tensorflow
import numpy
from PIL import Image

model = tensorflow.keras.models.load_model("model_keras.h5")
classes = [  "breakup" ,  "clean" ,  ]


img = Image.open( "image.jpg" ).convert('RGB')
img = img.resize((300, 300 * img.size[1] // img.size[0] ), Image.ANTIALIAS)
inp_numpy = numpy.array( img )[None]

class_scores = model.predict( inp_numpy )[0]

print("")
print("class_scores" , class_scores)
print("Class : " , classes[  class_scores.argmax()])