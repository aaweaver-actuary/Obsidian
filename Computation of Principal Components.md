[[Unsupervised Learning]] [[Principal Components Analysis (PCA)]]

- Suppose we have $n\times p$ data set $\mathbf{X}$
- Since we are only interested in [[Variance|variance]], we assume that each of the variables in $\mathbf{X}$ has been centered[^1]
- We then look for the [[Linear Combination|linear combinations]] of the sample features of the form$$
z_{i1} = \phi_{11}x_{i1} + \phi_{21}x_{i2} + \cdots + \phi_{p1}x_{ip} \hspace{13em} 
$$for $i=1, 2, \dots, n$ that has the largest [[Variance|sample variance]], subject to the constraint that $\sum_{j=1}^p \phi_{j1}^2=1$ 
- Since each of the $x_{ij}$ has mean 0, so does $z_{i1}$[^2]
	- Hence the [[Variance|sample variance]] of the $z_{i1}$ can be written as $$\frac{1}{n}\sum_{i=1}^nz_{i1}^2 \hspace{20em}$$
- Plugging $z_{i1}$ into the first [[Principal Components|principal component]] #loading vector solves the [[Optimization|optimization]] problem $$\text{maximize}_{\phi_{11},\dots,\phi_{p1}}\frac{1}{n}\sum_{i=1}^n\left( \sum_{j=1}^p \phi_{j1}x_{ij}\right)^2,\space\text{ subject to }\sum_{j=1}^p\phi_{j1}^2=1$$
- This problem can be solved via a [[Singular Value Decomposition|singular value decomposition]] of the matrix $\mathbf{X}$, a standard technique in [[Linear Algebra]]
- We refer to $Z_1$ as the first [[Principal Components|principal component]] with realized values $z_{11}, \dots, z_{n1}$ 

[^1]: Eg all columns of $\mathbf{X}$ have mean 0
[^2]: for any values of $\phi_{j1}$