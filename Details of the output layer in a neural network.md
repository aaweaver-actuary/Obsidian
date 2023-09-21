- let $Z_m = \beta_{m0} + \sum_{\ell = 1}^{K_2} \beta_{m\ell}A_{\ell}^{(2)}$, $m=0, 1, \dots, 9$ be 10 [[Linear Combination|linear combinations]] of [[Activation Function|activations]] at the second [[Hidden Layers In a Neural Network|hidden layer of a neural network]] 
	- $A_{\ell}^{(2)}$ means the [[Activation Function|activation function]] from the second [[Hidden Layers In a Neural Network|hidden layer]] 
- the output [[Activation Function|activation function]] encodes the #softmax function:

$$
f_m(X) = \text{Pr}(Y=m|X) = \frac{e^{Z_m}}{\sum_{\ell=0}^9 e^{Z_{\ell}}}
$$
- note that the #softmax function is also used in [[Logistic regression for multiclass classification|multi-class logistic regression]] 
- we fit the model by minimizing the #negative-multinomial #loglikelihood, AKA #cross-entropy
  $$
 -\sum_{i=1}^n \sum_{m=0}^9 y_{im}\log \left( f_m(x_i) \right) \hspace{20em}
 $$
 - here $y_m$ is 1 if true class for observation $i$ is $m$, else 0
	 - ie it is #one-hot-encoded
	 - in statistics, called #dummy-variable's 