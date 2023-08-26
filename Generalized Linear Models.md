#statistical-learning 


## #generalized-linear-model

- #linear-regression is used for #quantitative #target
- #logistic-regression is the counterpart for #binary #target
  - models the #logit of the probability of class membership as a #linear-function of the features
- other response types exist:
  - #count-data -> #Poisson-regression
  - non-negative data -> #Tweedie-regression
  - skewed distributions -> #gamma-regression
- all these models are a #special-case of the #generalized-linear-model
  - the response $Y$ is assumed to follow some distribution in the #exponential-family
  - the #mean of $Y$ is related to the #linear-predictor via a #link-function
  - the #linear-predictor is a #linear-combination of the features

### #Poisson-regression Model

- #Poisson distribution is useful for modeling #count-data:

$$
\begin{align}
p(y|\lambda) &= \frac{e^{-\lambda}\lambda^y}{y!} \\
\lambda &= E(Y) = Var(Y)
\end{align}
$$

- the #mean and #variance of the #Poisson distribution are equal
- with covariates $X$, the #Poisson-regression model is:

$$
\begin{align}
\log \left[ \lambda(X_1, \dots, X_p )\right] =& \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \\
\lambda(X_1, \dots, X_p ) =& e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}

\end{align}
$$

### #generalized-linear-model

- so far have covered three types of #generalized-linear-model:
  - #linear-regression
  - #logistic-regression
  - #Poisson-regression
- each of these has a #characteristic-link-function:
	- a #link-function is the #transformation of the #mean that is represented by the #linear-model
  $$
  \begin{align}
  \eta \left( E[Y | X_1, \dots, X_p] \right) &= \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p
  \end{align}
  $$
- #linear-regression #link-function: identity
  - $\eta(\mu) = \mu$
- #logistic-regression #link-function: #logit 
  - $\eta(\mu) = \log \left( \frac{\mu}{1-\mu} \right)$
- #Poisson-regression #link-function: #log

  - $\eta(\mu) = \log(\mu)$

- each also has a #characteristic-variance-function 
- the models are fit by #maximum-likelihood 
- other types of #generalized-linear-model include:
  - #gamma-regression 
  - #Tweedie-regression
  - #negative-binomial-regression
  - #inverse-Gaussian-regression
  - more