"""
* Always split the datas into train and test before to make
the preprocessing *

- Treating Missing Values:

1 - Drop the Columns or Rows with missing values

/ This techniquee is not so much good because your dataset
will lose some information that can be very useful to train
the model.
"""

# Dropping Columns #

cols_missing_values = [col for col in df_train.columns
						  if df_train[col].isnull().any()]

df_train.drop(cols_missing_values, axis=1, inplace=True)
df_val.drop(cols_missing_values, axis=1, inplace=True)

# Dropping Rows #

df_train.dropna(inplace=True)
df_test.dropna(inplace=True)

"""
2 - Imputation

/ This method is one of the best because the missing values
are replaced by the mean of the column.

/ Notice that how we use the mean, this method is just valid
for numeric variables or categorical variables that have been
labelled
"""

from sklearn.impute import SimpleImputer

imputer = SimpleImputer()

imputed_df_train = pd.DataFrame(imputer.fit_transform(df_train))
imputed_df_val = pd.DataFrame(imputer.transform(df_val))

# Imputation removes the columns' names, so we have to get
# them back

imputed_df_train.columns = df_train.columns
imputed_df_val.columns = df_val.columns

"""
3 - Extended Imputation

/ the missing values are replaced by the mean of the column
and a new column is added into the dataframe for each column
containing missing values.

/ these new columns just store boolean values informing whether
the row has been imputed (TRUE) or hasn't (FALSE)
"""

# Copying the datasets
df_train_plus = df_train.copy()
df_val_plus = df_val.copy()

# Getting columns with missing values
cols_missing_values = [col for col in df_train.columns
					   if df_train[col].isnull().any()]

# Adding new columns to indicate imputation
# and setting the values
for col in cols_missing_values:
	df_train_plus[col + 'was_missing'] = df_train_plus[col].isnull()
	df_val_plus[col + 'was_missing'] = df_val_plus[col].isnull()

# Making the imputation
imputation = SimpleImputer()

df_train_plus = pd.DataFrame(imputer.fit_transform(df_train_plus))
df_val_plus = pd.DataFrame(imputer.transform(df_val_plus))

# Getting the columns names
df_train_plus.columns = df_train.columns
df_val_plus.columns = df_val.columns