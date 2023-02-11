"""
	Trends

Trends are slow and long term changes in the plot
along the time. This change can be positive 
(increasing), negative (decreasing) or both
(increasing in one part and decreasing in another
one).

To calculate the shape of the trend line, we usually
plot all the points in a plot, get a window (like 12
points at a time) and calculate the average between
them. After calculating all averages, we just fit
the line over them.

A visualization of how it works is in 'images'
folder (image 0).
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Reading the Dataset
tunnel = pd.read_csv('filepath'
					, parse_dates=['Day']
					index_col='Day')

tunnel = tunnel.to_period()

# Creating the Moving Window
#
# as far we have datas along the years, the window
# will take 365 datas/days in other to get the
# trend line by year
moving_average = tunnel.rolling(
	window=365, # 365 days
	center=True, # puts the average at the center of the window
	min_periods=183, # half of the window value
).mean() # gets the 'mean'. You can change it to 'median, min, max, std...'

ax = tunnel.plot(style='.', color=0.5)

moving_average.plot(
	ax=ax, linewidth=3, legend=False,
	title='Tunnel Trafic - 365-Day Moving Average'
)

#######

"""
n Lesson 1, we engineered our time dummy in Pandas 
directly. From now on, however, we'll use a 
function from the statsmodels library called 
'DeterministicProcess'. 

Using this function will help us avoid some 
tricky failure cases that can arise with time 
series and linear regression. 

The order argument refers to polynomial order: 
	/ 1 for linear 
	/ 2 for quadratic
	/ 3 for cubic
	/ and so on...
"""

from statsmodel.tsa.deterministic import DeterministicProcess

dp = DeterministicProcess(
	index=tunnel.index, # dates from the training data
	constant=True, # dummy feature for the bias (y_intercept)
	order=1, # linear relationship (the trend)
	drop=True, # drops terms if neecessary to avoid collinearity
)

# Creating the Model
from sklearn.linear_model import LinearRegression

# `in_sample` creates features for the dates 
# given in the `index` argument
X = dp.in_sample()
X_forecast = dp.out_of_sample(steps=30)
y = tunnel['NumVehicles']

# the 'fit_intercept' removes duplicated dates
model = LinearRegression(fit_intercept=False)
model.fit(X,y)

y_predictions = pd.Series(model.predict(X), index=X.index)
y_forecast = pd.Series(model.predict(X_forecast), index=X_forecast.index)

# Plotting
ax = tunnel.plot(
	style=".", color="0.5", 
	title="Tunnel Traffic - Linear Trend",
	label='Sales'
)

y_pred.plot(ax=ax, linewidth=3, label="Trend")
y_forecast.plot(ax=ax, linewidth=3, label='Forecast')

# An alternative way of using 'sklearn Linear Regression'
# is using the 'Earth' model from 'pyearth'
from pyearth import Earth

model = Earth()
model.fit(X,y)

y_pred = pd.Series(model.predict(X), index=X.index)

ax = y.plot(style='.', color=0.5, label='Sales'
			, title='Bla bla bla')

y_pred.plot(ax=ax, linewidth=3, label='Forecasting')