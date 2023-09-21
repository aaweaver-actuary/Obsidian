
A #linear-spline with [[Knots in Cubic Splines|knots]] at $\xi_k, \space k=1, \dots, K$ is a piecewise linear polynomial [[A spline is continuous at the knots|continuous at each knot]]

We can represent this model as
$$
y_i = \beta_0 + \beta_1b_1(x_i) + \beta_2b_2(x_i) + \cdots + \beta_{K+3}b_{K+3}(x_i) + \epsilon_i
$$
where the $b_k$ are **basis** functions
$$
\begin{array}{cc}
b_{1}(x_i) = \space x_i & \space \\
\dots & \space\\
b_{k+1}(x_i) = \space (x_i - \xi_k)_+, & k=1, \dots, K 
\end{array}
$$
Here the $()_+$ means the positive part, ie
$$
(x_i - \xi_k)_+ = \left\{ 
\begin{array}{cc}
x_i - \xi_k & \text{if } x_i > \xi_k,\\
0 & \text{otherwise}
\end{array}
\right.
$$
