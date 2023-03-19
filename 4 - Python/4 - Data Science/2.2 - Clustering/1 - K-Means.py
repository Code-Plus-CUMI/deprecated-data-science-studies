"""

	************************
	** K-Means - Clusters **
	************************

	K-Means defines CENTROIDS and it's goal is to find
the perfect position for each centroid and its territory 
(TESSALATION).

-*-*-*-*-

	When creating this algorithm, you have to pay attention to three
parameters:

	/ n_clusters: number of Clusters (K)

	/ max_iter: number of iterations

	/ n_init: gets the Centroids' Position has the least total
distance between each point and its centroid, the optimal 
clustering.

-*-*-*-*-

	Besides, since K-Means clustering is sensitive to scale, it can
be a good idea RESCALE or NORMALIZE data with extreme values.
Our features are already roughly on the same scale, so we'll
leave them as-is.
"""



# ---- Importing Libraries and Preparing DataSet ----
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('filepath')
X = df.loc[:, ['Latitude', 'Longitude', 'MedInc']]



# ---- WCSS and Elbow Method ----
#
# Their function is to check out how many clusters is great
# to the process
#
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



# ---- Using K-Means ----
#
# Consider that 4 clusters was the great amount and we
# will repeat the K-Means centroids moviment 10 times
kmeans = KMeans(n_clusters=4,
    			init='k-means++',
    			max_iter=300,
    			n_init=10,
    			random_state=0)

X['Cluster'] = kmeans.fit_predict(X)
X['Cluster'] = X['Cluster'].astype('category')



# ---- Plotting the Results ----
sns.relplot(
    x="Longitude", y="Latitude", hue="Cluster", data=X, height=6,
);



# OBS.: Comparing the Target - box-plots show the distribution of
#the target within each cluster. If the clustering is informative,
# these distributions should, for the most part, separate across
# MedHouseVal (Target), which is indeed what we see.
X["MedHouseVal"] = df["MedHouseVal"]
sns.catplot(x="MedHouseVal", y="Cluster", data=X, kind="boxen", height=6);