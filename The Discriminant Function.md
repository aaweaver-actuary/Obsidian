- To classify at the value $x$[^1], we compute the #discriminant-function for each class, and then pick the class with the largest value.
- We need to see which of the $p_k(x)$ is largest.
- If you take logs and drop terms that don't depend on $k$, you get that the largest $p_k(x)$ corresponds to the largest $\delta_k(x)$, where
- $$
    \delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \log \pi_k
    $$
- note here that $\delta_k(x)$ is linear in $x$.
- $\pi_k$ is the #prior #probability for class $k$.
    - this is the proportion of the training observations that belong to class $k$.
- $\mu_k$ is the mean of $X$ for observations in class $k$.
    - this is the mean of $X$ for the training observations in class $k$.
- If there are $k=2$ classes and we assume equal #prior-distribution, eg $\pi_1 = \pi_2 = 0.5$, then we can simplify the #discriminant-function further \* the [[Decision Boundary|decision boundary]] is at
    $$
    x = \frac{\mu_1 + \mu_2}{2}
    $$
- if $x$ is less than this, we predict class 1, otherwise we predict class 2.
- this is the same as the [[Logistic Regression|logistic regression]] [[Decision Boundary|decision boundary]].[^2]

[[Estimating the parameters for the discriminant function]]

[^1]: [[Classification]]
[^2]: [[Logistic regression is linear regression on the log-odds]]
