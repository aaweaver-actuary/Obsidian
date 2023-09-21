
With $f(X) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_pX_p$, can rephrase [[Support Vector Classifier|support vector classifier]] optimization as 
$$
\min_{\beta_i} \left\{ \sum_{i=1}^n \max[0, 1-y_if(x_i)] + \lambda\sum_{j=1}^p \beta_j^2  \right\} \hspace{15em}
$$
- This has the form loss plus penalty 
- the loss is known as the [[Hinge Loss|hinge loss]]
- very similar to loss in [[Logistic Regression|logistic regression]] (with a [[Ridge regularization|ridge]] penalty term)
	- this is #negative-loglikelihood 

## [[Logistic Regression]]
- modeling the probability of being in one class or other

## support vector machines
- going for the [[Decision Boundary|decision boundary]] directly, not the intermediate step of getting the probability

## which to use?
- when the classes are (nearly) separable, [[Support Vector Machines (SVMs)|support vector machines]] do better than [[Logistic Regression|logistic regression]] 
	- so does [[Linear Discriminant Analysis|linear discriminant analysis]]
	- [[Logistic Regression|logistic regression]] actually breaks down if the classes are exactly separable
- when the classes are not, [[Logistic Regression|logistic regression]] with a [[Ridge regularization|ridge]] penalty and [[Support Vector Machines (SVMs)|SVMs]] are very similar
- if you want to estimate probability, [[Logistic Regression|logistic regression]] is the choice
- for a nonlinear [[Decision Boundary|decision boundary]], [[Kernel functions are functions of two variables that compute inner products|kernel functions]] with [[Support Vector Machines (SVMs)|support vector machines]] are popular
	- can use [[Kernel functions are functions of two variables that compute inner products|kernel functions]] with [[Logistic Regression|logistic regression]] and [[Linear Discriminant Analysis|linear discriminant analysis]] as well, but the computations are more expensive
