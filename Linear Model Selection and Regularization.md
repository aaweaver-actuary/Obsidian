* recall the [[Linear Model|linear model]]:
$$
Y=\beta_0+\beta_1X_1+\beta_2X_2+\cdots+\beta_pX_p+\epsilon
$$
* in the lectures that follow, we consider some approaches for extending the [[Linear Model|linear model]] framework
* in the lectures covering [[7. Moving Beyond Linearity|chapter 7 of the text]], we generalize the linear model to accommodate nonlinearity, but still additive relationships between the features and the response 
* in the lectures covering chapter 8 we consider even more general nonlinear models

### In praise of [[Linear Model|linear models]]!

* despite its simplicity, the linear model has distinct advantages in terms of its #interpretability and often shows good #prediction-accuracy`
* hence we discuss in this lecture some ways in which the simple [[Linear Model|linear model]] can be improved
    * by replacing ordinary least squares [[Ordinary Least Squares (OLS)|OLS]] with some alternative fitting procedures

[[Two reasons to consider alternatives to OLS]]
[[Three classes of alternatives to OLS]]
[[Choosing the optimal model]]


### 6.13 Dimension reduction methods

* the methods discussed so far in this chapter have involved fitting a linear model involving $p$ predictors using either  [[Ordinary Least Squares (OLS)|least squares]] or a [[Shrinkage in Linear Model Selection and Regularization|shrinkage]] approach
* we now consider some approaches that transform the predictors and then fit a least squares model using the transformed variables
    * these approaches will be called **dimension reduction methods**
* the goal of dimension reduction is to reduce the $p$ predictors to a $M$-dimensional subspace, where $M < p$

#### 6.13.1 Details

* Let $Z_1, Z_2, \dots, Z_M$ represent $M < p$ [[Linear Combination|linear combinations]] of our original $p$ predictors. That is,
$$
Z_m = \sum_{j=1}^p \phi_{jm}X_j
$$
* where $\phi_{1m}, \phi_{2m}, \dots, \phi_{pm}$ are constants
* we can then fit the following linear regression model using least squares:
$$
y_i = \theta_0 + \sum_{m=1}^M \theta_m z_{im} + \epsilon_i, \quad i = 1, \dots, n
$$
* note that in the model, the regression coefficients are given by $\theta_0, \theta_1, \dots, \theta_M$
    * if the constants $\phi_{jm}$ are chosen wisely, then the $M$-dimensional response $Z_m$ may be much simpler to model than the original $p$-dimensional response $X_j$
* note that, from the definition of $Z_m$, we have
$$
\begin{align}
\sum_{m=1}^M \theta_m z_{im}  =& \sum_{m=1}^M \theta_m \sum_{j=1}^p \phi_{jm} x_{ij} \\
=& \sum_{j=1}^p \sum_{m=1}^M \theta_m \phi_{jm} x_{ij} \\
=& \sum_{j=1}^p \beta_j x_{ij} \\
\text{where } \beta_j =& \sum_{m=1}^M \theta_m \phi_{jm}
\end{align}
$$
* thus the model is equivalent to the least squares regression of $y$ onto $X_1, X_2, \dots, X_p$
    * it can be considered a special case of the linear model in which the predictors are linear combinations of the original predictors
* the dimension reduction approach is most useful in the case where $M < p$, that is, when we have reduced the problem to a smaller number of predictors
    * in this case, the least squares approach is more stable
    * can win in the bias-variance tradeoff

### 6.14 Principal Components Regression

* here we apply principal components analysis (PCA) to define the linear combinations of the predictors, for use in our regression model
* the first principal component that is that (normalized) linear combination of the variables that has the largest variance
    * the second principal component has largest variance out of all linear combinations that are uncorrelated with the first principal component
    * and so on
* hence with many correlated original variables, we replace them with a small set of principal components that capture their joint variation

### partial least squares

* principal components regression identifies linear combinations or *directions* that best represent the predictors $X_1, X_2, \dots, X_p$
* these directions are identified in an *unsupervised* way, since the repsonse $Y$ plays no role in determining them
* consequently, PCR suffers from a potentially serious drawback:
    * there is no guarantee that the directions that best explain the predictors will also be the best directions to use for predicting the response
* like PCR, partial least squares (PLS) is also a dimension reduction method
* PLS first identifies a new set of features $Z_1, Z_2, \dots, Z_M$ that are linear combinations of the original features, and then fits the model
* unlike PCR, PLS identifies these new features in a *supervised* way - that is, it makes use of the response $Y$
    * PLS identifies new features that not only approximate the old features well, but also that are related to the response
* roughly speaking, the PLS approach attempts to find directions that help explain both the response and the predictors

#### details of PLS

* standardize the $p$ predictors to have mean zero and standard deviation one
* the first PLS direction $Z_1$ is found by setting each $\phi_{1j}$ equal to the coefficient from the simple linear regression of $Y$ onto $X_j$
* one can show that this coefficient is proportional to the correlation between $Y$ and $X_j$
* thus in computing $Z_1 = \sum_{j=1}^p \phi_{1j} X_j$, PLS places the highest weight on the variables that are most strongly related to the response
* subsequent directions are found by taking the residuals from the regression of each $X_j$ on $Z_1, Z_2, \dots, Z_{m-1}$