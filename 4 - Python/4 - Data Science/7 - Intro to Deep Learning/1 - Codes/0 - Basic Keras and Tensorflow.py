# Obs: tensorflow is a better version of NumPy
# suited to deep learning and to run in GPU and TPU

from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf

# Creating the model #
#
# / units         >>   number of outputs
# / input_shape   >>   number of inputs

model = keras.Sequential([
	layers.Dense(units=1, input_shape=[3])
])

# Checking out the weights and bias #

w, b = model.weights

print('Weights:', w)
print('Bias:', b)


"""
- Neural Networks with just Densee Layers can only work
with Linear Regressor, howerver, if we add Activation Functions
like Rectified Linear Unit (ReLU), we can find non-linear patterns, 
making the network smarter.

/ Predicting Values: combination of activation functions with linear
one. The last function should always be a linear.

/ Classification: combination of activation functions. The last function
should always be an activation one.

Besideds ReLU, there are others Activation Functions, such as ELU,
SELU, SWISH, Sigmoid and so on.
"""

model = keras.Sequential([

	# hidden layers = relu
	layers.Dense(units=4, activation='relu', input_shape=[2]),
	layers.Dense(units=3, activation='relu'),

	# output layer = linear
	layers.Dense(units=1),
])

model = keras.Sequential([

	# hidden layers = relu
	layers.Dense(units=4, input_shape=[2]),
	layers.Activation('relu'),
	layers.Dense(units=3),
	layers.Activation('relu'),

	# output layer = linear
	layers.Dense(units=1),
])

"""
- Loss Function calculates how good the model is. Mean Absolute
Error (MAE) is often used as a Loss Function

- Optimizers (Stochastic Gradient Descent - SGD) are functions to
improve the learning of model in order to get more accurate results
and decrease the Loss. ADAM is often applied as a SGD, because this
algorithm can improve by itself without the programmer sets the
improvement

- (Mini)Batch and Epoch: the first one is each time the model trains
with the data, whereas the second one is each round the model finishes
the traning. Which means, a model can have 5 EPOCHS with 200 BATCHES 
each one.

Besides, as longer the number (size) of batches and epochs, as better 
will be the model's learning rate.
"""

from tensorflow import keras
from tensorflow.keras import layers

# Creating the Model #
model = keras.Sequential([

	# hidden layers
	layers.Dense(units=512, activation='relu', input_shape=[11]),
	layers.Dense(units=512, activation='relu'),
	layers.Dense(units=512, activation='relu'),

	# output layer
	layers.Dense(units=1),
])

# Defining the Loss and Optimizer Functions #
model.compile(
	optimizer='adam',
	# optimizer='sgd', # SGD is more sensitive to differences of scale
	loss='mae',
)

# Training the Model #
#
# The model will receive 256 rows at a time (batch size)
# till proccess all of the dataset.
# And this step will be repeated 10 times (epochs)
history = model.fit(
	X_train, y_train,
	validation_data=(X_valid, y_valid),
	batch_size=256,
	epochs=10,
)

# Plotting the Loss Evolution #

import pandas as pd

history_df = pd.DataFrame(history.history)
history_df['loss'].plot()