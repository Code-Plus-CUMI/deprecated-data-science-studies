"""
** Binary Classification **

- Cross-Entropy: while the MAE is the Loss Function often applied
to measure the Regression/Prediction Models, the Cross-Entropy is
often applied to measure the Binary Classifications.

Different from the MAE, this Loss Function doesn't measure the 
difference between the real value with the prediction one, but yes, 
the probability distribution of the classes.

- Sigmoid Activation: while the ReLU is the Activation Function often
applied in Regression/Prediction Models, Sigmoid is often applied
in Binary Classifications.

As long the Cross-Entropy must receive probabilities as input to
calculate the loss, the Sigmoid Function converts the model outputs
into probabilities.

- Threshold: the probabilities go from 0.0 to 1.0 and, when working
with Binary Classifications, the threshold is often defined as 0.5,
which means, when the output is lower than 0.5, the predicted class
will be CLASS_1; and when the output is equal or higher than 0.5, 
the predicted class will be CLASS_2.
"""

from tensorflow import keras
from tensorflow.keras import layers

# Creating the Model #
model = keras.Sequential([
	# hidden
	layers.Dense(units=4, activation='relu', input_shape=[33]),
	layers.Dense(units=4, activation='relu'),

	# outputs
	layers.Dense(units=1, activation='sigmoid'),
])

# Defining the Optimizer and Loss Functions #
model.compile(
	optimizer='adam',
	loss='binary_crossentropy',
	metrics=['binary_accuracy'],
)

# Early Stopping #
early_stopping = keras.callbacks.EarlyStopping(
	min_delta=0.001,
	patience=10,
	restore_best_weights=True,
)

# Fitting the Model #
history = model.fit(
	X_train, y_train,
	validation_data=(X_valid, y_valid),
	batch_size=512,
	epochs=1000,
	callbacks=[early_stopping],
	verbose=0,
)

# Plotting the Losses #
import pandas as pd

history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot(title='Cross-Entropy')
history_df.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot(title='Accuracy')

"""
 
Indicator that the neural network is good:

/ the accuracy rose at the same rate as the cross-entropy fell, 
so it appears that minimizing cross-entropy was a good stand-in
"""



######

# We can also make Binary Classifications with
# sklearn rather than using Deep Learning

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)