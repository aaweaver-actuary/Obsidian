
- standard Bayes theorem:
  $$
  Pr(Y=k|X=x) = \frac{Pr(X=x|Y=k) \cdot Pr(Y=k)}{Pr(X=x)}
  $$
- we write this slightly differently for [[Linear Discriminant Analysis|discriminant analysis]][^1]:
  $$
  Pr(Y=k|X=x) = \frac{\pi_k \cdot f_k(x)}{\sum_{l=1}^K \pi_l \cdot f_l(x)}
  $$
- $f_k(x)$ is the density function for $X$ in class $k$.
  - here we use the [[Gaussian]] distribution, so $f_k(x) = \frac{1}{\sqrt{2\pi}\sigma_k} \exp\left(-\frac{1}{2\sigma_k^2}(x-\mu_k)^2\right)$
- $\pi_k$ is the #marginal-probability or [[Prior Distribution|prior distribution]] for class $k$.
  - this is the proportion of the training observations that belong to class $k$.


[^1]: [[Discriminant analysis for classification]]
