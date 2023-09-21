
* the [[Standard errors can also be used to perform hypothesis tests on model coefficients|standard error]] of an estimator reflects how it varies under repeated sampling$$
\begin{align}
\text{SE}(\hat{\beta}_1)^2 =& \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2}\\


\text{SE}(\hat{\beta}_0)^2 =& \space \sigma^2\left[  \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i-\bar{x})^2} \right] \\

\sigma^2 =& \text{Var}(\epsilon)
\end{align}
$$
* the [[Standard errors can also be used to perform hypothesis tests on model coefficients|standard error]] can be used to compute [[Confidence Intervals|confidence intervals]]
* the 95% [[Confidence Intervals|confidence interval]] is defined as the range of values such that with 95% probability, the range will contain the true unknown value of the parameter
* the [[Confidence Intervals|confidence interval]] takes the form
$$
\hat{\beta}_1 \pm 2 \cdot \text{SE}(\hat{\beta}_1)
$$
* this means that is there an approximate 95% chance that the interval
$$
\left[ \hat{\beta}_1 - 2 \cdot \text{SE}(\hat{\beta}_1), \hat{\beta}_1 + 2 \cdot \text{SE}(\hat{\beta}_1) \right]
$$
	will contain the true value of $\beta_1$ (under a scenario where we got repeated samples like the one we actually observed)

[[Standard errors can also be used to perform hypothesis tests on model coefficients]]

[[Assess the overall accuracy of the model by computing the residual standard error, an estimate of the standard deviation of the error]]
