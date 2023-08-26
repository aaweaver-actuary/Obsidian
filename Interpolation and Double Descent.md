#statistical-learning 

[[Double Descent]]

### Some facts
- in a wide #linear-model ($p \gg n$) fit by #least-squares, #sgd with a small #learning-rate leads to a #minimum-norm, zero #residual solution
- by analogy, when training #neural-network's, by training slowly to zero #residual, you get more #regularization in your network
- #stochastic-gradient-flow - the entire path of #sgd solutions - is somewhat similar to #ridge path[^1] 
- by analogy again, deep and wide #neural-network's fit by #sgd down to zero #training-error often give good solutions that generalize well
	- in particular, cases with high #signal-to-noise-ratio[^2] are less prone to #overfitting because the #zero-error solution is mostly signal

[^1]: [[Stochastic gradient flow]]
[^2]: [[High signal-to-noise ratio examples]]
