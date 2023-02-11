"""
	Fit x Transform x Fit_Transform

- Fit: just calculates the MEAN and the STANDARD DEVIATION of the Features;
- Transform: transforms the Features;
- Fit_Transform: it's the "Fit" and "Transform" methods together

Examples:
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_valid, y_train, y_valid = train_test_split(
	X, y
	, train_size=0.7
	, test_size=0.3
	, random_state=42
)

# 0 - Using Fit and Transform
transformer = StandardScaler()
fit = transformer.fit(X_train)

X_train_scaled = fit.transform(X_train)
X_valid_scaled = fit.transform(X_valid)

# 1 - Using Fit_Transform
transformer = StandardScaler()

X_train_scaled = transformer.fit_transform(X_train) 
X_valid_scaled = transformer.fit_transform(X_valid)