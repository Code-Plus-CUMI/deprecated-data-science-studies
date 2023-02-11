"""
	
	*****************************
	** Mutual Information (MI) **
	*****************************


Mutual Information is like Permutation Importance, but used BEFORE training the model. It's like you start
working with a dataset and you wanna know which features are the most important in order to make your model
more accurate.

Also, Mutual Information (MI) is a lot like correlation in that it measures a relationship between two
quantities. The advantage of mutual information is that it can detect ANY KIND OF RELATIONSHIP, while
correlation ONLY DETECTS LINEAR RELATIONSHIPS.

-*-*-*-*-*-

The minimum value for MI is 0.0, meaning that the Features are independent (doesn't have any relationships).
Also, values above 2.0 or so are uncommon (as far as Mutual information is a logarithmic quantity, 
it increases very slowly).

In the end, don't forget to apply Categorical Features Encoding before calculating MI.
"""

# Importing libraries, reading dataset, setting Target and Feature, and getting Discrete and Continuous Features
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns


plt.style.use("seaborn-whitegrid")

df = pd.read_csv("../input/fe-course-data/autos.csv")

X = df.copy()
y = X.pop("price")

# remember that the categorical variables must be encoded #
# and that them are considered as discrete (after being encoded) #
# they are turned into 'integers' #
discrete_features = X.dtypes == int
continuous_features = X.dtypes == float

"""
----
"""

# Importing libraries, calculating MI Scores and plotting 'em
from sklearn.feature_selection import mutual_info_regression
from sklearn.feature_selection import mutual_info_classif

mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
mi_scores = mi_scores.sort_values(ascending=False)

def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")

plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores)

sns.relplot(x="curb_weight", y="price", data=df);

"""
The fuel_type feature has a fairly low MI score, but as we can see from the figure, it clearly separates
two price populations with different trends within the horsepower feature. This indicates that fuel_type
contributes an interaction effect and might not be unimportant after all. Before deciding a feature is
unimportant from its MI score, it's good to investigate any possible interaction effects -- domain
knowledge can offer a lot of guidance here.
"""
sns.lmplot(x="horsepower", y="price", hue="fuel_type", data=df);