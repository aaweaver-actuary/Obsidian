

* we have fit a model $\hat{f}(x)$ to a training set $\text{Tr}$, and we let $(x_0, y_0)$ be a test observation not in the training set
* if the true model is $Y=f(X)+\epsilon$ (with $f(x)=E(Y|X=x)$), then the expected [[Testing Error|test error]] [[Mean Squared Error (MSE)|MSE]] at $x_0$ is given by
	* $E\left( y_0 -\hat{f}(x_0)\right)^2 = \text{Var}(\hat{f}(x_0)) + \text{Bias}^2(\hat{f}(x_0)) + \text{Var}(\epsilon)$
* the expectation averages over the variability in $y_0$ and over the variability in the training set $\text{Tr}$  
* note that:  
	* $\text{Bias}(\hat{f}(x_0)) = E\left( \hat{f}(x_0) \right) - f(x_0)$ and
	* $\text{Var}(\hat{f}(x_0)) = E\left( \hat{f}(x_0) - E(\hat{f}(x_0))\right)^2$  
- this [[Variance|variance]] comes from the fact that $\hat{f}$ is a random quantity that depends on the training set $\text{Tr}$
* we typically see that as the *flexibility* of $\hat{f}$ increases, the [[Variance|variance]] increases and the [[Bias|bias]] decreases
* so choosing the flexibility based on average [[Testing Error|test error]] [[Mean Squared Error (MSE)|MSE]] is a trade-off between [[Bias|bias]] and [[Variance|variance]]