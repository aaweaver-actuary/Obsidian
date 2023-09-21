For a [[Linear Regression|linear regression]] [[Linear Model|model]] fit by minimizing [[Ordinary Least Squares (OLS)|least squares]],$$
   \begin{align}
   \hat{\mathbf{y}} =& \ \mathbf{X}\hat{\beta} \\
   =& \ \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y} \\
   =& \ \mathbf{H}\mathbf{y}
   \end{align}
$$
- $\mathbf{H} = \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T$ is called the hat matrix
	- because it is the thing that puts a hat on $\mathbf{y}$

- Sometimes also called a projection matrix, because it computes an [[Geometric Representation of the Least Squares Estimate|orthogonal projection]] of $\mathbf{y}$ onto the [[The Column Space of a Matrix X|column space of the feature matrix]] $\mathbf{X}$ 