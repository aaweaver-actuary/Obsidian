[[Survival Analysis]]

AKA "hazard function", "hazard rate", "force of mortality"
$$
h(t) = \lim_{\Delta t \rightarrow0} \frac{\text{Pr}(t < T \le t = \Delta t | T > t)}{\Delta t}
$$
- $T$ - true [[Survival Time|survival time]]
- It is the death rate in the instant after time $t$, given survival up to that time
- The hazard function is the basis for the [[Cox Proportional Hazards Model]]