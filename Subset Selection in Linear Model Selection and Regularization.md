### 6.4 Subset selection

*best subset and stepwise model selection procedures*
#### 6.4.1 Best subset selection
1. Let $\mathcal{M}_0$ denote the *null model*, which contains no predictors. (This model simply predicts the sample mean for each observation.)
2. For $k=1,2,\cdots,p$:
    * Fit all $\binom{p}{k}$ models that contain exactly $k$ predictors.
    * Pick the best among these $\binom{p}{k}$ models, and call it $M_k$. Here *best* is defined as having the smallest [[Residual Sum of Squares (RSS)|RSS]], or equivalently largest $R^2$.
3. Select a single best model from among $\mathcal{M}_0, \mathcal{M}_1, \cdots, \mathcal{M}_p$ using cross-validated prediction error, $C_p$ (AIC), BIC, or adjusted $R^2$.

##### Extensions to other models

* we presented best subset selection for least squares linear regression
    * but the same framework can be applied to other models as well
* the **deviance** is negative twice the maximized log-likelihood
    * it is a measure of model fit
    * it plays the role of [[Residual Sum of Squares (RSS)|RSS]] for a broader class of models