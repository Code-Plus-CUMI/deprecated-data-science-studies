"""
	Stats Model (OLS) - Linear Regression

Stats Model is used to display useful information about a Linear
Regression Model (to know when to usee Linear Regression Models, use
pandas.corr() to check out for any Linear Relationships).
"""

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 0 - Creating the Model
linear_model = LinearRegression(n_jobs=4)
linear_model.fit(X_train, y_train)
predictions = linear_model.predict(X_valid)

# 1 - Plotting the Result
plt.scatter(y_valid, predictions) # predictions
plt.plot(y_valid, y_valid, 'r')   # real target values

# 2 - Cross Validation
from sklearn.model_seleciont import cross_val_score

cv_scores = cross_val_score(linear_model, X, y, cv=5)
print('Average 5-Fold CV Score:', np.mean(cv_scores).round(4))

# 3 - Checking out the Regression
import statsmodels.api as sm

X1 = sm.add_constant(X) # X is the whole Feature Dataset
results = sm.OLS(y, X1).fit()
results.summary()
print(results.summary())

"""
- R-squared : the coefficient of determination. It is the proportion of the variance in the dependent variable that is predictable/explained
- Adj. R-squared : Adjusted R-squared is the modified form of R-squared adjusted for the number of independent variables in the model. Value of adj. R-squared increases, when we include extra variables which actually improve the model.
- F-statistic : the ratio of mean squared error of the model to the mean squared error of residuals. It determines the overall significance of the model.
- coef : the coefficients of the independent variables and the constant term in the equation.
- t : the value of t-statistic. It is the ratio of the difference between the estimated and hypothesized value of a parameter, to the standard error
"""
coef = linear_model.coef_
intercept = linear_model.intercept_

y = coef * x[i] - intercept