#statistical-learning

### Background

- With #neural-network's, it seems better to have too many #hidden-node's than too few
    - likewise more #hidden-layer's are better than fewer
- running #sgd until zero #training-error often gives good #test-error
- increasing the number of #hidden-node's or #hidden-layer's and again training to zero #training-error sometimes gives **even better** #test-error

### Question

- What happened to #overfitting and the usual #bias-variance-tradeoff?

### Simulation

- $y=\sin (x) + \varepsilon$ with $x \sim U[-5, 5]$ and $\varepsilon \sim N(\mu, \sigma=0.3)$
- #training-set $n=20$, #test-set very large ($n > 10,000$)
- fit a #natural-cubic-spline to the data[^1] with $d$ #degrees-of-freedom 
	- ie a #linear-regression onto $d$ #basis-functions:
$$
\begin{align}
\hat{y}_i = \hat{\beta}_1 N_1(x_i) + \hat{\beta}_2 N_2(x_i) + \cdots + \hat{\beta}_d N_d(x_i) 
\end{align}
$$
- when $d=20$ we fit the #training-set exactly
	- all #residual's equal to zero
- when $d>20$, we still fit the #training-set exactly, but the solution is not unique
	- among the zero #residual solutions, pick the one with smallest #norm 
		- ie the zero #residual solution with smallest $\sum_{j=1}^d \hat{\beta}_j^2$ 
- when $d \le 20$, the model is #OLS and we see the usual #bias-variance-tradeoff 
- when $d>20$, we revert to the minimum #norm
- as $d$ increases above 20, $\sum_{j=1}^d \hat{\beta}_j^2$ decreases since it is easier to achieve zero #training-error, and hence less #wiggly solutions

### Results
- you see #training-error decrease until it hits exactly 0
- you see #test-error follow the usual #bias-variance-tradeoff when $d \le 20$
	- ie #test-error gets very high (above the top of the chart) as you approach $d=20$ from the left
- surprise is the #double-descent

[[You see less wiggly solutions with double descent]]

![[Simulation to understand double descent.ipynb]]
![[Simulation to understand double descent.html]]




[^1]: [[Natural cubic splines add extra constraints to cubic splines to pick boundary knots automatically]]