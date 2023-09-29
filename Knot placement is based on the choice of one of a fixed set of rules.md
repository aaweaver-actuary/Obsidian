- Quantile-based [[Knots in Cubic Splines|knot]] placement - place [[Knots in Cubic Splines|knots]] at quantiles of the data
- Expert-based [[Knots in Cubic Splines|knot]] placement - place [[Knots in Cubic Splines|knots]] at known important values
- Equally-spaced [[Knots in Cubic Splines|knot]] placement - place [[Knots in Cubic Splines|knots]] at  equally spaced intervals along the range of the data
- Optimal [[Knots in Cubic Splines|knot]] placement - place [[Knots in Cubic Splines|knots]] at the points where the [[Residual Sum of Squares (RSS)|RSS]] is minimized
    _ this is a computationally intensive approach
    _ can be #approximated by a #forward-stepwise algorithm
- a [[Cubic splines have 0th, 1st, 2nd derivatives equal to 0 at the knot|cubic spline]] with $K$ knots uses a total of $K+4$ #basis-function's / [[Degrees of Freedom|degrees of freedom]] / parameters
- a [[Natural cubic splines add extra constraints to cubic splines to pick boundary knots automatically|natural cubic spline]] with $K$ [[Knots in Cubic Splines|knots]] uses a total of $K$ basis functions/degrees of freedom/parameters