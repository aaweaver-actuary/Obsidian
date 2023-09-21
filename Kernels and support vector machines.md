

- if we can compute [[Inner Product|inner products]] between observations, we can fit a [[Support Vector Classifier|support vector classifier]]
- some special [[Kernel functions are functions of two variables that compute inner products|kernel functions]] can do this for us:
$$
K(x_i, x_{i'}) = \left( 1+\sum_{j=1}^p x_{ij}x_{i'j} \right)^d \hspace{20em}
$$
	- this computes the [[Inner Product|inner products]] needed for $d$-dimensional polynomials
		- $\binom{p+d}{d}$ #basis-function's 

- a [[Kernel functions are functions of two variables that compute inner products|kernel function]] is a function of two arguments that computes [[Inner Product|inner products]] 
- The solution has the form
  $$
 f(x) = \beta_0 + \sum_{i\in\mathcal{S}} \hat{\alpha}_i K(x, x_i)  \hspace{21em}
 $$
 
 [[One of the most popular kernels is the radial kernel]]
 