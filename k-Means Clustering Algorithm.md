[[Unsupervised Learning]] [[Clustering]] [[k-Means Clustering]] 

1. Randomly assign a number, from $1$ to $K$, to each of the observations. These are the initial [[Clustering|cluster]] assignments.
2. Iterate until the [[Clustering|cluster]] assignments stop changing:
	1. For each of the $K$ [[Clustering|clusters]], compute the cluster #centroid [^1]
	2. Assign each observation to the [[Clustering|cluster]] whose #centroid is closest[^2]



[^1]: The $k$th [[Clustering|cluster]] #centroid is the vector of the $p$ feature means for the observations in the $k$th [[Clustering|cluster]]
[^2]: "Closest" means Euclidean distance