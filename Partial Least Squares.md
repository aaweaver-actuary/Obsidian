- [[Principal Components Regression (PCR)|Principal components regression]] identifies [[Linear Combination|linear combinations]] or _directions_ that best represent the predictors $X_1, X_2, \dots, X_p$
- these directions are identified in an [[Unsupervised Learning|unsupervised]] way, since the response $Y$ plays no role in determining them
- consequently, [[Principal Components Regression (PCR)|PCR]] suffers from a potentially serious drawback:
    - there is no guarantee that the directions that best explain the predictors will also be the best directions to use for predicting the response
- like [[Principal Components Regression (PCR)|PCR]], partial least squares (PLS) is also a [[Dimension Reduction Methods|dimension reduction method]]
- PLS first identifies a new set of features $Z_1, Z_2, \dots, Z_M$ that are [[Linear Combination|linear combinations]] of the original features, and then fits the model
- unlike [[Principal Components Regression (PCR)|PCR]], PLS identifies these new features in a [[Supervised Learning|supervised]] way - that is, it makes use of the response $Y$
    - PLS identifies new features that not only approximate the old features well, but also that are related to the response
- roughly speaking, the PLS approach attempts to find directions that help explain both the response and the predictors

#### details of PLS

- standardize the $p$ predictors to have mean zero and standard deviation one
- the first PLS direction $Z_1$ is found by setting each $\phi_{1j}$ equal to the coefficient from the simple [[Linear Regression|linear regression]] of $Y$ onto $X_j$
- one can show that this coefficient is proportional to the [[Correlation|correlation]] between $Y$ and $X_j$
- thus in computing $Z_1 = \sum_{j=1}^p \phi_{1j} X_j$, PLS places the highest weight on the variables that are most strongly related to the response
- subsequent directions are found by taking the [[Residual|residuals]] from the [[Regression|regression]] of each $X_j$ on $Z_1, Z_2, \dots, Z_{m-1}$
