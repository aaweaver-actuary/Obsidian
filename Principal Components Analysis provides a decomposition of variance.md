[[Unsupervised Learning]] [[Principal Components Analysis]]

- to understand the strength of each component, we want to know the #proportion-of-variance-explained (PVE) by each one
- the #total-variance present in a data set (assuming variables have been #centered to have mean 0) is defined as$$
  \sum_{j=1}^p \text{Var} (X_j) = \sum_{j=1}^p \frac{1}{n}\sum_{i=1}^n x_{ij}^2, \hspace{15em}$$
- the [[Variance|variance]] explained by the $m$th [[Principal Components|principal component]] is then$$
  \text{Var}(Z_m) = \frac{1}{n} \sum_{i=1}^nz_{im}^2 \hspace{17em}
  $$
- it can be shown that $\sum_{j=1}^p \text{Var}(X_j) = \sum_{m=1}^M \text{Var}(Z_m)$ with $M=\min(n-1, p)$ 
- this means that the #proportion-of-variance-explained of the $m$th [[Principal Components|principal component]] is given by
$$
  \frac{\sum_{i=1}^n z_{im}^2}{\sum_{j=1}^p\sum_{i=1}^n x_{ij}^2} \hspace{20em}
  $$
  - this is a positive quantity between 0 and 1
- the #proportion-of-variance-explained sum to 1
- we sometimes display the cumulative #proportion-of-variance-explained:

![[Pasted image 20230829050151.png]]

- this is a #scree-plot
- left side is the "density function"
	- the first [[Principal Components|principal component]] explains about 60% of the [[Variance|variance]]
	- the second [[Principal Components|principal component]] explains about 25% of the [[Variance|variance]] 
	- the third is about 10%
	- the fourth is about 5%
- right side is something like the cumulative distribution function
- this plot is also used to help select an optimal number of [[Principal Components|principal components]]:
	- look for an "elbow" $\rightarrow$ bend in the plot