# Code used in Google Colab for model training
# 

!cp -r "/content/drive/MyDrive/Machine Learning/Facial_Recognition_Data" /content/data

train_dir = '/content/data/train'
test_dir = '/content/data/test'

import os

data_path = '/content/drive/MyDrive/Machine Learning/Facial_Recognition_Data'

import matplotlib.pyplot as plt
import cv2

%matplotlib inline

from tensorflow.keras.preprocessing.image import ImageDataGenerator

image_gen = ImageDataGenerator(rotation_range=30,
                              width_shift_range=0.1,
                              height_shift_range=0.1,
                              rescale=1/255,
                              shear_range=0.2,
                              zoom_range=0.2,
                              horizontal_flip=True,
                              fill_mode='nearest')

image_gen.flow_from_directory(train_dir)
input_shape = (200,200,3)

from keras.models import Sequential
from keras.layers import Activation,Dropout,Flatten,Conv2D,MaxPooling2D,Dense

model = Sequential()

model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=input_shape,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=input_shape,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=input_shape,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dropout(0.5))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])

batch_size = 16

train_image_gen = image_gen.flow_from_directory(train_dir,target_size=input_shape[:2],batch_size= batch_size,class_mode='binary')

test_image_gen = image_gen.flow_from_directory(test_dir,target_size=input_shape[:2],batch_size= batch_size,class_mode='binary')

train_image_gen.class_indices

results = model.fit(
    train_image_gen,
    epochs=150,
    steps_per_epoch=150,
    validation_data=test_image_gen,
    validation_steps=12
)