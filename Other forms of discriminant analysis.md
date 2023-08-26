#statistical-learning 


## Other forms of #discriminant-analysis

$$
Pr(Y=k|X=x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^K \pi_l f_l(x)}
$$

- when $f_k(x)$ is the #Gaussian #density-function for the $k$th class
  - **and** each class has the same #covariance-matrix $\Sigma$
  - we have #linear-discriminant-analysis
- by altering the forms for the $f_k(x)$, we get different classifiers:
  - #quadratic-discriminant-analysis
    - each class is still #Gaussian, but has its own #covariance-matrix $\Sigma_k$
  - #naive-Bayes
    - with $f_k(x) = \prod_{j=1}^p f_{jk}(x_j)$ ( #conditional-independence model) in each class
    - for #Gaussian this means the $\Sigma_k$ are #diagonal-matrices
    - this assumes that the features are #conditionally-independent given the class, which is a very #strong-assumption and rarely true in practice
    - this will #bias the #variance estimates and in turn the class probabilities
    - but in terms of #classification, all you need to know is the class with the highest probability, so it can tolerate some #bias in the #probability while still achieving good results
  - many other forms, by proposing different forms for $f_k(x)$ (including #nonparametric approaches)

[[Quadradic Discriminant Analysis]]

[[Naive Bayes]]
