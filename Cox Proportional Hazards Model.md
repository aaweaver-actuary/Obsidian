[[Survival Analysis]]

[[The Log Rank Test]]
[[Regression Models with a Survival Response]]
[[The Hazard Function]]

## The proportional hazards assumption

$$
h(t|x_i) = h_0(t)\exp\left( \sum_{j=1}^p x_{ij} \beta_j \right), \hspace{15em}
$$

^5f3048

- $h_0(t)$ - unspecified function called the #baseline-hazard
    - it is the hazard function for an individual with features $x_{i1} =\cdots=x_{ip} =0$

#### idea:

- The hazard at time $t$ is the #baseline-hazard $h_0$ times some [[Regression|regression]] quantity that is always positive (the $\exp(\cdot)$ term)

- The name ([[Cox Proportional Hazards Model]]) comes from the fact that the #hazard-function for individual $i$ is the #baseline-hazard times the #relative-risk for the feature vector $x_i=(x_{i1}, \dots, x_{ip})$, relative to that for the feature vector $x_i = (0, \dots, 0)$.

[[The baseline hazard function is unspecified]]

