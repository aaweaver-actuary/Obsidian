1. Let $\mathbf{X}$ be the $N\times(p+1)$ matrix with each row an input vector with a $1$ in the first position
2. Let $\mathbf{y}$ be the $N$-vector of outputs in the training set
3. Write the [[Residual Sum of Squares (RSS)|residual sum of squares]] as
   $\text{RSS}(\beta) = (\mathbf{y} - \mathbf{X}\beta)^T(\mathbf{y} - \mathbf{X}\beta)$
   - This is a quadratic function in the $p+1$ parameters
4. Differentiate WRT $\beta$:$$
\begin{align}
\frac{\partial \text{RSS}}{\partial\beta} =& -2\mathbf{X}^T(\mathbf{y} - \mathbf{X}\beta) \\
\frac{\partial^2\text{RSS}}{\partial\beta\partial\beta^T} =& 2\mathbf{X}^T\mathbf{X}
\end{align}
$$
5. Assume that $\mathbf{X}$ has full column rank, and so $\mathbf{X}^T\mathbf{X}$ is [[Definition of positive semi-definite|positive semi-definite]], we set the first derivative to 0:
   
   $\mathbf{X}^T(\mathbf{y} - \mathbf{X}\beta) =0$
   
   to obtain the unique solution:
   $\hat{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$  
6. The predicted values at an input vector $x_0$ are given by $\hat{f}(x_0) = (1:x_0)^T\hat{\beta}$, giving:$$
   \begin{align}
   \hat{\mathbf{y}} =& \ \mathbf{X}\hat{\beta} \\
   =& \ \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y} \\
   =& \ \mathbf{H}\mathbf{y}
   \end{align}
   $$
   - Here $\mathbf{H}$ is the [[Hat Matrix|hat matrix]]
