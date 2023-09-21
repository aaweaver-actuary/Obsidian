[[Neural Networks]]

- Will use the [[IMDB Movie Reviews Corpus]]
- #sentiment [[Classification|classification]] task
- [[Featurization - Bag of Words]]
- In the case of a model using the #bag-of-words-model , simpler [[The Lasso for regularization|Lasso]] [[Logistic Regression|logistic regression]] works as well as a 2-layer [[Neural Networks|neural networks]] in this case
	- they use #glmnet to fit the [[The Lasso for regularization|lasso]] model
	- #glmnet is very effective here because it can exploit #sparse matrices