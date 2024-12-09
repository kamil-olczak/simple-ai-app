import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow import keras
from keras.datasets import cifar10
from keras import layers
from keras.preprocessing import image


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
print(x_train.shape, 'train samples')
print(y_train.shape, 'train labels')

datagen = image.ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    zoom_range=0.4
)


model = keras.Sequential([
    layers.Input(shape=(32, 32, 3)),
    layers.Conv2D(32, 3, padding='valid', activation='relu'),
    layers.BatchNormalization(),
    layers.Conv2D(64, 3, padding='valid', activation='relu'),
    layers.BatchNormalization(),
    layers.Conv2D(128, 3, padding='valid', activation='relu'),
    layers.BatchNormalization(),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(10, activation='softmax')
])

print(model.summary())

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


model.fit(x_train, y_train, epochs=2, batch_size=128, validation_data=(x_test, y_test))
model.fit(datagen.flow(x_train, y_train, batch_size=128), epochs=20, validation_data=(x_test, y_test))
model.fit(x_train, y_train, shuffle=True, batch_size=128, epochs=5,  validation_data=(x_test, y_test))
model.evaluate(x_test, y_test, batch_size=64)
model.save('model_4.3_.h5')

