from tensorflow import keras
from tensorflow.keras import layers

"""
	** Dropout and Batch Normalization Layers **

1 - Dropout Layer:

It's used to avoid overfitting. In a nutshell, this layer just
makes some neurons in a deep layer (for example) don't process 
the input at in the first moment. After that, the dropout allows
these neurons to process, but disable other ones to process.

This technique avoids the model to learn spurius patterns that
lead to overfitting.

It's often added before the layer that will suffer the dropout
"""

model = keras.Sequential([

	# hidden
	layers.Dropout(rate=0.3), # apply 30% dropout to the next layer
	layers.Dense(units=16, activation='relu', input_shape=[11]),

	# output
	layers.Dense(1),
])

model = keras.Sequential([

	# hidden
	layers.Dropout(0.3),
	layers.Dense(units=16, input_shape=[11]),
	layers.Activation('relu'),

	# output
	layers.Dense(1),
])

"""
2 - Batch Normalization (Batch Norm) Layer:

It's used when the training step is taking TOO MUCH TIME or
is UNSTABLE. This layer just normalizes/standards/scales the 
datas inside the model (like the preprocessor step, but inside 
the model/network).

This technique avoids the model to be taking too much time to
train and to don't get stuck with unstable inputs.

It's often added before (preprocessor) or after (processor) of
a layer.
"""

# preprocessor
model = keras.Sequential([
	# hidden
	layers.BatchNormalization(input_shape=[11]),
	layers.Dense(units=1024, activation='relu'),

	# output
	layers.Dense(1),
])

# processor
model = keras.Sequential([
	# hidden
	layers.Dense(units=1024, activation='relu', input_shape=[11]),
	layers.BatchNormalization(),

	# output
	layers.Dense(1),
])

model = keras.Sequential([
	# hidden
	layers.Dense(units=1024, input_shape=[11]),
	layers.BatchNormalization(),
	layers.Activation('relu'),

	# output
	layers.Dense(1),
])