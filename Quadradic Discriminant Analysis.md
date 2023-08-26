#quadratic-discriminant-analysis #statistical-learning 

$$
\delta_k(x) = -\frac{1}{2} (x-\mu_k)^T \Sigma_k^{-1} (x-\mu_k) - \frac{1}{2} \log |\Sigma_k| + \log \pi_k
$$

- the #decision-boundary is #quadratic in $x$
- because the $\Sigma_k$ are different for each class, the #decision-boundary is #nonlinear /the #quadratic terms matter in a way they don't for #linear-discriminant-analysis [^1]

[^1]: [[The Discriminant Function]]