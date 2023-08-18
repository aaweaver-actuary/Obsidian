#bart #statistical-learning 
### First iteration
all trees are initialized to have a single root node with
$$
\hat{f}_k^1(x) = \frac{1}{nK}\sum_{i=1}^n y_i
$$
thus
$$
\begin{align}
\hat{f}^1(x) =& \sum_{k=1}^K\hat{f}_k^1 (x) \\
=& \frac{1}{n} \sum_{i=1}^{n} y_i
\end{align}
$$

### Subsequent iterations
Update each of the $K$ trees, one at a time.

In the $b$th iteration, to update the $k$th tree, subtract from each response value the predictions from all but the $k$th tree, in order to obtain a [[Partial residual|partial residual]] 
$$
r_i = y_i - \sum_{k' < k} \hat{f}_{k'}^b(x) - \sum_{k' > k}\hat{f}_{k'}^{b-1}(x_i), \space \space i = 1, \dots, n
$$
[[New BART trees are chosen by perturbations]]
