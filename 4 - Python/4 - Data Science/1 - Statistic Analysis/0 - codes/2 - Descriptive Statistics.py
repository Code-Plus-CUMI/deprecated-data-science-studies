#	****************************
#	** Descriptive Statistics **
#	****************************
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# ---- Measures of Center ----
# Number that describes the feature
# - arithmetic mean (when df does not have outliers)
# - median (when df has outliers)
# - mode (when feature is categorical)
#
# - OBS.: axis=0 (measures for each column), axis=1 (measures 
# for each row)
df.mean(axis=0)
df.median(axis=0)
df.mode(axis=0)



# ---- Measures of Spread ----
# Number that describes how data varies in a feature
# - range
# - quantiles
# - interquartile range
# - variance (when df does not have outliers)
# - standard deviation (when df does not have outliers)
# - standard error of the mean
# - median absolute deviation/mad (when df has outliers)
# - skewness
# - kurtosis
max(df['feature']) - min(df['feature'])
df['feature'].quantile(0) # 0, 0.25, 0.50, 0.75, 1
df['feature'].quantile(0.75) - df['feature'].quantile(0.25)
df['feature'].var()
df['feature'].std()
df['feature'].sem()
df['feature'].mad()
df['feature'].skew()
df['feature'].kurt()

# Skew Data: as close to 1, it meas that the distribution is skewed
# and we have to use the median and median absolute deviation to
# describes the feature. Decreased Order: [skewed, peaked,
# normal, uniform]

# Kurtosis Data: as higher the value, the more the datas as spread
# over the distribution tail rather than the center. Decreased Order:
# [peaked, skewed, normal, uniform]



# ---- Adding More Columns on Pandas Describe ----
# Just With Functions
# ---- Statistic Overview ----
def describe(df, stats):
    """
    Add statistics metrics to a DataFrame. Mean Absolute Deviation (MAD) is always added.
    
    Since the function 'mad' will become deprecated in the next pandas versions, MAD must be 
calculated manually.
    """
    
    # ---- Calculating the Common Describe ----
    common_describe = df.describe()
    
    # ---- Calculating Mean Absolute Deviation (MAD) ----
    mad_describe = lambda df: pd.DataFrame((df - df.mean()).abs().mean()).T.set_index(pd.Index(['mad']))
    mad_df = mad_describe(df)
    
    # ---- Calculating Other Statistics ----
    stats_df = df.reindex(df.columns, axis=1).agg(stats)
    
    # ---- Concatenating the Results ----
    return pd.concat([common_describe, mad_df, stats_df]).reindex(['count', 'mean', 'sem', 'var', 'std',  'median', 'mad', 'min',  '25%', '50%', '75%',  'max', 'skew',  'kurt'])

describe(df, ['median', 'var', 'skew', 'kurt', 'sem'])

df.mode()



# ---- Adding More Columns on Pandas Describe ----
# Make Your Own Calculations
def describe(df):
	return pd.concat([
		df.describe().T
		, df.sem().rename('sem')
		, df.var().rename('var')
		, df.median().rename('median')
		, abs(df.median() - df).median().rename('amd')		
		, df.skew().rename('skew')
		, df.kurt().rename('kurt')
		, max(df) - min(df).rename('range')
	], axis=1).T

describe(df)