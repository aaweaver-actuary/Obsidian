[[Unsupervised Learning]]

- we must select $M$, which is the number of [[Principal Components|principal components]] to use for the #imputation 
- if you select $M$ to be too high, it will [[Overfitting|overfit]], and if you select $M$ to be too low, it will not fit well

### An approach:

- randomly set some values to `NaN` that were actually observed
	- select $M$ based on how well those known values are recovered[^1]
- `softImpute` package in #R
- `matrix-completion` in [[Python]]

[^1]: closely related to: [[Use cross validation to select hyperparameters]]