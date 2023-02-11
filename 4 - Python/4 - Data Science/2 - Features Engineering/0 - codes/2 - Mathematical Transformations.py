"""

	**********************************
	** Mathematical Transformations **
	**********************************

1) Log and Power Functions

Log Functions are used to reshape features' distributions in order
to make it easier to the model learn.

Example: The distribution of WindSpeed in US Accidents is highly
skewed (image 2). In this case the logarithm is effective at
normalizing it.
"""

# If the feature has 0.0 values, use 'np.log1p' -> 'log(1+x)'
# instead of 'np.log'
accidents["LogWindSpeed"] = accidents.WindSpeed.apply(np.log1p)

# Plot a comparison
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
sns.kdeplot(accidents.WindSpeed, shade=True, ax=axs[0]) # old
sns.kdeplot(accidents.LogWindSpeed, shade=True, ax=axs[1]); # new

"""

2) Group Transformations

Other way to create new features using Math is applying Group
Transformations, which means, we group the rows by columns
and do some calculations using the Pandas pre-build function
'transform'.
"""
customer["AverageIncome"] = (
    customer.groupby("State")  # for each state
    ["Income"]                 # select the income
    .transform("mean")         # and compute its mean
)

X_5["MedNhbdArea"] = (
	df.groupby("Neighborhood")
	["GrLivArea"]
	.transform("median")
)