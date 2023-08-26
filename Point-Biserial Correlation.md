#binary #target #feature

- [[correlation coefficients]] used when one variable is #binary

### calculation
Let $Y = \left\{0,1\right\}$, and suppose we want to measure its #correlation with $X$. Then
$$
r_{pb}(x, y) = \frac{m_1 - m_0}{s_n}\sqrt{\frac{n_1n_0}{n^2}}
$$
	where:
	- $m_1$ is the #mean of values in $X$ where $Y=1$
	- $m_0$ is the #mean of values in $X$ where $Y=0$
	- $n_1$ is the number of data points where $Y=1$
	- $n_0$ is the number of data points where $Y=0$
	- $n=n_1+n_2$
	- $s_n$ is the #standard-deviation:
$$
s_n = \sqrt{\frac{1}{n} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2}
$$
