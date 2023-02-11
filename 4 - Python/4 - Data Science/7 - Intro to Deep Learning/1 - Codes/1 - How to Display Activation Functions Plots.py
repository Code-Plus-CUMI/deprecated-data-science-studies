import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers

# Change 'relu' to 'elu', 'selu', 'swish' or something else
activation_layer = layers.Activation('relu')

# tf.linspace(x, y, z): creates a tensor with Z equally distributed
# elements from X to Y
x = tf.linspace(-3.0, 3.0, 100)

# once created, a layer is callable just like a function
y = activation_layer(x)

plt.figure(dpi=100)
plt.plot(x, y)
plt.xlim(-3, 3)
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()