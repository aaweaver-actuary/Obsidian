[[Bayesian Additive Regression Trees (BART)]] 

- Rather than fitting a fresh [[Tree-Based Methods|tree]] to this #partial-residual
- BART randomly chooses a perturbation to the [[Tree-Based Methods|tree]] from the previous [[BART iterations|BART iteration]] $\left(\hat{f}_k^{b-1}\right)$ from a set of possible perturbations
	- Perturbations that improve the fit to the #partial-residual are preferred ([[Improving fit is minimizing the sum of squares]]) 

### Components to the perturbation
1. We may change the structure of the [[Tree-Based Methods|tree]] by adding or by #pruning-branches
2. We may change the prediction in each #terminal-node of the [[Tree-Based Methods|tree]]

### What are we doing?
- trying to cover the space of possible [[Tree-Based Methods|trees]]
- in a way, [[Bagging|bagging]] and [[Boosting|boosting]] are doing the same thing--trying to cover the space of possible [[Tree-Based Methods|trees]]
- [[Bayesian Additive Regression Trees (BART)|BART]] does the same thing, but in a different way (using perturbations)

### Benefits of perturbations
- guard against [[Overfitting|overfitting]]
	- perturbations limit how *hard* we fit the data in each iteration
