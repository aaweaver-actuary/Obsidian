[[Unsupervised Learning]]

- Let $C_1, C_2, \dots, C_K$ denote sets containing the indices of the observations in each [[Clustering|cluster]]. These sets satisfy two properties:
    1.  $C_1 \cup C_2 \cup \cdots \cup C_K = \{1, 2, \ldots, K\}$
        - eg each observation belongs to at least one of the $K$ [[Clustering|clusters]]
    2.  $C_k \cap C_{k'} = \emptyset$ for all $k\ne k'$
        - eg the clusters are non-overlapping: no observation belongs to more than one [[Clustering|cluster]]
- For instance, if the $i$th observation belongs to the $k$th [[Clustering|cluster]], then $i \in C_k$
- The idea behind [[k-Means Clustering|k-means clustering]] is that a "good" clustering is one for which the #within-cluster-variance is as small as possible
- The #within-cluster-variance for a cluster $C_k$ is a measure $\text{WCV}(C_k)$ of the amount by which the observations within a [[Clustering|cluster]] differ from each other
- This means that we want to solve this problem:
    $$
    \begin{equation}
    \text{minimize}_{C_1, \dots, C_K} \left\{ \sum_{k=1}^K \text{WCV}(C_k) \right\} \hspace{11em}
    \end{equation}
    $$
- In words, this says that we want to partition the observations into $K$ [[Clustering|clusters]] such that the total #within-cluster-variance, summed over all $K$ [[Clustering|clusters]], is as small as possible

### How to define #within-cluster-variance?

- typically we use [[l2 Norm]]:
    $$
    \text{WCV}(C_k) = \frac{1}{|C_k|} \sum_{i, i' \in C_k} \sum_{j=1}^p (x_{ij} - x_{i'j})^2 \hspace{10em}
    $$
- here $|C_k|$ denotes the number of observations in the $k$th [[Clustering|cluster]]
- Combining these two expressions gives:
    $$
    \text{minimize}_{C_1,\dots,C_K} \left\{ \sum_{k=1}^K \frac{1}{|C_k|} \sum_{i, i' \in C_k} \sum_{j=1}^p (x_{ij} - x_{i'j})^2 \right\}
    $$
