"""
	
	*************************************************
	** t-Distributed Stochastic Neighbor Embedding **
	*************************************************

	Suppose we had a dataset composed of 3 distinct classes
in a 2D plot and we want to convert it to a 1D plot maintaining
the differences and distances between each cluster.

	{ image 2.0 }
	{ image 2.1 }
"""

# ---- Import Libraries ----
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TNSE

# ---- Applying t-SNE ----
#
# \ n_components: number of compoennts / dimensions
#
# \ verbose: logger (1 >> true / 0 >> false)
#
# \ perplexity: number of nearest neighbors that is used
# to Manifold Learning Algorithms. This value should be fine
# between 5 and 50 and as larger the DataSet is, the larger
# its value should be
#
# \ n_iter: number of iterations to run the algorithm's process
# of learning
#

tsne = TSNE(n_components=2, verbose=0, perplexity=40, n_iter=300)
X_tsne = tsne.fit_transform(data_subset)
X_tsne.head()


# ---- Plotting the Result ----
palette = sns.color_palette("bright", 10)

sns.scatterplot(
	X_tsne[:,0]
	, X_tsne[:,1]
	, hue=y
	, legend='full'
	, palette=palette
)