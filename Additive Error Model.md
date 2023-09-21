Suppose our data arose from a [[Linear Model|linear model]]$$
\begin{align}
Y = f(X)+\epsilon, \text{ }&\text{where }\\ &E[\epsilon] = 0, \text{ and}\\
&\epsilon \perp X
\end{align}
$$
- For this model, the [[Regression Function|regression function]] is $f(x)=E[Y|X=x]$ 
	- here the conditional distribution depends on $X$ *only* through the conditional mean $f(x)$ 

This additive error model is a useful approximation to the truth:
- For most systems the input-output pairs $(X, Y)$ will not have a deterministic relationship $Y=f(X)$ - there will be:
	- other unmeasured variables