#	*****************************
#	** Machine Learning Models **
#	*****************************
#

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression


# ---- Linear Regression ----
#
# - Used to predict Regressions
#
# - It is the simplest Regression Model Algorithm
#
# - Equation: y = a + b * x
# \ y >> dependent variable
# \ a >> intercept
# \ b >> coefficient
# \ x >> independent variable
#
lin_m = LinearRegression()
lin_m.fit(X_train, y_train)
predictions = lin_m.predict(X_valid)

# ---- Logistic Regression ----
#
# - Used to predict Binary Classes
#
# - It is the simples Classification Model Algorithm
#
# - Equation: y = 1 / (1 + e^(-1 * (a + b * x)))
# \ y >> dependent variable
# \ e >> Plank's Constant
# \ a >> intercept
# \ b >> coefficient
# \ x >> independent variable
#
# - This equation converts the Linear Regression Results to a range
# between 0 and 1. 
#
log_m = LogisticRegression()
log_m.fit(X_train, y_train)
predictions = log_m.predict_proba(X_valid)