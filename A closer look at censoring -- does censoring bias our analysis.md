#statistical-learning #survival-analysis 

- Suppose that a number of patients drop out of a cancer study early because they are very sick
- An analysis that does not take into consideration the *reason* these patients dropped out will likely overestimate the true average #survival-time 
- Similarly, suppose that males who are very sick are more likely to drop out than females who are very sick
	- then a comparison of male and female #survival-time's may wrongly suggest that males survive longer than females
	- $\implies$ we need to worry about a #bias due to data being #censored 
- In general we need to assume that, #conditional on the #feature's, the #event-time $T$ is #conditionally-independent of the #censoring-time $C$
	- the two examples above violate the assumption of independent censoring