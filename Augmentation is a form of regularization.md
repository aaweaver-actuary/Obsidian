#statistical-learning 

- More specifically, data #augmentation 
- make many copies of each $(x_i, y_i)$ and add a small amount of #Gaussian noise to the $x_i$
	- a little cloud around each observation
	- but leave the copies of $y_i$ alone
- this makes the fit #robust to small perturbations in $x_i$, and is equivalent to #ridge #regularization in an #OLS setting[^1]  
- [[Data augmentation on the fly]]


[^1]: [[Equivalent regularization methods]]
