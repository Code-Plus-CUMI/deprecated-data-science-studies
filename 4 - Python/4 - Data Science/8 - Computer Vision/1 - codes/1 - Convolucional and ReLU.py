"""
	1 - Convolutional and ReLU

The feature extraction performed by the base consists of 
three basic operations:

	- Filter an image for a particular feature (convolution)

	- Detect that feature within the filtered image (ReLU)

	- Condense the image to enhance the features 
	(maximum pooling)
"""

# Reading a Single Image and displaying it
import tensorflow as tf
import matplotlib.pyplot as plt

image_path = 'immagepath.jpg'
image = tf.io.read_file(image_path)
image = tf.io.decode_jpeg(image, channels=1) #the channels define the colors
image = tf.image.resize(image, size=[400,400])

plt.figure(figsize=(6,6))
plt.imshow(tf.squeeze(image), cmap='gray')
plt.axis('off')
plt.show()

# Creating the Kernel for the weights
#
# Edge Detection

kernel = tf.constant([
	[-1, -1, -1],
	[-1, 8, -1],
	[-1, -1, -1]
])

plt.figure(figsize=(3,3))
show_kernel(kernel)

# Preparing the image to be filtered
image = tf.image.convert_image_dtype(image, dtype=tf.float32)
image = tf.expand_dims(image, axis=0)

kernel = tf.reshape(kernel, [*kernel.shape, 1, 1])
kernel = tf.cast(kernel, dtype=tf.float32)

# Filtering the Image Features
image_filter = tf.nn.conv2d(
	input=image,
	filters=kernel,
	strides=1,
	padding='SAME',
)

plt.figure(figsize=(6,6))
plt.imshow(tf.squeeze(image_filter))
plt.axis('off')
plt.show()

# Detecting the Image
image_detect = tf.nn.relu(image_filter)

plt.figure(figsize=(6,6))
plt.imshow(tf.squeeze(image_detect))
plt.axis('off')
plt.show()



##############

"""
	Types of Kernels - 2D Inputs

The weights sum should be between 0 and 1, but it's not
a rule, it's just a pattern.
"""

edge_detection = tf.constant([
	[-1, -1, -1],
	[-1, 8, -1],
	[-1, -1, -1]
])

bottom_sobel = tf.constant([
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]
])

emboss = tf.constant([
	[-2, -1, 0],
	[-1, 0, 0],
	[0, 1, 2]
])

sharpen = tf.constant([
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]
])

blur = tf.constant([
	[0.06, 0.12, 0.06],
	[0.12, 0.25, 0.12],
	[0.06, 0.12, 0.06]
])

"""
	Types of Kernels - 1D Inputs
"""
detrend = tf.constant([-1, 1], dtype=tf.float32)

average = tf.constant([0.2, 0.2, 0.2, 0.2, 0.2], dtype=tf.float32)

spencer = tf.constant([-3, -6, -5, 3, 21, 46, 67, 74, 67, 46, 32, 3, -5, -6, -3], dtype=tf.float32) / 320

#######

"""
	Using SimPy to print beautiful matrix and arrays
"""

import sympy
sympy.init_printing()
from IPython.display import display

image = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
])

kernel = np.array([
    [1, -1],
    [1, -1],
])

display(sympy.Matrix(image))
display(sympy.Matrix(kernel))