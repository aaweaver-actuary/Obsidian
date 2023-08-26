#regression 

$$
y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \beta_3 x_i^3 + \cdots + \beta_d x_i^d + \epsilon_i
$$
## 7.1.1 Details
* create new variables $X_1 = X$, $X_2 = X^2$, $X_3 = X^3$, etc. and then treat as #multiple-linear-regression
* not really interested in the individual #coefficient's, but rather the overall shape of the #curve at a value $x_0$:
$$

\hat{f}(x_0) = \hat{\beta}_0 + \hat{\beta}_1 x_0 + \hat{\beta}_2 x_0^2 + \hat{\beta}_3 x_0^3 + \cdots + \hat{\beta}_d x_0^d

$$
* since $\hat{f}(x_0)$ is a #linear-function of the $\hat{\beta}_j$, we can get a simple expression for #pointwise #variance's $\text{Var}(\hat{f}(x_0))$ at any value $x_0$