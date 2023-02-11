"""
	** Linear Regressions **

Equation:

	target = weight_1 * feature_1 + weight_2 * feature_2 + bias

/ weights >> regression coefficients
/ bias >> intercept (tells where the graph itercepts 
the y-axis)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plot_params = dict(
    color="0.75",
    style=".-",
    markeredgecolor="0.25",
    markerfacecolor="0.25",
    legend=False,
)

tunnel = pd.read_csv('filepath'
					, index_col='Day'
					, parse_dates=['Day'])

tunnel.index = pd.to_datetime(tunnel.index
							, format='%d/%m/%y'
							, format='%d/%m/%Y')

# By default, Pandas creates a `DatetimeIndex` with dtype `Timestamp`
# (equivalent to `np.datetime64`, representing a time series as a
# sequence of measurements taken at single moments. A `PeriodIndex`,
# on the other hand, represents a time series as a sequence of
# quantities accumulated over periods of time. Periods are often
# easier to work with
tunnel = tunnel.to_period()

########

"""
	1) Time-Step

Time-Step represents the length of the dataframe
which means, how many days are the datas from 
(in this case)
"""

# Creating a time-step feature
tunnel_df = tunnel.copy()
tunnel_df['Time-Step'] = np.arange(len(tunnel.index))

# Creating the Linear Model with the Time-Step
# With this, the equantion changes to:
#
# 	target = weight * time_step + bias
from sklearn.linear_model import LinearRegression

X = tunnel_df.loc[:, ['time']]
y = tunnel_df.loc[:, 'NumVehicles']

model = LinearRegression()
model.fit(X, y)
y_predictions = pd.Series(model.predict(X)
						, index=X.index)

# Plotting the Results
# and seeing the linear relationship
# of the # vehicles by time
ax = y.plot(**plot_params)
ax = y_predictions.plot(ax=ax, linewidth=3)
ax.set_title('Time Plot of Tunnel Traffic')

########

"""
	2) Lag

Lag represents the previous day/time data of a 
feature. When the previous day/time doesn't have
information, it's replaced by NaN
"""

# Creating the Lag
tunnel_df['Lag_1'] = tunnel_df['NumVehicles'].shift(1)

X = tunnel_df.loc[:, ['Lag_1']]
X.dropna(inplace=True) # drops the first row and the NaN others

y = tunnel_df.loc[:, ['NumVehicles']]
y, X = y.align(X, join='inner') # drop corresponding values in target


# Creating the Model
model = LinearRegression()
model.fit(X, y)
y_predictions = pd.Series(model.predict(X)
						, index = X.index)

# Plotting the Results
# and seeing the linear relationship
# of the # vehicles by time
ax = y.plot(**plot_params)
ax = y_predictions.plot(ax=ax, linewidth=3)
ax.set_title('Lag Plot of Tunnel Traffic')

ax = y.plot(**plot_params)
ax = y_pred.plot()