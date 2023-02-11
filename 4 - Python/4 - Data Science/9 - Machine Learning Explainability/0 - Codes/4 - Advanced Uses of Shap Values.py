"""
	
	**********************************
	** Advanced Uses of Shap Values **
	**********************************

There are two great advanced uses of Shap Values: Summary Plots and Contribution Plots.
"""

"""

	*******************
	** Summary Plots **
	*******************

They are used with Permutation Importance in order to know both the features' importance and how
they affect the predictions (increase/decrease predictions and if the values are low/high to affect
the predictions).

Besides, different from Shap Values, where we can use a single or multiple rows, you MUST use the WHOLE
VALIDATION DATASET in Summary Plots in order to get a general result!!
"""

# Importing libraries, reading dataset, setting Target and Features, and training a model
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('../input/fifa-2018-match-statistics/FIFA 2018 Statistics.csv')

y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64, np.int64]]
X = data[feature_names]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

my_model = RandomForestClassifier(random_state=0).fit(train_X, train_y)

# Importing, creating and calculating Shap Values
import shap
explainer = shap.TreeExplainer(my_model)
shap_values = explainer.shap_values(val_X) # yeah, we use the whole validation dataset

"""
	Observations:

	/ When plotting, we call shap_values[1]. For classification problems, there is a separate array
of SHAP values for each possible outcome. In this case, we index in to get the SHAP values for the
prediction of "True";

	/ Calculating SHAP values can be slow. It isn't a problem here, because this dataset is small.
But you'll want to be careful when running these to plot with reasonably sized datasets. The exception
is when using an xgboost model, which SHAP has some optimizations for and which is thus much faster;
"""
shap.summary_plot(shap_values[1], val_X)

"""

	************************
	** Contribution Plots **
	************************

They are used with Partial Plots in order to know the both how the features impact the predictions and
and the correlation between two features.

Besides, different from Shap Values, where we can use a single or multiple rows, you MUST use the WHOLE
VALIDATION DATASET in Contribution Plots in order to get a general result!!
"""

# Importing libraries, reading dataset, setting Target and Features, and training a model
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('../input/fifa-2018-match-statistics/FIFA 2018 Statistics.csv')

y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64, np.int64]]
X = data[feature_names]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

my_model = RandomForestClassifier(random_state=0).fit(train_X, train_y)

# Importing, creating and calculating Shap Values
import shap
explainer = shap.TreeExplainer(my_model)
shap_values = explainer.shap_values(val_X) # yeah, we use the whole validation dataset

# Plotting
#
# param 1 >> feature
# param 2 >> positive outcome
# param 3 >> validation dataset
# param 4 >> feature for interaction
shap.dependence_plot('Ball Possession %', shap_values[1], val_X, interaction_index="Goal Scored")