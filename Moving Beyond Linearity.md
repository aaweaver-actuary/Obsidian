* the truth is never linear 
* often it is good enough
* when it isn't:
    * [[Polynomial regression is linear regression with higher-order terms]]
    * [[Step Functions]]
    * [[Linear splines are piecewise linear polynomial continuous at each knot]]
    * [[Cubic splines are piecewise cubic polynomial with continuous derivatives up to order 2 at each knot]]
	    * [[Natural cubic splines add extra constraints to cubic splines to pick boundary knots automatically]]
    * local regression
    * generalized additive models (GAMs) [[GAMs are a generalization of linear models that allow for flexible nonlinearities in several variables, without losing the additivity of a linear model|generalized additive models (GAMs)]]
    
* these offer a lot of flexibility without losing the ease and interpretability of [[Linear Model|linear models]]



# 7.2 Piecewise Polynomials & Splines

- instead of a single polynomial $X$ over its whole domain, use different polynomials in regions defined by [[Knots in Cubic Splines|knots]], eg:
$$
y_i = \left\{\begin{align}
\beta_{01} + \beta_{11}x_i + \beta_{21}x_i^2 + \beta_{31}x_i^3 \space \space\space &\text{ if } x_i < c; \\
\beta_{02} + \beta_{12}x_i + \beta_{22}x_i^2 + \beta_{32}x_i^3 \space \space\space &\text{ if } x_i \ge c; \\ 
\end{align}\right.
$$
- better to add constraints to the polynomials, eg continuity
- [[A spline is continuous at the knots|Splines have maximum continuity]]

## 7.2.1 Different types
1. **Piecewise cubic** - nothing special here: just a cubic polynomial fit on the left and right side of the breakpoint 
	- very unlikely to be continuous
2. **Continuous piecewise cubic** - same as above, but enforce continuity at the break point
3. **Cubic spline** - same as above, but also enforce continuous 1st and 2nd derivatives
	- can't go further than 2nd for a *cubic* spline -- if all 3 derivatives are continuous it would just be a polynomial
	- the belief is that the discontinuity in the 3rd derivative is not detectable by the human eye
4. **Linear spline** - linear on the left and right side -- can only enforce continuity at the zeroth degree since this is based on polynomials of degree 1

# 7.3 Smoothing Splines

Smoothing splines are a way of fitting splines without having to worry about the number or placement of the knots

Criterion for fitting a smooth function $g(x)$ to some data:

$$
\min_{g\in S}\sum_{i=1}^n(y_i - g(x_i))^2 + \lambda\int g''(t)^2dt
$$

* the first term is the [[Residual Sum of Squares (RSS)|RSS]]
* the second term is a penalty on the roughness of $g$
    * if we didn't have this 2nd term, the solution would be some wild polynomial that goes through every point
* the $\lambda$ is a tuning parameter that controls the roughness penalty
		* $\lambda$ = 0 means we don't care about the [[Roughness Penalty|roughness penalty]]
		* $\lambda$ = $\infty$ means we only care about the roughness penalty
		* the smaller $\lambda$ is, the more wiggly the function will be, eventually going through every point
		* the larger $\lambda$ is, the smoother the function will be, eventually being a straight line

## 7.3.1 Solution

* the solution to the above minimization problem is a natural cubic spline with knots at each unique value of $x_i$
* the $\lambda$ controls the wiggliness of the function

## 7.3.2 Details

* smoothing splines avoid the knot selection issue by using all the knots
* there is a single tuning parameter $\lambda$ that controls the amount of wiggliness
* the vector of $n$ fitted values can be written as $\hat{\mathbf{g}}_{\lambda}=\mathbf{S}_{\lambda}\mathbf{y}$ where $\mathbf{S}_{\lambda}$ is an $n\times n$ matrix that depends on $\lambda$
    * this is a **linear smoother**, because it is a linear operator on the $y_i$'s
    * [[Linear Regression|Linear regression]] is also a linear operation on $y$
* the **effective degrees of freedom** of a smoothing spline is given by

$$
\begin{align}
df_{\lambda} =& \text{ trace}(\mathbf{S}_{\lambda}) \\
=& \sum_{i=1}^n \left\{ S_{\lambda} \right\}_{ii}
\end{align}
$$

* you might think the degrees of freedom would be $n$ since we have $n$ knots, but the penalty term reduces the effective degrees of freedom
    * a natural adjustment to get effective degrees of freedom is to take the trace of the smoothing matrix
    * when you think about it, it is like a polynomial of degree $n-1$ with $n$ knots, but the degrees of freedom are not all "spent" on the knots

## 7.3.3 Choosing $\lambda$

* because of the nice expression for the effective degrees of freedom, we can specify the degrees of freedom and solve for $\lambda$
* the leave-one-out cross-validation error is given by

$$
\begin{align}	
\text{RSS}_{CV}(\lambda) =& \sum_{i=1}^n(y_i - \hat{g}_{\lambda}^{(-i)}(x_i))^2 \\
=& \sum_{i=1}^n\left(\frac{y_i - \hat{g}_{\lambda}(x_i)}{1 - S_{\lambda ii}}\right)^2
\end{align}
$$

* compute this for a range of $\lambda$ values and choose the one that minimizes the CV error

# 7.4 Local Regression

* **local regression** is a generalization of splines
* with a sliding weight function, we can fit a linear regression model at each of a set of regions by weighted least squares
    * called **loess** (locally estimated scatterplot smoothing)
* the two main ways to do smoothing are splines and local regression  
    * splines are more interpretable
    * local regression is more flexible

# 7.5 Generalized Additive Models

[[GAMs are a generalization of linear models that allow for flexible nonlinearities in several variables, without losing the additivity of a linear model]]
