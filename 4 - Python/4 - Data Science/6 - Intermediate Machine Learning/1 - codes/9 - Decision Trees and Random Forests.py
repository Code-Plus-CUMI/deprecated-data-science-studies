#	*****************************
#	** Machine Learning Models **
#	*****************************
#

import pandas as pd

from sklearn import preprocessing
from sklearn import metrics
from sklearn import tree # Decision Trees
from sklearn.ensemble import RandomForestClassifier # Random Forests

import graphviz # decision trees visualization

# ---- Decision Trees ----
#
# - Can be used for Regressions (DecisionTreeRegressor) and for
# Classifications (DecisionTreeClassifier)
#
# - Is a Tree with leafes. Each leaf is a if/else result using metrics
#

# Encoding Categorical Features
label_encoder = preprocessing.LabelEncoder()
encoded_sex = pd.DataFrame(label_encoder.fit_transform(df['Sex']))

# Training the Model
tree_model = tree.DecisionTreeClassifier()
tree_model.fit(
	X=encoded_sex
	, y=df['Survived']
)

# Visualizing the Decision Tree
dot_data = tree.export_graphviz(tree_model, out_file=None)
graph = graphviz.Source(dot_data)
graph

# Evaluating the Model
predictions = tree_model.predict_proba(X=encoded_sex)

female = predictions[df['Sex'] == 'female'][0][1]
male = predictions[df['Sex'] == 'male'][0][1]


print(f'Female Survival Prob: {female}')
print(f'Male Survival Prob: {male}')



# ---- Random Forests ----
#
# - Can be used for Regressions (RandomForestRegressor) and for
# Classifications (RandomForestClassifier)
#
# - It is a group of Decision Trees
#
# - Each Decision Tree receives a Bootstrap Sample of the training
# data, that is, receives a random percentage of the training data
#
# - The final score/result will be the Average Result of all
# Decision Trees results
#
# - The proper number of Decision Trees in a Random Forest is between
# 500 and 1000
#
# - The OOB Score uses the features that has not been used in a Bootstrap
# Sample to validate/evaluate the Decision Tree

# Encoding Categorical Features
label_encoder = preprocessing.LabelEncoder()
df['Sex'] = label_encoder.fit_trasnform(df['Sex'])

# Creating and Training the Model
features = ['Sex', 'Pclass', 'SibSp', 'Age', 'Fare']

rf_model = RandomForestClassifier(
	n_estimators=1000 # number of Decision Trees
	, max_features=2 # number of features considered in each Bootstrap Sample
	, oob_score=True # using the other features not considered in each Bootstrap Sample to evaluate the model
)

rf_modedl.fit(
	X=df[features]
	, y=df['Survived']
)

# Evaluating the Model - OOB Score
print(f'OOB Score: {rf_model.oob_score_}')


# Evaluating the Model - Feature Importances
for feature, importance in zip(features, rf_model.feature_importances_):
	print(f'{feature}: {importance}')


# Evaluating the Model - Confusion Matrix
metrix.confusion_matrix(
	y_true=df['Survived']
	, y_pred=predictions
)