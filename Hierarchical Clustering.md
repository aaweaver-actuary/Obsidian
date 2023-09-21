[[Unsupervised Learning]] [[Clustering]]

- In ***hierarchical clustering*** we do not know in advance how many [[Clustering|clusters]] we want[^1] 
- We end up with a tree-like visual representation of the observations[^2] that allows us to view at once the [[Clustering|clusters]] obtained for each possible number of [[Clustering|clusters]], from $1$ to $n$ 
- the type of **hierarchical clustering** we look at is called #bottom-up-clustering or #agglomerative-clustering
	- this is the most common type[^3]
	- refers to the fact that a #dendrogram is built starting from the leaves and combining [[Clustering|clusters]] up to the trunk
- Unlike [[k-Means Clustering]] you don't have to choose $k$, and you actually get the [[Clustering|clusters]] for all $k$ at once

[[Hierarchical Clustering - The Idea]]
[[Hierarchical Clustering - Algorithm]]
[[Example of dendrogram using scikit-learn]]
[[Hierarchical Clustering - Types of Linkage]]
[[Hierarchical Clustering - Choice of Dissimilarity Measure]]
[[Hierarchical Clustering - Practical Issues]]



[^1]: In contrast with [[k-Means Clustering]] where we know we want $k$ clusters 
[^2]: known as a #dendrogram
[^3]: there is also #top-down-clustering, but this is much less common