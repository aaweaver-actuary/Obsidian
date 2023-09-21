- A function is convex if a line segment between any two points on the function lies above the function itself.
    - This property is useful for optimization as it ensures a single global minimum.
- a 1-D function $f: \mathbb{R} \rightarrow \mathbb{R}$ is convex if $f''(x) \ge 0$ for all $x \in \mathbb{R}$
    - for multivariate case, a function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is convex if its [[Hessian matrix]] is [[Definition of positive semi-definite|positive semi-definite]]

### In general

A function $f:\mathbb{R}^n \rightarrow \mathbb{R}$ is convex if for all $x,y \in \mathbb{R}^n$ and for all $\lambda \in [0,1]$, the following inequality holds:

$$
f(\lambda x + (1-\lambda)y) \le \lambda f(x) + (1-\lambda)f(y)
$$

### The point

Convex functions are useful in [[Optimization|optimization]] problems, because they guarantee a global minimum

### Checking convexity

- check the mathematical properties directly
- For a function:
	- See if it satisfies the convex inequality or its second derivative is negative
- For an optimization problem:
	- Confirm that the objective is a convex function
	- Check whether the constraints form a [[Convex sets|convex set]][^1]

[[Examples of convex sets, useful for optimization]]


[^1]: [[Convex sets]]