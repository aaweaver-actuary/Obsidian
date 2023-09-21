[[Support Vector Machines (SVMs)]]

- one of the most important [[Kernel functions are functions of two variables that compute inner products|kernel functions]] used for nonlinear [[Support Vector Machines (SVMs)|support vector machines]]
$$
\begin{align}
K(x_i, x_{i'}) =& \space \exp\left(-\gamma\sum_{j=1}^p (x_{ij} -x_{i'j})^2  \right) \hspace{19em}\\
f(x) =& \space\beta_0 + \sum_{i\in\mathcal{S}}\hat{\alpha}_i K(x, x_i)
\end{align}
$$
- here $\gamma$ is the #tuning-parameter
	- can think of it as $1/\sigma$, where $\sigma$ is [[Gaussian]] [[Standard Deviation|standard deviation]] 
	- if $\gamma$ is really large, it is like having a small [[Standard Deviation|standard deviation]] 
		- this leads to much more #wiggly decision boundaries
	- if $\gamma$ is small, it is like having a large [[Standard Deviation|standard deviation]] 
		- leads to much smoother [[Decision Boundary|decision boundary]]
- this is the "important part" of a #multivariate-gaussian distribution
- implicit feature space
	- very high dimensional
	- #infinitely-dimensional 
- controls [[Variance|variance]] by squashing down most dimensions severely
	- this is needed to keep from [[Overfitting|overfitting]] 
	- the dimensions that are squashed down tend to be the more #wiggly dimensions
