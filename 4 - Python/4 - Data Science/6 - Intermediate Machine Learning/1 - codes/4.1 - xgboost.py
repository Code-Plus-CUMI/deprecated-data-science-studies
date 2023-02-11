"""
This is a complement of XGBoost where I explain about some parameters
that can be set up when creating the model and I show how to apply
Cross-Validation with this technique.
"""

import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 0 - Transforming Dataset into DMatrix in order to get better
# results
X_dmatrix = xgb.DMatrix(data=X, label=y)

X_train, X_test, y_train, y_test = train_test_split(X_dmatrix, y, test_size=0.2, random_state=123)

# 1 - Creating XGB Model using some parameters
#
# - objective: will XGB make predictions (reg:linear) or classifications
# (reg:logistic for only decision, binary:logistic for decision and probability)
# - colsample_bytree: percentage of features used by tree (high values lead to overfitting)
# - learning_rate: the learning rate measure!
# - max_depth: maximum level that a tree can grown during any boosting round
# - alpha: regularization on leaf weights (high values lead to high regularizations)
# - n_estimators: number of trees that'll be build
xgb_model = XGBRegressor(
	objective='reg:linear'
	, colsample_bytree=0.3
	, learning_rate=0.1
	, max_depth=5
	, alpha=10
	, n_estimators=10
	, n_jobs=4
)

xgb_model.fit(
	X_train, y_train
	, early_stopping_rounds=5 # optional
	, verbose=False | True # False >> don't show logs
	, eval_set=[(X_valid, y_valid)] # optional
)

predictions = xgb_model.predict(X_valid)

###############

# 2 - Applying Cross-Validation (CV)

params = {
	'objective'         :  'reg:linear'
	, 'learning_rate'   :  0.1
	, 'max_depth'       :  0.1
	, 'alpha'           :  10
	# , 'n_estimators'    :  50 # replaced by 'num_boost_round'
}

# Parameters:
#
# - dtrain: the whole dataset to be split into train and validation
# - params: the parameters to createe the model (set as a dictionary)
# - nfold: number of folds to create the train and validation datasets
# - num_boost_round: number of trees that will be build (it's like 'n_estimators')
# - early_stopping_rounds: number of rounds without improving the learning to stop the training phase
# - metrics: metrics to evaluate the model
# - as_pandas: True >> returns the results in Pandas DataFrame format
# - seed: it's like 'random_state' for reproducability
cv_results = xgb.cv(
	dtrain=xgb.DMatrix(x=X_train, y=y_train)
	, params=params
	, nfold=5
	, num_boost_round=50
	, early_stopping_rounds=10
	, metrics='rmse'
	, as_pandas=True
	, seed=123
)

# seeing the first five rows of results
cv_results.head()

# returns the last RMSE
print(cv_results['test-rmse-mean'].tail(1))

# 3 - Creating the model after Cross-Validation Step, plotting the
# first tree and Feature Importance plotting
xgb_model = xgb.train(
	params=params
	, num_boost_round=10
	, dtrain=X_dmatrix
)

# First Tree Plotting
xgb.plot_tree(xgb_model, num_trees=0)
plt.rcParams['figure.figsize'] = [50, 10]
plt.show()

# Feature Importance Plotting (yeah, Machine Learning Explainability here!!)
xgb.plot_importance(xgb_model)
plt.rcParams['figure.figsize'] = [5, 5]
plt.show()

# 4 - Making Predictions
predictions = xgb_model.predict(xgb.DMatrix(x=X_valid, y=y_valid))