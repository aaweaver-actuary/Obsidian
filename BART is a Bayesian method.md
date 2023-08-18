## From #statistical-learning 

- [[Bayesian Additive Regression Trees (BART)|BART]] can be viewed as a [[Bayesian]] approach to fitting an #ensemble of #trees:
	- each time we randomly perturb a tree ([[New BART trees are chosen by perturbations]]) in order to fit the residuals, we are in fact drawing a new #tree from a #posterior-distribution
- Further #BART can be seen as a [[Markov Chain Monte Carlo (MCMC)]] #mcmc procedure for fitting the #BART model
- It can be shown that the parameters (eg the split points & perturbations) come from a specific #prior-distribution
	- the method is based on statistical theory
- We typically choose large values for $B$ and $K$ and a moderate value for $L$
	- eg $K=200$, $B=1,000$, and $L=100$ are reasonable choices
- #BART has been shown to have impressive out of the box performance
	- eg it performs well with minimal #hyperparameter tuning 
- 