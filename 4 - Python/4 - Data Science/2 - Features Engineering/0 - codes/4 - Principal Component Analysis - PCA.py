"""
	
	**********************************
	** Principal Component Analysis **
	**********************************

Principal Component Analysis (PCA) is used to create new Features
combining other Features. In general, we get these new Features
by tracing diagonal lines (axes) over the scatter plot between the
two features we would like calculate the PCA.

After that, the model will calculate the correlation and the
variance between these two features and return the Components
(new Features).

{ image 4 }

Often, we can give names to these axes of variation. The longer
axis we might call the "Size" component: small height and small
diameter (lower left) contrasted with large height and large
diameter (upper right). The shorter axis we might call the "Shape"
component: small height and large diameter (flat shape)
contrasted with large height and small diameter (round shape).

Notice that instead of describing abalones by their 'Height'
and 'Diameter', we could just as well describe them by their
'Size' and 'Shape'. This, in fact, is the whole idea of PCA:
instead of describing the data with the original features, we
describe it with its axes of variation. The axes of variation
become the new features.

These new features are called the principal components of the
data. The weights themselves are called loadings. There will be
as many principal components as there are features in the
original dataset: if we had used ten features instead of two,
we would have ended up with ten components.

-*-*-*-*-

- PCA Best Practices:

	/ PCA only works with numeric features, like continuous
quantities or counts, so don't forget to Encode the Categorical
Features;

	/ PCA is sensitive to scale. It's good practice to standardize
your data before applying PCA, unless you know you have good
reason not to;

	/ Consider removing or constraining outliers, since they can
have an undue influence on the results;

-*-*-*-*-

- When to use PCA:

    / when the dataset has a bunch of features (data set compression);
    / when the features are multi-colinear (there's a significant 
number of linear correlations between them);
    / when our goal is to apply denoising;
"""

# 0 - Importing libraries, creating functions to plot PCA's
# Variances and to calculate Mutual Information (MI), and reading
# the dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression

def plot_variance(pca, width=8, dpi=100):

    # Create figure #
    fig, axs = plt.subplots(1, 2)
    n = pca.n_components_
    grid = np.arange(1, n + 1)

    # Explained variance #
    evr = pca.explained_variance_ratio_
    axs[0].bar(grid, evr)
    axs[0].set(xlabel="Component", title="% Explained Variance", ylim=(0.0, 1.0))

    # Cumulative Variance #
    cv = np.cumsum(evr)
    axs[1].plot(np.r_[0, grid], np.r_[0, cv], "o-")
    axs[1].set(xlabel="Component", title="% Cumulative Variance", ylim=(0.0, 1.0))

    # Set up figure #
    fig.set(figwidth=8, dpi=100)
    return axs

def make_mi_scores(X, y, discrete_features):
	mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores


df = pd.read_csv("../input/fe-course-data/autos.csv")

"""
We've selected four features that cover a range of properties.
Each of these features also has a high MI score with the target,
price. We'll standardize the data since these features aren't
naturally on the same scale.

We say that the features are not in the same scale when their
ratio are different in a highly way, such as: person's age and 
salary, while a person's age varies from 0 - 100, the salary can
vary between 1,000 - 1,000,000. There's a huge gap between them,
so we gotta scale the features in order to tthe model doesn't
think that salary is more important than age just because the values
are higher.
"""

# 1 - Setting up Target, setting up Features for PCA,
# and scaling the Features
features = ["highway_mpg", "engine_size", "horsepower", "curb_weight"]

X = df.copy()
y = X.pop('price')
X = X.loc[:, features]

X_scaled = (X - X.mean(axis=0)) / X.std(axis=0)


# 2 - Importing library, calculating PCA, and converting the
# results into a DataFrame
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

component_names = [f"PC{i+1}" for i in range(X_pca.shape[1])]
X_pca = pd.DataFrame(X_pca, columns=component_names)

X_pca.head()

# variance ratio
print(pca.explained_variance_ratio_)

# 3 - Getting the loadings (loadings are the variance and
# correlations between each component created)
loadings = pd.DataFrame(
    pca.components_.T,  # transpose the matrix of loadings
    columns=component_names,  # so the columns are the principal components
    index=X.columns,  # and the rows are the original features
)
loadings

# 4 - Plotting the Results
plot_variance(pca);

mi_scores = make_mi_scores(X_pca, y, discrete_features=False)
mi_scores

"""

{ image 4.1 }

This table of loadings is telling us that in the Size component,
Height and Diameter vary in the same direction (same sign), but
in the Shape component they vary in opposite directions (opposite
sign).

In each component, the loadings are all of the same magnitude
and so the features contribute equally in both.
"""