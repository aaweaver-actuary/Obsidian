- don't go into much depth
- at each failure, compute the probability of surviving past that point
	- this includes both the [[Censored Data|censored]] data and the actual observed failures
- can then chain the survival probabilities together by just multiplying
- this overcomes the potential [[Bias|bias]] when doing [[Survival Analysis|survival analysis]] on [[Censored Data|censored]] data:[^1]
	- the censored points are included in the denominators of the survival probabilities, but they are not included as actual points on the curve
- can use [[Greenwoods Formula for Standard Error of Kaplan-Meier Curve|Greenwoods formula]] to get the [[Standard Error|standard error]]
- any study in survival analysis will start with a [[Kaplan-Meier]] curve

[^1]: [[A closer look at censoring -- does censoring bias our analysis]]