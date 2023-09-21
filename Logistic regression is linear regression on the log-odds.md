

- Write $p(X) = P(Y=1|X)$ for short and call this the probability of success
- Consider using credit card `balance` to predict `default`
- [[Logistic Regression|Logistic regression]] uses the form
  $$
  p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}
  $$
- It is easy to show that no matter what values $\beta_0$ and $\beta_1$ take, $p(X)$ will always be between 0 and 1
- You can rearrange the equation to get
  $$
  \log \left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X
  $$
- The left-hand side is called the #log-odds or #logit transformation of $p(X)$
  - it is also a monotonic transformation of $p(X)$, so the two are equivalent for [[Classification|classification]] purposes