"""
XGBoost works in the following way:

/ trains the first model (aka Naive Model)
/ predicts the results
/ calculates the loss (such as MAE, MSE, MRE and so on)
/ chooses a new model to train
/ adds the new model to the Naive one in order to get better
results

/ The cycle is repeated till the model reaches the learning
rate goal
"""

from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error


# Creating the XGBoost Model #
"""
Parameters:

/ n_estimators: how many times the cycle will be repeated.
It's often between 100-1000 times. However, take care, because:

- Too low a value causes underfitting, which leads to inaccurate 
redictions on both training data and test data.

- Too high a value causes overfitting, which causes accurate 
predictions on training data, but inaccurate predictions on test 
data (which is what we care about).

/ early_stopping_rounds: the model will stop running if it gets X
cycles without improving the learning rate. It's often setted
by 5.

Also, when you use this parameter, you gotta assign the validation
dataset to the model too with the EVAL_SET parameter

/ learning_rate: this parameter is multiplied to the predictions
results in order to get more accurate results. As small the learning
rate is and larger the n_estimators are, the better the predictions
will be.

In the other hand, how the learning_rate makes the model goes through
the cycle more times, the model will take more time to process.

The default leaning_rate is 0.1.

/ n_jobs: you assign the number of cores the CPU/GPU/TPU has
in order to run the code in parallel

/ verbose: False >> turns off the train log. True (default) >>
turns on
"""

my_model = XGBRegressor(n_estimators=500
						, learning_rate=0.05
						, n_jobs=4)

my_model.fit(X_train, y_train
			, early_stopping_rounds=5
			, eval_set=[(x_valid, y_valid)]
			, verbose=False)


# Calculating the Final Mean Absolute Error #

predictions = my_model.predict(X_valid)
mae = mean_absolute_error(predictions, y_valid)
print('MAE:', mae)