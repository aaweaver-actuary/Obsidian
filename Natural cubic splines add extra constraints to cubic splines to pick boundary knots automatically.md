
* A [[Natural cubic splines add extra constraints to cubic splines to pick boundary knots automatically|natural cubic spline]] #extrapolates a linear function beyond the boundary [[Knots in Cubic Splines|knots]].
* Adds 4 = 2 * 2 extra #constraints to the [[Cubic splines have 0th, 1st, 2nd derivatives equal to 0 at the knot|cubic spline]]:
	* $f''(\xi_1) = 0$
	* $f''(\xi_K) = 0$
* allows us to put more internal [[Knots in Cubic Splines|knots]] for the same [[Degrees of Freedom|degrees of freedom]] as a regular [[Cubic splines have 0th, 1st, 2nd derivatives equal to 0 at the knot|cubic spline]]
    * because we don't have to worry about the boundary [[Knots in Cubic Splines|knots]]