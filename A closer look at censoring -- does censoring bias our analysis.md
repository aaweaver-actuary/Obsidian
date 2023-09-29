[[Survival Analysis]]

- Suppose that a number of patients drop out of a cancer study early because they are very sick
- An analysis that does not take into consideration the *reason* these patients dropped out will likely overestimate the true average [[Survival Time|survival time]]
- Similarly, suppose that males who are very sick are more likely to drop out than females who are very sick
	- then a comparison of male and female [[Survival Time|survival times]] may wrongly suggest that males survive longer than females
	- $\implies$ we need to worry about a [[Bias|bias]] due to data being [[Censored Data|censored]]
- In general we need to assume that, #conditional on the features, the #event-time $T$ is #conditionally-independent of the [[Censoring Time|censoring time]] $C$
	- the two examples above violate the assumption of independent censoring