import pandas as pd
import datetime
import numpy as np
np.random.seed(0)

"""
		** Parsing Dates **

Transforming 'objects' dtype into 'datetime' one.
"""

# Checking out the 'date' column
# of a imaginary dataset

df = pd.read_csv('filepath')

df['date'].head()
# > 01/05/99
# > 02/05/99
# > 03/05/99
# > 04/05/99
# > 05/05/99

df['date'].dtype
# > Object

####

# Formatting to:
#
# day/month/two-digit-year
# %d/%m/%y

df['formatted_date'] = pd.to_datetime(df['date']
									, format='%d/%m/%y')

df['formatted_date'].dtype
# > datetime64


# When the column has more than one date time format
# use 'infer_datetime_format=True' in order to pandas
# guess the correct format for each row
#
# - Problem 1: pandas can't recognize the correct format
# for all cases;
# - Problem 2: it takes more time than specifying the
# format by yourself
df['formatted_date'] = pd.to_datetime(df['date']
									, infer_datetime_format=True)

########

# Extracting information from the dates

df['formatted_date'].dt.day
# > 01
# > 02
# > 03
# > 04
# > 05

#######

# Checking out the Days Distribution in order
# to check if the pandas missformatted the months 
# as days
#
# See: "0 - Good Days Distribution.png" to an example
# of a correct distribution!!
sns.distplot(df['formatted_date'].dt.day
			, kde=False,
			, bins=31)