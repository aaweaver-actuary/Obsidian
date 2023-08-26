- Quantile-based #knot placement - place #knot's at #quantiles of the data
- Expert-based #knot placement - place #knot's at known important values
- Equally-spaced #knot placement - place #knot's at  equally spaced intervals along the range of the data
- Optimal #knot placement - place #knot's at the points where the #RSS is minimized
    _ this is a computationally intensive approach
    _ can be #approximated by a #forward-stepwise algorithm
- a #cubic-spline [^1] with $K$ knots uses a total of $K+4$ #basis-functions / #degrees-of-freedom / #parameter's
- a #natural-cubic-spline [^2] with $K$ knots uses a total of $K$ basis functions/degrees of freedom/parameters

[^1]: [[Cubic splines have 0th, 1st, 2nd derivatives equal to 0 at the knot]]
[^2]: [[Natural cubic splines add extra constraints to cubic splines to pick boundary knots automatically]]