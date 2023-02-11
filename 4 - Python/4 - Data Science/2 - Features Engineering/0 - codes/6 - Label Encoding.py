"""
	Label Encoding

OBS.: this a complement of "5 - Target Encoding.py" file.

Different than One-Hot and Ordinal Encoding, Label Encoding is applied
in the Target Feature, then:

	- One-Hot Encoding and Ordinal Encoding: applied in the Features
	- Label Encoding: applied in the Target
"""

import pandas as pd

# 0 - Creating DataFrame and seeparating Features from Target
df = pd.read_csv('blabla.csv')
X = df.copy()
y = X.pop('Target')

# 1 - Label Encoding
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
X['cat_feature'] = encoder.fit_transform(X['cat_feature'])