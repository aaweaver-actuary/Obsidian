- [[Linear regression is a simple approach to supervised learning]]
- Also called [[Ordinary Least Squares (OLS)]]
- [[Linear regression assumes the dependence of Y on X is approximately linear]]
	- The [[Linear Model|model]] is linear in its parameters
- [[Assess the accuracy of a linear regression model using standard errors, confidence intervals, and hypothesis testing]]

- [[Multiple linear regression]]

- [[The ideal scenario for interpreting regression coefficients is when they are uncorrelated]]
- For prediction purposes, [[Linear Model|linear models]] can sometimes outperform nonlinear models, especially in situations with small numbers of training cases
	- Eg [[Modeling low signal-to-noise or sparse data|low signal-to-noise or sparse data]]
- [[Residual Sum of Squares (RSS) Criterion for linear regression]]
- [[How do we minimize the residual sum of squares (RSS)]]
- [[Geometric Representation of the Least Squares Estimate]]
- [[Linear regression when the columns of X are not linearly independent]]

### Distributional assumptions
- Assume observations $y_i$ are uncorrelated and have constant [[Variance|variance]] $\sigma^2$
- Assume the $x_i$ are fixed - not random
- Then the [[Variance-Covariance Matrix|variance-covariance matrix]] of the [[Ordinary Least Squares (OLS)|least squares]] parameter estimates:$$
  \text{Var}(\hat{\beta}) = (\mathbf{X}^T\mathbf{X})^{-1}\sigma^2 \hspace{10em}
  $$where$$
  \hat{\sigma}^2 = \frac{1}{N-p-1} \sum_{i=1}^N (y_i - \hat{y}_i)^2
  $$
### Additional assumptions needed for inference

We assume that$$
Y = \beta_0 \sum_{j=1}^p X_j\beta_j + \varepsilon, \text{ where } \varepsilon \sim N(0, \sigma^2).
$$This implies that$$
\hat{\beta} \sim N\left[\beta, (\mathbf{X}^T\mathbf{X})^{-1}\sigma^2\right]
$$