

The [[Gradient Vector|gradient vector]] is defined
$$
\nabla R(\theta^t) = \left. \frac{\partial R(\theta)}{\partial \theta} \right|_{\theta=\theta^t} \hspace{20em}
$$
This is the vector of #partial-derivatives at the current guess $\theta^t$

The [[Gradient Vector|gradient vector]] points uphill, so our update in the [[Gradient Descent|gradient descent]] algorithm is
$$
\begin{align}
\delta =& -\rho\nabla R(\theta^t) \hspace{24em}\\
\text{or}&\\
\theta^{t+1} \leftarrow & \theta^t - \rho \nabla R(\theta^t)
\end{align}
$$
where $\rho$ is the #learning-rate (typically small, eg $\rho = 0.001$)