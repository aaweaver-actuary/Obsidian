[[Unsupervised Learning]] [[k-Means Clustering]] 

- guaranteed to decrease the value of the objective[^3] at each step
	- note that
	  $$
	  \begin{align}
	  \frac{1}{|C_k|} \sum_{i, i' \in C_k} &\sum_{j=1}^p (x_{ij} - x_{i'j})^2 = \\ 
		2 \sum_{i \in C_k} &\sum_{j=1}^p (x_{ij} - \overline{x}_{kj})^2 \hspace{15em}
	\end{align}
	  $$
	  - here $\overline{x}_{kj} = \frac{1}{|C_k|} \sum_{i\in C_k} x_{ij}$ is the mean for feature $j$ in cluster $C_k$[^4]
- However it is not guaranteed to give the global minimum
	- this is not a [[Convex functions|convex function]]

[^3]: [[Details of k-Means Clustering#How to define within-cluster-variance?]]
[^4]: AKA the #centroid
