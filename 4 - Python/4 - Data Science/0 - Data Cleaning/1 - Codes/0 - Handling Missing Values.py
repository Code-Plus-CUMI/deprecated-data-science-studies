# read the dataset
# check out how many missing values we have per column
# check out the percentage of missing values per column
# check out the percentage of missing values in the dataset

"""
Is the missing values because it wasn't recorded or 
because it doesn't exist?

Answer: If a value is missing becuase it doesn't exist 
(like the height of the oldest child of someone who 
doesn't have any children) then it doesn't make sense 
to try and guess what it might be. 

These values you probably do want to keep as NaN. On the 
other hand, if a value is missing because it wasn't 
recorded, then you  can try to guess what it might have 
been based on the other values in that column and row. 
"""

# Counting the Missing Values and its Percentage #

import pandas as pd
import numpy as np
np.random.seed(0)

df = pd.read_csv('filepath')

# Counting how many missing values each column has
df.isnull().sum()

# Counting the percentage of the missing values
# for each column
df.isnull().sum() / len(df)
df.isnull().sum() * 100 / len(df)

# Counting the percentage of the missing values
# for the whole dataset
total_missing = df.isnull().sum().sum()
total_cells = np.product(df.shape)

percent_missing = (total_missing / total_cells) * 100