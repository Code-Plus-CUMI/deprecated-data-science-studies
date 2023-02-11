"""

- Signal: it's the generalization, helping the model to get
good results with new datas in the validation, prediction and
production steps.

- Noise: it's the fluctuation/gaps/problems present ONLY in the
training data, so, noises don't help the model to get good
predictions in the future.

The Data Scientist's goal is to make the model learns a few noises
and a good amount of signals (but not too much). However, we gotta
a problem: as many signals the model learns, as many noises it'll
learn too!

So, to overcome this trade, Data Scientists have to get the BALANCE
between signal and noise in order to avoid Underfitting and
Overfitting.

----

- Underfitting: 

	/ the model doesn't learn enough
	/ it gets bad results in both training and validation steps
	/ the loss is high OR the train and valid loss just decrease
	/ the model didn't learn the enough signals

- Overfitting:

	/ the model learns more than the expected
	/ it gets great results in the training step, but
	bad ones in the validation step
	/ the loss is not too much high in the traning step,
	but it's too much high in the validation one
	/ the model learns signals/noises more than enough


Example 1: The gap between these curves is quite small and the validation 
loss NEVER INCREASES, so it's more likely that the network is 
underfitting than overfitting. 

Example 2: Now the validation loss begins to rise very early, while 
the training loss continues to decrease. This indicates that the 
network has begun to overfit. At this point, we would need to try 
something to prevent it, either by reducing the number of units or 
through a method like early stopping.
"""

from tensorflow import keras
from tensorflow.keras import layers

"""
** Capacity **

	- It's the capacity of the model to learn new patterns;

	- If the model gets Underfitting, we have to increase
	the model's capacity. If the model gets Overfitting,
	we have to decrease the capacity;

	- If the problem is the LINEAR RELATIONSHIPS, we gotta make
	the model wider (more units/neurons in each layer) for
	Underfitting; and less wider for Overfitting;

	- If the problem is the NON-LINEAR RELATIONSHIPS, we gotta
	make the model deeper (more layers) for Underfitting; and
	less deeper for Overfitting

In the examples below, consider that the model is being
underfitting and we decided to increase the depth and the
wide.
"""

# first version of the model
model = keras.Sequential([
	layers.Dense(16, activation='relu', input_shape=[2]),
	layers.Dense(1),
])

# wider >> more units/neuros per layer
wider = keras.Sequential([
	layers.Dense(32, activation='relu', input_shape=[2]),
	layers.Dense(1),
])

# deeper >> more layers
deeper = keras.Sequential([
	layers.Dense(16, activation='relu', input_shape=[2]),
	layers.Dense(16, activation='relu'),
	layers.Dense(1),
])

"""
** Early Stopping **

	- it helps the model doesn't learn too many noises in order
	to get underfitting and overfitting;

	- this technique checks out the loss of the model for each
	batch and, if it realizes that the loss is not decreasing
	after X epochs anymore, it'll stop the model of fitting 
"""

# Parameters:
#
# - min_delta >> minimum amount of change to the early stop
# consider that the loss function is decreasing and the model
# is improving (in this example, for each 0.001 the loss decreases
# is considered as an improvement for the model);
#
# - patience >> how many epochs without decreasing the loss value
# the early stopping will wait to stop the trainig;
#
# - restore_best_weights >> gets the weights that resulted in the
# lower loss value
#
# In a nutshell, if there hasn't been at least an improvement of 
# 0.001 in the validation loss over the previous 20 epochs, then
# stop the training and keep the best model you found.
#

from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
	min_delta=0.001,
	patience=20,
	restore_best_weigths=True,
)

##########

# Final Example #

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd


# early stopping
early_stopping = EarlyStopping(
	min_delta=0.001,
	patience=20,
	restore_best_weights=True,
)

# creating the model
model = keras.Sequential([

	# hidden
	layers.Dense(512, activation='relu', input_shape=[11]),
	layers.Dense(512, activation='relu'),
	layers.Dense(512, activation='relu'),

	# output
	layers.Dense(1),
])

# defining the optimizer and loss functions
model.compile(
	optimizer='adam',
	loss='mae',
)

# training the model
history = model.fit(
	X_train, y_train,
	validation_data=(X_valid, y_valid),
	batch_size=256,
	epochs=500,
	callbacks=[early_stopping],
	verbose=0, # turns off the training log
)

# plotting the loss along the epochs
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot()

print('Minimum Validation Loss:', history_df['val_loss'].min())