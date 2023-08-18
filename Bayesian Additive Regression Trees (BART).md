## from #statistical-learning 
	
- AKA #bart
- #ensemble method
- uses decision #trees as its building block
- recall that [[Bagging|bagging]] and [[Random forests|random forests]] make predictions from an average of #regression #trees
	- each #tree is built using a random sample of data and/or predictors
	- each #tree is built separately from the others
- [[Boosting]] uses a weighted sum of #trees
	- each #tree is constructed by fitting a new #tree to the residual of the current fit
	- thus each new #tree tries to capture signal that is not yet accounted for by the current set of #trees
- #BART is related to both [[Random forests|random forests]] and [[Boosting|boosting]]
	- each #tree is constructed in a random manner as in [[Bagging|bagging]] and [[Random forests|random forests]] 
	- each #tree tries to capture signal not yet accounted for by the current model, as in [[Boosting|boosting]]
- the main novelty of #bart is the way in which new #trees are generated
- #bart can be applied to #regression , #classification, as well as other problems (like #survival-analysis)
	- we focus here on #regression

# BART algorithm
- [[BART Algorithm#the idea|the idea]] 
- [[BART notation]]
- [[BART iterations]] 
- [[New BART trees are chosen by perturbations]]

# What does BART deliver?
- [[BART output|the output of BART]]
- [[Overfitting is reduced by slower learning]]
- [[BART is a Bayesian method]]


