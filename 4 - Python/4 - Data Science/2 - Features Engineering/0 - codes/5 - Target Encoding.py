"""
	
	*********************
	** Target Encoding **
	*********************

Target Encoding, like One-Hot and Ordinal Encoding, is applied
in the Categorical Features in other to transform them into numbers.
However, differently than these two techniques, Target Encoding
uses the Target as a parameter to encode the Categorical Features.

-*-*-*-*-

Use Cases for Target Encoding

	/ High-Cardinality Features: a feature with a large number
of categories can be troublesome to encode - a one-hot encoding
would generate too many features and alternatives, like a label
encoding, might not be appropriate for that feature. A target
encoding derives numbers for the categories using the feature's
most important property: its relationship with the target;

	/ Domain-Motivated Features: from prior experience, you might
suspect that a categorical feature should be important even if
it scored poorly with a feature metric. A target encoding can
help reveal a feature's true informativeness;
"""

"""
	0 - Mean Encoding

	AKA: Bin Counting, Likelihood Encoding, Impact Encoding and
Leave-One-Out Encoding.

	Groups the Features bu another one, selects a Feature and
Calculate the their Mean.
"""

autos['make_encoded'] = (
	autos.groupby('make') # for each make
	['price']             # select the 'price'
	.transform('mean')    # and calculate price's mean
)

"""

	1 - Smoothing

An encoding like the Mean One presents a couple of problems, however.

	/ Unknown Categories: target encodings create a special risk of
overfitting, which means they need to be trained on an independent
"encoding" split. When you join the encoding to future splits,
Pandas will fill in missing values for any categories not present
in the encoding split. These missing values you would have to
impute somehow;

	/ Rare Categories: when a category only occurs a few times in
the dataset, any statistics calculated on its group are unlikely
to be very accurate. In the Automobiles dataset, the mercurcy make
only occurs once. The "mean" price we calculated is just the price
of that one vehicle, which might not be very representative of any
Mercuries we might see in the future. Target encoding rare
categories can make overfitting more likely;

-*-*-*-*-

A solution to these problems is to add SMOOTHING. The idea is to
blend the in-category average with the overall average. Rare
categories get less weight on their category average, while
missing categories just get the overall average:

	encoding = weight * in_category + (1 - weight) * overall

Where weight is a value between 0 and 1 calculated from the
category frequency. An easy way to determine the value for
weight is to compute an m-estimate:

	weight = n / (n + m)

Where n is the total number of times that category occurs
in the data. The parameter m determines the "smoothing factor".
Larger values of m put more weight on the overall estimate.
"""

"""
----

Example:
"""

# 0 - Importing libraries and reading dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("../input/fe-course-data/movielens1m.csv")
df = df.astype(np.uint8, errors='ignore') # reduce memory footprint
print("Number of Unique Zipcodes: {}".format(df["Zipcode"].nunique()))

"""
With over 3000 categories, the Zipcode feature makes a good
candidate for target encoding, and the size of this dataset
(over one-million rows) means we can spare some data to create
the encoding.

We'll start by creating a 25% split to train the target encoder.
"""

# 1 - Setting up Features and Target, splitting dataset into
# Target Encoding's Train and Pretrain
X = df.copy()
y = X.pop('Rating')

X_encode = X.sample(frac=0.25)
y_encode = y[X_encode.index]
X_pretrain = X.drop(X_encode.index)
y_train = y[X_pretrain.index]

# 2 - Importing library, creating and training the encoder,
# and encoding the dataset
from category_encoders import MEstimateEncoder

encoder = MEstimateEncoder(cols=["Zipcode"], m=5.0) # 'm' is used to control the noisy
encoder.fit(X_encode, y_encode)

X_train = encoder.transform(X_pretrain)