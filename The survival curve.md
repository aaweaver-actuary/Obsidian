#statistical-learning #survival-analysis 

- The #survival-function or #survival-curve is defined as
	- $S(t) = \text{Pr}(T > t)$
- This decreasing function quantifies the probability of surviving past time $t$
- For example, if modeling #churn:
	- $T$ is the time that a customer cancels a service 
	- then $S(t)$ represents the probability that a customer cancels later than time $t$
		- the larger the value of $S(t)$, the less likely that the customer will cancel before time $t$
- 