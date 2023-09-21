
### #naive-Bayes

- assume that the features are #conditionally-independent given the class
- useful when there are many features ($p$ is large), and so multivariate approaches are infeasible
- the #conditionally-independent assumption means that the #covariance-matrix  $\Sigma_k$ are #diagonal-matrices 
- [[Gaussian]] #naive-Bayes assumes that each $\Sigma_k$ is a #diagonal-matrices:

$$
\begin{align}
\delta_k(x) \propto& \log \left[ \pi_k \prod_{j=1}^p f_{jk}(x_j) \right] \\
=& -\frac{1}{2} \sum_{j=1}^p \left( \frac{x_j - \mu_{jk}}{\sigma_{jk}} + \log \sigma_{kj}^2 \right)^2 + \log \pi_k
\end{align}
$$

- can use for #mixed-feature-vectors
  - some continuous, some discrete, some qualitative, some quantitative
  - if $X_j$ is qualitative, replace $f_{jk}(x_j)$ with $P(X_j = x_j | Y = k)$ over the discrete values of $X_j$
- despite really strong assumptions, #naive-Bayes often produces surprisingly good results
  - it is often used as a benchmark for [[Classification|classification]] methods
  - it is very fast and can be used on very large datasets
  - it is often surprisingly hard to beat
