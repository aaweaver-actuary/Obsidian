
- [[Poisson Distribution|The Poisson distribution]] is useful for modeling count data:

$$
\begin{align}
p(y|\lambda) &= \frac{e^{-\lambda}\lambda^y}{y!} \\
\lambda &= E(Y) = Var(Y)
\end{align}
$$

- the mean and [[Variance|variance]] of [[Poisson Distribution|the Poisson distribution]] are equal
- with covariates $X$, the ***Poisson regression*** model is:

$$
\begin{align}
\log \left[ \lambda(X_1, \dots, X_p )\right] =& \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \\
\lambda(X_1, \dots, X_p ) =& e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}

\end{align}
$$
