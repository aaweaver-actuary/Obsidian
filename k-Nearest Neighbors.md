This method takes the average of the $k$ closest values of $y$:
$$
\hat{Y}(x) = \frac{1}{k} \sum_{x_i\in N_k(x)} y_i
$$
- $N_k(x)$ - neighborhood of $x$ defined by the $k$ closest points[^1] $x_i$ in the training set

#### Properties:
- [[Training Error]] for kNN fits is approximately an increasing function of $k$
	- always equal to 0 when $k=1$
- High [[Variance|variance]], low [[Bias|bias]]


[[How to pick k for k-Nearest Neighbors]]
[[k-Nearest Neighbors - Effective Number of Parameters]]
[[k-Nearest Neighbors - Regression Function]]
[[k-Nearest Neighbors - Approximations In the Regression Function]]

- For large $N$, points in $N_k(x)$ are likely to be close to $x$
- As $N, k \rightarrow \infty$ such that $k/N \rightarrow 0$, $\hat{f}(x)\rightarrow E[Y|X=x]$ 

[^1]: "Closeness" implies a metric, often [[Euclidean Distance|Euclidean distance]]