[[Survival Analysis]] [[The Hazard Function]] #baseline-hazard

[[Cox Proportional Hazards Model#^5f3048|Proportional hazards model assumption]]

- This means that we make no assumptions about the functional form of the [[Cox Proportional Hazards Model]]
- We allow the instantaneous probability of death at time $t$ given one has survived until at least time $t$ to take any form
- This means that the [[The Hazard Function|hazard function]] is very flexible, and can model a wide range of relationships between the covariates and survival time
- Our only assumption is that a one-unit increase in $x_{ij}$ corresponds to an increase in $h(t|x_i)$ by a factor of $\exp(\beta_j)$ 