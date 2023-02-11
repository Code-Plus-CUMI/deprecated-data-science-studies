"""
	2 - Maximum Pooling

This last step in the head intensifies the features,
making the model gets just the most useful part of the
image (ignoring the most zeros [black pixels] and turning
the classification better and faster).
"""

import tensorflow as tf
import matplotlib.pyplot as plt

# 0 - Reading the image #
image_path = 'imagePath.jpg'
image = tf.io.read_file(image_path)
image = tf.io.decode_jpeg(image)

# 1 - Defining the Kernel (Edge Detection) #
kernel = tf.constant([
	[-1, -1, -1],
	[-1,  8, -1],
	[-1, -1, -1]
], dtype=tf.float32)

# 2 - Reformatting the image and kernel for batch compatibility #
image = tf.image.convert_image_dtype(image, dtype=tf.float32)
image = tf.expand_dims(image, axis=0)
kernel = tf.reshape(kernel, [*kernel.shape, 1, 1])

# 3 - Filtering the Features (Convolutional Layer) #
image_filter = tf.nn.conv2d(
	input=image,
	filters=kernel,
	strides=1,
	padding='SAME',
)

# 4 - Detecting the Features (ReLU) #
image_detect = tf.nn.relu(image_filter)

# 5 - Showing the Results so far #
plt.subplot(131)
plt.title('Input')
plt.axis('off')
plt.imshow(tf.squeeze(image), cmap='gray')

plt.subplot(132)
plt.title('Filter')
plt.axis('off')
plt.imshow(tf.squeeze(image_filter), cmap='gray')

plt.subplot(133)
plt.title('Detect')
plt.axis('off')
plt.imshow(tf.squeeze(image_detect), cmap='gray')

plt.show()

# 6 - Enhancing/Condensing the Features (Max Pooling) #
image_condense = tf.nn.pool(
	input=image_detect,
	window_shape=(2,2),
	pooling_type='MAX',
	strides=(2,2),
	padding='SAME', # the output is in the same size of the input
	#padding='VALID', # the output is not in the same size of the input (it's in the same size of the padding)
)

plt.title('Condense')
plt.axis('off')
plt.imshow(tf.squeeze(image_condense))
plt.show()