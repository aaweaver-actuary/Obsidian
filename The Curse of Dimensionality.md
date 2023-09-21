Consider the [[k-Nearest Neighbors|nearest neighbor]] procedure for inputs uniformly distributed in a $p$-dimensional hypercube.
- We send out a hypercubical neighborhood about a target point to capture a fraction $r$ of the unit volume
- Expected edge length: $e_p(r) = r^{1/p}$
- For $p=10$:
	- $e_{10}(0.01)=0.63$
	- $e_{10}(0.1)=0.80$
	- this means that to capture either 1% or 10% of the data to form a local average, we must cover 63% or 80% of the range of each input variable
		- this is really not a "local" range
		- this is not really improved by reducing $p$, since fewer observations in the average $\implies$ higher variance of fit

[[Another consequence of the sparse sampling in high dimensions is that all sample points are close to an edge of the sample]]
