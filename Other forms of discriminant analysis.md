## Other forms of discriminant analysis

$$
Pr(Y=k|X=x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^K \pi_l f_l(x)}
$$

- when $f_k(x)$ is the [[Gaussian|Gaussian density function]] for the $k$th class
  - **and** each class has the same [[Variance-Covariance Matrix|variance-covariance matrix]] $\Sigma$
  - we have [[Linear Discriminant Analysis|linear discriminant analysis]]
- by altering the forms for the $f_k(x)$, we get different classifiers:
  - [[Quadradic Discriminant Analysis]]
    - each class is still [[Gaussian]], but has its own [[Variance-Covariance Matrix|variance-covariance matrix]] $\Sigma_k$
  - [[Naive Bayes]]
    - with $f_k(x) = \prod_{j=1}^p f_{jk}(x_j)$ ( #conditionally-independent model) in each class
    - for [[Gaussian]] this means the $\Sigma_k$ are diagonal matrices
    - this assumes that the features are #conditionally-independent given the class, which is a very #strong-assumption and rarely true in practice
    - this will [[Bias|bias]] the [[Variance|variance]] estimates and in turn the class probabilities
    - but in terms of [[Classification|classification]], all you need to know is the class with the highest probability, so it can tolerate some [[Bias|bias]] in the probability while still achieving good results
  - many other forms, by proposing different forms for $f_k(x)$ (including nonparametric approaches)

[[Naive Bayes]]
