
## Maximum Likelihood

- We use [[Maximum likelihood is used to fit linear regression parameters|maximum likelihood]] to estimate $\beta_0$ and $\beta_1$
- The [[Likelihood|likelihood]] function is
  $$
  \ell(\beta_0, \beta_1) = \prod_{i:y_i=1} p(x_i) \prod_{i':y_{i'}=0} (1 - p(x_{i'}))
  $$
- This [[Likelihood|likelihood]] function gives the probability of the observed data as a function of $\beta_0$ and $\beta_1$
- We choose $\beta_0$ and $\beta_1$ to maximize this [[Likelihood|likelihood]] function