
* A #natural-cubic-spline #extrapolates a linear function beyond the boundary #knots.
* Adds 4 = 2 * 2 extra #constraints to the #cubic-spline:
	* $f''(\xi_1) = 0$
	* $f''(\xi_K) = 0$
* allows us to put more internal #knots for the same #degrees-of-freedom as a regular #cubic-spline
    * because we don't have to worry about the boundary knots