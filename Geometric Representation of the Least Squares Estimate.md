- $\mathbf{x}_0, \mathbf{x}_1, \dots, \mathbf{x}_p$ - column vectors of $\mathbf{X}$
	- $\mathbf{x}_0 == 1$   
	- These vectors span a subspace of $\mathbb{R}^N$ called the [[The Column Space of a Matrix X|column space of X]]
- We minimize$$
  \text{RSS}(\beta) = ||\mathbf{y} - \mathbf{X}\beta||^2
  $$by choosing $\hat{\beta}$ so that the [[Residual|residual vector]] $\mathbf{y} - \hat{\mathbf{y}}$ is orthogonal to the [[The Column Space of a Matrix X|column space of X]]
- $\hat{\mathbf{y}}$ is the orthogonal projection of $\mathbf{y}$ onto [[The Column Space of a Matrix X|this subspace]]
- The [[Hat Matrix|hat matrix]] $\mathbf{H}$ computes the orthogonal projection