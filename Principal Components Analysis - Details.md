[[Unsupervised Learning]] [[Principal Components Analysis (PCA)]]

- the first [[Principal Components|principal component]] of a set of features $X_1, X_2, \dots, X_p$ is the #normalized[^1] [[Linear Combination|linear combination]] of the features:$$
Z_1 = \phi_{11}X_1 + \phi_{21}X_2 + \cdots + \phi_{p1}X_p \hspace{12em}
$$that has the largest [[Variance|variance]]
- we refer to the elements $\phi_{11}, \dots, \phi_{p1}$ as the #loading's of the first [[Principal Components|principal component]]
	- together the #loading's make up the [[Principal Components|principal component]] #loading vector $\phi_1 = (\phi_{11}, \dots, \phi_{p1})^T$ 
- we constrain the #loading's so that their [[Residual Sum of Squares (RSS)|sum of squares]] is 1[^2]

[^1]: meaning that $\sum_{j=1}^p \phi_{j1}^2 =1$ 
[^2]: Otherwise setting $\phi$ to an arbitrarily large value could result in an arbitrarily large [[Variance|variance]]