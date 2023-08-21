#deep-learning 

$$
\begin{align}
f(X) =& \beta_0 + \sum_{k=1}^K \beta_kh_k(X) \hspace{23em} \\
=& \beta_0 + \sum_{k=1}^K \beta_kg\left(w_{k0} + \sum_{j=1}^p w_{kj} X_j\right)
\end{align}
$$
- $A_k = h_k(X) = g\left(w_{k0} + \sum_{j=1}^p w_{kj} X_j\right)$ are called the #activations in the #hidden-layer
- $g(z)$ is called the #activation-function
	- popular choices are #sigmoid and #rectified-linear or #relu
- you need the #activation-function to be #nonlinear 
	- otherwise the whole #neural-network would just be #linear: #linear transformations of a #linear-function are themselves #linear
- the #activations are #derived-features
	- eg #nonlinear transformations of #linear-combinations of the features
- the model is fit by minimizing
  $$
 \sum_{i=1}^n (y_i - f(x_i))^2 \hspace{25em} 
 $$
 