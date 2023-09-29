This is how we fit the [[Non-convex objective function]] in [[Deep Learning]] / [[Neural Networks|neural network]] models

Let $R(\theta) = \frac{1}{2} \sum_{i=1}^n (y_i - f_{\theta}(x_i))^2$ with $\theta = \left( \{ w_k\}_1^K, \beta\right)$ 
	(eg [[Weights|weights]] and [[Bias|biases]])

1. Start with a guess $\theta^0$ for all the parameters in $\theta$, and set $t=0$
2. Iterate until the objective $R(\theta)$ fails to decrease:
	1. Find a vector $\delta$ that reflects a small change in $\theta$ such that $\theta^{t+1} = \theta^t + \delta$ reduces the objective
	   - ie $R(\theta^{t+1}) < R(\theta^t)$
	2. Set $t \leftarrow t+1$  

Note this only finds a *local* minimum - result depends on where you start

[[Gradient descent finds the direction pointing downhill by computing the gradient vector]]

