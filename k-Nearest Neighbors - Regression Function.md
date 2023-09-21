[[k-Nearest Neighbors|Nearest neighbor methods]] attempt to directly implement [[Regression Function|the regression function]] using the training data:
$$
\hat{f}(x) = \text{Ave}(y_i|x_i \in N_k(x)) \hspace{10em}
$$
- $N_k(x)$ - the neighborhood containing the $k$ points in $\mathcal{T}$ closest to $x$
- $\mathcal{T}$ - training data set