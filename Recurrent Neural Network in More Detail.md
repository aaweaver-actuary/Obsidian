#deep-learning #rnn #neural-network #statistical-learning 

- Suppose $X_{\ell} = (X_{\ell 1}, X_{\ell 2}, \dots, X_{\ell p})$ has $p$ components, and $A_{\ell} = (A_{\ell 1}, A_{\ell 2}, \dots A_{\ell K})$ has $K$ components. Then the computation at the $k$-th components of #hidden-layer unit $A_{\ell}$ is
$$
\begin{align}
A_{\ell k} =& \space g \left(w_{k0} + \sum_{j=1}^p w_{kj}X_{\ell j} + \sum_{s=1}^K u_{ks}A_{\ell - 1, s} \right) \hspace{10em} \\
O_{\ell} =& \space \beta_0 + \sum_{k=1}^K\beta_kA_{\ell k}
\end{align}
$$

## structure:
- $w_{k0}$ is the #bias or the #intercept 
- then there is a #linear-combination of the input vector at that point:
	- $\sum_{j=1}^p w_{kj}X_{\ell j}$
- then a #linear-combination of the #activation-function units from the previous step
- then there is a #nonlinear thing such as #relu 
- then the #output-layer is just a #linear-model or a #softmax or a #logistic transformation

- Often we are concerned only with the prediction $O_L$ at the last unit
- For squared error loss, and $n$ sequence/response pairs, we would minimize
  $$
  \begin{align}
&\sum_{i=1}^n(y_i - o_{iL})^2 = \\
&\sum_{i=1}^n \left\{ y_i - \left[ \beta_0 + \sum_{k=1}^K \beta_{k}g\left( w_{k0} + \sum_{j=1}^p w_{kj}x_{iLj} + \sum_{s=1}^K u_{ks} a_{i, L-1, s}\right) \right] \right\}^2
\end{align}
  $$
   