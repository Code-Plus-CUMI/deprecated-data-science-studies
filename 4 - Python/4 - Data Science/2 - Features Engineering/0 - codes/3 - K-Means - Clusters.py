"""

	************************
	** K-Means - Clusters **
	************************

K-Means is used to the model groups the datas into Groups/Clusters
and ake the learning and prediction easier to the main model.

In the process, K-Means defines CENTROIDS and it's goal is to find
the perfect position for each centroid and its territory 
(TESSALATION).

When creating this algorithm, you have to pay attention to three
parameters:

	/ n_clusters: number of Clusters (K)

	/ max_iter: number of iterations

	/ n_init: gets the Centroids' Position has the least total
distance between each point and its centroid, the optimal 
clustering.

Besides, since k-means clustering is sensitive to scale, it can
be a good idea rescale or normalize data with extreme values.
Our features are already roughly on the same scale, so we'll
leave them as-is.
"""

# 0- Importing libraries, reading dataset, 
# and defining the Features for K-Means
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('filepath')
X = df.loc[:, ['Latitude', 'Longitude', 'MedInc']]

# 1 - Checking out how many clusters is great to the Clustering
from sklearn.cluster import KMeans

wcss = []

# testing out with 1 to 11 clusters
for i in range(1, 11):

    # n_clusters >> number of clusters to be identified
    # max_iter   >> number of iterations for each run (n_init)
    # n_init     >> number of runs (centroids iteration)
    kmeans = KMeans(n_clusters=i,
    				init='k-means++',
    				max_iter=300,
    				n_init=10,
    				random_state=0)

    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# plotting the results (we often choose the amount
# of clusters where the WCSS starts to level off -
# elbow method)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# 2 - Using K-Means (consider that 4 clusters
# was the great amount and we will repeat the
# K-Means centroids moviment 10 times)

#kmeans = KMeans(n_clusters=4, n_init=10, max_iter=300)
kmeans = KMeans(n_clusters=4,
    			init='k-means++',
    			max_iter=300,
    			n_init=10,
    			random_state=0)

X['Cluster'] = kmeans.fit_predict(X)
X['Cluster'] = X['Cluster'].astype('category')

# 3 - Plotting the Results
sns.relplot(
    x="Longitude", y="Latitude", hue="Cluster", data=X, height=6,
);


# 4 - Comparing the Target. Box-plots show the distribution of
#the target within each cluster. If the clustering is informative,
# these distributions should, for the most part, separate across
# MedHouseVal (Target), which is indeed what we see.
X["MedHouseVal"] = df["MedHouseVal"]
sns.catplot(x="MedHouseVal", y="Cluster", data=X, kind="boxen", height=6);