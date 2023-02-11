"""
** Convolutional Neural Network (CNN) **

CNN's consist in two parts: Convolutional Base and Dense Head. Being:

- Convolutional Base: in these layers, the image's features (lines,
patterns, color, textures, shapes and so on) are extract to be 
analysed. This part is often made by Convolutional Layers, but can 
includes other types too.

- Dense Head: in these layers, the image will be classified. This
part is often maded by Dense Layers, but can includes other types too,
such as Dropout and BatchNormalization.

----

One important thing to know is that most CNN's are not created by
scratch, but yes, by Transfer Learning. Which means, we use a
pretrained Base and add an untrained Head.

The model's training has two goals:
	1 - to learn which features to extract;
	2 - to learn which class these features are in.
"""

# Imports
import os, warnings
import matplotlib.pyplot as plt
from matplotlib import gridspec

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Reproducability
def set_seed(seed=31415):
    np.random.seed(seed)
    tf.random.set_seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
set_seed()

# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('image', cmap='magma')
warnings.filterwarnings("ignore") # to clean up output cells


# Load training and validation sets
ds_train_ = image_dataset_from_directory(
    '../input/car-or-truck/train',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=True,
)
ds_valid_ = image_dataset_from_directory(
    '../input/car-or-truck/valid',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=False,
)

# Data Pipeline
def convert_to_float(image, label):
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    return image, label

AUTOTUNE = tf.data.experimental.AUTOTUNE
ds_train = (
    ds_train_
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)
ds_valid = (
    ds_valid_
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)

########

import tensorflow_hub as hub

# Loading the Pretrained Base #

# this one is not so good because this is more
# likely to provide overfitting
#pretrained_base = tf.keras.models.load_model(
#    '../input/cv-course-models/cv-course-models/vgg16-pretrained-base',
#)

pretrained_base = tf.keras.models.load_model(
    '../input/cv-course-models/cv-course-models/inceptionv1'
)

# As long the base has already been pretrained, #
# we define it as non-trainable #
pretrained_base.trainable = False

# Creating the Head #
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    pretrained_base,
    layers.Flatten(), # this layer convert two dimensional input to one dimensional
    layers.Dense(units=6, activation='relu'),
    layers.Dense(units=1, activation='sigmoid'),
])

model = keras.Sequential([
    pretrained_base,
    layers.GlobalAvgPool2D(), # this layer superceeds all the Hidden ones (dense and flatten layers)
    layers.Dense(units=1, activation='sigmoid'),
])

model = keras.Sequential([
    layers.Conv2D(filters=64,
                  kernel_size=3,
                  strides=1,
                  padding='same',
                  activation='relu'),
    layers.MaxPool2D(pool_size=2,
                     strides=1,
                     padding='same')
    
    layers.Flatten(), # this layer convert two dimensional input to one dimensional
    layers.Dense(units=6, activation='relu'),
    layers.Dense(units=1, activation='sigmoid'),
])

# Optimizer and Loss Functions and Metrics #
#
# The Optimizer, we can always use the Adam in the first moment
#
# About the Loss Function and the Metrics, we have to always choose
# those ones that are appropriate for the problem.
# How the CNN are working with binary classification, we use the
# 'binary_crossentropy (get distribution probabilities)' and the 
# 'binary_accuracy'
optimizer = tf.keras.optimizers.Adam(epsilon=0.01)
model.compile(
    optimizer=optimizer,
    loss = 'binary_crossentropy',
    metrics=['binary_accuracy'],
)

# Training the Model #
history = model.fit(
    ds_train,
    validation_data=ds_valid,
    epochs=30,
)

# Evaluating the Model #
import pandas as pd
history_frame = pd.DataFrame(history.history)
history_frame.loc[:, ['loss', 'val_loss']].plot()
history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot();