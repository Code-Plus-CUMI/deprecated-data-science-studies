"""
0 - Scaling

It's used to change the RANGE of the datas. The RANGE
goes from 0 to 1.

----

About the models, you'll need to scale the datas when
you're using methods based on measures of how far apart 
data points are, like the models:
	
	/ Gradient Descent Optimization
	/ Support Vector Machines (SVM)
	/ K-Nearest Neighbors (KNN)
"""

from sklearn.preprocessing import MinMaxScaler

scaler_1 = MinMaxScaler()
scaler_1.fit_transform(df_train)
scaler_1.transform(df_val)

"""
1 - Standardization

It's like the Scale, but the scale range doesn't go
from 0 to 1, it varies.

----

About the models, you'll need to scale the datas when
you're using methods based on measures of how far apart 
data points are, like the models:
	
	/ Gradient Descent Optimization
	/ Support Vector Machines (SVM)
	/ K-Nearest Neighbors (KNN)
"""

from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler

# Robust Scaler >> Less Sensitive to Outliers
scaler_2 = RobustScaler()
scaler_2.fit_transform(df_train)
scaler_2.transform(df_val)

# Standard Scaler >> Used when the Mean is near to 0
scaler_3 = StandardScaler()
scaler_3.fit_transform(df_train)
scaler_3.transform(df_val)
"""
2 - Normalization

It's used to change the DISTRIBUTION of the data.

In a nutshell, Normalization just changes the distribution
of the datas in order to get a Normal Distribution
(Gaussian Distribution or Bell Curve).

----

About the models, you'll need to normalize the datas
when using:

	/ Linear Discriminant Analysis (LDA)
	/ Gaussian Naive Bayes

Tip: any method with "Gaussian" in the name probably 
needs that you normalize the datas.
"""

from sklearn.preprocessing import Normalizer

normalizer = Normalizer()
normalizer.fit_transform(df_train)
normalizer.transform(df_val)

#########

"""
		***********
		** Notes **
		***********

		Explanation Scale/Standardization

It's like to scale Real (R$) to Dollar (U$), where
1 dollar is equals 5 reals nowadays. So, if we don't
use the Scale, the model will consider 1 dollar equals
to 1 real, and that's not true.

Another example is the height and weight, where we gotta
scale the datas, like where 1 inch is equals 2.54 cm,
and 1 pound is equals 0.45 kg.

-*-*-*-*-

		Another Explanation Just to Get the Feeling

Scale, Standardization and Normalization avoid the model 
considers some features more important than others by 
the scale, like consider the salary (from 40,000 to 
210,000) more important than the age (from 18 to 100).
"""