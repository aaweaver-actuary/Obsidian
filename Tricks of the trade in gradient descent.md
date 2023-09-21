

- **Slow Learning** - [[Gradient Descent|Gradient descent]] is slow, and a small #learning-rate $\rho$ slows it even more
    - along with #early-stopping, this is a form of [[Regularization|regularization]]
- [[Stochastic Gradient Descent (SGD)|Stochastic gradient descent]] or SGD - rather than compute the [[Gradient Vector|gradient vector]] using all the data, use a small #minibatch drawn at random at each step
- an #epoch is a count of iterations and amounts to the number of #minibatch updates such that $n$ samples in total have been processed
- [[Regularization]] - [[Ridge regularization|ridge]] and [[The Lasso for regularization|lasso]] [[Regularization|regularization]] can be used to shrink the #weight's at each layer
    - two other popular forms of [[Regularization|regularization]]:
        - [[Dropout is a form of regularization]]
        - [[Augmentation is a form of regularization]]
-
