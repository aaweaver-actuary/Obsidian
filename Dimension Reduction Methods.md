
* the methods discussed so far in the section on [[Linear Model Selection and Regularization|linear model selection and regularization]] have involved fitting a [[Linear Model|linear model]] involving $p$ predictors using either  [[Ordinary Least Squares (OLS)|least squares]] or a [[Shrinkage in Linear Model Selection and Regularization|shrinkage]] approach
* we now consider some approaches that transform the predictors and then fit a [[Ordinary Least Squares (OLS)|least squares]] model using the transformed variables
    * these approaches will be called **dimension reduction methods**
* the goal of dimension reduction is to reduce the $p$ predictors to a $M$-dimensional subspace, where $M < p$

#### 6.13.1 Details

* Let $Z_1, Z_2, \dots, Z_M$ represent $M < p$ [[Linear Combination|linear combinations]] of our original $p$ predictors. That is,
$$
Z_m = \sum_{j=1}^p \phi_{jm}X_j
$$
* where $\phi_{1m}, \phi_{2m}, \dots, \phi_{pm}$ are constants
* we can then fit the following [[Linear Regression|linear regression]] model using [[Ordinary Least Squares (OLS)|least squares]]:
$$
y_i = \theta_0 + \sum_{m=1}^M \theta_m z_{im} + \epsilon_i, \quad i = 1, \dots, n
$$
* note that in the model, the [[Regression|regression]] coefficients are given by $\theta_0, \theta_1, \dots, \theta_M$
    * if the constants $\phi_{jm}$ are chosen wisely, then the $M$-dimensional response $Z_m$ may be much simpler to model than the original $p$-dimensional response $X_j$
* note that, from the definition of $Z_m$, we have
$$
\begin{align}
\sum_{m=1}^M \theta_m z_{im}  =& \sum_{m=1}^M \theta_m \sum_{j=1}^p \phi_{jm} x_{ij} \\
=& \sum_{j=1}^p \sum_{m=1}^M \theta_m \phi_{jm} x_{ij} \\
=& \sum_{j=1}^p \beta_j x_{ij} \\
\text{where } \beta_j =& \sum_{m=1}^M \theta_m \phi_{jm}
\end{align}
$$
* thus the model is equivalent to the [[Ordinary Least Squares (OLS)|least squares]] [[Regression|regression]] of $y$ onto $X_1, X_2, \dots, X_p$
    * it can be considered a special case of the [[Linear Model|linear model]] in which the predictors are [[Linear Combination|linear combinations]] of the original predictors
* the dimension reduction approach is most useful in the case where $M < p$, that is, when we have reduced the problem to a smaller number of predictors
    * in this case, the [[Ordinary Least Squares (OLS)|least squares]] approach is more stable
    * can win in the [[Bias-variance trade-off in statistical learning|bias-variance tradeoff]]