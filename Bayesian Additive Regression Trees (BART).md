
	
- AKA BART
- #ensemble method
- uses decision [[Tree-Based Methods|trees]] as its building block
- recall that [[Bagging|bagging]] and [[Random Forests|random forests]] make predictions from an average of [[Regression|regression]] [[Tree-Based Methods|trees]]
	- each [[Tree-Based Methods|tree]] is built using a random sample of data and/or predictors
	- each [[Tree-Based Methods|tree]] is built separately from the others
- [[Boosting]] uses a weighted sum of [[Tree-Based Methods|trees]]
	- each [[Tree-Based Methods|tree]] is constructed by fitting a new [[Tree-Based Methods|tree]] to the residual of the current fit
	- thus each new [[Tree-Based Methods|tree]] tries to capture signal that is not yet accounted for by the current set of [[Tree-Based Methods|trees]]
- [[Bayesian Additive Regression Trees (BART)|BART]] is related to both [[Random Forests|random forests]] and [[Boosting|boosting]]
	- each [[Tree-Based Methods|tree]] is constructed in a random manner as in [[Bagging|bagging]] and [[Random Forests|random forests]] 
	- each [[Tree-Based Methods|tree]] tries to capture signal not yet accounted for by the current model, as in [[Boosting|boosting]]
- the main novelty of [[Bayesian Additive Regression Trees (BART)|BART]] is the way in which new [[Tree-Based Methods|tree]] are generated
- [[Bayesian Additive Regression Trees (BART)|BART]] can be applied to [[Regression|regression]], [[Classification|classification]], as well as other problems (like [[Survival Analysis|survival analysis]])
	- we focus here on [[Regression|regression]]

# BART algorithm
- [[BART Algorithm#the idea|the idea]] 
- [[BART notation]]
- [[BART iterations]] 
- [[New BART trees are chosen by perturbations]]

# What does BART deliver?
- [[BART output|the output of BART]]
- [[Overfitting is reduced by slower learning]]
- [[BART is a Bayesian method]]


