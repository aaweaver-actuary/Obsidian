### Background

- With [[Neural Networks|neural networks]], it seems better to have too many #hidden-node's than too few
    - likewise more [[Hidden Layers In a Neural Network|hidden layers]] are better than fewer
- running [[Stochastic Gradient Descent (SGD)|SGD]] until zero [[Training Error|training error]] often gives good [[Testing Error|test error]]
- increasing the number of #hidden-node's or [[Hidden Layers In a Neural Network|hidden layers]] and again training to zero [[Training Error|training error]] sometimes gives **even better** [[Testing Error|test error]]

### Question

- What happened to [[Overfitting|overfitting]] and the usual [[Bias-variance trade-off in statistical learning|bias-variance tradeoff]]?

### Simulation

- $y=\sin (x) + \varepsilon$ with $x \sim U[-5, 5]$ and $\varepsilon \sim N(\mu, \sigma=0.3)$
- training set $n=20$, test set very large ($n > 10,000$)
- fit a #natural-cubic-spline to the data[^1] with $d$ #degrees-of-freedom 
	- ie a [[Linear Regression|linear regression]] onto $d$ #basis-function's:
$$
\begin{align}
\hat{y}_i = \hat{\beta}_1 N_1(x_i) + \hat{\beta}_2 N_2(x_i) + \cdots + \hat{\beta}_d N_d(x_i) 
\end{align}
$$
- when $d=20$ we fit the training set exactly
	- all [[Residual|residuals]] equal to zero
- when $d>20$, we still fit the training set exactly, but the solution is not unique
	- among the zero [[Residual|residual]] solutions, pick the one with smallest #norm 
		- ie the zero [[Residual|residual]] solution with smallest $\sum_{j=1}^d \hat{\beta}_j^2$ 
- when $d \le 20$, the model is [[Ordinary Least Squares (OLS)|OLS]] and we see the usual [[Bias-variance trade-off in statistical learning|bias-variance tradeoff]] 
- when $d>20$, we revert to the minimum #norm
- as $d$ increases above 20, $\sum_{j=1}^d \hat{\beta}_j^2$ decreases since it is easier to achieve zero [[Training Error|training error]], and hence less #wiggly solutions

### Results
- you see [[Training Error|training error]] decrease until it hits exactly 0
- you see [[Testing Error|test error]] follow the usual #bias-variance-tradeoff when $d \le 20$
	- ie [[Testing Error|test error]] gets very high (above the top of the chart) as you approach $d=20$ from the left
- surprise is the [[Double Descent|double descent]]

[[You see less wiggly solutions with double descent]]

![[Simulation to understand double descent.ipynb]]
![[Simulation to understand double descent.html]]




[^1]: [[Natural cubic splines add extra constraints to cubic splines to pick boundary knots automatically]]