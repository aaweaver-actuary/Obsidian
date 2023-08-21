#statistical-learning 

- if we can compute #inner-products between observations, we can fit #support-vector-classifiers 
- some special #kernels can do this for us:
$$
K(x_i, x_{i'}) = \left( 1+\sum_{j=1}^p x_{ij}x_{i'j} \right)^d \hspace{20em}
$$
	- this computes the #inner-products needed for $d$-dimensional polynomials
		- $\binom{p+d}{d}$ #basis-functions 

- a #kernel-function is a function of two arguments that computes #inner-products 
- The solution has the form
  $$
 f(x) = \beta_0 + \sum_{i\in\mathcal{S}} \hat{\alpha}_i K(x, x_i)  \hspace{21em}
 $$
 
 [[One of the most popular kernels is the radial kernel]]
 