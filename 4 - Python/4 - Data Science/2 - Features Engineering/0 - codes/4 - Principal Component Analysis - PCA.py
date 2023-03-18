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

{ image 1.0 }

    These new features are called the principal components of the
data. The weights themselves are called loadings. There will be
as many principal components as there are features in the
original dataset: if we had used ten features instead of two,
we would have ended up with ten components.
"""

# ---- Importing Libraries and Defining Functions ----
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression
from sklearn.decomposition import PCA

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

# ---- Reading DataSet and Treating the Features ----
df = pd.read_csv("../input/fe-course-data/autos.csv")
features = ["highway_mpg", "engine_size", "horsepower", "curb_weight"]

X = df.copy()
y = X.pop('price')
X = X.loc[:, features]

X_scaled = (X - X.mean(axis=0)) / X.std(axis=0)


# ---- Calculating PCA ----
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)
component_names = [f"PC{i+1}" for i in range(X_pca.shape[1])]
X_pca = pd.DataFrame(X_pca, columns=component_names)

X_pca.head()
print(pca.explained_variance_ratio_) # variance ratio

# ---- Getting the Loadings ----
#
# \ loadings are the variance and correlations between each
# created component
loadings = pd.DataFrame(
    pca.components_.T,  # transpose the matrix of loadings
    columns=component_names,  # so the columns are the principal components
    index=X.columns,  # and the rows are the original features
)
loadings

# ---- Calculating Mutual Info Scores and Plotting the Results ----
mi_scores = make_mi_scores(X_pca, y, discrete_features=False)
mi_scores

plot_variance(pca);

"""

{ image 1.1 }

This table of loadings is telling us that in the Size component,
Height and Diameter vary in the same direction (same sign), but
in the Shape component they vary in opposite directions (opposite
sign).

In each component, the loadings are all of the same magnitude
and so the features contribute equally in both.
"""