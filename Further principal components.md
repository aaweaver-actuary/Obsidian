[[Principal Components Analysis (PCA)]] [[Unsupervised Learning]]

- The second [[Principal Components|principal component]] is the [[Linear Combination|linear combination]] of $X_1, \dots, X_p$ that has maximal [[Variance|variance]] among all [[Linear Combination|linear combinations]] that are uncorrelated with $Z_1$
- The second [[Principal Components|principal component]] takes the form$$
  z_{i2}=\phi_{12}x_{i1} + \cdots + \phi_{p2}x_{ip} \hspace{15em}
  $$where $\phi_2$ is the second [[Principal Components|principal component]] #loading vector with elements $\phi_{12}, \phi_{22}, \dots, \phi_{p2}$ 
- It turns out that constraining $Z_2$ to be uncorrelated with $Z_1$ is equivalent to constraining the direction $\phi_2$ to be #orthogonal ( #perpendicular ) to the direction of $\phi_1$
- The [[Principal Components|principal component]] directions $\phi_1, \phi_2, \dots$ are the ordered sequence of right #singluar vectors of the matrix $\mathbf{X}$
	- The [[Variance|variances]] of the components are $\frac{1}{n}$ times the squared #singular values
	- The solution comes also from the [[Singular Value Decomposition|singular value decomposition]] of $\mathbf{X}$
- There are at most $\min(n-1,p)$ [[Principal Components|principal components]]