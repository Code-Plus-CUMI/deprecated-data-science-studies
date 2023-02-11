"""
	0 - Reading the File and Splitting it up
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('filepath') # if needed, we can solve the charset problem here
df.dtype() # if needed, we can convert some columns here (datetime, int64 or float64)

y = df.Price
X = df.drop(['Price'], axis=1)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=0
													, train_size=0.80
													, test_size=0.20)

"""
	1 - Separating the Numerical from the Categorical Features
"""

num_cols = [col for col in X_train.columns
			if X_train[col].dtype in ['int64', 'float64']]

cat_ord_cols = [col for col in X_train.columns
				if X_train[col].dtype == 'object'
				   and X_train[col].nunique() >= 10]

cat_oh_cols = [col for col in X-train.columns
				if X_train[col].dtype == 'object'
				   and X_train[col].nunique() < 10]

"""
	2 - Checking out for Inconsistent Data Entry

/ in this example, I'm checking out the 'Countries'
column only, however, in a real world analysis, I must
do to every categorical one!!
"""

import fuzzywuzzy
from fuzzywuzzy import process

# Getting the Unique Countries

train_countries = X_train['Countries'].unique()
train_countries.sort()
print(train_countries)

valid_countries = X_valid['Countries'].unique()
valid_countries.sort()
print(valid_countries)

# Getting the Matches to the Unique Countries

train_matches = fuzzywuzzy.process.extract('country_1'
										  , train_countries
										  , limit=10
										  , scorer=fuzzywuzzy.fuzz.token_sort_ratio)
print(train_matches)

valid_matches = fuzzywuzzy.process.extract('country_1'
										  , valid_countries
										  , limit=10
										  , scorer=fuzzywuzzy.fuzz.token_sort_ratio)
print(valid_matches)

# Creating Function to Deal with the Incoonsistent Entries

def replace_matches_in_column(df, column, string_to_match
							 , min_ratio):
	
	# getting list of strings and the matches
	strings = df[column].unique()
	matches = fuzzywuzzy.process.extract(string_to_match
										, strings
										, limit=10
										, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

	# getting the most similar matches
	close_matches = [matche[0] for matche in matches
					 if matche[1] >= min_ratio]

	# getting the rows with the close matches
	# and replacing them
	rows_with_matches = df[column].isin(close_matches)
	df.loc[rows_with_matches, column] = string_to_match

	# success log
	print('All done with ', string_to_match, ' matche!')

# Calling the function
replace_matches_in_column(X_train, 'Countries'
						 , 'country_1', 75)

replace_matches_in_column(X_valid, 'Countries'
						 , 'country_1', 75)

"""
	3 - Getting the Good Labels and Bad Labels
	in Ordinal and One-Hot Categorical Variables
	and Dropping the Bad Ones
"""

# Getting the Good and Bad Labels
good_labels_ord_cols = [col for col in cat_ord_cols
						if set(X_valid[col]).issubset(set(X_train[col]))]

bad_labels_ord_cols = list(set(cat_ord_cols) - set(good_labels_ord_cols))


good_labels_oh_cols = [col for col in cat_oh_cols
					   if set(X_valid[col]).issubset(set(X_train[col]))]						

bad_labels_oh_cols = list(set(cat_oh_cols) - set(good_labels_oh_cols))

# Dropping the Bad Labels
good_labels_X_train = X_train.drop(bad_labels_ord_cols, axis=1).copy()
good_labels_X_train = good_labels_X_train.drop(bad_labels_oh_cols, axis=1)

good_labels_X_valid = X_valid.drop(bad_labels_ord_cols, axis=1).copy()
good_labels_X_valid = good_labels_X_valid.drop(bad_labels_oh_cols, axis=1)

"""
	4 - Pipelines and Preprocessing

/ Scaling: It's used to change the RANGE of the datas. 
The RANGE goes from 0 to 1.

/ Standardization: It's like the Scale, but the scale 
range doesn't go from 0 to 1, it varies.	

/ Normalization: changes the distribution of the datas 
in order to get a Normal Distribution (Gaussian 
Distribution or Bell Curve).
"""

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

# Numerical Variables Preprocessing
#
# / Imputer (strategy: mean|most_frequent|median|constant)
# / Scale | Standardization | Normalization (uncomment the code to change the preprocessing)

numerical_transformer = Pipeline(steps=[
	('imputer', SimpleImputer(strategy='mean')),
	('scale', MinMaxScaler()),
	#('standardization', StandardScaler()),
	#('robustscaler', RobustScaler()),
	#('normalization', Normalizer()),
])


# Ordinal Categorical Preprocessor
#
# / Imputer (strategy: most_frequent|constant)
# / Ordinal Encoder

cat_ord_transformer = Pipeline(steps=[
	('imputer', SimpleImputer(strategy='most_frequent')),
	('ordinal_encoder', OrdinalEncoder()),
])


# One-Hot Categorical Preprocessor
#
# / Imputer (strategy: most_frequent|constant)
# / One-Hot Encoder (handle_unknown=ignore, sparse=False)

cat_oh_transformer = Pipeline(steps=[
	('imputer', SimpleImputer(strategy='most_frequent')),
	('oh_encoder', OneHotEncoder(handle_unknown='ignore', sparse=False)),
])

"""
	5 - Bundling the Preprocessors
"""

from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
	transformers=[
		('num', numerical_transformer, num_cols),
		('ord_cat', cat_ord_transformer, good_labels_ord_cols),
		('oh_cat', cat_oh_transformer, good_labels_oh_cols),
	]
)

"""
	6 - Creating the Model and Getting the First Results
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Creating the Model and the Pipeline
model = RandomForestRegressor(n_estimators=250
							 , random_state=0)

pipeline = Pipeline(steps=[
	('preprocessor', preprocessor),
	('model', model),
])

# Training and Predicting
pipeline.fit(good_labels_X_train, y_train)
predictions = pipeline.predict(good_labels_X_valid)

# Getting the Score
mae = mean_absolute_error(predictions, y_valid)
print('MAE: ', mae)

"""
	7 - Getting Best Results with Cross-Validation
"""

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(pipeline,
							 , good_labels_X_train.concat(good_labels_X_valid)
							 , y
							 , cv=5
							 , score='neg_mean_absolute_error')

print('Average MAE Score (Across Experiments):', scores.mean())

"""
	8 - Testing XGBoost out too
"""

from XGBoost impot XGBRegressor

xgb_model = RGBRegressor(n_estimators=500
						, learning_rate=0.05
						, n_jobs=4)

xgb_model.fit(good_labels_X_train, y_train
			 , early_stopping_rounds=5
			 , eval_set=[(good_labels_X_valid, y_valid)]
			 , verbose=False)

xgb_predictions = xgb_model.predict(good_labels_X_valid)
mae = mean_absolute_error(xgb_predictions, y_valid)

print('MAE: ', mae)