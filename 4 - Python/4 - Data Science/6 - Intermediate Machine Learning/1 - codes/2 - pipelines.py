"""
* Always split the datas into train and test before to make
the preprocessing *

With Pipelines, you can make the preprocessing (Encode Categorical
Variables and Fill the Missing Values) with a few lines of code,
making your code cleaner and shorter.

Other advantages of the Pipelines uses:

/ Cleaner Code: Accounting for data at each step of preprocessing can
get messy. With a pipeline, you won't need to manually keep track 
of your training and validation data at each step.

/ Fewer Bugs: There are fewer opportunities to misapply a step or 
forget a preprocessing step.

/ Easier to Productionize: It can be surprisingly hard to transition 
a model from a prototype to something deployable at scale. 
We won't go into the many related concerns here, but pipelines can 
help.

/ More Options for Model Validation: Cross-validation.
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder

'''
** Strategy Parameter **

- If “mean”, then replace missing values using the mean along each 
column. Can only be used with numeric data.

- If “median”, then replace missing values using the median along each 
column. Can only be used with numeric data.

- If “most_frequent”, then replace missing using the most frequent 
value along each column. Can be used with strings or numeric data. 
If there is more than one such value, only the smallest is returned.

- If “constant”, then replace missing values with fill_value. 
Can be used with strings or numeric data.
'''

# Getting the Numerical and Categorical Columns #
numerical_cols = [col for col in df_train.columns
                  if df_train[col].dtype in ('int64', 'float64')]

categorical_cols = [col for col in df_train.columns
                    if df_train[col].dtype == 'object']

# Creating the Preprocessors #

# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='constant')

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

###########################

# Creating the Model #
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=0)

###########################

# Creating and Evaluating the Pipeline #
from sklearn.metrics import mean_absolute_error

# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('model', model)
                             ])

# Preprocessing of training data, fit model 
my_pipeline.fit(X_train, y_train)

# Preprocessing of validation data, get predictions
preds = my_pipeline.predict(X_valid)

# Evaluate the model
score = mean_absolute_error(y_valid, preds)
print('MAE:', score)