Here the class of functions is controlled by explicitly penalizing [[Residual Sum of Squares (RSS)|RSS(f)]] with a roughness penalty:

$\text{PRSS}(f;\lambda) = \text{RSS}(f) + \lambda J(f)$

- $J(f)$ - user-selected [[Functional|functional]] is large for functions $f$ that vary too rapidly over small regions of the input space
	- Example: [[Cubic splines are piecewise cubic polynomial with continuous derivatives up to order 2 at each knot|Cubic smoothing splines]] for one-dimensional inputs is the solution to the [[Penalized Least Squares|penalized least squares criterion]]: 
	  
	  $\text{PRSS}(f;\lambda) = \text{RSS}(f) + \lambda \int [f''(x)]^2 dx$

- [[Regularization|Penalty functions]] $J$ can be constructed for functions in any dimension
	- Special versions can be created to impose special structure

- [[Regularization|Penalty function, or regularization methods]] express a prior belief that functions we seek have a certain type of smooth behavior