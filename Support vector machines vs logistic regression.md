#svm #support-vector-machines #logistic-regression

With $f(X) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_pX_p$, can rephrase #support-vector-classifiers optimization as 
$$
\min_{\beta_i} \left\{ \sum_{i=1}^n \max[0, 1-y_if(x_i)] + \lambda\sum_{j=1}^p \beta_j^2  \right\} \hspace{15em}
$$
- This has the form #loss-plus-penalty 
- the loss is known as the #hinge-loss
- very similar to loss in #logistic-regression (with a #ridge penalty term)
	- this is #negative-loglikelihood 

## logistic regression
- modeling the #probability of being in one class or other

## support vector machines
- going for the #decision-boundary directly, not the intermediate step of getting the probability

## which to use?
- when the classes are (nearly) #separable, #support-vector-machines do better than #logistic-regression 
	- so does #linear-discriminant-analysis
	- #logistic-regression actually breaks down if the classes are exactly #separable
- when the classes are not, #logistic-regression with a #ridge penalty and #support-vector-machines are very similar
- if you want to estimate #probability, #logistic-regression is the choice
- for #nonlinear #decision-boundary, #kernels with #support-vector-machines are popular
	- can use #kernels with #logistic-regression and #linear-discriminant-analysis as well, but the computations are more expensive
