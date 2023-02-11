"""
- Exploratory Analysis Steps:

/ read datas with pandas
/ get the shape
/ get the describe method
/ split the datas into target (y) and features (X)
/ split the target and features variables into train and validation
/ treat missing values
/ check out the columns types and convert them if needed
/ convert categorical variables to numeric ones
/ check out for relationships and correlations (plots with matplotlib and seaborn)

"""

home_data = pd.read_csv('filepath')


# \ count >> number of rows with NON-MISSING values
# \ mean >> mean '-'
# \ std >> standard deviation (how spread the datas are)
# \ min, 25%, 50%, 75% and max >> percentiles 
#
# \ low outlier  <= Q1 - (1.5 * IQR)
# \ high outlier >= Q3 + (1.5 * IQR)

home_data.describe()

############


"""
- Scikit Learn Steps:

/ Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.

/ Fit: Capture patterns from provided data. This is the heart of modeling.

/ Predict: Just what it sounds like

/ Evaluate: Determine how accurate the model's predictions are.

Just a reminder: 'mean_absolute_error' is a loss function and it
measures how good the model is
"""

from sklearn.model_selection import train_test_split
from skelarn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Defining the target (y) and the feature (X) variables
y = home_data.Price

feature_names = ['Lot', 'Build Year', 'Rooms']
X = home_data[feature_names]

# Splitting up the variables into train and validation
train_X, val_X, train_y, test_y = train_test_split(X, y, random_state=1, test_size=0.3)

# Creating and training the model
home_model = DecisionTreeRegressor(random_state=1)
home_model.fit(train_X, train_y)

# Predicting and evaluating the model
predicted_values = home_model.predict(val_X)

print('First Five Predicted Values: ', predicted_values[0:5])
print('First Five Real Values: ', val_y.head().tolist())
print('\n')
print('Mean Absolute Error (MAE): ', mean_absolute_error(val_y, predicted_values))
print('Mean Squared Error (MSE): ', mean_squared_error(val_y, predicted_values) )

########

"""
Overfitting VS Underfitting

- Overfitting: the model makes good predictions in the training phase,
but makes poor predictions in the validation phase.
When using DecisionTreeRegressor, the model has a bunch of
leaves and a high depth in most cases.

- Underfitting: the model makes poor prediction in both training
and validation phases.
When using DecisionTreeRegressor, the model has a few leaves
and a low depth in most cases.

To avoid this, we can use the 'max_leaf_nodes' parameter in the
Decision Tree constructor and get some tests with different values
for this parameter.
"""

def get_mae(max_leaf, train_X, val_X, train_y, val_y):
	model = DecisionTreeRegressor(max_leaf_nodes=max_leaf
								  , random_state=1)
	
	model.fit(train_X, train_y)
	predicted_val = model.predict(val_X)
	mae = mean_absolute_error(val_y, predicted_val)
	
	return mae

for i in [5, 50, 500, 5000]:
	print(i)
	print(get_mae(i, train_X, val_X, train_y, val_y))
	print('\n')

# after making the test above, you will know which tree size
# (max_leaf_nodes) gives the lower MAE.
#
# So, you don't have the need to split the data into training
# validation anymore, which means you don't have the validation
# datas anymore and you can consider all the datas as training
# datas.

model = DecisionTreeRegressor(max_leaf_nodes=50
							, random_state=0)
model.fit(X, y)


#############

"""
A good alternative for the Decision Tree is the Random Forest
Regressor. This algorithm creates a bunch of Decision Tree, testing
with different numbers of leaves and returning the average result
between the trees.

This techinique helps a lot to minimize the overfitting and the
underfitting when compared to the Decision Tree
"""

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)

predicted_values = rf_model.predict(val_X)
mae = mean_absolute_error(val_y, predicted_values)

print("Random Forest Regressor's MAE: ", mae)

###########

# Random Forest Regressor accepts some parameters
# that can help you to get better results
#
# n_estimators >> number of Decision Trees
# min_samples_split >> how many leaves the Decision Trees will have
# max_depth >> how many subdivisions the Decision Tress will have
# criterion >> I can specify the Loss Function!!
# random_state >> always get the same result when running the model again
model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
model_3 = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0)
model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

models = [model_1, model_2, model_3, model_4, model_5]

##########

# Saving the Model

import pickle


model_filename = 'best_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model1, file)


# Loading the Saved Model
with open(model_filename, 'rb') as file:
    pickle_model = pickle.load(file)