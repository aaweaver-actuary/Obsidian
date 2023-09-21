
* for computational reasons, best subset selection cannot be applied with very large $p$
* best subset selection may also suffer from statistical problems when $p$ is large
    * it will tend to choose models that have too many variables
    * larger search space => larger chance of overfitting
* an enormous search space can lead to overfitting
* we can use stepwise selection instead
    * stepwise methods explore a far more restricted set of models
* big idea is that you restrict the number of models examined by best subset selection
    * by **imposing a threshold** on the variable entry and exit
    * restricting the number of models examined lowers the risk of overfitting/the risk of selecting models that include irrelevant variables
* forward and backward stepwise selection are two closely related variants of this idea

#### 6.5.1 Forward stepwise selection

* begin with a model containing no predictors
* we then add predictors to the model, one-at-a-time, until all of the predictors are in the model
* at each step, the variable that gives the greatest additional improvement to the fit is added to the model
* we stop once no significant improvement can be made

##### In detail - forward stepwise selection
1. Let $\mathcal{M}_0$ denote the null model, which contains no predictors (ie just the intercept)
2. For $k=0,\dots,p-1$:
    1. Consider all $p-k$ models that augment the predictors in $\mathcal{M}_k$ with one additional predictor
    2. Choose the best among these $p-k$ models, and call it $\mathcal{M}_{k+1}$
3. Select a single best model from among $\mathcal{M}_0,\dots,\mathcal{M}_p$ using cross-validated prediction error, $C_p$ (AIC), BIC, or adjusted $R^2$

* computational advantage over best subset selection
    * best subset selection involves fitting $2^p$ models for $p predictors
        * really only feasible for $p < 40$, but even authors only recommend for $p < 10$
    * forward stepwise selection considers $1 + p(p+1)/2$ models
        
* it is not guaranteed to find the best possible model containing a subset of the p predictors
    * in fact, [[Residual Sum of Squares (RSS)|RSS]] can be no lower than that obtained by best subset selection, but it can be higher
    * this is due to the correlation between predictors
  
#### 6.5.2 Backward stepwise selection

* like forward stepwise selection, but in reverse:
    * start with all predictors in the model
    * remove the least useful predictor one at a time

##### Details - backward stepwise selection

1. Let $\mathcal{M}_p$ denote the full model, which contains all $p$ predictors.
2. For $k = p, p-1, \dots, 1$:
    * Consider all $k$ models that contain all but one of the predictors in $\mathcal{M}_k$, for a total of $k-1$ predictors.
    * Choose the best among these $k$ models, and call it $\mathcal{M}_{k-1}$.
    * Best is defined as having the smallest [[Residual Sum of Squares (RSS)|RSS]] or highest $R^2$.
3. Select a single best model from among $\mathcal{M}_0, \dots, \mathcal{M}_p$ using [[k-fold Cross Validation|cross-validated]] prediction error, $C_p$ (AIC), BIC, or adjusted $R^2$.

##### More on backward stepwise selection

* considers $1 + p(p+1)/2$ models
* like forward stepwise selection, it is not guaranteed to find the best possible model containing a subset of the p predictors
    * in fact, [[Residual Sum of Squares (RSS)|RSS]] can be no lower than that obtained by best subset selection, but it can be higher
    * this is due to the correlation between predictors
* backward selection requires that the number of samples $n$ is larger than the number of predictors $p$, or else the full model cannot be fit
    * in contrast, **forward selection** can be used even when $n < p$, and so is the **only viable subset method when $p > n$**