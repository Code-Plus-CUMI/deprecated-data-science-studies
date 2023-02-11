"""
		****************************
		** Permutation Importance **
		****************************

Features Importance is a process to find out which features have the bigger impact on predictions.

There are a bunch of techniques to calculate Features Importance, such as PERMUTATION IMPORTANCE,
which has the following advantages when compared to the other techniques:

		/ fast to calculate;
		/ widely used and understood;
		/ consistent with properties we would want a feature importance measure to have.

To use this technique, the model MUST BE FITTED, and the technique works shuffling a single datasets' column
in order to check out how the column would affect the accuracy of predictions. Think about Permutation
Importance like this:

	"If I randomly shuffle a single column of the VALIDATION data, leaving the target and all other
	columns in place, how would that affect the accuracy of predictions in that now-shuffled data?"

As bigger the difference between the Real Prediction and the New Prediction (after shuffling the column),
as most important the Feature is!!
"""

# Importing libraries, reading dataset, setting Target and Features, and training a model
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('../input/fifa-2018-match-statistics/FIFA 2018 Statistics.csv')

y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
X = data[feature_names]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(n_estimators=100,
                                  random_state=0).fit(train_X, train_y)


# Calculating Permutation Importance
import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(my_model, random_state=1).fit(val_X, val_y)
eli5.show_weights(perm, feature_names = val_X.columns.tolist())

"""

	************************************************
	** Interpreting Permutation Importance Tables **
	************************************************

The first number in each row shows how much model performance decreased with a random
shuffling (in this case, using "accuracy" as the performance metric).

The number after the ± measures how performance varied from one-reshuffling to the next (it's like the
Error Margin).

You'll occasionally see negative values for permutation importances. In those cases, the predictions
on the shuffled (or noisy) data happened to be more accurate than the real data. This happens when the
feature didn't matter (should have had an importance close to 0), but random chance caused the predictions
on shuffled data to be more accurate. This is more common with small datasets, like the one in this
example, because there is more room for luck/chance.
"""

"""
Also, Permutation Importance is great to check out whether the variables you've created in Features
Engineering Step are important.
"""