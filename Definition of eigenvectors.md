[[Linear Algebra]]

[[Definition of eigenvectors|Eigenvectors]] $\mathbf{x}$ of a square matrix $A$ are non-zero vectors that, when multiplied by $A$, result in a scaled version of themselves: $A\mathbf{x} = \lambda \mathbf{x}$

- here, $\lambda$ is the corresponding [[Definition of eigenvalues|eigenvalues]]

### In Machine Learning

[[Definition of eigenvectors|Eigenvectors]] are used in [[Principal Components Analysis (PCA)]]:

1. Start with a data matrix $X$ and compute its [[Variance-Covariance Matrix|variance-covariance matrix]] $\Sigma$.
2. Then find the [[Definition of eigenvalues|eigenvalues]] and [[Definition of eigenvectors|eigenvectors]] of $\Sigma$ 1. Sort [[Definition of eigenvalues|eigenvalues]] in descending order and select the top $k$ corresponding to the largest [[Definition of eigenvalues|eigenvalues]] 2. Form a matrix $W$ with these top $k$ [[Definition of eigenvectors|eigenvectors]] as columns 3. Transform the original data:$$
	   Y=XW \hspace{17em}
	   $$
   This transformed data $Y$ is now in a new space where the axes are the [[Principal Components|principal components]]
