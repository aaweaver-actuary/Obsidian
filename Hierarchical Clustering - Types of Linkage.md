[[Unsupervised Learning]] [[Hierarchical Clustering]] 

![[Pasted image 20230831050836.png]]

| Linkage | Description |
|-|-|
| **Complete**| Maximal inter-cluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster $A$ and cluster $B$, and record the **largest** of these dissimilarities.|
| **Single**| Minimal inter-cluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster $A$ and cluster $B$, and record the **smallest** of these dissimilarities. |
| **Average**| Mean inter-cluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster $A$ and cluster $B$, and record the **mean** of these dissimilarities.|
| **Centroid**| Dissimilarity between the #centroid for cluster $A$[^1] and the #centroid for cluster $B$. Can result in undesirable #inversions. |

#complete-linkage and #average-linkage are most common

[^1]: a mean vector of length $p$