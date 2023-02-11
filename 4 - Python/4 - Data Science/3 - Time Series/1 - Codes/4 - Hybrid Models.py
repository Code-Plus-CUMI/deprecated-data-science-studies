"""
	Hybrid Models

Hybrid Models is a technique to use different
ML algorithms to forecast series. Which means,
instead of using just one algorithm to learn
all the series' components, we use one algorithm
to learn one component and so on.

-*-*-*-*-

Series = Trends + Seasons + Cycles + Errors

	Series >> Result
	Trends, Seasons, Cycles and Errors >> Components
"""

model_1.fit(X_train_1, y_train)
y_pred_1 = model_1.predict(X_train_1)

model_2.fit(X_train_2, y_train - y_pred_1)
y_pred_2 = model_2.predict(X_train_2)

y_pred = y_pred_1 + y_pred_2