- the most common hypothesis test involves testing:
	* $H_0$: There is no relationship between $X$ and $Y$ $\rightarrow$ [[Null Hypothesis in Hypothesis Testing|the null hypothesis]]
        _ $H_1$: There is some relationship between $X$ and $Y$ $\rightarrow$ [[Alternative Hypothesis in Hypothesis Testing|the alternative hypothesis]]

- here $H_0$ is called the [[Null Hypothesis in Hypothesis Testing|null hypothesis]], and is the model where $\beta_1 = 0$
- $H_1$ is called the [[Alternative Hypothesis in Hypothesis Testing|alternative hypothesis]], and is the model where $\beta_1 \neq 0$
- Mathematically, this corresponds to testing:
        _ $H_0$: $\beta_1 = 0$ vs
        _ $H_1$: $\beta_1 \neq 0$
        \* this is because if $\beta_1 = 0$, then the model reduces to $Y = \beta_0 + \epsilon$, and so $X$ is not associated with $Y$
- To test $H_0$, we compute a [[t-Statistic|t-statistic]], given by

$$

t = \frac{\hat{\beta}_1 - 0}{SE(\hat{\beta}_1)}


$$

- the [[t-Statistic|t-statistic]] measures the number of [[Standard Deviation|standard deviations]] that $\hat{\beta}_1$ is away from 0
- assuming $\beta_1 = 0$, the [[t-Statistic|t-statistic]] follows a [[t-Distribution|t-distribution]] with $n-2$ [[Degrees of Freedom|degrees of freedom]]
- then use statistical software to compute the probability of observing any value equal to $|t|$ or larger
- this probability is called the [[p-Value|p-value]]