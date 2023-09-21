

[[Double Descent]]

### Some facts
- in a wide [[Linear Model|linear models]] ($p \gg n$) fit by [[Ordinary Least Squares (OLS)|least squares]], [[Stochastic Gradient Descent (SGD)|SGD]] with a small #learning-rate leads to a #minimum-norm, zero [[Residual|residual]] solution
- by analogy, when training [[Neural Networks|neural networks]], by training slowly to zero [[Residual|residual]], you get more [[Regularization|regularization]] in your network
- [[Stochastic Gradient Flow|Stochastic gradient flow]] - the entire path of [[Stochastic Gradient Descent (SGD)|SGD]] solutions - is somewhat similar to [[Ridge regularization|ridge]] path[^1] 
- by analogy again, deep and wide [[Neural Networks|neural networks]] fit by [[Stochastic Gradient Descent (SGD)|SGD]] down to zero #training-error often give good solutions that generalize well
	- in particular, cases with high #signal-to-noise-ratio[^2] are less prone to [[Overfitting|overfitting]] because the #zero-error solution is mostly signal

[^1]: [[Stochastic Gradient Flow]]
[^2]: [[High signal-to-noise ratio examples]]
