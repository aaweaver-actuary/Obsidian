
- We need to estimate $\pi_k$, $\mu_k$, and $\sigma^2$.
- $\pi_k$ is just the proportion of the training observations that belong to class $k$.
- $\mu_k$ is the #mean of $X$ for the training observations in class $k$.
- $\sigma^2$ is the #mean of the #sample-variance for each of the $K$ classes.

$$
\begin{align}
\hat{\pi}_k &= \frac{n_k}{n} \\
\hat{\mu}_k &= \frac{1}{n_k} \sum_{i:y_i=k} x_i \\
\hat{\sigma}^2 &= \frac{1}{n-K} \sum_{k=1}^K \sum_{i:y_i=k} (x_i-\hat{\mu}_k)^2 \\
&= \sum_{k=1}^K \frac{n_k-1}{n-K} \cdot \hat{\sigma}_k^2
\end{align}
$$

- $\hat{\sigma}_k^2$ is the #sample-variance for the observations in the $k$th class.
- $n_k$ is the number of observations in the $k$th class.
- $n$ is the total number of observations.
- $K$ is the number of classes.
- $\hat{\sigma}^2$ is a #weighted-average of the #sample-variance for each of the $K$ classes.
  - the weights are the proportions of observations in each class.
  - this is the pooled estimate of variance.
- the pooled estimate of variance is a weighted average of the sample variances for each of the $K$ classes.
  - the weights are the proportions of observations in each class.