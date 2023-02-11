"""
	Time Series as Features

Cycles: the data shows irregular cycles 
instead of a regular seasonality, like the peak 
tends to occur around the new year, but sometimes 
earlier or later, sometimes larger or smaller.

In the other hand, Seasonality is wheen the 'cycles'
are regular, repeat in the same especific time of 
a year (for example) and the curves are in the same
proportion.

-*-*-*-*-

Example - Flu Trends
The Flu Trends dataset contains records of 
doctor's visits for the flu for weeks between 
2009 and 2016. Our goal is to forecast the number 
of flu cases for the coming weeks.

We will take two approaches. In the first we'll 
forecast doctor's visits using lag features. 
Our second approach will be to forecast doctor's 
visits using lags of another set of time series: 
flu-related search terms as captured 
by Google Trends
"""

# Importing Libraries #

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scipy.signal import periodogram
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statsmodels.graphics.tsaplots import plot_pacf

plot_params = dict(
    color="0.75",
    style=".-",
    markeredgecolor="0.25",
    markerfacecolor="0.25",
)

# Reading the dataset and plotting an overview #

flu_trends = pd.read_csv('filepath.csv')

flu_trends.set_index(
    pd.PeriodIndex(flu_trends.Week, freq="W"),
    inplace=True,
)

flu_trends.drop("Week", axis=1, inplace=True)

ax = flu_trends.FluVisits.plot(title='Flu Trends', **plot_params)
ax.set(ylabel="Office Visits")

# Adding Lags - 1 to 4 #

def make_lags(ts, lags):
    return pd.concat(
        {
            f'y_lag_{i}': ts.shift(i)
            for i in range(1, lags + 1)
        },
        axis=1)


X = make_lags(flu_trends.FluVisits, lags=4)
X = X.fillna(0.0)

# Creating the Model #
y = flu_trends.FluVisits.copy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=60, shuffle=False)

# Fit and predict
model = LinearRegression()  # `fit_intercept=True` since we didn't use DeterministicProcess
model.fit(X_train, y_train)
y_pred = pd.Series(model.predict(X_train), index=y_train.index)
y_fore = pd.Series(model.predict(X_test), index=y_test.index)


ax = y_train.plot(**plot_params)
ax = y_test.plot(**plot_params)
ax = y_pred.plot(ax=ax)
_ = y_fore.plot(ax=ax, color='C3')