[[Gradient Descent]] 

This is a sum:
$$
R(\theta) = \sum_{i=1}^n R_i(\theta) \hspace{25em}
$$
This means that a [[Gradient Vector|gradient vector]] is a sum of [[Gradient Vector|gradient vectors]]
$$
\begin{align}
R_i(\theta) =& \frac{1}{2} (y_i - f_{\theta}(x_i))^2  \\
=& \frac{1}{2} \left[ y_i -\beta_0 -\sum_{k=1}^K \beta_kg\left( w_{k0} + \sum_{j=1}^p w_{kj}x_{ij} \right) \right]^2 \hspace{9em}
\end{align}
$$

For ease of notation, let $z_{ik} = w_{k0} + \sum_{j=1}^p w_{kj}x_{ij}$ 

#backpropagation uses the chain rule for differentiation[^1]



[^1]: See [Wikipedia article on backpropagation](https://en.wikipedia.org/wiki/Backpropagation#Derivation) for the derivation