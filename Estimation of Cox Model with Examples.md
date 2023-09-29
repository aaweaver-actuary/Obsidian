[[Survival Analysis]]

- [[Cox Proportional Hazards Model]]
- [[Cox Proportional Hazards Model - Partial Likelihood]]
- [[Cox Proportional Hazards Model - Connection with Log-Rank Test]]

## Additional Details

- [[There is no intercept in the Cox Proportional Hazards model]]
- We assume here that there are no tied failure times
	- if there are, the exact form of the [[Partial Likelihood|partial likelihood]] becomes complicated and a number of computational approximations must be used
- The [[Partial Likelihood|partial likelihood]] gets its name because it is not exactly a [[Likelihood|likelihood]] 
	- But it is a very good approximation
- We have focused only on the estimation of  coefficients $\beta$.
	- We could want to estimate the #baseline-hazard $h_0(t)$
	- This can help us estimate the [[Survival Curve|survival curve]] $S(t|x)$
	- Need computational techniques - use a computer