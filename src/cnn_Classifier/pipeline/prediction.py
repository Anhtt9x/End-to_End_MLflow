import numpy as np 
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeLine:
    def __init__(self, file_name):
        self.file_name = file_name

    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.keras"))

        image_file_name = self.file_name

        test_image = image.load_img(image_file_name, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] ==1:
            prediction = 'Normal'
            return [{"image": prediction}]
        else:
            prediction = 'Cancer'
            return [{"image": prediction}]
        
