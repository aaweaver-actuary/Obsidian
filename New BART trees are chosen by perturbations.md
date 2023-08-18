#bart #statistical-learning 

- Rather than fitting a fresh tree to this [[Partial residual|partial residual]]
- BART randomly chooses a perturbation to the tree from the previous iteration ([[BART iterations]]) $\left(\hat{f}_k^{b-1}\right)$ from a set of possible perturbations
	- Perturbations that improve the fit to the partial residual are preferred ([[Improving fit is minimizing the sum of squares]]) 

### Components to the perturbation
1. We may change the structure of the tree by adding or by pruning branches
2. We may change the prediction in each terminal node of the tree

### What are we doing?
- trying to cover the space of possible trees
- in a way, [[Bagging|bagging]] and [[Boosting|boosting]] are doing the same thing--trying to cover the space of possible trees
- this does the same thing, but in a different way (using perturbations)

### Benefits of perturbations
- guard against overfitting
	- perturbations limit how *hard* we fit the data in each iteration
