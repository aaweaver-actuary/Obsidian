[[Residual Sum of Squares (RSS)#^86c8f2|Matix notation for RSS definition]]

- Differentiate with respect to $\beta$:
$$
\begin{align}
\frac{d}{d\beta} \text{ RSS}(\beta) =& \frac{d}{d\beta} (\mathbf{y}-\mathbf{X}\beta)^T(\mathbf{y}-\mathbf{X}\beta) \\
=& \space \mathbf{X}^T(\mathbf{y} - \mathbf{X}\beta) \\
=& \space 0
\end{align}
$$
- These are the [[Normal Equations|normal equations]]
- This has a solution when $\mathbf{X}^T\mathbf{X}$ is [[Nonsingular Matrix|nonsingluar]]:  $\hat{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ 
- 