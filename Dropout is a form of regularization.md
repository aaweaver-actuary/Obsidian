#statistical-learning #sgd #stochastic-gradient-descent 

- at each #sgd update, randomly remove #node's with probability $\phi$ and scale up the #weights of the remaining #node's by $1/(1-\phi)$ to compensate
- in simple scenarios like #linear-regression, a version of this process can be shown to be equivalent to #ridge #regularization [^3]
- as in #ridge, the other units stand in for those temporarily removed, and their weights are drawn closer together[^1]
- similar in concept to randomly omitting variables when growing #tree's in #random-forest's[^2]

[^1]: [[Ridge regularization]]
[^2]: [[Random forests]]
[^3]: [[Equivalent regularization methods]]
