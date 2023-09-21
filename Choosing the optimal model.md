
* the model containing all the predictors will always have the smallest training error
    * this is because the training error decreases as more variables are added to the model
* we want to choose a model with low *test* error, not low *training* error
    * recall that training error is not a good estimate of test error
    * therefore [[Residual Sum of Squares (RSS)|RSS]] and $R^2$ are not suitable for selecting the best model among a collection of models with different numbers of predictors
    * we can estimate test error using [[k-fold Cross Validation|cross validation]], AIC, BIC, or adjusted $R^2$
##### what do we need?
a way to estimate the test error associated with a given model, in order to select the best model

### 6.7 Estimating test error: two approaches
* we can indirectly estimate test error by making an adjustment to the training error to account for the bias due to overfitting
    * this adjustment is estimated using the same training data
    * this approach is called **shrinkage**
* we can directly estimate the test error, using either a validation set approach or a cross-validation approach
    * this approach is called **subset selection**

### 6.8 $C_p$, AIC, BIC, and adjusted $R^2$

* these techniques adjust the training error for the model size, and can be used to select among a set of models with different numbers of variables
* the next figure displays $C_p$, AIC, BIC, and adjusted $R^2$ for all models ranging from the intercept-only model containing no predictors, to the full model containing all $p$ predictors


#### 6.8.1 Mallows' $C_p$
* this is an statistic that adjusts the training [[Residual Sum of Squares (RSS)|RSS]] by adding a penalty term that is larger when $p$ is larger
    * used to approximate test error
$$
C_p = \frac{1}{n}(RSS + 2d\hat{\sigma}^2)
$$
where  
* $d$ is the total number of parameters in the model
* $\hat{\sigma}^2$ is an estimate of the variance of the error $\epsilon$ associated with each response measurement

#### 6.8.2 Akaike information criterion (AIC)

* defined for a large class of models fit by [[Maximum likelihood is used to fit linear regression parameters|maximum likelihood]]
$$
\text{AIC} = -2\log L + 2d
$$
where
* $L$ is the maximized value of the likelihood function for the estimated model

**NOTE** that in the case of a [[Linear Model|linear model]] with [[Gaussian]] errors, [[Maximum likelihood is used to fit linear regression parameters|maximum likelihood]] and [[Ordinary Least Squares (OLS)|least squares]] are the same thing, up to a constant additive term:
$$
-2\ell = \frac{\text{RSS}}{\hat{\sigma}^2}
$$
* this means that the [[Akaike Information Criterion (AIC)]] statistic is equivalent to $C_p$ up to an additive constant

#### 6.8.3 Bayesian information criterion (BIC)

$$
\begin{align}
\text{BIC} =& \frac{1}{n}\left(\text{RSS} + \log(n)d\hat{\sigma}^2\right) \\
=& -2 \ell + \log(n)d
\end{align}
$$

* like $C_p$, BIC will tend to take on a small value for a model with a low test error, and so generally we select the model for which BIC is smallest
* notice that BIC replaces the $2d\hat{\sigma}^2$ term in $C_p$ with a $\log(n)d\hat{\sigma}^2$ term
    * this is a stronger penalty than $C_p$, and so BIC tends to favor smaller models than $C_p$
    * in particular, when $n \geq 8$, $\log(n) \geq 2$, so BIC places a heavier penalty on the number of parameters
    * this is sometimes referred to as a *Bayesian Occam's razor*

#### 6.8.4 Adjusted $R^2$

* for a least squares model with $d$ variables, the adjusted $R^2$ statistic is calculated as
$$
\text{Adjusted } R^2 = 1 - \frac{\text{RSS}/(n-d-1)}{\text{TSS}/(n-1)}
$$

* here $\text{TSS} = \sum_{i=1}^n(y_i - \bar{y})^2$ is the total sum of squares
* unlike $C_p$, AIC, BIC, for which a *small* value indicates a model with a low test error, a *large* value of adjusted $R^2$ indicates a model with a low test error
* maximizing the adjusted $R^2$ is equivalent to minimizing $\text{RSS} / (n-d-1)$
    * while $\text{RSS}$ is guaranteed to decrease as more variables are added to the model, $\text{RSS} / (n-d-1)$ may increase or decrease, due to the presence of the $(n-d-1)$ term in the denominator
* unlike the $R^2$ statistic, the adjusted $R^2$ statistic *pays a price* for the inclusion of unnecessary variables in the model

#### 6.8.5 Validation and cross-validation

* each of the procedures returns a sequence of models $\mathcal{M}_0, \dots, \mathcal{M}_p$ indexed by the number of variables
    * our job here is to select a single model from among these
* we compute the vaidation set error or the cross-validation error for each model, and then select the model for which the resulting estimated test error is smallest
* this procedure has an advantage relative to AIC, BIC, $C_p$, and adjusted $R^2$, in that it provides a direct estimate of the test error, and *does not require an estimate of the error variance $\hat{\sigma}^2$*
* it can also be used in a wider range of model selection tasks, even in cases where it is hard to pinpoint the model degrees of freedom $d$ or hard to estimate the error variance $\hat{\sigma}^2$
* **DON'T CHOOSE THE SMALLEST CV ERROR, CHOOSE THE SIMPLEST MODEL *WITHIN ONE STANDARD DEVIATION* OF THE SMALLEST MEAN CV ERROR**