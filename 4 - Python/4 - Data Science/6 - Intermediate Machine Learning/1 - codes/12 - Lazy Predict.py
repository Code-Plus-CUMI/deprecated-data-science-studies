#	******************
#	** Lazy Predict **
#	******************
#
# 	Even though there is "Lazy" in its name, Lazy Predict library has nothing
# to do with it!! This library, nothing more and nothing less, creates tons
# of Machine Learning Models to train and validate your dataset and, after
# the process, returns a DataFrame containing the Scores and Metrics of each
# trained Model.
#
# 	With it, you can see which ML Algorithm suits better for your dataset
# without having to create each model by hand!
#
#	The library provides processes for Regression, Classification and
# Clustering Problems via its Supervised and Unsupervised sub-modules.
#
#	Simple Tutorial: https://www.geeksforgeeks.org/lazy-predict-library-in-python-for-machine-learning/
#


# ---- Installing Library ----
!pip install lazypredict



# ---- Imports ----
import pandas as pd
from lazypredict.Supervised import LazyRegressor  # for Regression Problems
from lazypredict.Supervised import LazyClassifier # for Classification Problems

 

# ---- Reading Dataset ----
df = pd.read_csv('csv')

# [ split up dataset into features and target ... ]
# [ split up dataset into train and validation ... ]
# [ other processes ]



# ---- Applying Lazy Predict for Regression Problems ----
lazy_regressor = LazyRegressor(
	verbose=0                 # False >> turns off log; True >> turns on log;
	, ignore_warnings=False   # False >> does not ignore warning messages; True >> ignores warning messages;
	, custom_metric=None      # when "None", the library chooses the best metrics to measure all models
)

models, predictions = lazy_regressor.fit(X_train, X_valid, y_train, y_valid)

print(models)



# ---- Applying Lazy Regressor for Classification Problems ----
lazy_classifier = LazyClassifier(
	verbose=0
	, ignore_warnings=False
	, custom_metric=None
)

models, predictions = lazy_classifier.fit(X_train, X_valid, y_train, y_valid)

print(models)