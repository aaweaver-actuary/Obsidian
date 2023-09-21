- Parameters in a [[Ordinary Least Squares (OLS)|least squares]] [[Linear Regression|linear regression]] are generally selected to minimize the [[Residual Sum of Squares (RSS)|residual sum of squares]]:$$
\text{RSS}(\beta) = \sum_{i=1}^N \left( y_i - \beta_0 - \sum_{j=1}^p x_{ij}\beta_j \right)^2
$$
* From a statistical point of view, this is a reasonable criterion if the training observations $(x_i, y_i)$ represent independent random draws from their population
	* or at least if the $y_i$ are conditionally independent given the inputs $x_i$
* This makes no assumption about the reasonability/validity of a [[Linear Model|linear model]] - it is simply the best linear fit to the data