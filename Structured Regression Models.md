Consider the [[Residual Sum of Squares (RSS)|RSS criterion]] for an arbitrary function $f$:$$
\text{RSS}(f) = \sum_{i=1}^N \left(y_i - f(x_i) \right)^2
$$Minimizing this leads to infinitely many solutions.

- In order to obtain useful results for finite $N$, we must restrict $f$ to be in a smaller set of functions
- In general the restrictions are [[Complexity]] restrictions of some kind
- Any method that tries to produce locally-varying functions in small neighborhoods will run into [[The Curse of Dimensionality|problems in high dimensions]]
	- Conversely, any method that overcomes [[The Curse of Dimensionality|the curse of dimensionality]] has an associated metric for measuring neighborhoods
		- this metric does not allow the neighborhood to be small in all directions at the same time

[[Roughness Penalty]]