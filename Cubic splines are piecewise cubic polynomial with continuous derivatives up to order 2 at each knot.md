
A cubic spline with knots at $\xi_k, \space k=1, \dots, K$ is a piecewise cubic polynomial with continuous derivatives up to order 2 at each knot.

Again we represent this model with truncated power basis functions:

$$
\begin{align}
y_i =& \beta_0 + \beta_1b_1(x_i) + \cdots + \beta_{K+3}b_{K+3}(x_i) + \epsilon_i, \\
b_1(x_i) =& \space x_i, \\
b_2(x_i) =& \space x_i^2, \\
b_3(x_i) =& \space x_i^3, \\
\dots & \\
b_{K+3}(x_i) =& \space (x_i - \xi_k)_+^3, \space k=1, \dots, K \\
\end{align}
$$

where

$$
(x_i - \xi_k)_+^3 = \left\{ \begin{array}{rr}
(x_i - \xi_k)^3 & \text{ if } x_i > \xi_k, \\
0 & \text{otherwise}
\end{array}
\right.
$$

### Note
[[Cubic splines have 0th, 1st, 2nd derivatives equal to 0 at the knot]]
[[A spline is continuous at the knots]]
[[Knot placement is based on the choice of one of a fixed set of rules]]
