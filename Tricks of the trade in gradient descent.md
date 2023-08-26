#statistical-learning 

- **Slow Learning** - #gradient-descent is slow, and a small #learning-rate $\rho$ slows it even more
	- along with #early-stopping, this is a form of #regularization 
- #stochastic-gradient-descent or #sgd - rather than compute the #gradient using all the data, use a small #minibatch drawn at random at each step
- an #epoch is a count of iterations and amounts to the number of #minibatch updates such that $n$ samples in total have been processed
- #regularization - #ridge and #lasso #regularization can be used to shrink the #weights at each layer
	- two other popular forms of #regularization:
		- [[Dropout is a form of regularization]]
		- [[Augmentation is a form of regularization]]
- 