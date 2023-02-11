"""

	*****************
	** Shap Values **
	*****************

Whereas Partial Plots explains the features' impacts over the general predictions, Shap Values
explains the features' impacts over a single prediction.

So, Shap Values is largely applied in Production Environment, while Partial Plots, in Development
Environment.


-*-*-*-

To calculate Shap Values, we gotta get a row from the dataset, and calculate the prediction assuming
some fictional values for the features (Baseline) and calculate the prediction with the real values
(Real Prediction). The Shap Value will be the difference between the Real Prediction and the Baseline
Prediction.

	sum(SHAP values for all features) = pred_for_team - pred_for_baseline_values

To stick it on your mind, suppose instead of ask:

	"How much was a prediction driven by the fact that the team scored 3 goals?"

we ask:

	"How much was a prediction driven by the fact that the team scored 3 goals, instead of some
								baseline number of goals."
"""


"""

IMPORTANT

{ image 3 }
How do you interpret this?

We predicted 0.7, whereas the base_value is 0.4979. Feature values causing increased predictions
are in pink, and their visual size shows the magnitude of the feature's effect. Feature values
decreasing the prediction are in blue.

The biggest impact comes from Goal Scored being 2. Though the ball possession value has a meaningful
effect decreasing the prediction.

If you subtract the length of the blue bars from the length of the pink bars, it equals the distance
from the base value to the output.
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

# Selecting a single row to calculate the Shap Value
#
# in this example we used a single row, but we can select multiples
row_to_show = 5
data_for_prediction = val_X.iloc[row_to_show]
data_for_prediction_array = data_for_prediction.values.reshape(1, -1)

# Real Prediction
my_model.predict_proba(data_for_prediction_array)

# Importing library, creating object and calculating Shap Values
import shap
explainer = shap.TreeExplainer(my_model)
shap_values = explainer.shap_values(data_for_prediction)

# Showing Shap Values' Results
shap.initjs()

# List Positions:
# [0] >> Negative Outcome
# [1] >> Positive Outcome (always consider this on in Shap Values)
#
# explainer.expected_value[1] >> Real Prediction
# shap_values[1] >> Baseline Prediction
# data_for_prediction >> Selected Data
shap.force_plot(explainer.expected_value[1], shap_values[1], data_for_prediction)




"""
If you look carefully at the code where we created the SHAP values, you'll notice we reference 
Trees in 'shap.TreeExplainer(my_model)'. But the SHAP package has explainers for every type of model.

	/ shap.DeepExplainer: works with Deep Learning models;
	/ shap.KernelExplainer: works with all models, though it is slower than other Explainers and it
offers an approximation rather than exact Shap values;

Here is an example using KernelExplainer to get similar results. The results aren't identical because
KernelExplainer gives an approximate result. But the results tell the same story:
"""

# use Kernel SHAP to explain test set predictions
#
# realize that we have to calculate the 'predict_proba' and provides
# the whole Train dataset because 'KernelExplainer' doesn't know which
# model we're using, so it must receive these parameters as a basis
k_explainer = shap.KernelExplainer(my_model.predict_proba, train_X)
k_shap_values = k_explainer.shap_values(data_for_prediction)

shap.initjs()
shap.force_plot(k_explainer.expected_value[1], k_shap_values[1], data_for_prediction)