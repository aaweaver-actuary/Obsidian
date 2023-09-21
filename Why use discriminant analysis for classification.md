Why use [[Discriminant analysis for classification|discriminant analysis]]?
- When the classes are well-separated, the parameter estimates for the [[Logistic Regression|logistic regression]] model[^1] are surprisingly unstable.
  - [[Linear Discriminant Analysis|linear discriminant analysis]] does not suffer from this problem.
- If $n$ is small and the distribution of the predictors $X$ is approximately a [[Gaussian|Gaussian distribution]] in each of the classes, the [[Linear Discriminant Analysis|linear discriminant analysis]] model is again more stable than the [[Logistic Regression|logistic regression]] model.
- [[Linear Discriminant Analysis|Linear discriminant analysis]] is popular when we have more than two response classes.
  - there is no straightforward generalization of the [[Logistic Regression|logistic regression]] model to a multi-class response.
  - [[Linear Discriminant Analysis|Linear discriminant analysis]] provides low-dimensional views of the data.
- Under the assumption that the [[Gaussian|Gaussian distribution]] is the correct one, [[Bayes' Theorem for classification|Bayes theorem]] is the absolute best we can do.
  - [[Linear Discriminant Analysis|Linear discriminant analysis]] is asymptotically equivalent to the [[the Bayes optimal classifier is the one that assigns each observation to the most likely class, given its predictor values|Bayes optimal classifier]][^2]
  - #quadratic-discriminant-analysis is not.
  - #quadratic-discriminant-analysis is more flexible than [[Linear Discriminant Analysis|linear discriminant analysis]], but can suffer from [[Overfitting|overfitting]]
  - This is probably rarely the case in practice, but it is a nice property to have.

[^1]: [[Logistic regression is linear regression on the log-odds]]
[^2]: [[the Bayes optimal classifier is the one that assigns each observation to the most likely class, given its predictor values]]
