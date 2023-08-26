#statistical-learning 

- [[Survival analysis concerns a special kind of outcome variable - the time until an event occurs]]
- For example, if we have conducted a 5-year medical study in which patients have been treated for cancer
	- We want to fit a model to predict patient survival time, using features like baseline health measurements or type of treatment
		- this sounds like a regression problem
		- but there is an issue:
			- some of the patients have survived the entire 5-year study
			- such a patient's survival time is said to be #censored
- we don't want to discard this subset of surviving patients
	- the fact that they survived the entire study is valuable information
- [[Non-medical applications of survival analysis]]
- [[Survival and censoring times]]
- [[A closer look at censoring -- does censoring bias our analysis]]
- [[The survival curve]]
- [[Kaplan-Meier]]

