**widely used approach** for estimating [[Testing Error|test error]]
- estimates can be used:
        _ to select the best model
        _ to give an idea of the [[Testing Error|test error]] of the final chosen model
- idea is to randomly divide the data into $K$ equal-sized parts, or folds
	- we leave out part $k$, fit the model to the other $K-1$ parts, and then obtain predictions for the left-out $k$th part
	- this is done in turn for each part $k = 1, 2, \dots, K$, and then the results are combined

## 5.5.1 the details

- let the $K$ parts be $C_1, C_2, \dots, C_K$
	- $C_k$ denotes the indices of the observations in the $k$th part
	- there are $n_k$ observations in part $k$
		- if $N$ is a multiple of $K$, then $n_k = N/K$ for all $k$
- compute:
    $$
    \text{CV}_{(K)} = \sum_{k=1}^K \frac{n_k}{n}\cdot \text{MSE}_k
    $$
- where $\text{MSE}_k = \sum_{i \in C_k} (y_i - \hat{y}_i)^2 / n_k$
- $\hat{y}_i$ is the fit for observation $i$, obtained from the data with $i$th part removed
- $\text{CV}_{(K)}$ is an estimate of the test [[Mean Squared Error (MSE)|MSE]], called **cross validation error rate**
- _special case:_ $K = N$, then $\text{CV}_{(N)} = \text{MSE}_{\text{LOOCV}}$
        * called [[Leave-One-Out Cross Validation (LOOCV)|leave-one-out cross validation]]

## 5.5.2 A nice special case!

- with [[Ordinary Least Squares (OLS)|least squares]] [[Linear Regression|linear regression]] or #polynomial-regression, an amazing shortcut makes the cost of [[Leave-One-Out Cross Validation (LOOCV)|LOOCV]] the same as that of a single model fit!
- the following formula holds:
    $$
    \text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{y}_i}{1 - h_i} \right)^2
    $$
- where $\hat{y}_i$ is the $i$th fitted value from the original [[Ordinary Least Squares (OLS)|least squares]] fit
        \* that is, the fit obtained when all of the data are used to fit the model
- $h_i$ is the #leverage (the #diagonal of the [[Hat Matrix|hat matrix]] -- see book for details)
- this is like the normal [[Mean Squared Error (MSE)|MSE]], but the $i$th [[Residual|residual]] is divided by $1 - h_i$
- [[Leave-One-Out Cross Validation (LOOCV)|LOOCV]] is sometimes useful, but typically doesn't shake up the data enough
        _ the estimates from each fold are highly correlated
        _ hence the average of these estimates has high [[Variance|variance]]
- a better choice is $K = 5$ or $K = 10$
- so when picking $K$ for [[k-fold Cross Validation|cross validation]], there is a [[Bias-variance trade-off in statistical learning|bias-variance tradeoff]] similar to the one you see in the [[Bias-variance trade-off in statistical learning|bias-variance tradeoff]] for the $K$-nearest neighbors classifier
        _ higher $K$ means less [[Bias|bias]], but higher [[Variance|variance]]
        _ lower $K$ means higher [[Bias|bias]], but lower [[Variance|variance]]

## 5.5.3 Other issues with cross validation

- since each training set is only $(K-1)/K$ as big as the original data set, the estimates of the [[Testing Error|prediction error]] will typically be [[Bias|biased]] upward
- [[Bias]] is minimized when $K=n$ (aka [[Leave-One-Out Cross Validation (LOOCV)|LOOCV]]), but [[Variance|variance]] is high
- $K=5$ or $K=10$ is a good compromise for this [[Bias-variance trade-off in statistical learning|bias-variance tradeoff]]