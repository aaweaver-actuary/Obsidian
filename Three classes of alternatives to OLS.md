

1. [[Subset Selection in Linear Model Selection and Regularization]] - we identify a subset of the $p$ features that we believe to be related to the response[^1]
    * we then fit a model using [[Ordinary Least Squares (OLS)|least squares]] on the reduced set of variables
2. [[Shrinkage in Linear Model Selection and Regularization]] - we fit a model involving all $p$ predictors, but the estimated coefficients are shrunken towards zero relative to the [[Ordinary Least Squares (OLS)|least squares]] estimates
    * this [[Shrinkage in Linear Model Selection and Regularization|shrinkage]] (aka [[Regularization|regularization]]) has the effect of reducing [[Variance|variance]] of the fitted coefficients, and can also perform variable selection
    * [[Shrinkage in Linear Model Selection and Regularization|shrinkage]] methods can also be viewed as *constrained* versions of [[Ordinary Least Squares (OLS)|least squares]]
3. *dimension reduction* - we project the $p$ predictors into a $M$-dimensional subspace, where $M < p$
    * this is achieved by computing $M$ different [[Linear Combination|linear combinations]], or *projections*, of the variables
    * then these $M$ projections are used as predictors to fit a [[Linear Regression|linear regression]] model by [[Ordinary Least Squares (OLS)|least squares]]
    * we will look at two approaches: *principal components regression* and *partial least squares*

[^1]: see also [[Stepwise Selection in Linear Model Selection and Regularization]]