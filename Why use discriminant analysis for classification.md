Why use #discriminant-analysis?
- When the classes are #well-separated, the #parameter estimates for the #logistic-regression model[^1] are surprisingly #unstable.
  - #linear-discriminant-analysis does not suffer from this problem.
- If $n$ is small and the #distribution of the predictors $X$ is approximately a #normal-distribution in each of the classes, the #linear-discriminant-analysis model is again more #stable than the #logistic-regression model.
- #linear-discriminant-analysis is popular when we have more than two response classes.
  - there is no straightforward #generalization of the #logistic-regression model to a #multi-class response.
  - #linear-discriminant-analysis provides #low-dimensional views of the data.
- Under the #assumption that the #normal-distribution is the correct one, #Bayes-theorem is the absolute best we can do.
  - #linear-discriminant-analysis is #asymptotically-equivalent-to the #bayes-optimial-classifier[^2]
  - #quadratic-discriminant-analysis is not.
  - #quadratic-discriminant-analysis is more flexible than #linear-discriminant-analysis, but can suffer from #overfitting
  - This is probably rarely the case in practice, but it is a nice property to have.

[^1]: [[Logistic regression is linear regression on the log-odds]]
[^2]: [[the Bayes optimal classifier is the one that assigns each observation to the most likely class, given its predictor values]]
