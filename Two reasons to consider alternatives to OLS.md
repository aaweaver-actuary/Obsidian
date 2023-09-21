

### Why consider alternatives to [[Ordinary Least Squares (OLS)|OLS]]?

1. #prediction-accuracy
    - [[Ordinary Least Squares (OLS)|OLS]] will perform well if $n$ is large relative to $p$ (number of features)
    - when $p > n$, look at alternatives to control [[Variance|variance]] of the estimates
        - in this case [[Ordinary Least Squares (OLS)|least squares]] is not even defined
2. #interpretability

- by removing irrelevant features
    - eg by setting their coefficients to zero
- we obtain a model that is easier to interpret
    - we will present some approaches for automatically performing feature selection
        - ie for automatically identifying a subset of the $p$ predictors that we believe to be related to the response
