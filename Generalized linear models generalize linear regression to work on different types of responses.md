
- [[Linear Regression|Linear regression]] is used for quantitative target
- [[Logistic Regression|Logistic regression]] is the counterpart for binary target
    - models the #logit of the probability of class membership as a linear function of the features
- other response types exist:
    - #count-data -> [[Poisson Regression]]
    - non-negative data -> [[Tweedie Regression]]
    - skewed distributions -> [[Gamma Regression]]
- all these models are a #special-case of the generalized [[Linear Model|linear model]]
    - the response $Y$ is assumed to follow some distribution in the [[Exponential Family of Distributions|exponential family]]
    - the mean of $Y$ is related to the linear predictor via a [[Link Function - the transformation of the mean that is represented by the linear model|link function]]
    - the linear predictor is a [[Linear Combination|linear combination]] of the features

### Generalized Linear Model (GLM)

- so far have covered three types of generalized linear model:
    - [[Linear Regression]]
    - [[Logistic Regression]]
    - [[Poisson Regression]]
- each of these has a characteristic [[Link Function - the transformation of the mean that is represented by the linear model|link function]]
- each also has a #characteristic-variance-function
- the models are fit by [[Maximum likelihood is used to fit linear regression parameters|maximum likelihood]]
- other types of generalized linear model include:
    - [[Gamma Regression]]
    - [[Tweedie Regression]]
    - [[Negative Binomial Regression]]
    - [[Inverse Gaussian Regression]]
    - more
