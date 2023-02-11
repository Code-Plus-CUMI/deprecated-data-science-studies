"""
* Always split the datas into train and test before to make
the preprocessing *

- Treating Categorical Variables:

1 - Drop Categorical Variables Columns

/ this technique is suggested to be done when these
columns doesn't have important information to the model.
So, dropping them wouldn't affect our model's results

/ this technique normally works worse than the others
"""

reduced_df_train = df_train.select_dtypes(exclude=['object'])
reduced_df_valid = df_valid.select_dtypes(exclude=['object'])

"""
2 - Ordinal Encoder

/ this technique transforms each possible categorical values
to a number;

/ also, it applies some hierarchy between the values: as higher
the number that represents a value is, the more important is the
categorical value
"""

from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder()

# Getting the Categorical Variable Columns
object_cols = [col for col in df_train.columns
				if df_train[col].dtype == 'object']

# Encoding the columns
label_df_train = df_train.copy()
label_df_valid = df_valid.copy()

label_df_train[object_cols] = pd.DataFrame(encoder.fit_transform(df_train[object_cols]))
label_df_valid[object_cols] = pd.DataFrame(encoder.transform(df_valid[object_cols]))

"""
Some times we can stumble upon with this problem:

- The train dataset has some categorical values (classes)
that the validation one doesn't. For example:

	train dataset color classes       = red, green, blue
	validation dataset color classes  = red, yellow, blue, green

- The train one doesn't have the 'yellow' class, so, when
we try to encode this column, we will get an error;

- One option is to drop all of the columns that have the problem.
"""

# Getting the Categorical Columns
object_cols = [col for col in df_train.columns
				if df_train[col].dtype == 'object']

# Columns that can be safely ordinal encoded
good_label_cols = [col for col in object_cols
					if set(df_valid[col]).issubset(set(df_train[col]))]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))

# Drop categorical columns that will not be encoded
label_df_train = df_train.drop(bad_label_cols, axis=1)
label_df_valid = df_valid.drop(bad_label_cols, axis=1)

# Encoding
label_df_train[object_cols] = pd.DataFrame(encoder.fit_transform(label_df_train[object_cols]))
label_df_valid[object_cols] = pd.DataFrame(encoder.transform(label_df_valid[object_cols]))

"""
3 - One-hot Encoding

/ this technique is suggested to be applied when the categorical
variables has less than 10 possible values AND there are not a
hierarchy between them

/ it's recommended to use this techinique with cattegorical
variables up to 10 possible values because One-Hot Encoding
adds a new column to each possible value, so, there is a high
probability to the dataframe gets too much 'datas'

/ when creating the One-hot class, we have two parameters to set:

	- handle_unknown: ignore >> avoid errors when the validation
	dataset contains classes (categorical values) that are not
	represented in the training one

	- sparse: False >> returns a numpy array. True >> returns a
	sparse matrix

/ this technique normally works better thant the others
"""

from sklearn.preprocessing import OneHotEncoder

OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

# Getting all the object columns
object_cols = [col for col in df_train.columns
				if df_train[col].dtype == 'object'
				   and df_train[col].nunique < 10]

# Encoding the columns
OH_train_cols = pd.DataFrame(OH_encoder.fit_transform(df_train[object_cols]))
OH_valid_cols = pd.DataFrame(OH_encoder.transform(df_valid[object_cols]))

# One Hot Encoding removes the index, so we have to get
# them back
OH_train_cols.index = df_train.index
OH_valid_cols.index = df_valid.index

# Removing the Categorical Columns from the dataset
numerical_df_train = df_train.drop(object_cols, axis=1)
numerical_df_valid = df_valid.drop(object_cols, axis=1)

# Adding the One Hot Encoded Columns in the Dropped
# Categorical Columns

OH_df_train = pd.concat([numerical_df_train, OH_train_cols], axis=1)
OH_df_valid = pd.concat([numerical_df_valid, OH_valid_cols], axis=1)


"""
Example of how to check out how many classes a Categorical Variable
has. Remember that it's good to use One-Hot Encoding with Categorical
Columns that have less than 10 classes
"""

# Get number of unique entries in each column with categorical data
object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
d = dict(zip(object_cols, object_nunique))

# Print number of unique entries by column, in ascending order
sorted(d.items(), key=lambda x: x[1])

# Getting all the object columns that have less
# than 10 classes
object_cols = [col for col in df_train.columns
				if df_train[col].dtype == 'object'
				   and df_train[col].nunique() < 10]