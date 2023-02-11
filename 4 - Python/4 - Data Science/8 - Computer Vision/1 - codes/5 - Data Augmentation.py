"""
	5 - Data Augmentation

The best way to improve the performance of a machine 
learning model is to train it on more data. 
The more examples the model has to learn from, 
the better it will be able to recognize which 
differences in images matter and which do not. 
More data helps the model to generalize better.

One easy way of getting more data is to use the data 
you already have. If we can transform the images in 
our dataset in ways that preserve the class, we can 
teach our classifier to ignore those kinds of 
transformations. For instance, whether a car is facing 
left or right in a photo doesn't change the fact that 
it is a Car and not a Truck. So, if we augment our 
training data with flipped images, our classifier 
will learn that "left or right" is a difference it 
should ignore.

And that's the whole idea behind data augmentation: add 
in some extra fake data that looks reasonably like the 
real data and your classifier will improve!!
"""

"""
Typically, many kinds of transformation are used when 
augmenting a dataset. These might include rotating the 
image, adjusting the color or contrast, warping the image, 
or many other things, usually applied in combination. 
Here is a sample of the different ways a single image 
might be transformed (see image 6).

It's important to remember though that not every 
transformation will be useful on a given problem. 
Most importantly, whatever transformations you use 
should not mix up the classes. If you were training a 
digit recognizer, for instance, rotating images would 
mix up '9's and '6's. In the end, the best approach for 
finding good augmentations is the same as with most ML 
problems: try it and see!
"""

# 0 - Setting the Configs and Reading the Dataset #
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

#########

# 1 - Creating the Model and the Data Augmentation
# Transformation #

from tensorflow import keras
from tensorflow.keras import layers

# these are a new feature in TF 2.2
from tensorflow.keras.layers.experimental import preprocessing


pretrained_base = tf.keras.models.load_model(
    '../input/cv-course-models/cv-course-models/vgg16-pretrained-base',
)
pretrained_base.trainable = False

model = keras.Sequential([

    # Input Layer #
    layers.InputLayer(input_shape=[128, 128, 3]),

    # Preprocessing
    preprocessing.RandomFlip('horizontal'), # flip left-to-right
    preprocessing.RandomContrast(0.5), # contrast change by up to 50%

    # Base
    pretrained_base,

    # Head
    layers.Flatten(),
    layers.Dense(6, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])


from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([

	# Input Layer #
    layers.InputLayer(input_shape=[128, 128, 3]),
    
    # Data Augmentation #
    preprocessing.RandomContrast(factor=0.10),
    preprocessing.RandomFlip(mode='horizontal'),
    preprocessing.RandomRotation(factor=0.10),

    ## Base ##

    # Block One #
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Two #
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Three #
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'),
    layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    ## Head ##
    layers.BatchNormalization(renorm=True),
    layers.Flatten(),
    layers.Dense(8, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

# 2 - Training #
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

history = model.fit(
    ds_train,
    validation_data=ds_valid,
    epochs=30,
    verbose=0,
)

# 3 - Evaluating #
import pandas as pd

history_frame = pd.DataFrame(history.history)

history_frame.loc[:, ['loss', 'val_loss']].plot()
history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot();

#######

"""
	Some Augmentation Functions That We Can Apply	
"""

preprocessing.RandomContrast(factor=0.5),
preprocessing.RandomFlip(mode='horizontal'), # meaning, left-to-right
preprocessing.RandomFlip(mode='vertical'), # meaning, top-to-bottom
preprocessing.RandomWidth(factor=0.15), # horizontal stretch
preprocessing.RandomRotation(factor=0.20),
preprocessing.RandomTranslation(height_factor=0.1, width_factor=0.1),