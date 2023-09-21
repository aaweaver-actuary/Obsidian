[[Regularization]] #linear-model-selection-and-regularization 

* [[Ridge regularization]] has one obvious disadvantage: it includes all $p$ predictors in the final model
* the **lasso** is a relatively recent alternative to ridge regression that overcomes this disadvantage
* lasso coefficients $\hat{\beta}^L = \hat{\beta}^L(\lambda)$ minimize
$$
\begin{align}
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 +& \lambda \sum_{j=1}^p |\beta_j| \\
= \text{RSS } +& \lambda \sum_{j=1}^p |\beta_j|
\end{align}
$$
* lasso uses an $\ell_1$ penalty instead of an $\ell_2$ penalty
* as with ridge regression, the lasso shrinks the coefficient estimates towards zero
* however, in the case of the lasso, the $\ell_1$ penalty has the effect of forcing some of the coefficient estimates to be exactly equal to zero when the tuning parameter $\lambda$ is sufficiently large
* hence, much like best subset selection, the lasso performs *variable selection* and yields *sparse* models with only a subset of the variables
* as with ridge regression, selecting a good value for $\lambda$ is critical
    * cross-validation can be used to make this choice
