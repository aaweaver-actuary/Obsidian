

- [[GAMs are a generalization of linear models that allow for flexible nonlinearities in several variables, without losing the additivity of a linear model|GAMs]] are a generalization of [[Linear Model|linear models]] that allow for a flexible nonlinear structure in several variables, without losing the [[Additive Models|additive model]] structure:
    $$
    y_i = \beta_0 + f_1(x_{i1}) + f_2(x_{i2}) + \cdots + f_p(x_{ip}) + \epsilon_i
    $$
- the $f_j$'s are unspecified #smooth-function's

## 7.5.1 Details

- can be fit simply using [[Natural cubic splines add extra constraints to cubic splines to pick boundary knots automatically|natural cubic splines]]:

```R
lm(wage ~ ns(age, df=4) + ns(year, df=4) + education, data=Wage)
```

- [[GAM coefficients are not really interesting, but the smooth functions are]]
- can plot the smooth functions using `plot.gam()`
- can mix terms -- some linear, some nonlinear
    - then use `anova()` to compare models and test if the nonlinear terms are significant
- can use #smoothing-spline's or #local-regression as well:

```R
gam(wage ~ lo(age, span=.5) + s(year, df=4) + education, data=Wage)
```

- [[GAMs are a generalization of linear models that allow for flexible nonlinearities in several variables, without losing the additivity of a linear model|GAMs]] are additive, though low-order interactions can be added in a natural way
    - eg by using #bivariate-smoother's or interactions of the form $f_1(x_1)f_2(x_2)$

## [[GAMs are a generalization of linear models that allow for flexible nonlinearities in several variables, without losing the additivity of a linear model|GAMs]] for [[Classification|Classification]] Problems

$$
\log \left( \frac{p(X)}{1-p(X)} \right) = \beta_0 + f_1(X_1) + f_2(X_2) + \cdots + f_p(X_p)
$$

- when you do a plot, it will plot the contribution of each variable to the log-odds
    - the probabilities are not additive, but the log-odds are
