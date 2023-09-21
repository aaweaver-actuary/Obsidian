* subset selection methods use [[Ordinary Least Squares (OLS)|least squares]] to fit a [[Linear Model|linear model]] that contains a subset of the predictors
* as an alternative, we can fit a model containing all $p$ predictors using a technique that *constrains* or [[Regularization|regularizes]] the coefficient estimates, or equivalently, that *shrinks* the coefficient estimates towards zero
* it may not be immediately obvious why such a constraint should improve the fit, but it turns out that shrinking the coefficient estimates can significantly reduce their [[Variance|variance]]


* neither [[Ridge regularization|ridge]] nor [[The Lasso for regularization|lasso]] will universally dominate the other
* in general, one might expect the [[The Lasso for regularization|lasso]] to perform better in a setting where a relatively small number of predictors have substantial coefficients, and the remaining predictors have coefficients that are very small or that equal zero
* however, the number of predictors that is related to the response is never known a priori for real data sets
* a technique such as [[k-fold Cross Validation|cross validation]] can be used in order to determine which approach is better on a particular data set

### 6.12 Selecting the tuning parameter $\lambda$ for ridge regression and the lasso

* it is important
* as for subset selection we require a method to determine which of the models under consideration is best
* that is, we require a way to select the tuning parameter $\lambda$
* [[k-fold Cross Validation|cross validation]] provides a simple way to tackle this problem[^1]
    * we choose a [[Parameter Grid|grid]] of $\lambda$ values, and compute the [[k-fold Cross Validation|cross validation]] error for each value of $\lambda$
    * we then select the tuning parameter value for which the [[k-fold Cross Validation|cross validation]] error is smallest
    * finally, the model is re-fit using all of the available observations and the selected value of $\lambda$

[^1]: [[Use cross validation to select hyperparameters]]