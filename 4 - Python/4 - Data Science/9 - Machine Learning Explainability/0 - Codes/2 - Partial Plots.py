"""
	
	*******************
	** Partial Plots **
	*******************

Partial Plots are a technique to find out how the features impact in a single prediction and/or in all
predictions in general.

It's like finding the Coefficient in Linear Regression in order to know if a feature is more likely
to increase or decrease the prediction's result (when the feature is correlated to the target) or
is more likely to don't interfere (when the feature is not correlated to the target).

To use this technique, the model MUST BE FITTED, and the technique works changing the values of a column
and making predictions in order to know the general impact of that feature in the target (does the feature
increase or decrease the target? And from each value is the impact most notable?).

We can use calculate Partial Plots with a single row,but this is atypical and not appropriate, so we
should apply it in multiple rows and then we plot the average predicted outcome on the vertical axis.

So we first calculate the Partials and then Plot them!!
"""

# Importing libraries, reading dataset, setting Target and Features, and training a model
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('../input/fifa-2018-match-statistics/FIFA 2018 Statistics.csv')

y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
X = data[feature_names]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
tree_model = DecisionTreeClassifier(random_state=0,
									max_depth=5,
									min_samples_split=5).fit(train_X, train_y)

# Importing libraries, Calculating PDP (Partial Points) and Plotting it
from matplotlib import pyplot as plt
from pdpbox import pdp, get_dataset, info_plots

pdp_goals = pdp.pdp_isolate(model=tree_model, dataset=val_X, model_features=feature_names, feature='Goal Scored')

pdp.pdp_plot(pdp_goals, 'Goal Scored')
plt.show()

"""
About the Partial Plot:

	- The y axis is interpreted as CHANGE IN THE PREDICTION from what it would be predicted at the
baseline or leftmost value;
	
	- A blue shaded area indicates level of confidence.
"""


"""
	
	**********************
	** 2D Partial Plots **
	**********************

It's like the common Partial Plots, but calculating TWO FEATURES simultaneously!!
"""
features_to_plot = ['Goal Scored', 'Distance Covered (Kms)']
inter1  =  pdp.pdp_interact(model=tree_model, dataset=val_X, model_features=feature_names, features=features_to_plot)

pdp.pdp_interact_plot(pdp_interact_out=inter1, feature_names=features_to_plot, plot_type='contour')
plt.show()

"""
This graph shows predictions for any combination of Goals Scored and Distance covered.

For example, we see the highest predictions when a team scores at least 1 goal and they run a total
distance close to 100km. If they score 0 goals, distance covered doesn't matter. Can you see this by
tracing through the decision tree with 0 goals?

But distance can impact predictions if they score goals. Make sure you can see this from the 2D partial
dependence plot. Can you see this pattern in the decision tree too?
"""