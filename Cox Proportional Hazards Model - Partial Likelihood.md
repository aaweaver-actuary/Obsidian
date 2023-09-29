[[Survival Analysis]]

[[Cox Proportional Hazards Model]]

- Because the form of the #baseline-hazard is unknown[^1] we cannot simply plug $h(t|x_i)$ into the [[Likelihood|likelihood]] and then estimate $\beta = (\beta_1, \beta_2, \ldots, \beta_p)^T$ by [[Maximum likelihood is used to fit linear regression parameters|maximum likelihood]]
- The magic of the [[Cox Proportional Hazards Model]] lies in the fact that it is possible to estimate $\beta$ without having to specify the form of $h_0(t)$
- To accomplish this we make use of the same sequential-in-time logic as we used for the [[Kaplan-Meier]] survival curve[^2] and the [[The Log Rank Test|log rank]] test[^3]
    - Then the total [[The Hazard Function|hazard rate]] at failure time $y_i$ for the at-risk observations is $$
	  \sum_{y_{i' \ge y_i}} h_0(y_i)\exp\left( \sum_{j=1}^p x_{i'j}\beta_j\right) \hspace{15em}
	  $$
  - This means that the probability that the $i$th observation is the one to fail at time $y_i$[^4] is 
    $$
    \frac{\exp \left( \sum_{j=1}^p x_{ij} \beta_j \right)}{\sum_{y_{i'} \ge y} \exp \left( \sum_{j=1}^p x_{i'j}\beta_j \right)} \hspace{13em}
    $$
- Note that the the $h_0$ terms are no longer present
- This is a probability -- it has the hazard of the $i$th person on top, the total [[The Hazard Function|hazard rate]] on bottom, and all the $h_0$'s cancel out

## Partial Likelihood

- Now that we have these probabilities, we can just multiply to get the #partial-likelihood:
$$
PL(\beta) = \prod_{i:\delta_i =1} \frac{\exp \left( \sum_{j=1}^p x_{ij} \beta_j \right)}{\sum_{y_{i'} \ge y} \exp \left( \sum_{j=1}^p x_{i'j}\beta_j \right)} \hspace{10em}
$$
- this is the product of the probabilities over all of the uncensored observations
- this is valid regardless of the true value of $h_0(t)$
	- makes the model very flexible and robust

### Computation 

- Need iterative algorithms
- Get goodies:
	- #p-value's corresponding to a #null-hypothesis $H_0: \beta_j =0$ 
	- estimated #standard-error's
	- #confidence-interval's for the #coefficient's
- 


[^1]: [[The baseline hazard function is unspecified]]
[^2]: [[Kaplan-Meier]]
[^3]: [[The Log Rank Test]]
[^4]: as opposed to one of the other observations in the risk set