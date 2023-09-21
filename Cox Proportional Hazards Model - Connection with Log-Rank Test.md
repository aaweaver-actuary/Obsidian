[[Survival Analysis]]

- Suppose we have a single predictor ($p=1$) with $x_i \in \{0,1 \}$
- To test whether there is a difference between the [[Survival Time|survival times]] of the observations in the two groups, we can consider taking to approaches:
	1. Fit a [[Cox Proportional Hazards Model]] and test the [[Null Hypothesis in Hypothesis Testing|null hypothesis]] $H_0: \beta=0$[^1]
	2. Perform a #log-rank test to compare the two groups
- There are a few ways to do number 1 -- one way is a #score-test
- In the case of a single binary feature the #score-test for $H_0: \beta=0$ is [[Cox Proportional Hazards Model]] is exactly equal to the #log-rank test


[^1]: Since $p=1$, $\beta$ is a scalar