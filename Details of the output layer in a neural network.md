- let $Z_m = \beta_{m0} + \sum_{\ell = 1}^{K_2} \beta_{m\ell}A_{\ell}^{(2)}$, $m=0, 1, \dots, 9$ be 10 #linear-combinations of #activations at the second #hidden-layer of a #neural-network 
	- $A_{\ell}^{(2)}$ means the #activation-function from the second #hidden-layer 
- the output #activation-function encodes the #softmax function:

$$
f_m(X) = \text{Pr}(Y=m|X) = \frac{e^{Z_m}}{\sum_{\ell=0}^9 e^{Z_{\ell}}}
$$
- note that the #softmax function is also used in #multi-class #logistic-regression 
- we fit the model by minimizing the #negative-multinomial #loglikelihood, AKA #cross-entropy
  $$
 -\sum_{i=1}^n \sum_{m=0}^9 y_{im}\log \left( f_m(x_i) \right) \hspace{20em}
 $$
 - here $y_m$ is 1 if true class for observation $i$ is $m$, else 0
	 - ie it is #one-hot-encoded
	 - in statistics, called #dummy-variables 