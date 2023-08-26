* #standard-error's can also be used to perform #hypothesis-test's on the #coefficient's

* the most common #hypothesis-test involves testing:
    * $H_0$: There is no relationship between $X$ and $Y$ #null-hypothesis
    * $H_1$: There is some relationship between $X$ and $Y$ #alternative-hypothesis

* here $H_0$ is called the #null-hypothesis, and is the model where $\beta_1 = 0$
* $H_1$ is called the #alternative-hypothesis, and is the model where $\beta_1 \neq 0$
* Mathematically, this corresponds to testing:
    * $H_0$: $\beta_1 = 0$ vs
    * $H_1$: $\beta_1 \neq 0$
    * this is because if $\beta_1 = 0$, then the model reduces to $Y = \beta_0 + \epsilon$, and so $X$ is not associated with $Y$
* To test $H_0$, we compute a #t-statistic, given by

$$

t = \frac{\hat{\beta}_1 - 0}{SE(\hat{\beta}_1)}

$$

* the #t-statistic measures the number of #standard-deviations that $\hat{\beta}_1$ is away from 0
* #assuming $\beta_1 = 0$, the #t-statistic follows a #t-distribution with $n-2$ #degrees-of-freedom
* then use #statistical-software to compute the #probability of observing any value equal to $|t|$ or larger
* this #probability is called the #p-value

[[Assess the accuracy of a linear regression model using standard errors, confidence intervals, and hypothesis testing]]
[[Assess the overall accuracy of the model by computing the residual standard error, an estimate of the standard deviation of the error]]
