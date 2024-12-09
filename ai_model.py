from tensorflow import keras
import numpy as np
from keras.preprocessing import image as keras_image
import PIL as pil


class AIModel:
    def __init__(self):
        self.model = self.prepare_model()
        self.classes = ('Airplane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck')

    def __repr__(self):
        return self.model.summary()

    def recognize_image(self, image_path):
        image = pil.Image.open(image_path).convert("RGB")
        image = image.resize((32, 32))
        image = keras_image.img_to_array(image)
        image = image.astype('float32') / 255.0
        image = image.reshape(-1, 32, 32, 3)
        prediction = self.model.predict(image)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        return self.classes[predicted_class_index]

    def prepare_model(self):
        model = keras.models.load_model('model_4.3_.h5')
        return model






