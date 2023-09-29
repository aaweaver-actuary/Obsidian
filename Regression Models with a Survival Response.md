[[Survival Analysis]]

- Task is fitting a [[Regression|regression]] model to [[Survival Time|survival time]] data
- Want to predict the true [[Survival Time|survival time]] $T$
- Observed quantity $Y=\min(T,C) > 0$ and may have a long right tail, may be tempted to fit a [[Linear Regression|linear regression]] on $\log(Y)$ on $X$
    - but censored data again creates a problem
- To overcome this difficulty, we instead make use of a sequential construction, similar to the idea used for the [[Kaplan-Meier]] [[Survival Curve|survival curve]]

[[The Hazard Function]]
