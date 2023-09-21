[[Unsupervised Learning]] [[Clustering]] [[Hierarchical Clustering]] 

- build a hierarchy in a bottom-up fashion:
	1. find the two closest[^1] objects - cluster those
		- this now becomes itself an object, and the #centroid of the object is used for the next step
	2. Iterate until there is a cluster with everything in it

[^1]: generally means squared distance / [[l2 Norm]] though can make other choices