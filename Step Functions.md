## Piecewise polynomials

Instead of a single polynomial $X$ over its whole domain, use different polynomials in regions defined by [[Knots in Cubic Splines|knots]], eg:

$$
y_i = \left\{\begin{align}
\beta_{01} + \beta_{11}x_i + \beta_{21}x_i^2 + \beta_{31}x_i^3 \space \space\space &\text{ if } x_i < c; \\
\beta_{02} + \beta_{12}x_i + \beta_{22}x_i^2 + \beta_{32}x_i^3 \space \space\space &\text{ if } x_i \ge c; \\
\end{align}\right.
$$

- better to add constraints to the polynomials, eg continuity
- [[A spline is continuous at the knots|Splines]] have the "maximum" amount of [[A spline is continuous at the knots|continuity]]

## 7.2.1 Different types

1. #Piecewise-cubic - nothing special here: just a cubic polynomial fit on the left and right side of the breakpoint
    - very unlikely to be continuous
2. #Continuous-piecewise-cubic - same as above, but enforce continuity at the break point
