

- [[Bayesian Additive Regression Trees (BART)|BART]] can be viewed as a [[Bayesian]] approach to fitting an #ensemble of [[Tree-Based Methods|trees]]:
	- each time([[New BART trees are chosen by perturbations|we randomly perturb a tree]] in order to fit the residuals, we are in fact drawing a new [[Tree-Based Methods|tree]] from a [[Posterior Distribution|posterior distribution]]
- Further [[Bayesian Additive Regression Trees (BART)|BART]] can be seen as a [[Markov Chain Monte Carlo (MCMC)]] procedure for fitting the [[Bayesian Additive Regression Trees (BART)|BART]] model
- It can be shown that the parameters (eg the split points & perturbations) come from a specific [[Prior Distribution|prior distribution]]
	- the method is based on statistical theory
- We typically choose large values for $B$ and $K$ and a moderate value for $L$
	- eg $K=200$, $B=1,000$, and $L=100$ are reasonable choices
- [[Bayesian Additive Regression Trees (BART)|BART]] has been shown to have impressive out of the box performance
	- eg it performs well with minimal #hyperparameter tuning 
- 