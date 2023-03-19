"""
	
	******************************
	** Dimensionality Reduction **
	******************************

	Dimensionality Reduction is the process to decrease the number
of features from a DataSet combining them to create a new small
number of features called "Components".

-*-*-*-*-

	To apply this technique, your DataSet must attend the following
requisition:

	/ all Categorical Features must be Encoded, since Dimensionality
Reduction works out just with Numerical Features;

	/ the features must be standardized, unless you know you have
good reason not to, such as, the DataSet is already standardized
by default;

	/ outliers must be treated being removed or constrained, since
they can have an undue influence on the results.

-*-*-*-*-

	Situations when you can use Dimensionality Reduction:

	/ when you desire to check out whether clusters have similar
properties and attributes;

	/ when the DataSet contains lot of features (DataSet
Compression to two or three features);

	/ when the features are multi-colinear (there is a significant
number of Linear Correlations between them);
	
	/ when your goal is to apply denoising.

-*-*-*-*-

	Variations of Dimensionality Reduction:

	/ Principal Component Analisys (PCA): maximizes the variance;

	/ t-Distributed Stochastic Neighbor Embedding (t-SNE): creates a
reduced feature space where similar samples are modeled by nearby
points and dissimilar samples are modeled by distant points with
high probability;

	/ Uniform Manifold Approximation and Projection (UMAP): applies
Nearest Neighbors to cluster the datas and then reducts the
dimensions.
"""