#### 6.9.1 Ridge regression
* recall that the least squares fitting procedure estimates $\beta_0, \beta_1, \dots, \beta_p$ using the values that minimize
$$
\text{RSS} = \sum_{i=1}^n \left( y_i - \beta_0 -\sum_{j=1}^p \beta_j x_{ij} \right)^2
$$
* in contrast, the ridge regression coefficient estimates $\hat{\beta}^R = \hat{\beta}^R(\lambda)$ are the values that minimize
$$
\begin{align}
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 +& \lambda \sum_{j=1}^p \beta_j^2 \\
= \text{RSS } +& \lambda \sum_{j=1}^p \beta_j^2
\end{align}
$$
* here $\lambda \geq 0$ is a *tuning parameter*, to be determined separately
* as with least squares, ridge regression seeks coefficient estimates that fit the data well, by making the [[Residual Sum of Squares (RSS)|RSS]] small
* however, the second term, $\lambda \sum_j\beta_j^2$, called a [[Shrinkage in Linear Model Selection and Regularization|shrinkage penalty]], is small when $\beta_1, \dots, \beta_p$ are close to zero, and so it has the effect of shrinking the estimates of $\beta_j$ towards zero
* the tuning parameter $\lambda$ serves to control the relative impact of these two terms on the regression coefficient estimates
* selecting a good value for $\lambda$ is critical
    * cross-validation can be used to make this choice

#### 6.9.2 Ridge regression: scaling of predictors

* the standard least squares coefficient estimates are *scale equivariant*: 
    * multiplying $X_j$ by a constant $c$ simply leads to a scaling of the least squares coefficient estimates by a factor of $1/c$
    * in other words, regardless of how the $j$th predictor is scaled, the least squares coefficient estimates will remain the same
* in contrast, the ridge regression coefficient estimates can change substantially when multiplying a given predictor by a constant, due to the sum of squared coefficients term in the penalty part of the ridge regression objective function
* therefore it is best to apply ridge regression after standardizing the predictors

#### 6.9.3 Ridge regression: centering of predictors

* ridge regression also has an intercept term that is not shrunk
* therefore, ridge regression coefficient estimates are not equivariant to the addition of a constant to each predictor, and so it is best to apply ridge regression after *centering* the predictors to have mean zero
* in this case, the intercept will equal the mean of the response, and so can be ignored in making predictions

#### 6.9.4 Why does ridge regression improve over least squares?

* the bias-variance tradeoff states that the expected test MSE, for a given value $x_0$, can always be decomposed as follows:
$$
\begin{align}
\text{E}(y_0 - \hat{f}(x_0))^2 &= \text{Var}(\hat{f}(x_0)) + [\text{Bias}(\hat{f}(x_0))]^2 + \text{Var}(\epsilon) \\
&= \text{Var}(\hat{f}(x_0)) + [\text{Bias}(\hat{f}(x_0))]^2 + \sigma^2
\end{align}
$$
* here $\text{Var}(\hat{f}(x_0))$ represents the amount by which $\hat{f}$ would change if we estimated it using a different training data set
* $\text{Bias}(\hat{f}(x_0))$ represents the error that is introduced by approximating a real-life problem, which may be extremely complicated, by a much simpler model
* $\sigma^2$ is the irreducible error, which is the variance of the error term $\epsilon$
* as we increase the $\lambda$ parameter, the flexibility of the ridge regression fit decreases, leading to decreased variance but increased bias
    * if a given model had a small variance, then the decrease in variance due to shrinking the coefficients will be small
    * on the other hand, if a given model had a large variance, then the decrease in variance could be dramatic and offset the increase in bias