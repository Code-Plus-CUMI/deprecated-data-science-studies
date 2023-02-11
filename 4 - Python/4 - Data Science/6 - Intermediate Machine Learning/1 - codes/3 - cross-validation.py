"""
* Always split the datas into train and test before to make
the preprocessing *

Cross-Validation is used to test different folders/groups
of train and validation datasets in order to get the best
resultt with the best combination of train and validation
datasets.

If a dataset is folded in 5 groups, the model will process five
times, using different one part as the validation dataset for each 
time.

Besides, Cross-Validation can take a considerable amount of time
if the dataset is big enough. So, before using this technique,
consider this:

- For small datasets: where extra computational burden isn't a 
big deal, you should run cross-validation.

- For larger datasets: a single validation set is sufficient. 
Your code will run faster, and you may have enough data that 
there's little need to re-use some of it for holdout.

Alternatively, you can run cross-validation and see if the scores
for each experiment seem close. If each experiment yields the same
result, a single validation set is probably sufficient.
"""

# Creating the Pipeline #
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(
  steps=[
    ('preprocessor', SimpleImputer())
    , ('model', RandomForestRegressor(n_estimators=50, random_state=0))
  ]
)


# Calculating the Cross-Validation #
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold, StratifiedKFold \
, LeaveOneOut, LeavePOut, ShuffleSplit

k_folds = KFold(n_splits=5) # common k fold
sk_folds = StratifiedKFold(n_splits=5) # to apply when there's a chance to have imbalanced classes
loo = LeaveOneOut() # leaves a single row in the validation dataset (repeats the process in order to make all rows be into validation dataset once)
lpo = LeavePOut(p=50) # it's like LeaveOneOut, but you can set the number of rows to be into the validation dataset
shuffle_split = ShuffleSplit(
  train_size=0.6
  , test_size=0.3
  , n_splits=5
) # you set the percentage of train and validation dataset. The remaining will be discarded over the Cross-Validation Step

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(
  my_pipeline, X, y
  , cv=k_folds
  , scoring='neg_mean_absolute_error'
)

print("Average MAE score (across experiments):", scores.mean())