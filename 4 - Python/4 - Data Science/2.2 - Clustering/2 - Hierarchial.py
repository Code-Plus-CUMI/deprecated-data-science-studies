"""
	
	****************************
	** Hierarchial Clustering **
	****************************

	Hierarchial cluster the datas and each cluster has a weight
that represents its position in a hierarchy between them.

-*-*-*-*-

	When creating this algorithm, you have to pay attention to three
parameters:

	/ n_clusters: number of Clusters (K)

	/ linkage: type of linkage in the hierarchy

	/ afinity: variation of the algorithm (Euclidean is the most
common).

-*-*-*-*-

	Besides, since Hierarchial clustering is sensitive to scale, it can
be a good idea RESCALE or NORMALIZE data with extreme values.
Our features are already roughly on the same scale, so we'll
leave them as-is.
"""

# ---- Importing Libraries ----
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt



# ---- Dendograms and Linkage Visualization ----
#
# 	With this visualization is possible to know how many
# clusters (n_clusters parameter) will best fit the algorithm
#
linkage_data = linkage(df, method='ward', metric='euclidean')
dendrogram(linkage_data)



# ---- Applying Hierarchial ----
hierarchical_cluster = AgglomerativeClustering(
	n_clusters=2
	, affinity='euclidean'
	, linkage='ward'
)

labels = hierarchical_cluster.fit_predict(df)



# ---- Plotting the Result ----
plt.scatter(x, y, c=labels)
plt.show()